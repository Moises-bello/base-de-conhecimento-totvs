---
article_id: 6502168930327
category: Materiais - Compras (SIGACOM)
content_hash: 9ed2c2cb4f2f1545d0fac1168d51d5f756ab4ae0c1b3d56431265cf000a7825e
fetched_at: '2026-06-28T22:41:14.340889+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Campos Compras para
  uso da NT 2021.004
type: support-article
updated_at: '2022-06-02T19:06:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6502168930327-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Campos-Compras-para-uso-da-NT-2021-004
---

**Dúvida**Criação de campos do Compras para uso da NT 2021.004.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - a partir da 12.1.27.  
  
**Solução**Para preenchimento do grupo obs. Item, será necessário a atualização do dicionário de dados com 08 novos campos, sendo 04 para o módulo de compras e 04 para o módulo de faturamento. 

**Os campos do Compras serão: D1\_OBSCONT, D1\_OBSCCMP, D1\_OBSFISC, D1\_OBSFCMP**

Todavia, a última expedição contínua do Compras disponível no portal já contempla a alteração do dicionário de dados com estes campos, sendo necessário sua aplicação e atualização com UPDDISTR.

Para aplicação clique aqui:  **[SIGACOM](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)**

A legislação para a **NT2021.004** entraria em **vigor a partir de 16.05.22,** mas **foi** **prorrogada** **para entrar em vigor a partir de 08.08.22**.

Também é possível a inclusão dos campos  **manualmente** via configurador, base de dados, editando a tabela **SD1**, segue a configuração do campos:

|  |  |
| --- | --- |
| **Campo** | **D1\_OBSCONT** |
| **Tipo** | Memo |
| **Tamanho** | 60 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | D1\_OBSCONT |
| **Descrição** | Observação do **contribuinte**. |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Campo de uso livre para informações do contribuinte. |

|  |  |
| --- | --- |
| **Campo** | **D1\_OBSCTIT** |
| **Tipo** | Caractere |
| **Tamanho** | 20 |
| **Decimal** | 0 |
| **Formato** |  |
| **Título** | D1\_OBSCTIT |
| **Descrição** | Título da observação do **contribuinte** |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Informar o título da observação do contribuinte informada. |

|  |  |
| --- | --- |
| **Campo** | **D1\_OBSFISC** |
| **Tipo** | Memo |
| **Tamanho** | 60 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | D1\_OBSCONT |
| **Descrição** | Observação do **fisco**. |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Campo de uso livre para informações do **fisco**. |

|  |  |
| --- | --- |
| **Campo** | **D1\_OBSFTIT** |
| **Tipo** | Caractere |
| **Tamanho** | 20 |
| **Decimal** | 0 |
| **Formato** |  |
| **Título** | D1\_OBSFTIT |
| **Descrição** | Título da observação do **fisco**. |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Informar o título da observação do **fisco**informada. |

Os campos são para observações do item e não são obrigatórios o preenchimento deles.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5826328080279/mceclip0.png)

**Saiba mais: [13053128 DSERTSS1-18512 DT Protheus NF-e Implementação NT 2021.004](https://tdn.totvs.com/x/6oubK)**

**OBS:**

Na documentação da Issue do link acima, é mencionada a criação dos campos D1\_OBSCONT e D1\_OBSFISC como Tipo "Caractere", porém o correto é serem criados como Memo como ocorre ao aplicar da atualização.

Dessa forma, já está aberta Issue para correção apenas da documentação mencionada acima, com informação da criação do campos com Tipo "Memo". ISSUE de Correção da Documentação: DMANMAT02-38202

***Saiba Mais:***

* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Campos do Faturamento para uso da NT 2021.004](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5717173840791)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACO](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
