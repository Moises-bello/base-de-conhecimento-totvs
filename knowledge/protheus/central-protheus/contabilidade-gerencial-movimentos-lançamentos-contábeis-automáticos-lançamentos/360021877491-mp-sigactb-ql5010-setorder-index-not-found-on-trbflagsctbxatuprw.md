---
article_id: 360021877491
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 6bb0ba415c3ea18a261ee42616c537eb3bed9ddc455ab4f74110aa83bfb679a1
fetched_at: '2026-06-28T22:40:32.627568+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'MP - SIGACTB : QL5010: SetOrder - Index not found. on TRBFLAGS(CTBXATU.PRW)'
type: support-article
updated_at: '2021-04-28T22:11:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021877491-MP-SIGACTB-QL5010-SetOrder-Index-not-found-on-TRBFLAGS-CTBXATU-PRW
---

**Dúvida**THREAD ERROR ([0000], adm, xxxxxx) 10/01/2018 09:34:  
QL5010: SetOrder - Index not found. on TRBFLAGS(CTBXATU.PRW) 13/12/2018 17:55:00 line : 4745  
  
 **Ambiente**  
Protheus  – contabilidade – A partir da versão P12  
  
   
**Solução**

Para que o erro não seja apresentado se faz necessário criação índice 03 na tabela QL5 com a chave QL5\_FILIAL+QL5\_RCNCT2.

Ajuste na verificação do registro de log , que agora é validado pelo Recno da CT2.

*Criação ou Alteração* de **Índices** no arquivo **SIX – Índices**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018559631/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018559651/mceclip0.png)

Veja mais :

[MPRIMESP-17526](http://tdn.totvs.com/pages/viewpage.action?pageId=445648511)foi liberado o fonte CTBXATU.PRW  13/12/2018  17:55:01

[DSERCTR1-15910](http://tdn.totvs.com/display/public/PROT/4210410+DSERCTR1-15910+Chave+duplicada+na+tabela+QL5) foi liberada a documentação : [Clique aqui](https://tdn.totvs.com/display/public/PROT/4210410+DSERCTR1-15910+Chave+duplicada+na+tabela+QL5)

[DSERCTR1-6297](http://tdn.totvs.com/pages/releaseview.action?pageId=372556085) foi liberado os fontes :

CTBXATU.PRW  27/06/2018 17:48:13 17

CTBXLOG.PRW  27/06/2018 17:48:13 17
