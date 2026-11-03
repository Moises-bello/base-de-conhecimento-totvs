---
content_hash: 5c0997077d916d64573681098eb11a97a503272c85373c17fbc6bbd52a6527a8
fetched_at: '2026-06-29T00:10:09.360825+00:00'
page_id: '452719641'
product: rm
source: tdn-rm
title: Código de Cálculo 88 - Diferença Outros Eventos Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719641
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Provento do tipo valor. O sistema lançará o valor da diferença de outros eventos referente as férias pagas em meses anteriores.   
Será necessário a discriminação, o evento com código de cálculo 88 deve ser inserido também como Desconto do tipo valor.

Sendo que devem existir um evento com incidências e outro evento sem incidências, tanto para provento quanto para desconto.

Veja exemplo abaixo para melhor entendimento.

## **02. EXEMPLO DE UTILIZAÇÃO**

Supondo um cálculo de férias com os valores abaixo:

Criados eventos conforme abaixo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CÓD | DESCRIÇÃO | CC | TIPO |  |
| 0107 | DIF. OUTROS EVENTOS DE FERIAS PROVENTO COM INCIDÊNCIAS | 88 | Provento | Valor |
| 0245 | DIF. OUTROS EVENTOS DE FERIAS DESCONTO COM INCIDÊNCIAS | 88 | Desconto | Valor |
| 9088 | DIF. OUTROS EVENTOS DE FERIAS PROVENTO SEM INCIDÊNCIAS | 88 | Provento | Valor |
| 9188 | DIF. OUTROS EVENTOS DE FERIAS DESCONTO SEM INCIDÊNCIAS | 88 | Desconto | Valor |

Cálculo da diferença de férias por dissidio:

**Observação:** Veja que no cálculo do código de cálculo 116 - Estorno Base INSS Dissídio Retroativo Férias, somente os eventos com incidência em INSS foram considerados, ou seja, foram somados os valores:

(0045 - DIF.FERIAS) + (0079 - DIF 1/3FERIAS MÊS) + (0107 - DIF. OUTROS EVENTOS DE FERIAS PROVENTO COM INCIDÊNCIAS) – (0245 - DIF. OUTROS EVENTOS DE FERIAS DESCONTO COM INCIDÊNCIAS)

166,67 + 55,56 + 150,00 – 5,00 = 367,23

**Atenção:** Caso existam eventos com valores de diferenças que deveriam ser lançados nos eventos de código de cálculo 88 e não existam os respectivos eventos com o código de cálculo 88 necessários para o lançamento da diferença, serão emitidas mensagens. Veja como ficariam segundo o exemplo acima:

## **03.** **TABELAS UTILIZADAS**

* PEVENTO

---

Códigos de Cálculo
