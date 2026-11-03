---
content_hash: b4a543e661c99c9d24ba7c169f0a72a7dac01ae151918ede64d715842b2dc014
fetched_at: '2026-07-02T19:24:20.503864+00:00'
page_id: '253986044'
product: protheus
source: tdn-tec
title: GetRpoLog
type: documentation
url: https://tdn.totvs.com/display/tec/GetRpoLog
version: 6
---

GetRpoLog

Retorna um array com os dados de todos os patchs aplicados. 

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nRPO | numérico | Indica o nome o repositório que será feita a busca. Valores possíveis: 1 - RPO Padrão, 3 - RPO Custom. Caso o parâmetro não seja informado o valor 1 é assumido como padrão. Este parâmetro é válido a partir a release 20.3.1.x (Application Server Harpia) |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aData | vetor | Retorna um array com os dados de todos os patchs aplicados. Para informações do formato do array, consulte a tabela Formato do array de retorno, na área Observações. |

## Observações

Formato do Array de retorno:

| Posição | Valor |
| --- | --- |
| aData[1] | Array com informações sobre o RPO |
| aData[1][1] | Versão do RPO |
| aData[1][2] | Data do RPO |
| aData[2] | Quantidade de patchs aplicados |
| aData[3] | Array com informações sobre o patch |
| aData[3][1] | Nome do patch |
| aData[3][2] | Data de geração do patch |
| aData[3][3] | Build de geração do patch |
| aData[3][4] | Data de aplicação do patch |
| aData[3][5] | Build de aplicação do patch |
| aData[3][6] | Número de programas contidos no patch |
| aData[3][7] | Array com informações sobre os programas |
| aData[3][7][1] | Nome do programa |
| aData[3][7][2] | Data do programa |
| aData[3][8] | Array com informações sobre os programas |
| aData[3][8][1] | Nome do programa |
| aData[3][8][2] | Data do programa |
| aData[3][...] | Array com informações sobre os programas |
| aData[3][...+1] | Lógico com a informação se o patch foi aplicado forçado |
| aData[3][...+2] | Tipo do patch |

**Tipo do patch:**

| Valor | Descrição |
| --- | --- |
| 1 - Upd | .upd |
| 2 - Pak | .pak |
| 3 - Ptm | .ptm |

Esta função está disponível, na linguagem AdvPL, a partir da build 7.00.131227A 1.1.0 e 2.1.0 do TOTVS Application Server.

## Exemplos

cppEclipseExemplo 1truefalse

## Abrangência

Protheus 10, Protheus 11, Protheus 12
