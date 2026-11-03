---
article_id: 360018978571
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 880d54c319c8301c1984d69fe0005296fd6092d32d85290fbdb404478f209196
fetched_at: '2026-06-28T22:39:30.555162+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Configuração para
  cálculo de INSS (retenção).
type: support-article
updated_at: '2025-07-31T20:17:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018978571-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-para-c%C3%A1lculo-de-INSS-reten%C3%A7%C3%A3o
---

**Dúvida**  
Como configurar o Protheus para calcular o INSS retenção via documento de entrada ou saída?  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – Todas as versões  
  
**Solução**Para realizar o cálculo e a retenção do **INSS,** deverá configurar os cadastros e parâmetros abaixo:

**Fornecedor (SA2):**

Calc. INSS (A2\_RECINSS) = SIM

**Cliente (SA1):**

Rec. INSS (A1\_RECINSS) = SIM

**Produto (SB1):**

Calcula INSS (B1\_INSS) = SIM

%Red. INSS (B1\_REDINSS) este campo é para Redução da BASE do INSS. Informe o percentual a ser considerado em relação a base de cálculo. Ex: Se for informado 60%, a base de cálculo ficará com 60% de  
seu valor original.

**Natureza (SED):**

Calcula INSS (ED\_CALCINS)= SIM

Porc. INSS (ED\_PERCINS)= 11% ou alíquota necessária

Ded.INSS (ED\_DEDINSS): Informe "1" (Sim)para que o valor do INSS seja deduzido do valor do título quando houver retenção desta contribuição. Informe "2" (Não) em caso contrário.

 

**TES (SF4):**

Gera Dupl. (F4\_DUPLIC) = SIM

**Parâmetros:**

**MV\_ACMINSS** - Define se a cumulatividade dos valores de INSS levarão em conta a data de Emissão ou Vencimento do título principal.

1=Emissão

2=Vencto Real

 

**MV\_LIMINSS**- Valor limite de retenção para o INSS de pessoa física.

obs: caso tenha casa decimal no valor, informe ponto e não vírgula.

Exemplo: 856.46 e não 856,46

           

 **MV\_VENCINS** - Parametrização do cálculo do vencimento dos títulos de INSS.

1=Emissão

2=Vencto Real

 

**MV\_FORINSS** - Fornecedor padrão para geração de títulos de INSS.

 

**MV\_COMIINS** - Indica se o INSS será considerado para pagamento de comissão. Informar (S) ou (N).

 

**MV\_INSS** - Natureza de Títulos de Pagamento de INSS.

 

**MV\_VLRETIN** - Valor mínimo para dispensa de retenção de INSS.

 

**MV\_INSIRF** - Define se o valor do INSS deve ser abatido da base de cálculo do IRRF no Financeiro.

1=Abate o valor

2=Não abate

 

**MV\_RNDINS** - Informe o critério de arredondamento do INSS.

.T. arredonda

.F. trunca. Título principal

 

**MV\_RATINSS** - Indica se o valor do INSS deve ser ou não rateado pelo número de títulos a pagar em uma nota fiscal.

T=Rateio por parcela

F=Mantém na primeira parcela

 

**MV\_INSACPJ** - Define a regra de acumulo de INSS para fornecedores do tipo Pessoa Jurídica.

1=Acumula

2=Não acumula

 

**MV\_MININSS** - Valor mínimo para retenção de INSS. Caso o valor de INSS calculado no período seja inferior, o INSS não será retido.  (Pessoa Física)      

 

**MV\_ INSTPAC**   - Define o tipo de cumulatividade    1 = Mensal ( Padrão ) / 2 = Últimos 5 anos. 

<https://tdn.totvs.com/pages/releaseview.action?pageId=697252452>

**Campos que são gravados o INSS**

**Saída**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000559961-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Quais-campos-gravam-o-INSS-Retido-ap%C3%B3s-escriturar-a-nota-fiscal-de-sa%C3%ADda->

**Entrada**

[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046341373-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Em-quais-campos-s%C3%A3o-gravados-os-valores-de-INSS-via- Reten%C3%A7%C3%A3o-em-Opera%C3%A7%C3%B5es-de-Entrada-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046341373-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Em-quais-campos-s%C3%A3o-gravados-os-valores-de-INSS-via-Reten%C3%A7%C3%A3o-em-Opera%C3%A7%C3%B5es-de-Entrada-)
