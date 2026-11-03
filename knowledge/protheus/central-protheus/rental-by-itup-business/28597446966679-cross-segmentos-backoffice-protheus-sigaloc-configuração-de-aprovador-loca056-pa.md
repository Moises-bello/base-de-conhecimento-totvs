---
article_id: 28597446966679
category: Rental by ItUp Business
content_hash: e884c726da248019f5fadd022cfc6e5804be145c8bc845757917ec468c83fa14
fetched_at: '2026-06-28T22:36:20.597147+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Configuração de Aprovador
  (LOCA056) para Aprovações de Projetos
type: support-article
updated_at: '2026-04-09T12:50:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28597446966679-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Configura%C3%A7%C3%A3o-de-Aprovador-LOCA056-para-Aprova%C3%A7%C3%B5es-de-Projetos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28597469339031) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como efetuar a configuração de Aprovador (LOCA056) para Aprovações de Projetos  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Solução**  
A rotina de aprovação de projetos (LOCA057) é utilizado para determinar se uma proposta de locação incluso no sistema será liberado ou não para geração de contrato, através de um fluxo de aprovação com controle de alçada. A regra desse fluxo é determinada de acordo com as configurações, sendo eles três tipos: Desconto, Margem e ambos.

Exemplo de regra de aprovação tipo desconto:

|  |  |  |
| --- | --- | --- |
| **Desconto do aprovador** | **Desconto na proposta** | **Resultado** |
| **10%** | **5%** | **Aceita Aprovação ou reprovação** |
| **10%** | **10%** | **Aceita Aprovação ou reprovação** |
| **20%** | **25%** | **Enviado para próximo nível** |

Exemplo de regra de aprovação tipo margem:

|  |  |  |
| --- | --- | --- |
| **Margem do aprovador** | **Margem na proposta** | **Resultado** |
| **90%** | **95%** | **Aceita Aprovação ou reprovação** |
| **90%** | **90%** | **Aceita Aprovação ou reprovação** |
| **85%** | **80%** | **Enviado para próximo nível** |

Obs. O cadastro de aprovador (LOCA056) pode ser replicado a mesma configuração para vários usuários a ser utilizado ao mesmo tempo.

Saiba Mais: [*Aprovação de projetos*](https://tdn.totvs.com/pages/releaseview.action?pageId=606426368)
