---
article_id: 360021109171
category: ADVPL - Ponto de Entrada
content_hash: c3a5455c70be0be79f606d3a5d32d5dd00645468efaa31422a6ab018d6b57615
fetched_at: '2026-06-28T22:40:12.788419+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de Entrada
  SPEDPROD gera registro 0200 duplicado
type: support-article
updated_at: '2021-12-29T20:14:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021109171-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-Entrada-SPEDPROD-gera-registro-0200-duplicado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Ao processar o Bloco K no SPEDFISCAL com o ponto de entrada SPEDPROD, o sistema está duplicando os itens no Bloco 0200 afetando a geração também dos blocos K230 e K235.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**As ocorrências de registros **0200** duplicados, ao utilizar o ponto de entrada **SPEDPROD**, se deve ao fato do código do produto no *array* de retorno estar sendo informado de forma incorreta. Deve-se lembrar que a posição referente ao código do produto no registro é composta por código + filial, portanto caso seja informado essa posição com somente o código do produto o sistema entenderá que se trata de um produto isolado, sendo esta a causa mais provável de duplicidade do registro.  
Segue exemplo de implementação;

```
#Include 'Protheus.ch'  
  
User Function SPEDPROD()  
  
local cAlias := iif(len(paramixb) >= 1 , paramixb[1], '')  
local cRegspd := iif(len(paramixb) >= 2 , paramixb[2], '')  
local cUnid := iif(len(paramixb) >= 3 , paramixb[3], '')  
local aProd := {}  
local lFTProduto := .f.  
local lB1Cod := .f.  
local lCodItem := .f.  
local lD2Cod := .f.  
local lCF8Item := .f.  
local cProduto := ""  
  
//Alert("Ponto de entrada SPEDPROD")  
  
do case  
 //Verifica se o campo FT_PRODUTO existe no alias   
 case (cAlias)->(fieldPos('FT_PRODUTO')) > 0   
 cProduto := (cAlias)->FT_PRODUTO  
 //Verifica se o campo B1_COD existe no alias  
 case (cAlias)->(fieldPos('B1_COD')) > 0  
 cProduto := (cAlias)->B1_COD  
 //Verifica se o campo COD_ITEM existe no alias  
 case (cAlias)->(fieldPos('COD_ITEM')) > 0  
 cProduto := (cAlias)->COD_ITEM  
 //Verifica se o campo D2_COD existe no alias  
 case (cAlias)->(fieldPos('D2_COD')) > 0  
 cProduto := (cAlias)->D2_COD  
 //Verifica se o campo CF8_ITEM existe no alias  
 case (cAlias)->(fieldPos('CF8_ITEM')) > 0   
 cProduto := (cAlias)->CF8_ITEM  
endCase  
  
dbSelectArea("SB1")  
SB1->(dbSetOrder(1))  
  
if SB1->(dbSeek(xFilial("SB1") + cProduto) )   
 aAdd(aProd, SB1->B1_COD + cFilAnt) // 1 - Código do Produto  
 aAdd(aProd, "ALTERADO PE SPEDPROD" ) // 2 - Descrição do Produto  
 aAdd(aProd, "" ) // 3 - Código de Barras  
 aAdd(aProd, "" ) // 4 - Código Anterior  
 aAdd(aProd, SB1->B1_UM ) // 5 - Unidade de Medida  
 aAdd(aProd, "99" ) // 6 - Tipo do Item (Tipo SPED)  
 aAdd(aProd, "XX" ) // 7 - Código de NCM  
 aAdd(aProd, "XX" ) // 8 - Exceção da NCM  
 aAdd(aProd, "XX" ) // 9 - Código do Gênero do Item  
 aAdd(aProd, "XX" ) // 10 - Código de ISS  
 aAdd(aProd, "18" ) // 11 - Alíquota de ICMS  
endIf  
   
return aProd
```

Utilizando o código acima, seguem exemplos de implementação correta e incorreta da linha que alimenta o array de retorno com o código do produto;

**Correto:**

```
OBS: Na linha: aAdd(aProd, SB1->B1_COD + cFilAnt) // 1 - Código do Produto   
  
Se utiliza MV_COFLSPD = .T. ou insistente,  
A linha deve estar:  
aAdd(aProd, SB1->B1_COD + cFilAnt) // 1 - Código do Produto  
  
Se utiliza MV_COFLSPD = .F.  
A linha deve estar:  
aAdd(aProd, SB1->B1_COD ) // 1 - Código do Produto 
```
