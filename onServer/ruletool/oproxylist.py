[{
	"name": "crossdomain_youku",
	"find": "https?:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/swf\/.*\/q?player.*\.swf",
	"monitor": "https?:\/\/v\.youku\.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_tudou",
	"find": "http:\/\/static\.youku\.com(\/v[\d\.]*)?\/v\/custom\/.*\/q?player.*\.swf",
	"monitor": "https?:\/\/static.youku.com\/crossdomain\.xml",
	"exfind": "https?:\/\/static.youku.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_tudou_sp",
	"find": ".*olc[^\.]*\.swf",
	"exfind": "https?:\/\/v\.youku\.com\/crossdomain\.xml",
	"monitor": "https?:\/\/www\.tudou\.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_sohu",
	"find": "https?:\/\/(tv\.sohu\.com\/upload\/swf\/(?!(ap|56)).*\d+|(\d+\.){3}\d+(:\d+)?\/webplayer)\/(Main|PlayerShell)[^\.]*\.swf",
	"monitor": "https?:\/\/(photocdn|live\.tv)\.sohu\.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_iqiyi|pps-c1",
	"find": "https?:\/\/www\.iqiyi\.com\/(player\/(\d+\/Player|[a-z0-9]*|cupid\/.*\/(pps[\w]+|clear))|common\/flashplayer\/\d+\/((PPS)?Main|Coop|Share|Enjon)?Player.*_(.|ad\d+))\.swf",
	"monitor": "\w{32}\.\w{3}.*qyid=\w{32}.*ran=\d+",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_iqiyi|pps-c2",
	"find": "https?:\/\/www\.iqiyi\.com\/player\/cupid\/common\/icon\.swf",
	"monitor": "notavailable",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_iqiyi|pps-main",
	"find": "https?:\/\/.*(iqiyi|pps)\.com\/.*\.htm",
	"exfind": "\w{32}\.\w{3}.*qyid=\w{32}.*ran=\d+",
	"monitor": "policy\.video\.iqiyi\.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_letv",
	"find": "https?:\/\/.*letv[\w]*\.com\/.*\/((?!(Live|seed|Disk))(S[\w]{2,3})?(?!Live)[\w]{4}|swf)Player*\.swf",
	"monitor": "https?:\/\/player\.letvcdn\.com\/crossdomain\.xml",
	"extra": "crossdomain"
}, {
	"name": "crossdomain_douyu",
	"find": "https?:\/\/staticlive\.douyucdn\.cn\/common\/simplayer\/WebRoom.*\.swf",
	"monitor": "https?:\/\/www\.douyu\.com\/lapi\/live\/getPlay\/[\d+]",
	"extra": "crossdomain"
}, {
	"name": "aclog3.huomaotv.cn:80",
	"find": "",
	"monitor": "",
	"extra": "proxy"
}
]