<!-- Updated: 2026-02-07 -->
# Core Web Vitals しきい値 (2026年2月)

## 現在の指標

| 指標 | 良好 | 改善が必要 | 不良 |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤2.5s | 2.5s–4.0s | >4.0s |
| INP (Interaction to Next Paint) | ≤200ms | 200ms–500ms | >500ms |
| CLS (Cumulative Layout Shift) | ≤0.1 | 0.1–0.25 | >0.25 |

## 重要事項
- INPは**2024年3月12日**にFID (First Input Delay) を置き換えました。FIDは**2024年9月9日**にすべてのChromeツール（CrUX API、PageSpeed Insights、Lighthouse）から完全に削除されました。INPが唯一のインタラクティビティ指標です。
- 評価には実ユーザーデータ（CrUXのフィールドデータ）の**75パーセンタイル**が使用されます。
- Googleは**ページレベル**と**オリジンレベル**の両方で評価します。
- Core Web Vitalsは**タイブレーカー**のランキングシグナルです — コンテンツの品質が競合間で類似している場合に最も重要になります。
- **しきい値は当初の定義から変更されていません** — SEOブログの「しきい値が厳格化された」という主張は無視してください。
- 2025年12月のコアアップデートでは、**モバイルのCWVがより重視される**傾向が見られました。
- 2025年10月時点: デスクトップサイトの**57.1%**、モバイルサイトの**49.7%**が3つのCWVすべてに合格しています。

## LCPサブパート (2025年2月 CrUX追加)

LCPを診断用のサブパートに分解できるようになりました:

| サブパート | 測定内容 | 目標値 |
|---------|------------------|--------|
| **TTFB** | Time to First Byte（サーバー応答時間） | <800ms |
| **Resource Load Delay** | TTFBからリソースリクエスト開始までの時間 | 最小化 |
| **Resource Load Time** | LCPリソースのダウンロード時間 | サイズに依存 |
| **Element Render Delay** | リソース読み込み完了からレンダリングまでの時間 | 最小化 |

**LCP合計 = TTFB + Resource Load Delay + Resource Load Time + Element Render Delay**

この分解を使用して、どのフェーズがLCPの問題を引き起こしているかを特定してください。

## Soft Navigations API（実験的）

**Chrome 139+ Origin Trial (2025年7月)** — SPAにおけるCWV測定に向けた最初のステップ。

- SPAの測定における長年のブラインドスポットに対処
- 現在は実験段階であり、**ランキングへの影響はまだありません**
- 「ソフトナビゲーション」（完全なページ読み込みなしのURL変更）を検出
- 将来のSPA CWV測定に影響する可能性あり

**検出:** SPAフレームワーク（React、Vue、Angular、Svelte）を確認し、現在のCWV測定の制限について警告してください。

## 測定ソース

### フィールドデータ（実ユーザー）
- Chrome User Experience Report (CrUX)
- PageSpeed Insights（CrUXデータを使用）
- Search Console Core Web Vitalsレポート

### ラボデータ（シミュレーション）
- Lighthouse
- WebPageTest
- Chrome DevTools

> フィールドデータはGoogleがランキングに使用するものです。ラボデータはデバッグに役立ちます。

## よくあるボトルネック

### LCP (Largest Contentful Paint)
- 最適化されていないヒーロー画像（圧縮、WebP/AVIFの使用、preloadの追加）
- レンダリングブロッキングCSS/JS（defer、async、クリティカルCSSのインライン化）
- サーバー応答の遅延（TTFB >200ms — エッジCDN、キャッシュの使用）
- サードパーティスクリプトのブロッキング（アナリティクス、チャットウィジェットのdefer）
- Webフォントの読み込み遅延（font-display: swap + preloadの使用）

### INP (Interaction to Next Paint)
- メインスレッドでの長いJavaScriptタスク（50ms未満の小さなタスクに分割）
- 重いイベントハンドラー（debounce、requestAnimationFrameの使用）
- 過大なDOMサイズ（1,500要素を超えると要注意）
- メインスレッドを占有するサードパーティスクリプト
- 同期的なXHRまたはlocalStorage操作
- レイアウトスラッシング（複数回の強制リフロー）

### CLS (Cumulative Layout Shift)
- width/height属性のない画像/iframe
- 既存コンテンツの上に動的に挿入されるコンテンツ
- レイアウトシフトを引き起こすWebフォント（font-display: swap + preloadの使用）
- 予約スペースのない広告/埋め込み
- ページの下方にコンテンツを押し下げる遅延読み込みコンテンツ

## 最適化の優先順位

1. **LCP** — 体感パフォーマンスへの影響が最も大きい
2. **CLS** — ユーザー体験に影響する最も一般的な問題
3. **INP** — インタラクティブなアプリケーションで最も重要

## ツール

```bash
# PageSpeed Insights API
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&key=API_KEY"

# Lighthouse CLI
npx lighthouse URL --output json --output-path report.json
```

## パフォーマンスツールの更新 (2025年)

- **Lighthouse 13.0** (2025年10月): パフォーマンスカテゴリの再編成とスコアリングウェイトの更新を含む大規模な監査リストラクチャリング。Lighthouseはラボツール（シミュレーション条件）です — 実環境のパフォーマンスについては必ずCrUXフィールドデータと照合してください。
- **CrUX Vis**がCrUX Dashboardを置き換えました（2025年11月）。旧Looker Studioダッシュボードは非推奨となりました。[CrUX Vis](https://cruxvis.withgoogle.com)またはCrUX APIを直接使用してください。
- **LCPサブパート**がCrUXに追加されました（2025年2月）: Time to First Byte (TTFB)、Resource Load Delay、Resource Load Time、Element Render Delayが、CrUXデータにおけるLCPのサブコンポーネントとして利用可能になりました。
- **Google Search Console 2025年の機能** (2025年12月): 自動分析のためのAI搭載設定。ブランドクエリと非ブランドクエリのフィルター。APIで時間単位のデータが利用可能。カスタムチャートアノテーション。ソーシャルチャネルトラッキング。

> **モバイルファーストインデックス**は2024年7月5日に100%完了しました。Googleは現在、すべてのウェブサイトをモバイルGooglebotユーザーエージェントのみでクロールおよびインデックスしています。モバイル版にすべての重要なコンテンツ、構造化データ、メタタグが含まれていることを確認してください。
