---
content_hash: 6c02224f1f93905bc67ffa5a506440c8c97c1e6a13b49e9b77dd45f4100baa35
fetched_at: '2026-06-29T00:12:00.105303+00:00'
page_id: '880053638'
product: rm
source: tdn-rm
title: Guia do PIS/COFINS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=880053638
version: 19
---

Versão mínima

## **O quadro de PIS/COFINS está disponível somente a partir da versão 12.1.2406.**

# Conteúdo:

1Conteúdo:

# 1. Sobre

A Guia do PIS/COFINS oferece uma visão consolidada de toda a operação da empresa que sofreu incidência do PIS e da COFINS, tanto dos Lançamentos Fiscais, como de retenções realizadas através do módulo de Gestão Financeira.

Os dados necessários para a geração desta guia são provenientes dos Lançamentos Fiscais e dos Períodos de Apuração. São selecionados todos os Lançamentos Fiscais das Coligadas, Filiais e Período filtrados, que não estejam Cancelados ou Estornados. Serão considerados, também, Lançamentos Financeiros a pagar e a receber que tenham destaque da retenção do PIS, COFINS ou CSRF.

# 2. Requisito básico

A origem dos dados para geração da guia de PIS/COFINS é o Período de Apuração. Para que essas informações sejam preenchidas no Período de Apuração é preciso executar o .

Importante!

Caso haja Períodos de Apuração do PIS e/ou COFINS já encerrados, se for do seu interesse visualizar os dados desses Períodos, será preciso executar os seguintes passos:

1. Reabrir os Períodos de Apuração.
2. Executar o [Pré-Processamento da Apuração Fiscal](https://tdn.totvs.com/pages/viewpage.action?pageId=853282471).
3. Encerrar novamente os Períodos de Apuração.
4. E, por fim, regerar o [Processamento](https://tdn.totvs.com/pages/viewpage.action?pageId=934636030) do TOTVS Inteligência Tributária.

Caso existam lançamentos com tributos de PIS e/ou COFINS não processados, será exibida a mensagem abaixo indicando essas inconsistências na qual pode ser detalhada clicando em **Clique aqui para mais informações.**

O detalhe das inconsistências mostram a lista de períodos que contenham lançamentos com tributo de PIS/COFINS que não foram incluídos no  e o passo a passo para corrigir essa inconsistência

# 3. Quadros disponíveis na guia

CardsRetenções

* **Total do PIS:**

* + **Retido na Entrada:**Somatório dos valores de PIS retido calculados nos lançamentos financeiros **a pagar** de todas as Coligadas, Filiais e Períodos filtrados.
  + **Retido na Saída:**Somatório dos valores de PIS calculados nos lançamentos financeiros **a receber**, de todas as Coligadas, Filiais e Períodos filtrados.

* **Total do COFINS:**
  + **Retido na Entrada:**Somatório dos valores de COFINS retido calculados nos lançamentos financeiros **a pagar** de todas as Coligadas, Filiais e Períodos filtrados.
  + **Retido na Saída:**Somatório dos valores de COFINS calculados nos lançamentos financeiros **a receber**, de todas as Coligadas, Filiais e Períodos filtrados.

Quadros de valores

* **Valor Operacional**: Somatório do valor financeiro dos itens: (Valor da Mercadoria + Despesa + Seguro + Frete - Desconto) dos Lançamentos Fiscais de Entrada ou Saída.
* **Total do PIS:**

* + **Créditos:**Somatório dos Créditos de PIS calculados nos Períodos de Apuração Fiscal de todas as Coligadas, Filiais e Períodos filtrados que foram pré-processados.
  + **Débitos:**Somatório dos Débitos de PIS calculados nos Períodos de Apuração de todas as Coligadas, Filiais e Períodos filtrados que foram pré-processados.
* **Total do COFINS:**
  + **Créditos:**Somatório dos Créditos de COFINS calculados nos Períodos de Apuração Fiscal de todas as Coligadas, Filiais e Períodos filtrados que foram pré-processados.
  + **Débitos:**Somatório dos Débitos de COFINS calculados nos Períodos de Apuração de todas as Coligadas, Filiais e Períodos filtrados que foram pré-processados.

Gráfico de Apuração de PIS/COFINS

Este quadro representa, graficamente, o total dos créditos, dos débitos e o saldo do imposto a pagar ou o saldo credor por período de apuração. Os valores são apresentados somados, considerando os tributos PIS e COFINS.

A origem dos dados é o Período de Apuração. Se o mesmo estiver com Status aberto, o sistema faz uma simulação do encerramento e apresenta os valores parciais, considerando os lançamentos fiscais escriturados e processados pela Pré-Apuração até a data do processamento.

## 

Visão de débitos

Este grid apresenta o detalhamento de todas as operações selecionadas através do filtro aplicado agrupadas até o nível do CST, que geraram débito de PIS e COFINS.

A origem dos dados são os Itens do Lançamento Fiscal escriturados até o momento do processamento.

Origem dos valores na estrutura de dados

|  |  |  |
| --- | --- | --- |
| **Grupo** | **Campo** | **Origem (tabela/coluna)** |
| Débitos | Período (Data do Lançamento (E/S)) | DLAF.DATALF |
| Débitos | Coligada | DLAF.CODCOLIGADA |
| Débitos | Filial | DLAF.CODFILIAL |
| Débitos | Estado | DLAF.CODETD |
| Débitos | CST (Situação Tributária do ICMS) | DREGRAICMS.SITTRIBUTARIA |
| Débitos | CFOP (Código da Natureza) | DCFOP.CODNAT |
| Débitos | ICMS (Valor ICMS Produto) | DITEM.VLRICMSPRD |
| Débitos | ICMS-ST (Valor ICMS ST Produto) | DITEM.VLRICMSSTPRD |
| Débitos | Dif. Aliq. (Valor Diferencial de Alíquota) | DITEM.VLRDIFALIQUOTA |

## **Gráfico de Operações por CST**

Os dados da grid são apresentados neste gráfico agrupados por Código de Situação Tributária - CST.

Ao colocar o ponteiro do mouse sobre a série, o painel apresentará os detalhes do agrupamento. 

Visão de créditos

Esta grid traz o detalhamento de todas as operações selecionadas através do filtro aplicado agrupadas até o nível do Tipo de Crédito, que geraram crédito do PIS e da COFINS.

A origem dos dados são os Itens do Lançamento Fiscal escriturados até o momento do processamento.

Origem dos valores na estrutura de dados

|  |  |  |
| --- | --- | --- |
| **Grupo** | **Campo** | **Origem** |
| Créditos | Período (Data do Lançamento (E/S)) | DLAF.DATALF |
| Créditos | Coligada | DLAF.CODCOLIGADA |
| Créditos | Filial | DALAF.CODFILIAL |
| Créditos | Estado | GFILIAL.ESTADO |
| Créditos | CST (Situação Tributária do ICMS) | DREGRAICMS.SITTRIBUTARIA |
| Créditos | CFOP (Código da Natureza) | DCFOP.CODNAT |
| Créditos | ICMS (Valor ICMS Produto) | DITEM.VLRICMSPRD |

## **Gráfico de Operações por Tipo de Crédito**

Neste gráfico, os créditos do PIS e COFINS, que estão detalhados na grid, são agrupados por Tipo de Crédito.

Ao colocar o ponteiro do mouse sobre a série, o painel apresentará os detalhes do agrupamento. 

---

0solid

#### [Voltar para o Menu Principal](https://tdn.totvs.com/pages/viewpage.action?pageId=880053215)
