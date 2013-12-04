(ns lab-2.core
  (:gen-class))
(load "bin")

; Using this thread as example
; http://stackoverflow.com/questions/2760017/producer-consumer-with-qualifications

(def go-on? (atom true))
(def queue (java.util.concurrent.LinkedBlockingQueue.))
(def output (ref ()))
(def data nil)
(def filepath "resources/data.bin")

(defn- genTask [usernum relationnum votesnum maxvotes]
  (flatten
    (list
      usernum
      relationnum
      votesnum
      (repeatedly relationnum #(list
                             (rand-int usernum)
                             (rand-int usernum)))
      (repeatedly votesnum #(list
                              (rand-int usernum)
                              (rand-int maxvotes))))))

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

(defn- producer []
  (future
    (while @go-on?
      (let [next (first data)]
        (.put queue next)
        (Thread/sleep (rand-int 200))))))

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
  (writeBin (genTask 10 10 10 10) filepath)
  (def data (processBinData (readBin filepath)))
  (dorun (repeatedly 10 producer))
  (dorun (repeatedly 10 consumer))
  (halt)
  (println (deref output)))

