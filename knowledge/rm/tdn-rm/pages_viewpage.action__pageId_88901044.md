---
content_hash: 716892e51235c9caeedb4217d1d274e3a5ad58929eebe87388a6c4c249d17f65
fetched_at: '2026-06-29T00:12:01.174487+00:00'
page_id: '88901044'
product: rm
source: tdn-rm
title: Ativando segurança do Alias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=88901044
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | Seguança |
| **Subprocesso** | **:** | Ativando segurança do Alias |
| **Data da publicação** | **:** | 18/10/2013 |

#### Ativando Segurança do Alias

**Pre-Requisitos**

* + Possuir o ambiente parametrizado em 3 camadas
  + A configuração deverá ser realizada no arquivo RM.Host.Service.exe.config (Do servidor de aplicação)

#### Iniciando a Parametrização

        Para ativar a segurança do RM.AliasManager.exe, deverá ser editado o arquivo **RM.Host.Service.exe.config**, acrescentado a configuração:

 **<add key="AllowChangeAliasesOnClient" value="false" />**

        Assim, quando o usuário posicionar o mouse sobre o parametrizador do alias o mesmo será apresentado bloqueado conforme imagem abaixo:

     

 

#### Ao realizar a edição do Gerenciamento de Alias Observe que os campos ficaram Bloqueados.

  

 

 

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
