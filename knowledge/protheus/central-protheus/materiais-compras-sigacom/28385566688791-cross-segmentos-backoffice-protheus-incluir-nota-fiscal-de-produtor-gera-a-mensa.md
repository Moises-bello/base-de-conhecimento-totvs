---
article_id: 28385566688791
category: Materiais - Compras (SIGACOM)
content_hash: c880cf58b37bf1a0821fc5ceee7423b46e5165307ad0b1850ecdc0d2413c88cd
fetched_at: '2026-06-28T22:41:11.856255+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Incluir Nota Fiscal de Produtor  Gera
  a mensagem - A Nota original não foi Transmitida ao SEFAZ
type: support-article
updated_at: '2024-12-09T18:14:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28385566688791-Cross-Segmentos-Backoffice-Protheus-Incluir-Nota-Fiscal-de-Produtor-Gera-a-mensagem-A-Nota-original-n%C3%A3o-foi-Transmitida-ao-SEFAZ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28385566669335) Tempo aproximado para leitura: **00:02:SS min** **Dúvida**

Ao incluir nota fiscal de Produtor Rural gera a mensagem : A Nota Original não foi Transmitida ao SEFAZ

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28385547746583)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Versão 12

**Solução**

Para que o fornecedor seja indentificado como produtor rural, e não apresentar a mensagem, efetue os procedimentos :

1. O campo A2\_INDRUR (Ind.Prod.Rur) localizado no cadastro de fornecedor  deve estar preeenchido com **1=Seg.Espec.Geral PF, 2=Seg.Espec.Ent.PAA PF,  ou 3=Ent.PAA PJ.**  

2. Habilitar o parâmetro **MV\_VTRASEF**. Descrição do parâmetro : Valida se a nota original foi transmitida à SEFAZ antes de efetuar a devolução. S=Valida; N=Nao  

![produtor-rural-devol_1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28385566672151)

***Saiba Mais :***

[Documento de Entrada - Contranota de Produtor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28383730460951/live_preview/01JENW2V7P9ZP1HGPQ822GPCJW)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
