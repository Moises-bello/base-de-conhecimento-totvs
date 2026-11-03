---
article_id: 10161449824663
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: a96c671658ab6d70db7e738eae043eb1ec62b9485fd158e0908cbde55725893b
fetched_at: '2026-06-28T22:42:12.618264+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - FISA132-SPEDFISCAL
  REGISTRO C176
type: support-article
updated_at: '2022-11-11T20:42:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10161449824663-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-FISA132-SPEDFISCAL-REGISTRO-C176
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Como gerar o registro C176 do arquivo do SPEDFISCAL ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Primeiramente **rotina Ressarcimento de ICMS-ST (FISA132)** alimenta somente as **tabelas CD0 (Apuração do ICMS-ST) e CDA( Gravação dos lançamentos do Codigo de Reflexo)**.

Vou explicar os pré - requisitos para geração da Tabela CD0 e consequentemente irá gerar o **registro C176 do SPEDFISCAL**. Segue documentação e processo para implantação da **rotina FISA132:**

<https://tdn.totvs.com/display/public/PROT/RESST+-+Ressarcimento+de+ICMS-ST+-+Fiscal+-+P12#RESSTRessarcimentodeICMSSTFiscalP12-Composi%C3%A7%C3%A3odoscamposregistroC176>

Teste que foi realizado foi para o estado de SP, caso for outro estado basta ajusta os **parâmetros com UF correto e Código de ajuste do estado**. Primeiramente precisa configurar os parâmetros:

- MV\_ESTADO:= SP;

- MV\_ESPECIE := UNI=SPED;

- MV\_CODRESS :={"SP10090719","SP10090721"}

- MV\_DEVRESS :={"SP50000319"}

- MV\_TPRESS :=.F.

Para mais informações, acessar a documentação descrita acima... para identificar funcionalidade do **parâmetro**.

I. Escriturar uma NF de entrada, calcular os impostos ICMS + ICMS ST, alimentar Livro Fiscal (Tabelas SFT e SF3). No Período Fiscal de Outubro/201.

II. Escriturar uma NF de Saída, calcular os impostos ICMS + ICMS ST, alimentar Livro Fiscal (Tabelas SFT e SF3) e possui os códigos de ajustes. Onde os códigos de ajustes amarrado na TES(SF4) precisa estar com o seguinte código de reflexo. Lembrando que código de reflexo deve está amarrado no **parâmetro MV\_CODRESS**.

**Nota com direito ao ressarcimento.**

**Cadastro de TES**

Para que sistema identifique situação foi incluída no cadastro de reflexo a opção I – Ressarcimento.

* Deve ser cadastrado um Código de Reflexo com seguinte configuração:

Base para Cálculo = Zero

Alíquota = Zero

Valor = I (Ressarcimento)

* Amarrar reflexo na TES de Saída que será utilizada e Cadastrar nos Lançamentos da Apuração de ICMS:

Código Lançamento SP10090719 (Valor do ressarcimento)

Código Lançamento SP10090721 (Valor do crédito)

Devem ser preenchidos os campos abaixo para que seja processado **registro C197 no arquivo de EFD SPED FISCAL:**

Obs. Lan Fis (CC7\_IFCOMP) = Informações do livro da tabela CCE

O campo Obs. Lan Fis (CC7\_IFCOMP) poderá ser informado no **cadastro de TES ou no** complemento da nota fiscal na **Rotina MATA910/MATA920** – Opção – Informações complementares, campo Inf Compl. (CDT\_IFCOMP)

III. Processar Apuração de Ressarcimento ST (FISA132) e sem seguida executar o Relatório(FISR132);

IV. Realizar geração do SPEDFISCAL.

Iremos **demonstrar o Cálculo realizado pela rotina Ressarcimento ICMS-ST(FISA132)** e apresentação do SPED FISCAL nos REGISTROS C176 e C197.

Escriturar uma NF de entrada no seguinte Cenário:

Produto Skate

Quantidade:=30 IVA := 65,94%;

Valor Unitário:= 18,67;

VALOR TOTAL:= 560,10

NF calcula somente o imposto de ICMS ST.

|C100|0|1|SA2010002 02|55|00|003|2||12122017|12122017|727,40|0|0|0|560,10|9|0|0|0|0|0|0|0|0|||||

|C170|1|0010 01|ICMS\_ST|30,00000|FL|560,10|0|1|010|2101||0|18,00|0|0|0|0||||0|0|0||||||||||||||

|C190|010|2101|18,00|727,40|0|0|0|0|0|0||

Escriturar uma NF de saída com o mesmo produto adquirido em cima:

Produto Skate

Quantidade:= 4 IVA := 1%;

Valor Unitário:= 117,88;

VALOR TOTAL:= 471,52

|C100|1|0|SA1010002 10|55|00|001|000064||12122017|12122017|500,66|0|0|0|471,52|9|0|0|0|471,52|56,58|476,24|29,14|0|||||

|C170|1|0010 01|ICMS\_ST|4,00000|FL|471,52|0|1|010|6401||471,52|12,00|56,58|476,24|18,00|29,14||||0|0|0||||||||||||||

|C176|55|2|3|12122017|SA2010002 02|4,000|18,670|30,980||001|18,67|18,00|18,67 campo- 14 |3,361|18,00|2,216|1|1||||||||

|C190|010|6401|12,00|500,66|471,52|56,58|476,24|29,14|0|0|000001|

|C195|000001|INVALID COLUMN NAME 'D2\_FORNECE'.|

|C197|SP10090721| Crédito relativo à operação própria do Substituto em operação interestadual promovida pelo contribuinte substituído. Artigo 271 do RICMS/00|0010 01|0|0|13,44|0|

|C197|SP10090719| Ressarcimento de substituição tributária, por estabelecimento de contribuinte substituído. Artigos 269 e 270 do RICMS/00|0010 01|0|0|8,86|0|

**Registro C176:**

Campo 01 - Texto fixo contendo "C176”

Campo 02 - Código do modelo do documento fiscal relativa a última entrada // F1\_ESPECIE;

Campo 03 - Número do documento fiscal relativa a última entrada // F1\_ESPECIE;

Campo 04 - Série do documento fiscal relativa a última entrada // D1\_SERIE;

Campo 05 - Data relativa a última entrada da mercadoria // D1\_DTDIGIT;

Campo 06 - Código do participante (do emitente do documento relativa a última entrada) // D1\_FORNECE

Campo 07 - Quantidade do item relativa a última entrada // D2\_QUANT ;

Campo 08 - Valor unitário da mercadoria constante na NF relativa a última entrada inclusive despesas acessórias// - D1\_TOTAL(560,10) /D1\_QUANT(30) := 18,67;

Campo 09 - Valor unitário da base de cálculo do imposto pago por substituição. - //D1\_BRICMS(929,43)/D1\_QUANT(30) := 30,98/

Campo 10 - Número completo da chave da NFe relativo à última entrada // F1\_ESPECIE;

Campo 11 - Número sequencial do item na NF entrada que corresponde à mercadoria objeto de pedido de ressarcimento// D1\_ITEM;

Campo 12 - Valor unitário da base de cálculo da operação própria do remetente sob o regime comum de tributação// Quando não Tem cálculo do ICMS na entrada, informação vem do campo 08 DO REGISTRO C176.

Campo 13 - Alíquota do ICMS aplicável à última entrada da mercadoria// D1\_PICM porém quando não há cálculo do ICMS PROPRIA na entrada vai pegar informação da alíquota de ICMS-ST (D1\_ALIQSOL).

Campo 14 - (corresponde ao menor valor entre os campos VL\_UNIT\_BC\_ST e VL\_UNIT\_BC\_ICMS\_ULT\_E )// Neste caso é uma validação do campo 08 com campo 09. 18,67;

Campo 15 - equivalente a multiplicação entre os campos 13 e 14// (Campo 14 \* campo 13)/ 100 . (18,67\*18)/100;

Campo 16 - Alíquota do ICMS ST relativa à última entrada da mercadoria// D1\_ALIQSOL := 18;

Campo 17 - Valor unitário do ressarcimento (parcial ou completo) de ICMS decorrente da quebra da ST // (Campo 09(30,98) \* Campo 16(18)/100 := 5,57) - CAMPO 15 := 2,216;

|C176|55|2|3|12122017|SA2010002 02|4,000|18,670|30,980||001|18,67|18,00|18,67 campo- 14 |3,361|18,00|2,216|1|1||||||||

**Registro C197:**

|C197|SP10090721 Crédito relativo à operação própria do Substituto em operação interestadual promovida pelo contribuinte substituído. Artigo 271 do RICMS/00|0010 01|0|0|13,44|0|

Campo 07 - Campo 15 \* campo 07 do registro C176//3,361 \* 4 := 13,44

|C197|SP10090719| Ressarcimento de substituição tributária, por estabelecimento de contribuinte substituído. Artigos 269 e 270 do RICMS/00|0010 01|0|0|8,86|0|

Campo 07 - Campo 17 \* campo 07 do registro C176// 2,216 \* 4 := 8,86.

Segue abaixo um demonstrativo para a geração do registro C176.

<https://tdn.totvs.com/display/public/PROT/ARQ0005_Gerar_Registro_C176_Do_SPED_FISCAL>
