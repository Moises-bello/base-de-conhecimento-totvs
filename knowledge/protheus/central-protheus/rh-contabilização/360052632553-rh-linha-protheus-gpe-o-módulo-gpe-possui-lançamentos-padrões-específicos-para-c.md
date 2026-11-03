---
article_id: 360052632553
category: RH - Contabilização
content_hash: 0bb3652f0d578779e44b461cc5c5c0c160811a74370c532fbc42d946b7f849ab
fetched_at: '2026-06-28T22:43:46.011942+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - O Módulo GPE possui lançamentos padrões específicos
  para cada verba
type: support-article
updated_at: '2025-07-30T20:48:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052632553-RH-Linha-Protheus-GPE-O-M%C3%B3dulo-GPE-possui-lan%C3%A7amentos-padr%C3%B5es-espec%C3%ADficos-para-cada-verba
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33832492632599)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**O Módulo GPE possui lançamentos padrões específicos para cada verba?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Os lançamentos padrões do módulo Gestão de Pessoal devem ter códigos entre A01 e Z99 e amarração verba x lançamento padrão definida pelo próprio usuário.

De acordo com a fórmula criada e a regra de negócio da empresa é possível ter apenas um lançamento padrão para todo o processo de contabilização da folha de pagamento.

O arquivo SRZ (Resumo da Folha) contém os valores das verbas por centro de custo e podem ser informadas no lançamento padrão.

**Exemplos:**

**SRZ -> RZ-VAL** = Valor indica o valor da verba.

**SRZ -> RZ-CC =** Indica o Centro de Custo da Verba.

**SRZ -> RZ\_Tipo** = FL para Folha, 13 para 13º salário, PF Provisão Férias e PD Provisão 13º salário.  
  
**SRZ->RZ\_PD =** valor indica o código da verba  
  
**SRZ->RZ\_ITEM =** caso utilize contabilização por item

**SRZ->RZ\_CLVL =** Caso utilize contabilização por classe e valor

**Importante:**

A tabela a seguir apresenta alguns exemplos de códigos x lançamentos, entretanto **esta relação não é fixa.** Para a contabilização das verbas da folha de pagamento, a atribuição dos códigos é determinada **pelo próprio usuário, dentro da faixa A00-Z99.**

**Lançamentos Padronizados**

|  |  |
| --- | --- |
| **Código** | **Lançamento** |
| A01 | Salários a Pagar |
| A02 | Férias |
| A03 | Salário Família |
| A04 | Salário Maternidade |
| A05 | Pró-Labore |
| B01 | INSS Empregados |
| B02 | IRRF |
| B03 | Assistência Médica |
| B04 | Contribuição Sindical |
| B05 | Faltas |
| B06 | Aviso Prévio (Desconto) |
| B07 | Outros Descontos |
| B08 | Pensão Alimentícia |
| B09 | Vale-Transporte |
| B10 | Desc. Insuficiência de Saldo |
| C01 | INSS Empresa |
| C02 | FGTS |
| C03 | Provisão de Férias |
| C04 | Encargos Provisão de Férias |
| C05 | Provisão de 13° salário |
| C06 | Encargos de Provisão de 13° salário |

**Saiba Mais:**[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)
