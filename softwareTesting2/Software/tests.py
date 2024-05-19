import os
import unittest
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import random

# Create your tests here.

# 3 test
class LogTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LogTest, self).__init__(*args, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # test1
    def test_login(self):
        
        username = "yasin"
        password = "Yasin.emin.15"
        driver = self.driver
        driver.get('http://localhost:8000/blogs')
        time.sleep(2)
        
        # Login pop-up'ını aç
        login_popup_button = driver.find_element(By.ID, 'auth-buttons') # ID'yi HTML yapınıza göre değiştirin
        login_popup_button.click()
        time.sleep(2)
        
        # Login formunu doldur ve giriş yap
        user_input = driver.find_element(By.XPATH, '//*[@id="username"]')
        pass_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/button')
        
        user_input.send_keys(username)
        pass_input.send_keys(password)
        time.sleep(2)
        login_button.click()
        time.sleep(1)
        print("Login islemi tamamlandı.")
    
    # test2
    def test_logout(self):
        driver = self.driver
        driver.get('http://localhost:8000/blogs')
        time.sleep(3)

        login_popup_button = driver.find_element(By.XPATH, '//*[@id="logout-button"]') # ID'yi HTML yapınıza göre değiştirin
        login_popup_button.click()
        time.sleep(2)

        try:
        # Kullanıcı giriş yapmışsa çıkış yap butonunu bul
            logout_button = driver.find_element(By.ID, 'logoutbutton')
            logout_button.click()
            time.sleep(1)
        except NoSuchElementException:
            # Kullanıcı zaten giriş yapmamışsa bir şey yapma
            pass

        print("logout islemi tamamlandı.")
    
    # test3
    def test_register(self):

        username = "TestUser" + str(random.randint(0,100))
        password = "yaso123"
        driver = self.driver
        driver.get('http://localhost:8000/blogs')
        time.sleep(2)
        
        # Login pop-up'ını aç
        login_popup_button = driver.find_element(By.ID, 'auth-buttons') # ID'yi HTML yapınıza göre değiştirin
        login_popup_button.click()
        time.sleep(2)
  
        register_button = driver.find_element(By.ID, 'go-register')
        register_button.click()
        time.sleep(3)

        user_input = driver.find_element(By.XPATH, '//*[@id="username1"]')
        pass_input = driver.find_element(By.XPATH, '//*[@id="password1"]')

        user_input.send_keys(username)
        pass_input.send_keys(password)
        time.sleep(1)

        register_button2 = driver.find_element(By.XPATH, '//*[@id="register-form"]/button')
        register_button2.click()
        time.sleep(1)
        
        print("register islemi tamamlandı.")
     
        # test4 xpath

# 4 test
class AdminBlogTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AdminBlogTest, self).__init__(*args, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    def login(self):
        username = "yasin"
        password = "Yasin.emin.15"
        driver = self.driver
        driver.get('http://localhost:8000/admin')
        user_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
        pass_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input')

        user_input.send_keys(username)
        pass_input.send_keys(password)
        login_button.click()
    
    # test4
    def test_adminLogin(self):
        self.login()
        print("Admin Login islemi test edildi.")

    # test5
    def test_BlogPost_ADD(self):
        self.login()
        print("Blog post ekleme islemi yapiliyor.")
        driver = self.driver
        driver.get('http://localhost:8000/admin/')
        time.sleep(2)
        print(self.driver.current_url)
        self.driver.find_element(By.LINK_TEXT, "Blog posts").click()
        self.driver.find_element(By.LINK_TEXT, "ADD BLOG POST").click()

        title_input = self.driver.find_element(By.XPATH, '//*[@id="id_title"]')
        title_input.send_keys('Test Blog Post')

        content_input = self.driver.find_element(By.XPATH, '//*[@id="id_content"]')
        content_input.send_keys('Test Blog Post İçeriği.')

        author_select = Select(self.driver.find_element(By.XPATH, '//*[@id="id_author"]'))
        author_select.select_by_visible_text('Yasin')

        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, 'testImage.jpeg')  
        image_input = self.driver.find_element(By.ID, 'id_image')
        image_input.send_keys(image_path)

        category_select = Select(self.driver.find_element(By.XPATH, '//*[@id="id_categories"]'))
        category_select.select_by_visible_text('Teknoloji')

        tag_select = Select(self.driver.find_element(By.XPATH, '//*[@id="id_tags"]'))
        tag_select.select_by_visible_text('OOP')

        self.driver.find_element(By.NAME, "_save").click()
        time.sleep(3)
        success_message = self.driver.find_element(By.CLASS_NAME, 'success').text
        self.assertIn("was added successfully.", success_message)
        print("blog ekleme tamamlandı.")

    # test6
    def test_admin_Url(self):
        self.login()
        print("Yönlendirme doğrulama testi başlatıldı")
        driver = self.driver
        goLink = driver.current_url
        self.assertEqual(goLink, 'http://localhost:8000/admin/')
        print("Url Doğrulandı.")
        
    # test7
    def test_deletePost(self):
        self.login()
        driver = self.driver
        driver.get('http://localhost:8000/admin/Software/blogpost/')
        print("Blog silme işlemi yapılıyor.")
        # Get all post IDs
        post_ids = [int(checkbox.get_attribute("value")) for checkbox in driver.find_elements(By.CLASS_NAME, 'action-select')]
        largest_id = max(post_ids)
        
        # Click the link to the blog post with the largest ID
        largest_post_link = driver.find_element(By.XPATH, f'//a[@href="/admin/Software/blogpost/{largest_id}/change/"]')
        largest_post_link.click()

        # Click the delete link
        delete_link = driver.find_element(By.CLASS_NAME, 'deletelink')
        delete_link.click()

        # Confirm the deletion
        confirm_button = driver.find_element(By.XPATH, '//input[@type="submit"][@value="Yes, I’m sure"]')
        confirm_button.click()
        print("Blog silme işlemi tamamlandı.")

    # test8
    def test_category_count(self):
        self.login()
        driver = self.driver
        driver.get('http://127.0.0.1:8000/admin/Software/category/')

        category_rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
        categoryCount = 5

        currentCategory = len(category_rows)
        self.assertEqual(currentCategory,categoryCount,f"Expected {categoryCount} categories, but found {currentCategory}.")

    def test_tag_count(self):
        self.login()
        driver = self.driver
        driver.get('http://127.0.0.1:8000/admin/Software/tag/')

        tag_rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')

# x test
class BlogPostTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BlogPostTest, self).__init__(*args, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    def login(self):
        username = "yasin"
        password = "Yasin.emin.15"
        driver = self.driver
        driver.get('http://localhost:8000/blogs')
        user_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
        pass_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input')

        user_input.send_keys(username)
        pass_input.send_keys(password)
        login_button.click()

    # test9
    def test_Home(self):
        driver = self.driver
        driver.get('http://localhost:8000/blogs')
        print("Yönlendirme testi başladı.")
        homeButton = driver.find_element(By.XPATH, '//*[@id="mainNavigation"]/ul/li[1]/a')
        homeButton.click()
        time.sleep(2)

        goLink = driver.current_url
        self.assertEqual(goLink,"http://localhost:8000/index/")
        print("Yönlendirme testi tamamlandı.")
        time.sleep(2)
    
    # test10
    def test_industry(self):
        driver = self.driver
        driver.get('http://localhost:8000/blogs')
        print("industry testi başladı.")
        industryButton = driver.find_element(By.XPATH, '//*[@id="mainNavigation"]/ul/li[2]/a')
        industryButton.click()
        time.sleep(2)

        goLink = driver.current_url
        self.assertEqual(goLink,"http://localhost:8000/industries/")
        print("industry testi tamamlandı.")
        time.sleep(2)

    # test11
    def test_blog_author(self):
        driver = self.driver
        driver.get('http://localhost:8000/blog_details/6/') 
        print("Blog yazar testi başladı.")
        time.sleep(2)
        author_name = driver.find_element(By.CSS_SELECTOR, 'h6.blog-author__name').text
        expected_author = "Yasin"
        
        self.assertEqual(author_name, expected_author, f"Expected author to be {expected_author}, but found {author_name}.")
        print("Yazar testi tamamlandı.")
    
    # test12
    def test_blog_title(self):
        driver = self.driver
        driver.get('http://localhost:8000/blog_details/6/') 
        print("Blog yazar testi başladı.")
        time.sleep(2)

        title_element = driver.find_element(By.CSS_SELECTOR, 'h1.post__title.mb-30')
        actual_title = title_element.text
        expected_title = 'DevOps: Yazilim Gelistirme Ve Operasyonlarin Entegrasyonu'
        
        self.assertEqual(actual_title, expected_title, f"Expected title to be '{expected_title}', but found '{actual_title}'.")

class IndustryTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IndustryTest, self).__init__(*args, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # test13
    def test_heading_title(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/industries/')

        # Başlığı kontrol et
        title_element = driver.find_element(By.XPATH, '/html/body/div/section[2]/div/div[1]/div/div/h3')
        actual_title = title_element.text
        expected_title = "Offer The Latest Software And Solutions To Our Customers!"

        self.assertEqual(actual_title, expected_title, f"Expected title to be '{expected_title}', but found '{actual_title}'.")

    # test14
    def test_read_more_button(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/industries')  
        print("Servis Testi Başladı")
        read_more_button = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn__primary')

    
        self.assertTrue(read_more_button.is_enabled(), "Read More button is not enabled.")

        read_more_button.click()

        expected_url = 'http://127.0.0.1:8000/industry_details/1/'
        actual_url = driver.current_url
        self.assertEqual(actual_url, expected_url, f"Expected URL to be '{expected_url}', but found '{actual_url}'.")
        print("Servis testi tamamlandı")

    # test15
    def test_button_color(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/industry_details/1/')  # Sayfaya gidin
        print("Buton testi başladı")

        # Butonu bulun
        button = driver.find_element(By.XPATH, '/html/body/div/section[1]/div/div/div/a')

       
        button_color = button.value_of_css_property('background-color')
        expected_color = 'rgba(0, 146, 255, 1)'  
        self.assertEqual(button_color, expected_color, f"Button color is not as expected. Actual color: {button_color}")
        print("Buton testi tamamlandı")

    # test16
    def test_image_presence(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/industry_details/1/')
        print("Resim testi başladı")
        image = driver.find_element(By.XPATH, '//*[@id="overview"]/div/div/div[2]/div/img')
        self.assertTrue(image.is_displayed(), "Resim Mevcut Değil")
        print("Resim testi tamamlandı")

class ContactTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ContactTest, self).__init__(*args, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)   

    # test17
    def test_phone_number(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/blogs/')
        phone_link = self.driver.find_element(By.CLASS_NAME, 'phone-number')
        phone_number = phone_link.find_element(By.TAG_NAME, 'span').text
        phone_link.click()
        
    
        expected_phone_number = "01061245741"
        self.assertEqual(phone_number, expected_phone_number)
    # test18
    def test_address(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/blogs/')
        address_element = self.driver.find_element(By.XPATH, '/html/body/div/footer/div/div[2]/div/div[1]/div/div/ul/li[3]')
        address_text = address_element.text
        
        # Beklenen adres
        expected_address = "2307 Beverley Rd Brooklyn, New York 11226 United States."

        # Adresin doğru olup olmadığını kontrol etmek için beklenen adresle karşılaştırın
        self.assertEqual(address_text, expected_address)

class CategoryTagTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CategoryTagTest, self).__init__(*args, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    def login(self):
        username = "yasin"
        password = "Yasin.emin.15"
        driver = self.driver
        driver.get('http://localhost:8000/admin')
        user_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
        pass_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input')

        user_input.send_keys(username)
        pass_input.send_keys(password)
        login_button.click()

    # test19
    def test_categoryAdd(self):

        self.login()
        driver = self.driver
        driver.get('http://localhost:8000/admin/')
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Categorys").click()
        self.driver.find_element(By.LINK_TEXT, "ADD CATEGORY").click()

        time.sleep(2)
        category_input = self.driver.find_element(By.XPATH, '//*[@id="id_name"]')
        category_input.send_keys('Test category1')
        time.sleep(3)
        self.driver.find_element(By.NAME, "_save").click()
        print("kategori eklendi")

    #test20
    def test_TagAdd(self):

        self.login()
        driver = self.driver
        driver.get('http://localhost:8000/admin/')
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Tags").click()
        self.driver.find_element(By.LINK_TEXT, "ADD TAG").click()

        time.sleep(2)
        category_input = self.driver.find_element(By.XPATH, '//*[@id="id_name"]')
        category_input.send_keys('Test tag1')
        time.sleep(3)
        self.driver.find_element(By.NAME, "_save").click()
        print("tag eklendi")

    #test21
    def test_DeleteCategory(self):
        self.login()
        driver = self.driver
        driver.get('http://localhost:8000/admin/Software/category/')
        print("category silme işlemi yapılıyor.")
        # Get all post IDs
        category_ids = [int(checkbox.get_attribute("value")) for checkbox in driver.find_elements(By.CLASS_NAME, 'action-select')]
        largest_id = max(category_ids)
        
        # Click the link to the blog post with the largest ID
        largest_category_link = driver.find_element(By.XPATH, f'//a[@href="/admin/Software/category/{largest_id}/change/"]')
        largest_category_link.click()

        # Click the delete link
        delete_link = driver.find_element(By.CLASS_NAME, 'deletelink')
        delete_link.click()

        # Confirm the deletion
        confirm_button = driver.find_element(By.XPATH, '//input[@type="submit"][@value="Yes, I’m sure"]')
        confirm_button.click()
        print("category silme işlemi tamamlandı.")

    #test22
    def test_DeleteTag(self):
        self.login()
        driver = self.driver
        driver.get('http://localhost:8000/admin/Software/tag/')
        print("tag silme işlemi yapılıyor.")
      
        tag_ids = [int(checkbox.get_attribute("value")) for checkbox in driver.find_elements(By.CLASS_NAME, 'action-select')]
        largest_id = max(tag_ids)
        
        largest_tag_link = driver.find_element(By.XPATH, f'//a[@href="/admin/Software/tag/{largest_id}/change/"]')
        largest_tag_link.click()

        delete_link = driver.find_element(By.CLASS_NAME, 'deletelink')
        delete_link.click()

        confirm_button = driver.find_element(By.XPATH, '//input[@type="submit"][@value="Yes, I’m sure"]')
        confirm_button.click()
        print("tag silme işlemi tamamlandı.")

class CommonTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CommonTest, self).__init__(*args, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    #test23
    def test_blog_title(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/blogs/')

        title_element = driver.find_element(By.XPATH, '/html/body/div/section[1]/div/div/div/h1')
        actual_title = title_element.text
        expected_title = "Our Blog"

        self.assertEqual(actual_title, expected_title, f"Expected title to be '{expected_title}', but found '{actual_title}'.")

    #test24
    def test_industry_title(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/industries/')

        title_element = driver.find_element(By.XPATH, '/html/body/div/section[1]/div/div/div/h1')
        actual_title = title_element.text
        expected_title = "Consultative Approach On Emerging Technology!."

        self.assertEqual(actual_title, expected_title, f"Expected title to be '{expected_title}', but found '{actual_title}'.")

    #test25
    def test_link_color(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/blogs/')
        expected_color = "rgba(255, 255, 255, 1)"  
        actual_color = self.driver.find_element(By.XPATH, '//*[@id="mainNavigation"]/ul/li[3]/a').value_of_css_property("color")
        
        self.assertEqual(actual_color, expected_color, "Bağlantı rengi doğru değil")

    #test26
    def test_link_text(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/blogs/')
        expected_text = "7oroof.com"  # Beklenen metin
        actual_text = self.driver.find_element(By.XPATH, '/html/body/div/footer/div/div[3]/div/a').text
        
        self.assertEqual(actual_text, expected_text, "Bağlantı metni doğru değil")

    #test27
    def test_video_link(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/industries/')
        expected_url = "https://www.youtube.com/watch?v=nrJtHemSPW4"  # Beklenen URL
        actual_url = self.driver.find_element(By.XPATH, '/html/body/div/section[1]/div/div/div/div/a[2]').get_attribute("href")
        
        self.assertEqual(actual_url, expected_url, "Bağlantı URL'si doğru değil")

    #test28
    def test_blog_author_bio(self):
        expected_bio = "Sakarya Üniversitesi Bilgisayar Mühendisliği"
        self.driver.get("http://localhost:8000/blog_details/6/")  # Blog detay sayfası URL'si
        print("Blog yazar biyografi testi başladı.")
        actual_bio = self.driver.find_element(By.XPATH, '/html/body/div/section[2]/div/div/div[1]/div[4]/div[2]/p').text

        self.assertEqual(actual_bio, expected_bio, f"Expected author bio to be '{expected_bio}', but found '{actual_bio}'.")
        print("Yazar biyografi testi tamamlandı.")

class AuthorTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AuthorTest, self).__init__(*args, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options) 
    
    def login(self):
        username = "yasin"
        password = "Yasin.emin.15"
        driver = self.driver
        driver.get('http://localhost:8000/admin')
        user_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
        pass_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input')

        user_input.send_keys(username)
        pass_input.send_keys(password)
        login_button.click()

    #test29
    def test_AuthorAdd(self):

        self.login()
        driver = self.driver
        driver.get('http://localhost:8000/admin/')
        print("author ekleniyor")
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Authors").click()
        self.driver.find_element(By.LINK_TEXT, "ADD AUTHOR").click()

        time.sleep(2)
        Author_input = self.driver.find_element(By.XPATH, '//*[@id="id_name"]')
        Author_input.send_keys('TestAuthor')

        Bio_input = self.driver.find_element(By.XPATH, '//*[@id="id_bio"]')
        Bio_input.send_keys('TestBio')

        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, 'testAvatar.png')  
        image_input = self.driver.find_element(By.ID, 'id_avatar')
        image_input.send_keys(image_path)

        time.sleep(3)
        self.driver.find_element(By.NAME, "_save").click()
        print("author eklendi")

    #test30
    def test_AuthorDelete(self):
        self.login()
        driver = self.driver
        driver.get('http://localhost:8000/admin/Software/author/')
        print("author silme işlemi yapılıyor.")
        # Get all post IDs
        author_ids = [int(checkbox.get_attribute("value")) for checkbox in driver.find_elements(By.CLASS_NAME, 'action-select')]
        largest_id = max(author_ids)
        
        # Click the link to the blog post with the largest ID
        largest_author_link = driver.find_element(By.XPATH, f'//a[@href="/admin/Software/author/{largest_id}/change/"]')
        largest_author_link.click()

        # Click the delete link
        delete_link = driver.find_element(By.CLASS_NAME, 'deletelink')
        delete_link.click()

        # Confirm the deletion
        confirm_button = driver.find_element(By.XPATH, '//input[@type="submit"][@value="Yes, I’m sure"]')
        confirm_button.click()
        print("author silme işlemi tamamlandı.")

def close(self):
    # Tarayıcıyı kapatma işlemi burada manuel olarak yapılacak
    self.driver.quit()    



def run_tests(test_suite):
    unittest.TextTestRunner().run(test_suite)

def main():
    
    
    while True:
        print("\n--- Test Menüsü ---")
        print("1- Login - Register Testlerini Çalıştır")
        print("2- Admin Testlerini Çalıştır")
        print("3- Blog Post Testlerini Çalıştır")
        print("4- Industry Testlerini Çalıştır")
        print("5- contact Testleri Çalıştır")
        print("6- Category-Tag Testlerini Çalıştır")
        print("7- Genel Testleri Çalıştır")
        print("8- Author Testleri Çalıştır")
        print("9- Çıkış")
        choice = input("Seçiminiz: ")

        match choice:
            case '1':
                loginSuite = unittest.TestLoader().loadTestsFromTestCase(LogTest)
                run_tests(loginSuite)

            case '2':
                AdminBlogSuite = unittest.TestLoader().loadTestsFromTestCase(AdminBlogTest)
                run_tests(AdminBlogSuite)

            case '3':
                BlogPostSuite = unittest.TestLoader().loadTestsFromTestCase(BlogPostTest)
                run_tests(BlogPostSuite)

            case '4':
                IndustrySuite = unittest.TestLoader().loadTestsFromTestCase(IndustryTest)
                run_tests(IndustrySuite)

            case '5':
                CommonSuite = unittest.TestLoader().loadTestsFromTestCase(ContactTest)
                run_tests(CommonSuite)

            case '6':
                CategoryTagSuite = unittest.TestLoader().loadTestsFromTestCase(CategoryTagTest)
                run_tests(CategoryTagSuite)

            case '7':
                CommonSuite = unittest.TestLoader().loadTestsFromTestCase(CommonTest)
                run_tests(CommonSuite)

            case '8':
                AuthorSuite = unittest.TestLoader().loadTestsFromTestCase(AuthorTest)
                run_tests(AuthorSuite)

            case '9':
                print("Çıkış yapılıyor...")
                break

            case _:
                print("Geçersiz seçim. Tekrar deneyin.")

    # input("Testler tamamlandı. Tarayıcıyı kapatmak için Enter tuşuna basın...")
    # LogTest.close()

if __name__ == "__main__":
    main()