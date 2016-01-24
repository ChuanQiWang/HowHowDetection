filename = File.open('yahoo_list','r')
text = filename.readline()
st = []
while text != nil
    begin 
      st.push(text)
      text = filename.readline()
      s = "python2 ./Demo.py 2 ./yahoo/" + text.chomp + ">> yahoo.log"
      system(s)
    rescue EOFError
        break
    end
end 
filename.close()
