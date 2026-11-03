---
content_hash: b7ed258b378b12a4ccd896c5bbb06bd9031fd9c22d0cca8e3c391cd026d0660b
fetched_at: '2026-06-29T00:11:55.565670+00:00'
page_id: '862119342'
product: rm
source: tdn-rm
title: DT - Complemento da Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Complemento+da+Folha+de+Pagamento
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Complemento da Folha de Pagamento |
| País: | Brasil |
| Issue: | [DRHCALCRM-6497](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6497) |

## **02. Versões**

**A partir dos patches:**

* 12.1.2310.245
* 12.1.2402.206
* 12.1.2406.135
* 12.1.2410 e superiores

## **03.** **SITUAÇÃO/REQUISITO**

Implementar solução para lançamento do cálculo do Complemento da Folha de Pagamento conforme o [artigo nº 27 da Instrução Normativa 2110/2022](https://tdn.totvs.com/pages/releaseview.action?pageId=738253118#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosDiferen%C3%A7asSalariaisIN2110-3.4eSocial).

## **04. SOLUÇÃO**

Foi criado um processo em Folha Mensal | lançamentos | Complemento da Folha para executar o cálculo e fazer o lançamento no período atual da base e na tabela  PFVERBASDIS na competência período informado no processo a ser complementada, para que os valores seja enviado para o eSocial no evento S-1200 no registro infoPerAnt.

Para utilizar o processo é necessário fazer as seguintes configurações:

* Informar valor no parâmetro geral “Período Complemento Folha ” em “Configurações | Parametrizador | Folha Normal | Geral 2/2” que deve ser maior que 1000 e não pode ser igual a nenhum período do RRA seja Folha/Férias, 13o Salário ou Rescisão.
* Cadastrar em dados do dissídio apenas com o tipo de acordo J - Parcelas complementares conhecidas após o fechamento da folha.

## **05. ASSUNTOS RELACIONADOS**

* [Complemento da Folha de Pagamento](https://tdn.totvs.com/display/LRM/Complemento+da+Folha+de+Pagamento)
* [Parametrizador - Geral 2/2](https://tdn.totvs.com.br/pages/releaseview.action?pageId=715817366)
* [Orientações Consultoria de Segmentos](https://tdn.totvs.com/pages/releaseview.action?pageId=738253118)
