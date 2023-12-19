import pyttsx3,PyPDF2                                  
pdfreader = PyPDF2.PdfFileReader(open('book.pdf','rb'))#Change the file with your file
speaker = pyttsx3.init()
for page_num in range(pdfreader.numPages):   
    text = pdfreader.getPage(page_num).extractText()   #Extracting text from the PDF
    cleaned_text = text.strip().replace('\n',' ')      #Removes unnecessary spaces and break lines
    print(cleaned_text)                                #Print the text from PDF
    speaker.save_to_file(cleaned_text,'book.mp3')      #Saving Text In a audio file 'story.mp3'
    speaker.runAndWait()
speaker.stop()
