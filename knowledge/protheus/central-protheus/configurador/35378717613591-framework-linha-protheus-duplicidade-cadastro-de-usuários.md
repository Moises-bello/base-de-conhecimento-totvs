---
article_id: 35378717613591
category: Configurador
content_hash: f810dc8d51ed4e25d51ebedf2d817e238db525eca27ea3c69230aecbacf25fbc
fetched_at: '2026-06-28T22:42:19.278880+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus - Duplicidade cadastro de usuários
type: support-article
updated_at: '2025-10-03T14:14:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35378717613591-Framework-Linha-Protheus-Duplicidade-cadastro-de-usu%C3%A1rios
---

**Dúvida**

Mensagem apresentada ao incluir usuário:

**THREAD ERROR ([19736], danilo.aquino, SPON010118974)   03/10/2025 08:04:06**  
**SYS\_USR: DB error (Insert): -37 File: SYS\_USR - Error : 2601 (23000) (RC=-1) - [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Não é possível inserir uma linha de chave duplicada no objeto 'dbo.SYS\_USR' com índice exclusivo 'SYS\_USR\_UNQ'. O valor de chave duplicada é (000886, 0).**

**Ambiente**  
Protheus - Configurador - 12

**Solução**

* Verifique qual é o último código de usuário cadastrado na rotina de usuário, no SIGACFG
* Acesse a rotina de controle de numeração (APCFG110), procure manualmente pela chave: SYS\_USRUSR\_ID e ajuste a numeração da mesma, para que seja possível a inclusão do novo usuário, colocando no grid inferior o proximo número referente ao último cadastro de usuario e no grid superior o proximo número do grid inferior.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35379052407447)
