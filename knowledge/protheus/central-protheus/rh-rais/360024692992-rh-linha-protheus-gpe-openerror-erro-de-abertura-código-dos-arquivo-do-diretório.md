---
article_id: 360024692992
category: RH - RAIS
content_hash: c81bb535e1c7b2f27bd00f400d65a1c15e3289570937f77c3306a5f33cdb7965
fetched_at: '2026-06-28T22:44:05.713180+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: 'RH - Linha Protheus - GPE - Openerror  - Erro de abertura: código DOS arquivo
  do diretório especificado'
type: support-article
updated_at: '2025-08-21T18:04:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024692992-RH-Linha-Protheus-GPE-Openerror-Erro-de-abertura-c%C3%B3digo-DOS-arquivo-do-diret%C3%B3rio-especificado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34349855475735)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Por que o erro *Openerror* - Erro de abertura: código DOS arquivo do diretório especificado é gerado na geração do arquivo magnético da RAIS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal –  A partir da Versão 12.1.27  
  
**Solução**Este problema ocorre por alguns motivos, sendo eles:

1. Ocorre quando a empresa já validou o TXT e o programa da rais esta aberto.  
A solução é fechar o validador para gerar o TXT novamente.

2. No caminho de saída não tem a extensão .TXT  
A solução informar o .TXT. Exemplo: C:\RAIS\RAIS.TXT

3. O usuário não possui acesso à pasta especificada  
A solução é alterar para um diretório em que o usuário tenha acesso para gravação

**Saiba Mais**<http://tdn.totvs.com/x/DpjHEw>
