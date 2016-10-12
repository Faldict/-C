<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=gb2312"/>
    <title>Sina Visitor System</title>
</head>
<body>
<span id="message"></span>
<script type="text/javascript" src="/js/visitor/mini.js"></script>
<script type="text/javascript">
    window.use_fp = "1" == "1"; // �Ƿ�ɼ��豸ָ�ơ�
    var url = url || {};
    (function () {
        this.l = function (u, c) {
            try {
                var s = document.createElement("script");
                s.type = "text/javascript";
                s[document.all ? "onreadystatechange" : "onload"] = function () {

                    if (document.all && this.readyState != "loaded" && this.readyState != "complete") {
                        return
                    }
                    this[document.all ? "onreadystatechange" : "onload"] = null;
                    this.parentNode.removeChild(this);
                    if (c) {
                        c()
                    }
                };
                s.src = u;
                document.getElementsByTagName("head")[0].appendChild(s)
            } catch (e) {
            }
        };
    }).call(url);

    // ������ڡ�
    wload(function () {

        try {

            var need_restore = "1" == "1"; // �Ƿ��߻ָ��������̡�

            // �����Ҫ�߻ָ��������̣����Դ� cookie ��ȡ�û����ݡ�
            if (!need_restore || !Store.CookieHelper.get("SRF")) {

                // ����ȡʧ���ߴ����ÿ����̡�
                // ����ִ��ʱ����������� 3s��������Ϊ������
                var error_timeout = window.setTimeout("error_back()", 3000);

                tid.get(function (tid, where, confidence) {
                    // ȡָ��˳����ɣ�������� timeout ��
                    window.clearTimeout(error_timeout);
                    incarnate(tid, where, confidence);
                });
            } else {
                // �û����ݴ��ڣ����Իָ��û����ݡ�
                restore();
            }
        } catch (e) {
            // ������
            error_back();
        }
    });

    // �����ء� �ص�������
    var return_back = function (response) {

        if (response["retcode"] == 20000000) {
            back();
        } else {
            // ������
            error_back(response["msg"]);
        }
    };

    // ��ת�س�ʼ��ַ��
    var back = function() {

        var url = "http://weibo.com/";
        if (url != "none") {
            window.location.href = url;
        }
    };

    // ����㲥��
    var cross_domain = function (response) {

        var from = "weibo";
        if (response["retcode"] == 20000000) {

            var crossdomain_host = "login.sina.com.cn";
            if (crossdomain_host != "none") {

                var cross_domain_intr = window.location.protocol + "//" + crossdomain_host + "/visitor/visitor?a=crossdomain&cb=return_back&s=" +
                        encodeURIComponent(response["data"]["sub"]) + "&sp=" + encodeURIComponent(response["data"]["subp"]) + "&from=" + from + "&_rand=" + Math.random();
                url.l(cross_domain_intr);
            } else {

                back();
            }
        } else {

            // ������
            error_back(response["msg"]);
        }
    };

    // Ϊ�û�����ÿ����� ��
    var incarnate = function (tid, where, conficence) {

        var gen_conf = "";
        var from = "weibo";
        var incarnate_intr = window.location.protocol + "//" + window.location.host + "/visitor/visitor?a=incarnate&t=" +
                encodeURIComponent(tid) + "&w=" + encodeURIComponent(where) + "&c=" + encodeURIComponent(conficence) +
                "&gc=" + encodeURIComponent(gen_conf) + "&cb=cross_domain&from=" + from + "&_rand=" + Math.random();
        url.l(incarnate_intr);
    };

    // �ָ��û���ʧ�����ݡ�
    var restore = function () {

        var from = "weibo";
        var restore_intr = window.location.protocol + "//" + window.location.host +
                "/visitor/visitor?a=restore&cb=restore_back&from=" + from + "&_rand=" + Math.random();

        url.l(restore_intr);
    };

    // ����ָ���ʧ�����ݡ�
    var restore_back = function (response) {

        // ���ݻָ��ɹ��߹㲥���̣������ߴ����ÿ����̡�
        if (response["retcode"] == 20000000) {

            var url = "http://weibo.com/";
            var alt = response["data"]["alt"];
            var savestate = response["data"]["savestate"];
            if (alt != "") {
            	requrl = (url == "none") ? "" : "&url=" + encodeURIComponent(url);
                var params = "entry=sso&alt=" + encodeURIComponent(alt) + "&returntype=META" +
                        "&gateway=1&savestate=" + encodeURIComponent(savestate) + requrl;
                window.location.href = "http://login.sina.com.cn/sso/login.php?" + params;
            } else {

                cross_domain(response);
            }
        } else {

            tid.get(function (tid, where, confidence) {
                incarnate(tid, where, confidence);
            });
        }
    };

    // ����������ص�¼ҳ��
    var error_back = function (msg) {

        var url = "http://weibo.com/";
        if (url != "none") {

            if (url.indexOf("ssovie4c55=0") === -1) {
                url += (((url.indexOf("?") === -1) ? "?" : "&") + "ssovie4c55=0");
            }
            window.location.href = "http://weibo.com/login.php";
        } else {

            if(document.getElementById("message")) {
                document.getElementById("message").innerHTML = "Error occurred" + (msg ? (": " + msg) : ".");
            }
        }
    }

</script>
</body>
</html>