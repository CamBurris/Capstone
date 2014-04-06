/* skelJS v0.4.7 | (c) n33 | skeljs.org | MIT licensed */
var skel = function () {
    var a = {
        config: {
            prefix: null,
            preloadStyleSheets: !1,
            pollOnce: !1,
            resetCSS: !1,
            normalizeCSS: !1,
            boxModel: null,
            useOrientation: !1,
            useRTL: !1,
            pollOnLock: !1,
            usePerpetualLock: !0,
            useDomainLock: !0,
            containers: 960,
            grid: {
                collapse: !1,
                gutters: 40
            },
            breakpoints: {
                all: {
                    range: "*",
                    hasStyleSheet: !1
                }
            },
            events: {}
        },
        isConfigured: !1,
        isInit: !1,
        lockState: null,
        stateId: "",
        me: null,
        breakpoints: [],
        breakpointList: [],
        events: [],
        plugins: {},
        cache: {
            elements: {},
            states: {}
        },
        locations: {
            html: null,
            head: null,
            body: null
        },
        vars: {},
        lsc: "_skel_lock",
        sd: " ",
        css: {
            r: "html,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,menu,nav,output,ruby,section,summary,time,mark,audio,video{margin:0;padding:0;border:0;font-size:100%;font:inherit;vertical-align:baseline}article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section{display:block}body{line-height:1}ol,ul{list-style:none}blockquote,q{quotes:none}blockquote:before,blockquote:after,q:before,q:after{content:'';content:none}table{border-collapse:collapse;border-spacing:0}body{-webkit-text-size-adjust:none}",
            n: 'article,aside,details,figcaption,figure,footer,header,hgroup,main,nav,section,summary{display:block}audio,canvas,video{display:inline-block}audio:not([controls]){display:none;height:0}[hidden]{display:none}html{background:#fff;color:#000;font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}a:focus{outline:thin dotted}a:active,a:hover{outline:0}h1{font-size:2em;margin:.67em 0}abbr[title]{border-bottom:1px dotted}b,strong{font-weight:bold}dfn{font-style:italic}hr{-moz-box-sizing:content-box;box-sizing:content-box;height:0}mark{background:#ff0;color:#000}code,kbd,pre,samp{font-family:monospace,serif;font-size:1em}pre{white-space:pre-wrap}q{quotes:"\u0081C" "\u0081D" "\u00818" "\u00819"}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-0.5em}sub{bottom:-0.25em}img{border:0}svg:not(:root){overflow:hidden}figure{margin:0}fieldset{border:1px solid #c0c0c0;margin:0 2px;padding:.35em .625em .75em}legend{border:0;padding:0}button,input,select,textarea{font-family:inherit;font-size:100%;margin:0}button,input{line-height:normal}button,select{text-transform:none}button,html input[type="button"],input[type="reset"],input[type="submit"]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}input[type="checkbox"],input[type="radio"]{box-sizing:border-box;padding:0}input[type="search"]{-webkit-appearance:textfield;-moz-box-sizing:content-box;-webkit-box-sizing:content-box;box-sizing:content-box}input[type="search"]::-webkit-search-cancel-button,input[type="search"]::-webkit-search-decoration{-webkit-appearance:none}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}textarea{overflow:auto;vertical-align:top}table{border-collapse:collapse;border-spacing:0}'
        },
        presets: {
            "default": {},
            standard: {
                breakpoints: {
                    mobile: {
                        range: "-480",
                        lockViewport: !0,
                        containers: "fluid",
                        grid: {
                            collapse: 1,
                            gutters: 10
                        }
                    },
                    desktop: {
                        range: "481-",
                        containers: 1200
                    },
                    "1000px": {
                        range: "481-1200",
                        containers: 960
                    }
                }
            }
        },
        defaults: {
            breakpoint: {
                test: null,
                config: null,
                elements: null
            },
            config_breakpoint: {
                range: "",
                containers: 960,
                lockViewport: !1,
                viewportWidth: !1,
                hasStyleSheet: !0,
                grid: {}
            }
        },
        DOMReady: null,
        getElementsByClassName: null,
        indexOf: null,
        iterate: null,
        
}();