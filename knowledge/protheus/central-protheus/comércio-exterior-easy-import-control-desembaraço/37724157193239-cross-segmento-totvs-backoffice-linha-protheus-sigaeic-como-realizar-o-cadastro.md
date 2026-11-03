---
article_id: 37724157193239
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 6e3cdd575670a3a00ed4fc14d2a1c89a58bcbf8b4a7b9caeb59d12f36f1a012e
fetched_at: '2026-06-28T22:39:51.179093+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro das Regras de Escrituração do IPI no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-16T19:31:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37724157193239-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-das-Regras-de-Escritura%C3%A7%C3%A3o-do-IPI-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37724157178135) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro das Regras de Escrituração do IPI no Configurador de Tributos (FISA170)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.

**Solução**   
A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração das  Regras de Escrituração do IPI.

**REGRAS DE ESCRITURAÇÃO**

**Acesse:** Regras de Cálculo Documento Fiscal → Regra de Escrituração

Criar uma regra para cada tributo conforme exemplo abaixo:

| **Campo (Tributo)** | **Valor (Parâmetro)** | **Incidência** | **Observação** |
| --- | --- | --- | --- |
| **EICIPI** | Escrituração IPI Importação | 8 - Integração | **ESSENCIAL** para integração |

**Seção Incidência:**

* **Incidência:** 8 - Integração  **ESSENCIAL para integração**
* **Total da Nota:**Sem ação
* **Tabela CST:** Selecione o CST apropriado (consulte tabela específica para cada tributo)

| **Tributo** | **CST Sugerido** | **Tabela do CST** | **Observação** |
| --- | --- | --- | --- |
| **EICIPI** | 00, 49, 50 | 000003 - CST DO IPI | Conforme operação |

![d7767ee3-54f3-4010-abe6-db43d8a942c2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37724157179927)

**Vídeos** ***How to***

|  |  |
| --- | --- |
|  |  |

**Saiba mais:**  
[Configurador de Tributos (CFGTRIB) na Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o)  
[Guia Prático - Configurador de Tributos na Importação - SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=1017443678)

Vídeos:  
[How To TRADE COMÉRCIO EXTERIOR - Suporte Técnico Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=766411901)
