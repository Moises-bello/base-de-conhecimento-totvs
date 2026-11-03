---
content_hash: c048005fc5be5bf40a466013a1b66e55963c629f14ef054db19079e1a7f44c30
fetched_at: '2026-06-29T00:11:39.993085+00:00'
page_id: '793207583'
product: rm
source: tdn-rm
title: Tabelas Dinâmicas (Smart-UI)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=793207583
version: 10
---

### **01. VISÃO GERAL**

Por este cadastro você poderá **criar tabelas dinamicamente**. As tabelas poderão ter **finalidades diferentes** para as quais elas foram criadas e outras o próprio usuário poderá definir, além disso, é possível **cadastrar itens de tabelas dinâmicas**, que serão os campos da tabela. 

Veja como funcionam alguns campos:

* **Visível a todas coligadas:** Marque esta opção para que a tabela dinâmica fique disponível para todas as coligadas.
* **Finalidade**: Informe a finalidade do item da tabela. As tabelas dinâmicas poderão ter as finalidades:
  + **Código "0" – Diversos Usos internos**: Uso interno do sistema. Não é possível selecioná-la.
  + **Código "1" - Código de Serviços Bancários**: Tabelas de serviços bancários.
  + **Código "2" - Validações de Campos Complementares**: Cada tabela pode possuir quantos itens forem necessários.
  + **Código "3" – Uso Interno (permite incluir itens)**: Código de uso interno do sistema. Você não pode selecioná-lo, mas poderá incluir itens de tabela dinâmica

### **02. EXEMPLO DE UTILIZAÇÃO**

   É possível acessar a tela de Gerenciamento de Conectores:

* Pelo menu: Serviços Globais > Administração > Tabelas Dinâmicas > Tabelas Dinâmicas (Novo);

#### **LISTAGEM**

##### **Filtros de Pesquisa**

A interface de listagem oferece filtros simples e avançados, seguindo o padrão OData, para facilitar a busca de tabelas dinâmicas.

##### **Visibilidade por Coligada**

A opção "Visível a todas coligadas" permite filtrar os resultados com base na coligada de contexto ou mostrar conectores disponíveis globalmente.

##### **Contextualização por módulo**

Temos a opção de contextualizar por módulo, as tabelas dinâmicas, após escolher o módulo, todas as telas, todas as interações com as apis irão ser contextualizadas pelo módulo escolhido.

---

#### **CADASTRO**

##### **Definindo a Coligada**

* A coligada associada a tabela dinâmica é definida pela opção "**Visível a todas coligadas**". Você pode escolher entre a coligada do contexto atual ou torná-la global.

##### **Campos Obrigatórios e Opções Padrão**

* Os campos "**Código**" e "**Finalidade**" são obrigatórios para o cadastro.
* Por padrão, as opções "**Finalidade**", **"Descrição"** e "**Visível a todas coligadas**" estão ativadas.
* A opção "**Código**" vêm desabilitada por padrão.
* Ao editar o cadastro as opções **"Código"**, **"Finalidade"** e **"Visível a todas as coligadas"** vêm desabilitados por padrão.

---

#### **EDIÇÃO**

##### **Alterando Descrição**

* O único campo disponível a ser atualizado é a **"Descrição"**.

---

#### **EXCLUSÃO**

Apenas tabelas dinâmicas de finalidade **"Validações de Campos Complementares"** poderão ser excluidas.

---

### **03.** **ITENS DE UMA TABELA DINÂMICA**

##### Jornada de criação de itens de tabela dinâmica

Uma tabela dinâmica é composta de ítens cadastrados dinâmicamente e que fazem sentido para o negócio, podem vir de forma nativa, cadastrado pelos times do RM, como também podem ser cadastrados pelo produto conforme a necessidade.

### **04.** **DICIONÁRIO DE TERMINOLOGIAS**

**Código****:** Representa o código da tabela dinâmica ou do item da tabela dinâmica.

       **Finalidade:** Qual a finalidade de uso da tabela dinâmica, se ele é para uso interno ou se é público e pode ser cadastrado pelo cliente.

       **Descrição:** Texto descritivo que representa o objetivo da tabela dinâmica ou do item de tabela dinâmica de forma mais amigável e legível ao usuário.

**Visível a todas coligadas****:** É um Switch que representa a condição boleana se deve ser respeitado o id da coligada informada no contexto ou global (0).

false

**Versão:** 12.01.2310 ou superior
