# I have created this file
#code for video 6 from line 4 to line 10

#from django.http import HttpResponse

#def about(request):
   # return HttpResponse(' hey there! this is me learning django')

#def index(request):
   # return HttpResponse(' <h2>code with harry </h2>  <a href= " https://online.codingblocks.com/app/classroom/course/17/run/320" > Competitive programming CB </a>  ')


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
     #phrase = { 'name': "Deepti" , 'place': 'narnaul'}
     return render(request, 'index.html')
     #return HttpResponse("Home")





def analyse(request):
      # GET the text
      djtext= request.POST.get('text','default')

      #to check the checkbox value

      removepunc=request.POST.get('removepunc', 'off')
      capitalise= request.POST.get('capitalise', 'off')
      NewLineRemover= request.POST.get('NewLineRemover', 'off')
      Extraspaceremover= request.POST.get('Extraspaceremover', 'off')



      if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose':'punctuations are removed', 'analysis': analysed}
        return render(request, 'analyse.html', params)

      elif(capitalise== "on"):
          analysed=""
          for char in djtext:
              analysed = analysed+ char.upper()
          params = {'purpose': 'All letters are capital', 'analysis': analysed}
          return render(request, 'analyse.html', params)

      elif(NewLineRemover== 'on'):
          analysed= ""
          for char in djtext:
              if char != "\n" and char!="\r" :
                  analysed= analysed + char

          params= {'purpose':' New line is removed', 'analysis': analysed}
          return render(request, 'analyse.html',params)

      elif(Extraspaceremover=='on'):
          analysed=" "
          for index, char in enumerate(djtext):
              #if  djtext[index]==" " and djtext[index+1]== " " :
                 # pass
             # else:
                  #analysed= analysed+ djtext

              if not (djtext[index] == " " and djtext[index + 1] == " "):
                  analysed = analysed + djtext

          params = {'purpose': ' Extra space is removed', 'analysis': analysed}
          return render(request, 'analyse.html', params)


      else:
        return HttpResponse("Error")









# def spaceremove(request):
   # return HttpResponse("removes the space")

#def capitalisefirst(request):
 #   return HttpResponse("capitalises the first letter <a href='/' >back </a> ")

#def lineremove(request):
 #   return HttpResponse("removes the line")

#def charcount(request):
   # return HttpResponse("count char")



