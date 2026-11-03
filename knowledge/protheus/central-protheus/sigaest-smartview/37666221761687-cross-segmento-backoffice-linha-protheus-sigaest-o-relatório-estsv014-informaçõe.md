---
article_id: 37666221761687
category: SIGAEST - SMARTVIEW
content_hash: 54d3ce4301ba744205d0689db6109c009ff82929a9ec45b28d813640270a195f
fetched_at: '2026-06-28T22:38:47.139110+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O relatório ESTSV014
  informações em branco.
type: support-article
updated_at: '2026-01-14T13:30:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37666221761687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-O-relat%C3%B3rio-ESTSV014-informa%C3%A7%C3%B5es-em-branco
---

O relatório Listagem para Inventário (ESTSV014) pode não apresentar informações se o campo B2\_DTINV estiver preenchido, indicando bloqueio do inventário.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37666221755031) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
O relatório Listagem para Inventário(ESTSV014) ao imprimir não apresenta informações, como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Verificar os seguintes tópicos para apresentar informações no relatório ESTSV014.

1. Analisar se o campo B2\_DTINV  se encontra em branco no seu ambiente.
2. Caso o campo B2\_DTINV  esteja com preenchimento, o relatório ira apresentar em branco as informações, pois o campo mencionado, indica se o inventário gerado se encontra bloqueado.
3. Se o campo B2\_DTINV  estiver preenchido é necessário realizar o desbloqueio na rotina MATA271.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - - MATA271 - Bloqueio de produtos para inventário por data informada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021554891-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-informada)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA271 - Bloqueio de produtos para inventário por data calculada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021321072-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-calculada)

  4. E verifica se o parâmetro [MV\_CONTINV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061630273-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-MV-CONTINV-m%C3%BAltiplas-contagens-de-invent%C3%A1rio-por-sele%C3%A7%C3%A3o-de-contagem) está com preenchimento, caso tiver preenchido você usa o inventário por Múltiplas Contagens, por esse motivo também o relatório ESTSV014 apresenta em branco, então deixar o parâmetro sem preenchimento, para aparecer informações no relatório Listagem por Inventário.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Relatórios SmartView do Estoque Custos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/16108365627287-SIGAEST-SMARTVIEW)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SmartView ESTSV014 - Listagem dos Itens Inventariados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25611943160983-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SmartView-ESTSV014-Listagem-dos-Itens-Inventariados)

[Como configurar o SmartView](https://tdn.totvs.com/pages/releaseview.action?pageId=834823409)
