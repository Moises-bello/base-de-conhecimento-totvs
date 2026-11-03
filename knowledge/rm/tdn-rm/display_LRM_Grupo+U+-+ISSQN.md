---
content_hash: dac6c37fa7292714d88325c8f0cf5e6a57c1646ede70e595377d19133b701797
fetched_at: '2026-06-29T00:12:10.688133+00:00'
page_id: '953003411'
product: rm
source: tdn-rm
title: Grupo U - ISSQN
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+U+-+ISSQN
version: 4
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo U - ISSQN** | | | | | | | | | | | | |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocorrência | Tamanho | Observação | Campo de Origem | Campo da Aplicação | Mais Informações |
| 319 | U01 | ISSQN | Grupo ISSQN | CG | M01 |  | 0-1 |  | Campos para cálculo do ISSQN na NF-e conjugada, onde há a prestação de serviços sujeitos ao ISSQN e fornecimento de peças sujeitas ao ICMS. Grupo ISSQN é mutuamente exclusivo com os grupos ICMS, IPI e II, isto é se ISSQN for informado os grupos ICMS, IPI e II não serão informados e vice-versa (v2.0). |  |  |  |
| 320 | U02 | vBC | Valor da Base de Cálculo do ISSQN | E | U01 | N | 1-1 | 13v2 |  | TTRBMOV.BASEDECALCULO |  |  |
| 321 | U03 | vAliq | Alíquota do ISSQN | E | U01 | N | 1-1 | 3v2-4 |  | TTRBMOV.ALIQUOTA |  |  |
| 322 | U04 | vISSQN | Valor do ISSQN | E | U01 | N | 1-1 | 13v2 |  | TTRBMOV.VALOR |  |  |
| 323 | U05 | cMunFG | Código do município de ocorrência do fato gerador do ISSQN | E | U01 | N | 1-1 | 7 | Informar o município de ocorrência do fato gerador do ISSQN. Utilizar a Tabela do IBGE (Anexo IX - Tabela de UF, Município e País). Nota 1: Não vincular com o município do fato gerador de ICMS (id:B12), ou com o município do emitente (id:C10) ou do destinatário (id:E10). Nota 2: Pode ser informado 9999999 se a prestação de serviço for no Exterior. | DCODIFICACAOMUNICIPIO.CODIGO |  |  |
| 324 | U06 | cListServ | Item da Lista de Serviços | E | U01 | C | 1-1 | 5 | Informar o Item da lista de serviços em que se classifica o serviço no padrão :  O código de serviço federal deve ser informado de acordo com a LC 116/2003, ou seja, SEM zeros não significativos à esquerda. | TPRDFISCAL.CODIGOSERVICOFEDERAL |  |  |
| 324a | U07 | vDeducao | Valor dedução para redução da Base de Cálculo | E | U01 | N | 0-1 | 13v2 |  | TMOVFISCAL.VLRDEDUCAOMATERIAL  + TMOVFISCAL.VLRDEDCAOSUBEMPREITADA + TMOVFISCAL.VLRDEDUCAOOUTRO |  |  |
| 324b | U08 | vOutro | Valor outras retenções | E | U01 | N | 0-1 | 13v2 | Valor declaratório |  |  | NÃO SERÁ GERADO |
| 324c | U09 | vDescIncond | Valor desconto incondicionado | E | U01 | N | 0-1 | 13v2 |  | TITMMOV.RATEIODESC + TITMMOV.VALORDESC |  |  |
| 324d | U10 | vDescCond | Valor desconto condicionado | E | U01 | N | 0-1 | 13v2 |  | TITMMOV.VALORDESCCONDICONALITM |  |  |
| 324f | U11 | vISSRet | Valor retenção ISS | E | U01 | N | 0-1 | 13v2 | Valor declaratório | TTRBMOV.VALOR |  | Se Tipo de Recolhimento do ISS for = a Retido na Fonte ou Retido na Fonte Deduzido então TTRBMOV.VALOR Senão Não será Gerado. |
| 324g | U12 | indISS | Indicador da exigibilidade do ISS | E | U01 | N | 1-1 | 2 | 1=Exigível, 2=Não incidência; 3=Isenção; 4=Exportação; 5=Imunidade; 6=Exigibilidade Suspensa por Decisão Judicial; 7=Exigibilidade Suspensa por Processo Administrativo; |  |  | Se Tipo de Recolhimento do ISS igual a "Nenhum" Então: "2" - Não incidência Senão Se o Tipo de Recolhimento do ISS é “Isento” Então: “3” – Isenção Senão Se CFOP Iniciada com "7" Então: "4" - Exportação Senão Se tipo de recolhimento do ISS igual a Imune Então: “5” – Imunidade Senão Se Tipo Recolhimento ISS igual a Deposito Judicial Então: “6” - Exigibilidade suspensa por decisão judicial Senão Então: “1” – Exigível Exigibilidade Suspensa por Processo Administrativo Não será tratado |
| 324h | U13 | cServico | Código do serviço prestado dentro do município | E | U01 | C | 0-1 | 1-20 |  | DTRBMUNICIPIOPRB.CODIGOSERVICO |  |  |
| 324i | U14 | cMun | Código do Município de incidência do imposto | E | U01 | N | 0-1 | 7 | Tabela do IBGE. Informar "9999999" para serviço fora do País | cMunFG |  |  |
| 324j | U15 | cPais | Código do País onde o serviço foi prestado | E | U01 | N | 0-1 | 4 | Tabela do BACEN. Informar somente se o município da prestação do serviço for "9999999". |  |  | NÃO SERÁ GERADO |
| 324k | U16 | nProcesso | Número do processo judicial ou administrativo de suspensão da exigibilidade | E | U01 | C | 0-1 | 1-30 | Informar somente quando declarada a suspensão da exigibilidade do ISSQN. | DPROCESSOJUDICIAL.NUMERO |  |  |
| 324l | U17 | indIncentivo | Indicador de incentivo Fiscal | E | U01 | N | 1-1 | 1 | 1=Sim; 2=Não; |  |  | Será levado Fixo "2=Não" |
