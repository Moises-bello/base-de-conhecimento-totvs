---
article_id: 360018411671
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: c00817b3c1c093e140c26096dadceb3da4934acae4d320ff8f105d7289f7f8b3
fetched_at: '2026-06-28T22:42:05.419254+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  como gerar os registros F500, F525 e 1900 via Faturamento?
type: support-article
updated_at: '2025-08-05T19:13:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018411671-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-gerar-os-registros-F500-F525-e-1900-via-Faturamento
---

**Dúvida**Como gerar o registro F500, F525 e 1900 via faturamento?

**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.

**Solução**Para gerar o registro **F500** via **Faturamento,** é preciso que além de PIS e COFINS, incida sobre a operação I**SS, ICMS ou IPI**.   
  
Apenas quando houver incidência de um desses tributos no documento fiscal (ainda que não tributados) é que o F500 deve ser gerado via **Faturamento.** Caso haja incidência apenas de PIS/COFINS, o processo deve ser feito pelo módulo **Financeiro**, conforme link abaixo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038654813-MP-SIGAFIN-Como-gerar-registro-F500-e-F525>  
  
Para gerar o registro via Faturamento, realize o seguinte processo:

1. Altere no **Configurador** os parâmetros:  
**MV\_M996TPR** =1, assim o sistema buscará as informações da **TES;  
MV\_TXPIS =** 0.65 (separado por ponto); **MV\_TXCOFIN =** 3.00 (separado por ponto);  
**MV\_1DUPNAT =** A1\_NATUREZ ou C5\_NATUREZ.

2. Crie uma TES com as configurações abaixo:  
**Gera Dupl.** (**F4\_DUPLIC**) = Sim;  
**Livro ICMS, IPI ou ISS** = diferentes de **Não** -> Deve ser configurado no campo de um dos livros com opção diferente de não para geração dos valores de PIS COFINS nas tabelas **SF3** e **SFT**;  
**PIS/COFINS** (**F4\_PISCOF**) = Ambos;  
**Cred. PIS/COF** (**F4\_PISCRED**) = Debita(Saída);  
**Tp Regime** (**F4\_TPREG**) = Cumulativo  
**Sit trib PIS F4\_CSTPIS** = Saida (01 a 49);  
**Sit. trib. COF F4\_CSTCOF** = Saida (01 a 49).

3. Crie uma natureza no módulo financeiro, preenchendo os campos conforme abaixo:  
**Apur. Pis** (**ED\_APURPIS**)= DEBITO;  
**Apur. Cofins** (**ED\_APURCOF**)=DEBITO;  
**% Ap. PIs** (**ED\_PCAPPIS**) = 0,65;  
**% Ap. Cofins** (**ED\_PCAPCPF**) = 3,00;  
**Tipo Naturez** (**ED\_TIPO**) = cumulativa;  
**Cond Naturez** **(ED\_COND**) = Receita;  
**Tp Reg** (**ED\_TPREG**) = Cumulativo;  
**CST Cofins** (**ED\_CSTCOF**) = 01 a 49;  
**CST Pis** (**ED\_CSTPIS**) = 01 a 49;  
**Ind Cmulat** (**ED\_INDCMLT**) = cumulativo;

4. Realize o vinculo da natureza criada:  
Caso escolha o parâmetro **MV\_1DUPNAT** como **A1\_NATUREZ**, vincule utilizando o campo **Natureza** no cadastro de Cliente (**TABELA SA1**);  
Caso escolha o parâmetro **MV\_1DUPNAT** como **C5\_NATUREZ**, vincule utilizando o campo **Natureza** no momento em que realizar o pedido de venda (**TABELA SC5**).

5. Acesse o módulo de Faturamento:  
Realize o pedido de venda utilizando **TES** configurada;  
Processe o **documento de saída** gerando a **Nota Fiscal**.

6. Acesse o módulo Financeiro:  
Realize a baixa do título gerado.

7. Verificação da CFOP se é considerada como receita.  
  
**MV\_CFAREC** = Informar os CFOPs para serem incluídos, além dos já pré-definidos, para considerar como receitas no bloco P e no registro 0111 do SPED PIS/COFINS.  
  
Lembrando que as CFOP´s consideras pelo padrão no Protheus grvados nos campos FT\_CFOP e F3\_CFO  
  
Estadual:  
5101,5102,5103,5104,5105,5106,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5122,5123,5124,5125,5251,5525,5253,5254,5255,5256,5257,5301,5302,5303,5304,5305,5306,5307,5351,5352,5353,5354,5305,5306,5307,5351,5352,5353,5354, 5355,5356,5357,5359,5401,5402,5403,5405,5651,5652,5653,5654,5655,5656.  
  
Interestadual:  
6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,c6112,6113,6114,6115,6116,6117,6118,6119,6120,6122,6123,6124,6125,6251,6252,6253,6254,6255,6256,6257,6258,6301,6302,6303,6304,6305,6306,6307,6351,6352,6353,6354,6355,6356,6357,6359, 6401,6402,6403,6404,6501,6502,6651,6652,6653,6654,6655,6656.  
  
Exterior:  
7101,7102,7105,7106,7127,7251,7301,7358,7501,7651,7664.

8. Acesse o Módulo Livros Fiscais, Apuração EFD Contribuições, Processe a apuração preenchendo as principais perguntas conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013689312)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013689452)  
Confirme a apuração.

9. Gere o arquivo **EFD Contribuições** dentro da rotina de apuração, preencher os principais campos conforme a seguir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013708231)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013689612)

10. **Importante**: Os registro F500 e F525 são gerados através da baixa dos títulos, pois trata-se regime caixa, onde serão considerados na apuração somente os títulos recebidos.
