---
article_id: 37402760312087
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: cfc80aa07949dff7e0e079dd860e9fbebdfea446efa9b51ffec4329776394e60
fetched_at: '2026-06-28T22:39:51.225438+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro do tributo IPI no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-05T12:07:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37402760312087-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-do-tributo-IPI-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37402760287127) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro do tributo IPI no Configurador de Tributos (FISA170)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210

**Solução**  
  
A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores prontos.

Passos de Configuração do IPI

**ETAPA 1: Cadastro dos Tributos**

Acesse: Regras Fiscais → Cadastros → Tributo.

|  |  |
| --- | --- |
| **Campo** | **IPI** |
| Tributo | EICIPI |
| Esfera | 1-Federal |
| Espécie | 1-Imposto |
| Descrição | IPI IMPORTAÇÃO - SIGAEIC |
| ID Tributo (ID TOTVS) | 000022 |

![771a7280-3cad-4d04-8ea8-e9946250c958.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37402774276375)

|  |
| --- |
| **Nota - Todas as informações referentes a "CÓDIGO" apresentadas neste documento possuem caráter meramente indicativo. É responsabilidade do usuário analisar e determinar a codificação que melhor atenda às demandas de sua operação.** |

**Saiba Mais:**

[**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Configurador de Tributos (CFGTRIB) na Importação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o)

[**Guia Prático - Configurador de Tributos na Importação - SIGAEIC**](https://tdn.totvs.com/pages/releaseview.action?pageId=1017443678)
