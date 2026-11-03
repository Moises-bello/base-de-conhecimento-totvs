---
article_id: 360016177611
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: ee3b0c0a22d1abe014e7989ef18330dd02e44f8dc09bada78469c01eacca09d0
fetched_at: '2026-06-28T22:42:05.406209+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  como gerar o registro F600, 1300 e 1700 do Sped Contribuições
type: support-article
updated_at: '2023-07-14T13:26:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016177611-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-gerar-o-registro-F600-1300-e-1700-do-Sped-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar o registro F600, 1300 e 1700 do Sped Contribuições?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**Para a correta geração dos registros F600, 1300 e 1700, siga as seguintes orientações:  
1- Verifique os seguintes cadastros:  
  
**CLIENTES**Recolhe Cofins (**A1\_RECCOF**)= Sim  
Recolhe PIS (**A1\_RECPIS**)= Sim  
Recolhe Csll (**A1\_RECCSLL**)= Sim  
  
**PRODUTOS**Retem PIS (**B1\_PIS**)= Sim  
Retem Cofins (**B1\_COFINS**)= Sim  
Retem CSLL (**B1\_CSLL**)= Sim  
  
**TES**Calcula Pis e Cofins (**F4\_PISCOF**) = AMBOS  
Credito de Pis/Cofins, campo (**F4\_PISCRED**)= Não calcula  
Gera Dupl. (**F4\_DUPLIC**) = Sim

**NATUREZA**Calcula PIS (**ED\_CALCPIS**) = Sim  
Percentual de PIS (**ED\_PERCPIS**)= 0,65  
Calcula Cofins (**ED\_CALCCOF**)= Sim  
Percentual de Cofins (**ED\_PERCCOF**)= 3,00  
Calcula CSLL (**ED\_CALCCSL**) = Sim  
Percentual de CSLL (**ED\_PERCCSL**) = 1,00  
Tipo Natureza (**ED\_TIPO**) = 2- Analítico. Caso o campo não seja visualizado deve ser habilitado na tabela **SED** como usado.  
Cond Natureza (**ED\_COND**) = Receita  
Tp Reg. (**ED\_TPREG**) = Não Cumulativo / Cumulativo, conforme campo da TES (**F4\_TPREG**)  
CST COFINS (**ED\_CSTCOF**) = 01 a 49  
CST PIS (**ED\_CSTPIS**) = 01 a 49  
Ind. Cmulat (**ED\_INDCMLT**) = Não Cumulativo / Cumulativo, conforme campo da TES (**F4\_TPREG**)  
Ind. Ret. (**ED\_INDRET**) = 01,02,03,04,05 e 99 >>> Indicador de Natureza da Retenção na Fonte (Campo 02 do Registro F600)  
  
**PARÂMETROS  
MV\_1DUPNAT=SA1->A1\_NATUREZ**  
**MV\_CFAREC** = Informe os CFOPs a serem incluídos, além dos já pré-definidos, para que sejam considerados como receitas no bloco P e no registro 0111 do SPED PIS/COFINS.  
**MV\_CFEREC** = Informe os CFOPs para não que não sejam considerados como receita no bloco P e no registro 0111 do SPED PIS/COFINS.  
  
Estes são os CFOPs que o sistema considera como Receita por padrão:  
  
**Estadual:**5101,5102,5103,5104,5105,5106,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5122,5123,5124,5125,5251,5525,5253,5254,5255,5256,5257,5301,5302,5303,5304,5305,5306,5307,5351,5352,5353,5354,5305,5306,5307,5351,5352,5353,5354,5355,5356,5357,5359,5401,5402,5403,5405,5651,5652,5653,5654,5655,5656.  
  
**Interestadual:**6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,c6112,6113,6114,6115,6116,6117,6118,6119,6120,6122,6123,6124,6125,6251,6252,6253,6254,6255,6256,6257,6258,6301,6302,6303,6304,6305,6306,6307,6351,6352,6353,6354,6355,6356,6357,6359,6401,6402,6403,6404,6501,6502,6651,6652,6653,6654,6655,6656.  
  
**Exterior:**7101,7102,7105,7106,7127,7251,7301,7358,7501,7651,7664.  
  
Caso o CFOP utilizado na nota fiscal não esteja na relação acima, deverá ser incluído no parâmetro **MV\_CFAREC**.  
  
2- Verifique o lançamento da nota fiscal de saída;  
2.1 - Amarre a natureza ao cliente no campo Natureza (**A1\_NATUREZ**).  
2.2 - Gere a nota fiscal de saída utilizando Cliente, Produto e Natureza.  
2.3 - Após realizar faturamento da nota fiscal de saída efetue a baixa do titulo no módulo **Financeiro** - **Contas a receber** (FINA070).  
  
**IMPORTANTE:  
O Registro F600 somente será gerado mediante a baixa/pagamento do título, conforme regras de validação do Guia Prático da Receita Federal, abaixo segue link da consultoria de segmentos da Totvs sobre este assunto:**  
**<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=502440619>**

3- Realize a apuração da EFD Contribuições por meio da rotina FISA001;3.1 - Processe a apuração EFD Contribuições.  
3.2 - Na wizard da rotina, atente-se para a pergunta "Processa Retenções - Saídas" = SIM.  
  
4- Realize a apuração da EFD Contribuições por meio da rotina FISA001;  
  
**Obs.:** As tabelas para análise dos valores das retenções são estas: **SFV**, **SFW** e **CKY**.
