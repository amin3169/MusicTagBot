from FallenMusic import BOT_NAME

PM_START_TEXT = """
Salam {0},Mənim Adım {1}.

──────────────────
Bs Mp3 Bot'una Xoş Gəldin ⚜

Qrupunuza Əlavə Etməklə
Musiqi Dinləyə Bilərsiniz. 🎧



"""

START_TEXT = """
Salam {0}
{1} İɴᴅɪ ᴍᴀʜɴɪ ᴏxᴜʏᴀ ʙɪʟƏʀ {2}.

──────────────────
➻ Mənim Haqqımda Kömək Etmək Üçün Və Ya Bir Şey Soruşmaq İstəyirsizsə, Mənim [Dəstək Çatıma]({3}) Qoşula Bilərsiniz.
"""

HELP_TEXT = f"""
<u>❄ **İꜱtifadəçilər Üçün Mövcud Əmrlər {BOT_NAME} :**</u>

•━━━━━━━━•••━━━━━━━━•
๏ /play : Səslu Çatda Musiqi Başlayır.
๏ /pause : Carı İfaya Fasilə Verir.
๏ /resume : Dayandırılmış Yayımı Davam Etdirin.
๏ /skip : Carı İfanı Atlayır Və Növbədə Olan Treki Yayımlamağa Başlayar.
๏ /end : Carı İfa Axınını Bitirər.
๏ /ping : Botun Ping Və Sistem Statiskaların Göstərir.
๏ /sudolist : Botun Sudo İstifadəçilərinin Siyahısın Göstərir.
๏ /song : İstədiyiniz Mahnını Yükləyir.
๏ /search : Verilən Sorğunu Youtube de Axtarır Və Nəticələrin Sizə Göstərir.
•━━━━━━━━•••━━━━━━━━•
"""

HELP_SUDO = f"""
<u>✨ **Sudo Əmrlərinə Daxil Olur {BOT_NAME} :**</u>

•━━━━━━━━•••━━━━━━━━•
๏ /activevc : Hazırda Aktiv Səsli Söhbətlərin Siyahısın Göstərir .
๏ /eval və ya /sh : Verilmiş Kodu Bot Terminalında İşlədir.
๏ /speedtest : Botlar Serverində Sürət Testini Həyata Keçirir.
๏ /sysstats : Botlar Serverinin Sistem Statiskasım Həyata Keçirir .
๏ /setname [Mətn Və Ya Mətnə Cavab] : Köməkçi Hesabının Adını Dəyişdirin .
๏ /setbio [Mətn Və Ya Mətnə Cavab] :  Köməkçi Hesabının Bio-nu Dəyişdirin .
๏ /setpfp [Fotoya Cavab Verin] : Köməkçi Hesabının  .
๏ /delpfp : Köməkçi Hesabının PFP-Nı Silin.
•━━━━━━━━•••━━━━━━━━•
""""

HELP_DEV = f"""
<u>✨ **Sahib Əmr Verir {BOT_NAME} :**</u>

•━━━━━━━━•••━━━━━━━━•
๏ /config : ʙᴏᴛᴜɴ ʙÜᴛÜɴ ᴋᴏɴꜰɪQᴜʀᴀꜱɪʏᴀ ᴅƏʏɪŞƏɴʟƏʀɪɴɪ ƏʟᴅƏ ᴇᴛᴍƏᴋ ÜÇÜɴ.
๏ /broadcast: [ᴍᴇꜱᴀᴊ ɢÖɴᴅƏʀɪɴ ᴠƏ ʏᴀ ᴍᴇꜱᴀᴊᴀ ᴄᴀᴠᴀʙ ᴠᴇʀɪɴ] : ᴍᴇꜱᴀᴊɪ ʙᴏᴛᴜɴ xɪᴅᴍƏᴛ ᴇᴅɪʟƏɴ Çᴀᴛʟᴀʀɪɴᴀ Çᴀᴛᴅɪʀɪɴ.
๏ /rmdownloads :ʙᴏᴛʟᴀʀ ꜱᴇʀᴠᴇʀɪɴᴅƏ ʏÜᴋʟƏɴᴍɪŞ ᴋᴇŞ ꜰᴀʏʟʟᴀʀɪɴɪ ᴛƏᴍɪᴢʟƏʏɪʀ.
๏ /leaveall : ᴋÖᴍƏᴋÇɪ ʜᴇꜱᴀʙɪɴᴀ ʙÜᴛÜɴ ꜱÖʜʙƏᴛʟƏʀɪ ᴛƏʀᴋ ᴇᴛᴍƏʏɪ Əᴍʀ ᴇᴅɪʀ.
๏ /addsudo : [İꜱᴛɪꜰᴀᴅƏÇɪ ᴀᴅɪ ᴠƏ ʏᴀ ɪꜱᴛɪꜰᴀᴅƏÇɪʏƏ ᴄᴀᴠᴀʙ] : İꜱᴛɪꜰᴀᴅƏÇɪɴɪ ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ ʟɪꜱʀ-Ə ƏʟᴀᴠƏ ᴇᴅɪɴ.
๏ /rmsudo : [İꜱᴛɪꜰᴀᴅƏÇɪ ᴀᴅɪ ᴠƏ ʏᴀ ɪꜱᴛɪꜰᴀᴅƏÇɪʏƏ ᴄᴀᴠᴀʙ] : İꜱᴛɪꜰᴀᴅƏÇɪɴɪ ꜱᴜᴅᴏ ɪꜱᴛɪꜰᴀᴅƏÇɪʟƏʀɪ ꜱɪʏᴀʜɪꜱɪɴᴅᴀɴ Çɪxᴀʀɪɴ..
•━━━━━━━━•••━━━━━━━━•
"""
TAG_MSJ = f"""
•━━━━━━━━•••━━━━━━━━•
**“📚 Əmrlər„ Bunlardır.⤵**
•━━━━━━━━•••━━━━━━━━•
**㋡⇰ /tag “Səbəb„ - 5-Lı Tağ Atışları.**
**㋡⇰ /etag “Səbəb„ - Emoji İlə Etiketlər.**
**㋡⇰ /stag “Səbəb„ - Söz'Lü Tag Etiketlər.**
**㋡⇰ /tektag “Səbəb„ - Üzvləri Tək-Tək Etiletlər.**
**㋡⇰ /ctag “Səbəb„ - Cümlə İlə  Etiketlər.**
**㋡⇰ /admins “Səbəb„ - İdarəçiləri Tək-Tək Etiketlər.**
**㋡⇰ /cancel - Tag Eləməyi Dayandırır.**
•━━━━━━━━•••━━━━━━━━•
"""
