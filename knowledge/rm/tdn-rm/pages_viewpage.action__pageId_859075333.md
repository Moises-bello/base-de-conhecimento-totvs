---
content_hash: e8a1ec0eb42dc865fc41335fc630e3b2211192823b8d9f618a4744b84dc55195
fetched_at: '2026-06-29T00:11:54.936342+00:00'
page_id: '859075333'
product: rm
source: tdn-rm
title: Habilitar Integração TOTVS RH Orçamentos com TOTVS Gestão de Pessoas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=859075333
version: 10
---

## **01. PARAMETRIZAÇÃO**

Quando a integração estiver habilitada, a aba "**Integração com TOTVS RH Orçamento**" ficará visível nas requisições e nos pareceres.

O campo "**Centro de Custos**" será exibido e será obrigatório nas requisições.

Os campos "**Item Contábil**" e "**Classe de Valor**" serão exibidos de acordo com as regras vigentes na folha de pagamento para esses campos no cadastro do funcionário.

## **01.01 TOTVS Gestão de Pessoas**

**Caminho para habilitar a integração no TOTVS Gestão de Pessoas**

Configurações | Parametrizador | TOTVS RH Orçamentos| Configurações da Integração com TOTVS RH Orçamentos

## **Permissões de Acesso**

Inserir no Fluxo com Exceção

## **01.02 TOTVS Folha de Pagamento**

**Visibilidade dos Campos "Item Contábil" e "Classe de Valor":**

Para que os campos "Item Contábil" e "Classe de Valor" estejam visíveis, é necessário habilitar o parâmetro "Usa integração outros backOffice" no sistema de Folha de Pagamento, acessível através do seguinte caminho:

* + **Configurações | Parametrizador | Integrações | Outros BackOffice**

**Habilitação dos Campos "Item Contábil" e "Classe de Valor":**

Para habilitar os campos "Item Contábil" e "Classe de Valor", é necessário configurar os seguintes parâmetros no sistema de Folha de Pagamento:

* + **No módulo Folha Normal:**
    - **Caminho:** Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Contabilização
    - **Parâmetros a serem habilitados:** "Item Contábil" e/ou "Classe de Valor"

* + **No módulo Lancto Financeiro:**
    - **Caminho:** Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Lancto Financeiro
    - **Parâmetros a serem habilitados:** "Item Contábil" e/ou "Classe de Valor"

## **02. REQUISIÇÕES CONTEMPLADAS**

* Aumento de Quadro
* Substituição
* Alteração de Dados Funcionais

**Avisos Importantes:**

* O parâmetro **"Habilitar Integração com TOTVS RH Orçamento"** não poderá ser manipulado enquanto houver registros de requisições na base de dados com os status "Suspensa" ou "Em andamento".
* Ao marcar o parâmetro **"Habilitar Integração com TOTVS RH Orçamento"**, habilitando essa integração, caso a base esteja parametrizada para trabalhar com o controle de lotação, automaticamente este controle nativo do TOTVS Gestão de Pessoas será inativado.
* Além disso, as requisições passarão a ter um novo Status ('Aguardando Aprovação Orçamento') que será aplicado antes da requisição entrar no fluxo de repasses.
* Para as requisições do tipo Substituição os campos não poderão ser alterados e os dados do centro de custos serão provenientes da seguinte origem:
  + Valor informado no **cadastro do funcionário**
  + Caso não exista no cenário anterior, verificado se há valor preenchido no **rateio fixo do funcionário**, considerando o **centro de custo com o maior percentual**.
  + Caso ainda não exista nos cenário anteriores, será verificado se há valor preenchido na **seção do funcionário**.
