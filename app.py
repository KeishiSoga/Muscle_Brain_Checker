from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import os

app = Flask(__name__)
# セッション用の秘密鍵（本番環境では環境変数から取得、開発環境ではランダム生成）
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24).hex())

@app.route('/')
def index():
    # 今日の日付を取得
    today = datetime.now().strftime('%Y-%m-%d')
    
    # セッションから今日のチェック状態を取得
    checks = session.get('checks', {})
    today_checks = checks.get(today, {
        'exercise': False,
        'study': False,
        'challenge': False,
        'smile': False
    })
    
    # チェック数をカウント
    count = sum([
        today_checks['exercise'],
        today_checks['study'],
        today_checks['challenge'],
        today_checks['smile']
    ])
    
    return render_template('index.html', 
                         checks=today_checks, 
                         count=count,
                         today=today)

@app.route('/check', methods=['POST'])
def check():
    today = datetime.now().strftime('%Y-%m-%d')
    
    # セッションから今日のチェック状態を取得
    if 'checks' not in session:
        session['checks'] = {}
    
    if today not in session['checks']:
        session['checks'][today] = {
            'exercise': False,
            'study': False,
            'challenge': False,
            'smile': False
        }
    
    # すべてのチェックボックスの状態を更新
    check_types = ['exercise', 'study', 'challenge', 'smile']
    for check_type in check_types:
        value = request.form.get(check_type)
        if value is not None:
            session['checks'][today][check_type] = value == 'true'
    
    session.modified = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

