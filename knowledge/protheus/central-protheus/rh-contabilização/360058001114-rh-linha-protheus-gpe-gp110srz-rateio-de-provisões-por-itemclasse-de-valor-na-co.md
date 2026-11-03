---
article_id: 360058001114
category: RH - Contabilização
content_hash: 95889e8075d8880bfbcdae1970e07d6f45c7541201592052ce966a62c801c701
fetched_at: '2026-06-28T22:43:46.137523+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - GP110SRZ - Rateio de provisões por Item/Classe
  de Valor na Contabilização
type: support-article
updated_at: '2025-07-29T12:40:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058001114-RH-Linha-Protheus-GPE-GP110SRZ-Rateio-de-provis%C3%B5es-por-Item-Classe-de-Valor-na-Contabiliza%C3%A7%C3%A3o
---

**Dúvida**GP110SRZ - Rateio de provisões por item/classe de valor na contabilização.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Ponto de Entrada para manipulação do conteúdo dos vetores*aTotFunFer, a13Salar* e *a14Salar* de forma que seja permitido o rateio dos mesmos por Item e Classe de valor. 

O retorno deve ser um array tridimensional onde cada nível representará o rateio efetuado. 

Nesses níveis devem ser inclusas duas novas posições no final do vetor: uma para o código de Item e outra para o código de Classe de Valor. 

Os vetores *aTotFunfer,a13Salar* e *a14Salar* possuem a mesma estrutura.

Cada nível terá essa mesma estrutura composta por:

10 Linhas ou Elementos.

8 Colunas para cada Linha ou Elemento.

Sendo cada Coluna correspondente a valores ref. a :  
1- Provisão de Férias ou Décimo Terceiro Salário.  
2- Avos de 13º Salário.  
3- Média Salário Provisão de Férias (posição liberada para mercado internacional - Uruguai).  
4- Adicionais.  
5- Um Terço de Férias.  
6- INSS.  
7- FGTS.  
8- PIS.  
  
**Observações:**

Considerar a seguinte configuração de parâmetros:

MV\_RATPROV com conteúdo igual a 'N'.

MV\_ITMCLVL com conteúdo igual a '1'.

Contabilizar por Matrícula.

**Exemplos:**

#INCLUDE "Protheus.ch"  
#INCLUDE "RWMAKE.CH"  
  
User Function GP110SRZ()  
Local aRateio := {}  
Local aCpy := {}  
Local cItem := "000000001"  
Local cClVl1 := "900000001"  
Local cClVl2 := "123456789"  
Local nParam1 := PARAMIXB[1] // String referente ao Roteiro de Calculo  
Local nParam2 := PARAMIXB[2] // Data de Referencia  
Local nX := 0  
  
If nParam1 == "FER"  
// Tratamento de Rateio para Ferias  
  
// RATEIO 1  
// Copia estrutura  
aCpy := aClone(aTotFunFer)  
// Inclusao de Item e Classe de Valor 1  
For nX := 1 to Len(aTotFunFer)  
AADD(aTotFunFer[nX],cItem) // Item  
AADD(aTotFunFer[nX],cClVl1) // Classe de Valor 1  
Next nX  
  
aTotFunFer[3][2] := 1150  
aTotFunfer[3][4] := 416.66  
aTotFunfer[3][5] := 479.99  
aTotFunfer[3][6] := 133.33  
// Inclusao dos arrays rateados por Item  
AADD(aRateio,aTotFunfer)  
  
// RATEIO 2  
// Copia estrutura  
aTotFunfer := aClone(aCpy)  
For nX := 1 to Len(aTotFunFer)  
AADD(aTotFunFer[nX],cItem) // Item  
AADD(aTotFunFer[nX],cClVl2) // Classe de Valor  
Next nX  
aTotFunFer[3][2] := 1350  
aTotFunfer[3][4] := 416.66  
aTotFunfer[3][5] := 479.99  
aTotFunfer[3][6] := 133.33  
// Inclusao dos arrays rateados por Item  
AADD(aRateio,aTotFunfer)  
  
EndIf  
  
Return ( aRateio )

   
**Mais informações:**

|  |  |
| --- | --- |
| Parâmetros | PARAMIXB[1] correspondente ao código identificador do roteiro de cálculo, sendo as opções válidas:  "FER" - Roteiro de Férias (vetor aTotFunFer)  "13" - Décimo Terceiro Salário (vetor a13Salar)  "14" - Décimo Quarto Salário (vetor a14Salar)  PARAMIXB[2] correspondente ao conteúdo da variável dDataRef (Data de Referência) |
| Retorno | aRateio (**vetor**)  Deverá ser do tipo Local. |

**Saiba mais:** <https://tdn.totvs.com/pages/viewpage.action?pageId=181142163>
