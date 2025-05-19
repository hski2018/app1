from flet import * 
import datetime
import requests
import os,time
from num2words import num2words
# import psutil,threading
# browser_names = ["firefox.exe", "msedge.exe", "iexplore.exe", "opera.exe", "brave.exe"]
# # from try_list import create_customer_statement
# # import urllib.parse
# def close_browser_after_delay(delay=10):
#     time.sleep(delay)
#     browser_names = ["chrome.exe", "firefox.exe", "msedge.exe", "brave.exe"]
#     for proc in psutil.process_iter(['pid', 'name']):
#         try:
#             if proc.info['name'] and proc.info['name'].lower() in browser_names:
#                 # print(f"إغلاق المتصفح: {proc.info['name']}")
#                 proc.terminate()
#         except (psutil.NoSuchProcess, psutil.AccessDenied):
#             continue

def main(page: Page):
    page.title = "تطبيق تحصيل"
    page.bgcolor = "#E3F2FD"
    page.fonts = {
        "LB": "/lbc.ttf"
    }
    url = "http://192.168.8.14:8001/"
    key = "12345678999"
    page.theme = Theme(font_family="LB")
    page.update()

    page.scroll = True
    page.padding = 0

    list1=ListView(expand=1, spacing=10, padding=20, auto_scroll=False,width=500)
    list2=ListView(expand=1, spacing=10, padding=20, auto_scroll=False,width=500)
    list3=ListView(expand=1, spacing=10, padding=20, auto_scroll=False,width=500)
    list4=ListView(expand=1, spacing=10, padding=20, auto_scroll=False,width=500)
    list_t_sahm1=ListView(expand=1, spacing=10, auto_scroll=False)
    list_t_sahm=ListView(expand=1, spacing=10, auto_scroll=False)
    list_t_sahm2=ListView(expand=1, spacing=10, auto_scroll=False)


    # عناصر الإدخال
    username = TextField("admin",label="اسم المستخدم", border_radius=12,on_blur=lambda e:get_face(e),filled=True,text_vertical_align=-1.5, bgcolor="#F0F4FF", width=300,height=40)
    password = TextField("123",label="كلمة المرور", password=True, can_reveal_password=True, border_radius=12,text_vertical_align=-1.5, filled=True, bgcolor="#F0F4FF", width=300,height=40)
    userid=TextField("", border_radius=12, filled=True, bgcolor="#F0F4FF", width=300)
    all_mony=TextField(0.00,border_radius=12, filled=True, bgcolor="#F0F4FF", width=300)
    all_mony1=TextField(0.00,border_radius=12, filled=True, bgcolor="#F0F4FF", width=300)
    all_mony2=TextField(0.00,border_radius=12, filled=True, bgcolor="#F0F4FF", width=300)
    clint_info=TextField("اضافة عميل جديد",border_radius=0,width=320,read_only=True,height=40,text_vertical_align=-1.5,text_align="center",text_size=30)
    info=TextField("معلومات الحساب",border_radius=0,width=320,read_only=True,height=40,text_vertical_align=-1.5,text_align="center",text_size=30)
    info_id=TextField("رقم الحساب",border_radius=0,border_width=0,bgcolor="#093C69",width=150,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    info_type=TextField("نوع الحساب",border_radius=0,border_width=0,bgcolor="#093C69",width=150,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    info_name=TextField("الاسم",border_radius=0,bgcolor="#093C69",border_width=0,width=80,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    info_moto=TextField("المتاخرات",border_radius=0,bgcolor="#093C69",border_width=0,width=150,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    info_get_mony=TextField("المبلغ",border_radius=0,bgcolor="#093C69",border_width=0,width=150,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    info_mony=TextField("مبلغ التحصيل",border_radius=0,bgcolor="#093C69",border_width=0,width=340,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    id=TextField("",label="الرقم",filled=True,border_radius=0,width=170,border_width=1,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15)
  
    clint_new_name=TextField(label="ادخل الاسم",on_blur=lambda e:get_face(e), text_align=TextAlign.RIGHT,height=60)
    clint_new_no_b=TextField(label="ادخل رقم البطاقة",on_blur=lambda e:get_face(e), text_align=TextAlign.RIGHT,height=60)
    clint_new_not=TextField(label="ملاحظة",on_blur=lambda e:get_face(e), text_align=TextAlign.RIGHT,height=60)
    clint_new_phone1=TextField(label="ادخل رقم الهاتف",on_blur=lambda e:get_face(e), text_align=TextAlign.RIGHT,height=60)
    clint_new_phone2=TextField(label="ادخل رقم الهاتف2",on_blur=lambda e:get_face(e), text_align=TextAlign.RIGHT,height=60)
    clint_new_name_l=TextField("الاسم",border_radius=0,bgcolor="#093C69",border_width=0,width=80,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    clint_new_no_b_l=TextField("رقم البطاقة",border_radius=0,bgcolor="#093C69",border_width=0,width=150,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    clint_new_phon1_l=TextField("رقم الهاتف1",border_radius=0,bgcolor="#093C69",border_width=0,width=150,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    clint_new_phon2_l=TextField("رقم الهاتف2",border_radius=0,bgcolor="#093C69",border_width=0,width=150,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    rseed1_Y=TextField(0,text_size=8,expand=1,
                max_lines=1,)
    rseed2_S=TextField(0,text_size=8,expand=1,
                max_lines=1,)
    rseed3_D=TextField(0,text_size=8,expand=1,
                max_lines=1,)
    rseed1_Y1=TextField(0,text_size=8,expand=1,
                max_lines=1,)
    rseed2_S1=TextField(0,text_size=8,expand=1,
                max_lines=1,)
    rseed3_D1=TextField(0,text_size=8,expand=1,
                max_lines=1,)
    all_Y=TextField(0,text_size=8,expand=1,
                max_lines=1,)
    all_S=TextField(0,text_size=8,expand=1,
                max_lines=1,)
    all_D=TextField(0,text_size=8,expand=1,
                max_lines=1,)

    SAHM_new_name=TextField("",filled=True,on_blur=lambda e:get_face(e), border_radius=0,border_width=1,width=240,height=30,text_vertical_align=-1.5,text_align="center",text_size=15)
    SAHM_id=TextField("",label="رقم السهم",filled=True,on_blur=lambda e:get_face(e), border_radius=0,border_width=1,width=170,height=30,text_vertical_align=-1.5,text_align="center",text_size=15)
    clint_id=TextField("",label="رقم العميل",filled=True,on_blur=lambda e:get_face(e), border_radius=0,border_width=1,width=80,height=30,text_vertical_align=-1.5,text_align="center",text_size=15)
    SAHM_mony=TextField("",label="المبلغ",filled=True,on_blur=lambda e:get_face(e), border_radius=0,border_width=1,width=170,height=30,text_vertical_align=-1.5,text_align="center",text_size=15)
    SAHM_new_name_l=TextField("الاسم",border_radius=0,bgcolor="#093C69",border_width=0,width=80,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    SAHM_clint_id_l=TextField("رقم السهم",border_radius=0,bgcolor="#093C69",border_width=0,width=150,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    SAHM_mony_l=TextField("قيمة السهم",border_radius=0,bgcolor="#093C69",border_width=0,width=150,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    SAHM_date=TextField("قيمة ",border_radius=0,bgcolor="#093C69",border_width=0,width=170,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    SAHM_date_l=TextField("تاريخ الاحتساب",border_radius=0,bgcolor="#093C69",border_width=0,width=150,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")
    SAHM_type1_l=TextField("نوع الحساب",border_radius=0,bgcolor="#093C69",border_width=0,width=150,height=80,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15,color="white")

    names=TextField("",filled=True,on_blur=lambda e:get_face(e), border_radius=0,border_width=1,width=240,height=30,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15)
    moto=TextField("", filled=True,on_blur=lambda e:get_face(e),border_radius=0,width=170,height=30,border_width=1,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15)
    get_mony=TextField("",filled=True,on_blur=lambda e:get_face(e),border_radius=0,width=170,height=30,border_width=1,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15)
    type_name=TextField("",filled=True,on_blur=lambda e:get_face(e), border_radius=0,width=170,height=30,border_width=1,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=15)
    mony=TextField("0.00",label="المبلغ",on_blur=lambda e:get_face(e),on_focus=lambda x:get_val(x),border_radius=0,width=175,height=50,text_vertical_align=-1.5,text_align="center",text_size=15)
    now=datetime.datetime.now()
    dat_s =str(now.strftime("%Y/%m/%d"))
    dat11=TextField(dat_s,border_radius=0,color=colors.BLACK,height=25,width=105,read_only=True,text_align="center",text_size=13,border_width=0)
    dat2=TextField(dat_s,border_radius=0,color=colors.BLACK,height=25,width=105,read_only=True,text_align="center",text_size=13,border_width=0)
    header = Container(
        content=Text(
            "إشعار سداد",
            weight="bold",
            size=20,
            text_align="center",
            color=colors.WHITE
        ),
        bgcolor=colors.BLUE_800,
        padding=15,
        border_radius=10,
        margin=10,
        alignment=alignment.center
    )

    def open_pdf(e):
        # استخدم المسار الكامل للملف
        pdf_path = "file:///storage/emulated/0/Download/755.pdf"  # على Android مثلًا
        page.launch_url(pdf_path)
        page.update()
        #print("OK")
    # all_tsdid1=TextField(0,border_radius=0,bgcolor=colors.BLACK12,color=colors.YELLOW_400,height=25,width=340,read_only=True,text_vertical_align=-1.5,text_align="center",text_size=12)
    def handle_change(e):
        dat11.value=str(f"{e.control.value.strftime('%Y-%m-%d')}")
        page.update()
        # get_aeerad()  

    def handle_dismissal(e):
        dat11.value=str(f"DatePicker dismissed")
    def handle_change1(e):
        dat2.value=str(f"{e.control.value.strftime('%Y-%m-%d')}")
        page.update()
        # get_aeerad()
    def handle_dismissal1(e):
        dat2.value=str(f"DatePicker dismissed")

    # msgbox_add_clint = AlertDialog(
    #     modal=True,
    #     title=Text("هل تريد حفظ بيانات العميل",text_align="right"),
    #     content=Text(names.value+" ?",text_align="right"),
    #     actions=[
    #         TextButton("Yes",on_click=lambda x:go_save(x)),
    #         TextButton("No",on_click=lambda x:close_msg1(x)),
        
            
    #     ],
    #     # actions_overflow_button_spacing=250,
    #     actions_alignment=MainAxisAlignment.SPACE_BETWEEN,
    #     on_dismiss=lambda e: page.add(
    #         Text("Modal dialog dismissed"),
    #     ),
    # )
    # msgbox_add_snd = AlertDialog(
    #     modal=True,
    #     title=Text("هل تريد حفظ السند",text_align="right"),
    #     content=Text(names.value+" ?",text_align="right"),
    #     actions=[
    #         TextButton("Yes",on_click=lambda x:go_save(x)),
    #         TextButton("No",on_click=lambda x:close_msg1(x)),
        
            
    #     ],
    #     # actions_overflow_button_spacing=250,
    #     actions_alignment=MainAxisAlignment.SPACE_BETWEEN,
    #     on_dismiss=lambda e: page.add(
    #         Text("Modal dialog dismissed"),
    #     ),
    # )
    # msgbox_add_sahm= AlertDialog(
    #     modal=True,
    #     title=Text("هل تريد اضافة الحساب؟",text_align="right"),
    #     content=Text(names.value+" ?",text_align="right"),
    #     actions=[
    #         TextButton("Yes",on_click=lambda x:go_save(x)),
    #         TextButton("No",on_click=lambda x:close_msg1(x)),
        
            
    #     ],
    #     # actions_overflow_button_spacing=250,
    #     actions_alignment=MainAxisAlignment.SPACE_BETWEEN,
    #     on_dismiss=lambda e: page.add(
    #         Text("Modal dialog dismissed"),
    #     ),
    # )
    
    def get_re(url, query, lists, key):
        try:
            params = {
                'query': query,
                'lists': lists,
                'key': key
            }
            response = requests.get(url, params=params)
            response.raise_for_status()  # هذا يرفع استثناء لو حصل خطأ في الاستجابة

            return response.json()
        
        except requests.exceptions.RequestException as e:
            # عرض رسالة خطأ باستخدام SnackBar
            page.snack_bar = SnackBar(Text(f"حدث خطأ أثناء الاتصال: {e}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return None

    def get_face(e):
        try:

            
            # x=float(e.control.value)
            e.control.autofocus=True
            # #print(e.control.value)
            page.update()

                    
        except:
            pass
    
    def get_val(e):
        try:

            if e.control.value.isdigit():
                x=float(e.control.value)
                e.control.value=f"{x:.2f}"
                #print(e.control.value)
                page.update()
                # #print(e.control.value)
                # #print("ok")
            else:
                try:

                    x=e.control.label
                    a3=AlertDialog(
                                        title=Text(f"قيمة حقل {x} غير صحيحة",size=13),

                                        actions_alignment=MainAxisAlignment.CENTER,

                                    )
                    page.overlay.append(a3)
                    e.control.value=0.00
                    e.control.focus()
                    a3.open=True
                    page.update()
                except:
                    pass
        except:
            pass
    no_hwala=TextField("",label="رقم الحوالة", border_radius=0,width=340,height=48,text_vertical_align=-1.5,text_align="center",text_size=15)
    not1=TextField("",label="ملاحظه", border_radius=0,width=340,height=48,text_vertical_align=-1.5,text_align="center",text_size=15)
    

    now=datetime.datetime.now()
    dat_s =str(now.strftime("%Y/%m/%d"))
    dat1=TextField(dat_s,border_radius=0,filled=True,height=40,width=105,read_only=True,text_vertical_align=-1.7,text_align="center",text_size=15)
    now = datetime.datetime.now().strftime("%Y/%m/%d")
    amlah=Dropdown(
        label="تحديد العملة",
        expand=1,
        # width=175,
        options=[
            dropdown.Option(key="ريال يمني"),
            dropdown.Option(key="ريال سعودي"),
            dropdown.Option(key="دولار"),

        ],
    )
    amlah.value=amlah.options[0].key
    # تعريف الحقول داخل النافذة
    name_sahm_input= TextField(label="اسم العميل", text_align=TextAlign.RIGHT,read_only=True,height=60,on_click=lambda x: open_client_search(x),on_focus=lambda x: open_client_search(x))
    mony_sahm_input= TextField(value=0.00,label="ادخل المبلغ",on_focus=lambda e:get_face(e),on_blur=lambda x:get_val(x), text_align=TextAlign.CENTER,height=60,keyboard_type="number")
    id_clint_sahm_input= TextField(label="رقم العميل",on_blur=lambda e:get_face(e), text_align=TextAlign.RIGHT,height=60)
    dat_sahm_input= TextField(now,label="التاريخ",on_blur=lambda e:get_face(e), text_align=TextAlign.CENTER,height=60)
    sahm_new_not= TextField("",label="ملاحظة",on_blur=lambda e:get_face(e), text_align=TextAlign.RIGHT,height=60)
    direction_sahm = RadioGroup(
        on_change=lambda x:ty(x),
        value="حساب جاري",
        content=Row([
            Radio(value="سهم",label="سهم" ),
            Radio(value="حساب جاري",label="حساب جاري" ),
        ])
    )
    amount_input = TextField(label="ادخل المبلغ", on_blur=lambda x:get_val(x),on_focus=lambda e:get_face(e),text_align=TextAlign.CENTER,height=60,keyboard_type="number")
    note_input = TextField(label="اكتب البيان",on_blur=lambda e:get_face(e), text_align=TextAlign.RIGHT,height=60)
    mony_sahm_input.visible=False
    direction = RadioGroup(
        value="ايداع",
        content=Row([
            Radio(value="ايداع",label="ايداع" ),
            Radio(value="سحب",label="سحب" ),
        ])
    )
    ########################
    search_box = TextField(label="بحث عن عميل",rtl=True,autofocus=True)
    result_list = Column()

    ##################################################
    def search(e):
        clients=get_re(f'{url}1/', 'SELECT * FROM CLIENTS','', key)
        if clients != None:
            search_text = search_box.value
            result_list.controls.clear()
            for c in clients:
                if search_text in c["CLIENT_NAME"]:
                    result_list.controls.append(
                        ListTile(
                            leading=Text(c["ID"],rtl=True,text_align="right"),
                            title=Text(""),
                            subtitle=Text(c["CLIENT_NAME"]),
                            on_click=lambda e, client=c: select_client(client)
                        )
                    )
            result_list.update()
    
    def select_client(client):
        name_sahm_input.value = client["CLIENT_NAME"]
        id_clint_sahm_input.value = client["ID"]
        dlg.open = False
        open_dialog_sahm("5")
        page.update()

    # ربط البحث بحقل البحث
    search_box.on_change = search

    # إنشاء الديالوج
    dlg = AlertDialog(
        # modal=True,
        title=Text("بحث واختيار عميل",text_align="right"),
        content=Column([search_box, result_list],rtl=True, tight=True,scroll="auto"),
        actions=[],
        actions_alignment="end",
        scrollable="auto"
        
    )

    page.overlay.append(dlg)

    def open_client_search(e):
     
        page.dialog = dlg
        dlg.open = True
        page.update()
    ##################################



    #################################
    ########################
    search_box1 = TextField(label="بحث عن حساب",rtl=True,autofocus=True)
    result_list1 = Column()

    ##################################################
    def search1(e):
        data = get_re(f'{url}1/', 'SELECT * FROM sahm_q','', key)
        if data != None:
            clients=data
            search_text = search_box1.value
            result_list1.controls.clear()
            for c in clients:
                if search_text in c["name"]:
                    result_list1.controls.append(
                        ListTile(
                            leading=Text(c["id"],rtl=True,text_align="right"),
                            title=Text(""),
                            subtitle=Text(c["name"]),
                            on_click=lambda e, client=c: select_acauont1(client)
                        )
                    )
            result_list1.update()
        
    def select_acauont1(client):
        acount1_input.value = client["name"]
        acount1_id_input.value = client["id"]
        dlg1.open = False
        dialog_acaount1.open=True
        page.update()

    # ربط البحث بحقل البحث
    search_box1.on_change = search1

    # إنشاء الديالوج
    dlg1 = AlertDialog(
        # modal=True,
        title=Text("البحث عن حساب ",text_align="right"),
        content=Column([search_box1, result_list1],rtl=True, tight=True,scroll="auto"),
        actions=[],
        actions_alignment="end",
        scrollable="auto"
        
    )

    page.overlay.append(dlg1)

    def open_acaun1_search(e):
     
        page.dialog = dlg1
        dlg1.open = True
        page.update()
    search_box2 = TextField(label="بحث عن حساب",rtl=True,autofocus=True)
    result_list2 = Column()

    ##################################################
    def search2(e):
        data = get_re(f'{url}1/', 'SELECT * FROM sahm_q','', key)
        if data != None:
            clients=data
                # #print(li11)
            search_text = search_box2.value
            result_list2.controls.clear()
            for c in clients:
                if search_text in c["name"]:
                    result_list2.controls.append(
                        ListTile(
                            leading=Text(c["id"],rtl=True,text_align="right"),
                            title=Text(""),
                            subtitle=Text(c["name"]),
                            on_click=lambda e, client=c: select_acauont2(client)
                        )
                    )
            result_list2.update()
    
    def select_acauont2(client):
        acount2_input.value = client["name"]
        acount2_id_input.value = client["id"]
        dlg2.open = False
        dialog_acaount1.open=True
        # open_dialog_sahm("5")
        page.update()

    # ربط البحث بحقل البحث
    search_box2.on_change = search2

    # إنشاء الديالوج
    dlg2 = AlertDialog(
        # modal=True,
        title=Text("البحث عن حساب ",text_align="right"),
        content=Column([search_box2, result_list2],rtl=True, tight=True,scroll="auto"),
        actions=[],
        actions_alignment="end",
        scrollable="auto"
        
    )

    page.overlay.append(dlg2)

    def open_acaun1_search1(e):
     
        page.dialog = dlg2
        dlg2.open = True
        page.update()
    def get_mony_son():
        try:
            data = get_re(f'{url}3/', 'SELECT * from son_all_mony where id_son= ? ',f'{userid.value}', key)
            if data != None:
                li5=data
                #print(li5)
                for i in li5:
                    if str(i["id_amlah"])=="1":
                        #print(i["get_all_mony"])
                        x= float(i["get_all_mony"])
                        all_mony.value=f"{x:.2f}"
                    elif str(i["id_amlah"])=="2":
                        x= float(i["get_all_mony"])
                        #print(i["get_all_mony"]) 
                        all_mony1.value=f"{x:.2f}"
                    elif str(i["id_amlah"])=="3":
                        x= float(i["get_all_mony"])
                        all_mony2.value=f"{x:.2f}"
                        #print(i["get_all_mony"]) 
                page.update()   
        except:
            pass
        page.update()
    def ty(e):
        if str(direction_sahm.value)=="سهم":
            mony_sahm_input.visible=True
        else:
            mony_sahm_input.visible=False
        page.update()
    id_clint_sahm_input.visible=False
    
    dialog_sahm = AlertDialog(
        
        modal=True,
        
        title=Text("اضافة حساب", text_align=TextAlign.RIGHT),
        content=Container(
            height=300,
            content=Column([
             Row([
            # Text("رقم السند:", text_align=TextAlign.RIGHT),
            # Text(id.value, color="blue")
        ], alignment=MainAxisAlignment.END),
            # Text(now, text_align=TextAlign.RIGHT, color="blue"),
            # account_dropdown,
            # Container(content=Text(f"الرصيد له: {rseed3} ريـال", text_align=TextAlign.CENTER), bgcolor="orange"),
            dat_sahm_input,
            name_sahm_input,
            direction_sahm,
            mony_sahm_input,
            id_clint_sahm_input,
            sahm_new_not,
           
           
            # id,
            
        ], alignment=MainAxisAlignment.START, horizontal_alignment=CrossAxisAlignment.START,spacing=0,scroll="auto"),
        ),
        actions=[
            TextButton("إلغاء", on_click=lambda e: exit_dialog_sahm(e)),
            ElevatedButton("حفظ", on_click=lambda e: new_add_sahm(e)),
        ],
        actions_alignment=MainAxisAlignment.END,
        scrollable="auto",
    )
    acount1_input = TextField(label="من حساب ", on_focus=lambda x:open_acaun1_search(x),read_only=True,text_align=TextAlign.RIGHT,height=50)
    acount1_id_input = TextField(label="", text_align=TextAlign.RIGHT,height=50)
    acount2_input = TextField(label="الى حساب", on_focus=lambda x:open_acaun1_search1(x),read_only=True,text_align=TextAlign.RIGHT,height=50)
    acount2_id_input = TextField(label="اكتب البيان", text_align=TextAlign.RIGHT,height=50)
    acount_mony_input = TextField(label="ادخل المبلغ", text_align=TextAlign.CENTER,height=50,on_blur=lambda x:get_val(x),keyboard_type="number")
    acount_not_input = TextField(label="اكتب الملاحظات", text_align=TextAlign.RIGHT,height=50)
    acount1_id_input.visible=False
    acount2_id_input.visible=False
    dialog_acaount1 = AlertDialog(
        # width=400,
        # height=400,
        modal=True,
        
        title=Text("اضافة قيد", text_align=TextAlign.RIGHT),
        content=Container(
            # height=300,
            content=Column([
             
        acount1_input,
        acount1_id_input,
        acount2_input,
        acount2_id_input,
        acount_mony_input,
        amlah,
        acount_not_input,
            
        ], alignment=MainAxisAlignment.START, horizontal_alignment=CrossAxisAlignment.START,spacing=2,tight=True,scroll="auto"),
        ),
        actions=[
            TextButton("إلغاء", on_click=lambda e: exit_dialog_acount(e)),
            ElevatedButton("حفظ", on_click=lambda e: transfer_funds(e)),
        ],
        actions_alignment=MainAxisAlignment.END,scrollable="auto"
    )
    dialog_clints = AlertDialog(
        # width=400,
        # height=400,
        modal=True,
        
        title=Text("اضافة حساب", text_align=TextAlign.RIGHT),
        content=Container(
            # height=300,
            content=Column([
             
        clint_new_name
        ,clint_new_no_b
        ,clint_new_phone1
        ,clint_new_phone2
        ,clint_new_not
         
            # Text(now, text_align=TextAlign.RIGHT, color="blue"),
            # account_dropdown,
            # Container(content=Text(f"الرصيد له: {rseed3} ريـال", text_align=TextAlign.CENTER), bgcolor="orange"),
      
           
           
            # id,
            
        ], alignment=MainAxisAlignment.START, horizontal_alignment=CrossAxisAlignment.START,spacing=2,tight=True,scroll="auto"),
        ),
        actions=[
            TextButton("إلغاء", on_click=lambda e: exit_dialog_clint(e)),
            ElevatedButton("حفظ", on_click=lambda e: new_add_clint(e)),
        ],
        actions_alignment=MainAxisAlignment.END,scrollable="auto"
    )
    dialog99 = AlertDialog(
        # width=400,
        # height=400,
        modal=True,
        
        title=Text("سند جديد", text_align=TextAlign.RIGHT),
        content=Container(
           
            content=Column([
             Row([
        ], alignment=MainAxisAlignment.END),
            Text(now, text_align=TextAlign.RIGHT, color="blue"),
            amount_input,
            amlah,
            note_input,
            direction,
            
        ], alignment=MainAxisAlignment.START, horizontal_alignment=CrossAxisAlignment.START,spacing=0,tight=True,scroll="auto"),
        ),
        actions=[
            TextButton("إلغاء", on_click=lambda e: exit_dialog(e)),
            ElevatedButton("حفظ", on_click=lambda e: save1(e)),
        ],
        actions_alignment=MainAxisAlignment.END,scrollable="auto",
    )
    message = Text(size=14)
  
    new_type=Dropdown(
        label="نوع العملية",

        # width=175,
        options=[
            dropdown.Option(key="ايداع"),
            dropdown.Option(key="سحب"),
            dropdown.Option(key="تسليم سهم"),

        ],
        disabled=True,
    )
    new_type.value=new_type.options[0].key
    
    Cach=Dropdown(
        label="طرقة الدفع",
        on_change=lambda x:get_h(x),
        options=[
            dropdown.Option(key="نقداَ"),
            dropdown.Option(key="حوالة مالية"),

        ],
        # adaptive=True,
    
        width=175,     # ضبط العرض
           # لن تؤثر مباشرة على Dropdown، لكن نقدر نغلفه
    
    )
    op=0
    def open_dialog_acount(e):
   
        dialog_acaount1.open = True
        page.update()
    def exit_dialog_acount(e):
        dialog_acaount1.open = False
        page.update()
    
    def open_dialog_clint(e):
   
        dialog_clints.open = True
        page.update()
    def exit_dialog_clint(e):
        dialog_clints.open = False
        page.update()
    def open_dialog_sahm(e):
      
        dialog_sahm.open = True
        page.update()
    def exit_dialog_sahm(e):
        dialog_sahm.open = False
        page.update()
    def open_dialog(e):
        dialog99.open = True
        page.update()
    def exit_dialog(e):
        dialog99.open = False
        page.update()
    def get_aml(e):
        if str(Cach.value)=="حوالة مالية":
            no_hwala.visible=True
            op=1
        else:
            no_hwala.visible=False
            op=0
        page.update()
    def get_h(e):
        if str(Cach.value)=="حوالة مالية":
            no_hwala.visible=True
            op=1
        else:
            no_hwala.visible=False
            op=0
        page.update()
    Cach.value=Cach.options[0].key
    def combo(dr):
        return Container(
            # styled_dropdown = Container(
        content=dr,
        width=175,
        height=60,         # الآن نتحكم بالارتفاع
        padding=padding.only(left=5, right=5),
        bgcolor="#f5f5f5",
        border_radius=8,
        alignment=alignment.center,
        adaptive=True,
    )
    def combo1(dr):
        return Container(
            # styled_dropdown = Container(
        content=dr,
        padding=padding.only(left=5, right=5),
        bgcolor="#f5f5f5",
        border_radius=8,
        alignment=alignment.center,
        adaptive=True,
    )
    def login_page():
        return Container(
            content=Column(
                [
                    Row([
                        Image(src="/icons/logo.png",width=200,height=200,border_radius=150),

                    ],MainAxisAlignment.CENTER,spacing=0
                    ),
                    
                    Text("🔐 تسجيل الدخول", size=30, weight=FontWeight.BOLD, color="#093C69"),
                    username,
                    password,
                    Container(
            content=Column(
                [
                    # Image(src=icon_path, width=40, height=40),
                    Text("تسجيل الدخول", size=15, weight=FontWeight.BOLD, text_align=TextAlign.CENTER,color="white"),
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            width=int(username.width),
            # height=55,
            bgcolor="#093C69",
            border_radius=20,
            adaptive=True,
            padding=15,
            alignment=alignment.center,
            ink=True,
            on_click=login_click,
        ),
                    message
                ],
                alignment=MainAxisAlignment.CENTER,scroll="auto",
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
                # spacing=20
            ),
            padding=30,
            width=330,
            bgcolor="white",
            border_radius=20,
            shadow=BoxShadow(
                spread_radius=2,
                blur_radius=10,
                color=colors.GREY_400,
                offset=Offset(4, 4),
            ),
            alignment=alignment.center
        )
    def login_page1(a):
        return Container(
            content=a,
            # alignment="center",
            padding=5,
            # width=340,
            bgcolor="white",
            border_radius=20,
            shadow=BoxShadow(
                spread_radius=2,
                blur_radius=10,
                color=colors.GREY_400,
                offset=Offset(4, 4),
            ),
            alignment=alignment.center
        )
    def login_page5(a):
        return Container(
            content=a,
            # alignment="center",
            padding=5,
            width=360,
            height=600,
            bgcolor="white",
            border_radius=20,
            shadow=BoxShadow(
                spread_radius=2,
                blur_radius=10,
                color=colors.GREY_400,
                offset=Offset(4, 4),
            ),
            alignment=alignment.center
        )
    def create_text():
        return Container(
            content=Column(
                [
                    info,
                    Row([
                        info_id,id,
                    ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                    Row([
                        info_name,names
                    ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                    # Row([
                    #     names
                    # ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                    Row([
                        info_type,type_name
                    ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                    Row([
                        info_moto,moto
                    ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                    Row([
                        info_get_mony,get_mony
                    ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                    Row([
                        Text(""),
                    ],MainAxisAlignment.CENTER,spacing=5,rtl=True),
                    Column(
                [
                  
                    ],spacing=0)
                ],
                alignment=MainAxisAlignment.CENTER,spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            width=340,
            border_radius=20,
            padding=2,
            alignment=alignment.center,
            ink=True,
           
        )
    dialog1 = AlertDialog(
       
        content=
                  
                    create_text(),
                       
                   
        
       # actions_alignment=MainAxisAlignment.END
    )
    def create_button(icon_path, text,cmd):
        return Container(
            content=Column(
                [
                    Image(src=icon_path, width=40, height=40),
                    Text(text, size=10, weight=FontWeight.BOLD, text_align=TextAlign.CENTER,color="white"),
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            width=100,
            height=80,
            bgcolor="#093C69",
            border_radius=20,
            padding=0,
            alignment=alignment.center,
            ink=True,
            on_click=cmd,
            adaptive=True,
        )
    def create_button2(icon_path, text,text1,bg):
        return Container(
            content=Column(
                [
                    Image(src=icon_path, width=40, height=40),
                    Text(text, size=12, weight=FontWeight.BOLD, text_align=TextAlign.CENTER,color="white"),
                    Text(text1, size=18, weight=FontWeight.BOLD, text_align=TextAlign.CENTER,color="white"),
                ],
                alignment=MainAxisAlignment.CENTER,spacing=1,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            width=320,
            height=100,
            bgcolor=bg,
            border_radius=20,
            padding=15,
            alignment=alignment.center,
            ink=True,
            adaptive=True,
            
        )
    def on_back_pressed(e):
        if len(page.views) > 1:
            page.views.pop()
            page.update()
        else:
            page.window_close() 

            # def on_back_pressed(e):
    #     if len(page.views) > 1:
    #         page.views.pop()
    #         page.update()
    #     else:
    #         page.window_close() 
    page.on_back = on_back_pressed
    def create_button3(icon_path, text,cmd,x,y):
        return Container(
            content=Column(
                [
                    Image(src=icon_path, width=40, height=40),
                    Text(text, size=10, weight=FontWeight.BOLD, text_align=TextAlign.CENTER,color="white"),
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            width=x,
            height=y,
            bgcolor="#093C69",
            border_radius=20,
            padding=15,
            alignment=alignment.center,
            ink=True,
            on_click=cmd,
            adaptive=True,
        )
    def create_text_clint():
        return Container(
            content=Column(
                [
                    
                    Row([
                       clint_info,
                    ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                   Row([
                        clint_new_name_l,clint_new_name
                    ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                    Row([
                        clint_new_no_b_l,clint_new_no_b
                    ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                    Row([
                        clint_new_phon1_l,clint_new_phone1
                    ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                    Row([
                        clint_new_phon2_l,clint_new_phone2
                    ],MainAxisAlignment.CENTER,spacing=0,rtl=True),
                    Row([
                        Text(""),
                    ],MainAxisAlignment.CENTER,spacing=5,rtl=True),
                    Row([
                        ElevatedButton(
                        text="اضافة",
                        on_click=lambda x: new_add_clint(x),
                        bgcolor="#093C69",
                        color="white",
                        width=int(username.width),
                        style=ButtonStyle(
                            shape=RoundedRectangleBorder(radius=12),
                            padding=20
                        )),
                    ],MainAxisAlignment.CENTER,spacing=5,rtl=True),
         
                ],spacing=0

            ),
            width=340,
     
            border_radius=20,
            padding=2,
            alignment=alignment.center,
            ink=True,
           
        )
    save_status=Text()
    def handle_save(event: FilePickerResultEvent):
        try:
            if event.path:
                # إنشاء محتوى الملف
                content = "هذا ملف تجريبي/nتم إنشاؤه بواسطة Flet!"
                
                # الكتابة إلى الملف
                with open(event.path, "w", encoding="utf-8") as f:
                    f.write(content)
                
                save_status.value = f"✅ تم الحفظ بنجاح في:/n{event.path}"
                save_status.color = colors.GREEN
                page.update()
            else:
                save_status.value = "⚠️ تم إلغاء العملية"
                save_status.color = colors.ORANGE
        except PermissionError:
            save_status.value = "❌ خطأ: لا يوجد صلاحية للكتابة في هذا المسار"
            save_status.color = colors.RED
        except Exception as e:
            save_status.value = f"❌ خطأ غير متوقع: {str(e)}"
            save_status.color = colors.RED
        finally:
            page.update()

        page.update()
    
    # إنشاء FilePicker لحفظ الملفات
    pdf_path = "E:/my_app/الجمعية_هاتف/new_app/src/statement.pdf"  # أو حسب المكان الذي تحفظ فيه الملف

    # def share_file(e):
    #     if os.path.exists(pdf_path):
    #         message = "مرحبًا، هذا رابط الملف المطلوب 📎"
    #         file_url = "https://yourserver.com/files/myfile.pdf"  # يجب رفع الملف إلى الإنترنت

    #         # توليد رابط واتساب
    #         url = f"https://wa.me/?text={urllib.parse.quote(message + ' ' + file_url)}"
    #         page.launch_url(url)
    #         page.update()
    #     else:
    #         #print("الملف غير موجود")
    #         # page.snack_bar = SnackBar(Text("❌ الملف غير موجود"))
    #         # page.snack_bar.open = True
    #         # page.update()
    file_picker = FilePicker()
    output_file=""
    def save_file_result(e: FilePickerResultEvent):
        if e.path:
            #print(f"📁 تم تحديد المسار: {e.path}")
            # يمكنك الآن استخدام e.path لحفظ الملف بهذا المسار
            page.snack_bar = SnackBar(Text(f"سيتم الحفظ في: {e.path}"))
            output_file=str(e.path)
            page.snack_bar.open = True
            
            page.update()
        return output_file

    file_picker.on_result = save_file_result
    page.overlay.append(file_picker)
    
    def build_row(row_data, current_balance):
        # global row_data
        return Row([
            Row([
                # get_kaid(g,d_g,k_g,name_g,bian2_g,aml_g,str_mony_g,mony_g,not1_g)
                IconButton(icons.DELETE_OUTLINE,on_click=lambda e: get_kaid(row_data["id"],row_data["dat"],row_data["no_s"],row_data["bian2"],row_data["na_amlah"],row_data["str_mony"],row_data["mony"],row_data["not1"]),
                           
        
        ),
        #  IconButton(icons.SHARE_OUTLINED,on_click=lambda e: share_file(e),),
                Text(str(row_data["id"]), color="red", size=10),
            ],  expand=1),
            Text(
                f"{current_balance}",
                text_align=TextAlign.LEFT,
                expand=1,
                max_lines=1,
                size=10,
                
            ),
            
            Column([
                Text(row_data["bian2"], text_align=TextAlign.CENTER, size=10),
                Text(row_data["dat"].split("T")[0], color="blue", size=10, text_align=TextAlign.RIGHT),
            ], expand=2, alignment=MainAxisAlignment.END),
            Text(
                f"{row_data['mony']:,.2f}",
                color="green" if row_data["bian"] == "ايداع" else "red",
                text_align=TextAlign.RIGHT,
                expand=1,
                max_lines=1,
                size=12,
            ),
            Text(
                row_data["bian"],
                color="green" if row_data["bian"] == "ايداع" else "red",
                text_align=TextAlign.RIGHT,
                expand=1,
                max_lines=1,
                size=12,
            ),
        ],
        alignment=MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=CrossAxisAlignment.CENTER,
        spacing=5,
        )

    table_header = Row([
        Text("العملة", weight="bold", width=100,expand=1, text_align=TextAlign.RIGHT),
        Text("التفاصيل", weight="bold", expand=1, text_align=TextAlign.RIGHT),
        Text("المبلغ", weight="bold", width=100,expand=1, text_align=TextAlign.RIGHT),
        Text("النوع", weight="bold", width=50,expand=1, text_align=TextAlign.RIGHT),
    ],alignment=MainAxisAlignment.SPACE_BETWEEN, spacing=8)
    def add_clients(e):
        global table_rows
        global bottom_bar
        # global table_header
        data = get_re(f'{url}3/', 'SELECT bian,mony,bian2,id,rseed,dat,id_amlah,na_amlah,no_s,str_mony,name,not1 FROM move_q where no_s= ?',f'{id.value}', key)
        # create_customer_statement("customer_name", data, output_file, r"E:/my_app/الجمعية_هاتف/new_app/src/assets/icon.png")
        if data != None:
            li11=data
            # #print(li11)
            rseed1_Y.value=0.00
            rseed2_S.value=0.00
            rseed3_D.value=0.00
            rseed1_Y1.value=0.00
            rseed2_S1.value=0.00
            rseed3_D1.value=0.00
            all_Y.value=0.00
            all_S.value=0.00
            all_D.value=0.00
            list_t_sahm.controls.clear()
            list_t_sahm1.controls.clear()
            list_t_sahm2.controls.clear()
            current_balance = 0  # الرصيد يبدأ من صفر
            table_rows = []
            #print(li11)
            for r in li11:
            
                if str(r["bian"]) == "ايداع":
                    current_balance = r["na_amlah"]
                    if int(int(r["id_amlah"]))==1:
                        rseed1_Y.value+=float(r["mony"])
                    elif int(r["id_amlah"])==2:
                        rseed2_S.value+=float(r["mony"])
                    elif int(r["id_amlah"])==3:
                        rseed3_D.value+=float(r["mony"])
                elif str(r["bian"]) == "سحب":
                    current_balance = r["na_amlah"]
                    if int(r["id_amlah"])==1:
                        rseed1_Y1.value+=float(r["mony"])
                    elif int(r["id_amlah"])==2:
                        rseed2_S1.value+=float(r["mony"])
                    elif int(r["id_amlah"])==3:
                        rseed3_D1.value+=float(r["mony"])
                    # rseed2.value+=float(r["mony"])
                    if float(rseed1_Y1.value)>=0:
                        all_Y.value=float(rseed1_Y.value)-float(rseed1_Y1.value)
                    else:
                        all_Y.value=float(rseed1_Y.value)
                    if float(rseed2_S1.value)>=0:
                        all_S.value=float(rseed2_S.value)-float(rseed2_S1.value)
                    else:
                        all_S.value=float(rseed2_S.value)
                    if float(rseed3_D1.value)>=0:
                        all_D.value=float(rseed3_D.value)-float(rseed3_D1.value)
                    else:
                        all_D.value=float(rseed3_D.value)
                    # all_S.value=float(rseed2_S.value)-float(rseed2_S1.value)
                    # all_D.value=float(rseed3_D.value)-float(rseed3_D1.value)

                # rseed3.value=rseed1.value-rseed2.value
                    bottom_bar = Container(
                                content=Column([
                                    Row([
                                        Text("ريال يمني",color="white",text_align=TextAlign.CENTER,size=12),
                                        Text(f"عليه: {rseed1_Y1.value:,.2f} : له {rseed1_Y.value:,.2f} : الرصيد : {all_Y.value:,.2f}",color="white",text_align=TextAlign.CENTER,size=12,),
                                        
                                    ],spacing=5,expand=1,alignment=MainAxisAlignment.CENTER),
                                    Row([
                                        Text("ريال سعودي",color="white",text_align=TextAlign.CENTER,size=12),
                                        Text(f"عليه: {rseed2_S1.value:,.2f} : له {rseed2_S.value:,.2f} : الرصيد : {all_S.value:,.2f}",color="white",text_align=TextAlign.CENTER,size=12,),
                                        

                                    ],spacing=5,expand=1,alignment=MainAxisAlignment.CENTER),
                                    Row([
                                        Text("دولار امريكي",color="white",text_align=TextAlign.CENTER,size=12),
                                        Text(f"عليه: {rseed3_D1.value:,.2f} : له {rseed3_D.value:,.2f} : الرصيد : {all_D.value:,.2f}",color="white",text_align=TextAlign.CENTER,size=12,),
                                                
                                                ],spacing=5,expand=1,alignment=MainAxisAlignment.CENTER),
                                                ],spacing=5),
                                    # color="white",
                                    # text_align=TextAlign.RIGHT
                                # ),
                                    bgcolor="#093C69",
                                    padding=5,
                                    alignment=alignment.top_right,
                                    # height=50
                                        )
                # page.update
                
                table_rows.append(build_row(r, current_balance))
    
        list_t_sahm1.controls.append(table_header)
        list_t_sahm.controls.extend(table_rows)
        try:

            list_t_sahm2.controls.append(bottom_bar)
        except Exception as ex:
            bottom_bar = Container(
                        content=Text(f"عليه: 0 : له 0 : الرصيد له: 0",
                            color="white",
                            text_align=TextAlign.RIGHT
                        ),
                        bgcolor="#093C69",
                        padding=10,
                        alignment=alignment.center_right,
                        height=50
                    )

        page.update()

    def login_click(e):
        try:  

            data = get_re(f'{url}1/','SELECT * FROM sond',f'', key)
            # v=data.json()
            #print(data)
            for i in data:
                    if str(username.value.strip())==str(i["USNAME"]) and str(password.value.strip())==str(i["USPASS"]):
                        userid.value= int(i["no"])
                        page.go("/main")
                        page.update()

                        #print(userid.value)
                        break
                    else:
                        message.value = "❌ اسم المستخدم أو كلمة المرور غير صحيحة"
                        message.color = "red"
        except Exception as ex:
            message.value = f"⚠️ خطأ في الاتصال: {ex}"
            message.color = "red"

        page.update()
    text_search=TextField(label="بحث بالاسم",text_align="right",
                    height=40,bgcolor="gray",border_radius=30,border_color="#093C69",rtl=True,width=280,text_vertical_align=-1.5,on_submit=lambda x:search_items(x),)
    
    text_search1=TextField(label="بحث بالاسم",text_align="right",
                    height=40,bgcolor="gray",border_radius=30,border_color="#093C69",rtl=True,width=280,text_vertical_align=-1.5,on_submit=lambda x:search_items1(x),
                
                    )

    def on_click_item_sahm(e, text):
        k=str(text).split("*")
        clint_id.value=k[0]
        SAHM_new_name.value=k[1]

        page.update()
    def on_click_item(e, text):
        #print(str(text))

        k=str(text).split("*")
        id.value=k[0]
        names.value=k[1]
        type_name.value=k[2]
        moto.value=k[3]
        get_mony.value=k[4]
        add_clients("x")
        page.go("/t_sahm")
        page.update()
    def get_t_sahm(e):
        # try:
            pdf_file_url = "file:///path/to/your/file.pdf"  # غيّره لمسار ملفك

        # page.add(
        #     Text("عرض ملف PDF"),
            e.IFrame(src=pdf_file_url, width=800, height=600)
            # )
            # data =  get_re(f'{url}/3', 'SELECT * FROM sahm_q1','', key)
            # file_path = "/path/to/your/file.pdf"

            # os.startfile(file_path)  
        # except:
        #     pass


    def search_items(e):
        global li
        li = []
        if text_search.value!="":
            list1.controls.clear()
            try:
           
                data =  get_re(f'{url}1/', 'SELECT * FROM sahm_q1','', key)
                li=data
                # if data.status_code == 200:
                #     li=data.json()
                    # #print()    
            except:
                ac=AlertDialog(
                    title=Text("لايوجد اتصال بالسيرفر",size=13),

                    actions_alignment=MainAxisAlignment.CENTER,
                )
                page.overlay.append(ac)
                ac.open=True
                page.update()
            

            search_query = text_search.value.lower()
            for item_data in li:
                try:
                    if search_query in item_data["name"]:
                        item = ListTile(
                            leading=Icon(icons.PERSON_ROUNDED,color="white",size=40),
                            title=Text(str(item_data["id"])+" - "+str(item_data["name"]),text_align="right",color="white"),
                            subtitle=Text("YR "+str(item_data["get_mony"]),text_align="left",color=colors.YELLOW_400,size=22),bgcolor ="#093C69"
                     
                        )
                        x=str(item_data["id"])+"*"+str(item_data["name"])+"*"+str(item_data["type_name"])+"*"+str(item_data["moto"])+"*"+str(item_data["get_mony"])
                        item.on_click = lambda e, text=x:on_click_item(e, text)
                        item.rtl=True
                        list1.controls.append(item)
                        # page.update()

                except:
                    pass
            page.update()
    def search_items_sahm(e):
        li11 = []
        if text_search4.value!="":
            list4.controls.clear()
            # try:
        
            data = get_re(f'{url}1/', 'SELECT * FROM sahm_q','', key)
            if data != None:
                li11=data
                search_query = text_search4.value.lower()
                for item_data in li11:
                    date_str = str(item_data["dat_end1"])
                    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
                    formatted_date = date_obj.strftime("%d-%m-%Y")
                    # #print(formatted_date)
                
                    try:
                        if search_query in item_data["name"]:
                            item = ListTile(
                                title=ListTile(leading=Icon(icons.PERSON_ROUNDED,color="white",size=20),title=Text(str(item_data["id"])+" - "+str(item_data["name"]),text_align="right",color="white",size=12),bgcolor ="#093C69"),
                                subtitle=ListTile(title=Text(str("نوع الحساب")+" "+str(item_data["type_name"])+"                  "+str("الانتهاء")+" "+str(formatted_date),text_align="right",color="red"),subtitle=Text("YR "+str(item_data["get_mony"]),text_align="left",color=colors.YELLOW_400,size=20),bgcolor ="#093C69"),bgcolor ="#093C69"
                        
                            )
                            x=str(item_data["id"])+"*"+str(item_data["name"])+"*"+str(item_data["type_name"])+"*"+str(item_data["moto"])+"*"+str(item_data["get_mony"])+"*"+str(formatted_date)
                            item.on_click = lambda e, text=x:on_click_item(e, text)
                            item.rtl=True
                            list4.controls.append(item)
                            # page.update()

                    except:
                        pass
            page.update()

    text_search4=TextField(label="بحث بالاسم",text_align="right",
                    height=45,bgcolor="gray",border_radius=20,border_color="#093C69",rtl=True,width=265,text_vertical_align=-1.5,on_submit=lambda x:search_items_sahm(x),
                
                    )
    xx=create_text_clint()
    xx.visible=False
    def search_items1(e):
        global li1
        li1 = []
        if text_search1.value!="":
            list2.controls.clear()
            try:
                data = get_re(f'{url}3/', 'SELECT * from moving_q_day WHERE id_son= ? ',f'{userid.value}', key)
                if data != None:
                    li1=data
                    # #print(li1)    
            except:
                ac=AlertDialog(
                    title=Text("لايوجد اتصال بالسيرفر",size=13),

                    actions_alignment=MainAxisAlignment.CENTER,
                )
                page.overlay.append(ac)
                ac.open=True
                page.update()
            

            search_query = text_search1.value.lower()
            for item_data in li1:
                try:
                    if search_query in item_data["type"]:
                        item = ListTile(
                            leading=Icon(icons.PERSON_ROUNDED,color="white",size=40),
                            title=Text(str(item_data["id_s"])+" - "+str(item_data["type"]),text_align="right",color="white"),
                            subtitle=Text("YR "+str(item_data["mony"]),text_align="left",color=colors.YELLOW_400,size=22),bgcolor ="#093C69"
                     
                        )
                        x=str(item_data["id_s"])+"*"+str(item_data["type"])+"*"+str(item_data["dat"])+"*"+str(item_data["bian2"])+"*"+str(item_data["dat"])+"*"+str(item_data["na_amlah"])+"*"+str(item_data["MOVE_ID"])
                        # item.on_click = lambda e, text=x:on_click_item(e, text)
                        item.rtl=True
                        list2.controls.append(item)
                        # page.update()

                except:
                    pass
            page.update()

    

    def search_items_clint(e):
        li11 = []
        if text_search3.value!="":
            list3.controls.clear()
            # try:
            data = get_re(f'{url}1/', 'SELECT * FROM CLIENTS',f'', key)
            if data != None:
                li11=data
            search_query = text_search3.value.lower()
            for item_data in li11:
                try:
                    if search_query in item_data["CLIENT_NAME"]:
                        item = ListTile(
                            leading=Icon(icons.PERSON_ROUNDED,color="white",size=40),
                            title=Text(str(item_data["ID"])+" - "+str(item_data["CLIENT_NAME"]),text_align="right",color="white"),
                            subtitle=Text(str(item_data["phone1"]),text_align="left",color=colors.YELLOW_400,size=22),bgcolor ="#093C69"
                     
                        )
                        x=str(item_data["ID"])+"*"+str(item_data["CLIENT_NAME"])+"*"+str(item_data["phone1"])+"*"+str(item_data["phone2"])+"*"+str(item_data["CLIENT_NO_B"])
                        item.on_click = lambda e, text=x:on_click_item_sahm(e, text)
                        item.rtl=True
                        list3.controls.append(item)
                        # page.update()

                except:
                    pass
            page.update()
    text_search3=TextField(label="بحث بالاسم",text_align="right",
                    height=45,bgcolor="gray",border_radius=20,border_color="#093C69",rtl=True,width=265,text_vertical_align=-1.5,on_submit=lambda x:search_items_clint(x),
                
                    )
    def search_items_sdad(e):
        global li1
        li1 = []
        # if text_search1.value!="":
        list2.controls.clear()
        try:
            data = get_re(f'{url}3/', 'SELECT * from moving_q_day WHERE id_son= ? ',f'{userid.value}', key)
            li1=data
            #print(li1)    
        except:
            ac=AlertDialog(
                title=Text("لايوجد اتصال بالسيرفر",size=13),

                actions_alignment=MainAxisAlignment.CENTER,
            )
            page.overlay.append(ac)
            ac.open=True
            page.update()
        

        # search_query = text_search1.value.lower()
        for item_data in li1:
            try:
                # if search_query in item_data["type"]:
                item = ListTile(
                    leading=Icon(icons.PERSON_ROUNDED,color="white",size=40),
                    title=Text(str(item_data["id_s"])+" - "+str(item_data["type"]),text_align="right",color="white"),
                    subtitle=Text("YR "+str(item_data["mony"]),text_align="left",color=colors.YELLOW_400,size=22),bgcolor ="#093C69"
                
                )
                x=str(item_data["id_s"])+"*"+str(item_data["type"])+"*"+str(item_data["dat"])+"*"+str(item_data["bian2"])+"*"+str(item_data["dat"])+"*"+str(item_data["na_amlah"])+"*"+str(item_data["MOVE_ID"])
                # item.on_click = lambda e, text=x:on_click_item(e, text)
                item.rtl=True
                list2.controls.append(item)
                # page.update()

            except:
                pass
        page.update()
    g_dat=TextField("",text_align="center",multiline=False, text_size=10,border_width=0,)
    g_k=TextField("",text_align="center",multiline=False, text_size=10,border_width=0,)
    g_id=TextField("",text_align="center",multiline=False, text_size=10,border_width=0,)
    g_name=TextField("",text_align="center",multiline=False, text_size=10,border_width=0,)
    g_bian2=TextField("",text_align="center",multiline=False, text_size=10,border_width=0,)
    g_aml=TextField("",text_align="center",multiline=False, text_size=10,border_width=0,)
    g_str_mony=TextField("",text_align="center",multiline=False, text_size=10,border_width=0,)
    g_not1=TextField("",text_align="center",multiline=False, text_size=10,border_width=0,)
    g_mony=TextField("",text_align="center",multiline=False, text_size=10,border_width=0,)
    def get_kaid(g,d_g,k_g,bian2_g,aml_g,str_mony_g,mony_g,not1_g):
    #    row_data["id"],row_data["dat"],row_data["no_s"],names.value,row_data["bian2"],row_data["na_amlah"],row_data["str_mony"],row_data["mony"],row_data["not1"] 
        # global g_dat,g_k,g_id,g_name,g_bian2,g_aml,g_aml,g_str_mony,g_not1,g_mony
        # #print(g)
        # for i in g:
        #     #print(i)
        g_dat.value=d_g
        # # g_dat.update()
        g_k.value=k_g
        g_id.value=g
        # g_id.update()
        g_name.value=names.value
        g_bian2.value=bian2_g
        g_aml.value=aml_g
        g_str_mony.value=str_mony_g
        g_not1.value=not1_g
        g_mony.value=mony_g
        page.update()
        # #print(g_mony)
        page.go("/PDF")
        page.update()
        # #print(str(g_id.width),"*********************",str(g_id.height))
        
    #شاشة الاشهار
    content_container = Container(
        content=Column([
            Container(
                content=Column([

                    Row([ 
                    Column([Image(src="icons/trwis.png",expand=1)

                    ], expand=2, alignment=MainAxisAlignment.START), ]),

  
                ], alignment=MainAxisAlignment.CENTER),
                padding=5
            ),

            Divider(thickness=1),

            ResponsiveRow([
                Column([
                    Container(
                        content=Text("التاريخ", text_align="center", size=10),
                        bgcolor=colors.RED_100,
                        alignment=alignment.center,
                        padding=4
                    ),
                    Container(
                        content=g_dat,
                        border=border.all(1),
                        height=25,
                        alignment=alignment.center,
                        padding=4

                    )
                ], col=6,rtl=True),

                Column([
                    Container(
                        content=Text("رقم القيد", text_align="center", size=10),
                        bgcolor=colors.RED_100,
                        alignment=alignment.center,
                        padding=4
                    ),
                    Container(
                        content=g_id,
                        border=border.all(1),
                        height=25,
                        alignment=alignment.center,
                        padding=4
                    )
                ], col=6),
            ], spacing=5, run_spacing=5),

            Container(
                content=Text("اشعار سداد", size=14, weight="bold", color=colors.WHITE, text_align="center"),
                bgcolor=colors.BLUE_900,
                padding=8,
                alignment=alignment.center,
                border_radius=border_radius.all(5),
                margin=margin.symmetric(vertical=10)
            ),

            Column([
                Row([
                    
                    Container(Text("عميلنا", size=10, text_align="center"), border=border.all(1), expand=0, padding=4),
                    Container(g_name, border=border.all(1),height=25, expand=4, padding=4),
                    Container(Text("رقم الحساب", size=10, text_align="center"), border=border.all(1), expand=0, padding=4),
                    Container(g_k, border=border.all(1),height=25, expand=1, padding=4),
                   
                ], spacing=0,rtl=True),

                Row([
                    Container(Text("البيان", weight="bold", size=10, text_align="center"), border=border.all(1), expand=1, padding=4),
                ], spacing=0),

                Row([
                    Container(g_bian2, border=border.all(1),height=25, expand=1, padding=4),
                ], spacing=0),

                Row([
                    Container(Text("تم إيداع المبلغ في حسابكم", size=10, text_align="center"), border=border.all(1), expand=1, padding=4),
                ], spacing=0),

                Row([
                    Container(Text("العملة", size=10, text_align="center"), border=border.all(1), expand=0, padding=4),
                    Container(g_aml, border=border.all(1),height=25, expand=1, padding=4),
                    Container(Text("المبلغ", size=10, text_align="center"), border=border.all(1), expand=0, padding=4),
                    Container(g_mony, border=border.all(1),height=25, expand=2, padding=4),
                ], spacing=0,rtl=True),

                Row([
                    Container(Text("المبلغ بالحروف", size=10, text_align="center"), border=border.all(1), expand=1, padding=4),
                    Container(g_str_mony, border=border.all(1),height=25, expand=3, padding=4),
                ], spacing=0,rtl=True),

                Row([
                    Container(Text("ملاحظات", weight="bold", size=10, text_align="center"), border=border.all(1), expand=1, padding=4),
                ], spacing=0),

                Container(g_not1,height=50, border=border.all(1))
            ], spacing=4, alignment=MainAxisAlignment.CENTER),

            Row([
                Text("Sunday, April 06, 2025", size=10, italic=True),
                Text("Page 1 of 1", size=10, text_align="right", expand=True)
            ], alignment=MainAxisAlignment.SPACE_BETWEEN, )

        ], spacing=8),
        padding=8,
        border_radius=border_radius.all(8),
        bgcolor=colors.WHITE,
        expand=True
    )
    # def get_kaid(e,g):
    #     global g_dat,g_k,g_id,g_name,g_bian2,g_aml,g_aml,g_str_mony,g_not1,g_mony
    #     #print(g)
    #     for i in g:
    #         #print(i)
    #     g_dat=g["dat"]
    #     g_k=g["id"]
    #     g_id=g["no_s"]
    #     g_name=names.value
    #     g_bian2=g["bian2"]
    #     g_aml=g["na_amlah"]
    #     g_str_mony=g["str_mony"]
    #     g_not1=g["not1"]
    #     g_mony=g["mony"]
    #     #print(g_mony)
    #     page.go("/PDF")
    #     page.update()
#         bian
# mony
# bian2
# id
# rseed
# dat
# id_amlah
# na_amlah



    def routes_Change(route):
        page.views.clear()
  
        page.views.append(
            View(
                "/",
                [

                    Row(
                        [
                        login_page()
                        
                    
                    ],MainAxisAlignment.CENTER, expand=True
                    )
                    # ,BottomAppBar(Text("M-Soft    برنامج تسديد الفواتير",text_align="right",color="white",size=12),height=40,bgcolor="#093C69",)

                ]

            )

        )
        

        if page.route=="/main":
            page.views.clear()
            get_mony_son()
            page.views.append(
                View(
                    "/main",
                    [
                        AppBar(
                        title=Text("الرئيسية"),
                        center_title=True,
                        color="white",
                        bgcolor="#093C69",
                        leading=IconButton(icons.HOME)

                        ),
                        
                        Column([
                         login_page5(Column([
                             Column([
                           
                                    Row([
                            create_button2("/icons/Refund.png","ريال يمني" ,all_mony.value,"#093C69"),

                        ],MainAxisAlignment.CENTER,rtl=True,spacing=0,),
                        Row([
                            create_button2("/icons/Refund.png","ريال سعودي" ,all_mony1.value,"#393A69"),

                        ],MainAxisAlignment.CENTER,rtl=True,spacing=0,),
                        Row([
                            create_button2("/icons/Refund.png","دولار",all_mony2.value,"#593B69"),

                        ],MainAxisAlignment.CENTER,rtl=True,spacing=0,),
                        
                             ],horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=3),
                        Row([
                            create_button("/icons/Search Client.png", "العملاء",lambda e: page.go("/add_new")),
                            create_button("/icons/Cash.png", "الحسابات",lambda e: page.go("/add_sahm")),
                            create_button("/icons/Cash.png", "التحصيل اليومي",lambda e:page.go("/thsil")),
                            # ElevatedButton("ov,[]",on_click=lambda e:os_exit())
                        ],MainAxisAlignment.CENTER,rtl=True,spacing=15,),
                        Row([
                            # create_button("/icons/PowerOffButton.png", "خروج",lambda e:close(e)),
             
                        ],MainAxisAlignment.CENTER,rtl=True,spacing=15,),
                        # userid,



                         ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=10))      


                        ],MainAxisAlignment.CENTER, expand=True  )
             

        
                    ],vertical_alignment="center",horizontal_alignment="center"
                
            )
        )
        if page.route=="/add_new":
            page.views.clear()
            page.views.append(
                View(
                    "/add_new",
                    [
                        AppBar(
                        title=Text("اضافة عميل"),
                        center_title=True,
                        color="white",
                        bgcolor="#093C69",
                        leading=IconButton(icons.ARROW_BACK,on_click=lambda x:page.go("/main")),
                       

                        ),
           
                        
                        
                        Row([
                            login_page1(Column(

                            # [
                            #     Column(
                [
                   
            # ),
                                Row([
                                    # IconButton(icons.ADD ,on_click=lambda x:open_dialog_sahm(x),bgcolor="#093C69",icon_color="white",icon_size=20),
                    IconButton(icons.ADD ,on_click=lambda x:open_dialog_clint(x),icon_size=20,icon_color= "white",bgcolor="#093C69"),
                                    text_search3,

                                ],alignment=MainAxisAlignment.CENTER                  
                                        
                                    ),
                            ],
                        
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
                            )),
                            
                    
                        ],MainAxisAlignment.CENTER
                        ),
                        Row([
                            xx

                        ]),
                       
                      
                
                        list3,
                        dialog1,
                        dialog_clints,
  
        
                    ],vertical_alignment="center",horizontal_alignment="center"
                
            )
       )
        if page.route=="/add_sahm":
            page.views.clear()
            list4.controls.clear
            text_search4.value=""
            page.views.append(
                View(
                    "/add_sahm",
                    [
                        AppBar(
                        title=Text("الحسابات"),
                        center_title=True,
                        color="white",
                        bgcolor="#093C69",
                        leading=IconButton(icons.ARROW_BACK,on_click=lambda x:page.go("/main")),
                       

                        ),
       
                        
                        Row([
                            login_page1(Column(

                 
                [
                   Row([Container(
            content=Row(
                [
                    Text("اضافة قيد بسيط", size=15, weight=FontWeight.BOLD, text_align=TextAlign.CENTER,color="white",width=300),
                ],alignment=MainAxisAlignment.CENTER,expand=True
                
            ),
            expand=1,
            height=60,
            bgcolor="#093C69",
            border_radius=20,
            # adaptive=True,
            padding=10,
            alignment=alignment.center,
            ink=True,
            on_click= lambda e:open_dialog_acount(e),
        ),
                       
                   ]),
       
                                Row([
       
                    IconButton(icons.ADD ,on_click=lambda x:open_dialog_sahm(x),bgcolor="#093C69",icon_color="white",icon_size=20),
                                    text_search4,

                                ],alignment=MainAxisAlignment.CENTER                  
                                        
                                    ),
                            ],
                        
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=10
                            )),
                            
                    
                        ],MainAxisAlignment.CENTER
                        ),
                        Row([
                            xx

                        ]),
                       
                      
                
                        list4,
                        dialog1,
                       dialog_sahm,
                       dialog_acaount1,
            
                     
        
                    ],vertical_alignment="center",horizontal_alignment="center"
                
            )
       )
       
        if page.route=="/t_sahm":
            page.views.clear()
            # #print(SAHM_id.value)
            page.views.append(
                View(
                    "/t_sahm",
                    [
                        AppBar(
                        title=Text(names.value),
                        center_title=True,
                        color="white",
                        bgcolor="#093C69",
                        leading=IconButton(icons.ARROW_BACK,on_click=lambda x:page.go("/add_sahm")),
                        # bgcolor=colors.RED,

                        ),
                        
                             
                             
            #             Row([Container(
            # content=Column(
            #     [
        #             Row(
                            
        #                         [
        #                             Text("من", size=12, weight=FontWeight.BOLD, text_align=TextAlign.CENTER,color="#093C69"),
        #                             IconButton(icon=Icons.CALENDAR_MONTH,icon_color="#093C69",on_click=lambda x:page.open(
        #         DatePicker(
        #             first_date=datetime.datetime(year=2023, month=1, day=1),
        #             last_date=datetime.datetime(year=2034, month=1, day=1),
        #             on_change=handle_change,
        #             on_dismiss=handle_dismissal,
        #         )
        #     ),
        #     ),
        # dat11,
        # Text("الى", size=12, weight=FontWeight.BOLD, text_align=TextAlign.CENTER,color="#093C69"),
        # IconButton(icon=Icons.CALENDAR_MONTH,icon_color="#093C69",on_click=lambda x:page.open(
        #         DatePicker(
        #             first_date=datetime.datetime(year=2023, month=1, day=1),
        #             last_date=datetime.datetime(year=2034, month=1, day=1),
        #             on_change=handle_change1,
        #             on_dismiss=handle_dismissal1,
        #         )
        #     ),
        #     ),
        #  dat2,
        #                      ],alignment=MainAxisAlignment.CENTER,rtl=True,spacing=0,tight=True,
        #                      ),
        #             Row([
        #                  Text("طباعة كشف حساب", size=15, weight=FontWeight.BOLD, text_align=TextAlign.CENTER,color="#093C69"),
        #                 IconButton(icon=Icons.#print,icon_color="#093C69",on_click= lambda x:page.go("/PDF")),
        #                   amlah,
                         

        #             ],spacing=0),
                   
                    
        #         ],spacing=0,
        #         alignment=MainAxisAlignment.CENTER,
        #         horizontal_alignment=CrossAxisAlignment.CENTER
        #     ),
        #     expand=1,
        #     height=130,
            
        #     # bgcolor="#093C69",
        #     border_radius=0,
        #     adaptive=True,
        #     padding=0,
        #     alignment=alignment.center,
        #     ink=True,
            # on_click= lambda e:open_dialog_acount(e),
        # ),
                       
        #            ]),
                   Row([
                      
                       
                   ]),
                        Column([
                        Row([list_t_sahm2,]),
                        Row([
                            
                            list_t_sahm1,
                            
                        ],MainAxisAlignment.CENTER
                        ),
                        list_t_sahm,
                        dialog1,
                        dialog99,
                        # file_picker,
                       
                       
                       
                        ],expand=1,spacing=0),
                     Column([
                             

                        ],alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,spacing=0),
                FloatingActionButton(icon=icons.ADD,bgcolor="red",on_click=lambda x: open_dialog(x)),
                       

                    ],vertical_alignment="center",horizontal_alignment="center"
                
            )
        )
            
        if page.route=="/sdad5":
            page.views.clear()
            ttype="1"
            new_type.value=new_type.options[1].key
            new_type.disabled=True
            page.views.append(
                View(
                    "/sdad5",
                    # text_search.focus(),
                    
                    [
                        AppBar(
                        title=Text("البحث"),
                        center_title=True,
                        color="white",
                        bgcolor="#093C69",
                        leading=IconButton(icons.ARROW_BACK,on_click=lambda x:page.go("/main")),
                        # bgcolor=colors.RED,

                        ),
                        
                        Row([
                            login_page1(Column(
                [
                    Column([
                        text_search,

                    ],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER                    
                            
                        ),
                ],
             
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
                            )),
                            
                    
                        ],MainAxisAlignment.CENTER
                        ),
                       
                      
                
                        list1,
                        dialog1,

                    ],vertical_alignment="center",horizontal_alignment="center"
                
            )
        )
            
        if page.route=="/PDF":
            page.views.clear()
            ttype="1"
            new_type.value=new_type.options[1].key
            new_type.disabled=True
            page.views.append(
                View(
                    "/PDF",
                    # text_search.focus(),
                    
                    [
                    IconButton(icons.ARROW_BACK,on_click=lambda x:page.go("/main")),
                       content_container,

                    ],vertical_alignment="center",horizontal_alignment="center",bgcolor=colors.WHITE,
                
            )
        )

    

        if page.route=="/thsil":
            page.views.clear()
            # text_search1.focus()
            search_items_sdad("e")
            page.views.append(
                View(
                    "/thsil",
                    [
                        AppBar(
                        title=Text("التحصيل اليومي"),
                        center_title=True,
                        color="white",
                        bgcolor="#093C69",
                        leading=IconButton(icons.ARROW_BACK,on_click=lambda x:page.go("/main")),
                       

                        ),

                        
                        Row([
                            login_page1(Column(
                            [
                                Column([
                                    text_search1,

                                ],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER                    
                                        
                                    ),
                            ],
                        
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
                            )),
                            
                    
                        ],MainAxisAlignment.CENTER
                        ),
                       
                      
                
                        list2,
                        dialog1,   

                    ],vertical_alignment="center",horizontal_alignment="center"
                
            )
        )
        page.update()
    # def close_app(e):
    #     page.window.destroy()
    def get_ressd11(customer_id: int, currency_id: int) -> float:
        try:
            data = get_re(f'{url}3/', 'SELECT rseed FROM raseed WHERE ID = ? AND CurrencyID = ?',f'{customer_id},{currency_id}', key)
            current_balance=data[0]['rseed']
            
        except Exception as e:
            print(f"خطأ في جلب الرصيد: {e}")
            current_balance = 0.0

        return current_balance
    def transfer_funds(e):
        if userid.value!="":
            if acount1_id_input.value!=None or acount2_id_input.value!=None:

                try:
                    B1  = "تم  " + "السحب " + " " + "من " + "  حسابكم  " + acount_not_input.value
                    B2  = "تم  " + "الايداع " + " " + "في " + "  حسابكم  " + acount_not_input.value
                    b3  = "  سحب من حساب" + acount1_input.value + " " + "  الي حساب " + acount2_input.value + "  " + acount_not_input.value
                    b4 = " ايداع من حساب" + acount1_input.value + " " + "  الي حساب " + acount2_input.value + "  " + acount_not_input.value
                    aml=""
                    min_aml=""
                    if str(amlah.value)=="ريال يمني":
                        id_amlah=1
                        aml="ريال يمني"
                        min_aml="فلس"
                    elif str(amlah.value)=="ريال سعودي":
                        id_amlah=2
                        aml="ريال سعودي"
                        min_aml="هلله"
                    elif str(amlah.value)=="دولار":
                        id_amlah=3
                        aml="دولار"
                        min_aml="فلس"
                    from_customer_id=acount1_id_input.value
                    to_customer_id=acount2_id_input.value
                    currency=id_amlah
                    amount=float(acount_mony_input.value)
                    bian1=B1
                    bian2=B2
                    str_mony=taqfeet_currency(float(amount), main_unit=aml, sub_unit=min_aml)
                    id_son1=userid.value
                    id_m1=1
                    ty=acount1_input.value
                    ty1=acount2_input.value

                    not1=b3
                    not2=b4
                    data = get_re(f'{url}3/', 'SELECT rseed FROM raseed WHERE ID = ? AND CurrencyID = ?',f'{from_customer_id},{currency}', key)
                    # #print(data.json())
                    v=data
                    dd=0.00
                    try:
                        dd=float(v[0]['rseed'])
                    except:
                        dd=0.00

                    # التحقق من رصيد العميل المرسل
        
                    current_balance = dd

                    # #print(current_balance)

                    if current_balance < amount:
                        d1=SnackBar(
                                        content=Text("الرصيد غير كافي"),
                                        bgcolor="red",
                                        action=f"الرصيد الحالي من العملة هو {dd}"

                                    )
                        page.overlay.append(d1)
                        d1.open=True
                        page.update()
                        #print("الرصيد غير كافي")
                    #     conn.rollback()
                        return False  # الرصيد غير كافٍ
                    ressad=get_ressd11(int(from_customer_id), int(currency))
                    R_b=float(ressad)-float(amount)
                    ressad1=get_ressd11(int(to_customer_id), int(currency))
                    R_b1=float(ressad1)+float(amount)
                    # # أول عملية: سحب من العميل المرسل
                    data1 = get_re(f'{url}2/', 'INSERT INTO MOVE (id_s, mony, id_amlah, bian, bian2, str_mony, id_son, id_m, type, not1) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',f'{from_customer_id},{amount},{currency},سحب,{bian1},{str_mony},{id_son1},{id_m1},{ty},{not1}', key)
                    v1=data1
                    if v1=='1':

                        data2 = get_re(f'{url}2/', 'INSERT INTO MOVE (id_s, mony, id_amlah, bian, bian2, str_mony, id_son, id_m, type, not1) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',f'{to_customer_id},{amount},{currency},ايداع,{bian2},{str_mony},{id_son1},{id_m1},{ty1},{not2}', key)

                        v2=data2
                        #print(v2)
                        if v2=='1':
                                # #print(v)
                            d1=SnackBar(
                                        content=Text("تم الحفظ بنجاح"),
                                        bgcolor="green",
                                        action="Ok"

                                    )
                            page.overlay.append(d1)
                            d1.open=True
                            dialog_acaount1.open=False
                            acount_not_input.value=""
                            acount1_input.value=""
                            acount2_input.value=""
                            acount1_id_input.value=""
                            acount2_id_input.value=""
                        
                            acount_mony_input.value=""
                            acount1_input.value=""
                            acount2_input.value=""
                            amlah.value="ريال يمني"
                

            
                    page.update()
                    return True

                except Exception as e:
                    # #print("خطأ:", e)
                    d1=SnackBar(
                                        content=Text("فشلة العملية"),
                                        bgcolor="red",
                                        action=e

                                    )
                    page.overlay.append(d1)
                    d1.open=True
                    page.update()
                    return False
        else:
            page.go('/')
            page.update()

    #     finally:
    #         cursor.close()
    #         conn.close()
    # transfer_funds(243, 1)
    def save1(e):
   
        page.update()

        
        if userid.value!="":

            # try:
            
                if amount_input.value=="":
                    amount_input.value=0.00
                    page.update()
                else:
              
                        if float(amount_input.value)> 0:
                            # renger.visible=True
                            page.update()
                            
                            aml=""
                            min_aml=""
                            if str(amlah.value)=="ريال يمني":
                                id_amlah=1
                                aml="ريال يمني"
                                min_aml="فلس"
                            elif str(amlah.value)=="ريال سعودي":
                                id_amlah=2
                                aml="ريال سعودي"
                                min_aml="هلله"
                            elif str(amlah.value)=="دولار":
                                id_amlah=3
                                aml="دولار"
                                min_aml="فلس"

                            ressad=get_ressd11(int(id.value), int(id_amlah))
                            # print(ressad)
                            tfk=taqfeet_currency(float(amount_input.value), main_unit=aml, sub_unit=min_aml)
                            kk=""
                            kk1=direction.value
                            R_b=0
                            if str(direction.value)=="ايداع":
                                kk=f"تم {kk1} في حسابكم  {note_input.value}"
                                R_b=float(ressad)+float(amount_input.value)
                            else:
                                kk=f"تم {kk1} من حسابكم  {note_input.value}"
                                R_b=float(ressad)-float(amount_input.value)
                            data = get_re(f'{url}/2', 'insert into MOVE (id_s,type,mony,bian,bian2,id_son,id_amlah,id_m,op,no_h,str_mony,R_BACK) values (?,?,?,?,?,?,?,?,?,?,?,?)',f'{id.value},{names.value},{amount_input.value},{kk1},{kk},{userid.value},{id_amlah},{id.value},{op},{no_hwala.value},{tfk},{R_b}', key)
                            v=data
                            if v=='1':
                                # #print(v)
                                d1=SnackBar(
                                        content=Text("تم الحفظ بنجاح"),
                                        bgcolor="green",
                                        action="Ok"

                                    )
                                page.overlay.append(d1)
                                d1.open=True
                                all_mony.value=float(all_mony.value)+float(mony.value)
                                mony.value=0.00
                                exit_dialog("e")
                                add_clients("e")
                                amount_input.value=0.00
                                amlah.value="ريال يمني"
                                note_input.value=""
                                direction.value="ايداع"
                                list4.controls.clear()
                                search_items_sahm("e")
                                d1=SnackBar(
                                    content=Text("تم العملية بنجاح"),
                                    bgcolor="green",
                                    action="Ok"

                                )
                                page.overlay.append(d1)
                                d1.open=True
                                        
                                page.update()
                            
                            
                        else:
                            a2=AlertDialog(
                                title=Text("حدث خطاء اثناء",size=13),

                                actions_alignment=MainAxisAlignment.CENTER,

                            )
                            page.overlay.append(a2)
                            a2.open=True
                            page.update()
                          
        else:
            page.go('/')
            page.update()
    def new_add_clint(e):
        if userid.value!="":
            if clint_new_name.value!="":
        
                try:
                    maxid=0
            
                    data = get_re(f'{url}1/', 'SELECT MAX(ID) FROM CLIENTS',f'', key)

                    maxid=data
                    for item in data:
                        maxid=int(item["Expr1000"])+1
                        #print(maxid)
          
                    data = get_re(f'{url}2/', 'INSERT INTO CLIENTS(CLIENT_NAME, CLIENT_NO_B, phone1, phone2, ID, user_id, CLIENT_NOTE) VALUES (?, ?, ?, ?, ?, ?, ?)',f'{clint_new_name.value},{clint_new_no_b.value},{clint_new_phone1.value},{clint_new_phone2.value},{maxid},{userid.value},{clint_new_not.value}', key)
                    if data == "1":
                        clint_new_name.value=""
                        clint_new_phone1.value=""
                        clint_new_phone2.value=""
                        clint_new_no_b.value=""
                        exit_dialog_clint("e")
                        d1=SnackBar(
                                    content=Text("تم العملية بنجاح"),
                                    bgcolor="green",
                                    action="Ok"

                                )
                        page.overlay.append(d1)
                        d1.open=True

  
                    page.update()
                except:
                    a3=AlertDialog(
                                    title=Text("القيمة المدخلة غير صحيحة",size=13),

                                    actions_alignment=MainAxisAlignment.CENTER,

                                )
                    page.overlay.append(a3)
                    a3.open=True
                    page.update()
        else:
            page.go('/')
            page.update()
    def new_add_sahm(e):
        # msgbox5.open=False
        if userid.value!="":
            if name_sahm_input.value!="":
        
                try:
                    maxid=0

                    data = get_re(f'{url}1/', 'SELECT MAX(ID) FROM SAHM',f'', key)

                    maxid=data
                    for item in data:
                        maxid=int(item["Expr1000"])+1
                        print(maxid)
                    end_day="0"
                    many=0
                    t=0
                    if str(direction_sahm.value)=="سهم":
                        end_day=print_future_date(99)
                        many=mony_sahm_input.value
                        t=0
                    else:
                         end_day=print_future_date(0)
                         many=0
                         t=1     
                    data = get_re(f'{url}2/', 'INSERT INTO SAHM (clint_id, g_id, mony_s, dat_end, dat, status, NOT1, type_s, type_name,ID,id_user) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',f'{id_clint_sahm_input.value},1,{many},{end_day},{dat_s},نشط,{sahm_new_not.value},{t},{direction_sahm.value},{maxid},{userid.value}', key)
                    if data == "1":
                        direction_sahm.value="حساب جاري"
                        id_clint_sahm_input.value=""
                        mony_sahm_input.value=0.00
                        sahm_new_not.value=""
                        mony.value=0.00
                        name_sahm_input.value=""
                  
                      
                        
                        
                        exit_dialog_sahm("e")

  
                    page.update()
                except:
                    a3=AlertDialog(
                                    title=Text("القيمة المدخلة غير صحيحة",size=13),

                                    actions_alignment=MainAxisAlignment.CENTER,

                                )
                    page.overlay.append(a3)
                    a3.open=True
                    # sdad.value=""
                    page.update()
        else:
         
            page.go('/')
            page.update()
    def print_future_date(days_to_add):
        now = datetime.datetime.now()  # الحصول على الوقت الحالي
        future_date = now + datetime.timedelta(days=days_to_add)
        return future_date.strftime("%Y-%m-%d") # إضافة الأيام
        # #print()
    #print_future_date(99)
    def taqfeet_currency(amount, main_unit="ريال", sub_unit="هللة"):
        try:
            amount = round(float(amount), 2)  # التأكد من دقة رقمية من منزلتين
            integer_part = int(amount)
            fractional_part = int(round((amount - integer_part) * 100))

            # تفقيط الأجزاء
            words = num2words(integer_part, lang='ar') + f" {main_unit}"
            if fractional_part > 0:
                words += f" و{num2words(fractional_part, lang='ar')} {sub_unit}"
            words += " فقط لا غير"
            return words

        except Exception as e:
            return f"خطأ: {e}"
    def close(e):
        import sys
        sys.exit(100)
    page.on_route_change=routes_Change
    page.go(page.route)
# threading.Thread(target=close_browser_after_delay, daemon=True).start()


app(target=main,assets_dir="./assets/",port=5521,host="0.0.0.0",view=WEB_BROWSER)



# t = threading.Thread(target=close_browsers)
# t.start()
