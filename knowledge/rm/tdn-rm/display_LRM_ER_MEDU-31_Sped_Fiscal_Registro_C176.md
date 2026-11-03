---
content_hash: d77c3e5411a892d9179b3cd8d327d1c291714b4dbc1a2ef69d89e3a0cbb360b5
fetched_at: '2026-06-29T00:08:23.951573+00:00'
page_id: '270098607'
product: rm
source: tdn-rm
title: ER_MEDU-31_Sped_Fiscal_Registro_C176
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_MEDU-31_Sped_Fiscal_Registro_C176
version: 32
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Sped Fiscal - Registro C176 - Cat.: 158

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Totvs Getsão Fiscal |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_ | | |

**Manual do Sped Fiscal Registro C176**

Portaria CAT 158 de 2015 - Ressarcimento ICMS Retido por Sujeição Passiva de Subs.Tributaria.

Conforme o manual a obrigatoriedade e a forma de escrituração deste registro serão definidas pela UF de domicílio do contribuinte.

 A inclusão da Referencia do Item é somente para Gerar o Registro C176, por este motivo não vamos tratar no processo de Escrituração e no “TOTVS Gestão de Estoques, Compras e Faturamento”.

 A Referencia do Item deve ser incluída manualmente.

 Este Registro deve ser gerado para Todos os Lançamentos de Saída, Interestadual e que tenha Valor do ICMS ST.

 Registro Filho do Registro C170, então será necessário para o Tipo de Documento 55(NFe) será necessário gerar o Registro C170 somente para os Item que tem Referencia preenchida.

Observação:

Atualmente já geramos este Registro para os lançamentos de Entrada ou Saída com Natureza de Operação 5.603 ou 6.603 ou 1.603 ou 2.603 e a Referencia no Lançamentos Fiscal.

Este registro será gerado para todas as referências do mesmo item.

Este registro será gerado para todas as operações de saída em quem o parâmetro "Operação com Ressarcimento de ST na Compra" estiver habilitado na Natureza de Operação (CFOP) associado ao Lançamento ao Lançamento Fiscal.

**Implementações TOTVS Gestão Fiscal**

**Lançamento Fiscal**

* Habilitar no Item do Lançamento Fiscal a Sub Pasta Referencia (Tabela DITEMREFERENCIA) somente para:  
  Lançamento de Saída;  
  Com CFOP do Grupo 6.4xx - Saídas de Mercadoria Sujeitas ao Regime de Substituição;  
  Regra de ICMS – Tipo de Operação “Substituição Tributaria”;
* Tela Referência por Item novo campo “Código do motivo do ressarcimento”.

**Dicionário de Dados**

Alteração na Tabela DITEMREFERENCIA

Novo Campo:

| Tabela | Campo | Tipo | Tam | Obrig. |
| --- | --- | --- | --- | --- |
| DITEMREFERENCIA | MOTIVORESSARCIMENTO | Integer | - | Não |

**Importação de Lançamento Fiscal Delphi**

Este novo campo Não será importado no processo Delphi, apenas na importação .Net (Web Service).

**Geração do Registro C176 no Sped Fiscal - RESSARCIMENTO DE ICMS EM OPERAÇÕES COM SUBSTITUIÇÃO TRIBUTÁRIA (CÓDIGO 01, 55).**

Registro C176 filho do Registro C170;

Alterar a consistência que existe atualmente, na Geração do Registro C176.

Este Registro deve ser gerado somente para os Itens que geram direito ao Ressarcimento da ST e que a Referencia por Item tenha informação;

Ao gerar os Registros C100 e C190 dos Lançamentos de Saída com o Tipo de Documento 55(NFe), temos que  gerar o Registro C170 somente dos Itens que tem Referencia informado.

Este registro deve ser informado quando da escrituração de documento fiscal, que acoberte operação que represente

desfazimento de substituição tributária realizada em operações anteriores.

O documento informado neste registro deverá ser diferente do documento informado no registro pai (C100), pois

é o documento referente à(s) última(s) aquisição(ões) da mercadoria e à retenção do imposto.

A obrigatoriedade e a forma de escrituração deste registro serão definidas pela UF de domicílio do contribuinte, inclusive

sobre a apresentação dos campos:

CHAVE\_NFE\_RET; COD\_PART\_NFE\_RET; SER\_NFE\_RET; NUM\_NFE\_RET;ITEM\_NFE\_RET.

Este registro não se aplica a contribuintes que utilizam o SCANC.

| Nº | Campo | Descrição | Tipo | Tam | Dec | Obrig | Origem do Campo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "C176" | C | 004 | - | O | Fixo |
| 02 | COD\_MOD\_ULT\_E | Código do modelo do documento fiscal relativa a última entrada | C | 002 | - | O | Código Modelo do Documento Fiscal - Lançamento Referenciado |
| 03 | NUM\_DOC\_ULT\_E | Número do documento fiscal relativa a última entrada | N | 009 | 02 | O | Número do Documento do Lançamento Referenciado |
| 04 | SER\_ULT\_E | Série do documento fiscal relativa a última entrada | C | 003 | 02 | OC | Serie do Documento do Lançamento Referenciado |
| 05 | DT\_ULT\_E | Data relativa a última entrada da mercadoria | N | 008 | - | O | Data de Entrada do Documento do Lançamento Referenciado |
| 06 | COD\_PART\_ULT\_E | Código do participante (do emitente do documento relativa a última entrada) | C | 060 | - | O | Código do Cliente\Fornecedor do Documento do Lançamento Referenciado |
| 07 | QUANT\_ULT\_E | Quantidade do item relativa a última entrada | N | - | 03 | O | Quantidade do Item do Documento do Lançamento Referenciado |
| 08 | VL\_UNIT\_ULT\_E | Valor unitário da mercadoria constante na NF relativa a última entrada inclusive despesas acessórias. | N | - | 03 | O | (Total da Mercadoria + Despesas + Acrescimentos – Desconto)  do Item do Documento do Lançamento Referenciado |
| 09 | VL\_UNIT\_BC\_ST | Valor unitário da base de cálculo do imposto pago por substituição. | N | - | 03 | O | Base de Calculo da Substituição Tributaria do Item do Documento do Lançamento Referenciado.  Este campo será gerado com base no valor unitário do item. O valor calculado será dividido pela quantidade de itens. |
| 10 | CHAVE\_NFE\_ULT\_E | Número completo da chave da NFe relativo à última entrada | N | 044 | - | OC | Chave da NFe do Documento do Lançamento Referenciado |
| 11 | NUM\_ITEM\_ULT\_E | Número sequencial do item na NF entrada que corresponde à mercadoria objeto de pedido de ressarcimento | N | 003 | - | OC | Número sequencial do Item no Lançamento Referenciado |
| 12 | VL\_UNIT\_BC\_ICMS\_ULT\_E | Valor unitário da base de cálculo da operação própria do remetente sob o regime comum de tributação | N | - | 02 | OC | Base de Calculo do ICMS informado na Situação Tributaria\Sub Pasta ICMS e IPI – Campo BC do Documento do Lançamento Referenciado.  Este campo será gerado com base no valor unitário do item. O valor calculado será dividido pela quantidade de itens. |
| 13 | ALIQ\_ICMS\_ULT\_E | Alíquota do ICMS aplicável à última entrada da mercadoria | N | - | 02 | OC | Alíquota ICMS informado na Situação Tributaria\Sub Pasta ICMS e IPI – Campo Alíquota do Documento do Lançamento Referenciado. Este campo será gerado com base no valor unitário do item. O valor calculado será dividido pela quantidade de itens. |
| 14 | VL\_UNIT\_LIMITE\_BC\_ICMS\_ULT\_E | Valor unitário da base de cálculo do ICMS relativo à última entrada da mercadoria, limitado ao valor da BC da retenção (corresponde ao menor valor entre os campos VL\_UNIT\_BC\_ST e VL\_UNIT\_BC\_ICMS\_ULT\_E ) | N | - | 02 | OC | Se o Campo Tipo de Retenção da Regra do ICMS  for igual a “Substituto Tributário” recebe o valor da BC do ICMS ST do Item do Documento do Lançamento Referenciado.  Se for “Antecipação” recebe o valor do Campo 09 ou do campo 12. Deve ser o de menor valor.  Este campo será gerado com base no valor unitário do item. O valor calculado será dividido pela quantidade de itens. |
| 15 | VL\_UNIT\_ICMS\_ULT\_E | Valor unitário do crédito de ICMS sobre operações próprias do remetente, relativo à última entrada da mercadoria, decorrente da quebra da ST – equivalente a multiplicação entre os campos 13 e 14 | N | - | 03 | OC | Se o Campo Tipo de Retenção da Regra do ICMS  for igual a “Substituto Tributário” recebe o valor do ICMS ST do Item do Documento do Lançamento Referenciado.  Se for “Antecipação” será o resultado  da multiplicação entre os campos 13 e 14.  Este campo será gerado com base no valor unitário do item. O valor calculado será dividido pela quantidade de itens. |
| 16 | ALIQ\_ST\_ULT\_E | Alíquota do ICMS ST relativa à última entrada da mercadoria | N | - | 02 | OC | Alíquota ICMS ST informado na Situação Tributaria\Sub Pasta Substituição Tributaria Alíquota ST – Campo Alíquota do Documento do Lançamento Referenciado |
| 17 | VL\_UNIT\_RES | Valor unitário do ressarcimento (parcial ou completo) de ICMS decorrente da quebra da ST | N | - | 03 | OC | Resultado da Multiplicação dos Campos 09 e 16.  Este campo será gerado com base no valor unitário do item. O valor calculado será dividido pela quantidade de itens. |
| 18 | COD\_RESP\_RET | Código que indica o responsável pela retenção do ICMS-ST: 1-Remetente Direto 2-Remetente Indireto 3-Próprio declarante | N | 001 | - | OC | Gerado conforme a CFOP do Documento do Lançamento Referencia – Campo Situação de Retenção do ICMS ST |
| 19 | COD\_MOT\_RES | Código do motivo do ressarcimento 1 – Venda para outra UF; 2 – Saída amparada por isenção ou não incidência; 3 – Perda ou deterioração; 4 – Furto ou roubo 9 - Outros | N | 001 | - | OC | Gerado conforme o Código informado no Campo novo “Código do motivo do ressarcimento” |
| 20 | CHAVE\_NFE\_RET | Número completo da chave da NF-e emitida pelo substituto, na qual consta o valor do ICMS-ST retido | N | 044 | - | OC | Campo preenchido quando o campo 18 for igual a “2-Remetente Indireto” Gerado conforme a informação do Documento do Lançamento Referenciado |
| 21 | COD\_PART\_NFE\_RET | Código do participante do emitente da NF-e em que houve a retenção do ICMS-ST – campo 02 do registro 0150 | C | 060 | - | OC | Campo preenchido quando o campo 18 for igual a “2-Remetente Indireto” – Cliente\Fornecedor do Documento do Lançamento Referenciado |
| 22 | SER\_NFE\_RET | Série da NF-e em que houve a retenção do ICMSST | C | 003 | - | OC | Campo preenchido quando o campo 18 for igual a “2-Remetente Indireto” – Serie  do Documento do Lançamento Referenciado |
| 23 | NUM\_NFE\_RET | Número da NF-e em que houve a retenção do ICMS-ST | N | 009 | - | OC | Campo preenchido quando o campo 18 for igual a “2-Remetente Indireto” – Numero do Documento do Lançamento Referenciado |
| 24 | ITEM\_NFE\_RET | Número sequencial do item na NF-e em que houve a retenção do ICMS-ST, que corresponde à mercadoria objeto de pedido de ressarcimento | N | 003 | - | OC | Número sequencial do Item no Lançamento Referenciado |
| 25 | COD\_DA | Código do modelo do documento de arrecadação : 0 - documento estadual de arrecadação 1 – GNRE | C | 001 | - | OC | Não será Gerado |
| 26 | NUM\_DA | Número do documento de arrecadação estadual, se houver | C | - | - | OC | Não será Gerado |

Observação: 1. Os campos 10 a 26 são válidos a partir de 01/01/2017 e utilizados conforme critério da UF do domicílio do  
contribuinte.  
Nível hierárquico - 4  
Ocorrência 1:N

**Campo 01** (REG) - Valor Válido: [C176]

**Campo 02** (COD\_MOD\_ULT\_E) - Valores Válidos: [01, 55]

**Campo 03** (NUM\_DOC\_ULT\_E) - Validação: o valor informado no campo deve ser maior que “0” (zero).

**Campo 05** (DT\_ULT\_E) - Validação: o valor informado deve ser no formato “ddmmaaaa”. O valor informado no campo  
deve ser menor ou igual ao valor no Campo10 (DT\_DOC) do registro C100.

**Campo 06** (COD\_PART\_ULT\_E) - Validação: o valor informado deve existir no campo COD\_PART do registro 0150.

**Campo 07** (QUANT\_ULT\_E) –Validação: o valor informado no campo deve ser maior que “0” (zero).

**Campo 08** (VL\_UNIT\_ULT\_E) - Validação: o valor informado no campo deve ser maior que “0” (zero).

**Campo 09** (VL\_UNIT\_BC\_ST) - Validação: o valor informado no campo deve ser maior que “0” (zero).

**Campo 10** (CHAVE\_ULT\_NFE) - Preenchimento: campo de preenchimento obrigatório para NF-e, COD\_MOD igual a  
“55”. Validação: é conferido o dígito verificador (DV) da chave da NF-e. Este campo é de preenchimento obrigatório para  
COD\_MOD igual a “55”. Para confirmação inequívoca de que a chave da NF-e corresponde aos dados informados do  
documento, é comparado o CNPJ base existente na CHV\_ULT\_NFE com o campo CNPJ base do registro 0150, que  
corresponde ao CNPJ do participante. São verificados a consistência da informação dos campos NUM\_DOC e SER com o  
número do documento e série contidos na chave da NF-e. É também comparada a UF codificada na chave da NF-e com o  
campo UF informado no registro 0150.

**Campo 11** (NUM\_ITEM\_ULT\_E) - Validação: o valor informado no campo deve ser maior que “0” (zero).

**Campo 12** (VL\_UNIT\_BC\_ICMS\_ULT\_E) - Preenchimento:  
Se o emitente informado no campo COD\_PART\_ULT\_E deste registro for o substituto, informar o valor unitário  
destacado no documento fiscal a título de base de cálculo do ICMS; ou  
se o emitente informado no campo COD\_PART\_ULT\_E deste registro for o substituído, informar o valor unitário  
que seria atribuído à base de cálculo do ICMS na operação própria do remetente, caso esta fosse submetida ao  
regime comum de tributação. Validação: o valor informado no campo deve ser maior que “0” (zero).

**Campo 13** (ALIQ\_ICMS\_ULT\_E) - Preenchimento: informar a alíquota do ICMS incidente na operação própria do  
documento fiscal de entrada. Validação: o valor informado no campo deve ser maior que “0” (zero).

**Campo 14** (VL\_UNIT\_LIMITE\_BC\_ICMS\_ULT\_E) Preenchimento:  
Se o emitente informado no campo COD\_PART\_ULT\_E deste registro for o substituto, informar o valor unitário  
da base de cálculo destacada no documento fiscal; ou  
Se o emitente informado no campo COD\_PART\_ULT\_E deste registro for o substituído, informar o menor dos  
valores entre o unitário informado no documento fiscal, a título de base de cálculo do ICMS ST (campo  
VL\_UNIT\_BC\_ST), ou o unitário da base de cálculo do ICMS que seria atribuído na operação própria do  
remetente, caso esta fosse submetida ao regime comum de tributação (campo VL\_UNIT\_BC\_ICMS\_ULT\_E).  
Validação: o valor informado no campo deve ser maior que “0” (zero), e corresponder ao menor valor entre os campos  
VL\_UNIT\_BC\_ST e VL\_UNIT\_BC\_ICMS\_ULT\_E.

**Campo 15** (VL\_UNIT\_ICMS\_ULT\_E) Preenchimento:  
Se o emitente informado no campo COD\_PART\_ULT\_E deste registro for o substituto, informar o valor unitário  
destacado no documento fiscal a título de ICMS; ou  
Se o emitente informado no campo COD\_PART\_ULT\_E deste registro for o substituído, informar o valor  
unitário do ICMS que seria atribuído à operação própria do remetente caso estivesse submetida ao regime comum  
de tributação, limitado ao valor unitário da retenção;  
Validação: o valor informado no campo deve ser maior que “0” (zero), e deve corresponder a multiplicação entre os  
campos ALIQ\_ICMS\_ULT\_E e VL\_UNIT\_LIMITE\_BC\_ICMS\_ULT\_E

**Campo 16** (ALIQ\_ST\_ULT\_E) - Preenchimento: informar alíquota interna do produto a ser aplicada na apuração do  
ICMS ST. Validação: o valor informado no campo deve ser maior que “0” (zero).

**Campo 17** (VL\_UNIT\_RES) - Preenchimento: valor unitário destacado no documento fiscal de entrada a título de ICMS  
ST ou valor unitário do ICMS ST informado a título de reembolso.  
Validação: o valor informado no campo deve ser maior ou igual que “0” (zero), e deve corresponder a multiplicação entre  
os campos VL\_UNIT\_BC\_ST e ALIQ\_ST\_ULT\_E, subtraindo, deste resultado, o campo VL\_UNIT\_ICMS\_ULT\_E.

**Campo 18** (COD\_RESP\_RET) Validação: Valores válidos: [1,2,3]

Código que Indica o Responsável pela Retenção do ICMS ST,  equivale ao campo “Situação da Retenção do ICMS ST” do Aplicativo Gestão Fiscal.

|  |  |
| --- | --- |
| Informação do Manual do Sped | Informação Da Regra do ICMS do CFOP |
| Código que indica o responsável pela retenção do ICMS-ST | Situação da Retenção do ICMS ST |
| 1 - Remetente Direto | Substituto Tributário |
| 2 - Remetente Indireto | Não Se Aplica |
| 3 - Próprio declarante | Antecipação |

**Campo 19** (COD\_MOT\_RES) Validação: Valores válidos: [1,2,3,4,9]

Obs.: Novo campo criado.

**Campo 20** (CHAVE\_NFE\_RET) - Preenchimento: informar a chave da NF-e em que houve a retenção do ICMS-ST.  
Informar este campo caso a informação seja diferente da relativa à última entrada informada no campo  
CHAVE\_NFE\_ULT\_E deste registro.  
Validação: é conferido o dígito verificador (DV) da chave da NF-e. Este campo somente poderá ser apresentado quando  
COD\_RESP\_RET=2. Neste caso, obrigatoriamente, o campo CHAVE\_NFE\_RET ou os campos COD\_PART\_NFE\_RET,  
SER\_NFE\_RET e NUM\_NFE\_RET deverão ser preenchidos.

**Campo 21** (COD\_PART\_NFE\_RET) - Preenchimento: o valor informado deve existir no campo COD\_PART do registro  
0150. Informar este campo caso a informação seja diferente da relativa à última entrada e o informante da EFD não teve  
acesso ao número da chave solicitado no campo CHAVE\_NFE\_RET.  
Validação: se informado o campo CHAVE\_NFE\_RET, este campo não deve ser preenchido. O valor informado deve  
existir no campo COD\_PART do registro 0150. Este campo somente poderá ser apresentado quando COD\_RESP\_RET=2

**Campo 22** (SER\_NFE\_RET) - Preenchimento: informar a série da NF-e. Informar este campo caso a informação seja  
diferente da relativa à última entrada e o informante da EFD não teve acesso ao número da chave solicitado no campo  
CHAVE\_NFE\_RET. Validação: se informado o campo CHAVE\_NFE\_RET, este campo não deve ser preenchido. Se informado o campo  
COD\_PART\_NFE\_RET, este campo deve ser preenchido.

**Campo 23** (NUM\_NFE\_RET) - Preenchimento: informar o número da NF-e. Informar este campo caso a informação  
seja diferente da relativa à última entrada e o informante da EFD não teve acesso ao número da chave solicitado no campo  
CHAVE\_NFE\_RET. Validação: se informado o campo CHAVE\_NFE\_RET, este campo não deve ser preenchido. Se informado o campo  
COD\_PART\_NFE\_RET, este campo deve ser preenchido.

**Campo 24** (ITEM\_NFE\_RET) - Preenchimento: informar o número do item da NF-e correspondente ao ressarcimento.  
Informar este campo caso a informação seja diferente da relativa à última entrada.  
Validação: se informado o campo CHAVE\_NFE\_RET ou o COD\_PART\_NFE\_RET, este campo deve ser preenchido

**Campo 25** (COD\_DA) - Valores válidos: [0, 1] Validação: Este campo deve ser apresentado quando COD\_RESP\_RET=3

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
