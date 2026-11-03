---
article_id: 37725817919255
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: c69067f2a20e9d2bdf3cec7f165d5da83b70110e45196b37cd38e88a432e2e56
fetched_at: '2026-06-28T22:39:51.146790+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Como realizar
  o cadastro das Regras de Escrituração do CBS no Configurador de Tributos (FISA170)?
type: support-article
updated_at: '2026-01-16T19:41:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37725817919255-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-das-Regras-de-Escritura%C3%A7%C3%A3o-do-CBS-no-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37725817896983)  Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro das Regras de Escrituração do CBS no Configurador de Tributos (FISA170)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - a partir da versão 12.1.2210.  
  
**Solução**  
A configuração do Configurador de Tributos para importação tem como objetivo **receber** os valores de impostos já calculados pelo SIGAEIC. O sistema **não** deve recalcular os tributos, mas sim utilizar os **Operandos de Integração** para capturar os valores pronto.

Passos de Configuração das  Regras de Escrituração do CBS.

**REGRAS DE ESCRITURAÇÃO**

**Acesse:** Regras de Cálculo Documento Fiscal → Regra de Escrituração

Criar uma regra para cada tributo conforme exemplo abaixo:

| **Campo (Tributo)** | **Valor (Parâmetro)** | **Incidência** | **Observação** |
| --- | --- | --- | --- |
| **CBSFED** | ESCRITURCAO CBS IMPORTACAO | 1 - Tributado | **ESSENCIAL** para integração |

**Seção Incidência:**

* **Incidência:** 8 - Integração **ESSENCIAL para integração**
* **Total da Nota:**Sem ação
* **Tabela CST:** Selecione o CST apropriado (consulte tabela específica para cada tributo)

| **Tributo** | **CST Sugerido** | **Tabela do CST** | **Observação** |
| --- | --- | --- | --- |
| **CBS** | A definir | *(Aguardando definição)* | Conforme operação |

![22375f28-591b-41d4-a929-e09a9615f936.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37725817897367)

|  |
| --- |
| **IMPORTANTE**  **Configuração do campo "Incidência":** A opção **8 - Integração** ainda não está completamente implementada. O sistema requer ajustes adicionais para atender às configurações de integração. Recomendamos utilizar a opção 1 = Tributado até que as melhorias sejam disponibilizadas. |

**Vídeos** ***How to***

|  |  |
| --- | --- |
|  |  |

**Saiba mais:**  
[Configurador de Tributos (CFGTRIB) na Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644911173911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configurador-de-Tributos-CFGTRIB-na-Importa%C3%A7%C3%A3o)  
[Guia Prático - Configurador de Tributos na Importação - SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=1017443678)

**Vídeos:**  
[How To TRADE COMÉRCIO EXTERIOR - Suporte Técnico Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=766411901)
