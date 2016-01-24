filename = File.open('jserv_list','r')
text = filename.readline()
st = []
while text != nil
    begin 
      st.push(text)
      text = filename.readline()
      s = "python2 ./Demo.py 1 ./jserv/" + text.chomp + ">> jserv.log"
      system(s)
    rescue EOFError
        break
    end
end 
filename.close()
