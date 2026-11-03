---
article_id: 360018835752
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 6815692202045010ddf91b834dc7146810412886368c5f96c0d48651b7c77823
fetched_at: '2026-06-28T22:39:22.059153+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Nota fiscal não
  foi gerada na Apuração do ICMS '
type: support-article
updated_at: '2021-07-15T17:53:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018835752--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nota-fiscal-n%C3%A3o-foi-gerada-na-Apura%C3%A7%C3%A3o-do-ICMS
---

**Dúvida**Possuo uma nota fiscal que gera no Livro Fiscal (MATR930), porém não gera na Apuração do ICMS ( MATA953)

**Ambiente**

Protheus - Livros Fiscais - Todas as Versões  
  
   
**Solução**Erro acontece quando por algum motivo acontece alguma divergência na transmissão da nota fiscal e embora na Sefaz a nota fiscal esteja com Status Normal/ Transmitida corretamente grava no Campo: F3\_CODRSEF = Código de Rejeição

Para correção:

Confirmar na Sefaz se a nota fiscal foi transmitida corretamente e logo em seguida acessar Monitor para que o código seja Atualizado, atualizando o Campo: F3\_CODRSEF

Maiores informações acesse:

<http://tdn.totvs.com/pages/releaseview.action?pageId=198946617>
