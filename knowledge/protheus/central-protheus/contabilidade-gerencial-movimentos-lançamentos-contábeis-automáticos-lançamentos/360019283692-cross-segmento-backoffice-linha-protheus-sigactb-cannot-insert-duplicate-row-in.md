---
article_id: 360019283692
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: fe504e8e0f1295899b9c874b34b3e903c6e9faedb8ed318ae7ec49695c1d6b90
fetched_at: '2026-06-28T22:40:32.371464+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- Cannot insert duplicate
  row in object "dbo.QL5"
type: support-article
updated_at: '2023-04-12T13:27:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019283692-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Cannot-insert-duplicate-row-in-object-dbo-QL5
---

**Ocorrência**Ao **excluir** um Lançamento Contábil vindo de **integração pela rotina CTBA102** é gerado o seguinte **error.log** de **chave duplicada na tabela QL5**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015261831/mceclip0.png)

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12.1.17

**Causa**Quando se efetua uma nova exclusão de um lançamento de integração que fora excluído anteriormente e contabilizado novamente, a rotina está apresentando mensagem de **errorlog.**A mensagem diz respeito a chave duplicada na tabela **Log de Exclusão de Flag da LC**(**QL5)**

**Solução**Para solucionar essa questão deve-se **ajustar** o campo de **filial do lançamento** na tabela **QL5(QL5\_FLCT2)** conforme o tamanho do campo filial em sua **CT2(CT2\_FILIAL)**, verifique a seguinte documentação técnica criada sobre o caso:

<http://tdn.totvs.com/display/public/PROT/4210410+DSERCTR1-15910+Chave+duplicada+na+tabela+QL5>

Veja Mais :  
[MP - SIGACTB : QL5010: SetOrder - Index not found. on TRBFLAGS(CTBXATU.PRW)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021877491-MP-SIGACTB-QL5010-SetOrder-Index-not-found-on-TRBFLAGS-CTBXATU-PRW-?source=search)
