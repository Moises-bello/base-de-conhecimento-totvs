---
content_hash: b3bf9900e998ad3bbef73535df7931261f09c49aa4a05596ba16063c68837526
fetched_at: '2026-06-29T00:10:26.025854+00:00'
page_id: '510496178'
product: rm
source: tdn-rm
title: 5588822  FISCAL01-8810 DT Alterar forma de geração da tag cBenef na NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=510496178
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Totvs Gestão Fiscal |
| Função: | Cadastro de Produtos - Anexo Dados Fiscais por UF |
| Ticket: | [5588822](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%225588822%22 "5588822") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8810 |

## **02. SITUAÇÃO/REQUISITO**

O cliente solicita melhoria no sistema quanto ao preenchimento do campo cBenef em Dados Fiscais Por UF no cadastro do produto, a solicitação de melhoria e evidenciada pois a opção disponível no RM para o preenchimento da informação do cBenef não atende, tendo em vista a estrutura de cadastro da COMAU.

Atualmente, os produtos cadastrados são utilizados para qualquer operação (remessa, venda, transferência, etc.), sendo assim,o fiscal do cliente teria que supervisionar a emissão de notas, avaliar o tipo de ICMS, associar o código e ainda, retirá-lo após a emissão, para não prejudicar o fluxo pois o mesmo produto é utilizado para remessa ou venda e sendo assim os códigos são diferentes.

## **03. SOLUÇÃO**

Alterações cadastrais:

* Anexo Dados Fiscais por UF no Cadastro do Produto. Este campo deverá ser marcado caso ocorra de um mesmo Produto possuir ou não Benefício Fiscal em uma mesma UF.

Alterações no processo de envio da NF-e

Vamos passar a considerar na Emissão da NF-e tag cBenef da NFe 4.00,  conforme a seguinte sequência:

* Cadastro do Produto - Anexo Dados Fiscal por UF - Campo Código Fiscal.  
  Ou, se não estiver preenchido:
* A tag será preenchida com o Código de Ajuste associado ao CFOP informado no Item do Movimento se o campo Registro estiver com a opção "E115" selecionada e o Estado do respectivo cadastro for igual à UF da Filial emitente do documento eletrônico, além disso deve estar marcado um flag no Anexo de Dados Fiscais por UF do Cadastro do Produto, informando que o mesmo possui benefício fiscal.
