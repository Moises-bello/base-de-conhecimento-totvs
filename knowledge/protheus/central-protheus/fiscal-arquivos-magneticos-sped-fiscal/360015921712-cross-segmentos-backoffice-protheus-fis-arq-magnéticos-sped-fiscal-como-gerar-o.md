---
article_id: 360015921712
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: bd29c6f3234105a3977904b4cdc278c76ffaab5e874acacf72ec08686c56f090
fetched_at: '2026-06-28T22:42:02.506959+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL-
  Como Gerar o Registro D100 do Sped Fiscal
type: support-article
updated_at: '2025-02-11T21:35:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015921712-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-Gerar-o-Registro-D100-do-Sped-Fiscal
---

**Dúvida**  
Como gerar o registro D100 do Sped Fiscal?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Segue abaixo passo a passo para a geração do registro D100 para Documentos de Entrada:  
  
1. Verifique se a espécie utilizada no lançamento do documento, é uma espécie válida para este registro. O **registro D100** do **SPED Fiscal** é gerado para todos os documentos de entrada com a espécie (**CTR**, **CTA**, **CA**, **CTF**, **CTM**e **CTE**);  
  
2. Verifique o preenchimento dos campos do **registro D100** por meio da rotina Nota fiscal de Conhecimento de Frete (**MATA116**);

![](https://tdn.totvs.com/download/attachments/346489571/2.png?version=1&modificationDate=1521383186000&api=v2)  
  
Registro que utilizaremos como modelo:

|D100|0|1|SA20100131501|57|00|000||200|35180704876970000378570000000002001000136216|02072018|02072018|0||1202,73|0|1|1202,73|1202,73|144,33|0||43030014|3556503|3556503|  
  
2.1: Campo 1 (**REG**): Texto fixo contendo "**D100**";  
  
2.2: Campo 2 (**IND\_OPER**): Preenchido com 0 para entradas e 1 para saídas;  
  
2.3: Campo 3 (**IND\_EMIT**): Preenchido de acordo com o campo Form. Próprio. Quando o campo Form. Próprio igual a "Não", o registro **D100** será gerado com o campo **IND\_EMIT** = 1, quando o campo Form. Próprio igual a "Sim", o campo será gerado com **IND\_EMIT** = 0;  
  
2.4: Campo 4 (**COD\_PART**): Preenchido de acordo com o fornecedor do conhecimento de transporte;  
  
2.5: Campo 5 (**COD\_MOD**): Códigos dos modelos do documento fiscal que podem ser utilizados;  
  
Este registro é gerado a partir do Livro Fiscal e é composto de Notas Fiscais dos seguintes modelos:  
Nota Fiscal de Serviço de Transporte, Modelo 7 - **Espécie= NFST**

* Conhecimento de Transporte Rodoviário, Modelo 8 - **Espécie = CTR**.
* Conhecimento de Transporte Aquaviário, Modelo 9 - **Espécie = CTA**.
* Conhecimento de Transporte Aéreo, Modelo 10 - **Espécie = CA**.
* Conhecimento de Transporte Ferroviário, Modelo 11 - **Espécie = CTF**.
* Conhecimento Multimodal de Cargas, Modelo 26 - **Espécie= CTM**.
* Conhecimento de Transporte Eletrônico CTe, Modelo 57 - **Espécie = CTE**.

2.6: Campo 6 (**COD\_SIT**): Código da situação do documento fiscal;

* 00 Documento regular
* 01 Documento regular extemporâneo
* 02 Documento cancelado
* 03 Documento cancelado extemporâneo
* 04 NF-e ou CT-e - Denegado
* 05 NF-e ou CT-e - Numeração inutilizada
* 06 Documento Fiscal Complementar
* 07 Documento Fiscal Complementar extemporâneo.
* 08 Documento Fiscal emitido com base em Regime Especial ou Norma Específica

Segue abaixo, documento para auxiliar no preenchimento  
[SPDFBC0003\_Como\_o\_sistema\_determina\_a\_situação\_do\_documento?\_Campo\_06\_(COD\_SIT)\_do\_registro\_C100](http://tdn.totvs.com/pages/viewpage.action?pageId=6076083)2.7: Campo 7 (**SER**): Série do documento fiscal;  
  
2.8: Campo 8 (**SUB**): Subsérie do documento fiscal - Este campo não tem preenchimento, seu conteúdo é vazio;  
  
2.9: Campo 09 (**NUM\_DOC**): Número do documento fiscal;  
  
2.10: Campo 10 (**CHV\_CTE**): Chave do Conhecimento de Transporte Eletrônico ou do Bilhete de Passagem Eletrônico. Preenchido de acordo com o campo (**FT\_CHVNFE**);  
  
2.11: Campo 11 (**DT\_DOC**): Data da emissão do documento fiscal. Esse campo é preenchido através do (**FT\_ENTRADA**);  
  
2.12: Campo 12 (**DT\_A\_P**): Data da aquisição ou da prestação do serviço. Esse campo é preenchido através do (**FT\_ENTRADA**);  
  
2.13: Campo 13 (**TP\_CT-e**): Tipo de Conhecimento de Transporte;  
  
2.14: Campo 14 (**CHV\_CTE\_REF**): Chave do CT- e de referência cujos valores foram complementados (opção “1” do campo anterior) ou cujo débito foi anulado (opção “2” do campo anterior) ou do Bilhete de Passagem Eletrônico substituído;  
  
2.15: Campo 15 (**VL\_DOC**): Valor total do documento fiscal;  
  
2.16: Campo 16 (**VL\_DESC**): Valor total do desconto. Esse campo é preenchido através do campo (**FT\_DESCON**)**;**2.17: Campo 17 (**IND\_FRT**): Indicador do tipo do frete: 0- Por conta de terceiros; 1- Por conta do emitente; 2- Por conta do destinatário; 9- Sem cobrança de frete;

Na aba informações da DANFE:

![](http://tdn.totvs.com/download/thumbnails/346489571/danfe.png?version=1&modificationDate=1521383186000&api=v2)

As regras para preenchimento se encontram no link abaixo  
[ARQ0059\_Regra Preenchimento Do Campo 17\_TIPO\_FRT - Nos Registros C100 e D100 No SPEDFISCAL e EFD Contribuições](http://tdn.totvs.com/pages/viewpage.action?pageId=243653535)2.18: Campo 18 (**VL\_SERV**): Valor total da prestação de serviço. Valor total do documento;  
  
2.19: Campo 19 (**VL\_BC\_ICMS**): Valor da base de cálculo do ICMS. Valor preenchido através do campo (**FT\_BASEICMS**);

![](http://tdn.totvs.com/download/attachments/346489571/image2018-3-19_16-55-24.png?version=1&modificationDate=1521489323000&api=v2)

2.20: Campo 20 (**VL\_ICMS**): Valor do ICMS;  
  
2.21: Campo 21 (**VL\_NT**): Valor não-tributado - Totaliza a parte do valor da mercadoria que não foi tributada;

Esse valor é formado quando o campo (**F4\_CONSUMO**) está igual a "S" e suas espécies são 07, 08, 8B, 09, 10, 11, 26 e 57. Somando o valor de todos os campos: **FT\_OUTRICM**+**FT\_OUTRRET**+**FT\_ISENICM**+**FT\_ISENRET** = **VL\_NT**. Caso contrário o registro será preenchido com 0 (Vazio)  
  
2.22: Campo 22 (**COD\_INF**): Código da informação complementar do documento fiscal (campo 02 do **Registro 0450**);  
  
2.23: Campo 23 (**COD\_CTA**): Código da conta analítica contábil debitada/creditada. Esse campo é preenchido através do (**B1\_CONTA**) e (**FT\_CONTA**);  
  
2.24: CAMPOS 24 e 25.

Campo 24 (**COD\_MUN\_ORIG**): Código do município de origem do serviço, conforme a tabela IBGE (Preencher com 9999999, se Exterior)

Campo 25 (**COD\_MUN\_DEST**): Código do município de destino, conforme a tabela IBGE (Preencher com 9999999, se Exterior)

**- Na aba informações adicionais:**

Criação dos campos UF Origem Transporte (**F1\_UFORITR**), Município Origem Transporte (**F1\_MUORITR**), UF Destino Transporte (**F1\_UFDESTR**) e Município Destino Transporte (**F1\_MUDESTR**). Estes campos que irão alimentar os campos 24 e 25 do Sped Fiscal:

![](http://tdn.totvs.com/download/attachments/346489571/5.png?version=1&modificationDate=1521383186000&api=v2)

![](http://tdn.totvs.com/download/attachments/346489571/image2018-3-18_12-5-31.png?version=1&modificationDate=1521385532000&api=v2)

Anexo estão os arquivos do dicionário, para aplicar o UPDDISTR para a criação dos campos.

<https://tdn.totvs.com/display/public/PROT/ARQ0089+-+Como+gerar+registro+D100+-+SPED+FISCAL>
