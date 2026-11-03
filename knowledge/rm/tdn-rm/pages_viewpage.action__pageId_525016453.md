---
content_hash: 0b3734a8f8a43624373b20789c411340ab6e088614f0e7990521d7f2c8e93a3e
fetched_at: '2026-06-29T00:10:32.012267+00:00'
page_id: '525016453'
product: rm
source: tdn-rm
title: Anonimizar funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525016453
version: 2
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Regras para anonimizar funcionários**
3. **Processo para anonimizar funcionários**

## **01. VISÃO GERAL**

Para atender a [Lei Nº 13.709/18](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) foi criado o processo "anonimizar funcionários", este processo irá verificar se o funcionário da empresa possui algum vínculo com vagas ou solicitações de funcionários em vagas de estágio, se não possuir, o processo irá excluir o funcionário, caso este possua algum vínculo o sistema irá verificar algumas regras (descritas no item 02) e se o funcionário for elegível para anonimizar o sistema irá alterar os campos permitidos e definidos para um valor fictício (ex: 000).

Campos passíveis de anonimizar:

| Coluna | Descrição |
| --- | --- |
| CARTIDENTIDADE | Nº da Carteira de Identidade |
| CPF | CPF |
| DTEMISSAOCARTCIDADAO | Data emissão do cartão de cidadão |
| DTEMISSAOIDENT | Data de Emissão da Identidade |
| DTEMISSAOPASSAPORTE | Data emissão passaporte |
| DTVALIDADECARTCIDADAO | Data validade do cartão de cidadão |
| DTVALIDADEPASSAPORTE | Data validade passaporte |
| EMAIL | E-mail do funcionário na Empresa |
| NOME | Nome do funcionário |
| NPASSAPORTE | Número do passaporte |
| NUMEROCARTCIDADAO | Número do cartão de cidadão |
| ORGEMISSORIDENT | Órgão Emissor da Identidade |
| ORGEXPCARTCIDADAO | Órgão expedidor do cartão de cidadão |
| RFC | RFC |
| TELEFONE | Telefone do funcionário |
| UFCARTIDENT | UF da Carteira de Identidade |

## **02.****REGRAS PARA ANONIMIZAR FUNCIONÁRIOS**

O funcionário que não possuir vínculo com nenhum dos itens abaixo será excluído do sistema, caso este possua, o sistema irá mascarar, os vínculos são:

* Estar vinculado a uma termo de compromisso de estágio.
* Estar vinculado uma solicitação de estágio.

## **03. PROCESSO PARA ANONIMIZAR FUNCIONÁRIOS**

Para ter acesso ao processo é necessário que seja concedida permissão ao item de menu no perfil desejado:

O processo será executado com base na visão de funcionários da empresa, sendo necessário somente selecionar o(s) funcionário(s) que o sistema irá executar o processo:

O processo será executado em segundo plano e seu resultado poderá ser consultado no rodapé do TOTVS Educacional:

Log do processo:

Dados do usuários anonimizado:
