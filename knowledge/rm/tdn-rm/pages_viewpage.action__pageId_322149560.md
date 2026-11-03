---
content_hash: f28dee90455461f48723436a9e1a0ebd451b81ef6668b73bcc37ef49cc464603
fetched_at: '2026-06-29T00:08:48.033265+00:00'
page_id: '322149560'
product: rm
source: tdn-rm
title: RMEDU00001_Configuração Soap-Ui
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=322149560
version: 3
---

Como configura o WebService e Obter as chaves primarias.

[Como Expor os Web Services do RM através do Host (recomendado)](http://tdn.totvs.com/pages/viewpage.action?pageId=89620766)

[Utilizando o TOTVS WS Client - Ferramenta para auxiliar a utilização dos Web Services providos pelo TBC](http://tdn.totvs.com/pages/viewpage.action?pageId=189307798)

Após configurar o ambiente acessar o link abaixo e validar a conexão

<http://localhost:8051/wsPageIndex/>

Onde Localhost deve ser igual ao servidor onde o WebService foi configurado

Ao acessar o Link a tela abaixo deve ser exibida

Para DataServer

**Ler candidatos Processo Seletivo**

Acesse o aplicativo SoapUi (Disponível na web gratuitamente <http://www.soapui.org/>)

Solicite um novo projeto e informe:

- O nome do projeto

- O link WSDL copiado anteriormente na configuração do WS RM

Será criado um projeto com as opções do print abaixo, onde deverão ser definidas as propriedades listadas:

- Name = Nome da Janela/página do ReadRecord para o projeto

- Encoding = UTF-8

- **Username** = Usuário do sistema RM

- **Password** = Senha do usuário do sistema RM

Localizar o Projeto Criado "Inscrição Processo Seletivo"

RM\_IwsSataServer

Localizar

ReadRecord - Request 1

Clicar com Botão direito Rename

Clicar duas vezes no Item criado.e a tela abaixo será exibida

Metodo de Aultenticação

Clicar em Auth

Clicar em Authorization alterar de No Authorization para Add Ner Authorization...

Selecionar a Opção Basic

Utilizar um usuario com autorização de gravar candidatos (Neste caso optamos por utilizar o usuario mestre, mas pode ser criardo um usuario com permissões necessarias para o cadastro de um candidato no EXE.)

Utilizar um usuario que permissões de criação, alteração e exclusão de registros.

Os procedimentos informados acima são os mesmos para todos os DataServers e Processos.
