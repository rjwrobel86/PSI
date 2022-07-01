import requests

links = ["https://www.schmittchevrolet.com","https://www.jackschmitt.com","https://www.steveschmittauto.com","https://www.londoff.com","https://www.webergranitecitychevy.com"]
stores = ['JSCWR','OFallon','Steve Schmitt','Londoff','Weber GC']

fcps = []
fids = []
lcps = []
clss = []

for i in links:
    x = requests.get("https://www.googleapis.com/pagespeedonline/v5/runPagespeed", params={"url":i,"strategy":"mobile","key":"APIKEYGOESHERE"})
    data = x.json()
    
    fcp = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"] #into seconds (/1000)
    fid = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["percentile"] #into seconds (/1000)
    lcp = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["percentile"]
    cls = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["percentile"]/100
    
    fcps.append(fcp)
    fids.append(fid)
    lcps.append(lcp)
    clss.append(cls)

print("First Contentful Display (MS): " + str(fcps))
print("First Input Delay (MS): " + str(fids))
print("Largest Contentful Paint (MS): " + str(lcps))
print("Cumulative Layout Shift: " + str(clss))


