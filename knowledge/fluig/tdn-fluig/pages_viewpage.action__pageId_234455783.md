---
content_hash: bb98478d271d01abe44f4aab81203a6617c73fc7a9c6d97450b05cf66b9bed9a
fetched_at: '2026-06-28T21:35:21.812670+00:00'
page_id: '234455783'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Oauth application
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=234455783
version: 65
---

.\*ndice

# Falando de OAuth *application*...

---

OAuth é um protocolo padrão aberto para autorização, que é comumente utilizado para permitir que terceiros acessem os dados de um usuário sem a necessidade de conhecer a senha do mesmo.

A plataforma possui uma API Pública com os principais serviços disponíveis na plataforma. Através da API é possível criar mensagens em nome do usuário, adicionar um contato como favorito, criar artigos e muito mais. Para que aplicativos possam atuar em nome de um usuário ou em nome próprio, a autorização é realizada através do protocolo OAuth, sendo necessário que ele esteja previamente cadastrado na plataforma com suas chaves pública e privada.

Caso seu aplicativo execute ações em nome próprio, você pode criar um usuário aplicativo (Opcional). Se desejar que o usuário aplicativo execute ações em nome de outro usuário cadastrado na plataforma, basta selecionar a opção Permite Impersonalização. Selecionando este recurso, o usuário aplicativo pode, por exemplo, fazer um post em uma comunidade, publicar documentos e movimentar processos. em nome de outro usuário.

O cadastro de OAuth *application* para servidores é uma autorização que o servidor de destino concede pra que o servidor atual possa exportar páginas sem a necessidade de baixar e importar arquivos.

## Ver OAuth *applications*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **OAuth *application***.

**04.** Veja os OAuth *applications* existentes.

## Adicionar OAuth *application*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **OAuth *application***.

**04.** Clique em **Adicionar**.

**05.** Insira a ***Consumer Key***.

**06.** Informe a descrição.

**07.** Selecione o **OAuth** ***Provide**r*.

**08.** Defina ***Consumer Secret*.**

**09.** Clique em **Salvar**.

#f2f2f2#f2f2f2

Para mais detalhes sobre o cadastro e o uso, acesse a documentação .

## Criar usuário aplicativo (opcional)

---

Importante!

Este usuário será exclusivo para integrações e customizações de aplicativos, por isso não deve ser utilizado para navegação na plataforma. Portanto, não será possível efetuar login com ele na plataforma.

Usuários aplicativos são considerados na contagem de  da plataforma e também na contagem de licenças quando estão ativos. Mais informações podem ser obtidas em [Licenciamento da plataforma](https://tdn.totvs.com/display/fluig/Licenciamento+da+plataforma).

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **OAuth *application***.

**04.** Selecione um Oauth *application* existente.

**05.** Clique em **Usuário aplicativo**.

**06**. Clique em **Gerar *token***.

#f2f2f2#f2f2f2solid

Neste momento é criado um *token* e um usuário na plataforma para que o aplicativo possa atuar em nome de um usuário ou em nome próprio.

**07**. Para gerenciar as informações de cadastro, entenda seu conceito abaixo:

#f2f2f2#f2f2f2solid

**Nome do usuário**Nome do usuário criado pelo sistema. Este campo vem preenchido com o valor da Descrição cadastrada na tela Adicionar Oauth *Application*. Este nome pode ser alterado para um de sua preferência.

**Permite impersonalização**Selecionando esta opção, permite que o usuário aplicativo execute ações em nome de outro usuário.

**Escolher imagem**Altera a foto padrão do sistema que identifica o usuário cadastrado.

**08.** Clique em **Alterar.**

## Cadastrar OAuth *application* para servidores

---

trueimageVeja a imagem#0897E9INLINE

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **OAuth *application***.

**04.** Clique em **Adicionar.**

**05.** Defina ***Consumer Key*.**

#f2f2f2#f2f2f2

Quem administra a empresa pode escolher o valor da *Consumer Key.*

**06.** Informe uma descrição.

#f2f2f2#f2f2f2

A descrição não pode conter acentos e caracteres especiais.

**07.** Selecione o **OAuth *Provider*** cadastrado com as especificações descritas em [Cadastrar OAuth Provider para servidores](https://tdn.totvs.com/pages/viewpage.action?pageId=234455787#Plataforma%E2%9D%99OAuthprovider-CadastrarOAuthProviderparaservidores).

**08.** Defina ***Consumer Secret*.**

#f2f2f2#f2f2f2

Quem administra a empresa pode escolher o valor da Consumer Secret.

**09.** Clique em **Salvar**.

#f2f2f2#f2f2f2

Após o cadastro do OAuth *application* é necessário habilitar as opções de Usuário aplicativo.

**10.** Selecione o OAuth *application* criado e acionar **Usuário aplicativo.**

**11.** Clique em **Gerar *token*.**

**12**. Habilite opção de impersonalização.

**13.** Clique em **Alterar.**

**14.** Clique em **Painel de controle**, agrupador **Pessoas**,  **Usuários**.

**15.** Selecione o usuário Aplicativo OAuth criado e clique em **Editar**.

**16.** Conceda o papel de administração ao usuário.

Não pare por aqui!

Confira a [documentação](http://tdn.totvs.com/x/jYtJF) para saber mais sobre o cadastro de servidores.

## Renovar *token*

---

**01.**Para alterar os valores ***Access token*** e ***Token secret*** , clique em **Renovar *token***.

#f2f2f2#f2f2f2

***Access token****Token* de acesso para autenticação de requisições gerado pela servidor de aplicação de forma automática.

***Token secret***Chave para autenticação de requisições gerado pela servidor de aplicação de forma automática.

## Editar OAuth *application*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **OAuth *application***.

**04.** Selecione o OAuth *application* que deseja editar.

**05.** Clique em **Editar**.

**06.** Efetue as alterações desejadas.

#f2f2f2#f2f2f2

A plataforma não permite que o campo OAuth *Provider* seja editado.

**07.** Clique em **Salvar.**

## Excluir OAuth *application*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **OAuth *application***.

**04.** Selecione o OAuth *application* que deseja remover.

**05.** Clique em **Remover**.

**06.** Clique em **OK**.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
