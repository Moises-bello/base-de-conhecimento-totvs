---
content_hash: 0896752e8051e4daf8acd5807a6210bb675702465aafd3414d8c8700a7f32044
fetched_at: '2026-06-29T00:11:40.005209+00:00'
page_id: '793806080'
product: rm
source: tdn-rm
title: Execução dos Processos de Ressuprimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=793806080
version: 20
---

## **01. VISÃO GERAL**

Realizar a parametrização para execução dos processos de ressuprimento, BackOffice → Gestão de Estoque, Compras e Faturamento → Ambiente → Configuração → Parâmetros → Gestão de Estoque, Compras e Faturamento → Gestão de Estoque

A parametrização consiste em:

1. Definir se vai utilizar o módulo de ressuprimento
2. Qual o nível de gestão.

* O nível de gestão vai influenciar no processo de ressuprimento, nas seleções de coligadas, filiais, locais de estoque.

* Quando estiver utilizando o módulo de ressuprimento vai ser obrigatório escolher um nível de gestão diferente de "não utiliza"



## **02. FORMA DE****CÁLCULO**

### Seleção de Coligadas

Os processos de ressuprimento exibem as opções para serem executados por multicoligadas, para exibir o filtro de seleção das coligadas devem:

* Existir mais de uma coligada ativa cadastrada na base e parametrizada para utilizar os processos de ressuprimento;
* O usuário ter a permissão de executar os processos de ressuprimento em mais de uma coligada;

### Seleção de Filiais

As Filiais são exibidas conforme as coligadas selecionadas

* Serão exibidas apenas as filiais que possuem suas coligadas parametrizadas para utilizar os processos de ressuprimento por nível de gestão Por Filial ou Por Local.

### Seleção de Locais de Estoque

Os Locais de Estoque são exibidos conforme as filiais selecionadas

* Serão exibidas apenas os locais de estoque que possuem suas coligadas parametrizadas para utilizar os processos de ressuprimento por nível de gestão Por Local.

## **03. CÁCULO DE CONSUMO / CLASSE ABC / ATRIBUTOS**

Seleção dos cálculos

## **04. CÁCULO DE ATRIBUTOS**

Se a opção de cálculo de tributos for selecionadas na tela anterior, será exibida a tela abaixo para seleção dos produtos

* Serão exibidas apenas os produtos que possuem as coligadas parametrizadas para utilizar os processos de ressuprimento.

A partir da versão/patch **12.1.2310.108**, os processos de ressuprimentos poderão ser configurados para utilizar o fracionamento de jobs, utilizando a classe à seguir:

* EstProcessarRessuprimentoData

Os processos de ressuprimento poderão ser executados com ou sem fracionamentos de jobs. 

Para informações detalhadas sobre o fracionamento de jobs, consultar a documentação [Configuração de fracionamento de jobs.](https://tdn.totvs.com/x/lpR-I)
