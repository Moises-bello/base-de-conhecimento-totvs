---
article_id: 360007202292
category: Gestão de Transportes (TMS)
content_hash: d840617fd7197ec7f5a61c60d2bd3d4304c6bd26c1dde1a7b6e048491edfb6b5
fetched_at: '2026-06-28T22:45:29.619992+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM040ATZ Validações de
  Cálculos em Cotação de Frete
type: support-article
updated_at: '2022-01-18T17:33:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007202292-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040ATZ-Valida%C3%A7%C3%B5es-de-C%C3%A1lculos-em-Cota%C3%A7%C3%A3o-de-Frete
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:01:12 min  
  
Dúvida**Como implementar o ponto de entrada **TM040ATZ** **Validações de Cálculos em Cotação de Frete**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM040ATZ** está localizado no **TMSA040** **Cotação de Frete** e é executado após o calculo da cotação, permitindo assim o usuário realizar consistências e validações com os valores calculados.  
  
**Programa Fonte**: TMSA040.PRW  
  
**Sintaxe**: TM040ATZ - Validações de Cálculos em Cotação de Frete ( [ ParamIxb[1] ], [ ParamIxb[2] ], [ ParamIxb[3] ], [ ParamIxb[4] ], [ ParamIxb[5] ], [ ParamIxb[6] ], [ ParamIxb[7] ], [ ParamIxb[8] ], [ ParamIxb[9] ] ) --> Nil  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| ParamIxb[1] | Numérico | Valor Total Líquido |  |  |  |
| ParamIxb[2] | Array of Record | Valor Total do Imposto |  |  |  |
| ParamIxb[3] | Array of Record | Valor Total Bruto |  |  |  |
| ParamIxb[4] | Array of Record | Total de Volumes |  |  |  |
| ParamIxb[5] | Array of Record | Quantidade |  |  |  |
| ParamIxb[6] | Array of Record | Peso |  |  |  |
| ParamIxb[7] | Array of Record | Peso Cubado |  |  |  |
| ParamIxb[8] | Array of Record | Valor da Mercadoria |  |  |  |
| ParamIxb[9] | Array of Record | Metragem Cúbica |  |  |  |

**Retorno:**

Nil      (nulo)

**Exemplos**:  
#Include "Protheus.ch"  
User Function TM040ATZ()  
Local nValor := 0  
Local nValPas := ParamIxb[1]  
Local nQtdVol := ParamIxb[4]  
If !Empty(nValMer)   
       nValor := nValPas \* nQtdVol\

End If  
Return Nil  
  
**Variáveis**:  

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record | Global | Não |  |
