---
article_id: 4415789825303
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 65f365491b0ee2f9f8b34e65906af9c3e6323a5e8cd604f74090e8b9dda338d9
fetched_at: '2026-06-28T22:42:03.723459+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Ponto de Entrada
  SPDFIS02 - Unidade de medida e quantidade do item do documento.
type: support-article
updated_at: '2022-07-25T17:18:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415789825303-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Ponto-de-Entrada-SPDFIS02-Unidade-de-medida-e-quantidade-do-item-do-documento
---

**Dúvida**Quais os procedimentos de utilização do ponto de entrada SPDFIS02?  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.25  
  
**Solução**

**DESCRIÇÃO:**

Ponto de Entrada que define a unidade de medida e quantidade do item do documento. Por padrão é assumida sempre a primeira unidade de medida e a primeira quantidade (para gerar o registro 0190 e campo 06 do registro C170). Para utilizar a segunda unidade de medida e a segunda quantidade, é preciso realizar o tratamento utilizando este ponto de entrada.

## **ESPECIFICAÇÃO:**

## Parâmetros do ponto de entrada:

| Nome | Tipo | Descrição |
| --- | --- | --- |
| PARAMIXB | Array of Record | Array com dados de processamento com 3 elementos  [1] = Alias da tabela;  [2] = Tipo Movimento - Que pode ser **E** de Entrada ou **S** de Saída;  [3] = Registro em que ocorre a alteração;    Observação  É possível fazer um tratamento específico ao posicionar o produto, ou simplesmente retornar a segunda unidade de medida e a segunda quantidade deste documento (D1\_SEGUM ou D2\_SEGUM).  Importante  Na chamada do SPDFIS02 para alguns registros K200, H010(SPED Fiscal) não ocorrerá tratamento para o Tipo Movimento, pois estes registros não são gerados com base na movimentação das notas do período e sim com base na produção(K200) e no inventário(H010) do período respectivamente. |

## Retorno:

| Nome | Tipo | Descrição |
| --- | --- | --- |
| Nome | Tipo | Descrição |
| --- | --- | --- |
|  | Array of Record | Retorna Array com conversão da unidade de medida.  **Importante:**     * aRet[1] => Unidade de Medida do item do documento * aRet[2] => Quantidade do item do documento * aRet[3] => Fator de Conversão * aRet[4] => Tipo de Conversão M=Multiplicação/D=Divisão   A terceira posição do *array*é o **Fator de Conversão**, essa posição do *array*é opcional. A Quarta posição do array é o **Tipo de Conversão** , essa posição do *array*é opcional. |

Este ponto de entrada é utilizado para retornar o código do modelo de documento fiscal que não conste na lista de modelos de documentos fiscais oficial, a partir do Convenio 31/99. A espécie utilizada é passada como parâmetro, retornando o código válido.

Ponto de chamada: na função aModNot, que retorna o código do modelo.

Programa Fonte

```
.PRW
```

Sintaxe

MTMODNOT - Retorna código do modelo de doc. fiscal ( < cEspecie> ) --> cCodigo

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cEspecie |  |  | Array of Record |  |  |  |  |  |  |  |  | X |  |  |  |  |

Retorno

**cCodigo**

(caracter)* Código válido do modelo de documento fiscal, com dois dígitos.

## **EXEMPLO DE UTILIZAÇÃO :**

<https://tdn.totvs.com/display/public/PROT/PE+-+SPDFIS02+-+Unidade+de+medida+e+quantidade+do+item+do+documento>
