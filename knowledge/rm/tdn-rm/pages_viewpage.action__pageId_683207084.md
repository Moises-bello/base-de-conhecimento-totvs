---
content_hash: 98e064fda045cc8cc3a70c4355e4015f04e4c21055c91ce3175262ce0f902878
fetched_at: '2026-06-29T00:11:18.108127+00:00'
page_id: '683207084'
product: rm
source: tdn-rm
title: FISCAL01-17948 - DT - Melhoria da mensagem de erro na geração de Guias GPS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=683207084
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Guias Apuração |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17948 |

## **02. SITUAÇÃO/REQUISITO**

Ao executar a geração de Guias GPS para períodos de apuração de INSS, caso o lançamento fiscal de entrada tenha um Identificador de código de receita preenchido nos tributos da situação tributária que não corresponda a nenhum cadastro INSS\PJ uma mensagem de alerta era exibida.

O campo Identificador de Código de Receita é utilizado para realizar um lookup de outro registro no entanto o tipo do campo é um texto simples, de forma que pode haver um entendimento de que o valor preenchido no campo será o valor de Código de Receita usado na geração da Guia.

## **03. SOLUÇÃO**

Alterada a mensagem de erro exibida no log da geração de guias gps para deixar mais evidente o motivo do código da guia ser preenchido com o código do cadastro do tributo e da necessidade de fazer o cadastro de um INSS\PJ.

Mensagem que era exibida antes da atualização:

O Código de Pagamento foi gerado com o Código de Receita preenchido no Tributo! Motivo: O Identificador do Código de Receita não foi preenchida em Outros Tributos da Situação Tributaria 5555 do Lançamento 55555.

Nova mensagem:

O Código de Pagamento foi gerado com o Código de Receita preenchido no Tributo! Motivo: O Identificador do Código de Receita não foi preenchida em Outros Tributos da Situação Tributaria 5555 do Lançamento 55555 **ou não foi feito um cadastro de Código de Receita correspondente ao Identificador informado. Acesse BackOffice Gestão de Estoque Compras e Faturamento -> Cadastros -> Fiscais -> Mais -> INSS\PJ e cadastre um Código de Retenção para o Identificador informado na Situação Tributária.**

Disponível a partir da versão 12.1.33
