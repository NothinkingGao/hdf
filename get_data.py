import requests

url = "https://www.haodf.com/ndisease/ajaxLoadMoreDoctor"
data={
   "nowPage":3,
   "pageSize":15,
   "placeId":"",
   "termId":462
}
headers = {
   "authority":"www.haodf.com",
   "method":"POST",
   "path":"/ndisease/ajaxLoadMoreDoctor",
   "scheme":"https",
   "accept":"*/*",
   "accept-encoding":"gzip, deflate, br",
   "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
   "content-length":"41",
   "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
   "cookie":"Hm_lvt_dfa5478034171cc641b1639b2a5b717d=1681358019; g=HDF.22.64347c21e38e4; krandom_a119fcaa84=806705; __bid_n=18778c95bff3eefd244207; FPTOKEN=m8m0t90CtGM/3qF39jGJKzqpsxviBId10LnoXIzPyHEemIk+GgEUmPJCQxe7/HD6eN9BHF72ffy16z3DZg1DJ2ETy4fW8vER0K1MaRQJAV9isHYF4LsgwEZ01F48Bklc13eMHZUHFQ8wNkIHD6vbnVAYhMzBG55bGS0X8u+4uJ27D3xLkzsIcg+hgd11dEyWQj28B1bsU5xRxY7/+0hQ7q0aevtwk5j9oiCblp96T4sdvgEUVnjJrrQf7WYLMO5aS4u0KEdvhLlwCQPVXehhONO0aEK7mgckzuepBNfLPyQuz7wbF8MEJgAO36YG/8FOEBBfvH+mJiIBLCLVIBOML++ZBKDjOF+NUQiaxsEn7nY4tnce1bxQMCPmZgxvJKyUNToabde9+So9U2pp2EIy1Q==|5XGbV0aFwM3RrHZ1BSooukVjdmuv1gqx9a2bSwozg2E=|10|b9a672794b92555df63a1db363853141; acw_tc=dcb5873716813656070631281ebf9966a187adcc875ffd9e29b77e141f; Hm_lpvt_dfa5478034171cc641b1639b2a5b717d=1681366313",
   "origin":"https://www.haodf.com",
   "referer":"https://www.haodf.com/citiao/jibingfenlei-xinzangbing/tuijian-doctor.html?p=2",
   "sec-ch-ua":'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
   "sec-ch-ua-mobile":"?0",
   "sec-ch-ua-platform":"macOS",
   "sec-fetch-dest":"empty",
   "sec-fetch-mode":"cors",
   "sec-fetch-site":"same-origin",
   "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
   "x-requested-with":"XMLHttpRequest",
}
response = requests.post(url,data=data,headers = headers)
print(response.text)
