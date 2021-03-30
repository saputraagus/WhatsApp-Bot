from selenium import webdriver
import time

PATH = "C:/Users/Extramarks_Indonesia/Documents/AutoReplyWa/chromedriver" # Ganti dengan sesuai dengan tempat drive anda berada
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

# Jeda waktu untuk melakukan Scan QR Code
time.sleep(10)

# Isi pesan yang akan dikirim
text1 = "Hai "
text2 = ", Kami sedang sibuk saat ini , tunggu beberapa saat"

# Daftar nama yang akan dikirim pesan
namelist = ["Whatsapp Bot", "Catatan Penting"]
while(1):
    for name in namelist:
        # Klik search bar
        getsearchbox = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
        getsearchbox.click()
        time.sleep(2)

        # Ketik nama yang ada dalam kontak
        getsearchbox.send_keys(name)
        time.sleep(3)

        # Cek jika ada pesan yang belum dibaca
        unreadMsgs = False

        getlist = driver.find_elements_by_xpath("//span[@class ='_38M1B']")
        if (len(getlist)):
            unreadMsgs = True


        # Jika tidak ada maka tombol back pada search bar akan di klik
        if not unreadMsgs:
            back = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/button")
            back.click()

        # Jika ada maka akan mengirim pesan ke kontak tersebut
        else:
            # Klik chat
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()

            # Ketik pesan didalam kotak pesan
            textbox = driver.find_element_by_xpath('//div[@class="_2A8P4"]')
            textbox.send_keys(text1+name+text2)

            # Kirim pesan
            send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
            send.click()

            # Cetak nama kontak dalam log
            print(name , "mengirim pesan kepadamu!")

            time.sleep(5)

    # code nya akan jalan lagi setelah 120 detik (2 menit)
    time.sleep(120)

driver.quit()