---
content_hash: c8bee77c8f20834218a188c980ef9e5fb0dedf949b2afdfa461d1f744b1663b6
fetched_at: '2026-06-29T00:10:32.067109+00:00'
page_id: '525030898'
product: rm
source: tdn-rm
title: FISCAL01-11263 DT Layout TAF - Registro T154 - Tributo COSIRF
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11263+DT+Layout+TAF+-+Registro+T154+-+Tributo+COSIRF
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | TAF |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11263 |

## **02. SITUAÇÃO/REQUISITO**

1. Buscar dados

Devem ser selecionados os lançamentos que atendam aos seguintes requisitos:

* Cliente/Fornecedor seja Pessoa Jurídica
* Status "Normal"
* Data esteja dentro do período selecionado para integração \*
* Possuam um tributo do tipo **COSIRF** associado

2. Ligar os campos no layout do Registro T154:

Implementar a partir do Release 12.1.24.

OBSERVAÇÃO: Não será necessário testar a integração com o TAF. Faremos essa atividade ao final de toda a implementação.

## **03. SOLUÇÃO**

Foi implementado a Geração do Registro T154 para Lançamento Fiscal com o Tributo COSIRF.
