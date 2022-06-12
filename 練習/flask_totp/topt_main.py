from flask import Flask, render_template,redirect
from flask import request
app = Flask(__name__)

@app.route('/')
def main():
	return render_template('certificate_page.html')

@app.route('/check',methods=['POST'])
def check_passwd():
	from pyotp import totp
	if request.form['passwd']:
		totp_pass = request.form['passwd']
		atotp = totp.TOTP('brentchang') # brentchang is the key for generating totp
	if atotp.verify(totp_pass):
		return redirect(f'/login/user')
	else:
		return 'Sorry. Verify failed, please retry!<br><a href = "/">返回主頁</a> '

@app.route('/login/user')
def user_page():
	return 'hello, verfiy sucessfully<br><a href = "/">返回主頁</a> '

if __name__ == '__main__':
	app.run(debug=True)