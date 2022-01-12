# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:44:10 2021

@author: ADMIN
"""
def chaomung():
    print("Xin chào mừng đến với cửa hàng của chúng tôi\nCửa hàng chúng tôi hiện tại cung cấp 3 dòng sản phẩm:")
    print(" Hải Sản - bao gồm các mặt hàng Tôm, Cua, Cá;")
    print(" Thịt - bao gồm các mặt hàng Gà, Bò, Heo;")
    print(" Rau - bao gồm các mặt hàng Khoai, Ngô")
    print("Xin mời chọn sản phẩm:")
Tom=Ca=Cua=0
Ga=Bo=Heo=0
Khoai=Ngo=0
def haisan():
    try:
        global Tom,Ca,Cua 
        loaihs='nhap'
        while(loaihs!='exit'):
            try:
                loaihs=input("Xin mời nhập: 'Tôm', 'Cua' hoặc 'Cá' để chọn, Nhập 'exit' để thoát:")
                if(loaihs =='Tôm'): Tom=Tom+eval(input("Bạn muốn mua bao nhiêu kg tôm:"))
                elif(loaihs=='Cua'):Cua=Cua+eval(input("Bạn muốn mua bao nhiêu kg cua:"))
                elif(loaihs=='Cá'):  Ca=Ca+eval(input("Bạn muốn mua bao nhiêu kg cá:"))    
                elif(loaihs=='exit'):loaihs='exit'
                else: print("Hiện tại cửa hàng chưa có loại Hải sản này hoặc bạn đã nhập sai cú pháp, vui lòng nhập lại")
            except: print("Bạn đã nhập sai cú pháp vui lòng nhập lại")
    except: print("Bạn đã nhập sai cú pháp")
def thit():
    try:
        global Ga,Bo,Heo 
        loaithit='nhap'
        while(loaithit!='exit'):
            try:
                loaithit=input("Xin mời nhập: 'Gà', 'Bò' hoặc 'Heo' để chọn, Nhập 'exit' để thoát:")
                if(loaithit =='Gà'): Ga=Ga+ eval(input("Bạn muốn mua bao nhiêu kg Gà:"))
                elif(loaithit=='Bò'): Bo=Bo+ eval(input("Bạn muốn mua bao nhiêu kg Bò:"))
                elif(loaithit=='Heo'): Heo=Heo+ eval(input("Bạn muốn mua bao nhiêu kg Heo:"))    
                elif(loaithit=='exit'):loaithit='exit'
                else: print("Hiện tại cửa hàng chưa có loại thịt này hoặc bạn đã nhập sai cú pháp, vui lòng nhập lại")
            except: print("Bạn đã nhập sai cú pháp vui lòng nhập lại")
    except: print("Bạn đã nhập sai cú pháp")
def rau():
    try:
        global Ngo,Khoai 
        loairau='nhap'
        while(loairau!='exit'):
            try:
                loairau=input("Xin mời nhập: 'Ngô' hoặc 'Khoai' để chọn, Nhập 'exit' để thoát:")
                if(loairau =='Ngô'): Ngo=Ngo+eval(input("Bạn muốn mua bao nhiêu kg Ngô:"))
                elif(loairau=='Khoai'): Khoai=Khoai+eval(input("Bạn muốn mua bao nhiêu kg Khoai:"))
                elif(loairau=='exit'):loairau='exit'
                else: print("Hiện tại cửa hàng chưa có loại rau này hoặc bạn đã nhập sai cú pháp, vui lòng nhập lại")
            except: print("Bạn đã nhập sai cú pháp vui lòng nhập lại")
    except: print("Bạn đã nhập sai cú pháp")
def kiemtraskt(a):
    if(len(a)==16): return 0
    else: return 1

def kiemtravidt(a):
    if(len(a)==9): return 0
    else: return 1
        
def cuahang():
    global Tom,Cua,Ca,Ngo,Khoai,Ga,Bo,Heo
    chaomung()
    loai='batdau'
    m=0
    try:
        while(loai!="finish"):
            if(m!=0): print("Bạn còn muốn xem thêm dòng sản phẩm nào nữa không")
            m=m+1
            try:
                loai = input("Xin mời nhập loại hàng:'Hải sản','Thịt','Rau' để chọn, Nhập 'finish' để thoát:")
                if(loai=='Hải sản'): haisan()
                elif(loai=='Thịt'): thit()
                elif(loai=='Rau'): rau()
                elif(loai=='finish'): loai='finish'
                else: print("Hiện tại cửa hàng chưa có loại mặt hàng này hoặc bạn đã nhập sai cú pháp, vui lòng nhập lại")
            except: print("Bạn đã nhập sai cú pháp vui lòng nhập lại")
        if(Tom!=0): print("Bạn đã mua",Tom,"kg Tôm,thành tiền:",Tom*200000,"VNĐ")
        if(Ca!=0): print("Bạn đã mua",Ca,"kg Cá,thành tiền:",Ca*60000,"VNĐ")
        if(Cua!=0): print("Bạn đã mua",Cua,"kg Cua,thành tiền:",Cua*500000," VNĐ")
        if(Ga!=0): print("Bạn đã mua",Ga,"kg Gà,thành tiền:",Ga*80000,"VNĐ")
        if(Bo!=0): print("Bạn đã mua",Bo,"kg Bò,thành tiền:",Bo*120000,"VNĐ")
        if(Heo!=0): print("Bạn đã mua",Heo,"kg Heo,thành tiền:",Heo*100000,"VNĐ")
        if(Ngo!=0): print("Bạn đã mua",Ngo,"kg Ngô, thành tiền:",Ngo*18000,"VNĐ")
        if(Khoai!=0): print("Bạn đã mua",Khoai,"kg Khoai,thành tiền:",Khoai*10,"VNĐ")
        print("Tổng thành tiền hóa đơn của bạn là:",Tom*200000+Ca*60000+Cua*500000+Ga*80000+Bo*120000+Heo*100000+Ngo*18000+Khoai*10000,"VNĐ")
        kt=1
        kt2=1
        pthuc=''
        while(kt==1):
            try:
                pthuc=input("Xin chọn một phương thức thanh toán ['Tiền Mặt', 'Thẻ Tín Dụng', 'Ví Điện Tử']:")
                if(pthuc=='Tiền Mặt'):
                    print("Bạn đã hoàn thành thanh toán. Cảm ơn mua hàng tại cửa hàng của chúng tôi")
                    kt=0
                elif (pthuc=='Thẻ Tín Dụng'):
                    kt=0
                    kt2==1
                    while(kt2==1):
                        try:
                            skt=input("Xin mời nhập số thẻ tín dụng của bạn:")
                            if(kiemtraskt(skt)==0):
                                print("Bạn đã hoàn thành thanh toán. Cảm ơn mua hàng tại cửa hàng của chúng tôi")
                                kt2=0
                            else: print("Bạn đã nhập sai số tài khoản vui lòng nhập lại")
                        except: print("Không có hình thức thanh toán này hoặc bạn đã nhập sai cú pháp vui lòng nhập lại")
                elif(pthuc=='Ví Điện Tử'):
                    kt=0
                    kt2==1
                    while(kt2==1):
                        try:
                            skt=input("Xin mời nhập số mã ví điện tử của bạn:")
                            if(kiemtravidt(skt)==0):
                                print("Bạn đã hoàn thành thanh toán. Cảm ơn mua hàng tại cửa hàng của chúng tôi")
                                kt2=0
                            else: print("Bạn đã nhập sai mã ví điện tử vui lòng nhập lại")
                        except: print("Không có hình thức thanh toán này hoặc bạn đã nhập sai cú pháp vui lòng nhập lại")
                else: print("Không có hình thức thanh toán này hoặc bạn đã nhập sai cú pháp vui lòng nhập lại")
            except: print("Không có hình thức thanh toán này hoặc bạn đã nhập sai cú pháp vui lòng nhập lại")
    except: print("Bạn đã nhập sai cú pháp")
cuahang()




