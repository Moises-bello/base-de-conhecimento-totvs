---
article_id: 360054179894
category: Escrita Fiscal - Impostos - ISS
content_hash: c465510d606744da0cae864ad3348072b4822e9e5e81a36315ae6d637abb7e13
fetched_at: '2026-06-28T22:39:35.308435+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: MP - MP - Gravação do Campo FT_CODISS
type: support-article
updated_at: '2021-04-29T18:04:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054179894-MP-MP-Grava%C3%A7%C3%A3o-do-Campo-FT-CODISS
---

**Dúvida**  
Qual o fluxo de gravação do campo FT\_CODISS?  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

O que faz não gravar o código de serviço no campo FT\_CODISS é não ter gravado nos campos D1\_CODISS/D2\_CODISS, pois é preciso gravar primeiro nos campos da SD1 e SD2.   
  
Outro ponto de não gravar é se a configuração utilizada não for uma configuração de serviço.   
Será necessário avaliar as configurações para calcular ISS abaixo, se a espécie utilizada é referente serviço ou SPED, em Brasília-DF é utilizada a espécie SPED na nota de serviço.  
  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027870472-MP-FIS-Reten%C3%A7%C3%A3o-de-ISS>  
  
Outro ponto pode estar relacionado a alguma regra configurada na rotina FISA052 e que esteja forçando o erro.  
  
Ou alguma customização direta ou indireta que possa estar impactando no processo.   
**Abaixo um exemplo do campo FT\_CODISS não ser gravado com o código de serviço:**  
  
Suponhamos que na SX3 (Estrutura de Campos) para o campo FT\_CODISS o campo X3\_VALID esteja com o conteúdo abaixo:   
  
X3\_VALID = ExistCpo("CCQ",M->SFT\_CODISS) 

Ao incluir um documento de entrada o código do ISS será gravado no campo D1\_CODISS corretamente, mas não será gravado no campo FT\_CODISS por motivo da validação contida no X3\_VALID estar diferente do padrão conforme abaixo:   
  
MAFISREF ("LF\_CODISS","MT100",M->FT\_CODISS)   
  
No fonte IMPXFIS existe a regra conforme abaixo:   
  
 If !(AllTrim(X3\_CAMPO) == "F1\_II" .And. ("MAFISREF"$UPPER(X3\_VALID)) .And. aSX6[MV\_EASY] == "S")  
 aadd( aRefSX3 , { aAlias[nX] , AllTrim(X3\_CAMPO) , xFisGetRF(SX3->X3\_VALID)[1] } )  
  
Caso o X3\_VALID esteja diferente do padrão, no momento de gravar informação no campo FT\_CODISS a referencia MAFISREF não será encontrada na validação do campo e o mesmo será desprezado não sendo gravado o conteúdo.    
  
Caso esteja correto as informações acima, será necessário verificar os itens abaixo:  
  
-Verificar se existe alguma regra na rotina FISA052 (Alíquotas do ISS).  
-Verificar se o código de ISS consta na tabela de códigos de ISS  
-Verificar se o código de ISS que consta no produto esta sendo carregado da tabela 60 da SX5 ou CCQ e de onde a consulta padrão buscando.  
-Verificar se esta configurado para utilizar a tabela SBZ conforme configuração do campo MV\_ARQPROD.
