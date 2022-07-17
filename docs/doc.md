---
title: 資料作成方法
---

# 概要
MarkdownでWEBサイトを作成し, HTMLへ変換および公開するために*Github Pages*を使用しました.
環境構築の備忘録です.

## Github Pages
以下を参考にしました.
* [GitHubを使ってMarkdown文書を５ステップでホームページとして公開する方法](https://qiita.com/MahoTakara/items/3800e9dc83b530d0a050)
* [Markdownで書かれたページをGitHub Pagesで公開する](http://yoshikyoto.github.io/text/git/gh_pages_md.html)

## Github Pagesをローカルでテストする
以下Windows環境を想定しています.
* [jekyll](https://jekyllrb.com/docs/installation/)のインストール
  * [ruby](https://rubyinstaller.org/)のインストール
  * [gcc](https://ja.osdn.net/projects/mingw/)(MinGW)のインストール
  * [make](https://sourceforge.net/projects/gnuwin32/files/make/3.81/make-3.81.exe/download?use_mirror=jaist&download=)のインストール
  * [jekyll](https://jekyllrb.com/docs/installation/windows/)のインストール
* [Bundler](https://bundler.io/)のインストール
  * Gemfileの作成と編集