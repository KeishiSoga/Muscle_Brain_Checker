# 脳筋最強習慣アプリ

身体を鍛え、脳を鍛え、周りを笑顔にする。"脳筋最強"の新習慣アプリ。

## 機能

- 4つのチェック項目で毎日の習慣を記録
  - 運動しましたか？
  - 脳を鍛えましたか（勉強しましたか？）
  - 何か新しいことに挑戦していますか？
  - 周りを笑顔にするようにユーモアを発揮しましたか？
- チェック数に応じた励ましメッセージ
- 書籍へのリンク

## セットアップ

### 1. 仮想環境の作成

```bash
python3 -m venv venv
```

### 2. 仮想環境のアクティベート

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 4. アプリの起動

```bash
python app.py
```

ブラウザで `http://127.0.0.1:5001` にアクセスしてください。

## Renderへのデプロイ

### 1. Renderアカウントの作成
1. [Render](https://render.com)にアクセスしてアカウントを作成
2. GitHubアカウントと連携

### 2. 新しいWebサービスの作成
1. Renderのダッシュボードで「New +」→「Web Service」を選択
2. GitHubリポジトリを選択（または接続）
3. 以下の設定を行う：
   - **Name**: `brain-musle-app`（任意の名前）
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: `Free`

### 3. 環境変数の設定（オプション）
- **SECRET_KEY**: セッション用の秘密鍵（任意の文字列、例：`your-secret-key-here`）
  - 設定しない場合、アプリ起動時に自動生成されます

### 4. デプロイ
「Create Web Service」をクリックしてデプロイを開始します。数分で完了します。

### 5. アクセス
デプロイ完了後、Renderが提供するURL（例：`https://brain-musle-app.onrender.com`）でアプリにアクセスできます。

## ファイル構成

```
Brain_Musle/
├── app.py              # Flaskアプリケーション
├── requirements.txt    # 依存パッケージ
├── Procfile            # Render用の起動コマンド
├── render.yaml         # Render用の設定ファイル（オプション）
├── templates/
│   └── index.html      # メイン画面
├── static/
│   ├── style.css       # スタイルシート
│   └── 表紙.png        # 書籍の表紙画像
└── README.md           # このファイル
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

