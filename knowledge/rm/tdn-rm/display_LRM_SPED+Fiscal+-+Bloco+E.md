---
content_hash: 2b6c2fc60de6408d93d3af3a4ed2fa0e3879df40cfd8460b28a7ab646809feb5
fetched_at: '2026-06-29T00:09:20.000426+00:00'
page_id: '422545627'
product: rm
source: tdn-rm
title: SPED Fiscal - Bloco E
type: documentation
url: https://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+E
version: 33
---

Este bloco é composto pelos registros:

BLOCOEleftE100E100

**Período de apuração do ICMS**

Este registro tem por objetivo informar o(s) período(s) de apuração do ICMS. Os períodos informados devem abranger todo o intervalo da escrituração fiscal, sem sobreposição ou omissão de datas ou períodos.

E110E110

**Apuração do ICMS - Operações Próprias**

Este registro tem por objetivo informar os valores relativos à apuração do ICMS referentes às operações próprias. O registro deve ser apresentado inclusive nos casos de períodos sem movimento. Neste caso, os valores deverão ser apresentados zerados.

Será considerado os ajustes C197 e D197 dos lançamentos fiscais no registro E110 da EFD ICMS\IPI.

Deve ser considerado como Ajuste de Débito (Considerar como débito) os Códigos de Ajuste cujo o Terceiro caractere for igual a ‘3’, ‘4’ ou ‘5’ e o Quarto caractere for igual a “0”, “3”, “4”, “5”, “6”, “7” ou “8”.

Exemplo de código: UF30xxxxxx, UF04xxxxxx

Deve ser considerado como Ajuste de Crédito (Considerar como crédito) os Códigos de Ajuste cujo o Terceiro caractere for igual a ‘0’, ‘1’ ou ‘2’ e o Quarto caractere for igual a ‘0’, “3”, “4”, “5”, “6”, “7” ou “8”.

Exemplo de código: UF00xxxxxx, UF03xxxxxx.

Os registros com os códigos de ajuste conforme descrito acima sempre serão gerados na rotina, mesmo que a flag para gerar os registros C197 e/ou D197 estejam desmarcadas na geração do SPED. Os demais códigos de ajuste somente serão gerados caso a flag esteja marcada na rotina.

| Nº | CAMPO | DESCRIÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "E110" |  |
| 02 | VL\_TOT\_DEBITOS | Valor total dos débitos por "Saídas e prestações com débito do imposto" | Gerado do ao somatório de todos os documentos fiscais de saída que geram débito de ICMS.  DITEM.VLRICMSPRD |
| 03 | VL\_AJ\_DEBITOS | Valor total dos ajustes a débito decorrentes do documento fiscal. | Este campo é calculado internamente com a seguinte expressão:  È somatório do campo VL\_ICMS dos registros C197, C597, C857, C897, D197 e D737 se o terceiro caractere do campo COD\_AJ for igual a ‘3’, ‘4’ ou ‘5’ e o quarto caractere for igual a “0”, “3”, “4”, “5”, “6”, “7” ou “8”.  Consideramos todos os Lançamentos que tem Código de Ajuste no Lançamento ou no Item do Lançamento. |
| 04 | VL\_TOT\_AJ\_DEBITOS | Valor total de "Ajustes a débito" | Este campo é calculado internamente com a seguinte expressão:  O somatório do campo VL\_AJ\_APUR dos registros E111, se o terceiro caractere for igual a ‘0’ e o quarto caractere for igual a ‘0’.  Consideramos Lançamento de Outros Débitos\Credito. |
| 05 | VL\_ESTORNOS\_CRED | Valor total de Ajustes “Estornos de créditos” | Este campo é calculado internamente com a seguinte expressão:  Somatório do campo VL\_AJ\_APUR dos registros E111, se o terceiro caractere for igual a ‘0’ e o quarto caractere do campo COD\_AJ\_APUR, for igual a ‘1’.  Consideramos Lançamento de Outros Débitos\Credito – Tipo Estorno Credito |
| 06 | VL\_TOT\_CREDITOS | Valor total dos créditos por "Entradas e aquisições com crédito do imposto" | Gerado com somatório de todos os documentos fiscais de entrada que geram crédito de ICMS.  DITEM.VLRICMSPRD |
| 07 | VL\_AJ\_CREDITOS | Valor total dos ajustes a crédito decorrentes do documento fiscal. | Este campo é calculado internamente com a seguinte expressão:  È somatório do campo VL\_ICMS dos registros C197, C597, C857, C897, D197 e D737, se o terceiro caractere do código de ajuste for ‘0’, ‘1’ ou ‘2’ e o quarto caractere for ‘0’, “3”, “4”, “5”, “6”, “7” ou “8”.  Consideramos todos os Lançamentos que tem Código de Ajuste no Lançamento ou no Item do Lançamento. |
| 08 | VL\_TOT\_AJ\_CREDITOS | Valor total de "Ajustes a crédito" | Este campo é calculado internamente com a seguinte expressão:  Somatório dos valores constantes dos registros E111, quando o terceiro caractere for igual a ‘0’ e o quarto caractere for igual a ‘2’.  Consideramos Lançamento de Outros Débitos\Credito. |
| 09 | VL\_ESTORNOS\_DEB | Valor total de Ajustes “Estornos de Débitos” | Este campo é calculado internamente com a seguinte expressão:  Somatório do VL\_AJ\_APUR dos registros E111, quando o terceiro caractere for igual a ‘0’ e o quarto caractere for igual a ‘3’.  Consideramos Lançamento de Outros Débitos\Credito – Tipo Estorno de Debito |
| 10 | VL\_SLD\_CREDOR\_ANT | Valor total de "Saldo credor do período anterior" | Gerado com o Valor do Campo Saldo Credor do Período Anterior informado no Período de Apuração - Sub Pasta Apuração |
| 11 | VL\_SLD\_APURADO | Valor do saldo devedor apurado | Este campo é calculado internamente com a seguinte expressão:  Soma do total de débitos (VL\_TOT\_DEBITOS- Campo 02) com total de ajustes (VL\_AJ\_DEBITOS +VL\_TOT\_AJ\_DEBITOS- Campo 03 e campo 04) com total de estorno de crédito (VL\_ESTORNOS\_CRED – Campo 05 ) menos a soma do total de créditos (VL\_TOT\_CREDITOS – Campo 06) com total de ajuste de créditos (VL\_AJ\_CREDITOS + VL\_TOT\_AJ\_CREDITOS – campo 07 e 08) com total de estorno de débito (VL\_ESTORNOS\_DEB – Campo 09) com saldo credor do período anterior (VL\_SLD\_CREDOR\_ANT – campo 10).  Se o valor da expressão for menor que “0” (zero), então este campo deve ser preenchido com “0” (zero) e o valor absoluto da expressão deve ser informado no campo VL\_SLD\_CREDOR\_TRANSPORTAR, adicionado ao valor total das deduções (VL\_TOT\_DED) |
| 12 | VL\_TOT\_DED | Valor total de "Deduções" | Este campo é calculado internamente com a seguinte expressão:  Este campo é gerado conforme o Código de Ajuste informado no Lançamento Fiscal ou Código de Ajuste informado no Item do Lançamento Fiscal, se o terceiro caractere do código de ajuste do registro C197, C597, C857, C897, D197 ou D737, for ‘6’ e o quarto caractere for ‘0’, Lançamento de Outros Créditos\Débitos – Tipo Dedução, quando o terceiro caractere for igual a ‘0’ e o quarto caractere for igual a ‘4’, do campo COD\_AJ\_APUR do registro E111. Neste campo são informados os valores que, segundo a legislação da UF, devam ser tratados como “Dedução do imposto”, ainda que no campo VL\_SLD\_APURADO tenha como resultado o valor zero. |
| 13 | VL\_ICMS\_RECOLHER | Valor total de "ICMS a recolher (11-12) | Este campo é calculado internamente com a seguinte expressão:  o valor informado deve corresponder à diferença entre o (campo 11 - VL\_SLD\_APURADO) e o (campo 12 - VL\_TOT\_DED). Se o resultado dessa operação for negativo, informe o valor zero neste campo, e o valor absoluto correspondente no (campo 14 -VL\_SLD\_CREDOR\_TRANSPORTAR). Verificar se a legislação da UF permite que dedução seja maior que o saldo devedor. O valor da soma deste campo com o campo DEB\_ESP deve ser igual à soma dos valores do campo VL\_OR do registro E116. |
| 14 | VL\_SLD\_CREDOR\_TRANSPORTAR | Valor total de "Saldo credor a transportar para o período seguinte” | Este campo é calculado internamente com a seguinte expressão:  se o valor da expressão: soma do total de débitos (VL\_TOT\_DEBITOS – Campo 02) com total de ajustes (VL\_AJ\_DEBITOS + VL\_TOT\_AJ\_DEBITOS – Campos 03 e 04) com total de estorno de crédito (VL\_ESTORNOS\_CRED – Campo 05) menos a soma do total de créditos (VL\_TOT\_CREDITOS – Campo 06) com total de ajuste de créditos (VL\_AJ\_CREDITOS + VL\_TOT\_AJ\_CREDITOS – campos 07 e 08) com total de estorno de débito (VL\_ESTORNOS\_DEB – campos 09) com saldo credor do período anterior (VL\_SLD\_CREDOR\_ANT – campo 10) com total de deduções (VL\_TOT\_DED – campo 12) for maior que “0” (zero), este campo deve ser preenchido com “0” (zero). Se for menor que “0” (zero), o valor absoluto do resultado deve ser informado neste campo. |
| 15 | DEB\_ESP | Valores recolhidos ou a recolher, extra-apuração. | Este campo é calculado internamente com a seguinte expressão:  o valor informado deve corresponder ao somatório do campo VL\_ICMS dos registros C197, C597, C857, C897, D197 e D737, se o terceiro caractere do código informado no campo COD\_AJ for igual a “7” (débitos especiais) e o quarto caractere for igual a “0” (operações próprias).  o valor informado deve corresponder ao somatório de ajustes do campo VL\_AJ\_APUR do registro E111, se o terceiro caractere do código informado no campo COD\_AJ\_APUR do registro E111 for igual a “0” (apuração ICMS próprio) e o quarto caractere for igual a “5”(débito especial).  O valor da soma deste campo com o campo VL\_ICMS\_RECOLHER deve ser igual à soma dos valores do campo VL\_OR do registro E116.  Valores Extra Apuração, não afeta a apuração do ICMS e a Guia deve ser incluída manualmente, no período de Apuração. |

E111E111

**Ajuste/benefício/incentivo da apuração do ICMS**

Este registro tem por objetivo discriminar todos os ajustes lançados nos campos VL\_TOT\_AJ\_DEBITOS, VL\_ESTORNOS\_CRED, VL\_TOT\_AJ\_CREDITOS, VL\_ESTORNOS\_DEB e VL\_TOT\_DED do registro E110. É gerado também, caso no registro E110, no campo DEB\_ESP, contenha algum valor e cujo COD\_AJ\_APUR, tamanho 8, se enquadre para gerar este.

ATENÇÃO

Não serão considerados os Lançamentos de Outros Débitos/Créditos  cujo campo "Sub-Apuração do Período" esteja preenchido.

E112E112

**Informações adicionais dos ajustes da apuração do ICMS**

Este registro tem por objetivo detalhar os ajustes do registro E111 quando forem relacionados a processos judiciais ou fiscais ou a documentos de arrecadação, observada a legislação estadual pertinente. Valores recolhidos, com influência na apuração do ICMS – Operações Próprias, devem ser detalhados neste registro, com identificação do documento de arrecadação específico.

E113E113

**Informações adicionais dos ajustes da apuração do ICMS - Identificação dos documentos fiscais**

Este registro tem por objetivo identificar dos documentos fiscais relacionados ao ajuste.

| N° | Campo | Descrição | Origem da Informação |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "E313" | Não se aplica |
| 02 | COD\_PART | Código do participante (campo 02 do registro 0150) |  |
| 03 | COD\_MOD | Código do modelo do documento fiscal |  |
| 04 | SER | Série do documento fiscal |  |
| 05 | SUB | Subsérie do documento fiscal |  |
| 06 | NUM\_DOC | Número do documento fiscal |  |
| 07 | CHV\_DOCe | Chave do documento eletrônico | Chave de acesso do lançamento referenciado |
| 08 | DT\_DOC | Data da emissão do documento fiscal |  |
| 09 | COD\_ITEM | Código do item (campo 02 do registro 0200) |  |
| 10 | VL\_AJ\_ITEM | Valor do ajuste para a operação/item |  |

E115E115

**Informações adicionais da apuração - valores declaratórios**

Este registro tem o objetivo de informar os valores declaratórios relativos ao ICMS, conforme definição da legislação estadual pertinente.

Os dados deste registro tem as seguintes origens:

* Ajustes vinculados à Situação Tributária, cujos Códigos de Ajuste estejam cadastrados como "*Registro E115*";
* "*Valores Adicionais Apuração*" cadastrados no Período de Apuração.

Os valores serão totalizados por Código de Ajuste e Descrição.

Esses valores são meramente declaratórios e não são computados na apuração do ICMS.

E116E116

**Obrigações do ICMS a recolher - Operações próprias**

Este registro tem o objetivo de discriminar os pagamentos realizados ou a realizar, referentes à apuração do ICMS – Operações Próprias do período. A soma do valor das obrigações deste registro deve ser igual à soma dos campos VL\_ICMS\_RECOLHER e DEB\_ESP, do registro E110.

E200E200

**Período da apuração do ICMS - Substituição tributária**

Este registro tem por objetivo informar o(s) período(s) de apuração do ICMS – Substituição Tributária para cada UF onde o informante seja inscrito como substituto tributário, inclusive para o seu estado, nas operações internas que envolvam substituição, e também para UF para a qual o declarante tenha comercializado e que não tenha inscrição como substituto. Os períodos informados devem abranger todo o período previsto no registro 0000, sem haver sobreposição ou omissão de datas, por UF.

E210E210

**Apuração do ICMS - Substituição tributária**

Este registro tem por objetivo informar valores relativos à apuração do ICMS de substituição tributária, mesmo nos casos de períodos sem movimento.  
  
**Débitos Especiais para o Estado MG:**  
Quando não houver valor apurado mas for usado no Lançamento Fiscal código de ajuste iniciado por MG71\*\*\*\*\*\*  pertinente a Débitos especiais, será gravado o valor zerado no período de apuração para geração do registro.

| Nr | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "E210" | Fixo |
| 02 | IND\_MOV\_ST | Indicador de movimento: 0 – Sem operações com ST 1 – Com operações de ST |  |
| 03 | VL\_SLD\_CRED\_ANT\_ST | Valor do "Saldo credor de período anterior – Substituição Tributária" | Gerado com o Valor do Saldo Credor do Período Anterior informado  Período de Apuração  DPERIODOST.SALDOTRBANT |
| 04 | VL\_DEVOL\_ST | Valor total do ICMS ST de devolução de mercadorias | Soma do Valor do ICMS ST do Item do Lançamento Fiscal  DITEM.VLRICMSSTPRD |
| 05 | VL\_RESSARC\_ST | Valor total do ICMS ST de ressarcimentos |  |
| 06 | VL\_OUT\_CRED\_ST | Valor total de Ajustes "Outros créditos ST" e “Estorno de débitos ST” | Gerado com o Valor outros Créditos\ Débitos com ICMS ST e Tipo Credito  e Estorno de Débitos |
| 07 | VL\_AJ\_CREDITOS\_ST | Valor total dos ajustes a crédito de ICMS ST, provenientes de ajustes do documento fiscal. | corresponder ao somatório do campo VL\_ICMS do registro C197 |
| 08 | VL\_RETENÇAO\_ST | Valor Total do ICMS retido por Substituição Tributária |  |
| 09 | VL\_OUT\_DEB\_ST | Valor Total dos ajustes "Outros débitos ST" " e “Estorno de créditos ST” | Gerado com o Valor outros Créditos\ Débitos com ICMS ST e Tipo Débito  e Estorno de Crédito |
| 10 | VL\_AJ\_DEBITOS\_ST | Valor total dos ajustes a débito de ICMS ST, provenientes de ajustes do documento fiscal. | corresponder ao somatório do campo VL\_ICMS do registro C197 |
| 11 | VL\_SLD\_DEV\_ANT\_ST | Valor total de Saldo devedor antes das deduções |  |
| 12 | VL\_DEDUÇÕES\_ST | Valor total dos ajustes "Deduções ST" | DPERIODOST.TOTALDEDUCOES |
| 13 | VL\_ICMS\_RECOL\_ST | Imposto a recolher ST (11-12) | Calculado Internamente |
| 14 | VL\_SLD\_CRED\_ST\_TRANS PORTAR | Saldo credor de ST a transportar para o período seguinte [(03+04+05+06+07+12) – (08+09+10)]. | Calculado Internamente |
| 15 | DEB\_ESP\_ST | Valores recolhidos ou a recolher, extra-apuração. | Considerar o Valor do ICMS ST dos Lançamentos Fiscais que tem Código de Ajuste do Sped  cujo o Terceiro caractere for igual a '7' (débitos especiais) e o Quarto caractere for igual a '1'” (operações por ST).  Ajustes descriminados nos Registros C197 |

E220E220

**Ajuste/benefício/incentivo da apuração do ICMS substituição tributária**

Este registro deve ser apresentado para discriminar os ajustes lançados nos campos VL\_OUT\_CRED\_ST, VL\_OUT\_DEB\_ST e VL\_DEDUÇOES\_ST do registro E210.

E230E230

**Informações adicionais dos ajustes da apuração do ICMS substituição tributária**

Este registro deve ser apresentado para detalhar os ajustes do registro E220 quando forem relacionados a processos judiciais ou fiscais ou a documentos de arrecadação, observada a legislação estadual pertinente. Valores recolhidos, com influência na apuração do ICMS-ST, devem ser informados neste registro, com identificação do documento de arrecadação específico.

E240E240

**Informações adicionais dos ajustes da apuração do ICMS substituição tributária - Identificação dos documentos fiscais**

Este registro deve ser apresentado para identificação dos documentos fiscais relacionados ao ajuste.

E250E250

**Obrigações do ICMS a recolher - Substituição tributária**

Este registro deve ser apresentado para discriminar os pagamentos realizados ou a realizar, referentes à apuração do ICMS devido por Substituição Tributária do período, por UF. A soma do valor das obrigações deste registro deve ser igual ao campo VL\_ICMS\_RECOL\_ST somado ao campo DEB\_ESP\_ST, ambos do registro E210.

Quando ocorre Débitos Especiais - Campo 15 do Registro E210 deve ser incluída uma guia manualmente no Período de Apuração - Anexo Guia GNR

E300E300

**Período de apuração do Fundo de Combate à Pobreza e do ICMS Diferencial de Alíquota – UF ORIGEM/DESTINO EC 87/15**

Este registro tem por objetivo informar o(s) período(s) de apuração do ICMS – Diferencial de Alíquota por UF  
origem/destino, segundo o disposto na Emenda Constitucional 87/2015.

A partir de janeiro de 2019, deixa de ser obrigatória a apresentação do registro E300 para a UF de origem.  
Os períodos informados no registro E300 deverão abranger todo o período da escrituração, para cada UF informada, não sendo permitidos intervalos.

E500E500

**Período de apuração do IPI**

Este registro deve ser apresentado pelos estabelecimentos industriais ou equiparados, conforme dispõe o Regulamento do IPI, para identificação do(s) período(s) de apuração. O(s) período(s) informado(s) deve(m) abranger todo o período previsto no registro 0000. Poderão coexistir um período mensal com períodos decendiais. Para os períodos decendiais, não poderá haver sobreposição ou omissão de datas.

E510E510

**Consolidação dos valores do IPI**

Este registro deve ser preenchido com os valores consolidados do IPI, de acordo com o período informado no registro E500.

| Nº | CAMPO | DESCRIÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "E510" |  |
| 02 | CFOP | Código Fiscal de Operação e Prestação do agrupamento de itens | Código da Natureza de Operação da situação tributária correspondente.  DLAF.IDNAT |
| 03 | CST\_IPI | Código da Situação Tributária referente ao IPI, conforme a Tabela indicada no item 4.3.2. | Código da situação tributária do IPI informado na regra de IPI vinculada a natureza de operação.  DREGRAIPI.SITTRIBUTARIAIPIENT |
| 04 | VL\_CONT\_IPI | Parcela correspondente ao "Valor Contábil" referente ao CFOP e ao Código de Tributação do IPI | Soma do valor contábil do documento.  (DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA + DITEM.VALORSEGURO + DITEM.VLRFRETE + DITEM.VALORIPI + DITEM.VALORIPISEMCREDITO) - (Se (regra de IPI = IPI Metade) então DITEM.VALORIPI senão 0) |
| 05 | VL\_BC\_IPI | Parcela correspondente ao "Valor da base de cálculo do IPI" referente ao CFOP e ao Código de Tributação do IPI, para operações tributadas | Soma da base de cálculo do IPI.  DLAF.BASEIPI |
| 06 | VL\_IPI | Parcela correspondente ao "Valor do IPI" referente ao CFOP e ao Código de Tributação do IPI, para operações tributadas | Valor do IPI tributado.  DLAF.VALORIPI |

E520E520

**Apuração do IPI**

Este registro deve ser preenchido para demonstração da apuração do IPI no período.

E530E530

**Ajustes da apuração do IPI**

Este registro deve ser apresentado para discriminar os ajustes lançados nos Campos Outros Débitos e Outros Crédito do registro E520.

E531E531

**Informações Adicionais dos Ajustes da Apuração do IPI – Identificação dos Documentos Fiscais (01 e 55)**

Este registro tem por objetivo identificar dos documentos fiscais relacionados ao ajuste
