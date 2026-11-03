---
content_hash: 59bda3ddaa032ccb4cc7a09d9d8141e404993d097d6c0fbaed9d7c795b0efc81
fetched_at: '2026-06-28T21:35:19.717850+00:00'
page_id: '221554568'
product: fluig
source: tdn-fluig
title: Identity | Tutorial da API SCIM REST
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Tutorial+da+API+SCIM+REST
version: 59
---

# Índice

true.\*ndicenone

# APIs para User Experience

---

Este tutorial explica como utilizar as APIs Identity para as funcionalidades de User Experience baseadas em SCIM. APIs baseadas em SCIM são um subconjunto de APIs REST do Identity, que estão documentadas neste artigo.

Localização das APIs: <https://app.fluigidentity.com/rest/swagger-ui/index.html>

## Prepare o Ambiente

Este tutorial utiliza um cliente SOAP para acessar as APIs REST do Identity. Este conjunto de instruções demonstra a configuração do cliente.

falseambientetruePasso 1  

* Faça o *download* do aplicativo SoapUI em [http://www.soapui.org/.](http://www.soapui.org/)

* Abra o aplicativo SoapUI.

* Faça o *download* do projeto teste CloudPass-Rest-soapui-project.xml.

Passo 2

* Importe o projeto teste CloudPass-Rest-soapui-project.xml

Passo 3

* Clique em **File** → **Import Project**.

* Selecione o arquivo CloudPass-Rest-soapui-project.xml.

## Cliente SOAP para Windows

O projeto importado possui exemplos de dados e chamadas das APIs. Para entender a estrutura da API, podemos observar a chamada Create User.

Lembre-se de definir o *endpoint* para o *sandbox* de desenvolvedores.

falsecliente\_soaptrueAbrir requisição

* Navegue para Users → Create User → Post e clique em Request 1 conforme a imagem abaixo:

1. É o nome da API e seu caminho relativo
2. É o método HTTP da API
3. É o link da janela de requisição. Dê um duplo clique para abrir a janela de detalhes da API.

Área de requisição

* Na imagem abaixo:

1. Contém a área para parâmetros de URL.
2. Contém a área do corpo da requisição HTTP.
3. Contém o botão **Send request**.

# APIs de Usuário

---

As APIs de Usuário possuem quatro funções: *Create, Get, Update e Delete*. Esta sessão irá utilizar cinco passos para demonstrar essas funções.

* Criar um novo usuário
* Obter os dados de um usuário pelo ID
* Atualizar usuário
* Remover um usuário pelo ID
* Ao tentar obter o usuário removido, a chamada retorna um erro

## Criar um novo usuário

falsecreate\_usertruePasso 1  

* Navegue para Users → Create User → POST e clique em Request 1.

Passo 2

* Insira os dados do novo usuário, e clique no botão Send.

Passo 3

* Verifique o retorno clicando na aba JSON.

## Obter dados do usuário pelo ID getuser

falseget\_usertruePasso 1

* Navegue para Users → Get User by Id → GET e clique em Request 1.

Passo 2

* Insira o valor do userId na área de parâmetros de URL.

Passo 3

* Clique no botão *Send request*, aguarde o resultado e verifique o mesmo.

## Atualizar usuário

falseupdate\_usertruePasso 1

* Navegue para Users → Update User → PUT e clique em Request 1.

Passo 2

* Mude o campo displayName para "jacob-update".

Passo 3

* Clique no botão Send request, aguarde o resultado e então verifique o mesmo.

## Remover usuário pelo userId

falsedelete\_user\_by\_idPasso 1

* Navegue para Users → Delete User → DELETE e clique em Request 1.

Passo 2

* Insira o userId.

Passo 3

* Clique no botão Send request, aguarde o resultado e verifique o mesmo.

## Ao tentar obter um usuário removido, a chamada retorna erro

Use a chamada  para o ID do usuário que acabou de ser removido (veja acima).

# API de Recursos

---

Recursos são implementados para serem utilizados como opções de menu, mas podem ser estendidos para outras aplicações. Nesta seção nós iremos aprender como criar, listar e deletar um recurso.

Este cenário de teste segue os seguintes casos de teste.

* Criar recursos
* Obter o recurso menu1 pelo ID
* Obter todos os recursos de aplicações
* Remover o recurso menu1 pelo ID

## Criar recursos

Irá criar três recursos: menu1, menu2 e menu3 para aplicação

falsecreate\_resourcetruePasso 1

* Navegue para Resources → Create Resource → POST e clique em Request 1.

Passo 2

* Insira os dados dos recursos menu1, menu2, menu3 e o applicationId.

Passo 3

* Clique no botão Send request, aguarde o resultado e verifique o mesmo.

## Obter o recurso menu1 pelo ID

falseget\_resourcePasso 1

* Navegue para Resources → Get Resource → GET e clique em Request 1.

Passo 2

* Insira o ID do menu1.

Passo 3

* Clique no botão Send request, espere pelo resultado e verifique o mesmo.

## Obter todos os recursos de aplicações

Irá obter três recursos: menu1, menu2, menu3.

falseget\_all\_resourcestruePasso 1

* Navegue para Resources → Get All Resources → GET e clique em Request 1.

Passo 2

* Insira o applicationId.

Passo 3

* Clique no botão Send request, espere pelo resultado e verifique o mesmo.

## Remover o recurso menu1 pelo ID

falsedelete\_by\_idPasso 1

* Navegue para Resources → Delete by Id → DELETE e clique em Request 1.

Passo 2

* Insira o ID do recurso menu1.

Passo 3

* Clique no botão Send request, espere pelo resultado e verifique o mesmo.

# APIs de Papéis

---

Papéis são conexões entre usuários e direitos.

Este cenário de testes inclui o seguinte teste de caso:

* Criar dois papéis: "user" e "admin" para a empresa

## Criar dois papéis: "user" e "admin" para a empresa

falsecreate\_rolesPasso 1

* Navegue para Roles → Create Roles → POST e clique em Request 1.

Passo 2

* Insira o valor companyId e os dados para os papéis "user" e "admin".

Passo 3

* Clique no botão Send request, espere pelos resultados e verifique o retorno.

# APIs de Direitos

---

Direitos são como os recursos são atribuídos aos usuários.

Este cenário de testes contém os seguintes casos de teste:

* Criar o usuário "Jacob"
* Criar os recursos "menu1", "menu2", "menu3"
* Atribuir os recursos "menu1", "menu2" para o usuário "Jacob"
* Deletar todos os recursos com direitos do usuário "Jacob"

## Criar o usuário "Jacob"

falsecreate\_user\_jacobtruePasso 1

* Navegue para Users → Create User → POST e clique em Request 1.

Passo 2

* Insira os dados do novo usuário e clique no botão Send.

Passo 3

* Aguarde os resultados e verifique os mesmos.

## Criar os recursos "menu1", "menu2", "menu3"

falsecreate\_resources\_jacobPasso 1

* Navegue para Resources → Get All Resources of Application → GET e clique em Request 1.

Passo 2

* Insira os dados dos recursos menu1, menu2 e menu3 e preencha o applicationId.

Passo 3

* Clique no botão Send request, espere os resultados e verifique o mesmo.

## Atribuir os recursos "menu1" e "menu2" para o usuário "Jacob"

falseget\_resources\_of\_userPasso 1

* Navegue para Entitlements → Assign Resources to User → POST e clique em Request 1.

Passo 2

* Insira o userId e o valor do ID dos recursos "menu1" e "menu2".

Passo 3

* Clique no botão Send request, espere pelo resultado e verifique o mesmo.

## Deletar todos os recursos com direitos do usuário "Jacob"

unassign\_all\_resourcesPasso 1

* Navegue para Entitlements → Unassign all Resources to User → DELETE e clique em Request 1.

Passo 2

* Insira o userId.

Passo 3

* Clique no botão Send request, espere pelo resultado e verifique se o mesmo não possui nenhum direito.

# APIs de Favoritos

---

Marcações de favoritos adicionadas a recursos para o usuário.

Este cenário de teste incluí os seguintes casos de teste:

* Adicionar o recurso "menu2" como favorito do usuário "Jacob"
* Obter os favoritos do usuário "Jacob" , irá retornar "menu2"
* Remover os favoritos do usuário "Jacob"

## Adicionar o recurso "menu2" como favorito do usuário "Jacob"

falseadd\_favorites\_to\_userPasso 1

* Navegue para Favorites → Add Favorites to User → POST e clique em Request 1.

Passo 2

* Insira o userId e o ID do recurso "menu2" como favorito.

Passo 3

* Clique no botão Send request, espere pelo resultado e verifique o mesmo.

## Obter os favoritos do usuário "Jacob", irá retornar "menu2"

falseget\_user\_favoritesPasso 1

* Navegue para Favorites → Get user's Favorites → GET e clique em Request 1.

Passo 2

* Insira o userId.

Passo 3

* Clique no botão Send request, espere pelo resultado e verifique o mesmo.

## Remover os favoritos do usuário "Jacob"

falsedelete\_user\_favoritesPasso 1

* Navegue para Favorites → Delete user's Favorites → DELETE e clique em Request 1.

Passo 2

* Insira o userId.

Passo 3

* Clique no botão Send request, espere o resultado e verifique o mesmo. Nenhum dado de favoritos irá aparecer.

 ]]>
