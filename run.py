from booking.booking import Booking

# inst=Booking()
# inst.land_first_page()
#The above code will just open the chrome will not close it

#The below code automatically closes chrome once the task is done
try:
    with Booking() as bot:  #If I pass teardown as True here,then window will close after execution
        bot.land_first_page()
        bot.change_currency(currency='INR')
        bot.select_place_to_go(input("Where you want to go ?"))
        bot.select_dates(check_in_date=input("What is the check in date ?"),
                         check_out_date=input("What is the check out date ?"))
        bot.search_adults(int(input("How many people ?")))
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh() # A workaround to let our bot to grab the data properly
        bot.report_results()
        print("Exiting........")
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise