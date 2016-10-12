
<!DOCTYPE html>
<!--[if IE 6]><html class="ie lt-ie8"><![endif]-->
<!--[if IE 7]><html class="ie lt-ie8"><![endif]-->
<!--[if IE 8]><html class="ie ie8"><![endif]-->
<!--[if IE 9]><html class="ie ie9"><![endif]-->
<!--[if !IE]><!--> <html> <!--<![endif]-->

  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=Edge">
<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"1255494d3a","applicationID":"15702971","transactionName":"e1daR0JWVV9RER9fWlVdG1peXVxL","queueTime":17,"applicationTime":24,"agent":""}</script>
<script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o||e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(t,e,n){function r(){}function o(t,e,n){return function(){return i(t,[(new Date).getTime()].concat(u(arguments)),e?null:this,n),e?void 0:this}}var i=t("handle"),a=t(2),u=t(3),c=t("ee").get("tracer"),f=NREUM;"undefined"==typeof window.newrelic&&(newrelic=f);var s=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit"],p="api-",l=p+"ixn-";a(s,function(t,e){f[e]=o(p+e,!0,"api")}),f.addPageAction=o(p+"addPageAction",!0),e.exports=newrelic,f.interaction=function(){return(new r).get()};var d=r.prototype={createTracer:function(t,e){var n={},r=this,o="function"==typeof e;return i(l+"tracer",[Date.now(),t,n],r),function(){if(c.emit((o?"":"no-")+"fn-start",[Date.now(),r,o],n),o)try{return e.apply(this,arguments)}finally{c.emit("fn-end",[Date.now()],n)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){d[e]=o(l+e)}),newrelic.noticeError=function(t){"string"==typeof t&&(t=new Error(t)),i("err",[t,(new Date).getTime()])}},{}],2:[function(t,e,n){function r(t,e){var n=[],r="",i=0;for(r in t)o.call(t,r)&&(n[i]=e(r,t[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],3:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(o<0?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=r},{}],ee:[function(t,e,n){function r(){}function o(t){function e(t){return t&&t instanceof r?t:t?u(t,a,i):i()}function n(n,r,o){t&&t(n,r,o);for(var i=e(o),a=l(n),u=a.length,c=0;c<u;c++)a[c].apply(i,r);var s=f[m[n]];return s&&s.push([w,n,r,i]),i}function p(t,e){g[t]=l(t).concat(e)}function l(t){return g[t]||[]}function d(t){return s[t]=s[t]||o(n)}function v(t,e){c(t,function(t,n){e=e||"feature",m[n]=e,e in f||(f[e]=[])})}var g={},m={},w={on:p,emit:n,get:d,listeners:l,context:e,buffer:v};return w}function i(){return new r}var a="nr@context",u=t("gos"),c=t(2),f={},s={},p=e.exports=o();p.backlog=f},{}],gos:[function(t,e,n){function r(t,e,n){if(o.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[e]=r,r}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){o.buffer([t],r),o.emit(t,e,n)}var o=t("ee").get("handle");e.exports=r,r.ee=o},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!h++){var t=y.info=NREUM.info,e=s.getElementsByTagName("script")[0];if(t&&t.licenseKey&&t.applicationID&&e){c(m,function(e,n){t[e]||(t[e]=n)});var n="https"===g.split(":")[0]||t.sslForHttp;y.proto=n?"https://":"http://",u("mark",["onload",a()],null,"api");var r=s.createElement("script");r.src=y.proto+t.agent,e.parentNode.insertBefore(r,e)}}}function o(){"complete"===s.readyState&&i()}function i(){u("mark",["domContent",a()],null,"api")}function a(){return(new Date).getTime()}var u=t("handle"),c=t(2),f=window,s=f.document,p="addEventListener",l="attachEvent",d=f.XMLHttpRequest,v=d&&d.prototype;NREUM.o={ST:setTimeout,CT:clearTimeout,XHR:d,REQ:f.Request,EV:f.Event,PR:f.Promise,MO:f.MutationObserver},t(1);var g=""+location,m={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-974.min.js"},w=d&&v&&v[p]&&!/CriOS/.test(navigator.userAgent),y=e.exports={offset:a(),origin:g,features:{},xhrWrappable:w};s[p]?(s[p]("DOMContentLoaded",i,!1),f[p]("load",r,!1)):(s[l]("onreadystatechange",o),f[l]("onload",r)),u("mark",["firstbyte",a()],null,"api");var h=0},{}]},{},["loader"]);</script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0,user-scalable=no">
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta property="wb:webmaster" content="294ec9de89e7fadb" />
  <meta property="qc:admins" content="104102651453316562112116375" />
  <meta property="qc:admins" content="11635613706305617" />
  <meta property="qc:admins" content="1163561616621163056375" />
  <meta name="google-site-verification" content="cV4-qkUJZR6gmFeajx_UyPe47GW9vY6cnCrYtCHYNh4" />
  <meta name="google-site-verification" content="HF7lfF8YEGs1qtCE-kPml8Z469e2RHhGajy6JPVy5XI" />
  <meta http-equiv="mobile-agent" content="format=html5; url=http://localhost/">
  
  <title>首页 - 简书</title>
  <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="XVrFkGSBFH0E3/tTskioAcVxjDDHgNS4uPDdMXOR8iOnf056Cs0ZCWgOOiMbqzEWs0EXjB73akcJeYuRf8KQPA==" />
  <!--[if lte IE 8]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
  <link rel="stylesheet" media="all" href="http://cdn-qn0.jianshu.io/assets/base-fcbb465e0d570eff94222aef0113921f.css" />

    <link rel="stylesheet" media="all" href="http://cdn-qn0.jianshu.io/assets/reading-d4bf6a5970a6bc204c9ac8222b651adb.css" />
  <link rel="stylesheet" media="all" href="http://cdn-qn0.jianshu.io/assets/base-read-mode-9b4a364d3a94a577397974de707192a5.css" />
  <script src="http://cdn-qn0.jianshu.io/assets/modernizr-613ea63b5aa2f0e2a1946e9c28c8eedb.js"></script>
  <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
  <!--[if IE 8]><link rel="stylesheet" media="all" href="http://cdn-qn0.jianshu.io/assets/scaffolding/for_ie-7f1c477ffedc13c11315103e8787dc6c.css" /><![endif]-->
  <!--[if lt IE 9]><link rel="stylesheet" media="all" href="http://cdn-qn0.jianshu.io/assets/scaffolding/for_ie-7f1c477ffedc13c11315103e8787dc6c.css" /><![endif]-->
  <link href="http://baijii-common.b0.upaiyun.com/icons/favicon.ico" rel="icon">
      <link rel="apple-touch-icon-precomposed" href="http://cdn-qn0.jianshu.io/assets/apple-touch-icons/57-b426758a1fcfb30486f20fd073c3b8ec.png" sizes="57x57" />
      <link rel="apple-touch-icon-precomposed" href="http://cdn-qn0.jianshu.io/assets/apple-touch-icons/72-feca4b183b9d29fd188665785dc7a7f1.png" sizes="72x72" />
      <link rel="apple-touch-icon-precomposed" href="http://cdn-qn0.jianshu.io/assets/apple-touch-icons/76-ba757f1ad3421192ce7192170393d2b0.png" sizes="76x76" />
      <link rel="apple-touch-icon-precomposed" href="http://cdn-qn0.jianshu.io/assets/apple-touch-icons/114-8dae53b3bcea3f06bb139e329d1edab3.png" sizes="114x114" />
      <link rel="apple-touch-icon-precomposed" href="http://cdn-qn0.jianshu.io/assets/apple-touch-icons/120-fa315ee0177dba4c55d4f66d4129b47f.png" sizes="120x120" />
      <link rel="apple-touch-icon-precomposed" href="http://cdn-qn0.jianshu.io/assets/apple-touch-icons/152-052f5799bec8fb3aa624bdc72ef5bd1d.png" sizes="152x152" />

</head>

  <body class="output fluid zh cn reader-day-mode reader-font2" data-js-module="recommendation" data-locale="zh-CN">
    
    <div class="navbar navbar-jianshu shrink">
  <div class="dropdown">
    <a class="dropdown-toggle logo" id="dLabel" role="button" data-toggle="dropdown" data-target="#" href="javascript:void(0)">
      简
    </a>
    <ul class="dropdown-menu" role="menu" aria-labelledby="dLabel">
      <li><a href="/"><i class="fa fa-home"></i> 首页</a></li>
      <li><a href="/collections"><i class="fa fa-th"></i> 专题</a></li>
    </ul>
  </div>
</div>
<div class="navbar-user">
    <a class="login" data-signup-link="true" data-toggle="modal" href="/sign_up">
      <i class="fa fa-user"></i> 注册
</a>    <a class="login" data-signin-link="true" data-toggle="modal" href="/sign_in">
      <i class="fa fa-sign-in"></i> 登录
</a>    <a class="daytime set-view-mode pull-right" href="javascript:void(0)"><i class="fa fa-moon-o"></i></a>
</div>
<div class="navbar navbar-jianshu expanded">
  <div class="dropdown">
      <a class="active logo" role="button" data-original-title="个人主页" data-container="div.expanded" href="/">
        <b>简</b><i class="fa fa-home"></i><span class="title">首页</span>
</a>      <a data-toggle="tooltip" data-placement="right" data-original-title="专题" data-container="div.expanded" href="/collections">
        <i class="fa fa-th"></i><span class="title">专题</span>
</a>    <a class="ad-selector" href="/apps">
      <i class="fa fa-mobile"></i><span class="title">下载手机应用</span>
</a>    <div class="ad-container ">
      <div class="ad-pop">
        <img class="ad-logo" src="http://cdn-qn0.jianshu.io/assets/apple-touch-icons/114-8dae53b3bcea3f06bb139e329d1edab3.png" alt="114" />
        <p class="ad-title">简书</p>
        <p class="ad-subtitle">交流故事，沟通想法</p>
        <img class="ad-qrcode" src="http://cdn-qn0.jianshu.io/assets/app-page/download-app-qrcode-053849fa25f9b44573ef8dd3c118a20f.png" alt="Download app qrcode" />
        <div>
          <a class="ad-link" href="https://itunes.apple.com/cn/app/jian-shu/id888237539?ls=1&amp;mt=8">iOS</a>·
          <a class="ad-link" href="http://downloads.jianshu.io/apps/haruki/JianShu-1.11.2.apk">Android</a>
        </div>
      </div>
    </div>
  </div>
  <div class="nav-user">
      <a href='#view-mode-modal' data-toggle='modal'><i class="fa fa-font"></i><span class="title">显示模式</span></a>

      <a class="signin" data-signin-link="true" data-toggle="modal" data-placement="right" data-original-title="登录" data-container="div.expanded" href="/sign_in">
        <i class="fa fa-sign-in"></i><span class="title">登录</span>
</a>    </div>
  </div>

    
    <div class="row-fluid">
      
  <div class="recommended">
    <!-- aside -->
      <div class="span3 left-aside">
    <div class="cover-img" style="background-image: url(http://upload.jianshu.io/daily_images/images/PqYBgcpAscjTgM1xgwQs.jpg)"></div>
    <div class="bottom-block">
      
      <h1>简书</h1>
      <h3>交流故事，沟通想法</h3>
      <p>一个基于内容分享的社区</p>
      <a class="btn btn btn-large btn-success" id="write-button" data-signin-link="true" data-toggle="modal" href="/sign_in">提笔写篇文章</a>

    </div>
      <div class="img-info">
        <i class="fa fa-info"></i>
        <div class="info">
           Photo by <a target="_blank" href="https://www.flickr.com/photos/barroomuniverse">barroomuniverse</a>
        </div>
      </div>
  </div>

    <div class="span7 offset3">
      <div class="page-title">
        <ul class="recommened-nav navigation clearfix" data-container='#list-container' data-loader='.loader-tiny'
           data-user-slug=>
            <!-- 未登录状态 -->
            <!-- Active: recommended notes list -->
            <li class="active">
              <a data-pjax="true" href="/trending/now">发现</a>
            </li>
            <li class="bonus">
              <a href="/zodiac/2015"><i class="fa fa-bars"></i> 2015精选</a>
            </li>
          <img class="hide loader-tiny" src="http://baijii-common.b0.upaiyun.com/loaders/tiny.gif" alt="Tiny" />
          <li class="search">
            <form class="search-form" target="_blank" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  <input type="search" name="q" id="q" placeholder="搜索" class="input-medium search-query" />
  <span class="search_trigger" onclick="$('form.search-form').submit();"><i class="fa fa-search"></i></span>
</form>
          </li>
        </ul>
      </div>
      <div id="list-container">
        

  <ul class="unstyled clearfix sort-nav" id="collection-categories-nav" data-js-module="collection-category" data-fetch-url="/recommendations/notes">
      <li class=active><a class="category" data-dimension="now" href="javascript:void(null);">热门</a></li>
      <li ><a class="category" data-category-id="64" href="javascript:void(null);">时事热闻</a></li>
      <li ><a class="category" data-category-id="66" href="javascript:void(null);">小说精选</a></li>
      <li ><a class="category" data-category-id="70" href="javascript:void(null);">摄影游记</a></li>
      <li ><a class="category" data-category-id="68" href="javascript:void(null);">漫画手绘</a></li>
      <li ><a class="category" data-category-id="67" href="javascript:void(null);">签约作者</a></li>
      <li ><a class="category" data-category-id="56" href="javascript:void(null);">新上榜</a></li>
      <li ><a class="category" data-dimension="weekly" href="javascript:void(null);">七日热门</a></li>
      <li ><a class="category" data-dimension="monthly" href="javascript:void(null);">三十日热门</a></li>
      <li ><a class="category" data-category-id="60" href="javascript:void(null);">日报</a></li>
      <li ><a class="category" data-category-id="65" href="javascript:void(null);">专题精选</a></li>
      <li ><a class="category" data-category-id="61" href="javascript:void(null);">有奖活动</a></li>
      <li ><a class="category" data-category-id="62" href="javascript:void(null);">简书出版</a></li>
      <li ><a class="category" data-category-id="63" href="javascript:void(null);">简书播客</a></li>
    <li><img class="hide loader-tiny" src="http://baijii-common.b0.upaiyun.com/loaders/tiny.gif" alt="Tiny" /></li>
  </ul>


<ul class="article-list thumbnails">
  
  <li class=have-img>
      <a class="wrap-img" href="/p/4463c1b659a6"><img src="http://upload-images.jianshu.io/upload_images/2954983-d72ddb79f28068e3.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/6d2e8e20ad9f">语不惜</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T15:01:29+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/4463c1b659a6">张靓颖：世界欠你们家一枚奥斯卡金奖</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/4463c1b659a6">
          阅读 17167
</a>        <a target="_blank" href="/p/4463c1b659a6#comments">
           · 评论 193
</a>        <span> · 喜欢 87</span>
          <span> · 打赏 3</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/ebe8f9e31389"><img src="http://upload-images.jianshu.io/upload_images/2288859-c5990748a6e9a310.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/3a5c7f0d3cd2">蜗流儿</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T18:26:08+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/ebe8f9e31389">高情商的人丨教你如何缓解尴尬的10个栗子，确实高明！</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/ebe8f9e31389">
          阅读 3761
</a>        <a target="_blank" href="/p/ebe8f9e31389#comments">
           · 评论 35
</a>        <span> · 喜欢 120</span>
          <span> · 打赏 1</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/7a345c8c174a"><img src="http://upload-images.jianshu.io/upload_images/3142177-555f78ba7451ee51.png?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/19a3688fd3dc">echokanmei</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-11T22:07:30+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/7a345c8c174a">工作中文字回复，尽量减少“你”和“我”字眼的出现，会让沟通更有温度</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/7a345c8c174a">
          阅读 3574
</a>        <a target="_blank" href="/p/7a345c8c174a#comments">
           · 评论 53
</a>        <span> · 喜欢 86</span>
          <span> · 打赏 3</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/386485579d31"><img src="http://upload-images.jianshu.io/upload_images/568470-b2597284fc5742d5.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/d9edcb44e2f2">简书日报</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T17:47:23+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/386485579d31">简书晚报161012——《张靓颖：世界欠你们家一枚奥斯卡金奖》</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/386485579d31">
          阅读 14094
</a>        <a target="_blank" href="/p/386485579d31#comments">
           · 评论 9
</a>        <span> · 喜欢 50</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/72d02821a23a"><img src="http://upload-images.jianshu.io/upload_images/195046-c00319e74e654d9a.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/1441f4ae075d">彭小六</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T17:32:41+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/72d02821a23a">这3项能力，让你成为一个知识“手艺人”</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/72d02821a23a">
          阅读 8262
</a>        <a target="_blank" href="/p/72d02821a23a#comments">
           · 评论 83
</a>        <span> · 喜欢 334</span>
          <span> · 打赏 3</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/53ce3c6694e0"><img src="http://upload-images.jianshu.io/upload_images/2993841-db644a7574ee1a46.png?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/c297c06d4a50">乱刀</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T18:38:54+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/53ce3c6694e0">PPT系列教程——封面篇一</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/53ce3c6694e0">
          阅读 614
</a>        <a target="_blank" href="/p/53ce3c6694e0#comments">
           · 评论 41
</a>        <span> · 喜欢 46</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/04ffb2e9cbe4"><img src="http://upload-images.jianshu.io/upload_images/3270795-34ff1ff6b20c0d7e.JPG?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/51b0fd079c28">瘦身达人卞万合</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T13:32:34+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/04ffb2e9cbe4">爆照啦：2011~2016/我从210斤瘦到135：我把青春写给你听</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/04ffb2e9cbe4">
          阅读 5026
</a>        <a target="_blank" href="/p/04ffb2e9cbe4#comments">
           · 评论 202
</a>        <span> · 喜欢 100</span>
          <span> · 打赏 13</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/07f5bcaf281e"><img src="http://upload-images.jianshu.io/upload_images/1537594-f751a07edec3263a.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/bfe4c3547845">十三夜</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T20:26:29+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/07f5bcaf281e">别让未来平庸的你，痛恨现在还未拼尽全力的自己</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/07f5bcaf281e">
          阅读 917
</a>        <a target="_blank" href="/p/07f5bcaf281e#comments">
           · 评论 3
</a>        <span> · 喜欢 33</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/d1217b0e6066"><img src="http://upload-images.jianshu.io/upload_images/1466850-31a7196dbcdc739f.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/54f558825984">李静于</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T09:14:48+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/d1217b0e6066">何必用最大的恶意去揣测一个人的心意</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/d1217b0e6066">
          阅读 1094
</a>        <a target="_blank" href="/p/d1217b0e6066#comments">
           · 评论 30
</a>        <span> · 喜欢 29</span>
          <span> · 打赏 1</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/325d2621355d"><img src="http://upload-images.jianshu.io/upload_images/259-df66839afab2296b.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/yZq3ZV">简书</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-09-23T17:07:00+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/325d2621355d">给简书找BUG赢好礼——简书Android 1.11.3公测</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/325d2621355d">
          阅读 9729
</a>        <a target="_blank" href="/p/325d2621355d#comments">
           · 评论 195
</a>        <span> · 喜欢 62</span>
          <span> · 打赏 1</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/f4bc96e5cf32"><img src="http://upload-images.jianshu.io/upload_images/2311396-285fc0859c383a18.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/51cd6fc40769">小熊样</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T11:09:03+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/f4bc96e5cf32">33本适合设计师看的好书 别说你一本没看过！</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/f4bc96e5cf32">
          阅读 4451
</a>        <a target="_blank" href="/p/f4bc96e5cf32#comments">
           · 评论 26
</a>        <span> · 喜欢 333</span>
        
      </div>
    </div>
  </li>

  <li >
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/cd73ae789321">简书活动精选</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T19:48:12+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/ea7725ad9004">Heresay | 想知道手速党的最高极限</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/ea7725ad9004">
          阅读 436
</a>        <a target="_blank" href="/p/ea7725ad9004#comments">
           · 评论 14
</a>        <span> · 喜欢 4</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/b1a1711b00d1"><img src="http://upload-images.jianshu.io/upload_images/2499352-8405c83d32a0b8b8.png?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/3f09afc4db6e">莫小南</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-11T19:36:02+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/b1a1711b00d1">久坐电脑前，眼睛干涩、颈椎疼、偏头痛纷纷来袭，小南有妙招。</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/b1a1711b00d1">
          阅读 3560
</a>        <a target="_blank" href="/p/b1a1711b00d1#comments">
           · 评论 41
</a>        <span> · 喜欢 192</span>
          <span> · 打赏 1</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/ba9fbe62655b"><img src="http://upload-images.jianshu.io/upload_images/2102090-c3f6aeecc0230cc1.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/1089b7cfd6a9">少女陆sunny</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-11T18:31:58+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/ba9fbe62655b">大叔爱萝莉，鲜肉爱熟女，人间好循环</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/ba9fbe62655b">
          阅读 2401
</a>        <a target="_blank" href="/p/ba9fbe62655b#comments">
           · 评论 20
</a>        <span> · 喜欢 75</span>
          <span> · 打赏 1</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/b023ae663d2e"><img src="http://upload-images.jianshu.io/upload_images/424183-4dd9b57ddbeb2099?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/597283c5668c">小小小小的鱼</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T08:36:01+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/b023ae663d2e">夏冬：我的意中人，他是个盖世英雄。</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/b023ae663d2e">
          阅读 1651
</a>        <a target="_blank" href="/p/b023ae663d2e#comments">
           · 评论 12
</a>        <span> · 喜欢 41</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/f0820054f68b"><img src="http://upload-images.jianshu.io/upload_images/3093198-c41024c8ce448ed8.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/6c7bd8324013">英语Mango姐</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T16:04:13+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/f0820054f68b">英语口语达人是如何看美剧学英语的</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/f0820054f68b">
          阅读 621
</a>        <a target="_blank" href="/p/f0820054f68b#comments">
           · 评论 2
</a>        <span> · 喜欢 35</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/725b4d1c9f06"><img src="http://upload-images.jianshu.io/upload_images/1669869-d62dbf0afdba433c.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/c1fed915ed12">顾一宸</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T10:06:07+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/725b4d1c9f06">从你的全世界路过：你爱得那么傻，我好想为你哭啊</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/725b4d1c9f06">
          阅读 16764
</a>        <a target="_blank" href="/p/725b4d1c9f06#comments">
           · 评论 445
</a>        <span> · 喜欢 624</span>
          <span> · 打赏 2</span>
        
      </div>
    </div>
  </li>

  <li >
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/3e2efc2e9191">为底迟</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T15:15:55+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/49841d683fc5">做不了你的新娘，就当一辈子哥们吧</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/49841d683fc5">
          阅读 3058
</a>        <a target="_blank" href="/p/49841d683fc5#comments">
           · 评论 44
</a>        <span> · 喜欢 106</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/54fc392c75ae"><img src="http://upload-images.jianshu.io/upload_images/2700910-3a9e70fae0d22fe4.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/fb4f9f27f3f9">沈小四</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-12T17:09:41+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/54fc392c75ae">温州民房倒塌事故：何必忙于感动，冷落真相！</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/54fc392c75ae">
          阅读 1159
</a>        <a target="_blank" href="/p/54fc392c75ae#comments">
           · 评论 34
</a>        <span> · 喜欢 38</span>
          <span> · 打赏 1</span>
        
      </div>
    </div>
  </li>

  <li class=have-img>
      <a class="wrap-img" href="/p/c8bf5949373a"><img src="http://upload-images.jianshu.io/upload_images/1835526-29c91a61f1d77bc3.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/55b597320c4e">简书出版</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-10-10T12:11:57+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/c8bf5949373a">无戒《大山里女人的三生三世》上线</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/c8bf5949373a">
          阅读 4995
</a>        <a target="_blank" href="/p/c8bf5949373a#comments">
           · 评论 95
</a>        <span> · 喜欢 95</span>
          <span> · 打赏 5</span>
        
      </div>
    </div>
  </li>

</ul>

  <div class="load-more"><button class="ladda-button "
  data-style="slide-left"
  data-type="script"
  data-remote
  data-size="medium"
  data-url="/top/daily?note_ids%5B%5D=6282099&note_ids%5B%5D=6287470&note_ids%5B%5D=6270798&note_ids%5B%5D=6286595&note_ids%5B%5D=6281284&note_ids%5B%5D=6287508&note_ids%5B%5D=6277451&note_ids%5B%5D=6289496&note_ids%5B%5D=6273480&note_ids%5B%5D=5948743&note_ids%5B%5D=6278768&note_ids%5B%5D=6193462&note_ids%5B%5D=6265319&note_ids%5B%5D=6204188&note_ids%5B%5D=6275734&note_ids%5B%5D=6284405&note_ids%5B%5D=6277299&note_ids%5B%5D=6283496&note_ids%5B%5D=6285945&note_ids%5B%5D=6237820&page=2"
  data-color="maleskine"
  data-method="get">
  <span class="ladda-label">点击查看更多</span>
</button></div>

      </div>
    </div>
  </div>

  <div id="time-machine-modal"
       class="modal hide fade share-weixin-modal time-machine-modal"
       tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" data-stats2015-url="http://localhost/stats2015">

    <div class="modal-header">
      <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
    </div>
  </div>

    </div>
    <footer>
  <div class="footer-l">
    <p>
      <a href="http://www.jianshu.com/collection/jppzD2" target="_blank">关于简书</a> |
      <a target="_blank" href="/contact">联系我们</a> |
      <a href="http://www.jianshu.com/collection/fc488cd78374" target="_blank">作者成书计划</a> |
      <a href="http://www.jianshu.com/notebooks/547/latest" target="_blank">帮助中心</a> |
      <a href="http://jianshucom.taobao.com/" target="_blank">简书周边</a> |
      <a href="http://www.jianshu.com/p/cabc8fa39830">合作伙伴</a> |
    </p>
    <p>©2012-2016 <a href="/" target="_blank">简书</a> / 沪ICP备11018329号-5 /<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31010602000064"><img style="width: 18px; height: 18px" src="http://cdn-qn0.jianshu.io/assets/beianbgs-8077429238867bbe0d8c66a2a3c298af.png" alt="Beianbgs" /> 沪公网安备31010602000064号</a> <a key ="549264633b05a3da0fbd5c99" logo_size="83x30" logo_type="realname" href="http://www.anquan.org"><script src="http://static.anquan.org/static/outer/js/aq_auth.js"></script></a></p>
  </div>

  <div class="footer-r pull-right">
    <div class="app-download-btn">
      <a href="/apps">
        <img src="http://cdn-qn0.jianshu.io/assets/app-page/ios-bf05821ad054ccfb594fcc43a92a3753.png" alt="Ios" />
</a>      <a href="/apps">
        <img src="http://cdn-qn0.jianshu.io/assets/app-page/android-63f9ad04e8805deae8d8e93ee45c5a2d.png" alt="Android" />
</a>    </div>
    <div>
      关注我们:
      <a href="http://weibo.com/jianshuio" target="_blank">
        <i class="fa fa-weibo"></i>
      </a>
      <a class="weixin" href="#share-weixin-modal" data-toggle="modal">
        <i class="fa fa-weixin"></i>
      </a>
      <a href="https://twitter.com/jianshucom" target="_blank">
        <i class="fa fa-twitter"></i>
      </a>
      <br><a href="http://windows.microsoft.com/zh-CN/internet-explorer/download-ie" class="upgrade-ie">本网站不支持 IE6/IE7，如果您希望继续使用 IE 浏览器，请升级至IE8及以上版本</a>
    </div>
  </div>

  <!--modal-->
  <div class="modal hide fade share-weixin-modal" id="share-weixin-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
      </div>
      <div class="modal-content">
        <div class="modal-body">
          <p>关注我们的微信公众号，获得每日好文推荐。微信中搜索「简书」或者扫一扫下方二维码：</p>
          <img src="http://baijii-common.b0.upaiyun.com/logos/jianshu_wechat_qrcode.jpg" alt="Jianshu wechat qrcode" />
        </div>
      </div>
    </div>
  </div>

</footer>

    <div id="flash" class="hide"></div>
    
  <div id="view-mode-modal" tabindex="-1" class="modal hide read-modal" aria-hidden="false" data-js-module='view-mode-modal'>
    <div class="btn-group change-background" data-toggle="buttons-radio">
      <a class="btn btn-daytime active" data-mode="day" href="javascript:void(null);">
        <i class="fa fa-sun-o"></i>
</a>      <a class="btn btn-nighttime " data-mode="night" href="javascript:void(null);">
        <i class="fa fa-moon-o"></i>
</a>    </div>
    <div class="btn-group change-font" data-toggle="buttons-radio">
      <a class="btn font " data-font="font1" href="javascript:void(null);">宋体</a>
      <a class="btn font hei active" data-font="font2" href="javascript:void(null);">黑体</a>
    </div>
    <div class="btn-group change-locale" data-toggle="buttons-radio">
      <a class="btn font active" data-locale="zh-CN" href="javascript:void(null);">简</a>
      <a class="btn font hei " data-locale="zh-TW" href="javascript:void(null);">繁</a>
    </div>
  </div>

    <!-- Javascripts
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://cdn-qn0.jianshu.io/assets/base-ded41764c207f7ff545c28c670922d25.js"></script>
    
    <script src="http://cdn-qn0.jianshu.io/assets/reading-base-0028299ec0c770293c0f07e2f338b48f.js"></script>
      <script src="http://cdn-qn0.jianshu.io/assets/reading/module_sets/home-8a7011753fe744d1ec1a3b7af35d9590.js"></script>
  

    <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-35169517-1', 'auto');
  ga('send', 'pageview');
</script>

<div style="display:none">
  <script src="https://s11.cnzz.com/z_stat.php?id=1258679142&web_id=1258679142" language="JavaScript"></script>
</div>

<script>
  (function(){
      var bp = document.createElement('script');
      var curProtocol = window.location.protocol.split(':')[0];
      if (curProtocol === 'https') {
          bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
      }
      else {
          bp.src = 'http://push.zhanzhang.baidu.com/push.js';
      }
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(bp, s);
  })();
</script>

  </body>
</html>
