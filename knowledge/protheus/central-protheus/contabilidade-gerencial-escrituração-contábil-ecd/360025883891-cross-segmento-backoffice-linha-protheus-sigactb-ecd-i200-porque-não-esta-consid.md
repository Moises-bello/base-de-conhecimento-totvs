---
article_id: 360025883891
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 6d9d544e0a7579fe1fab52d6960d6acab46235e7f55ba7c0362712af85f33cf7
fetched_at: '2026-06-28T22:40:52.737185+00:00'
product: protheus
section_id: 1500001537561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB ECD I200 PORQUE NÃO ESTA
  CONSIDERANDO O NUMERO DO LOTE
type: support-article
updated_at: '2022-04-19T14:00:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025883891-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-I200-PORQUE-N%C3%83O-ESTA-CONSIDERANDO-O-NUMERO-DO-LOTE
---

**Dúvida**Porque na composição do registro I200 o sistema não esta considerando o número do lote?  
  
**Ambiente**Protheus – Contabilidade – A partir da versão 12.1.17  
  
 **Motivo:**

No padrão o I200 é composto pelo número do lote, exemplo: lote 008850 (financeiro).

Neste lote pode ter documentos de contas a pagar e contas a receber.

Na advertência a Receita quer que separe esses fatos contábeis.

**Solução**O parâmetro **MV\_CTBSDOC= .F. (padrão)**

* Valor .F. para validar os lançamentos por Lote

 Esse parâmetro foi criado para atender a composição a advertência do "Fato Contábil"

O parâmetro define qual a "chave" que o sistema irá considerar na criação do registro o I200. (Apenas o lote ou Lote + documento)

Importante! Se o parâmetro estiver habilitado é imprescindível que os saldos por documento estejam batidos.

 |I200|**00 20180604000001001000001**|04062018|100,00|N||  
|I250|31102001||100,00|D|0120180604000001001000000001001D0110400||TESTE||  
|I250|11101002||100,00|C|01 20180604000001001000000001001C0110400||TESTE||

**MV\_CTBSDOC= .T.**

* Valor .T. para validar os lançamentos por Documento.

|I200|**01 20171231000001001**|31122017|2000,00|N|  
|I250|11101002||2000,00|D|00 20171231000001001000000001001D0110400||hISTORICO||  
|I250|24101001||2000,00|C|00 20171231000001001000000001001C0110400||hISTORICO||

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069905514/mceclip0.png)Dependendo de como estive contabilizado o lançamento o sistema irá somente minimizar as advertência. Se o lançamento contábil não estiver exatamente conforme exemplo apresentado acima, o parâmetro não terá efeito, com isso para alguns lotes a advertência continuará ser apresentada

Saiba mais:

<http://tdn.totvs.com/pages/viewpage.action?pageId=362459051>

Advertência I200 | Fato Contábil

<http://tdn.totvs.com/pages/viewpage.action?pageId=145362299>

<https://tdn.totvs.com/display/public/PROT/CTB0085_Parametro_MV_ORDLCTB>
