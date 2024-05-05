# # task_app/context_processors.py

# def custom_context_processor(request):
#     # Define your custom context variables here
#     user_agent = request.META.get('HTTP_USER_AGENT')
#     print("User Agent:", user_agent)  # Print user agent string to console for debugging

#     is_desktop = True
#     if user_agent:
#         is_desktop = 'mobile' not in user_agent.lower()
    
#     return {'is_desktop': is_desktop}
def custom_context_processor(request):
    # Define your custom context variables here
    user_agent = request.META.get('HTTP_USER_AGENT')
    print("User Agent:", user_agent)  # Print user agent string to console for debugging

    is_desktop = True
    if user_agent:
        is_desktop = 'mobile' not in user_agent.lower()

    # Check screen width
    screen_width = request.GET.get('screen_width')
    if screen_width:
        is_desktop = int(screen_width) >= 768  # Adjust threshold as needed

    return {'is_desktop': is_desktop}
