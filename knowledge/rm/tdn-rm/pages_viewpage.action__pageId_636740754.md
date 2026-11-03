---
content_hash: a97127a8e5ef325d7689ce3aa27400c11f27cf508207042f8de1e70688d37b0b
fetched_at: '2026-06-29T00:11:06.909509+00:00'
page_id: '636740754'
product: rm
source: tdn-rm
title: MDI - Cenários - Inclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=636740754
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**12.1.31 |
| **Processo** | **:** | Cenários |
| **Subprocesso** | **:** | Parametrização de cenários |
| **Data da publicação** | **:** | 01/09/2021 |

#### Incluindo cenários no sistema

O Cenário é um ambiente onde você poderá colocar vários recursos da Linha RM em um só lugar. Entre os recursos estão as telas .NET, cadastro de Consultas SQL, Gráficos, Canais RSS e Atendimentos do CRM. Cada um destes recursos é chamado de RM Part.

Você poderá ainda incluir vários cenários com estes recursos, distribuindo-os de acordo com o objetivo de cada cenário: Cenário financeiro, cenário administrativo, cenário com informações de estoque.

Alerta

É importante frisar que no sistema Corpore.Net, apenas as seguintes **RMParts** estão disponíveis: **Cubo, Gráfico, Consulta SQL**e **Relatórios**. Caso o Cenário acessado pelo Corpore possua RMParts diferentes das citadas, estas **NÃO**serão exibidas

**Desenvolvimento/Procedimento**

**1)** **Criando Cenários no sistema**

***OBS****: Caso **NÃO** tenha acesso / permissão ao ícone **“PAINEL DE CENÁRIOS”,** verifique a partir da **opção** “Liberando acesso para Usuário acessar Painéis de Cenários”        disponibilizada ao final deste material.*

A primeira tela apresenta quais são as RM Parts que poderão ser utilizadas para montar este Painel de cenários

**Como exemplo utilizaremos CUBOS e Gráficos para criação do nosso Painel de Cenários**

Observe que será apresentada a **inclusão do Gráfico** Selecionado no painel de Cenários.

Abaixo segue o Painel com os Gráficos e Cubos inseridos. Para disponibilizar as RM Parts ao lado uma da outra basta selecionar a barra e arrasta-las soltando-a na posição desejada.

**2)** **Funcionalidades disponibilizadas para Painel de cenários.**

**3)** **Liberando acesso para Usuário acessar Painéis de Cenários**

Primeiramente deverá ser disponibilizado acesso para o usuário utilizar o recurso no sistema. Abaixo segue o modelo como proceder para habilitar este processo.

Acesse o RM.EXE e siga as orientações:

false

*A partir da versão **12.1.23 não será mais possível o uso da Planilha.Net como RMPart nos Cenários**. Permanecendo a inclusão de [Planilhas RM](http://tdn.totvs.com/x/MceFDg) somente.*

**OBS:** Após estes processos será necessário “SAIR” do sistema e acessá-lo novamente para validar estas alterações parametrizadas.
