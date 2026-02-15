<!-- Updated: 2026-02-07 -->
---
name: seo-images
description: >
  SEOとパフォーマンスのための画像最適化分析。alt テキスト、ファイルサイズ、
  フォーマット、レスポンシブ画像、遅延読み込み、CLS 防止をチェックします。
  ユーザーが「画像最適化」「alt テキスト」「画像SEO」「画像サイズ」
  「画像監査」と言った場合に使用します。
---

# 画像最適化分析

## チェック項目

### Alt テキスト
- すべての `<img>` 要素に存在すること（装飾用画像は除く: `role="presentation"`）
- 説明的であること: 画像の内容を説明し、"image.jpg" や "photo" ではないこと
- 関連キーワードを自然に含めること。キーワードの詰め込みはしない
- 長さ: 10〜125文字

**良い例:**
- "Professional plumber repairing kitchen sink faucet"
- "Red 2024 Toyota Camry sedan front view"
- "Team meeting in modern office conference room"

**悪い例:**
- "image.jpg"（ファイル名であり、説明ではない）
- "plumber plumbing plumber services"（キーワードの詰め込み）
- "Click here"（説明的ではない）

### ファイルサイズ

**画像カテゴリ別の段階的しきい値:**

| 画像カテゴリ | 目標 | 警告 | 危険 |
|----------------|--------|---------|----------|
| サムネイル | < 50KB | > 100KB | > 200KB |
| コンテンツ画像 | < 100KB | > 200KB | > 500KB |
| ヒーロー/バナー画像 | < 200KB | > 300KB | > 700KB |

品質を損なわない範囲で、目標しきい値への圧縮を推奨します。

### フォーマット
| フォーマット | ブラウザサポート | 用途 |
|--------|-----------------|----------|
| WebP | 97%以上 | デフォルトの推奨 |
| AVIF | 92%以上 | 最高の圧縮率、より新しい |
| JPEG | 100% | 写真のフォールバック |
| PNG | 100% | 透過のあるグラフィック |
| SVG | 100% | アイコン、ロゴ、イラスト |

JPEG/PNG よりも WebP/AVIF を推奨します。フォーマットのフォールバック付き `<picture>` 要素を確認してください。

#### 推奨される `<picture>` 要素パターン

最も効率的なフォーマットを先頭にしたプログレッシブエンハンスメントを使用します:

```html
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Descriptive alt text" width="800" height="600" loading="lazy" decoding="async">
</picture>
```

ブラウザは最初にサポートされているフォーマットを使用します。現在のブラウザサポート: AVIF 93.8%、WebP 95.3%。

#### JPEG XL — 新興フォーマット

2025年11月、Google の Chromium チームは2022年の決定を覆し、Rust ベースのデコーダーを使用して Chrome に JPEG XL サポートを復活させると発表しました。実装は機能的に完了していますが、Chrome の安定版にはまだ搭載されていません。JPEG XL はロスレス JPEG 再圧縮（品質劣化なしで約20%の削減）と競争力のある非可逆圧縮を提供します。Web での実用的な展開にはまだ至っていませんが、将来の普及に向けて注視する価値があります。

### レスポンシブ画像
- 複数サイズ用の `srcset` 属性
- レイアウトのブレークポイントに一致する `sizes` 属性
- デバイスピクセル比に適した解像度

```html
<img
  src="image-800.jpg"
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 600px) 400px, (max-width: 1200px) 800px, 1200px"
  alt="Description"
>
```

### 遅延読み込み
- ファーストビュー外の画像に `loading="lazy"` を設定
- ファーストビュー内/ヒーロー画像には遅延読み込みを使用しないこと（LCP に悪影響）
- ネイティブと JavaScript ベースの遅延読み込みを確認

```html
<!-- ファーストビュー外 - 遅延読み込み -->
<img src="photo.jpg" loading="lazy" alt="Description">

<!-- ファーストビュー内 - 即時読み込み（デフォルト） -->
<img src="hero.jpg" alt="Hero image">
```

### LCP 画像への `fetchpriority="high"`

ブラウザのネットワークキューでダウンロードを優先させるため、ヒーロー/LCP 画像に `fetchpriority="high"` を追加します:

```html
<img src="hero.webp" fetchpriority="high" alt="Hero image description" width="1200" height="630">
```

**重要:** ファーストビュー内/LCP 画像には遅延読み込みを使用しないでください。LCP 画像に `loading="lazy"` を使用すると、LCP スコアに直接悪影響を与えます。`loading="lazy"` はファーストビュー外の画像にのみ使用してください。

### 非 LCP 画像への `decoding="async"`

画像のデコードがメインスレッドをブロックしないよう、非 LCP 画像に `decoding="async"` を追加します:

```html
<img src="photo.webp" alt="Description" width="600" height="400" loading="lazy" decoding="async">
```

### CLS 防止
- すべての `<img>` 要素に `width` と `height` 属性を設定
- 代替として `aspect-ratio` CSS を使用
- サイズ未指定の画像を警告

```html
<!-- 良い例 - サイズ指定あり -->
<img src="photo.jpg" width="800" height="600" alt="Description">

<!-- 良い例 - CSS aspect-ratio -->
<img src="photo.jpg" style="aspect-ratio: 4/3" alt="Description">

<!-- 悪い例 - サイズ指定なし -->
<img src="photo.jpg" alt="Description">
```

### ファイル名
- 説明的にする: `blue-running-shoes.webp` であり `IMG_1234.jpg` ではない
- ハイフン区切り、小文字、特殊文字なし
- 関連キーワードを含める

### CDN の利用
- 画像が CDN から配信されているか確認（異なるドメイン、CDN ヘッダー）
- 画像が多いサイトには CDN を推奨
- エッジキャッシュヘッダーを確認

## 出力

### 画像監査サマリー

| 指標 | ステータス | 件数 |
|--------|--------|-------|
| 画像総数 | - | XX |
| alt テキスト未設定 | ❌ | XX |
| 過大サイズ（>200KB） | ⚠️ | XX |
| 不適切なフォーマット | ⚠️ | XX |
| サイズ未指定 | ⚠️ | XX |
| 遅延読み込み未設定 | ⚠️ | XX |

### 優先度順の最適化リスト

ファイルサイズの影響順にソート（削減量が大きい順）:

| 画像 | 現在のサイズ | フォーマット | 問題点 | 推定削減量 |
|-------|--------------|--------|--------|--------------|
| ... | ... | ... | ... | ... |

### 推奨事項
1. X 枚の画像を WebP フォーマットに変換（推定 XX KB 削減）
2. X 枚の画像に alt テキストを追加
3. X 枚の画像にサイズを追加
4. ファーストビュー外の X 枚の画像に遅延読み込みを有効化
5. X 枚の過大サイズ画像を圧縮
