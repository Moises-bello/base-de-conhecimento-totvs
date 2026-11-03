---
content_hash: 80116ec209d90a87f3d23d0f6fb1320e9ea4aa02655bf56a64b3feabec614df0
fetched_at: '2026-06-29T00:11:35.894086+00:00'
page_id: '768409874'
product: rm
source: tdn-rm
title: 'DT - S-1210: Quando há troca de CPF e existe <perRef> diferentes'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=768409874
version: 12
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Geração para perRef diferentes quando há troca de CPF (S-1210) |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-4955 |

## **02. VERSÕES**

**A partir dos patches:**

* 12.1.2209.235
* 12.1.2302.211
* 12.1.2306.128
* e Superiores

## **03. SITUAÇÃO/REQUISITO**

Quando era realizado a alteração de CPF no inicio da competência e a empresa trabalhava com o mês caixa, o envio do pagamento no evento S-1200 era enviado no CPF anterior e o evento corresponde ao liquido, evento S-1210, era enviado com o novo CPF, o que ocasionava erro no envio e-Social.

## **04. SOLUÇÃO**

Segundo documento abaixo, da Consultoria de Segmentos, quando ocorrer uma troca de CPF, o envio do S-1210 deve ser realizado com o CPF vinculado ao S-1200.

Implementamos a geração do evento do S-1210 no CPF correspondente, conforme orientação acima.

Para situação onde existe envelope do mês anterior e envelope do mês atual, sendo os dois com pagamento no mês atual, e o funcionário trocou o CPF no mês anterior, é necessário o envio de dois S-1210 com o mesmo período de apuração, sendo:

* Um XML S-1210 de período apuração MESATUAL com o CPF antigo e período referência MESANTERIOR;
* Um XML S-1210 de período apuração MESATUAL com o CPF novo e período referência MESATUAL.

**Exemplo:**

Funcionário tinha **CPF X** e teve alteração em 01/09/2022 para **CPF Y**

Envelope do mês 08 com pagamento em 09/2022

Envelope do mês 09 com pagamento em 09/2022

Serão gerados dois XML's do evento S-1210, sendo um com o **CPF X** e perRef 08/2022 e outro com **CPF Y** e perRef 09/2022

ATENÇÃO - LEMBRETE

Para realizar a tratativa mencionada anteriormente, é imprescindível executar o script por meio da versão correta do sistema RM.Atualizador.exe. Essa medida é necessária para criar um campo interno no produto, a fim de identificar o CPF a ser considerado no evento S-1210.

## **05. ASSUNTOS RELACIONADOS**

* <https://tdn.totvs.com.br/pages/viewpage.action?pageId=550306792>
