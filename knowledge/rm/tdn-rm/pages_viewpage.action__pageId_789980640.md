---
content_hash: 2e722db46db908eba0a60bd2b07a5cd940ede0455a0d7d17dcc802304a6b19de
fetched_at: '2026-06-29T00:11:39.797630+00:00'
page_id: '789980640'
product: rm
source: tdn-rm
title: FISCAL01-20646 - DT - EFD REINF - CSRF não carrega natureza de rendimento do
  produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789980640
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro de Movimento |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-20646 |

## **02. SITUAÇÃO/REQUISITO**

Para as Retenções de PIS-RF\CSLL-RF\COFINS-RF e CSRF será implementado a opção de buscar o Código da Natureza de Rendimento do Cadastro do Produto – Anexo – Dados Fiscais do Produto – Campo Código de Natureza de Rendimento.

## **03. SOLUÇÃO**

Adicionamos a regra para verificar se existe produto cadastrado no movimento, se sim, buscar a natureza de rendimento do produto e preencher no item do movimento, na coluna tributos.

Com esta implementação a seleção será a seguinte:

Para as retenções de **PISRF, COFINSRF, COSIRF, CSLLRF e CSRF**, o Campo Natureza de Rendimento no Tributo do Item do Movimento ou no Tributo do Movimento passa a ter o preenchimento na inclusão do Movimento conforme a regra:

> Se preenchido no Cadastro do Produto (Anexo – Dados Fiscais do Produto – Campo Código de Natureza de Rendimento), considera este.

>Senão, preenchido no Cadastro do Cliente\ Fornecedor (Tributos, demais tributos na pasta Tributos Default do Fornecedor), considera este.

>Senão, considera o preenchido no tipo de Movimento

Disponível a partir da biblioteca 12.1.2302
