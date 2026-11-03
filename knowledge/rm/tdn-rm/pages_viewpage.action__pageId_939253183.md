---
content_hash: 0e1835e6232cf12ddab869abe981c3ea498bda0faabd27ffd281be6b8f64fb7c
fetched_at: '2026-06-29T00:12:09.131476+00:00'
page_id: '939253183'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - Importação/Exportação do cadastro de empréstimo
  e histórico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=939253183
version: 4
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Importação/Exportação do cadastro de empréstimo e histórico |
| País: | Brasil |
| Issue: | [DRHCALCRM-8103](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-8103) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.270
* 12.1.2410.223
* 12.1.2502.139
* 12.1.2506 e superiores

## **03. SITUAÇÃO/REQUISITO**

A primeira modificação ocorreu ao selecionar o funcionário que se deseja registrar o empréstimo, seguindo o caminho Anexos | Folha de Pagamento | Empréstimos , ao criar ou editar um empréstimo, foram adicionados os campos Comp. Final Desc. (com Mês e Ano), Valor da Parcela, Percentual  e o checkbox "Aplicar percentual abaixo sobre remuneração líquida para o limite do desconto" (que, quando marcado, habilita o já citado checkbox Percentual). Os campos adicionados só se tornam editáveis com a opção da modalidade Crédito do Trabalhador eSocial selecionada no campo Modalidade do empréstimo (conforme destaques em vermelho abaixo).

 

A segunda modificação ocorreu após a edição do empréstimo selecionado, utilizando o caminho Anexos | Descontos de Empréstimo, onde foi incluído o campo "Insuficiência de Saldo empréstimo crédito ao trabalhador". Assim como os outros campos incluídos, este também só será habilitado quando a opção da modalidade Crédito do Trabalhador eSocial estiver selecionada no campo Modalidade do empréstimo (conforme destaques em vermelho abaixo).

## **04.****ASSUNTOS RELACIONADOS**

**Menus / Processos**

[Importação de Empréstimo Consignado](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677&draft=true)

[Empréstimos Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=452719572)

**Documentações**

[Leiaute S-1.3 e Nota Técnica 01/2024](https://tdn.totvs.com/pages/viewpage.action?pageId=862114556)

[Governo cria o Crédito do Trabalhador, linha com juros mais baixos](https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2025/03/governo-cria-o-credito-do-trabalhador-linha-com-juros-mais-baixos)

[Crédito do Trabalhador - Nova modalidade de consignado](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-nova-modalidade-de-consignado/)

[Crédito do Trabalhador – Cronograma de Desconto da 1° parcela](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-cronograma-de-desconto-da-1-parcela/) 

[Crédito do Trabalhador – MTE Publica Novas Regras para Descontos Consignados em Folha de Pagamento](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-mte-publica-novas-regras-para-descontos-consignados-em-folha-de-pagamento/)  
  
[Crédito Consignado – Requisitos para operacionalização dos sistemas e plataformas digitais](https://www.totvs.com/blog/fiscal-clientes/credito-consignado-requisitos-para-operacionalizacao-dos-sistemas-e-plataformas-digitais/)

[Crédito do Trabalhador – Definição de Regras para Habilitação de Instituições Financeiras](https://www.totvs.com/blog/fiscal-clientes/credito-do-trabalhador-definicao-de-regras-para-habilitacao-de-instituicoes-financeiras/)

[Perguntas Frequentes do Crédito do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/perguntas-frequentes/perguntas-frequentes/)
