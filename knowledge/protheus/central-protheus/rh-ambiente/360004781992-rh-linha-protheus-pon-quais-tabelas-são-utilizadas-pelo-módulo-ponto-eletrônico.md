---
article_id: 360004781992
category: RH - Ambiente
content_hash: 087dba4fa2d74f5ef0d60f2423a0cf926d4ff8fa32936cd7ede84c503c352cf3
fetched_at: '2026-06-28T22:44:55.967241+00:00'
product: protheus
section_id: 32302375681815
source: central-protheus
title: RH - Linha Protheus - PON - Quais tabelas são utilizadas pelo módulo Ponto
  Eletrônico
type: support-article
updated_at: '2025-06-16T12:19:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004781992-RH-Linha-Protheus-PON-Quais-tabelas-s%C3%A3o-utilizadas-pelo-m%C3%B3dulo-Ponto-Eletr%C3%B4nico
---

**Dúvida**Quais **tabelas são utilizadas** pelo módulo **Ponto Eletrônico**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O módulo **Ponto Eletrônico** (X2\_MODULO = **16**) é proprietário das seguintes tabelas:

|  |  |  |  |
| --- | --- | --- | --- |
| **Arquivo/Tabela** | **Descrição** | **Chave única (X2\_UNICO)** | Nome da Rotina |
| **AC0** | Cadastro de Feriado | AC0\_FILIAL+AC0\_CODIGO |  |
| **RF0** | Pré-Abonos |  | PONA350 |
| **RF2** | Tabela de Horário Padrão |  |  |
| **RF3** | Jornada | RF3\_FILIAL+RF3\_JORN |  |
| **RF4** | Horário - Item | RF4\_FILIAL+RF4\_HOR+RF4\_DIA |  |
| **RF5** | Tipo de Dia - Item | RF5\_FILIAL+RF5\_TIPO+RF5\_DIA |  |
| **RF6** | Cabeçalho do Calendário |  |  |
| **RF7** | Item do Calendário |  |  |
| **RF8** | Horário - Cabeçalho | RF8\_FILIAL+RF8\_HOR |  |
| **RF9** | Tipo de Dia - Cabeçalho | RF9\_FILIAL+RF9\_TIPO |  |
| **RFA** | Tabela de Pré-Leitura |  |  |
| **RFB** | Cabeçalho de Pré-Leitura |  |  |
| **RFD** | Motivo de Manutenção | RFD\_FILIAL+RFD\_CODIGO+RFD\_APLIC+RFD\_TIPO | PONA430 |
| **RFE** | Pré-Leitura |  |  |
| **RFF** | Pré-ACJEF |  |  |
| **RFG** | Acumulado de Pré-ACJEF |  |  |
| **RFH** | Acumulado de Pré-Leitura |  |  |
| **RFK** | Apontamentos Informados | RFK\_FILIAL+RFK\_MAT+DTOS(RFK\_DATA)+RFK\_PD+RFK\_PROCES+RFK\_PERIOD+RFK\_ROTEIR+RFK\_NUMPAG+RFK\_PDI+STR(RFK\_HRINI)+STR(RFK\_HRFIM) |  |
| **RFL** | Jornadas | RFL\_FILIAL+RFL\_JORN |  |
| **RFM** | Itens da Exceção | RFM\_FILIAL+RFM\_CODEXC |  |
| **RR0** | Feriados | RR0\_FILIAL+DTOS(RR0\_DATA)+RR0\_CODCAL |  |
| **RS3** | Tab Auxiliar Solicitações Portais | RS3\_FILIAL+RS3\_CODIGO+RS3\_MAT |  |
| **RS4** | Controle de Espelhos de Ponto | RS4\_FILIAL+RS4\_MAT+RS4\_PER+RS4\_CODEBA |  |
| **SP0** | Relógio de Ponto | P0\_FILIAL+P0\_RELOGIO | PONA030 |
| **SP1** | Refeições | P1\_FILIAL+P1\_CODREF+P1\_SEQ | PONA250 |
| **SP2** | Exceções | P2\_FILIAL+P2\_MAT+P2\_CC+P2\_TURNO+DTOS(P2\_DATA)+P2\_TIPODIA | PONA090 |
| **SP3** | Feriados | P3\_FILIAL+DTOS(P3\_DATA) | PONA020 |
| **SP4** | Tipos de Horas Extras |  | PONA070 |
| **SP5** | Movimento Refeitório |  | PONA150 |
| **SP6** | Motivo Abono/Justificativa | P6\_FILIAL+P6\_CODIGO | PONA050 |
| **SP8** | Movimento de Marcações |  | PONA040 |
| **SP9** | Eventos | P9\_FILIAL+P9\_CODIGO | PONA100 |
| **SPA** | Regras de Apontamento | PA\_FILIAL+PA\_CODIGO | PONA060 |
| **SPB** | Resultados do Período |  | PONA170 |
| **SPC** | Apontamentos |  | PONA130 |
| **SPD** | Arredondamentos |  | PONA110 |
| **SPE** | Crachás Provisórios | PE\_FILIAL+PE\_MAT+DTOS(PE\_DATAINI) | PONA120 |
| **SPF** | Transferência de Turno | PF\_FILIAL+PF\_MAT+DTOS(PF\_DATA) | PONA160 |
| **SPG** | Histórico de Marcações |  | PONA040 |
| **SPH** | Histórico de Apontamentos |  | PONA190 |
| **SPI** | Banco de Horas |  | PONA200 |
| **SPJ** | Horário Padrão | PJ\_FILIAL+PJ\_TURNO+PJ\_SEMANA+PJ\_DIA | PONA080 |
| **SPK** | Eventos Abonados |  | PONA130 |
| **SPL** | Histórico de Resultados |  | PONA170 |
| **SPM** | Tipos de Refeições | PM\_FILIAL+PM\_TIPOREF | PONA260 |
| **SPN** | Histórico Movimento Refeitório |  |  |
| **SPO** | Períodos de Apontamento | PO\_FILIAL+DTOS(PO\_DATAINI) | PONA290 |
| **SPP** | Mensagens Acesso | PP\_FILIAL+PP\_CODMSG |  |
| **SPQ** | Ocorrências Acesso | PQ\_FILIAL+PQ\_CODOCOR |  |
| **SPR** | Itens de Ocorrências Acesso | PR\_FILIAL+PR\_CODOCOR+PR\_ITOCOR+PR\_TPMARCA |  |
| **SPS** | Programação Ocorrências Acesso |  |  |
| **SPT** | Horas Extras Autorizadas | PT\_FILIAL+PT\_MAT+DTOS(PT\_DATAREF)+DTOS(PT\_DATA)+STR(PT\_HORINI,5,2) | PONA300 |
| **SPU** | Gráfico RH | PU\_FILIAL+PU\_CODIGO | PONA320 |
| **SPV** | Itens do Gráfico RH | PV\_FILIAL+PV\_CODIGO+PV\_GRUPO+PV\_DADO | PONA320 |
| **SPW** | Visitantes | PW\_FILIAL+PW\_VISITA | PONA330 |
| **SPX** | Grupo de Série | PX\_FILIAL+PX\_CODIGO+PX\_GRUPO | PONA320 |
| **SPY** | Movimento de Visitas | PY\_FILIAL+PY\_VISITA+DTOS(PY\_DTVISIT)+PY\_CRACHA+PY\_NUMERO | PONA330 |
| **SPZ** | Acessos Visitantes |  | PONA330 |

**Saiba Mais**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
