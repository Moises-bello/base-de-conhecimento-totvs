---
content_hash: af8dfc72aa4fcf08e141c654c9f638494497fc06f21432aacce2b8555b1561c4
fetched_at: '2026-06-29T00:11:11.184853+00:00'
page_id: '64651285'
product: rm
source: tdn-rm
title: Alterando valores de MAXFILEHANDLES
type: documentation
url: https://tdn.totvs.com/display/LRM/Alterando+valores+de+MAXFILEHANDLES
version: 17
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                         **Versão:** *Aplicativo BDE* |
| **Processo** | **:** | Manutenção acesso ao banco de dados |
| **Subprocesso** | **:** | Alterando valores de 'MAXFILEHANDLES' e 'MAXBUFSIZES' |
| **Data da publicação** | **:** | 01/07/2013 |

Para correção desta mensagem "Erro de banco de dados: MAXFILEHANDLES", gentileza proceder da seguinte forma.

 

 

**Feche o sistema.**  
 Localize o BDE no seu painel de controle e abra o mesmo:

Altere os seguintes valores:

* + **MAXFILEHANDLES = 2048**
  + **MAXBUFSIZE = 4096**

Acesse o sistema novamente e realize o procedimento normalmente.

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
