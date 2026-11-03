---
content_hash: 83a900cb6fa106b83c6ad92e6a3963789c81667801b73fc32429a7e92d23eb03
fetched_at: '2026-06-28T21:35:25.052969+00:00'
page_id: '273980175'
product: fluig
source: tdn-fluig
title: Identity | Empresa
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Empresa
version: 35
---

# Falando de empresa...

---

O perfil da empresa reúne as principais informações relacionadas à empresa no TOTVS Identity e permite a edição de determinados campos.

## Editar perfil da empresa

---

**01.** Acionar o ícone  **Configurações**  no canto superior direito.

**02.** Selecionar a opção **Empresa**.

**03.** Acionar o ícone .

**04.** Substituir ou preencher os campos que permitem edição.

#f2f2f2#f2f2f2

**Telefone**Informar o telefone da empresa.

**Fax**Informar o número de fax da empresa.

**E-mail Oficial** (Obrigatório)  
Informar o e-mail oficial de contato da empresa.

**Site**Informar o site oficial da empresa.

**Endereço**Informar o endereço da empresa.

**País**Informar o país em que a empresa está localizada.

**Estado/Região**Informar o estado ou região em que a empresa está localizada.

**Cidade**Informar a cidade em que a empresa está localizada.

**CEP**Informar o CEP do endereço da empresa.

**05.** Acionar **Atualizar** para salvar as alterações.

## Consultar campos que não podem ser editados

---

Os campos abaixo devem ser preenchidos no momento de criação da empresa e não podem ser editados.

#f2f2f2#f2f2f2

**Nome da empresa** (Obrigatório)  
Informar o nome da empresa. Esta informação será exibida no topo do  da empresa após o usuário sair da sessão e acessar novamente o Identity.

**Empresa Parceira**Indica se a empresa em questão é uma parceira.

**Empresa Desenvolvedora**  
Indica se a empresa em questão é uma desenvolvedora.

**Subdomínio da Empresa**O subdomínio é o endereço de acesso da empresa no Identity.

**Código da Empresa**O código é definido durante a criação da empresa.

**Modelo**O único modelo disponível é SaaS.

]]>

## Customização da Seleção de Empresa

---

Para facilitar a identificação do ambiente correto (como Produção, Homologação ou Desenvolvimento), é possível configurar os campos **environmentType** e **environmentName**, permitindo que usuários com acesso a múltiplas empresas visualizem essas informações diretamente na lista de seleção da tela de login.

### 1. Atualização dos Dados da Empresa (via API)

Nota:

Atualmente, a alteração dessas informações não está disponível na interface administrativa (UI), devendo ser realizada via **Swagger**.

**Passo 1:** Autenticar-se no Swagger através do endpoint de [Token](https://app.fluigidentity.com/api/auth/doc/#!/IDM_Auth_Api_-_V1/token).

**Passo 2:** Utilizar o método `PATCH` no endpoint [/api/core/v1/companies/{id}](https://app.fluigidentity.com/api/core/doc/#!/Company_Service/patch_1).

**Payload (JSON Patch):** Para atualizar o tipo e o nome do ambiente, envie o seguinte array no corpo da requisição:

JSON

### 2. Requisitos para Visualização

Para validar se as informações estão sendo exibidas corretamente na tela de login:

1. **Usuário Multi-empresa:** O usuário deve estar associado a pelo menos duas empresas.
2. **Sem Empresa Favorita:** O usuário não deve ter uma "empresa padrão" selecionada, forçando o sistema a abrir a tela de escolha.
3. **Listagem:** O endpoint de listagem de empresas consumido pela tela de login deve retornar os novos campos preenchidos.

### 3. Fluxo de Autenticação e Consulta

O processo técnico segue a ordem abaixo:

* **Token:** Obtenha o token de acesso em [/api/auth/doc/v1/token](https://app.fluigidentity.com/api/auth/doc/#!/IDM_Auth_Api_-_V1/token).
* **Consulta:** Verifique o retorno das empresas em [/listAllCompaniesOfUserForLogin](https://app.fluigidentity.com/api/auth/doc/#!/IDM_Auth_Api_-_V1/listAllCompaniesOfUserForLogin).

**Resultado:** Após a configuração, o nome definido em `environmentName` será exibido abaixo da URL da empresa na lista de seleção.
