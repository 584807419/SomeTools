# encoding='utf-8'

aaa = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>重庆三峡银行股份有限公司首次公开发行股票申请文件反馈意见</title>
<link href="../../../images/zjh.css" rel="stylesheet" type="text/css">
</head>

<body>
<div class="body_bk">
<div class="body">
<script>
function simpsearch()
{
	var url_str=document.location.href;
	var url_lst=url_str.split("/");
	url_str="";

	for(var i=3;i<url_lst.length;i++){
		if(url_lst[i].indexOf(".html")==-1)
		{
			url_str+=url_lst[i]+"/";
		}
	}
	url_str = url_str.substring(0,url_str.length -1);
	//alert(url_str);
	var searchword=document.simsearch.schword.value;
	//alert(searchword);
	var mess='<>/?{}=&*%^~`/~`()[]';
	if(searchword==""||searchword==null||searchword=="本站点检索"){
		alert('请检查输入条件，因为它不符合要求！');
		return false;
	}

	if(searchword.length>50)
	{
		alert("字符超长、最多输入50个汉字！");
		return false;
	}
	document.simsearch.searchword.value= url_str;
	document.simsearch.schword.value= searchword;	
	
	document.simsearch.method='post';
	//document.simsearch.action="http://180.9.1.54:9000/was40/search";
	document.simsearch.action='/wcm/websearch/zjh_simp_list.jsp';
}
</script>


<div class="topbar">
  <div style="float:left; line-height:25px;">
    <a href="http://www.csrc.gov.cn/SuniT/www.csrc.gov.cn/pub/newsite" onmousedown="a1.style.display='none';a2.style.display='block'">繁体版</a>|<a href="http://www.csrc.gov.cn/pub/csrc_en">English</a>
  </div>

   <div class="sobox">
    	<table>
          <tr>
            <td>站内搜索：</td>
<form method="post" action="" name="simsearch" id="simsearch" onsubmit="return simpsearch()" >

            <td>
                        <input name="schword" type="text" class="search_input" id="schword" onclick="javascript:if(this.value=='本站点检索') this.value=''" value="本站点检索">
                        <input type="hidden" name="searchword" value=''>
                        <input type="hidden" name="channelid" value='3858'>
                        <input type="hidden" name="whereId" value=''>
           </td>
            <td><input class="so_btn" name="" type="submit" value=""></td>
            <td><input class="so_btn_2" name="" type="button" value="高级" onclick="window.location.href='/wcm/websearch/advsearch.htm'"></td>
</form>
          </tr>
        </table>
        <div class="clear"></div>
    </div>
  <div class="clear"></div>
</div>

<div class="banner"><img src="../../../images\banner.gif" width="990"></div>


       <div class="menu">
    	<div class="f_left"><a href="http://www.csrc.gov.cn" target="_self"><img src="../../../images/menu_index.gif"></a></div>
        <div class="f_left"><img src="../../../images/menu_1.gif"></div>
        <div class="menu_li" style="z-index:9999">
<!--隐藏部分  政务        	
<div class="menu_jia" style="display:none" id="b11" >
	<div class="menu_jia_di" style="z-index:9999">
    <table width="100%" onmouseout="b11.style.display='none';a11.style.display='block'" onmouseover="b11.style.display='block'">
      <tr>
    
    <td><a href="/pub/zjhpublic/">信息公开</a></td>
    <td><a href="http://neris.csrc.gov.cn/falvfagui/">政策法规</a></td>
    <td><a href="../../../zjhxwfb/">新闻发布</a></td>
  </tr>
  <tr>
    <td><a href="http://eid.csrc.gov.cn">信息披露</a></td>
    <td><a href="/pub/newsite/sjtj/">统计数据</a></td>
    <td><a href="/pub/newsite/rjb/gwykl/">人事招聘</a></td>
  </tr>

      <tr>
        <td><a href="#">政策法规</a></td>
        <td><a href="#">产品披露</a></td>
        <td><a href="#">诚信建设</a></td>
      </tr>
<tr>
        <td><a href="#">机构设置</a></td>
        <td><a href="#">信息公开</a></td>
        <td><a href="#">新闻发布</a></td>
      </tr>
      <tr>
        <td><a href="#">信息披露</a></td>
        <td><a href="#">统计数据</a></td>
        <td><a href="#">人事信息</a></td>
      </tr>
      <tr>
        <td><a href="#">政策法规</a></td>
        <td><a href="#">产品披露</a></td>
        <td><a href="#">诚信建设</a></td>
      </tr>

    </table>
		</div>
</div>
<table width="100%" id="a11" onmouseover="a11.style.display='none';b11.style.display='block'">-->
<table width="100%">
  <tr>
    <!--td><a href="/pub/newsite/zjhjs/">机构设置</a></td-->
    <td><a href="/pub/zjhpublic/">信息公开</a></td>
    <td><a href="http://neris.csrc.gov.cn/falvfagui/">政策法规</a></td>
    <td><a href="../../../zjhxwfb/">新闻发布</a></td>
  </tr>
  <tr>
    <td><a href="http://eid.csrc.gov.cn">信息披露</a></td>
    <td><a href="/pub/newsite/sjtj/">统计数据</a></td>
    <td><a href="/pub/newsite/rjb/gwykl/">人事招聘</a></td>
  </tr>

</table>
<!--div class="menu_btn_1"><a href="#"><img src="../../../images/menu_btn.gif" width="19" height="19"></a></div-->

      </div>
        <div class="f_left"><img src="../../../images/menu_2.gif"></div>
        <div class="menu_li" style="z-index:9999">
        	<table width="100%" id="c11" onmouseover="c11.style.display='none';d11.style.display='block'">
  <tr>
    <td><a href="http://neris.csrc.gov.cn/alappl/home/guideH">办事指南</a></td>
    <td><a href="/pub/newsite/zxbs/">在线申报</a></td>
       <td><a href="/pub/newsite/zjjg/hfjgml/">监管对象</a></td>
  </tr>
  <tr>
    <td><a href="/pub/newsite/zjjg/ywzg/">业务资格</a></td>
    <td><a href="/pub/newsite/zjjg/ryzg/">人员资格</a></td>
    <td><a href="/pub/newsite/tzzbh1/">投资者保护</a></td>
  </tr>

</table>
<div class="menu_jia" style="display:none" id="d11" >
	<div class="menu_jia_di" style="z-index:9999">
    <table width="100%" onmouseout="d11.style.display='none';c11.style.display='block'" onmouseover="d11.style.display='block'">
        <tr>
    <td><a href="http://neris.csrc.gov.cn/alappl/home/guideH">办事指南</a></td>
    <td><a href="/pub/newsite/zxbs/">在线申报</a></td>
     <td><a href="/pub/newsite/zjjg/hfjgml/">监管对象</a></td>
  </tr>
  <tr>
    <td><a href="/pub/newsite/zjjg/ywzg/">业务资格</a></td>
    <td><a href="/pub/newsite/zjjg/ryzg/">人员资格</a></td>
    <td><a href="/pub/newsite/tzzbh1/">投资者保护</a></td>
  </tr>
      <tr>
        <td colspan="3"><a href="/pub/newsite/djffzqqhhdj/djffzqhd/ffzqqhjs/">非法证券期货风险警示</a></td>
        

      </tr>
    </table>
	<!--div class="menu_btn_2"><a href="#"><img src="../../../images/menu_btn2.gif" width="19" height="19"></a></div-->
	</div>
</div>

        </div>
        <div class="f_left"><img src="../../../images/menu_3.gif"></div>
        <div class="menu_li">


<!--隐藏部分 互动
<div class="menu_jia" style="display:none" id="f11" >
	<div class="menu_jia_di" style="z-index:9999">
    <table width="100%" onmouseout="f11.style.display='none';e11.style.display='block'" onmouseover="f11.style.display='block'">
          <tr>
    <td><a href="http://gzly.12386.gov.cn/csrc/sh.inb.publicmessage!messageList.sh">主席信箱</a></td>
    <td><a href="/pub/newsite/hdjl/xfzl/">信访专栏</a></td>
    <td><a href="http://jubao.csrc.gov.cn">举报专栏</a></td>
    
      </tr>
  <tr>
    <td><a href="/pub/newsite/hdjl/zxft/">在线访谈</a></td>
    <td><a href="/pub/newsite/hdjl/yjzj/index.htm">征求意见</a></td>
    <td><a href="#">网上调查</a></td>
   </tr>
      <tr>
        <td><a href="#">政策法规</a></td>
        <td><a href="#">产品披露</a></td>
        <td><a href="#">诚信建设</a></td>
      </tr>
<tr>
        <td><a href="#">机构设置</a></td>
        <td><a href="#">信息公开</a></td>
        <td><a href="#">新闻发布</a></td>
      </tr>
      <tr>
        <td><a href="#">信息披露</a></td>
        <td><a href="#">统计数据</a></td>
        <td><a href="#">人事信息</a></td>
      </tr>
      <tr>
        <td><a href="#">政策法规</a></td>
        <td><a href="#">产品披露</a></td>
        <td><a href="#">诚信建设</a></td>
      </tr>

    </table>
	
	</div>
</div>
        	<table width="100%" id="e11" onmouseover="e11.style.display='none';f11.style.display='block'">-->
<table width="100%">
  <tr>
    <td><a href="http://gzly.csrc12386.org.cn/csrc">公众留言</a></td>
    <td><a href="/pub/newsite/hdjl/xfzl/">信访专栏</a></td>
    <td><a href="http://neris.csrc.gov.cn/jubaozhongxin">举报专栏</a></td>
      
      </tr>
  <tr>
    <td><a href="/pub/newsite/hdjl/zxft/">在线访谈</a></td>
    <td><a href="/pub/newsite/hdjl/yjzj/index.htm">征求意见</a></td>
    <td><a href="http://neris.csrc.gov.cn/lianzhengpingyi">廉政评议</a></td>   
   </tr>
  

</table>
        </div>
        <div class="clear"></div>
    </div>

<div class="srcbox">
    	<div class="f_left"><img src="../../../images/icon01.gif" width="38" height="32"></div>
        <div class="weizhi">
        	您的位置：<a href="../../../" target="_self">首页</a>&nbsp;&gt;&nbsp;<a href="../../" target="_self">发行监管部</a>&nbsp;&gt;&nbsp;<a href="../" target="_self">首次公开发行反馈意见</a>
        </div>
        <div class="f_right"><img src="../../../images/srcbg_r.gif" width="1" height="32"></div>
        <div class="clear"></div>
    </div>
  	
    <!--概览分类-->
    <div class="in_main">
    	<div class="content">
        	<div class="title">重庆三峡银行股份有限公司首次公开发行股票申请文件反馈意见<br>
                                   


                 </div>
				<div class="time">
					<span>中国证监会 www.csrc.gov.cn</span>
                                        <span>时间：2020-12-04</span>
					<span>来源：</span>
					
				</div>
				<DIV id='TRS_AUTOADD_1607075044140'><style id=_Custom_V6_Style_>

#TRS_AUTOADD_1607075044140 P {
	MARGIN-TOP: 6px; FONT-FAMILY: 宋体; MARGIN-BOTTOM: 6px; FONT-SIZE: 10.5pt
}
#TRS_AUTOADD_1607075044140 TD {
	MARGIN-TOP: 6px; FONT-FAMILY: 宋体; MARGIN-BOTTOM: 6px; FONT-SIZE: 10.5pt
}
#TRS_AUTOADD_1607075044140 DIV {
	MARGIN-TOP: 6px; FONT-FAMILY: 宋体; MARGIN-BOTTOM: 6px; FONT-SIZE: 10.5pt
}
#TRS_AUTOADD_1607075044140 LI {
	MARGIN-TOP: 6px; FONT-FAMILY: 宋体; MARGIN-BOTTOM: 6px; FONT-SIZE: 10.5pt
}
#TRS_AUTOADD_1607075044140 {
	MARGIN-TOP: 6px; FONT-FAMILY: 宋体; MARGIN-BOTTOM: 6px; FONT-SIZE: 10.5pt
}
/**---JSON--
{"p":{"font-family":"宋体","font-weight":"","font-size":"10.5pt","line-height":"","direction":"","margin-top":"6px","margin-bottom":"6px","text-indent":""},"td":{"font-family":"宋体","font-weight":"","font-size":"10.5pt","line-height":"","direction":"","margin-top":"6px","margin-bottom":"6px","text-indent":""},"div":{"font-family":"宋体","font-weight":"","font-size":"10.5pt","line-height":"","direction":"","margin-top":"6px","margin-bottom":"6px","text-indent":""},"li":{"font-family":"宋体","font-weight":"","font-size":"10.5pt","line-height":"","direction":"","margin-top":"6px","margin-bottom":"6px","text-indent":""},"":{"font-family":"宋体","font-weight":"","font-size":"10.5pt","line-height":"","direction":"","margin-top":"6px","margin-bottom":"6px","text-indent":""}}
--**/</style>
<DIV class=Custom_UnionStyle>
<DIV>
<DIV>重庆三峡银行股份有限公司首次公开发行股票申请文件反馈意见，具体见附件。</DIV></DIV></DIV>
</DIV>
<br/>
<script language="javascript">
	var file_appendix='<a href="./P020201204639988160963.docx">重庆三峡银行股份有限公司首次公开发行股票申请文件反馈意见.docx</a>';
		if(file_appendix!="")
	{             
           document.write('<table width="758" border="0" cellpadding="0" cellspacing="1" bgcolor="#cce2ee" class="dtmagb10 boxcenter"><tr><td width="758" align="center" bgcolor="#FFFFFF"><table width="94%" border="0" cellpadding="0" cellspacing="0" class="h12"><tr><td height="22" align="left" valign="top"><a href="./P020201204639988160963.docx" class=h12>重庆三峡银行股份有限公司首次公开发行股票申请文件反馈意见.docx</a></td></tr></table></td></tr></table>');
	}
</script>
<script language="javascript">
		var link_appendix='';
	if(link_appendix!="")
	{             
           document.write('<table width="758" border="0" cellpadding="0" cellspacing="1" bgcolor="#cce2ee" class="dtmagb10 boxcenter"><tr><td width="758" align="center" bgcolor="#FFFFFF"><table width="94%" border="0" cellpadding="0" cellspacing="0" class="h12"><tr><td height="22" align="left" valign="top"></td></tr></table></td></tr></table>');
	}
</script>

		</div>
	</div>

<div class="foot"><!--img src="../../../2014/images/foot_link.gif"><br /-->
    <img src="../../../images/foot_line.gif"><br />
   	<a href="/pub/newsite/fzlm/gywm">关于我们</a> | <a href="/pub/newsite/fzlm/lxwm">联系我们</a> | <a href="/pub/newsite/fzlm/flsm">法律声明</a> <br />
    版权所有：中国证券监督管理委员会 京ICP备 05035542号 　<a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11040102700080" style="text-decoration:none;" target="_blank"><img src="../../../images/gaba.png" style="vertical-align:middle;" border="0"><font color="#333333"> 京公网安备 11040102700080号</font></a >
    </div>
</div>
</div>
</body>
</html>"""

import re

# string = aaa.replace('\r', '').replace('\n', '').replace('\t', '')
# match = re.search(r'wzwsfactor\|\d+', string, re.I)   # 匹配字符串不区分大小
# print(match)
# print(match.group())
# print(string[553:568])




# match = re.search('data_callback\(\[([\d\D]+?|\s+?|[\r\n]+?)\]\)', aaa, re.S)   # 匹配字符串不区分大小
# match = re.search('data_callback\((.*|\n*)\)', aaa, re.S)   # 匹配字符串不区分大小
# print(match)
# print(type(match.group(1)))
# print(match.group(1))


# comment = re.compile('data_callback\((.*|\n*)\)', flags=re.S)
# print(comment.findall(aaa))

res = aaa

comment = re.compile("'<a(.*|\n*)/a>'", flags=re.S)
print(comment.search(aaa)[0])
#
# regex = "downloadPdf1\('([\s\S]*?)'\,"
# res1 = re.search(regex, res).group(1)
# print(res1)
from lxml import etree
print(etree.HTML(comment.search(aaa)[0]).xpath('//a/@href'))
print(etree.HTML(comment.search(aaa)[0]).xpath('//a/text()'))