---
article_id: 24035266833815
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 0f4642ec744e4572c66601855056a89cd6bc72823a282ee293a97da709322b5c
fetched_at: '2026-06-28T22:37:21.483143+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como devo cadastrar
  o Histórico de Índices?
type: support-article
updated_at: '2024-06-07T19:17:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24035266833815-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-devo-cadastrar-o-Hist%C3%B3rico-de-%C3%8Dndices
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24035266790295) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como devo cadastrar o Histórico de Índices(CNTA080) ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Gestão de Contratos - Todas as versões  
  
**Solução**

O cadastro do histórico de índice deve ser feito conforme a periodicidade de execução dos reajustes, considerando o percentual acumulado entre os períodos.

Exemplo:

*O índice IPCA é calculado mensalmente, porém o contrato é reajustado anualmente, nesse caso ao cadastrar o histórico do índice, é necessário cadastrá-lo conforme o acumulado entre o último reajuste e o dia da execução da revisão atual.*

*Supondo que o contrato tenha sido revisado em 01/06/2023 e vá sofrer reajuste no dia 01/06/2024, deve-se cadastrar o histórico com o percentual acumulado nesse intervalo de tempo.*

*Caso deseje que o sistema calcule mensalmente, seria necessário cadastrar o histórico mensalmente e realizar uma revisão ao mês.*

O sistema sempre buscará o histórico de índice cadastrado com base na data informada no campo **Referência Reajuste - CN9\_DREFRJ** da aba Parâmetros da Revisão.

***Saiba Mais:***

* [GCT0159\_Como devo cadastrar o histórico de índices ?](https://tdn.totvs.com/pages/releaseview.action?pageId=848365177)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a Configuração e Revisão de Reajuste em Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059174393-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-Configura%C3%A7%C3%A3o-e-Revis%C3%A3o-de-Reajuste-em-Contratos?source=search)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
