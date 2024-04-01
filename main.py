from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from openpyxl import Workbook

class NobitexBot:
    driver = webdriver.Chrome()
    
    def getPrices(self,
                delay: float = 2,
                infinityRequest : bool = True,
                optionalDelay : float = 0,
                link : str = None,
                element : str = None,
                exportInExcel : bool = False,
                excelPath : str = "./",
                *args, **kwargs
                ) -> None:
        """
            Extracts prices from a webpage and optionally exports them to an Excel file.

            Args:
                delay (float): The delay between each extraction request in seconds; change it if needed. Default is 2 seconds.
                infinityRequest (bool): If True, continuously extracts prices until manually stopped. Default is True.
                optionalDelay (float): Additional delay between each extraction request in seconds; if your internet connection is fast you can set this to 0 if not put 0.5> optionalDelay. Default is 0.
                link (str): The URL of the webpage from which to extract prices.
                element (str): The XPath of the HTML element containing the prices.
                exportInExcel (bool): If True, exports the extracted prices to an Excel file. Default is False.
                excelPath (str): The directory path where the Excel file will be saved. Default is current directory. Required if `exportInExcel` is True.
                *args: Variable positional arguments.
                **kwargs: Variable keyword arguments. Used to specify `timePeriod` if `infinityRequest` is False.

            Returns:
                None: This method does not return any value.

            Raises:
                ValueError: If `infinityRequest` is False and `timePeriod` is not an integer or not set.
                Exception: Any other exceptions that occur during the extraction process.

            Example usage:
                scraper = NobitexBot()
                scraper.getPrices(delay=3,
                                infinityRequest=True,
                                optionalDelay=0.5,
                                link="https://nobitex.ir/en/prices/",
                                element="/html/body/div/div/div/div/div[2]/div/section[3]/div/main/div/div/div[2]/table/tbody",
                                exportInExcel=True,
                                excelPath="./",
                                kwargs={"timePeriod": 60})
        """
        try:
            if exportInExcel:
                if element == None or link == None:
                    raise ValueError("Link or elements must be filled")
            
            if infinityRequest:
                while True:
                        self.driver.get(link)
                        
                        sleep(optionalDelay)
                        
                        selectedElement = self.driver.find_element(By.XPATH, element)
                        rawData = selectedElement.text
                        rawData = rawData.replace("Buy & Sell\n",'')
                        rawData = rawData.split('\n')
                        
                        before = 0
            
                        result = []
                        for i,text in enumerate(rawData):
                            if text.isdigit() and int(text) != 1:
                                result.append(rawData[before:i])
                                before = i
                                
                        if exportInExcel:
                            wb = Workbook()
                    
                            ws = wb.active
                            ws = wb.active
                            for row in result:
                                ws.append(row[1:5])

                            wb.save(excelPath + "prices.xlsx")
                        
                        
                        print("Prices updated successfully")      
                        sleep(delay)
                    
            else:
                for key , value in kwargs.items():
                    if key == "timePeriod" and isinstance(value,int):
                        timePeriod : int = value
                    else:
                        raise ValueError("Time period must be integer")
                    
                for i in range(timePeriod):
                    self.driver.get(link)
                    
                    sleep(optionalDelay)
                    
                    selectedElement = self.driver.find_element(By.XPATH, element)
                    rawData = selectedElement.text
                    rawData = rawData.replace("Buy & Sell\n",'')
                    rawData = rawData.split('\n')
                    
                    before = 0
        
                    result = []
                    for i,text in enumerate(rawData):
                        if text.isdigit() and int(text)!= 1:
                            result.append(rawData[before:i])
                            before = i
                            
                    if exportInExcel:
                        wb = Workbook()
                
                        ws = wb.active
                        ws = wb.active
                        for row in result:
                            ws.append(row[1:5])

                        wb.save(excelPath + "prices.xlsx")
                                        
                    sleep(delay)

        except Exception as e:
            import sys
            
            print(f"An error has occured during extraction process.\nmore details : {e}")
            self.driver.quit()
            
            sys.exit(1)
        

