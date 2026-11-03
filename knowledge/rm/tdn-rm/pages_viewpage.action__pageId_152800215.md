---
content_hash: 53778d41e2ab2de4c47c01651140ae9d3321188549dcfb2eaf2e2fb802122174
fetched_at: '2026-06-29T00:05:56.549381+00:00'
page_id: '152800215'
product: rm
source: tdn-rm
title: Criando a Aplicação RM no Identity
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=152800215
version: 13
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework         **Versão :** 11.83 |
| **Processo** | **:** | Fluig |
| **Subprocesso** | **:** | Criando a Aplicação RM no Identity |
| **Data da publicação** | **:** | 18/08/2014 |

# Objetivo

O objetivo deste documento é ensinar como criar a aplicação RM no Identity.

# Criando a aplicação

Acesse o menu Ações, do Identity e clique em . Será exibida a tela de inclusão de um novo aplicativo.

|  |
| --- |
| Preencha esses campos da maneira que desejar |

|  |
| --- |
| No caso da aplicação RM o modo de login deve ser o **Executável SAML**.    **O campo URL da página de login será preenchido automaticamente.** |
| Os campos **URL do Consumidor de Asserções e Destinatário** devem ser preenchidos da seguinte maneira:  **http(s):// + o IP da máquina host + :HttpPort configurada + /RMCloudPass/SSOSaml2**  Para mais informações sobre [HttpPort](http://tdn.totvs.com/x/phKqC) . |
| O campo **URL Rest** deve ser preenchido da seguinte maneira:  **http(s):// + o IP da máquina host + :HttpPort configurada + /RMRestScim**  Para mais informações sobre [HttpPort](http://tdn.totvs.com/x/phKqC) . |
| Clique em salvar. |

Após salvar a aplicação basta associar a mesma ao usuário do identity.

# Associando a aplicação ao usuário

Acesse o menu Ações, do IIentity e pesquise pelo nome do aplicativo criado. Após localizar o aplicativo basta clicar no nome dele e entrar nas configurações do app.

|  |  |  |
| --- | --- | --- |
| Selecione a opção | Clique na opção | Após pesquisar o usuário basta clicar em |

A aplicação poderá ser acessada pela opção de menu do Identity.

## **OBS: Este processos pertence a uma inovação que está sofrendo constantes alterações, algumas imagens poderão estar divergentes com a tela atual do sistema.**

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
