---
content_hash: 763243d036e2e7684072a23f902a6fad33642937a101a8bee7e4f4cea4d2e300
fetched_at: '2026-06-29T00:12:01.655584+00:00'
page_id: '897302545'
product: rm
source: tdn-rm
title: Registro Preliminar - SmartUI
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+Preliminar+-+SmartUI
version: 9
---

false

**A partir das Versões:**

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O cadastro de Registro Preliminar irá permitir que o usuário do departamento pessoal possua um cadastro para informar dados básicos de um funcionário que será admitido, utilizando um registro de pessoa existente. A nova tela utiliza a tecnologia do **Smart UI**. Esta nova tela receberá uma evolução visual e em partes funcional, da tela  Registro preliminar anterior.

Na inclusão de um Registro Preliminar, estarão disponíveis os campos:

* Pessoa
* Data de Admissão (Prevista)
* CPF da Pessoa (Esse campo é para conferência dos dados da Pessoa, **não é possível modificá-lo**)

No campo **Pessoa**, o usuário deverá buscar uma pessoa já existente na base de dados.

Quando há integração com o TOTVS Folha de Pagamento e o TOTVS Gestão de Pessoas, e existe a obrigatoriedade de requisição para admissão, ao incluir um funcionário, é exibida a tela de **Pré-cadastro**, que realiza a busca por todas as pessoas associadas a uma requisição. Nessa mesma tela, há o ícone **"Exibir somente pessoas com registro preliminar"**, que filtra as pessoas que já possuem cadastro no **Registro Preliminar**.

No caso de não haver integração com oTOTVS Folha de Pagamento e o TOTVS Gestão de Pessoas, e sem a utilização de requisição para admissão, ao incluir um novo funcionário, existe um ícone dentro do cadastro que permite localizar uma pessoa já cadastrada na base de dados e que também possui um **Registro Preliminar**.

Os campos do Registro Preliminar são de preenchimento obrigatório.

As informações contidas nesse cadastro serão utilizadas pelo eSocial e enviadas através do evento S-2190 -Admissão de Trabalhador-Registro Preliminar. Para incluir um novo registro de Pessoa no sistema para uso no Registro Preliminar, é necessário que o usuário tenha a permissão de **"Incluir Pessoa"** no sistema TOTVS Gestão de Pessoas.

## **02. EXEMPLO DE UTILIZAÇÃO**

Disponibilizamos a tela do **Registro Preliminar** utilizando a tecnologia **Smart UI** para as versões **12.1.2502** e superiores. Essa implementação trouxe uma atualização visual para a página, aprimorando não apenas sua aparência, mas também a forma como ela é utilizada, proporcionando uma experiência mais moderna e eficiente.

Veja a nova tela:

Agora, é possível buscar registros diretamente na tela sem a necessidade de criar um filtro específico. Por exemplo, ao visualizar uma lista de registros, caso queira retornar apenas o Registro Preliminar com o nome "teste preliminar", basta preencher o campo **Buscar na tabela**.

**Importante:** Vale lembrar que essa funcionalidade realiza a busca em qualquer campo exibido na tela, **somente os registros exibidos**, por padrão a tabela exibe 10 registros por busca, mas esse valor pode ser alterado, exibindo 20 / 50 / 100 / 1000 registros .

Outra funcionalidade que passou por alterações visuais e funcionais foi o gerenciamento e a aplicação de **Filtros**. Anteriormente, ao clicar em **Filtro**, era aberta uma janela pop-up para criar ou utilizar filtros existentes. Agora, ao clicar em **Filtro**, uma janela lateral será exibida, permitindo o gerenciamento de filtros de forma mais prática.

Nessa nova interface, estão disponíveis filtros padrão, como "Id Reg. Preliminar, Código Pessoa, CPF", além da possibilidade de criar filtros personalizados. Para isso, basta clicar eme, em seguida, clicar em

Para concluir a criação do Filtro, basta clicar então em **Salvar e Filtrar**

Para a inclusão de um novo registro basta clicar em

Para a Edição de um registro basta clicar no registro desejado e clicar em

Após alterar os dados necessários clique em

Caso queira **Excluir** o registro, é necessário selecionar a linha desejada e clicar em , após a confirmação o registro será excluído:

Na tela inicial do **Registro Preliminar**, é possível ajustar as colunas do grid, permitindo fixá-las, alterar sua posição de exibição ou optar por não exibi-las. Além disso, também é possível definir a quantidade de registros a serem exibidos. Todas essas configurações podem ser realizadas através da função **Configurar Grid**.

## **03. TABELAS UTILIZADAS**

* PFUNCPRELIMINAR

---
