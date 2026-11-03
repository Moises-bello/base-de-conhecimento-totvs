---
article_id: 360014064392
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: bccb6c5c7fe63d1ebf800d40d93cd5f751775f9b2ecca9c3743ed8cdc4b18e03
fetched_at: '2026-06-28T22:40:32.382638+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB/SIGAATF - Função xFilial
  para o campo X3_INIBRW
type: support-article
updated_at: '2022-07-18T18:13:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014064392-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAATF-Fun%C3%A7%C3%A3o-xFilial-para-o-campo-X3-INIBRW
---

**Ocorrência**

O sistema não preenche o ***Browse*** com os dados de **outra filia**l mesmo que o **usuário tenha acesso aos dados da mesma**.

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – 12.1.17

**Causa**

Isto ocorre devido ao fato da função **xFilial** buscar somente as filiais **posicionadas em memória no sistema**.

**Solução**

Para que o sistema carregue as informações desejadas de outras filiais no ***Browse***, no inicializador do Browse (**X3\_INIBRW**) deverá ser utilizado o **campo de filial da tabela** ao invés do **xFilial().**

**Exemplo:**Ao entrar na rotina Responsável x Bens(ATFA190) não é possível verificar a descrição dos bens contidos em outras filiais, mesmo tendo acesso a outra filial e está sendo utilizado a regra: **POSICIONE("SN1",1,XFILIAL("SN1")+SND->(ND\_CBASE+ND\_ITEM),"N1\_DESCRIC")** no campo **X3\_INIBRW**.

Para que os dados sejam apresentados deverá por exemplo utilizar a seguinte regra: **POSICIONE("SN1",1,SND->(ND\_FILIAL+ND\_CBASE+ND\_ITEM),"N1\_DESCRIC")**

Verifique que não está sendo utilizado o xFilial e sim o campo filial da própria tabela.
