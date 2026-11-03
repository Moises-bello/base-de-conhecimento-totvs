---
content_hash: c3bbc2c306901955f1903523e1fd2c7d59210d5a2c7bf4a404dfb080050e9903
fetched_at: '2026-06-29T00:05:48.818633+00:00'
page_id: '102924324'
product: rm
source: tdn-rm
title: Criação de Servidor de Aplicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=102924324
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.50 x 11.82 x |
| **Processo** | **:** | Servidor de Aplicação |
| **Subprocesso** | **:** | Número de registros |
| **Data da publicação** | **:** | 20/11/2013 |

O sistema por default permite que sejam apresentados apenas 1000 registros nas visões de modo a melhorar o desempenho do sistema.

Nesta situação, ocorrerá o seguinte erro ao tentar carregar uma visão que possua mais de 1000 registros:

Neste exemplo, o erro ocorreu ao tentar acessar a tela de Lançamentos -> Manutenção de Lançamentos no RM Saldus:

Para que isso seja modificado é necessária a criação de um servidor de aplicação com a permissão de mais registros na visão.

O cadastro desse servidor de aplicação deve ser realizado em: Cadastros--> Segurança --> Administrativa--> Servidores de aplicação:

Caso o acesso seja realizado via MDI, acesse o Sistema Serviços Globais -> Aba Serviços -> Servidores de Aplicação, conforme segue abaixo:

Deve-se criar um novo Servidor de Aplicação com o número máximo de registros, por exemplo, 5000.

Para tanto, inicialmente faz-se necessário ter conhecimento do nome da Action que será realizada a liberação dos registros.

Essa informação pode ser solicitada à equipe do aplicativo, neste caso, o cliente deverá entrar em contato com o suporte do RM Saldus, e solicitar o nome da Action.

Ou, poderá acessar a visão novamente, se atentando para o nome da Action que é apresentada ao se carregar a visão. O nome da Action estará visível no canto inferior da tela, à esquerda:

Neste caso, o nome da Action é CtbLanIntegradoAction.

Obs.: Nem sempre o nome é o mesmo, portanto, é necessário confirmar o mesmo com o aplicativo.

Tendo conhecimento do nome da Action, crie o Servidor de Aplicação com o número de registros desejado:

Neste caso, o nome da Action utilizada será CtblanData.

Após criação do Servidor de Aplicação, ao acessar a visão de Lançamentos -> Manutenção de Lançamentos, todos os registros serão apresentados, sem mensagem de erro:

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
