---
content_hash: 9b03b3809ba6bb740001974302d65d9807a04f1a9fdf26b8b4455ed27098dd08
fetched_at: '2026-06-29T00:11:21.410340+00:00'
page_id: '695606689'
product: rm
source: tdn-rm
title: Tratamento em Politraumatizados IAMSPE
type: documentation
url: https://tdn.totvs.com/display/LRM/Tratamento+em+Politraumatizados+IAMSPE
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

sumarioVisão Geral

## **01. VISÃO GERAL**

De acordo com o manual IAMSPE, as cirurgias em politraumatizados são cirurgias múltiplas ou procedimentos sequenciais procedidos em indivíduo que sofre traumatismo seguido de lesões que, ao acometer múltiplos órgãos (fígado, baço, pulmão etc.) ou sistemas corporais (circulatório, nervoso, respiratório, musculoesquelético, etc.), podem ou não pôr em risco a vida, pela gravidade de uma ou mais lesões.

Sob a denominação de politraumatizados, estão as internações de pacientes vítimas de causas externas.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

1 - Na Tabela de Preço deste convênio, o código 39.000.00.1 – POLITRAUMATIZADO tem o valor zero.

2 - Os únicos procedimentos clínicos aceitos para cobrança de Politraumatizado são: Traumatismo Cranioencefálico e Concussão Cerebral.

**3 - Percentual Profissional no Lançamentos de Honorários Médicos:**

Ateção

**O recálculo da redução de percentuais de SH e SADT somente será executado se houver lançado no mínimo 2 Prestadores com a Função “Cirurgião” nos procedimentos de Honorários Médicos**

Componentes Serviços

3.1 O componente **Serviço Hospitalar (SH)** será remunerado em **percentual decrescente** de valores, na ordem em que forem registrados na tela Procedimentos Realizados, conforme tabela abaixo:

|  |  |
| --- | --- |
| 1° procedimento | 100% |
| 2° procedimento | 100% |
| 3° procedimento | 75% |
| 4° procedimento | 75% |
| 5° procedimento | 50% |

3.2 O componente **Serviços Auxiliares de Diagnose e Terapia (SADT)** seguem o mesmo percentual aplicado para o **Serviço Hospitalar (SH)**.

3.3 Os componentes **Serviços Profissionais (SP)** recebem remuneração de **100%** dos valores para todos os procedimentos realizados e autorizados.

**OBS: O Cirurgião reparte o valor SP com seus auxiliares**

4 – RM.EXE : Como calcular o percentual SH, SP, SADT ao lançar os Honorários Médicos na conta do paciente:

**4.1 - No Registro de Atendimento, em Guia de Autorização:**

Lançar uma guia contendo o código de procedimento **39.000.00.1 POLITRAUMATIZADO**

Com esta guia de autorização lançada, o sistema irá entender que o atendimento do paciente trata-se de Politraumatizado, então os procedimentos lançados na Elaboração de Contas seguirá este cálculo de percentual.

**4.2 Elaboração de Contas – aba Honorários**

Na Elaboração de contas, o terceiro procedimento lançado para um cirurgião será calculado percentual de 75% sobre o valor SH e no valor de SP continua em 100% da tabela de preço IAMSPE. Seguindo os percentuais citados no item 3.1 acima.

Ao salvar honorário ou encerrar parcial, o sistema já recalcula os valores SH, SP, SADT específico para o convênio IAMSPE, somente se existir 2 prestadores com a função “Cirurgião”, aplicando as regras de faturamento do convênio.

Os valores dos procedimentos e percentuais SP, SH, SADT, anestesista encontram-se no menu “Cadastros | Faturamento | Tabela de Procedimetos e Serviços | Anexos | IPSEMG/IAMSPE – Valores”

Exemplo de lançamento de Honorário Médico: 

Lançar uma guia de autorização com o procedimento39.00.0001 na Parcial 4, ou seja, na parcial onde será lançado o honorário médico.

Tabela de Preço IAMSPE

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| PROCEDIMENTO | DESCRIÇÃO | SH | SP | SADT | ANESTESISTA | VLRTOTAL |
| 39001032 | REDUCAO CIRURGICA DA FRATURA DA COSTELA | 562,6600 | 281,8000 | 29,6000 | 97,5000 | 971,5600 |
| 39001083 | AMPUTACAO DO ANTEBRACO | 656,1800 | 351,0000 | 21,9000 | 97,5000 | 1126,5800 |
| 39001105 | AMPUTACAO AO NIVEL DE RAIO DA MAO | 263,3400 | 152,1000 | 5,6000 | 97,5000 | 518,5400 |

Percentuais aplicados:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| PROCEDIMENTO | DESCRIÇÃO | SH | SP | SADT | ANESTESISTA | VLRTOTAL |
| 1º Procedimento = 39001032 | REDUCAO CIRURGICA DA FRATURA DA COSTELA | 100% = 562,6600 | 100% = 281,8000 | 100% = 29,6000 | 97,5000 | 971,5600 |
| 2º Procedimento = 39001083 | AMPUTACAO DO ANTEBRACO | 100% = 656,1800 | 100% = 351,0000 | 100% = 21,9000 | 97,5000 | 1126,5800 |
| 3º Procedimento = 39001105 | AMPUTACAO AO NIVEL DE RAIO DA MAO | 75% de 263,3400 = 197,505 | 100% = 152,1000 | 75% de 5,6000 = 4,20 | 97,5000 | 518,5400 -> foi para 353,805 |

Na Elaboração de Contas do Paciente: Reduzido percentual SH no terceiro procedimento
