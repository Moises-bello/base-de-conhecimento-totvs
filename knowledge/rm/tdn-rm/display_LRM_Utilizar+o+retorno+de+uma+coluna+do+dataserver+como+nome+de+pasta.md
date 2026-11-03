---
content_hash: 952bddfb1543931d58174db0a3f8193bdb4737585e15223c0aa7802fee45c9bd
fetched_at: '2026-06-29T00:05:56.532447+00:00'
page_id: '152799429'
product: rm
source: tdn-rm
title: Utilizar o retorno de uma coluna do dataserver como nome de pasta
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizar+o+retorno+de+uma+coluna+do+dataserver+como+nome+de+pasta
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework |
| **Processo** | **:** | Integração RM X ECM |
| **Subprocesso** | **:** | Utilizar o retorno de uma coluna do dataserver como nome de pasta |
| **Data da publicação** | **:** | 12/08/2014 |

**Objetivo:**A finalidade da parametrização ECM de  é criar uma estrutura de pastas no ECM. **Sendo que o nome da pasta será o valor do registro selecionado de acordo com qual coluna do dataserver escolhida na configuração.**

Primeiramente é necessário realizar a configuração. No exemplo iremos utilizar a visão de usuários.Para acessar a visão basta acessar o menu   aba  , logo após o menu .

Após a visão ter sido aberta é necessário clicar na funcionalidade  opção  ,  e seguir os passos abaixo.

|  |  |  |
| --- | --- | --- |
| Passo 1    Clique em avançar | Passo 2    Selecione a opção | Passo 3    Na opção ECM escolha a pasta pai.  Na opção Colunas do data server escolha a coluna do dataserver. No exemplo foi escolhida a coluna CODUSUARIO.  Após selecionar os parâmetros clique em avançar e executar. |

Após executar os passos acima a parametrização "utilizar o retorno de uma coluna do dataserver como nome de pasta" foi realizada.

## Utilizando a Integração

Com a visão ainda aberta basta seguir os passos abaixo.

|  |
| --- |
| Selecione um registro da visão e acesse  a funcionalidade  opção . |

Será aberta a tela de anexos da Integração GED.

|  |  |  |
| --- | --- | --- |
| Clique em incluir() . | Clique em  e selecione o arquivo que deseja enviar para o ECM. | Será criada uma pasta com o nome do conteúdo da coluna CODUSUARIO do registro selecionado. Neste caso mestre. |

**Pasta criada dentro do ECM.**

|  |
| --- |
|  |

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
