PS C:\Windows\system32> docker logs 5d37f2b40c42
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: error: /etc/nginx/conf.d/default.conf differs from the packaged version
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
172.22.0.1 - - [11/Jun/2021:14:43:37 +0000] "POST /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:43:39 +0000] "GET / HTTP/1.1" 200 3487 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:43:40 +0000] "GET /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:43:54 +0000] "POST /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:19 +0000] "POST /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:31 +0000] "GET / HTTP/1.1" 200 3487 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:34 +0000] "GET /ad HTTP/1.1" 404 6012 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:37 +0000] "GET /admin/ HTTP/1.1" 302 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:37 +0000] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 1913 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:42 +0000] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0 "http://127.0.0.1/admin/login/?next=/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:42 +0000] "GET /admin/ HTTP/1.1" 200 8695 "http://127.0.0.1/admin/login/?next=/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:44 +0000] "GET /admin/auth/user/ HTTP/1.1" 200 7042 "http://127.0.0.1/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:45 +0000] "GET /admin/jsi18n/ HTTP/1.1" 200 3223 "http://127.0.0.1/admin/auth/user/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: error: /etc/nginx/conf.d/default.conf differs from the packaged version
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
172.22.0.1 - - [11/Jun/2021:15:42:22 +0000] "GET / HTTP/1.1" 200 4006 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:22 +0000] "GET /favicon.ico HTTP/1.1" 404 6039 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:24 +0000] "GET /auth/logout/?next=/ HTTP/1.1" 302 0 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:24 +0000] "GET / HTTP/1.1" 200 3487 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:25 +0000] "GET /auth/login/ HTTP/1.1" 200 3157 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:28 +0000] "GET /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/auth/login/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:39 +0000] "POST /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:47 +0000] "GET /admin/ HTTP/1.1" 302 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:47 +0000] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 1913 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:54 +0000] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0 "http://127.0.0.1/admin/login/?next=/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:54 +0000] "GET /admin/ HTTP/1.1" 200 8695 "http://127.0.0.1/admin/login/?next=/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:56 +0000] "GET /admin/auth/user/ HTTP/1.1" 200 7042 "http://127.0.0.1/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:57 +0000] "GET /admin/jsi18n/ HTTP/1.1" 200 3223 "http://127.0.0.1/admin/auth/user/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"PS C:\Windows\system32>




PS C:\Windows\system32> docker logs 5d37f2b40c42
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: error: /etc/nginx/conf.d/default.conf differs from the packaged version
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
172.22.0.1 - - [11/Jun/2021:14:43:37 +0000] "POST /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:43:39 +0000] "GET / HTTP/1.1" 200 3487 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:43:40 +0000] "GET /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:43:54 +0000] "POST /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:19 +0000] "POST /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:31 +0000] "GET / HTTP/1.1" 200 3487 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:34 +0000] "GET /ad HTTP/1.1" 404 6012 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:37 +0000] "GET /admin/ HTTP/1.1" 302 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:37 +0000] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 1913 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:42 +0000] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0 "http://127.0.0.1/admin/login/?next=/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:42 +0000] "GET /admin/ HTTP/1.1" 200 8695 "http://127.0.0.1/admin/login/?next=/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:44 +0000] "GET /admin/auth/user/ HTTP/1.1" 200 7042 "http://127.0.0.1/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:14:44:45 +0000] "GET /admin/jsi18n/ HTTP/1.1" 200 3223 "http://127.0.0.1/admin/auth/user/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: error: /etc/nginx/conf.d/default.conf differs from the packaged version4
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
172.22.0.1 - - [11/Jun/2021:15:42:22 +0000] "GET / HTTP/1.1" 200 4006 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:22 +0000] "GET /favicon.ico HTTP/1.1" 404 6039 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:24 +0000] "GET /auth/logout/?next=/ HTTP/1.1" 302 0 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:24 +0000] "GET / HTTP/1.1" 200 3487 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:25 +0000] "GET /auth/login/ HTTP/1.1" 200 3157 "http://127.0.0.1/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:28 +0000] "GET /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/auth/login/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:39 +0000] "POST /signup/ HTTP/1.1" 200 4058 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:47 +0000] "GET /admin/ HTTP/1.1" 302 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:47 +0000] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 1913 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:54 +0000] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0 "http://127.0.0.1/admin/login/?next=/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:54 +0000] "GET /admin/ HTTP/1.1" 200 8695 "http://127.0.0.1/admin/login/?next=/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:56 +0000] "GET /admin/auth/user/ HTTP/1.1" 200 7042 "http://127.0.0.1/admin/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:42:57 +0000] "GET /admin/jsi18n/ HTTP/1.1" 200 3223 "http://127.0.0.1/admin/auth/user/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:47:17 +0000] "POST /signup/ HTTP/1.1" 403 2513 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:47:26 +0000] "POST /signup/ HTTP/1.1" 403 2513 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:47:59 +0000] "POST /signup/ HTTP/1.1" 403 2513 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:48:01 +0000] "GET /signup/ HTTP/1.1" 200 4456 "http://127.0.0.1/auth/login/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:48:09 +0000] "POST /signup/ HTTP/1.1" 200 4456 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"
172.22.0.1 - - [11/Jun/2021:15:48:11 +0000] "POST /signup/ HTTP/1.1" 200 4456 "http://127.0.0.1/signup/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36" "-"