---
content_hash: e73fecc97fe9e6e763acaa8c0236631fce1793a42ca710d5d16a55467ac747c2
fetched_at: '2026-06-29T00:11:48.535567+00:00'
page_id: '82477734'
product: rm
source: tdn-rm
title: Alteração do Perfil do usuário nova MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=82477734
version: 6
---

lik

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                         **Versão:** 11.52.57/11.82.27 |
| **Processo** | **:** | Alteração do Perfil do usuário nova MDI atribuindo acesso ao Gerador de Saídas |
| **Subprocesso** | **:** | Gerador de Saídas |
| **Data da publicação** | **:** | 26/07/2013 |

**1.** Acesse a pasta RM.Net, em: xxxx... \totvs\CorporeRM\RM.Net e execute o RM.exe

**2.**  Caso não tenha nenhum Alias Cadastrado, será necessário cadastrar. 

**3.**  Após logar com usuário e senha,  Após logar com usuário e senha, entre no menu e clique em “Serviços Globais Serviços Globais”.

**4.**  Vá na aba segurança> Usuário,  e em Sistema escolha “Gestão Fiscal”

**5.** Localize o usuário e dê um duplo clique sobre o mesmo. Vá na aba Segurança e verifique qual o perfil está associado ao seu usuário. 

**6.**  Clique em OK e agora clique em Segurança> Perfil.

**6.1** Altere o Sistema para Integração

**7.** Localize o perfil que foi identificado no cadastro do usuário, e dê um duplo clique sobre o mesmo.

**8.**  Acesse a aba “Acesso a Menus Acesso a Menus” e localize o item 01.01.04 – Gerador  Gerador de Saídas 

\*\* **Lembrando que é necessário conferir se há permissão para o perfil nos Sistemas de Serviços Globais, Gestão Fiscal e Integração.**

Dê acesso ao grupo 01.01.04.02 - Categoria , clicando sobre este grupo e em Permitir Acesso. 

Obs: Recomenda-se que seja dado acesso a todo o grupo 01.01.04 - Gerador de Saída.

**9.** Clique em Salvar e Ok. Em seguida acesse o RmLiber em Utilitarios>Gerador de Saídas> Categoria. O botão de incluir categoria estará habilitado.

|  |  |
| --- | --- |
|  | **Para maiores informações:**   [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ApuracaoISS.aspx)  **COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal) |
