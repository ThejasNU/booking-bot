from selenium.webdriver.remote.webdriver import WebDriver
import time

class BookingFiltration:
    def __init__(self,driver:WebDriver): #Here we are specifying the type of driver to get autorecommendations coz code doesn't know the type of driver
        self.driver=driver
    def apply_star_rating(self,*star_values):
        star_filtration_box=self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        star_child_elements = star_filtration_box.find_elements_by_css_selector('*') #This gets a list of all elements in star_filtration_box
        for star_value in star_values:
            for star_element in star_child_elements:
                if(str(star_element.get_attribute('data-filters-item')).strip())==f"class:class={star_value}": #Here strip() removes whitespaces
                    star_element.click()
                    time.sleep(3) #This is to prevent clicking inbetween loading
    def sort_price_lowest_first(self):
        element = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        element.click()