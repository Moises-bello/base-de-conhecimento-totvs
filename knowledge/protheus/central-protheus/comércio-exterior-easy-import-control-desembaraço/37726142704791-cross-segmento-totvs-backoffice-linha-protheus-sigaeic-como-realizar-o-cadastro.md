---
article_id: 37726142704791
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 247fbd703206817d94ed2e8c9f09ec37d12e388fc9a0ecc91c8ddd54163cb579
fetched_at: '2026-06-28T22:39:51.162978+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro das Regras de Escrituração do IBS no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-16T19:43:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37726142704791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-das-Regras-de-Escritura%C3%A7%C3%A3o-do-IBS-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37726142688919) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro das Regras de Escrituração do IBS no Configurador de Tributos (FISA170)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.  
  
**Solução**  
A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração das  Regras de Escrituração do IBS.

**REGRAS DE ESCRITURAÇÃO**

**Acesse:** Regras de Cálculo Documento Fiscal → Regra de Escrituração

Criar uma regra para cada tributo conforme exemplo abaixo:

| **Campo (Tributo)** | **Valor (Parâmetro)** | **Incidência** | **Observação** |
| --- | --- | --- | --- |
| **IBSES** (IBS Estadual) | ESCRITURAÇÃO IBS IMPORTAÇÃO | 1 - Tributado | **ESSENCIAL** para integração |

**Seção Incidência:**

* **Incidência:** 8 - Integração **ESSENCIAL para integração**
* **Total da Nota:**Sem ação
* **Tabela CST:** Selecione o CST apropriado (consulte tabela específica para cada tributo)

| **Tributo** | **CST Sugerido** | **Tabela do CST** | **Observação** |
| --- | --- | --- | --- |
| **IBS** (Est/Mun) | A definir | *(Aguardando definição)* | Conforme operação |

|  |
| --- |
| **IMPORTANTE**  **Configuração do campo "Incidência":** A opção **8 - Integração** ainda não está completamente implementada. O sistema requer ajustes adicionais para atender às configurações de integração. Recomendamos utilizar a opção 1 = Tributado até que as melhorias sejam disponibilizadas. |

![d80c1117-f522-40a4-a861-a0ccb7f9ad5e.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37726142689559)

**Vídeos** ***How to***

|  |  |
| --- | --- |
|  |  |

**Saiba mais:**  
[Configurador de Tributos (CFGTRIB) na Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o)  
[Guia Prático - Configurador de Tributos na Importação - SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=1017443678)

Vídeos:  
[How To TRADE COMÉRCIO EXTERIOR - Suporte Técnico Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=766411901)
