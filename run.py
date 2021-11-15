from booking.booking import Booking

# inst=Booking()
# inst.land_first_page()
#The above code will just open the chrome will not close it

#The below code automatically closes chrome once the task is done
try:
    with Booking() as bot:  #If I pass teardown as True here,then window will close after execution
        bot.land_first_page()
        # bot.change_currency(currency='INR')
        bot.select_place_to_go("Delhi")
        bot.select_dates("2021-11-16", "2021-11-18")
        bot.search_adults(1)
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