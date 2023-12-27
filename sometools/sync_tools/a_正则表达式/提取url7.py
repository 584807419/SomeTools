# encoding='utf-8'

aaa = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>

<head>

	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>中国银行保险监督管理委员会 金融许可证信息</title>
	<link rel="Shortcut Icon" href="image/favicon.ico" />
	<script type="text/javascript">
		var basePath = "/jr";
			var inde=3;
			document.oncontextmenu = ppMousedownOfRight; 
		    function  ppMousedownOfRight(){      
		        event.cancelBubble = true     
			    event.returnValue = false;     
			    return false;
			}
		    var baseUrl = 'WkCLMg/';
	</script>

	<link href="css/style.css" rel="stylesheet" type="text/css" />
	<link rel="stylesheet" type="text/css" href="ext/resources/css/ext-all.css" />
	<script type="text/javascript" src="ext/adapter/ext/ext-base.js"></script>
	<script type="text/javascript" src="ext/ext-all.js"></script>

	<script type="text/javascript" src="ext/ext-lang-zh_CN.js"></script>
	<script type="text/javascript" src="js/common.js"></script>
	<script type="text/javascript" src="js/check.js"></script>
	<script type="text/javascript" src="js/licencequery.js?v=v1.11"></script>

	<script type="text/javascript" src="js/cookie.js"></script>


	<script type="text/javascript" src="js/jquery-1.3.2.min.js"></script>


	<script type="text/javascript">
		writercookie();
var isShowVerifyCode = true;
	</script>
</head>

<body onload="" style="min-width:960px;">




	<div class="log" style="background: url(/jr/image/logobg.jpg);background-repeat: repeat-x;height:85px;">
		<div
			style="position:relative;width:1024px;height:85px;margin:0 auto;background: url(/jr/image/logo-jr.png);background-repeat: no-repeat;">

			<div class="top_publish" id="top_publish" unselectable="on">

			</div>
		</div>
	</div>

	<div class="sheet">
		<div align="center">
			<table id="tblSheets" width="1024" border="0" cellpadding="0" cellspacing="0" class="sheet">
				<tr>
					<td nowrap="nowrap" id="tit_0" onclick="changeType(this,3)" class="on"><span>机构持有列表</span></td>
					<td nowrap="nowrap" id="tit_1" onclick="changeType(this,1)" class="noon">近期机构设立情况</td>
					<td nowrap="nowrap" id="tit_2" onclick="changeType(this,9)" class="noon">失控情况</td>
					<td nowrap="nowrap" id="tit_3" onclick="changeType(this,7)" class="noon">机构退出列表</td>
					<td width="70%" class="space"></td>
				</tr>
			</table>
		</div>
	</div>
	<div align="center">
		<table width="1024" border="0" align="center" cellpadding="0" cellspacing="0" class="trw-table-s1">
			<tr class="a0">
				<td align="right" height="30">
					机构名称：
				</td>
				<td>
					<input name="fullName" id="fullName" type="text" value="" class="trw-form-text-blank" autocomplete="off">
					</td>
				<td align="right">
					机构地址：
				</td>
				<td>
					<input name="address" id="address" type="text" value="" class="trw-form-text-blank" autocomplete="off">
					</td>
				<td align="right" height="25">
					流水号：
				</td>
				<td>
					<input name="flowNo" id="flowNo" type="text" value="" maxlength="8" class="trw-form-text-blank" onblur="value=value.replace(/[^\d]/g,'')"
	  onbeforepaste="clipboardData.setData('text',clipboardData.getData('text').replace(/[^\d]/g,''))" autocomplete="off">
					</td>
				<td rowspan="2" align="center">
					<input id="reportSearch" onclick='submitData()' type="button" class="btn sel" value="查询" disabled="disabled"><br />

					</td>
			</tr>
			<tr class="a0">
				<td align="right" height="25">
					机构类型：
				</td>
				<td>
					<div style="margin-bottom: 5px;margin-top: 3px;">
						<input type="text" id="organTypeNo" autocomplete="off"/></div>
						<div style="margin-bottom: 5px;">
							<input type="text" id="jrorganperproty" size="20" autocomplete="off"/></div>
							<div style="margin-bottom: 3px;">
								<input type="text" id="organBranchTypeNo" autocomplete="off"/></div>
				</td>
				<td align="right" height="25">
					监管机构：
				</td>
				<td>
					<div style="margin-bottom: 5px;margin-top: 3px;">
						<input type="text" id="fatherOrganNo" autocomplete="off"/></div>
						<div style="margin-bottom: 3px;"><input type="text" id="organNo" autocomplete="off"/></div>
				</td>

				<td align="right" height="25">
					所在省市：
				</td>
				<td>
					<div style="margin-bottom: 5px;margin-top: 3px;">
						<input type="text" id="provinece" autocomplete="off"/></div>
						<div style="margin-bottom: 3px;"><input type="text" id="orgAddress" autocomplete="off"/></div>
				</td>
			</tr>

		</table>
		<div style="width: 1024px;" align="left">
			<div id="queryResult" class="queryResult" unselectable="on">共查询出 0 条数据（用时约 0 s）</div>
			<div id="queryList"></div>
		</div>
	</div>

	<div id="mask" style="z-index: 99;">
	</div>
	<div id="show_msg" style="z-index: 100;width: 450px;">
		<table width="100%" border="0" align="center" cellpadding="0" cellspacing="0" class="trw-table-s1">
			<tr class="a1" style="height: 35px;">
				<td align="center" width="98%">
					请输入验证码(不区分大小写)
				</td>
			</tr>
			<tr>
				<td valign="middle" style="padding-top: 15px;">
					<input type="text" value="" placeholder="请输入验证码（不区分大小写）" class="verification-code" id ="verificationCode" autocomplete="off">

					<img id="verifyCodeImg" src="" onclick="changeCodeImg()" alt="验证码" title="点击刷新验证码" style="border: 1px solid #efefef;width:100px; height: 40px;">
                    </td>
			</tr>

			<tr class="a0">
				<td height="30" align="center">
					<input type="button" class="btn" onClick="closeDIV();" value="关闭" style="margin-right: 20px;" />
					<input type="button" class="btn" onClick="saveJW();" value="确定" />
                    </td>
			</tr>
		</table>
	</div>


	<div class="searchblock" id="bottom1" style="border-top: 1px;" align="center">
		<div style="width:1024px;margin:0 auto;" align="left">
			注：本系统中所称“发证日期”是监管部门对金融机构颁（换）发许可证的制证日期；“批准成立日期”为监管部门批准该机构设立的日期，金融机构自此具有开展金融业务的一般资质，其他具体新增业务以监管部门的相关文件为准。
			<span id ="bot_lz0" style="display:inline;">另注红色流水号为失控证，正在补办中；机构编码为红色的，其许可证被银保监会发证机关暂扣。</span>
			<span id ="bot_lz1" style="display:none;">另注此数据为近期一年机构设立情况。</span>
			<span id ="bot_lz2" style="display:none;">另注此数据为本系统模块上线以来的机构退出列表。</span>
		</div>
	</div>
	<div class="searchblock" id="bottom2" style="border-top: 1px;display: none;" align="center">
		<div style="width:1024px;margin:0 auto;" align="left">
			注：与此表流水号相符金融许可证已失控，已被监管部门确定为无效证，特此向社会公告。
		</div>
	</div>
	<style type="text/css">
		.footer-ll {
			width: 1024px;
			margin: 2px auto;
			font-size: 12px;
			color: #6f6f6f;
			/*     text-align: center; */
		}

		.footer-ll span {
			display: inline-block;
			height: 20px;
			line-height: 20px;
			margin: 1px 2px;

		}

		.footer-ll a {
			text-decoration: none;
			color: #6f6f6f;
		}
	</style>

	<div align="center">
		<div align="left" class="footer-ll">
			<div style="position:relative;width:1024px; margin:0 auto;">
				<div>
					<span>
	                        网站标识码：bm55000001 <a href="http://beian.miit.gov.cn/" target="_blank">京ICP备19014889号</a>
	        </span>
					<span style="background:url(image/bicon7.png) no-repeat;">
	            <a target="_bank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010202008000" style="padding-left:22px;color:#939393">
	                            京公网安备11010202008000号
	            </a>
	        </span>
					<span>本网站支持IPv6</span>
				</div>

				<div>
					<span>主办单位：中国银行保险监督管理委员会</span>
					<span>地址：北京市西城区金融大街甲15号</span>
					<span>邮政编码：100033</span>
				</div>
				<div style="position:absolute; right:0px; top: 0px; ">
					<div style="position:absolute; right:140px; top: -5px;">
						<a href="http://bszs.conac.cn/sitename?method=show&id=97AAC5543B920562E05310291AACE801"
							target="_blank">
							<img border="0" src="/jr/image/conace.png" style="width:80px;height:80px;">
	        </a>
					</div>
					<div style="position:absolute; right:0px; top:10px;">
						<script id="_jiucuo_" sitecode="bm55000001" src="https://zfwzgl.www.gov.cn/exposure/jiucuo.js"
							type="text/javascript"></script>
					</div>

				</div>
			</div>
		</div>
	</div>
	<div align="center">
		<div align="left" class="lic_botm" style="width:1024px; margin:0 auto;text-align:left;padding-left: 2px; ">
			访问次数：2280727 次</div>
	</div>
</body>

</html>"""



import re
match = re.search("var baseUrl = '(.*|\n*)/';\n\t</script>\n\n\t<link href=", aaa, re.S)   # 匹配字符串不区分大小
print(match.group(1))
print(type(match.group(1)))
print(match.group(1))

