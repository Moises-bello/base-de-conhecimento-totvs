---
article_id: 21079495590295
category: RH - Leitura e Apontamento
content_hash: 7a0c851097d136f2aeb8d3339f73094145cbff840c156707cf214e6324abef25
fetched_at: '2026-06-28T22:44:45.974092+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Marcações Automáticas para entrada/saída do expediente
  ficam com Motivo de Modificação de Registro diferente das marcações de intervalo
type: support-article
updated_at: '2025-10-10T13:27:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21079495590295-RH-Linha-Protheus-PON-Marca%C3%A7%C3%B5es-Autom%C3%A1ticas-para-entrada-sa%C3%ADda-do-expediente-ficam-com-Motivo-de-Modifica%C3%A7%C3%A3o-de-Registro-diferente-das-marca%C3%A7%C3%B5es-de-intervalo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21079519747223) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Por qual motivo as **Marcações Automáticas** para entrada/saída do expediente ficam como **Inclusão Manual** no campo Motivo de Modificação de Registro, e as marcações do intervalo ficam como Inclusão Automática?  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21079495570839)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O sistema dá este tratamento diferenciado entre as marcações de entrada/saída do expediente, pois apenas as **marcações de intervalos** podem ser **geradas ou pré-assinaladas**, conforme o **art. 74 §2º da CLT:**   
*Para os estabelecimentos com mais de 20 (vinte) trabalhadores será obrigatória a anotação da hora de entrada e de saída, em registro manual, mecânico ou eletrônico, conforme instruções expedidas pela Secretaria Especial de Previdência e Trabalho do Ministério da Economia, permitida a pré-assinalação do período de repouso.*  
Neste caso, o sistema atua como um facilitador para que o usuário não tenha que incluir as marcações de entrada/saída do expediente manualmente, porém, elas ficarão como **Inclusão Manual** mesmo quando geradas de forma automática através da rotina de Leitura/Apontamento.  
É possível customizar o texto utilizado na justificativa para a inclusão da marcação utilizando o [Ponto de Entrada PNMMOTMARC](https://tdn.totvs.com/pages/releaseview.action?pageId=6082557), mas apenas a justificativa será alterada e o registro continuará como uma marcação incluída.  
  
  
**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
