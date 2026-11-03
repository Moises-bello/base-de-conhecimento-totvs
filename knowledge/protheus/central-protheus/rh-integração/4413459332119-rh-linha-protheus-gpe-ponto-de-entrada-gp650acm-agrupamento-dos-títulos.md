---
article_id: 4413459332119
category: RH - Integração
content_hash: 719816f12bf9ed58f607cfb306104ba7d17c33cc809bc8ae6c243d7a60d6d950
fetched_at: '2026-06-28T22:43:44.980615+00:00'
product: protheus
section_id: 360003115611
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP650ACM - Agrupamento dos Títulos
type: support-article
updated_at: '2025-09-11T12:09:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413459332119-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP650ACM-Agrupamento-dos-T%C3%ADtulos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28423159832471) Tempo aproximado para leitura: **00:01:00** min **Dúvida**Utilização do ponto de entrada GP650ACM  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

O ponto de entrada GP650ACM é utilizado no momento do agrupamento dos títulos, sendo possível armazenar no array “aAliasFields” os dados que identificam a origem do título. Exemplo: filial, matricula, verba, centro de custo, valor.

#### Um exemplo de utilização deste ponto de entrada é a necessidade de criar uma tabela para listar todos os lançamentos que fazem parte de um determinado título.

Neste caso é necessário utilizar também o ponto de entrada GP650CHK para obter o número do título.

**Programa Fonte**

gpem650

**Sintaxe**

#### GP650ACM - Agrupamento dos Títulos ( [ ] )

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  |  |  |  | Array of Record |  |  |  |  |  |  |  |  |  |  |  |  |  |

Retorno

()

Observações

O exemplo a seguir ilustra a necessidade de criar uma tabela contendo o detalhamento do título, com os lançamentos que o compõe.

Utiliza-se os dois pontos de entrada: GP650ACM e GP650CHK.

**Exemplos**

```
============================================||Exemplo de utilização do ponto de entrada GP650ACM||============================================User Function GP650ACM()//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿//³ Declaracao de Variaveis                                             ³//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙLocal aArea := GetArea()Local cFil	 := &cFilLanLocal cMat	 := &cMatLanLocal cCC  	 := &cCcLanLocal cPD	 := &cPDLanLocal nSeq	 := 0              nPos:= Ascan( aAliasFields ,{|x|x[1]+x[2]+x[3]+x[4]==cFil+cMat+cCC+cPD }) If nPos == 0		Aadd( aAliasFields, { 	cFil, 	;			cMat, 	;			cCC,	;		    				cPD,	;			"001"	} )Else	nSeq := VAL(aAliasFields[nPos,5])+1		Aadd( aAliasFields, { 	cFil, 	;			cMat, 	;			cCC,	;		    				cPD,	;			strZero(nSeq,3)	} )EndIf      RestArea(aArea)Return=============================================||Exemplo de utilização do ponto de entrada GP650CHK:||=============================================User Function GP650CHK()Local nX 	:= 1Local aArea := getArea()       For nX := 1 to Len(aAliasFields)	       If Z01->(!dbSeek(aAliasFields[nX,1]+cNovoTit+aAliasFields[nX,2]+aAliasFields[nX,3]+ ;				aAliasFields[nX,4]+aAliasFields[nX,5] ))		RecLock("Z01", .T. )	Z01->Z01_FILIAL :=	aAliasFields[nX,1]	Z01->Z01_TIT       :=	cNovoTit	Z01->Z01_MAT     :=	aAliasFields[nX,2]	Z01->Z01_CC       :=	aAliasFields[nX,3]	Z01->Z01_PD       :=	aAliasFields[nX,4]	Z01->Z01_SEQ    :=	aAliasFields[nX,5]		MsUnLock()      EndIf	Next nXRestArea( aArea )Return
```

**Variáveis**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  | aAliasFields |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |
|  | cFilLan |  |  | Caracter |  |  | Global |  |  | Não |  |  |  |  |
|  | cCpoAgrup |  |  | Caracter |  |  | Global |  |  | Não |  |  |  |  |
|  | cCcLan |  |  | Caracter |  |  | Global |  |  | Não |  |  |  |  |
|  | cMatLan |  |  | Caracter |  |  | Global |  |  | Não |  |  |  |  |
|  | cPDLan |  |  | Caracter |  |  | Global |  |  | Não |  |  |  |  |
|  | cValLan |  |  | Caracter |  |  | Global |  |  | Não |  |  |  |  |

**Saiba Mais:**

https://tdn.totvs.com/pages/viewpage.action?pageId=6079183
