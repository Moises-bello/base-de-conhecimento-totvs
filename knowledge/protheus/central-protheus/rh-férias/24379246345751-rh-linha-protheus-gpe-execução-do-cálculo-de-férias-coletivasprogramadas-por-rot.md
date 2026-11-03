---
article_id: 24379246345751
category: RH - Férias
content_hash: 15d656c4e8e5c5ffe430436bc5e9b8751d8038779ca88f2fff49156ccbb76c0f
fetched_at: '2026-06-28T22:43:59.360297+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Execução do Cálculo de Férias Coletivas/Programadas
  por Rotina Automática - GPEM060
type: support-article
updated_at: '2025-09-02T17:18:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24379246345751-RH-Linha-Protheus-GPE-Execu%C3%A7%C3%A3o-do-C%C3%A1lculo-de-F%C3%A9rias-Coletivas-Programadas-por-Rotina-Autom%C3%A1tica-GPEM060
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24379240938263) Tempo aproximado para leitura: **00:01:30 min** **Dúvida** Execução do Cálculo de Férias Coletivas/Programadas por Rotina Automática - GPEM060  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 11

**Solução**Para realização do cálculo automático de Férias Coletivas/Programadas - GPEM060, será necessária a utilização de uma ***User Function***.  
É importante se atentar ao tipo do calculo que será executado, e essa informação é definida pela variável **nColPro,** que deve ser declarada com o escopo***Private**.*Outro ponto importante,é o filtro passado para a rotina, nesse exemplo contido na variável **cFiltro**, deve ser uma expressão em AdvPL com um retorno lógico, possibilitando filtrar as filiais ou matrículas que deseja calcular, por exemplo:

`#INCLUDE "TOTVS.CH"`

`#INCLUDE "TBICONN.CH"`

`/*/{Protheus.doc} User Function ExeFer060`

`Executa o cálculo de férias coletivas/programadas`

`@type User Function`

`@author Cícero Alves`

`@since 07/12/2020`

`@see https://tdn.totvs.com/x/D3JkIg`

`/*/`

`User Function ExeFer060()`

`Local aLogAuto      := {}`

`Local cFiltro       :=``"SRA->RA_FILIAL == 'D MG 02 ' "` `// Filtro utilizado no cálculo`

`Private lMsErroAuto := .F.`

`// Variável utilizada pela rotina define se o cálculo será de férias coletivas ou programadas`

`Private nColPro     := 1``// 1 - Coletivas / 2 - Programadas`

`PREPARE ENVIRONMENT EMPRESA``"T1"` `FILIAL``"D MG 02 "` `MODULO``"GPE"`

`// Alterar nome da função para as validações da rotina`

`SetFunName(``"GPEM060"``)`

`// Reinicializa as variáveis Static das rotinas de cálculo`

`// Necessário quando executado mais de um cálculo em sequência`

`RstGpm060()`

`RstGpm030()`

`If nColPro == 1``// Férias Coletivas`

`// Carrega as variáveis MV_PAR`

`Pergunte(``"GPM060"``, .F.)`

`// Altera os parâmetros do cálculo`

`SetMVValue(``"GPM060"``,``"MV_PAR01"``,``"00298"``)``// Processo`

`SetMVValue(``"GPM060"``,``"MV_PAR02"``, 1)``// Ordem 1 - Matricula / 2 - Centro de Custo`

`SetMVValue(``"GPM060"``,``"MV_PAR03"``, 20)``// Dias Ferias Colet.?`

`SetMVValue(``"GPM060"``,``"MV_PAR04"``, 0)``// Dias Abono Colet.?`

`SetMVValue(``"GPM060"``,``"MV_PAR05"``, 1)``// Func. Menos Um Ano? 1- Dias coletiva / 2- Dias de direito`

`SetMVValue(``"GPM060"``,``"MV_PAR06"``, cTOd(``"17/12/2018"``))``// Início Férias Coletivas?`

`SetMVValue(``"GPM060"``,``"MV_PAR07"``, cTOd(``"17/12/2018"``))``// Data Aviso Ferérias Coletivas?`

`SetMVValue(``"GPM060"``,``"MV_PAR08"``, cTOd(``"17/12/2018"``))``// Data Pagamento Férias Coletivas?`

`SetMVValue(``"GPM060"``,``"MV_PAR09"``, 1)``// Media do Mes Atual? 1- Sim / 2- Não`

`SetMVValue(``"GPM060"``,``"MV_PAR10"``, 3)``// Calcular p/ periodo? 1- Vencido / 2- A vencer / 3- Ambos`

`SetMVValue(``"GPM060"``,``"MV_PAR11"``, 0)``// Percentual 13.Salario?`

`SetMVValue(``"GPM060"``,``"MV_PAR12"``, 1)``// Dt Pagto Informada?  1-Não, 2-Sim`

`// Grava os novos valores na SX1`

`Pergunte(``"GPM060"``, .F.)`

`Else``// Férias Programadas`

`// Carrega as variáveis MV_PAR`

`Pergunte(``"GPM062"``, .F.)`

`SetMVValue(``"GPM062"``,``"MV_PAR01"``,``"00298"``)``// Processo`

`SetMVValue(``"GPM062"``,``"MV_PAR02"``, 1)``// Ordem 1 - Matricula / 2 - Centro de Custo`

`SetMVValue(``"GPM062"``,``"MV_PAR03"``, 2)``// Dt Pagto Informada? 1- Sim / 2- Não`

`SetMVValue(``"GPM062"``,``"MV_PAR04"``, cTOd(``"27/09/2018"``))``// Dt Pagto Fer. Prog?`

`SetMVValue(``"GPM062"``,``"MV_PAR05"``, cTOd(``"01/10/2018"``))``// Dt Inicio Prog. De?`

`SetMVValue(``"GPM062"``,``"MV_PAR06"``, cTOd(``"31/10/2018"``))``// Dt Inicio Prog. Ate?`

`SetMVValue(``"GPM062"``,``"MV_PAR07"``, 2)``// Média do Mes Atual? 1- Sim / 2- Não`

`SetMVValue(``"GPM062"``,``"MV_PAR08"``, 3)``// Calcular p/ periodo? 1 - Vencido / 2 - A vencer / 3 - Ambos`

`// Grava os novos valores na SX1`

`Pergunte(``"GPM062"``, .F.)`

`EndIf`

`// Executa a rotina`

`MSExecAuto( {|x, y| GPEM060(x, y)}, 2, cFiltro)``// 2 é a posição da opção Cálculo no menu da rotina (aRotina)`

`If !lMsErroAuto`

`ConOut(``"Cálculo de férias efetuado."``)`

`Else`

`If IsBlind()``// Sem Interface`

`aLogAuto := MostraErro(``'Null'``)`

`varinfo(``"aLogAuto"``, aLogAuto)`

`Else`

`MostraErro()`

`EndIf`

`EndIf`

`Return`

**Saiba Mais:**[DT - Execução do Cálculo de Férias por Rotina Automática](https://tdn.totvs.com/pages/releaseview.action?pageId=577008143)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Página Centralizadora - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)  
[RH - Linha Protheus - GPE - Execução do Cálculo de Férias por Rotina Automática - GPEM030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24378831659031-RH-Linha-Protheus-GPE-Execu%C3%A7%C3%A3o-do-C%C3%A1lculo-de-F%C3%A9rias-por-Rotina-Autom%C3%A1tica-GPEM030)  
[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
