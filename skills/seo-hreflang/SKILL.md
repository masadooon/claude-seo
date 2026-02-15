---
name: seo-hreflang
description: >
  hreflangおよび国際SEOの監査、検証、生成。よくあるミスの検出、言語・地域コードの
  検証、正しいhreflang実装の生成を行います。ユーザーが「hreflang」「i18n SEO」
  「international SEO」「多言語」「多地域」「language tags」と言った場合に使用します。
---

# Hreflang & International SEO

既存のhreflang実装を検証するか、多言語・多地域サイト向けに正しいhreflangタグを
生成します。HTML、HTTPヘッダー、XMLサイトマップでの実装に対応しています。

## 検証チェック

### 1. 自己参照タグ
- すべてのページは、自分自身を指すhreflangタグを含める必要があります
- 自己参照URLは、そのページのcanonical URLと完全に一致する必要があります
- 自己参照タグが欠落すると、Googleはhreflangセット全体を無視します

### 2. リターンタグ
- ページAがhreflangでページBにリンクしている場合、ページBもページAにリンクを返す必要があります
- すべてのhreflang関係は双方向でなければなりません（A→BかつB→A）
- リターンタグが欠落すると、両方のページのhreflangシグナルが無効になります
- すべての言語バージョンが相互に参照していることを確認してください（フルメッシュ）

### 3. x-defaultタグ
- 必須：一致しない言語・地域に対するフォールバックページを指定します
- 通常、言語選択ページまたは英語版を指します
- alternateセットごとにx-defaultは1つだけです
- 他のすべての言語バージョンからのリターンタグも必要です

### 4. 言語コードの検証
- ISO 639-1の2文字コードを使用する必要があります（例：`en`、`fr`、`de`、`ja`）
- よくあるエラー：
  - `en`ではなく`eng`を使用（ISO 639-2であり、hreflangでは無効）
  - `ja`ではなく`jp`を使用（日本語の正しいコードではない）
  - 地域修飾子なしの`zh`（曖昧 — `zh-Hans`または`zh-Hant`を使用）

### 5. 地域コードの検証
- オプションの地域修飾子はISO 3166-1 Alpha-2を使用します（例：`en-US`、`en-GB`、`pt-BR`）
- 形式：`language-REGION`（言語は小文字、地域は大文字）
- よくあるエラー：
  - `en-GB`ではなく`en-uk`を使用（UKは有効なISO 3166-1コードではない）
  - `es-LA`（ラテンアメリカは国ではない — 具体的な国を使用）
  - 言語プレフィックスなしの地域コード

### 6. Canonical URLとの整合性
- hreflangタグはcanonical URLにのみ配置する必要があります
- ページに別のURLを指す`rel=canonical`がある場合、そのページのhreflangは無視されます
- canonical URLとhreflang URLは完全に一致する必要があります（末尾のスラッシュを含む）
- 非canonicalページはhreflangセットに含めるべきではありません

### 7. プロトコルの一貫性
- hreflangセット内のすべてのURLは同じプロトコルを使用する必要があります（HTTPSまたはHTTP）
- hreflangセット内でHTTP/HTTPSが混在すると検証エラーが発生します
- HTTPS移行後は、すべてのhreflangタグをHTTPSに更新してください

### 8. クロスドメイン対応
- hreflangは異なるドメイン間で機能します（例：example.comとexample.de）
- クロスドメインのhreflangには、両方のドメインでリターンタグが必要です
- 両方のドメインがGoogle Search Consoleで確認済みであることを検証してください
- クロスドメイン構成にはサイトマップベースの実装を推奨します

## よくあるミス

| 問題 | 重大度 | 修正方法 |
|------|--------|----------|
| 自己参照タグの欠落 | Critical | 同じページURLを指すhreflangを追加 |
| リターンタグの欠落（A→Bはあるが、B→Aがない） | Critical | すべてのalternateに対応するリターンタグを追加 |
| x-defaultの欠落 | High | フォールバック/選択ページを指すx-defaultを追加 |
| 無効な言語コード（例：`eng`） | High | ISO 639-1の2文字コードを使用 |
| 無効な地域コード（例：`en-uk`） | High | ISO 3166-1 Alpha-2コードを使用 |
| 非canonical URLでのhreflang | High | hreflangをcanonical URLにのみ配置 |
| URL内のHTTP/HTTPSの不一致 | Medium | すべてのURLをHTTPSに統一 |
| 末尾スラッシュの不一致 | Medium | canonical URLの形式と完全に一致させる |
| HTMLとサイトマップの両方にhreflangがある | Low | 1つの方法を選択 — 大規模サイトにはサイトマップを推奨 |
| 必要な場合に地域なしの言語コード | Low | 地域ターゲティングコンテンツには地域修飾子を追加 |

## 実装方法

### 方法1：HTMLリンクタグ
最適な用途：1ページあたりの言語・地域バリエーションが50未満のサイト。

```html
<link rel="alternate" hreflang="en-US" href="https://example.com/page" />
<link rel="alternate" hreflang="en-GB" href="https://example.co.uk/page" />
<link rel="alternate" hreflang="fr" href="https://example.com/fr/page" />
<link rel="alternate" hreflang="x-default" href="https://example.com/page" />
```

`<head>`セクション内に配置します。すべてのページは自分自身を含むすべてのalternateを含める必要があります。

### 方法2：HTTPヘッダー
最適な用途：非HTMLファイル（PDF、ドキュメント）。

```
Link: <https://example.com/page>; rel="alternate"; hreflang="en-US",
      <https://example.com/fr/page>; rel="alternate"; hreflang="fr",
      <https://example.com/page>; rel="alternate"; hreflang="x-default"
```

サーバー設定またはCDNルールで設定します。

### 方法3：XMLサイトマップ（大規模サイトに推奨）
最適な用途：多くの言語バリエーション、クロスドメイン構成、または50ページ以上のサイト。

以下のHreflangサイトマップ生成セクションを参照してください。

### 方法の比較
| 方法 | 最適な用途 | メリット | デメリット |
|------|-----------|----------|-----------|
| HTMLリンクタグ | 小規模サイト（50バリエーション未満） | 実装が容易、ソースで確認可能 | `<head>`が肥大化、大規模での保守が困難 |
| HTTPヘッダー | 非HTMLファイル | PDF、画像に対応 | サーバー設定が複雑、HTMLで確認不可 |
| XMLサイトマップ | 大規模サイト、クロスドメイン | スケーラブル、一元管理 | ページ上で確認不可、サイトマップの保守が必要 |

## Hreflang生成

### プロセス
1. **言語の検出**：サイトをスキャンして言語指標を確認（URLパス、サブドメイン、TLD、HTML lang属性）
2. **ページの対応付け**：言語・地域間で対応するページをマッチング
3. **言語コードの検証**：すべてのコードをISO 639-1およびISO 3166-1に照合して検証
4. **タグの生成**：自己参照を含む各ページのhreflangタグを作成
5. **リターンタグの検証**：すべての関係が双方向であることを確認
6. **x-defaultの追加**：各ページセットにフォールバックを設定
7. **出力**：実装コードを生成（HTML、HTTPヘッダー、またはサイトマップXML）

## Hreflangサイトマップ生成

### hreflang付きサイトマップ
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://example.com/page</loc>
    <xhtml:link rel="alternate" hreflang="en-US" href="https://example.com/page" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/page" />
    <xhtml:link rel="alternate" hreflang="de" href="https://example.de/page" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/page" />
  </url>
  <url>
    <loc>https://example.com/fr/page</loc>
    <xhtml:link rel="alternate" hreflang="en-US" href="https://example.com/page" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/page" />
    <xhtml:link rel="alternate" hreflang="de" href="https://example.de/page" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/page" />
  </url>
</urlset>
```

重要なルール：
- `xmlns:xhtml`名前空間宣言を含めること
- すべての`<url>`エントリは、自分自身を含むすべての言語alternateを含める必要があります
- 各alternateは、独自の完全なセットを持つ個別の`<url>`エントリとして記載する必要があります
- サイトマップファイルあたり50,000 URLで分割

## 出力

### Hreflang検証レポート

#### サマリー
- スキャンしたページ総数：XX
- 検出された言語バリエーション：XX
- 発見された問題：XX（Critical: X、High: X、Medium: X、Low: X）

#### 検証結果
| 言語 | URL | 自己参照 | リターンタグ | x-default | ステータス |
|------|-----|----------|-------------|-----------|-----------|
| en-US | https://... | ✅ | ✅ | ✅ | ✅ |
| fr | https://... | ❌ | ⚠️ | ✅ | ❌ |
| de | https://... | ✅ | ❌ | ✅ | ❌ |

### 生成されたHreflangタグ
- HTML `<link>`タグ（HTML方式を選択した場合）
- HTTPヘッダー値（ヘッダー方式を選択した場合）
- `hreflang-sitemap.xml`（サイトマップ方式を選択した場合）

### 推奨事項
- 追加すべき欠落した実装
- 修正すべき不正なコード
- 方式移行の提案（例：スケーリングのためHTML → サイトマップ）
