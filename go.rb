filename = File.open('how_list','r')
text = filename.readline()
st = []
while text != nil
    begin 
      st.push(text)
      text = filename.readline()
      s = "python2 ./Demo.py 0 ./how/" + text.chomp + ">> how.log"
      system(s)
    rescue EOFError
        break
    end
end 
filename.close()
