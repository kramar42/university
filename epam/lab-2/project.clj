(defproject lab-2 "0.1.0-SNAPSHOT"
  :description "EPAM lab 2. Produces/consumer."
  :url "https://github.com/kramar42/lab-2"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.5.1"]]
  :main ^:skip-aot lab-2.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
