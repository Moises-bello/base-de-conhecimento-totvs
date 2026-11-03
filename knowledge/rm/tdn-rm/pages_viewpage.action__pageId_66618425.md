---
content_hash: 9dadd7b2c4fc3965f40a96ff85a498bffa517a57e911335bccea4e85fd175007
fetched_at: '2026-06-29T00:11:16.285581+00:00'
page_id: '66618425'
product: rm
source: tdn-rm
title: Configuração da Action FinCFODataBR Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66618425
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52 |
| **Processo** | **:** | Alteração Actions do sistema (FinCFODataBR) |
| **Subprocesso** | **:** | Configurações de busca dos registros de Cli/For |
| **Data da publicação** | **:** | 12/07/2013 |

**Introdução**

O objetivo deste documento é apresentar a configuração da Action de Cli/For (FinCFODataBR), para que sejam visualizados vários registros na tela.

**Procedimento**

Normalmente a quantidade de registros de Cli/For em base de clientes são altas devido à enorme movimentação de informações. Quando se tem vários registros (maiores de 1000 registros), ao realizar um filtro genérico que traga TODOS os Clientes Fornecedores Cadastrados no Sistema, costuma aparecer a seguinte mensagem do sistema para o Usuário:

Esta mensagem não quer dizer que o sistema esta com erro e não consegue filtrar seus cadastros, mas sim que a quantidade de registros que seria retornado para o usuário na tela é maior que a configurada no sistema.

No print acima existem 9895 registros de Clientes/Fornecedores, mas esta Action (ação) esta configurada default para trazer no máximo 1000 registros.

Caso deseje aumentar a quantidade de registros para esta Action realize o procedimento abaixo:

Acesse o Menu **Cadastros | Segurança | Administrativa | Servidores de Aplicação:**

Faça o seguinte Filtro: (Este filtro vai trazer todos os possíveis cadastros de Servidores de aplicação cadastrados no sistema)

Na tela que abrir, clique em NOVO para poder realizar a nova Configuração:

Configure a **Action “FinCFODataBR”** da seguinte forma:

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
