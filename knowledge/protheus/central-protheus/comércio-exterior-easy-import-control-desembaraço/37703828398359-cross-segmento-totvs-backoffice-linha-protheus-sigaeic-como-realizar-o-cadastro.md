---
article_id: 37703828398359
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: dfee3de19bc8b486a2c890d120b808e1b06669028a5c6a4fbf28345e4e38dfd4
fetched_at: '2026-06-28T22:39:51.219305+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro do Imposto IBS Municipal no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-15T20:18:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37703828398359-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-do-Imposto-IBS-Municipal-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37703828364951) Tempo aproximado para leitura: 00**:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro do Imposto IBS Municipal no Configurador de Tributos (FISA170)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.  
  
**Solução**

A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração do IBS Municipal

**ETAPA 1: Cadastro dos Tributos**

Acesse: Regras Fiscais → Cadastros → Tributo.

| **Campo** | **Tabela/Código** | **Esfera** | **Espécie** | **Descrição** | **ID Tributo (TOTVS)** |
| --- | --- | --- | --- | --- | --- |
| **IBS MUNICIPAL** | IBSMUN | 3 - Municipal | 1 - Imposto | IBS MUNICIPAL - IMPOSTO SOBRE BENS E SERVIÇOS MUNICIPAL | 000061 |

![149f4b78-6db3-4ec0-832e-410413273bf6.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37703842565271)

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
