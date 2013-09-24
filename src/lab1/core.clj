(ns lab1.core
  (:gen-class))

(import '(java.io File)
        '(javax.imageio ImageIO)
        '(java.awt.image BufferedImage)
        '(java.util.concurrent Executors))

(defn- makeNegFilename
  "Add _neg to filename before file extension"
  [filename]
  (let [dot (.lastIndexOf filename ".")]
    (str (.substring filename 0 dot) "_neg"
         (.substring filename dot))))

(defn- getExtension
  "Get file extension"
  [filename]
  (.substring filename
              (+ 1 (.lastIndexOf filename "."))))

(defn- imageFromFile
  "Read BufferedImage from file by name"
  [filename]
  (. ImageIO read (File. filename)))

(defn- imageToFile
  "Write BufferedImage to file by name"
  [image filename]
  (. ImageIO write
     image
     (getExtension filename)
     (File. filename)))

(defn- cloneImage
  "Returne deep copy of BufferedImage"
  [image]
  (BufferedImage.
   (.getColorModel image)
   (.copyData image nil)
   (.isAlphaPremultiplied image)
   nil))

(defn- rectFunc
  "Apply function to image region by rectangle, return new image"
  [image func rect]
  (let [x (first rect)
        y (second rect)
        w (nth rect 2)
        h (nth rect 3)
        new-image (cloneImage image)]
    (.setRGB new-image
             x y w h
             (int-array
              (map func
                   (.getRGB image
                            x y w h
                            (int-array (* w h))
                            0 w)))
             0 w)
    new-image))

(defn- makeSlices
  "Return list of rectangles: x y w h"
  [width height count]
  (let [size (int (/ height count))
        bounds (range 0 height size)
        bcount (+ 1 count)
        lastElem (last bounds)]
    (map list
         (repeat bcount 0)
         (cons lastElem (butlast bounds))
         (repeat bcount width)
         (cons (- height lastElem)
               (repeat count size)))))

(defn- sliceImage
  "Return #count slices from image as rectangles"
  [image count]
  (makeSlices (.getWidth image) (.getHeight image)
            count))
  
(defn -main
  "Apply negative filter to image using #nthreads"
  [imgPath nthreads]
  (let [image (imageFromFile imgPath)
        rimage (ref image)
        nthreads (. Integer parseInt nthreads)
        
        height (.getHeight image)
        nslices (int (/ height nthreads))
        
        pool (Executors/newFixedThreadPool nthreads)
        tasks (map (fn [rect]
                     (fn []
                       (dosync (alter rimage
                                      rectFunc
                                      #(- 255 %)
                                      rect))))
                   (sliceImage image nthreads))]
    (if (< nslices 6)
      (println "Too thin slices. Use smaller number of threads.")
      (do
        (.invokeAll pool tasks)
        (.shutdown pool)
        (imageToFile (deref rimage)
                      (makeNegFilename imgPath))))))
