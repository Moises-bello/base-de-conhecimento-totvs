---
content_hash: 7c388374c11223544b6e1c2593f936f0e7687544f25cc57eba0845699bb6f1c9
fetched_at: '2026-06-29T00:11:38.778625+00:00'
page_id: '784778874'
product: rm
source: tdn-rm
title: Conectores
type: documentation
url: https://tdn.totvs.com/display/LRM/Conectores
version: 28
---

## **CONTEÚDO**

## **01. VISÃO GERAL**

       Esta é uma funcionalidade de **criação, exclusão, edição e listagem** dos **conectores** que estarão disponíveis para a utilização do **Repositório de Arquivos**.

       Os **Conectores** podem ser contextualizados ou globais, condição essa que pode ser definida no Switch **Visível em todas coligadas**. Portanto uma coligada somente tem acesso aos seus registros ou aos registros que são globais.

       Da mesma forma, os **Conectores** podem ser contextualizados por sistema ou podem ser multi-sistema, condição essa que pode ser definida no Switch **Visível em todos módulos**.

## **02. EXEMPLO DE UTILIZAÇÃO**

   É possível acessar a tela de Gerenciamento de Conectores:

* Pelo menu: Serviços Globais > Administração > Repositório de Arquivos > Conectores;

### **LISTAGEM**

#### **Filtros de Pesquisa**

A interface de listagem oferece filtros simples e avançados, seguindo o padrão OData, para facilitar a busca de conectores.

#### **Visibilidade por Coligada**

A opção "Visível a todas coligadas" permite filtrar os resultados com base na coligada de contexto ou mostrar conectores disponíveis globalmente.

#### **Visibilidade por Módulo**

O uso do "Switch Visível a todos módulos" permite filtrar os resultados para exibir apenas os conectores associados ao módulo atual ou, alternativamente, mostrar todos os conectores que são multi-módulos ou multi-sistemas.

---

### **CADASTRO**

#### **Definindo a Coligada e o Módulo**

* A coligada associada ao conector é definida pela opção "**Visível a todas coligadas**". Você pode escolher entre a coligada do contexto atual ou torná-la global.
* O módulo do conector pode ser especificado através da opção "Módulo". Se você preferir criar um conector que seja multi-módulo, utilize a opção "**Visível a todos módulos**".

#### **Campos Obrigatórios e Opções Padrão**

* Os campos "**Nome**", "**Tipo**" e "**Credenciais**" são obrigatórios para o cadastro.
* Por padrão, as opções "**Status**", "**Visível a todas coligadas**" e "**Visível a todos módulos**" estão ativadas.
* As opções "**Código**" e "**Módulo**" vêm desabilitadas por padrão.

#### **Escolhas Excludentes**

* Note que as opções "**Módulo**" e "**Visível a todos módulos**" são excludentes. Você deve escolher entre especificar um único módulo ou tornar o conector multi-módulo.

#### **Tipo do Conector**

A partir da versão 12.1.2506 foi disponibilizado o Conector **One** **Drive for Business.**

Na seção "Credenciais do Conector", faça o upload do arquivo de credenciais disponibilizada pelo fornecedor, conforme o tipo de conector escolhido.

Orientações para obter as credenciais do Google Drive: [Como criar credenciais Utilizando Oauth](https://tdn.totvs.com.br/display/LRM/Como+criar+credenciais+Utilizando+Oauth)

Como obter as credenciais do One Drive for Business: <https://tdn.totvs.com/x/tWdpO>

---

### **EDIÇÃO**

#### **Alterando Coligada e Módulo**

* A coligada associada ao conector pode ser alterada utilizando a opção "**Visível a todas coligadas**".
* Da mesma forma, o módulo associado pode ser atualizado por meio da opção "**Módulo**" ou "**Visível a todos módulos**", dependendo se o conector é específico para um módulo ou multi-módulo.

#### **Atualização de Credenciais**

* As credenciais podem ser atualizadas, desde que pertençam ao mesmo projeto e usuário na Google API.

---

### **EXCLUSÃO**

#### **Arquivos associados**

 O conector só poderá ser excluído caso não possua arquivos associados a ele. Certifique-se de que todos os arquivos foram removidos antes de prosseguir com a exclusão.

---

## **03.****ERROS COMUNS**

### Credenciais fornecidas são inválidas

Este erro ocorre quando você tenta atualizar o arquivo de credenciais com informações que não correspondem ao conector selecionado. É importante notar que a atualização deve ser feita apenas se as credenciais forem referentes ao mesmo projeto e usuário da Google API.

### Anexar um arquivo inválido

Este erro ocorre quando o arquivo anexado não é compatível, o que pode acontecer se o arquivo não for uma credencial valida e do tipo de conector correto. Certifique-se de que o arquivo esteja no formato correto e não esteja corrompido.

### **Tentativa de Exclusão de Conector com Arquivos Associados**

Este erro ocorre quando você tenta excluir um conector que ainda possui arquivos associados. Para evitar essa situação, certifique-se de remover todos os arquivos relacionados antes de prosseguir com a exclusão.

## **04.** **DICIONÁRIO DE TERMINOLOGIAS**

**Código****:** Representa o código do conector.

**Nome:** Nome que irá representar o conector.

       **Tipo:** Qual o repositório de arquivos que será realizada o vinculo para o armazenamento dos arquivos

       **Descrição:** Texto descritivo que representa o objetivo, a finalidade do conector de forma mais amigável e legível ao usuário.

**Visível a todas coligadas****:** É um Switch que representa a condição boleana se deve ser respeitado o id da coligada informada no contexto ou global (0).

**Visível a todos módulos****:** É um Switch que representa a condição boleana se deve ser respeitado o código do módulo definido no Select **Módulo** ou se multi-módulo / multi-sistema.

**Módulo:** É um Select como todos os módulos disponíveis do ERP.

**Status:** É um Switch que indica o estado atual do conector, se está **Ativado** ou **Desativado**

**Credencial:** É um campo upload, onde as **credenciais de acesso ao Repositório de Arquivos**, devem ser **importadas**, para a devida conexão ser realizada

false

**Versão:** 12.01.2310 ou superior
