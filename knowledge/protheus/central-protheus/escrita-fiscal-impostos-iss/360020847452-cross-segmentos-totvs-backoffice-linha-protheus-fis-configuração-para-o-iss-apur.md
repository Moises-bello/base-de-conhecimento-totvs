---
article_id: 360020847452
category: Escrita Fiscal - Impostos - ISS
content_hash: 7f3104cf3eb468cab49d092bec58b90a7c81645eb548112709717e00272bc053
fetched_at: '2026-06-28T22:39:35.117883+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Configuração para
  o ISS Apurado- (Faturamento)
type: support-article
updated_at: '2022-03-28T18:17:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020847452-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-para-o-ISS-Apurado-Faturamento
---

**Dúvida**Como realizar parametrização para apuração de ISS (Faturamento)?

**Ambiente**Protheus - Pedido de Venda - A partir da versão 11.80  
  
**Solução**Para realizar calculo de **Apuração de ISS,** realize os seguintes passos:

**NATUREZA**

*Calcula ISS (ED\_CALCISS)* = NAO

Caso deixe *Calcula ISS (ED\_CALCISS)* = SIM, será gerado um título de ISS no contas a pagar por nota fiscal  emitida.

**TES**

*Calculo ISS (F4\_ISS)* = Sim

**Fiscal ISS (F4\_LFISS)** = Tributado/ Outros/ Isento

**PRODUTO**

*Aliq. ISS (B1\_ALIQISS)* = Informe a alíquota - Caso este campo esteja sem preenchimento, será válido o conteúdo do parâmetro MV\_ALIQISS

*Cód. Serv. ISS (B1\_CODISS)* = Informe o código de serviço do ISS - Caso não haja o código referente ao serviço deve ser incluído na tabela 60 do Configurador.

**CLIENTE**

*Recolhe ISS (A1\_RECISS)* *=* NÃO - o ISS poderá ser pago na apuração mensal.

*ISS no preço (A1\_INCISS**)* = SIM - Não agrega o valor de ISS à base de cálculo.

*F.Ret.ISS (A1\_FRETISS)**=* 1=Considera valor mínimo (MV\_VRETISS) ou 2=Sempre retém - Informe se o cliente deve respeitar o valor mínimo do ISS.

**Parâmetros referentes à retenção de ISS:**

MV\_DESCISS - Informa se o ISS deve ser descontado do valor do título financeiro, caso o cliente for responsável pelo recolhimento. Conteúdo .T. = verdadeiro ou .F. = falso.

MV\_MRETISS - Modo de retenção do ISS nas aquisições de serviços. Conteúdo 1 = na emissão do titulo principal.  2 = na baixa do título principal.

MV\_VRETISS - Valor mínimo para dispensa de retenção de ISS.

MV\_PRETISS - Definição do responsável pelo recolhimento do ISS por parte do Prestador ou Tomador do Serviço conforme limite conforme regulamento do ISS do município de Porto Alegre/RS.

MV\_MODRISS - Indica qual o modo de retenção do ISS. Conteúdo 1 - por título 2 - mensal vencimento 3 - por base.

MV\_TPNFISS - Caso esse parâmetro esteja sem conteúdo, obrigatoriamente o Cód. de Serviço de ISS deve estar preenchido no cadastro de produto para o correto cálculo do ISS. Informe os tipos de documentos que deverão realizar o calculo de ISS somente pela Natureza. Utilize: E - para entrada e S - para saída. = E.

MV\_VENCISS - Define o tipo de vencimento de ISS. Conteúdo E=Emissão ou Q=Quinzenal/ Emissão ou V=Vencimento ou F = Se a data de emissão for menor que 15 (primeira quinzena) a data de vencimento será 15  somados ao conteúdo

MV\_DIAISS (considerando o primeiro dia do mês na conta), se a data de emissão for maior que 15 (segunda quinzena) será no dia informado no MV\_DIAISS do mês subsequente.

MV\_DIAISS - Dia padrão para gerar os títulos de ISS.

MV\_DEDISS - Define o momento do tratamento da dedução do ISS. Conteúdo 1= Na baixa. 2= Na emissão.

MV\_ALIQISS - Define a alíquota do ISS para cada município, Ex: 5.00%.

MV\_ISS - Define a natureza dos títulos de ISS (Padrão: "ISS").

MV\_MUNIC - Indica o fornecedor do ISS. O Sistema gera títulos a pagar contra o município determinado neste parâmetro, no momento da inclusão do título a receber, no módulo Financeiro.

MV\_APURISS - Define a natureza a ser utilizada na geração do título a pagar por meio da Apuração de ISS. Caso este parâmetro não esteja configurado, é assumido como padrão o conteúdo do parâmetro MV\_ISS.

MV\_TPABISS (Parâmetro exclusivo para notas de saída) - Conteúdo = 1 indica que é efetuado um desconto na duplicata quando o cliente recolhe ISS.  2 = É gerado um título de abatimento.

MV\_DEISSBS (Parâmetro exclusivo para notas de saída) - Indica se o valor do ISS deve ser retirado da base de cálculo do PIS/COFINS/CSLL. Conteúdo .T. = não será descontado. Conteúdo .F. = será descontado.

MV\_RATISS- Indica se deve ratear o ISS no lançamento do documento fiscal de entrada.

T= Rateio por parcela

F= Mantém na primeira parcela
