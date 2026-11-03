---
article_id: 37702926351895
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: f9b20f6b0c9b51e933e3371117109fcfda960b73d8b5ffa5636ebcad108ba425
fetched_at: '2026-06-28T22:39:48.783795+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro da Contribuição CBS no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-16T19:05:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37702926351895-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-da-Contribui%C3%A7%C3%A3o-CBS-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37702926329623) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro da Contribuição CBS no Configurador de Tributos (FISA170)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.

**Solução**   
A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração do CBS

**Cadastro dos Tributos**

Acesse: Regras Fiscais → Cadastros → Tributo.

| **Campo** | **Tabela/Código** | **Esfera** | **Espécie** | **Descrição** | **ID Tributo (TOTVS)** |
| --- | --- | --- | --- | --- | --- |
| **CBS** | CBSFED | 1 - Federal | 2 - Contribuição | CBS FEDERAL - CONTRIBUIÇÃO SOBRE BENS E SERVIÇOS FEDERAL | 000062 |

![1d5fd624-be41-4e41-ae35-db58bfe545fe.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37702926330519)

|  |
| --- |
| **Nota - Todas as informações referentes a "CÓDIGO" apresentadas neste documento possuem caráter meramente indicativo. É responsabilidade do usuário analisar e determinar a codificação que melhor atenda às demandas de sua operação.**  **Importante - Este cadastro já vem por padrão na rotina, caso não tenha inclua conforme orientações.** |

**Vídeo** ***How to***

|  |
| --- |
|  |

**Saiba Mais:**  
[Configurador de Tributos (CFGTRIB) na Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o)  
[Guia Prático - Configurador de Tributos na Importação - SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=1017443678)

**Vídeos**  
[How To TRADE COMÉRCIO EXTERIOR - Suporte Técnico Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=766411901)
