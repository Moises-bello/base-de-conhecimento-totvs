---
article_id: 18135505861911
category: RH - Férias
content_hash: 83dd8ea16a2d4ce339e62dece1807d6d1cadcd98857ff6d22a2ff2ee18d705ae
fetched_at: '2026-06-28T22:43:59.409752+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GPM060CO - Define se calcula ou
  não Férias Programadas/Coletivas para funcionário
type: support-article
updated_at: '2025-09-02T17:10:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18135505861911-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GPM060CO-Define-se-calcula-ou-n%C3%A3o-F%C3%A9rias-Programadas-Coletivas-para-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18135528973975) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Ponto-de-Entrada: GPM060CO - Define se calcula ou não Férias Programadas/Coletivas para funcionário  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Ponto-de-Entrada: **GPM060CO - Define se calcula ou não Férias Programadas/Coletivas para funcionário**

Versões: Microsiga\_Protheus12.1.7  
Compatível Países: Todos  
Sistemas Operacionais: Todos  
Compatível às Bases de Dados: Todos

**Descrição**

O Ponto de Entrada **GPM060CO** define **se o cálculo de Férias Programadas/Coletivas será executado ou não** de acordo com o **filtro informado** no ponto de entrada.

Programa Fonte  
.PRW  
Sintaxe  
GPM060CO - Defini se calcula ou não Férias Programadas/Coletivas para funcionário ( [ PARAMIXB ] )

**Parâmetros**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | PARAMIXB |  |  | Vetor |  |  | PARAMIXB[1] := {cFiltroSRA} |  |  |  |  |  |  |  |  |  |  |

**Retorno**

aDados[1] = Define se executa cálculo ou não, retornar .T. ou .F.

aDados[2] => Novo filtro.

Observações

No vetor PARAMIXB[1] é passado variável de controle de filtro para execução do cálculo de Férias Programadas/Coletibas.

PARAMIXB[1] == "RA\_NACIONA" + " = '" + 10 + "'"

**Exemplos**

#Include '[Protheus.ch](http://protheus.ch/)'

User Function GPM060CO()  
Local cFiltro := PARAMIXB[1]  
Local aDados := Array(2)

cFiltro += " .AND. RA\_MAT = '000001'"

Alert("Ponto de Entrada GPM060CO está sendo executada - Cálculo liberado apenas para matrícula 000001.")  
  
aDados[1] := .T.  
aDados[2] := cFiltro

Return( aDados )

![GPM060CO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18137069301911)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Pontos de Entrada da rotina de Cálculo de Férias - GPEM030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053133974-RH-Linha-Protheus-GPE-Pontos-de-Entrada-da-rotina-de-C%C3%A1lculo-de-F%C3%A9rias-GPEM030)  
[RH - Linha Protheus - GPE - Pontos de Entrada disponíveis na rotina GPEM060 - Férias Coletivas/Programadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002601062-RH-Linha-Protheus-GPE-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-GPEM060-F%C3%A9rias-Coletivas-Programadas)

[GPM060CO - Define se calcula ou não Férias Programadas/Coletivas para funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=244914856)
