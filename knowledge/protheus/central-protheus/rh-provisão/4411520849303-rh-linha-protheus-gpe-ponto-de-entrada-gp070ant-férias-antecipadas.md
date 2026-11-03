---
article_id: 4411520849303
category: RH - Provisão
content_hash: f6ca87ec901d18610a56bda7d194d920d5f18703b6d91b64e8aaee83ef4aae06
fetched_at: '2026-06-28T22:43:56.935857+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP070ANT - Férias Antecipadas
type: support-article
updated_at: '2025-10-24T13:08:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411520849303-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP070ANT-F%C3%A9rias-Antecipadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32997894486039) Tempo aproximado para leitura: **00****:02:00 min** **Dúvida**Utilização do ponto de entrada GP070ANT.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução****01. Visão Geral**

Ponto de Entrada que permite alterar a data-base das férias e a quantidade de dias de férias antecipadas no cálculo de Provisão de Férias.

**Programa Fonte**

GPEM070.PRX

**Sintaxe**

GP070ANT - Férias Antecipadas ( [ PARAMIXB[1] ], [ PARAMIXB[2] ], [ PARAMIXB[3] ] ) --> aDados

## **02. Exemplos de Utilização:**

Exemplos:

User Function GP070ANT()  
Local cFilP := AllTrim( TPR->PR\_FILIAL )  
Local cMatP := AllTrim( TPR->PR\_MAT )  
Local aSaveSRH := {}  
Local aDados := {}   
Local dDtBasF := ParamIxb[1] //Data Base Ferias  
Local dDtPerAq := ParamIxb[2] //Data de Referencia para Calculo  
  
//Se a database de ferias eh maior que a data de referencia  
If dDtBasF > dDtPerAq   
If cFilP == "01" .And. cMatP == "000015"   
aSaveSRH := SRH->(GetArea())   
dbSelectArea("SRH")   
If SRH->( dbSeek( cFilP + cMatP ) ) //Se Inicio das ferias ocorreu antes de terminar o periodo aquisitivo.  
If SRH->RH\_DATAINI < SRH->RH\_DBASEAT //Quantidade de dias de ferias + abono pecuniario do recibo  
aAdd( aDados, 30 ) //Data de inicio do periodo aquisitivo das ferias  
aAdd( aDados, CTOD("17/02/2008") )  
Alert("Passou pelo Ponto de Entrada: GP070ANT")  
Endif  
Endif  
RestArea(aSaveSRH)  
EndIf   
EndIf  
Return(aDados)

**03.****Parâmetros****Outras Ações / Ações relacionadas**

| Nome | Tipo | Descrição | Default | Obrigatório | Referencia |
| --- | --- | --- | --- | --- | --- |
| PARAMIXB[1] | Array of Record | Data Base de Férias. |  |  |  |
| PARAMIXB[2] | Array of Record | Data de Referência para cálculo. |  |  |  |
| PARAMIXB[3] | Array of Record | Dias de Férias Antecipadas. |  |  |  |

**04. Retorno****aDados**()

Vetor com dois elementos contendo no primeiro elemento a quantidade de dias de férias, e no segundo a data de início do período aquisitivo.

Exemplo:

aDados := { nDiasAnt, dData }

Onde:

nDiasAnt: Dias de férias antecipadas

dData: Data de início do período aquisitivo.

**05. Tabelas Utilizadas:**

* Na execução do cálculo de Provisão, o sistema trabalha com a tabela temporária TPR que é alimentada com os dados do cadastro de Funcionários (SRA).  
    
  Portanto, esta tabela pode ser utilizada se houver a necessidade de avaliar algum funcionário durante o cálculo. Segue a relação dos principais campos da tabela TPR:  
    
  **TPR->PR\_FILIAL***(Filial)*  
  **TPR->PR\_MAT***(Matrícula)*  
  **TPR->PR\_NOME***(Nome)*  
  **TPR->PR\_CC***(Centro de Custo)*  
  **TPR->PR\_ADMISSA***(Data de Admissão)*  
  **TPR->PR\_DEMISSA***(Data de Demissão)*

**Saiba Mais:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=642630397>
