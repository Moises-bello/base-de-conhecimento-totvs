---
article_id: 360059335453
category: RH - Provisão
content_hash: 619a7e1427233877289dd4eab67d8b30b6f0f02eba62732760b91df7a96b883d
fetched_at: '2026-06-28T22:43:55.617464+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Alteração do Saldo do Mês da Provisão (Ponto de
  entrada  GPEPMSPRV)
type: support-article
updated_at: '2025-06-18T18:23:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059335453-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-do-Saldo-do-M%C3%AAs-da-Provis%C3%A3o-Ponto-de-entrada-GPEPMSPRV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32903426348055)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ajuste do saldo do Mês da Provisão pelo Ponto de Entrada GPEPMSRV.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de  Pessoal - Todas as versões.  
  
**Solução**Esse ponto de entrada é executado na função **fCalcProv**, após o cálculo do valor do mês das provisões.   
  
Através deste ponto de entrada o cliente pode alterar esse valor calculado, e estará disponível os valores referentes ao saldo anterior e saldo total atual calculados pelo sistema. Essa rotina é chamada em Gestão de Projetos (SIGAPMES), esses valores são utilizados no recálculo do custo do recurso.  
  
Gravação do valor referente ao mês de referência das provisões, **função fCalcProv,** chamada através da **função CalCustoFun(),**do sistema de Gestão de Projetos( SIGAPMS).

Programa Fonte

```
GPEXCAL2.PRX
```

**Sintaxe**

GPEPMSPRV - Alteração do Saldo do Mês da Provisão ( [ ] ) --> nProvFeV

Parâmetros:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  |  |  |  | Array of Record |  |  |  |  |  |  |  |  |  |  |  |  |  |

Retorno

**nProvFeV** (numérico)  
-> Saldo do mês da Provisão do 14º Salário

**Observações:**

Uma vez que optar em utilizar este ponto de entrada, o valor do mês da provisão de férias vencidas, proporcionais, 13ºsalário e 14ºsalário, devem ser retornados, pois do contrário seu valor ficará Zerado.

Hoje o sistema faz o cálculo do mês pegando o Saldo Atual menos o Saldo anterior, e as férias proporcionais é calculada juntamente com a vencida.

Retornar através deste ponto de entrada as variáveis:

**nProvFeV  =>** Saldo do mês da Provisão de Férias Vencidas  
**nProvFeP  =>** Saldo do mês da Provisão de Férias Proporcionais  
**nProv13S  =>** Saldo do mês da Provisão do 13ºSalário  
**nProv14S  =>** Saldo do mês da Provisão do 14ºSalário.

Exemplos:  
#INCLUDE 'RWMAKE.CH'  
USER FUNCTION GPEPMSPRV()  
If ( ( nPrFerVPos + nPrFerPPos) - ( nPrFerVPos - nPrFerPAnt) ) > 1000   
nProvFeV := (nPrFerVPos + nPrFerPPos) - (nPrFerVPos - nPrFerPAnt)   
Else   
nProvFeV := 1000  
EndIf   
If (nPr13SalPos - nPr13SalAnt) > 500   
nProv13S := (nPr13SalPos - nPr13SalAnt)   
Else   
nProv13S := 500  
EndIf   
nProv14S := If( (nPr14SalPos - nPr14SalAnt) == 0, 200,(nPr14SalPos - nPr14SalAnt) )   
Return (nProvFeV, nProv13S, nProvFeP, nProv13S)

Variáveis

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099742933)

**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) [Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
