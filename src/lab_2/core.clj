(ns lab-2.core
  (:gen-class))

(import '(java.io DataInputStream)
        '(java.io FileInputStream)
        '(java.io DataOutputStream)
        '(java.io FileOutputStream))

; Using this thread as example
; http://stackoverflow.com/questions/2760017/producer-consumer-with-qualifications

(def go-on? (atom true))
(def queue (java.util.concurrent.LinkedBlockingQueue.))
(def output (ref ()))

; swap!
; Atomically swaps the value of atom to be
(defn- halt
  ([] (halt 2000))
  ([timeout]
      (Thread/sleep timeout)
      (swap! go-on? not)))

; future
; Takes a body of expressions and yields a future object that will
; invoke the body in another thread, and will cache the result and
; return it on all subsequent calls to deref/@.

(defn- producer [vote]
  (future
    (while @go-on?
      (.put queue vote)
      (Thread/sleep (rand-int 200)))))

(defn- consumer []
  (future
    (while @go-on?
      (when-let [item (.poll queue)]
        (Thread/sleep (rand-int 200))
        (dosync (alter output conj item))))))

; reset!
; Sets the value of atom to newval without regard for the
; current value. Returns newval.

(defn -main
  [& args]
  (reset! go-on? true)
  (dorun (map #(%1 %2)
              (repeat 5 producer)
              (iterate inc 0)))
  (dorun (repeatedly 2 consumer))
  (halt)
  output)

(defn- readBin [filename]
  (let
    [filestream (FileInputStream. filename)
     stream (DataInputStream. filestream)

     usernum (. stream readInt)
     relations (. stream readInt)
     votings (. stream readInt)
     users (repeatedly relations #(list (. stream readInt)
                                        (. stream readInt)))
     votes (repeatedly votings #(list (. stream readInt)
                                      (. stream readInt)))]
    (flatten
      (list
        usernum
        relations
        votings
        users
        votes))))

(defn- writeBin [bytes filename]
  (let [filestream (FileOutputStream. filename)
        stream (DataOutputStream. filestream)]
    (dorun (map #(. stream writeInt %) bytes))))

(defn- genTask [usernum relations votings maxvotes]
  (flatten
    (list
      usernum
      relations
      votings
      (repeatedly relations #(list
                             (rand-int usernum)
                             (rand-int usernum)))
      (repeatedly votings #(list
                             (rand-int usernum)
                             (rand-int maxvotes))))))

