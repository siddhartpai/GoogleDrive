from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


def upload():
	fileName=raw_input('Enter FileName: ')
	gsFile=drive.CreateFile()
	gsFile.SetContentFile(fileName)
	gsFile.Upload()

def download():
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	i=1
	idList=[]
	fileList=[]
	print '\n'
	for file in file_list:
		print str(i)+'. '+file['title']+'\t'+file['createdDate']
		i+=1
		idList.append(file['id'])
		fileList.append(file['title'])	
	id=input('Enter FileId to be Downloaded: ')
	gsFile=drive.CreateFile({'id':idList[id-1]})
	gsFile.GetContentFile(fileList[id-1])
def main():
	choice=input('1.Upload\n2.Download\n3.Exit\n >> ');
	if(choice==1):
		upload();
		print 'Upload Successful'
	elif(choice==2):
		download();
		print 'Download Successful'
	elif(choice==3):
		exit();
		

if(__name__=='__main__'):
	main()
