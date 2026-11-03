---
article_id: 37703365011351
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 8afbafa7ab8685b48008077ae3df61f10d1d033550f638357caf252bfaa9b2e0
fetched_at: '2026-06-28T22:39:51.212207+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro do Imposto IBS Estadual no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-15T20:13:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37703365011351-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-do-Imposto-IBS-Estadual-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37703334245271) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
 Como realizar o cadastro do Imposto IBS Estadual no Configurador de Tributos (FISA170)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.  
  
**Solução**

A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração do IBS Estadual

**ETAPA 1: Cadastro dos Tributos**

Acesse: Regras Fiscais → Cadastros → Tributo.

| **Campo** | **Tabela/Código** | **Esfera** | **Espécie** | **Descrição** | **ID Tributo (TOTVS)** |
| --- | --- | --- | --- | --- | --- |
| **IBS ESTADUAL** | IBSEST | 2 - Estadual | 1 - Imposto | IBS ESTADUAL - IMPOSTO SOBRE BENS E SERVIÇOS ESTADUAL | 000060 |

![149f4b78-6db3-4ec0-832e-410413273bf6.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37703334247831)

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
