#to convert amr file to mp3
for f in os.listdir(output_dir):
    print( f)
    f_name=f.replace('.amr','.mp3')
    os.rename(os.path.join(output_dir,f), os.path.join(output_dir, f.replace(f,f_name)))

the above code will convert amr files to mp3 this is the most easiest way to convert and it dosent affect the bit rate too 
just give directory name where amr files are ther and simply renmae then , by modifying the code one can change to any format
that is amr to mp3 , or wav to mp3 and vice versa
