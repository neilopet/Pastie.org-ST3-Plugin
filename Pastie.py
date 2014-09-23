'''
Pastie.org Upload Selection
for Sublime Text 3
neil.opet@gmail.com
'''

import os
import sublime
import sublime_plugin
import sys
import urllib

try:
	from urllib.parse import urlencode
	from urllib.request import urlopen
except ImportError:
	from urllib import urlencode, urlopen

class PastieUploadCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.syntaxes = {
			'ActionScript.tmLanguage': '2',
			'C.tmLanguage': '7',
			'C#.tmLanguage': '20',
			'C++.tmLanguage': '7',
			'Clojure.tmLanguage': '38',
			'CoffeeScript.tmLanguage': '40',
			'CSS.tmLanguage': '8',
			'D.tmLanguage': '26',
			'Diff.tmLanguage': '5',
			'Erlang.tmLanguage': '27',
			'Go.tmLanguage': '21',
			'Haskell.tmLanguage': '29',
			'HTML.tmLanguage': '11',
			'Java.tmLanguage': '9',
			'JavaScript.tmLanguage': '10',
			'JSON.tmLanguage': '10',
			'JSON Generic Array Elements.tmLanguage': '10',
			'LaTeX.tmLanguage': '37',
			'LaTeX Beamer.tmLanguage': '37',
			'LaTeX Memoir.tmLanguage': '37',
			'Lisp.tmLanguage': '25',
			'Literate Haskell.tmLanguage': '30',
			'Lua.tmLanguage': '23',
			'Makefile.tmLanguage': '31',
			'Objective-C.tmLanguage': '1',
			'Objective-C++.tmLanguage': '1',
			'Perl.tmLanguage': '18',
			'PHP.tmLanguage': '15',
			'Plain text.tmLanguage': '6',
			'Python.tmLanguage': '16',
			'Regular Expressions (Python).tmLanguage': '16',
			'Ruby.tmLanguage': '3',
			'Ruby Haml.tmLanguage': '12',
			'Ruby on Rails.tmLanguage': '4',
			'Scala.tmLanguage': '32',
			'SCSS.tmLanguage': '8',
			'Shell-Unix-Generic.tmLanguage': '13',
			'SQL.tmLanguage': '14',
			'SQL (Rails).tmLanguage': '14',
			'TeX.tmLanguage': '37',
			'TeX Math.tmLanguage': '37',
			'Textile.tmLanguage': '37',
			'XML.tmLanguage': '11',
			'YAML.tmLanguage': '19'
		}
		self.edit = edit
		tmp_syntax = os.path.basename(self.view.settings().get('syntax'))
		if (tmp_syntax in self.syntaxes):
			self.syntax = self.syntaxes[tmp_syntax]
		else:
			self.syntax = 6
		for region in self.view.sel():
			if not region.empty():
				self.selectedText = str(self.view.substr(region));
				self.post(self.selectedText)
	def post( self, text ):
		args = {
			'utf8': "✓",
			'paste[authorization]': "burger",
			'paste[access_key]': "",
			'paste[parser_id]': self.syntax,
			'paste[body]': text,
			'paste[restricted]': "1",
			'commit': "Create Paste"
		}
		try:
			response = urlopen(url="http://pastie.org/pastes", data=urlencode(args).encode('utf8')).geturl()
		except urllib.error.HTTPError as err:
			sublime.error_message(str(err.code) + "\n" + str(err.reason))
		sublime.set_clipboard(str(response))
		sublime.status_message("Text submitted to pastie.org. " + str(response) + " is copied to your clipboard.")
