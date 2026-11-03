---
content_hash: d7850d1a2b39530f115683b964515c9d6bc62415a874db4bd43a1f020ebf2b3f
fetched_at: '2026-06-29T00:11:50.724573+00:00'
page_id: '84541591'
product: rm
source: tdn-rm
title: Permissão para Geração de Guias Automaticamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=84541591
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:**11.52 |
| **Processo** | **:** | Período de Apuração |
| **Subprocesso** | **:** | Permissão de Jobs |
| **Data da publicação** | **:** | 29/07/2013 |

Solução à inconsistência: “Você não está autorizado a utilizar essa funcionalidade”; vide orientações abaixo:

Orientações:

Necessário acessar a nova MDI e permissões do usuário:

Para isto acesse a pasta RM.Net, em: xxxx... \totvs\CorporeRM\RM.Net e execute o RM.exe. 

Caso não tenha nenhum Alias Cadastrado, será necessário cadastrar.

Após logar com usuário e senha, entre no menu e clique em “Serviços Globais.

Vá na aba segurança -  Usuário, e em Sistema escolha a opção de “Serviços Globais”.

Seleciona o usuário e edite-o.Na aba de Segurança, confirme se esta habilitado a opção da coligada e seleciona o perfil vinculado ao usuário.

OBS: Não recomendado associar mais de um Perfil, pois um pode influenciar no outro.

Após ter confirmado o Perfil do usuário, acesse a opção de Segurança – Perfis. Vide a opção Sistema e selecione a opção “Serviços Globais”.

 

Edita o Perfil do usuário e na aba “Acesso a Menus” – localize a opção “Ambiente” – Gerenciamento de Jobs e habilite a permissão.

Realize Logout/Login no sistema e posteriormente realize o processo desejado.

|  |  |
| --- | --- |
|  | **Para maiores informações:**   [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ApuracaoISS.aspx)  **COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal) |
