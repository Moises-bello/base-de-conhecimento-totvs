---
content_hash: aa5c1ae5bc4cd2e128043fec3e30b4055be6512db17b7cdf8751f6db3b1eb79f
fetched_at: '2026-06-29T00:12:10.195981+00:00'
page_id: '953000296'
product: rm
source: tdn-rm
title: DT - Contabilização - Parâmetro "Ajustar diferença (até R$ 0,99) entre débito
  e crédito lançando a diferença na última partida"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953000296
version: 8
---

## **1. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Contabilização -  Parâmetro "Ajustar diferença (até R$ 0,99) entre débito e crédito lançando a diferença na última partida" |
| **País:** | Brasil |
| **Issue** | [DRHROTRM-12914](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12914) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2410.250
* 12.1.2502.156
* 12.1.2506.100 ou superiores

## **03. SITUAÇÃO/REQUISITO**

Tratativa no produto para que, ao gerar a contabilização, caso existam diferenças de até R$ 0,99 entre os valores de débito e crédito no lote contábil, em decorrência de arredondamentos, o sistema registre automaticamente essa diferença na última partida do lançamento.

## **04. SOLUÇÃO**

Implementado o parâmetro **"Ajustar diferença (até R$ 0,99) entre débito e crédito lançando a diferença na última partida"**, no menu Configurações | Folha Normal | Contabilização | Parâmetros I.

Esse parâmetro permite que, nos casos em que houver uma diferença de atéR$ 0,99 entre os valores de débito e crédito, decorrente de arredondamentos, o sistema registre automaticamente essa diferença na última partida do lançamento contábil.

1) Exemplo de lote gerado com o parâmetro desmarcado:

Diferença de 0,01 de valores entre débito e crédito.

2) Exemplo de Lote gerado com o parâmetro marcado.

Não foi apresentada a diferença de 0,01.

A última partida do lote foi gerada acrescentado o valor 0,01 da diferença.

## **05. DEMAIS INFORMAÇÕES**

[Contabilização - Parâmetros](https://tdn.totvs.com.br/pages/viewpage.action?pageId=519715154)
