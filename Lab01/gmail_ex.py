# Gửi email về 20130075@student.hust.edu.vn 
from gmail import * 
from random import choice 


gmail = GMail('YBOX Vietnam <ybox.vn@gmail.com>','ybox@*1234')

html_content = """
<p style="text-align: center;">Cộng Ho&agrave; X&atilde; Hội Chủ Nghĩa Việt Nam</p>
<p style="text-align: center;"><em>Độc Lập - Tự Do - Hạnh Ph&uacute;c&nbsp;</em></p>
<p style="text-align: center;"><em>--------***--------</em></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC&nbsp;</strong></p>
<p>&nbsp;</p>
<p><em>K&iacute;nh gửi thầy: Đỗ Tuấn Anh</em></p>
<p>Em l&agrave; Đặng Hồng Th&aacute;i, em viết email n&agrave;y để xin thầy nghỉ học vì {{sickness}} </p>
<p>Em xin c&aacute;m ơn thầy &lt;3</p>
<p>Hồng Th&aacute;i&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></p>

"""

reasons = ["Ốm", "Đau Bụng","Gấu Dỗi"]
rand_reason = choice(reasons)
html_to_send = html_content.replace("{{sickness}}",rand_reason)



msg = Message(
    'Mail Subject',
    to='Receiver <thaidanghongftu@gmail.com >',
    html = html_to_send
    )
gmail.send(msg) 
