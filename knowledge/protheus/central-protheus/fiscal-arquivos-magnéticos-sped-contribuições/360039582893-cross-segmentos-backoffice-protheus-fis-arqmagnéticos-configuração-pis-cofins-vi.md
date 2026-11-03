---
article_id: 360039582893
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: df3a3965493fdd177f5cd39de6b6dcb2e39e5fedf17cb7a6b1129dd0470029c0
fetched_at: '2026-06-28T22:42:05.038501+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  PIS COFINS via apuração para correta gravação dos Livros Fiscais (Tabelas SF3 e
  SFT) na geração do EFD Contribuições
type: support-article
updated_at: '2023-01-25T20:28:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039582893-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-PIS-COFINS-via-apura%C3%A7%C3%A3o-para-correta-grava%C3%A7%C3%A3o-dos-Livros-Fiscais-Tabelas-SF3-e-SFT-na-gera%C3%A7%C3%A3o-do-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Configuração PIS COFINS via apuração para correta gravação dos Livros Fiscais (Tabelas SF3 e SFT) na geração do EFD Contribuições.

**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
**Solução:**

**Cadastro de TES**

**Aba Impostos**

**Livro ICMS ou ISS = Diferentes de Não** -> Deve ser configurado campo de um dos livros com opção diferente de não para geração dos valore de **PIS COFINS** nas tabelas **SF3** e **SFT** mesmo que não exista cálculo do imposto na nota fiscal.

 Atenção: Se não existir cálculo de **IPI** o campo **Livro de IPI** deve estar como Não. Devido as validações das do arquivo **GIA**.

**PIS/COFINS (F4\_PISCOF) = Ambos****Cred. PIS/COF (F4\_PISCRED) = Debita (Saída) /Credita (Entrada)**

**Aba Outros**

**Tp Regime (F4\_TPREG) = Cumulativo, Não Cumulativo ou AMBOS (Cumul/N Cumul) Sit. Trib PIS (F4\_CSTPIS) = Entrada (50 a 66) / Saída (01 a 49) lembrando que as CST de credito estão no intervalo 50 a 66 Sit. Trib COFINS (F4\_CSTCOF) = Entrada (50 a 66) / Saída (01 a 49) lembrando que as CST de credito estão no intervalo 50 a 66 Cod Bc cred (F4\_CODBCC) = ? - > Campo deve ser preenchido nas operações de credito "Nota Fiscal de entrada"**

**Atenção:**

Para o cálculo do **PIS COFINS apuração** o sistema verifica primeiro as alíquotas informadas na exceção fiscal, após produto, caso não tenha alíquota, serão verificados os parâmetros **MV\_TXPIS** e **MV\_TXCOFIN**.

**Produto:**

**Perc. Cofins (B1\_PCOFINS) = ?**

**Perc. Pis (B1\_PPIS) = ?**Ou   
  
**Parâmetros:**

**MV\_TXPIS = 1.65 ou 0.65 (separado por ponto)**

**MV\_TXCOFIN = 7.60 ou 3.00**

**Regime Cumulativo utiliza alíquotas de PIS 0,65 e COFINS 3,00**

**Regime Não Cumulativo utiliza alíquotas de PIS 1,65 e COFINS 7,60**

**MV\_M996TPR** : **1-F4\_TPREG / 2-B1\_TPREG / 3-A1\_TPREG** (Informa por onde vai ser tratado tipo de regime pela **TES** (**SF4**), Produto (**SB1**) ou Cliente (**SA1**).

**MV\_CFAREC** = Informar os **CFOP´s** para serem incluídos, além dos já pré-definidos, para considerar como receitas.

Lembrando que as **CFOP´s** consideras pelo padrão no **Protheus**.

Estadual:

**5101,5102,5103,5104,5105,5106,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5122,5123,5124,5125,5251,5525,5253,5254,5255,5256,5257,5301,5302,5303,5304,5305,5306,5307,5351,5352,5353,5354,5305,5306,5307,5351,5352,5353,5354, 5355,5356,5357,5359,5401,5402,5403,5405,5651,5652,5653,5654,5655,5656.**

Interestadual:

**6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6122,6123,6124,6125,6251,6252,6253,6254,6255,6256,6257,6258,6301,6302,6303,6304,6305,6306,6307,6351,6352,6353,6354,6355,6356,6357,6359, 6401,6402,6403,6404,6501,6502,6651,6652,6653,6654,6655,6656.**

Exterior:

**7101,7102,7105,7106,7127,7251,7301,7358,7501,7651,7664.**

Caso **CFOP** utilizada na nota não esteja informado acima deve ser incluída no parâmetro **MV\_CFAREC**.

Informações Adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=6076810>
