---
content_hash: 59446d1c766224f8adc1749af90eda1ca6407eb4fb938741a806484d1c3844f0
fetched_at: '2026-06-29T00:11:11.739543+00:00'
page_id: '648442103'
product: rm
source: tdn-rm
title: Folha de Pagamento de Prestadores1
type: documentation
url: https://tdn.totvs.com/display/LRM/Folha+de+Pagamento+de+Prestadores1
version: 24
---

**ÍNDICE**

1. **Visão Geral**
2. **Exemplo de Utilização**
3. **Relatório**
4. **Processo do Repasse**

sumarioVisão Geral

## **01. VISÃO GERAL**

Esta rotina tem como objetivo listar os repasses gerados com base nos lançamentos realizados na parcial do paciente.

O sistema calcula automaticamente o valor do repasse no momento do lançamento do item na conta médica, seguindo os critérios de repasse definidos pela instituição.

Na funcionalidade, é possível filtrar os repasses por prestador, período de apuração e outros filtros disponíveis. Além disso, permite liberar os repasses para pagamento ou cancelar sua liberação, conforme necessário

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

**Para liberar os créditos/débitos e descontos:**

* Selecione os registros a serem liberados
* Execute o processo "Libera repasse"
* Selecione a data de previsão de pagamento

**Para cancelar a liberação:**

* Selecione os registros liberados
* Execute o processa Cancelar Liberação

**Para Dividir o repasse:**

* O processo de divisão de repasse estará disponível somente para as seguintes situações:
  + Lançamentos de repasses de diárias
  + Lançamentos de repasses de taxas e serviços
  + Lançamentos de repasses de MATMED
  + Lançamentos de repasses de gastos particulares
  + Lançamentos de repasses oriundos de redirecionamento de honorário
  + Lançamentos de repasses oriundos de redirecionamento de exames
* Selecione o repasse desejado e clique no processo "Divisão de repasse"
* O valor do lançamento será exibido e deverá incluir os prestadores que receberão o repasse
* Informe o valor ou percentual para cada prestador
* Caso tenha incluído algum prestador ou valor errado, deve-se excluir e executar o processo.
* Ao final do processo, os valores informações aparecerão para cada prestador selecionado
* Caso deseje visualizar para quem a divisão foi feita, base selecionar a linha e clicar no processo, que os prestadores serão exibidos juntamente com os valores

**Para Redirecionar o repasse para outro prestador:**

* O processo estará disponível para as seguintes situações:
  + Lançamentos de honorários
  + Lançamentos de exames

Relatórios

## **03. RELATÓRIOS**

Para realizar a impressão da folha de pagamento, baixar no TOTVS Compartilhamento o arquivo "**SAUREL0042 - Folha de pagamento de prestadores**" e configurar o mesmo através da tela de Parâmetros Gerais, acessada através do menu **Ambiente> Parâmetros> Gestão Hospitalar> Relatórios**  
Relatórios via Gerador, no campo Folha de Pagamento.

Folha de pagamento de Prestadores

Para realizar a impressão dos repasses liberados para pagamento, baixar no TOTVS Compartilhamento o arquivo "**SAUREL0123 - Prestadores com lançamentos liberados para pagamento**" e configurar o mesmo através da tela de Parâmetros de Integração RM Nucleus, acessada através do menu **Ambiente> Parâmetros> Gestão Hospitalar****> Integrações > Integração Backoffice**, na aba Gerais 2/5, no campo Relatório de repasses liberados para pagamento.

Repasses liberados para pagamento.

Será apresentada a mensagem abaixo e caso responda Sim, o relatório será gerado somente com os repasses liberados para o prestador selecionado.

Caso responda Não, serão listados os repasses liberados de todos os prestadores. Sendo agrupado por prestador.

Processo do Repasse

## **04. PROCESSO DO REPASSE**

Faturamento \Folha de Pagamento de Prestadores

**Filtros**

**A tela já abre em modo de edição:**

**Liberando o repasse**

**Repasse Liberado**

**Gerar Folha de Pagamento**

**Pagamento**

**Cancelando a folha**

**Integração com BackOffice**

## **05.** **TABELAS UTILIZADAS**

* SZCONTROLREPASSE
