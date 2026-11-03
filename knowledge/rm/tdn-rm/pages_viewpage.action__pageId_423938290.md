---
content_hash: a8bc0f4636e5e4e6cc2e5227fa39253bd4fb0955e07fdfafa475961b1cc2429f
fetched_at: '2026-06-29T00:09:26.174979+00:00'
page_id: '423938290'
product: rm
source: tdn-rm
title: 'Exemplo 1:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938290
version: 2
---

Não optando pela composição de patrimônio, o sistema realiza a integração da aquisição de compras considerando que cada item de uma nota fiscal no qual o produto esteja com um grupo de patrimônio parametrizado, vai transformar em um ativo imobilizado no TOTVS Gestão Patrimonial.  
 

|  |  |  |  |
| --- | --- | --- | --- |
| **#** | **Item Nota** | **Quantidade** | **Patrimônio** |
| 1 | Cadeira giratória | 1 | *Será criado um patrimônio para este item* |
| 2 | Mesa de Escritório 4 lugares | 1 | *Será criado um patrimônio para este item* |
| 3 | Armário escritório | 1 | *Será criado um patrimônio para este item* |

Em determinadas situações da composição de patrimônio, um item da nota não irá representar um patrimônio, o patrimônio será  composto por mais de um item da nota.  
 

|  |  |  |  |
| --- | --- | --- | --- |
| **#** | **Item Nota** | **Quantidade** | **Patrimônio** |
| 1 | CPU | 1 | *Estes três itens irão constituir o patrimônio "COMPUTADOR"* |
| 2 | Teclado | 1 |
| 3 | Mouse | 1 |
