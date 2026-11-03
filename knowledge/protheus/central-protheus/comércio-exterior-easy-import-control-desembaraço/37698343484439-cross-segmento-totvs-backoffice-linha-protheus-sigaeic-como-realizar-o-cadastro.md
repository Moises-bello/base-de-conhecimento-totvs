---
article_id: 37698343484439
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: d8dd5ccc3a9f0cfd367d4f654b8ce344db7b86c70101ae68e6a09ca83c84503f
fetched_at: '2026-06-28T22:39:51.043991+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro da Contribuição COFINS no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-16T19:00:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37698343484439-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-da-Contribui%C3%A7%C3%A3o-COFINS-no-Configurador-de-Tributos-FISA170
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37698343461527) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro da Contribuição COFINS no Configurador de Tributos (FISA170)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.  
  
**Solução**  
A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração do COFINS

**Cadastro dos Tributos**

Acesse: Regras Fiscais → Cadastros → Tributo.

| **Campo** | **Tabela/Código** | **Esfera** | **Espécie** | **Descrição** | **ID Tributo (TOTVS)** |
| --- | --- | --- | --- | --- | --- |
| **COFINS** | EICCOF | 1 - Federal | 2 - Contribuição | COFINS IMPORTAÇÃO - SIGAEIC | 000015 |

![90a6b3e8-3194-473d-9fd7-a79a7da34010.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37698357436439)

|  |
| --- |
| **Nota - Todas as informações referentes a "CÓDIGO" apresentadas neste documento possuem caráter meramente indicativo. É responsabilidade do usuário analisar e determinar a codificação que melhor atenda às demandas de sua operação.** |

**Vídeo** ***How to***

|  |
| --- |
|  |

**Saiba Mais:**  
[Configurador de Tributos (CFGTRIB) na Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o)  
[Guia Prático - Configurador de Tributos na Importação - SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=1017443678)  
  
Vídeos  
[How To TRADE COMÉRCIO EXTERIOR - Suporte Técnico Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=766411901)
