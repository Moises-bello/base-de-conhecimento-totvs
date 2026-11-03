---
content_hash: b0d93ad1dd8ee807f7618e707aa40a93e1f60a799141b98bd06045714a96ad16
fetched_at: '2026-06-29T00:08:56.086871+00:00'
page_id: '351376165'
product: rm
source: tdn-rm
title: Evento S-1050
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1050
version: 10
---

Leiautestrue2Leiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideHorContratual | codHorContrat |  |  | Caso horário seja por INTERVALO retorna o seguinte valor: ("I" + "|" + AHORARIO.CODIGO + "|" + AINDHOR.INDINICIOHOR);  Caso horário seja por JORNADA retorna o valor do campo ("J" + "|" + AHORARIOJORNADA.CODHORARIO + "|" + AINDICEJORNADA.INDICE) ; |
| ideHorContratual | iniValid |  |  | Se o tipo da operação for Carga Inicial, retorna a data de obrigatoriedade parametrizada, caso contrário, retorna a competência atual.. Caso seja incluído manualmente pela fila de eventos assume a competência Informada |
| ideHorContratual | fimValid |  |  |  |
| dadosHorContratual | hrEntr |  |  | Caso horário seja por INTERVALO retorna o valor do campo AJORHOR.BATINICIO;  Caso horário seja por JORNADA não existe esse informação; |
| dadosHorContratual | hrSaida |  |  | Caso horário seja por INTERVALO retorna o valor do campo AJORHOR.BATFIM;  Caso horário seja por JORNADA não existe esse informação; |
| dadosHorContratual | durJornada |  |  | Retornará sempre o total de horas de trabalho da jornada; |
| dadosHorContratual | perHorFlexivel |  |  | Caso horário seja por INTERVALO e AHORARIO.TIPOHOR seja "2 - Intervalo Horário Variavel" retorna "S" caso contrário, retorna "N";  Caso horário seja por JORNADA não existe esse informação; |
| horarioIntervalo | tpInterv |  |  | Caso o tipo de horário "Rigido" (AHORARIO.TIPOHOR = 0) retorna "1 - Intervalo de Horário Fixo";  Caso contrário retorna "2 - Intervalo de Horário Variável". |
| horarioIntervalo | durInterv |  |  | Caso horário seja por INTERVALO retorna o valor através de cálculos no campo ABATHOR.BATIDA em minutos;  Caso horário seja por JORNADA não existe esse informação; |
| horarioIntervalo | iniInterv |  |  | Caso horário seja por INTERVALO retorna o valor através de cálculos no campo ABATHOR.BATIDA em minutos;  Caso horário seja por JORNADA não existe esse informação; |
| horarioIntervalo | termInterv |  |  | Caso horário seja por INTERVALO retorna o valor através de cálculos no campo ABATHOR.BATIDA em minutos;  Caso horário seja por JORNADA não existe esse informação; |
| novaValidade | iniValid |  |  |  |
| novaValidade | fimValid |  |  | Campo será preenchido com a data de encerrado informada ao executar o processo de Encerrar Atividades da Empresa. |
