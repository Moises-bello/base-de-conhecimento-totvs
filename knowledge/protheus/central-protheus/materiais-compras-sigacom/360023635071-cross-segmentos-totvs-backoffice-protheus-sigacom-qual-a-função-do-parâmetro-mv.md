---
article_id: 360023635071
category: Materiais - Compras (SIGACOM)
content_hash: 2aa4dcf28c9e01658850bdae0b98136c842b987852d2e3ce37fc62e783fe87f4
fetched_at: '2026-06-28T22:41:10.476050+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM – Qual a função do parâmetro
  MV_LIBESB6 no Retorno do Poder de Terceiros ?
type: support-article
updated_at: '2022-05-16T21:00:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023635071-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-fun%C3%A7%C3%A3o-do-par%C3%A2metro-MV-LIBESB6-no-Retorno-do-Poder-de-Terceiros
---

**Dúvida**Qual a função do parâmetro **MV\_LIBESB6** no Retorno do Poder de Terceiros ?

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**Disponibilizado parâmetro MV\_LIBESB6 na rotina Documento de Entrada (MATA103) que permite incluir uma nota de beneficiamento com as seguintes características:

* Tipo da Nota com conteúdo igual a ‘B’ –Beneficiamento;
* TES configurado com os campos abaixo:

\*Campo:Atu. Estoque (F4\_ESTOQUE) com conteúdo igual a ‘S’;  
\*Campo: Poder Terc. (F4\_PODER3)com conteúdo igual a ‘D’;

O valor informado no campo Quantidade (D1\_QUANT) zera o saldo total em quantidade do controle de poder de terceiros, ou seja, a inclusão desse item encerra o controle de poder de terceiros;

* O valor informado no campo Vlr.Total (D1\_TOTAL)não zera o saldo total em valor do controle de poder de terceiros;

***Saiba Mais:***

<http://tdn.totvs.com/display/public/PROT/Retorno+Poder+de+Terceiros+MV_LIBESB6_TGZRYX>
