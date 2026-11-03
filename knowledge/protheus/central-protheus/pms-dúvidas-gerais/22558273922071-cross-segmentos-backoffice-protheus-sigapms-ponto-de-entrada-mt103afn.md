---
article_id: 22558273922071
category: PMS - Dúvidas Gerais
content_hash: 0df1704857faa416dba0ec71ecf20e77df0ccb5aedc75ba7a0e1834ad6e285b4
fetched_at: '2026-06-28T22:37:17.696805+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Ponto de entrada "MT103AFN"
type: support-article
updated_at: '2024-04-05T11:23:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22558273922071-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Ponto-de-entrada-MT103AFN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22558266777751) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o exemplo de uso do ponto de entrada "MT103AFN"?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**

O objetivo do ponto de entrada é injetar o valor desejado no campo "Imobilizado (D1\_CBASEAF)"  
  
Dentro do fonte abaixo há explicações sobre o que ele pede de inserção e o que ele retorna para compor o campo na entrada "Imobilizado (D1\_CBASEAF)"

OBS 1: Foram passados por parâmetro dados auxiliares referentes aos campos do cadastro TES (Tipo de Entrada e Saída), "Atual. Ativo (F4\_ATUAATF)", "Desme. IT ATF (F4\_BENSATF)" e o parâmetro MV\_ATFDCBA.

OBS 2: O campo "Imobilizado (D1\_CBASEAF)" pode não receber o conteúdo todo dependendo de seu tamanho.

**Exemplo:**

```
#INCLUDE "RWMAKE.CH"
#INCLUDE "PROTHEUS.CH"

/*

±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±
±±³ Gravação do ativo fixo: A103GrvAtf                                              ±±³
±±³                                                                                 ±±³
±±³          ³cBase   : Codigo Base do Ativo                                        ³±±
±±³          ³cItem   : Item da Nota Fiscal                                         ±±³
±±³                                                                                 ±±³
±±³ Observacao³Este Programa grava um ativo por item de NF, alterando-se o          ³±±
±±³          ³Item do ativo. Nem todos os dados do Ativo serao gravados             ³±±
±±³          ³pois nao ha todas as informações na nota fiscal e o classificador     ³±±
±±³          ³da Nota Fiscal nao tem condições de faze-lo.                          ±±³
±±³                                                                                 ±±³
±±³ Campo destino: SD1->D1_CBASEAF := cBase + cItem                                 ±±³
±±³                                                                                 ±±³
±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±

*/

User Function MT103AFN()

    Local cBase      := "MT103AFN06"    // Codigo personalizado que irá no campo D1_CBASEAF
    Local cItem      := "0001"          // Numero item personalizado que irá no campo D1_CBASEAF depois da variável "cBase"	
    Local aRet       := {}              // Criação da variável que será retornada pela função ao sistema
    Local aTeste     := Paramixb[1]     // Dados do projeto
    Local cAtuaATF   := Paramixb[2]     // Campo F4_ATUATF (Atualiza ativo:  "S"-Sim | "N"-Nao)
    Local cDesItATF  := Paramixb[3]     // Campo F4_BENSATF (Desmembra itens ativo:  "1"-Sim | "2"-Nao)
    Local lTipoDes   := Paramixb[4]     // Parâmetro MV_ATFDCBA (".F." Desmembra itens | ".T." Desmembra codigo base)
    
    MsgAlert("Execução do ponto de entrada MT103AFN")

    If !Empty(aTeste)
        MsgAlert("Projeto (Integração PMS):" + aTeste[1][2][1][1])
    EndIf
    
    MsgAlert("Atualiza Ativo?(S-Sim /N-Nao): " + cAtuaATF)
    MsgAlert("Desmembra itens ativo?(1-Sim /2-Nao): " + cDesItATF)
    MsgAlert("F-Desmembra itens / T-Desmembra codigo base: " + (iif(lTipoDes,"T","F")))

    aRet := {cBase, cItem}

    MsgAlert("Codigo - Item personalizados: " + aRet[1] + " - " + aRet[2])  

Return(aRet)
```

**Saiba mais:**

[Pontos de Entrada - Gestão de Projetos - P12](https://tdn.totvs.com/x/fg_uHg)

[MT103AFN - Utiliza dados de ativo fixo](https://tdn.totvs.com/x/YLBn)
