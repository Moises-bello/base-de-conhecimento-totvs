---
content_hash: e1664f01b0f8095a34d1054b69b20fef6d5d79b90def80588c7ebbe05f502cd3
fetched_at: '2026-06-28T21:35:22.281372+00:00'
page_id: '235571102'
product: fluig
source: tdn-fluig
title: Modo de Provisionamento Fluig
type: documentation
url: https://tdn.totvs.com/display/fluig/Modo+de+Provisionamento+Fluig
version: 40
---

# Índice

true.\*ndicenone

# Pré-requisitos

---

* O ambiente Fluig precisa estar em uma **atualização Waterdrop (1.6.4) ou superior**.
* É necessário que tenha sido realizada a configuração de [acesso externo](https://centraldeatendimento.fluig.com/hc/pt-br/articles/360026366992) no ambiente Fluig.

# Sobre o provisionamento Fluig

---

Provisionamento é o processo de criação automática de usuários do Identity em uma outra aplicação ou serviço. Existem tipos distintos de provisionamento disponíveis, como SCIM, Salesforce, Google e Fluig. Nesta página será abordada a configuração do Modo de Provisionamento Fluig.

Em uma  entre fluig e Identity, o provisionamento do usuário é realizado apenas quando o indivíduo faz o primeiro acesso ao fluig através do Identity. Contudo, é possível configurar o aplicativo para que a criação no fluig seja feita ao atribuir o app para o usuário no Identity.

Por exemplo, ao criar o usuário João de Souza em <http://minhaempresa.fluigidentity.com>, o administrador poderá atribuir a ele um aplicativo Fluig. Após a atribuição, o Identity enviará uma requisição via API ao Fluig para que o perfil do usuário João de Souza também seja criado automaticamente na plataforma.

Saiba como fazer atribuição de aplicativos [Gerenciar usuários](http://tdn.totvs.com/pages/viewpage.action?pageId=317306108#Gerenciarusuário-Atribuiraplicativosaousuário).

Atenção

Usuários com status **Convidado** ou **Desativado** não serão provisionados, apenas usuários com status **Ativo**. Para usuários convidados, o provisionamento ocorrerá no momento em que a conta for ativada.

# Configuração de provisionamento no aplicativo

---

Siga o passo a passo para habilitar o provisionamento de usuários em um aplicativo Fluig.

falseprovisionamentotruePasso 1

* Acessar o Identity com o Administrador do contexto.

* Acionar o menu **Aplicativos**.

* Localizar o aplicativo **Fluig** e clicar sobre o nome para acessar as configurações.

* Acionar a opção **Clonar** para criar um novo aplicativo com as mesmas propriedades do atual.

Passo 2

* Selecionar a aba **Provisionar**.

* Marcar a opção **Habilitar Provisionamento**.

Passo 3

* No item **Modo de Provisionamento**, marcar a opção Fluig.

* Em **Tipo de Autenticação**, marcar a opção OAuth 1.0a.

* No campo **URL REST**, informar a URL da API de criação de usuários do Fluig, substituindo {dominio} pelo endereço de acesso ao Fluig:

* Em **Nome do usuário do Administrador do Domínio**, informar o e-mail de um usuário que seja administrador tanto do Fluig quanto do Identity. Este usuário deve existir em ambas as ferramentas.

* Informar a senha desse mesmo administrador no campo **Senha do Administrador do Domínio**.

* Definir uma senha padrão temporária para os usuários que serão criados através do provisionamento em **Senha Temporária do Usuário**.

4Passo 4

* Para concluir, é preciso atribuir o aplicativo aos usuários. Para saber mais, acesse a documentação [Atribuir aplicativos aos usuários](https://www.google.com/url?q=https://tdn.totvs.com/pages/viewpage.action?pageId%3D203763890&sa=D&source=hangouts&ust=1586283909786000&usg=AFQjCNGKNwXza4hnzGyU6EkDKgl8GH2DlQ).

#fdf7e8#fdf7e8

![](http://tdn.totvs.com/download/thumbnails/286221066/importante.png)

**IMPORTANTE!**  
Dependendo da quantidade de usuários que estejam na fila, o processo de provisionamento pode demorar a partir de 15 minutos para ser concluído.
