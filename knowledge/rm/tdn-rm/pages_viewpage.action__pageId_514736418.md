---
content_hash: 2f606fe647ac2340bfc84e03f8fb10d746f850cbf364bcfcb286d78bb292e9b7
fetched_at: '2026-06-29T00:10:26.773522+00:00'
page_id: '514736418'
product: rm
source: tdn-rm
title: Encerramento de Contas sem Débitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514736418
version: 13
---

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Parâmetros**

itensVisão Geral

## **01. VISÃO GERAL**

Nessa funcionalidade, é possível **encerrar em lote diversas parciais** que se enquadram nas seguintes situações:

1. 1. Parciais que **não possuem nenhum débito** associado.
   2. Parciais de **retorno** que **não devem ser cobradas** para o convênio.

Essa rotina foi projetada para agilizar o processo, permitindo o encerramento simultâneo de múltiplas contas que atendam a esses critérios.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

No menu do **Faturamento**, acesse a rotina de **Encerramento de Contas sem Débitos**.

Abaixo estão descritas as duas formas de realizar o encerramento de contas sem débitos:

#### **1. Seleção manual das parciais através da tela de visão**

* + Monte um filtro para pesquisar as parciais que serão carregadas na grid.
  + **Observação:** Somente parciais com status de **Elaboração,** que  **estejam com a data final preenchida** e que **não possuam débitos** serão exibidas na grid.
  + Marque as contas que deseja encerrar e execute o processo **Encerramento de Conta Sem Débito**.
  + Aguarde a conclusão do processo.
  + Após o processamento, as parciais serão marcadas como **Faturadas**.

#### **2. Encerramento de Contas com status de Retorno**

* + Ao selecionar essa opção, o sistema **ignorará** as parciais selecionadas na grid (caso existam) e pesquisará automaticamente as parciais com **status de Retorno**.
  + O sistema realizará o encerramento dessas parciais, marcando-as como **Faturadas**.

Configurações necessárias para o sistema considerar uma conta como retorno

## **03.** **Configurações necessárias para o sistema considerar uma conta como retorno**

Para que o sistema identifique e trate uma conta como **retorno**, os seguintes parâmetros devem ser configurados:

---

#### **1. Parâmetros Gerais**

* + Acesse: **Opções > Parâmetros > Parâmetros Gerais > Registro e controle II**.
  + Marque a opção: **“Utiliza Atividade Retorno Automático”**.

---

#### **2. Condições Contratuais com Convênio**

* + Acesse: **Cadastros > Faturamento > Condições contratuais com convênio > Aba parâmetros 1**.
  + Marque a opção: **“Considerar como retorno apenas o primeiro atendimento”**.

---

#### **3. Anexos - Retorno de Consulta**

* + Acesse: **Anexos > Retorno de consulta**.
  + Adicione um novo item, selecionando:

    - **Plano**
    - **Especialidade**
    - **Retorno XXX em dias** (onde "XXX" representa o prazo em dias para o retorno).

---

#### **4. Lançamento Automático no Registro de Atendimento**

* + Acesse: **Cadastro > Faturamento > Lançamento automático no registro de atendimento**.
  + **Exclua** o registro para atendimento externo, se aplicável.
