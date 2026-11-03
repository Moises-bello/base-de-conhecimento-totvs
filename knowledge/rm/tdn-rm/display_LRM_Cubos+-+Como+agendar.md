---
content_hash: a48b81a45a04780bd2a56563c8946edd1a83fc512268d1414370812bbb31a1e5
fetched_at: '2026-06-29T00:11:16.297562+00:00'
page_id: '66618974'
product: rm
source: tdn-rm
title: Cubos - Como agendar
type: documentation
url: https://tdn.totvs.com/display/LRM/Cubos+-+Como+agendar
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | CUBO |
| **Subprocesso** | **:** | Agendamento de Cubos |
| **Data da publicação** | **:** | 03/07/2013 |

#### Para a realização de agendamento de Cubos deverá ser realizado o seguinte procedimento.:

1 - Realize a alteração dos arquivos config alterando a TAG como TRUE.

**Os arquivos a serem alterados são:**

- RM.AliasManager.exe.config

- RM.exe.config

- RM.Host.exe.config

- RM.Host.Service.exe.config

- RM.Lib.Gerador.Execute.exe.config

Verifique as configurações do **ALIAS**

Pare o Serviço RM.Host em seguida apague o arquivo \_Broker.DAT

Em seguida reinicie o Serviço RM.Host (até aparecer a palavra INICIADO)

Acesse o sistema.

Ao atualizar o cubo será apresentada a Tela para realizar o agendamento do mesmo, conforme imagem abaixo:

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
