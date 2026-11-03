---
article_id: 9637798214039
category: Materiais - Compras (SIGACOM)
content_hash: 5f46ca5507411b0425c23df31064fb6725e9e780eb5932bf815a839cd91cf345
fetched_at: '2026-06-28T22:41:19.992065+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Inclusão deNota Fiscal
  com o mesmo Número
type: support-article
updated_at: '2024-05-27T11:33:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9637798214039-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Inclus%C3%A3o-deNota-Fiscal-com-o-mesmo-N%C3%BAmero
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min**

**Dúvida**

É possível a Inclusão de nota fiscal no Documento de Entrada (MATA103) com mesmo número?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

Atualmente o sistema não permite que seja incluída uma mesma numeração de documento de entrada pois existe uma integridade (chave única) na tabela**SF1**(**F1\_FILIAL+F1\_DOC+F1\_SERIE+F1\_FORN+F1\_LOJA**) que não permite tal processo.

Porém, para efetuar o lançamento quando necessário, poderá incluir o documento de entrada seguindo o exemplo abaixo:

**Primeira Nota :**

|  |  |
| --- | --- |
| **Coluna** | **Lançamento** |
| Nota | Número 1 |
| Série | 1 |
| Fornecedor | F01 |
| Loja | 01 |

**Segunda nota:**

|  |  |
| --- | --- |
| **Coluna** | Lançamento |
| Nota | Número 01 (Adicionando um zero a esquerda) |
| Série | 01 (Adicionando dois zeros a esquerda) |
| Fornecedor | F01 |
| Loja | 01 |

**Saiba mais em :**

**[Documento de Entrada com o mesmo Número](https://tdn.totvs.com/pages/releaseview.action?pageId=284471056)**

**[PÁGINA CENTRALIZADORA DE COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)**
