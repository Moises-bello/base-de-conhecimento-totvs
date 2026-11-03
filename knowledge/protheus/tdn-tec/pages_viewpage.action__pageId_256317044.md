---
content_hash: 830c30d6adbeefb513c664d417982dc102f5dbaeafb9f4bb207a75fbf08549ca
fetched_at: '2026-07-02T19:24:20.529583+00:00'
page_id: '256317044'
product: protheus
source: tdn-tec
title: DBAccess - Seção [General], chave ShowAllErrors
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=256317044
version: 5
---

Permite ativar ou desativar o registro de erros no dbaccess.log de qualquer erro retornado por *statements* submetidos ao SGBD.  
Até mesmo os *statements* que possuam algum tratamento adicional de recuperação de erro esperado, como erro de violação de *Primary Key* (RECNO) em inserção de registro, serão recuperados.

* Esta configuração  está disponível no true com build superior a 42.20160402.
* Recomenda-se que esta configuração seja ativada apenas para fins de diagnóstico específico.
* Esta configuração é assumida para todos os ambientes do ambiente.

**Valores válidos:**

| Valor | Descrição |
| --- | --- |
| 0 | Desabilita o registro das mensagens de erro (padrão) |
| 1 | Habilita o registro das mensagens de erro |

**Exemplo:**
