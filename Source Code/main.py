__verson__="1.0"

import kivy
import kivymd
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivymd.uix.textfield import MDTextFieldRound, MDTextFieldRect
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton,MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
import wikipedia
from kivy.uix.button import Button
from PyDictionary import PyDictionary
from kivy.uix.textinput import TextInput
from jnius import cast
from jnius import autoclass

kivy.require('1.11.1')



script = """
ScreenManager:
    Page_One:
    Next_Screen:
	Denote:
	
<Page_One>:
    name:'page_one'
    
    
	MDIconButton:
		icon:'ig.jpeg'
		pos_hint:{'center_x':0.94,'center_y':0.94}
		size_hint:0.06,0.05
		allow_stretch: True
		on_press:
			root.insta()

	Image:
		source:'font.png'
		pos_hint:{'center_x':0.5,'center_y':0.8}
		size_hint_x: 0.95
		
		height:500
		allow_stretch: True
	
	Image:
		source:'font2.png'
		pos_hint:{'center_x':0.5,'center_y':0.7}
		size_hint_x: 0.95
		allow_stretch: True
	
	

	
    MDRoundFlatButton:
        text:'[b][i]Click to start Your Search[/i][/b]'
        font_size:15
        markup:True
        pos_hint:{'center_x':0.49,'center_y':0.5}
        size_hint:0.6,0.1
        on_press:
            root.manager.transition.direction='left'
            root.manager.transition.duration= 0.3
            root.manager.current='next_screen'

            
    MDRoundFlatButton:
        text:'[b]About[/b]'
        markup:True
        pos_hint:{'center_x':0.88,'center_y':0.06}
        size_hint:0.2,0.06
        on_press:
            root.about() 

	MDRoundFlatButton:
        text:'[b]Rate us.[/b]'
        markup:True
        pos_hint:{'center_x':0.2,'center_y':0.06}
        size_hint:0.3,0.06
        
            
        
	
	MDRoundFlatButton:
        text:'[b]Denoting us.[/b]'
        markup:True
        pos_hint:{'center_x':0.55,'center_y':0.06}
        size_hint:0.3,0.06
        on_press:
        	root.manager.transition.direction='down'
            root.manager.transition.duration= 0.3
            root.manager.current='denote'
           
            
            

<Next_Screen>:
    name:'next_screen'
    MDTextFieldRound:
        id:search
        required:True
        hint_text: 'Search'
        size_hint:0.70,0.07
        pos_hint: {'center_x':0.42,'center_y':0.95}
        font_size:'20sp'
        normal_color:0.8,0.8,0.8,1
        color_active:1,1,1,1
        on_text_validate:
            root.on_click()
        

    MDRoundFlatButton:
        id:go
        text:'Go'
        pos_hint:{'center_x':0.92,'center_y':0.95}
        size_hint:0.14,0.06
        focus:False
        on_press:
            root.on_click()
    
    
    MDTextFieldRect:
        id:result
        line_anim:True
        hint_text: 'Answer.....'
        size_hint:0.80,0.9
        pos_hint: {'center_x':0.41,'center_y':0.45}
        font_size:'15sp'
        readonly:True


    MDRoundFlatButton:
		text:'Grammer'
		font_size:12
		background_color:1,1,1,1
		pos_hint:{'center_x':0.91,'center_y':0.82}
		size_hint:0.16,0.08
		on_press:
		    root.grammer()



    MDRoundFlatButton:
        text:'Google it!'
        font_size:12
        pos_hint:{'center_x':0.91,'center_y':0.72}
        size_hint:0.18,0.08
        on_press:
            root.google_it()

    MDRoundFlatButton:
        text:'Copy'
        font_size:12
        pos_hint:{'center_x':0.91,'center_y':0.62}
        size_hint:0.17,0.08
        on_press:
            root.text_copy()



    
    MDRoundFlatButton:
        text:'Clear'
        font_size:12
        background_color:1,1,1,1
        pos_hint:{'center_x':0.91,'center_y':0.52}
        size_hint:0.16,0.08
        on_press:
            root.clear_all()

	
	

	MDRoundFlatButton:
	    text:'[b]Back[/b]'
	    markup:True
	    pos_hint:{'center_x':0.91,'center_y':0.35}
	    size_hint:0.16,0.06
	    on_press:
	    	root.manager.transition.direction='right'
            root.manager.transition.duration= 0.3
            root.manager.current='page_one'

	        
	
	MDRoundFlatButton:
        text:'[b]Donate[/b]'
        markup:True
        pos_hint:{'center_x':0.91,'center_y':0.15}
        size_hint:0.16,0.06
        on_press:
            root.manager.transition.direction='down'
            root.manager.transition.duration= 0.3
            root.manager.current='denote'
            

    MDRoundFlatButton:
        text:'[b]About[/b]'
        markup:True
        pos_hint:{'center_x':0.91,'center_y':0.068}
        size_hint:0.16,0.06
        on_press:
            root.about()   




	       
<Denote>:
	name:'denote'
	MDRoundFlatButton:
	    text:'[b]Back[/b]'
	    markup:True
	    pos_hint:{'center_x':0.91,'center_y':0.1}
	    size_hint:0.16,0.06
	    on_press:
	    	root.manager.transition.direction='up'
            root.manager.transition.duration= 0.3
            root.manager.current='page_one'
            

	        
	Image:
		source: 'paytm.jpg'
		size: self.texture_size
		pos_hint:{'center_x':0.5,'center_y':0.65}
		
	Label:
		text:'Please Scan above QR for denote via Paytm.'
		pos_hint:{'center_x':0.5,'center_y':0.3}
		color:0,0,0,1
       
	Label:
		text:'A help of small amount[b] rs.50[/b] or[b] $3 USD[/b],'
		pos_hint:{'center_x':0.5,'center_y':0.26}
		color:0,0,0,1
		markup:True
	Label:
		text:'[b] will be a Great help[/b].'
		markup:True
		pos_hint:{'center_x':0.5,'center_y':0.22}
		color:0,0,0,1
		
"""




class Page_One(Screen):

    def about(self):
    	dialog=MDDialog(title='About',text='This Application is created by Mohit Devli from India (uttrakhand).\n'
                                           'Project-Shri Guru Ram Rai Karanpryag\nSubject-Computer Sceince Grapics Design',size_hint=(0.8,0.2))
    	dialog.open()	


    def insta(self):
        url='https://www.instagram.com/mohit_deoli/'

        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')

        intent = Intent()
        intent.setAction(Intent.ACTION_VIEW)
        intent.setData(Uri.parse(url))


        self.currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        self.currentActivity.startActivity(intent)
		
        self.currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        self.currentActivity.startActivity(intent)



class Next_Screen(Screen):

    def on_click(self):
        
        try:
        
            query = self.ids.search
            result_text = self.ids.result
            text_query=query.text
            result_text.hint_text=str('Searching..........')
            results = wikipedia.summary(text_query,sentences = 6,auto_suggest=False)
            result_text.text=results
            result_text.foreground_color = (0, 0, 0, 1)


        except:
        	
            result_text.text = "Oops! Ther is no Matching Results or There is no Internet Connection, or Some Problem Regarding to Network"
            
       
            result_text.foreground_color=(1,0,0,1)

    def grammer(self):
    
        query=self.ids.search
        result_text=self.ids.result
        result_text.hint_text='Searching......'
        dic=PyDictionary()
        gram=dic.meaning(query.text)

        result_text.text=str(gram)
        
    	
    	    

    def text_copy(self):
        result_text = self.ids.result
        result_text.copy(data=result_text.text)
	
    def google_it(self):
        query = self.ids.search
        url='https://www.google.com/search?q='+str(query.text)
        
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')

        intent = Intent()
        intent.setAction(Intent.ACTION_VIEW)
        intent.setData(Uri.parse(url))


        self.currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        self.currentActivity.startActivity(intent)
		
        self.currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        self.currentActivity.startActivity(intent)
		


    def clear_all(self):
        query = self.ids.search
        result_text = self.ids.result
        query.text=''
        result_text.text=''
        
    
    def about(self):
        dialog=MDDialog(title='About',text='This Application is created by Mohit Devli from India (uttrakhand).\n'
                                           'Project-Shri Guru Ram Rai Karanpryag\nSubject-Computer Sceince Grapics Design' ,size_hint=(0.8,0.2) )
        dialog.open() 
        



class Denote(Screen):
	pass	



   
sm=ScreenManager()
sm.add_widget(Page_One(name='page_one'))
sm.add_widget(Next_Screen(name='next_screen'))
sm.add_widget(Denote(name='denote'))



class WikoPediaApp(MDApp):
    def build(self): 
        script_kv=Builder.load_string(script)
        return script_kv

WikoPediaApp().run()

