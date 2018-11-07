import urllib.request; #用來建立請求
import urllib.parse;

def example_1(): #example-1，試著存取網頁
    x = urllib.request.urlopen('https://www.google.com');
    print(x.read()); #呈現請求後的結果…出現一堆看不懂的資料

def example_2():#example-2，試著用參數來進行查詢
    url = 'http://pythonprogramming.net';
    values = {'s':'basic',
              'submit':'search'}; #參數及參數值
    data = urllib.parse.urlencode(values); #解析並轉為url編碼格式
    data = data.encode('utf-8'); #將所有網址用utf8解碼
    req = urllib.request.Request(url, data); #建立請求
    resp = urllib.request.urlopen(req); #開啟網頁
    respData = resp.read();
    print(respData);

def example_3():#example-3，試著存取google，以關鍵字python來查詢
    try:
        url = 'https://www.google.com.tw/search?q=python' ;
        x = urllib.request.urlopen(url);
        print('example-3', x.read());
    except Exception as e:
        print('example-3', str(e));

    #=>出現HTTP Error 403: Forbidden錯誤
    
    
def example_4():#example-4 試著變更headers的資訊來存取google網頁的資訊
    try:   
        url = 'https://www.google.com.tw/search?q=python';
        #url = 'https://www.google.com.tw/#q=python'; #雖然在google網址上看到搜尋時是這個方式，但是實際操作起來是不成功的   
        headers = {};
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17';
        #headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0';
        req = urllib.request.Request(url, headers=headers);
        resp = urllib.request.urlopen(req);
        respData = str(resp.read().decode('utf-8')); #將所得的資料解碼
        saveFile = open('withHeaders.txt','w', encoding='utf8');
        saveFile.write(str(respData));
        saveFile.close();
    except Exception as e:
        print(str(e));
        
if __name__ == '__main__':
    example_4()
