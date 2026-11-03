---
content_hash: ca1e94a6c5ce681f97edfce3cf7587d7ee875a1b44e98ba441f58e1a33b966c2
fetched_at: '2026-06-29T00:10:20.197218+00:00'
page_id: '489766168'
product: rm
source: tdn-rm
title: Pagamento com Cartão de Crédito/Débito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=489766168
version: 29
---

## 

## **ÍNDICE**

1. **Visão Geral**
2. **Parametrização**
3. **Exemplo de utilização**

## **01. VISÃO GERAL**

No Processo Seletivo é possível realizar o pagamento da inscrição através dos seguintes modelos de transação para cartões de crédito e/ou débito:

* BuyPage
* Checkout
* GetNet
* [TOTVS Pagamento Cartão - TPC](https://tdn.totvs.com/x/jAhOI).

Para maiores detalhes sobre a parametrização de cada modelo, favor acessar a documentação do [TOTVS Gestão Financeira](http://tdn.totvs.com/pages/releaseview.action?pageId=421388865).

**GetNet:**O modelo de transação GetNet está disponível no Processo Seletivo a partir da versão 12.1.25

**EduConnect Pay:**O modelo de transação eduCONNECT Pay está disponível no Processo Seletivo a partir da versão 12.1.27.204 ( [clique aqui](https://tdn.totvs.com/display/LRM/eduCONNECT+Pay) para conhecer mais ).

Pagamento para Venda Online de Cursos

* Os candidatos que forem realizar o pagamento a partir de processo seletivo que utiliza Venda Online de Cursos, deve obrigatoriamente possuir um usuário de acesso ao portal. Portanto, a parametrização de Geração de Usuário automática, deve estar habilitada, para que o pagamento seja realizado com sucesso.

   Para mais informações sobre a geração de usuários, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001043088-RM-EDU-Parametriza%C3%A7%C3%A3o-para-gerar-usu%C3%A1rio-automaticamente-).

* A partir da versão **12.1.31.192**foi desenvolvida uma melhoria para os casos em que o Plano de Pagamento que tenha duas ou mais parcelas com datas de vencimento diferentes, como no exemplo abaixo:

Nestes casos, o sistema irá identificar e exibir  na opção de "**Pagamento**" na Central do Candidato a parcela cujo o vencimento está mais próximo da data em que está sendo feita a inscrição.

No exemplo acima, será exibida a parcela de vencimento na data "12/07/2021".

## **02. PARAMETRIZAÇÃO**

Para habilitar o pagamento com cartão basta acessar o cadastro do processo seletivo e marcar o parâmetro ""Disponibilizar pagamento com cartão no portal".

* **TOTVS Educacional Processo Seletivo | Cadastros | Processo seletivo / venda online de Cursos | aba Informações Financeiras**

Importante

O parâmetro "Não habilitar opções de pagamento para boleto vencido" faz com que os métodos de pagamento parametrizados(Boleto, Cartão, Pix) não estejam disponíveis na central do candidato caso o boleto esteja vencido. **Disponível a partir da versão 12.1.2209.114.**

Ao acessar a central do candidato no portal de inscrições, um candidato que possua lançamento gerado poderá visualizar um botão para pagamento via Cartão de Crédito.

O parâmetro Configurações por Filial definido no TOTVS Financeira sempre irá validar a filial informada no cadastro do Processo Seletivo.

No processo seletivo campo onde será definido a Filial.

## **03. EXEMPLO DE UTILIZAÇÃO**

Caso o processo seletivo esteja parametrizado para utilizar o modelo de transação GetNet, ao clicar no botão "Cartão de Crédito", na tela de confirmação de inscrição ou na central do candidato, ele será redirecionado à GetNet para realizar o pagamento.

###### Tela GETNET:

**Tela CyberSource:**

Tela checkout TOTVS Pagamento Cartão a partir da versão 12.1.2410

* Validar configurações do Rewrite e ARR .
]]>
