---
article_id: 37724581857687
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: b7490ecfc0666f2487e31a0e3a2ca2fd5d7ebb36abddaa743aaad5b24496cd80
fetched_at: '2026-06-28T22:39:51.171580+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro das Regras de Escrituração do ICMS no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-16T19:34:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37724581857687-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-das-Regras-de-Escritura%C3%A7%C3%A3o-do-ICMS-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37724567141143) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro das Regras de Escrituração do ICMS no Configurador de Tributos (FISA170)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.  
  
**Solução**  
A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração das  Regras de Escrituração do ICMS.

**REGRAS DE ESCRITURAÇÃO**

**Acesse:** Regras de Cálculo Documento Fiscal → Regra de Escrituração

Criar uma regra para cada tributo conforme exemplo abaixo:

| **Campo (Tributo)** | **Valor (Parâmetro)** | **Incidência** | **Observação** |
| --- | --- | --- | --- |
| **ICMS** | Escrituração ICMS Importação | 8 - Integração | **ESSENCIAL** para integração |

**Seção Incidência:**

* **Incidência:** 8 - Integração **ESSENCIAL para integração**
* **Total da Nota:**Sem ação
* **Tabela CST:** Selecione o CST apropriado (consulte tabela específica para cada tributo)

| **Tributo** | **CST Sugerido** | **Tabela do CST** | **Observação** |
| --- | --- | --- | --- |
| **EICICM** | 00, 10, 20 | 000001 - CST DO ICMS | Conforme operação |

![667e8721-1a9d-4f1c-a29f-8220d5f96eae.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37724567142039)

**Vídeos** ***How to***

|  |  |
| --- | --- |
|  |  |

**Saiba mais:**  
[Configurador de Tributos (CFGTRIB) na Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o)  
[Guia Prático - Configurador de Tributos na Importação - SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=1017443678)

Vídeos:  
[How To TRADE COMÉRCIO EXTERIOR - Suporte Técnico Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=766411901)
