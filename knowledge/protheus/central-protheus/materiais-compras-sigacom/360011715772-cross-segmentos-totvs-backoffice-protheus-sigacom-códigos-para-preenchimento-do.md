---
article_id: 360011715772
category: Materiais - Compras (SIGACOM)
content_hash: 960462764d10ae97a50f9dbb0f29127a0173ff0210aaad5cb1025b140bd4122b
fetched_at: '2026-06-28T22:41:07.519137+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Códigos para preenchimento
  do campo CKO_FLAG
type: support-article
updated_at: '2024-06-13T10:49:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011715772-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-C%C3%B3digos-para-preenchimento-do-campo-CKO-FLAG
---

**Dúvida**

Quais são os códigos de preenchimento do campo CKO\_FLAG

**Ambiente**

Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

Quando o XML não é importado e apresenta um código de erro, de inconsistência é apresentado o código de erro correspondente na tabela CKOCOL, conforme descrito abaixo:

* **CKO\_FLAG = 0** - Não processado
* **CKO\_FLAG = 1** - Processado com sucesso
* **CKO\_FLAG = 2** - Processado com erro
* **CKO\_FLAG = 3** - Erros específicos: {"COM005", "COM006", "COM019"}
* **CKO\_FLAG = 4** - Nota Fiscal "Deletada" (Excluída)

|  |  |
| --- | --- |
| **COM005** | ID de NF-e já registrado na NF do fornecedor. |
| **COM006** | ID de NF-e já registrado na NF do Cliente. |
| **COM019** | ID de CT-e já registrado na NF. |

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O que fazer quando o conteúdo do campo CKO\_FLAG está = "2"?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20062935263383-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-fazer-quando-o-conte%C3%BAdo-do-campo-CKO-FLAG-est%C3%A1-2-?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML?source=search)

[TC06 - Erros (Códigos)](https://tdn.totvs.com/pages/viewpage.action?pageId=271663193)

[TOTVS Colaboração - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=271661626)

[Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=485858148)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
