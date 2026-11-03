---
article_id: 360018254351
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 137642f1e148d6ada4f64af4d185ed8f8fb9a97e41757a9ad1af011c2ee0c33c
fetched_at: '2026-06-28T22:42:06.619392+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  NF não estão sendo levadas para o Arquivo do EFD Contribuições para um dos blocos
  A,C e D.
type: support-article
updated_at: '2023-07-14T13:03:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018254351-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-NF-n%C3%A3o-est%C3%A3o-sendo-levadas-para-o-Arquivo-do-EFD-Contribui%C3%A7%C3%B5es-para-um-dos-blocos-A-C-e-D
---

**Dúvida**Notas Fiscais não estão sendo levadas para o Arquivo do **EFD Contribuições** para um dos **blocos A,C e D**.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12.1.7  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Verifique se nas notas fiscais de saída ou entrada, os campos a seguir estão preenchidos na tabela **SFT**:

**FT\_BASEPIS**  
**FT\_BASECOF**  
**FT\_VALPIS**  
**FT\_VALCOF**  
**FT\_ALIQCOF**  
**FT\_ALIQPIS**

Os campos de base **FT\_BASEPIS** e**FT\_BASECOF** são preenchido mediante a configuração dos campos na **TES**:

- **PIS/COFINS (**F4\_PISCOF**) =** Ambos- **Cred. PIS/COF (**F4\_PISCRED**) =** Debita(Saída) / Credita(Entrada)  
  
Especificamente para as **Notas de Entradas**:  
O campo **NAT\_BC\_CRED** (Código da Base de Cálculo do Crédito, conforme a Tabela indicada no item 4.3.7) dos **Blocos A, C e D** do **arquivo txt**, só deve ser preenchido em **documentos que geram créditos**.  
O campo **F4\_CODBCC** deve estar preenchido, assim a informação será gravada no campo **FT\_CODBCC.**  
Para os campos **FT\_ALIQCOF** e**FT\_ALIQPIS,** o sistema considera as alíquotas dos parâmetros:  
**MV\_TXPIS** = 1.65 ou 0.65   
**MV\_TXCOFIN** = 7.60 ou 3.00

Ou do produto, conforme cadastro a seguir:  
**Perc. Cofins** (**B1\_PCOFINS**) = ?  
**Perc. Pis** (**B1\_PPIS**) = ?

Os campos de valores **FT\_VALPIS** e**FT\_VALCOF** considera o resultado de multiplicação da base de cálculo x alíquota.

Há uma exceção para alguns CST's que não preenchem a base de cálculo ou não preenchem nem um dos campos mencionados, mas mesmo assim devem ser levadas no arquivo **EFD Contribuições**.   
A seguir seguem os exemplos:

CST **04** e **06** (alíquota zero), somente a base de cálculo será preenchida para essas notas fiscais.

CST **07,08** e **09** (isenta e sem tributação), nenhum dos campos citados serão preenchidos.

2. Verifique também se os campos de **CST**(**FT\_CSTPIS**, **FT\_CSTCOF**) estão preenchidos com conteúdo de **01** a **49** para notas de saída. Para as notas de entrada os campos devem conter o CST de **50** a **66**.Os campos são preenchidos mediante a cadastro da TES, nos campos**Sit Trib Pis** e **Sit Trib Cof**.

3. Essa regra é valida somente para as notas de saída. Se o **CFOP** da nota de saída não constar na relação abaixo deverá ser informado no parâmetro **MV\_CFAREC,**se os **CFOPs** não estiverem entre os a baixos, devera informar no parâmetro os **CFOPs** para levar as notas fiscais ao arquivo do **EFD Contribuições**.

Exemplo de preenchimento do parâmetro:

**MV\_CFAREC** = 5925,6949,5949

Estadual:  
5101,5102,5103,5104,5105,5106,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5122,5123,5124,5125,5251,5525,5253,5254,5255,5256,5257,5301,5302,5303,5304,5305,5306,5307,5351,5352,5353,5354,5305,5306,5307,5351,5352,5353,5354,5355,5356,5357,5359,5401,5402,5403,5405,5651,5652, 5653,5654,5655,5656.  
  
Interestadual:  
6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6122,6123,6124,6125,6251,6252,6253,6254,6255,6256,6257,6258,6301,6302,6303,6304,6305,6306,6307,6351,6352,6353,6354,6355,6356,6357,6359,6401,6402,6403,6404,6501,6502,6651,6652,6653,6654, 6655,6656.  
  
Exterior:  
7101,7102,7105,7106,7127,7251,7301,7358,7501,7651,7664.

 4. Confira se o parâmetro da *wizard* está **Indicador NFe/Cupom= 2- individ**  
  
5. Verifique o campo **Livro** da *Wizard* da apuração e da geração do arquivo que deve estar preenchido com asterisco " **\*** ", se estiver vazio, pode deixar de levar registros (notas fiscais) ou valores a apuração e no arquivo do SPED.  
  
6. O campo **Atual.Ativo** da **TES** deve estar igual a "Não", caso esteja igual a "SIM", o sistema não irar considera a nota nos registros **A100, C100, D100,** pois com o campo igual "SIM" significa a entrada de um ativo, portanto será levado no registro **F120 (Depreciação do ativo)** ou **F130** (aquisição do ativo).

7. Para notas do **regime Cumulativo Caixa**, verificar se os campos **ED\_APURPIS** e **ED\_APURCOF** foram preenchidos no cadastro da natureza, pois o não preenchimento desse campo irar impactar a geração dos valores das notas fiscais na apuração e nos registros arquivo do **EFD Contribuições**.
