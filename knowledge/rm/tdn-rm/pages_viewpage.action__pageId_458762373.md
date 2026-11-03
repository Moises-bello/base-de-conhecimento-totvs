---
content_hash: 76fc2fad3ed10a36522acde09ab12d4044de9e6b46d9bc6a3419fa4c7afcf4d8
fetched_at: '2026-06-29T00:10:13.846173+00:00'
page_id: '458762373'
product: rm
source: tdn-rm
title: Imóvel - Integração RM x Protheus - Item Contábil e Classe de Valor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458762373
version: 6
---

Tendo em vista a melhor visualização da integração contábil dentro da interface RM x Protheus foi implementado a partir da versão 12.1.24,  no cadastro de imóveis, os campos “Item Contábil” e “Classe de Valor”, provenientes do Backoffice Protheus

**Procedimento para utilização**

* Os campos “Item Contábil” e “Classe de Valor” só estarão disponíveis caso exista integração ativa do TIN com o Protheus, no EAI 1.0.
* No Protheus, os adapters abaixo devem estar configurados:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mensagem Única** | **Rotina** | **Mensagem** | **Envia** | **Recebe** | **Método** | **Operação** | **Canal** | **Alias** | Versão |
| Sim | CTBA040A | ACCOUNTINGITEM | Sim | Não | Síncrono | Todas | EAI | CTD | 1.000 |
| Sim | CTBA060 | CLASSVALUE | Sim | Não | Síncrono | Todas | EAI | CTH | 1.000 |

* Caso a integração esteja ativa, o formulário de imóveis será apresentado desta forma:

* Para cadastrar um Item contábil e Classe de valor no Protheus o usuário deve ir ao módulo contábil e acessar os respectivos cadastros que exibem as opções de inclusão destes items.
* Não é possível cadastrar um novo Item contábil ou Classe de valor diretamente na interface do RM.

---

Veja Também
