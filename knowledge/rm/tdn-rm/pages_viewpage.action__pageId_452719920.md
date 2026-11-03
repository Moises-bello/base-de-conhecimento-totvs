---
content_hash: 237f1eb22f8b0fe7c4789540a55cdf2ab53d89420f7cb42ae2fb61b7d3b5ab15
fetched_at: '2026-06-29T00:10:10.726194+00:00'
page_id: '452719920'
product: rm
source: tdn-rm
title: De/Para Estado Civil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719920
version: 3
---

Devido à flexibilidade do sistema, que permite ao usuário incluir novos tipos de "Estado Civil" (tabela dinâmica "INT10") foi disponibilizado o "De/Para de Estado Civil" onde o usuário pode estabelecer o relacionamento dos tipos criados por ele, com as opções do leiaute do eSocial  
Exemplo do relacionamento padrão do sistema:

|  |  |
| --- | --- |
| **Estado Civil Labore** | **Estado Civil eSocial** |
| S-Solteiro | 1-Solteiro |
| C-Casado | 2-Casado |
| I-Divorciado | 3-Divorciado |
| P-Separado | 4-Separado |
| V-Viúvo | 5-Viúvo |

**Exemplo:**  
No Totvs Folha de Pagamento foi criado o Estado Civil do tipo "E-União Estável", porém, não existe esta opção no eSocial, então o usuário poderá definir o seguinte relacionamento.

|  |  |
| --- | --- |
| **Estado Civil Labore** | **Estado Civil eSocial** |
| E-União Estável | 2-Casado |
