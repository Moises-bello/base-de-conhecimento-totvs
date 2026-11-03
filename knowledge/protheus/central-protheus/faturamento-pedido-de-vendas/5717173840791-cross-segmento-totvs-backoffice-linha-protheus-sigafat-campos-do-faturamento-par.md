---
article_id: 5717173840791
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a0aff1135d5d109e66ac61d3ca4bd04530df9374cd36713fda54f448938d1710
fetched_at: '2026-06-28T22:38:38.474848+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Campos do Faturamento
  para uso da NT 2021.004
type: support-article
updated_at: '2022-09-05T20:51:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5717173840791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Campos-do-Faturamento-para-uso-da-NT-2021-004
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Criação de campos do Faturamento para uso da NT 2021.004.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da 12.1.27.  
  
**Solução**Para preenchimento do grupo obsItem, será necessário a atualização do dicionário de dados com 08 novos campos, sendo 04 para o módulo de compras e 04 para o módulo de faturamento.

**Os campos do Faturamento serão:** **C6\_OBSCONT, C6\_OBSCCMP, C6\_OBSFISC, C6\_OBSFCMP**

Todavia, a expedição contínua atual de faturamento datada de 15.04.2022 ainda não contempla a alteração do dicionário de dados com estes campos, pois a melhoria expedida pelo TSS saiu posterior a esta data.

O pacote de expedição contínua de faturamento que já contempla o dicionário diferencial com os campos em questão: **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)**

A legislação para a **NT2021.004** entraria em **vigor a partir de 16.05.22,** mas **foi** **prorrogada** **para entrar em vigor a partir de 08.08.22**.

Caso não queira implementar o uso do dicionário diferencial, também é possível a inclusão dos campos  **manualmente** via configurador, base de dados, editando a tabela **SC6**, segue a configuração do campos:

|  |  |
| --- | --- |
| **Campo** | **C6\_OBSCONT** |
| **Tipo** | Caractere |
| **Tamanho** | 60 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | C6\_OBSCONT |
| **Descrição** | Observação do **contribuinte**. |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Campo de uso livre para informações do contribuinte. |

|  |  |
| --- | --- |
| **Campo** | **C6\_OBSCCMP** |
| **Tipo** | Caractere |
| **Tamanho** | 20 |
| **Decimal** | 0 |
| **Formato** |  |
| **Título** | C6\_OBSCCMP |
| **Descrição** | Título da observação do **contribuinte** |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Informar o título da observação do contribuinte informada. |

|  |  |
| --- | --- |
| **Campo** | **C6\_OBSFISC** |
| **Tipo** | Caractere |
| **Tamanho** | 60 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | C6\_OBSCONT |
| **Descrição** | Observação do **fisco**. |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Campo de uso livre para informações do **fisco**. |

|  |  |
| --- | --- |
| **Campo** | **C6\_OBSFCMP** |
| **Tipo** | Caractere |
| **Tamanho** | 20 |
| **Decimal** | 0 |
| **Formato** |  |
| **Título** | C6\_OBSFCMP |
| **Descrição** | Título da observação do **fisco**. |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Informar o título da observação do **fisco**informada. |

Os campos são para observações do item e não são obrigatórios o preenchimento deles.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5826328080279/mceclip0.png)

**Obs. Os campos relacionados ao módulos de Compras (D1\_OBSCONT, D1\_OBSCTIT, D1\_OBSFISC, D1\_OBSFTIT), estão documentados  em:****[13053128 DSERTSS1-18512 DT Protheus NF-e Implementação NT 2021.004](https://tdn.totvs.com/x/6oubK)**

**Qualquer dúvida sobre eles, contato a equipe de Suporte de Compras/GCT/GCP.**
