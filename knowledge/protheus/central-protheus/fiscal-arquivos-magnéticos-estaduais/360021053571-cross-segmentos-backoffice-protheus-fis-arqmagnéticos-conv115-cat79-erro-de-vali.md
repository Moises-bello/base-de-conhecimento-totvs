---
article_id: 360021053571
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 7062c77c926c61b6363de55d662d65932b598c96e977c78056c45453efb162c5
fetched_at: '2026-06-28T22:42:10.646950+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - CONV115 - CAT79
  - Erro de validação na utilização ou classificação do item
type: support-article
updated_at: '2022-08-17T20:08:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021053571-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-CONV115-CAT79-Erro-de-valida%C3%A7%C3%A3o-na-utiliza%C3%A7%C3%A3o-ou-classifica%C3%A7%C3%A3o-do-item
---

**Ocorrência**Ao validar o arquivo do **convenio 115** ou **CAT79**, ocorre o seguinte erro:

260 Erro Item 04 18 18 Tipo de Utilização do item é incompatível com o Código de classificação do item

**Ambiente**Protheus - Livros fiscais  – A partir da versão 11.80]  
  
   
 **Solução**

O protheus realiza a seguinte validação para geração dos campos 04 - Fase ou Tipo de Utilização e 14 - Código de classificação do item do arquivo Item.

O protheus verifica primeiramente se a tabela SFX está preenchida. Se estiver, o conteúdo a ser levado no arquivo é o conteúdo da tabela, Se não estiver preenchido será verificado o conteúdo da tabela SA1 e SB5 respectivamente, de acordo com a configuração do parâmetro MV\_D5ICMS.

Para o campo 4, a informação é pega do campo FX\_TIPSERV, onde é realizado um CASE para cada situação pois o que grava de conteúdo no protheus não é exatamente o mesmo que deve ser levado no arquivo:

ITE->I\_FASE  :=    Iif (!Empty(cCmpUti),cCmpUti,Iif(lCmpUti,SA1->(FieldGet (FieldPos (&(SuperGetMv ("MV\_D5ICMS"))[2]))),"1"))

If SFX->(FieldPos("FX\_TIPSERV")) <> 0    .And.    lSFX

      If  substr(cCmpUti,2,len(cCmpUti)) <> (cAliasSFT)->(FT\_NFISCAL+FT\_SERIE+FT\_ESPECIE)

          Do Case

        Case  SFX->FX\_TIPSERV == '0'

            cCmpUti    :=    '1'+(cAliasSFT)->(FT\_NFISCAL+FT\_SERIE+FT\_ESPECIE)

        Case  SFX->FX\_TIPSERV == '1'

            cCmpUti    :=    '2'+(cAliasSFT)->(FT\_NFISCAL+FT\_SERIE+FT\_ESPECIE)

        Case  SFX->FX\_TIPSERV == '2'

            cCmpUti    :=    '3'+(cAliasSFT)->(FT\_NFISCAL+FT\_SERIE+FT\_ESPECIE)

        Case  SFX->FX\_TIPSERV == '3'

            cCmpUti    :=    '4'+(cAliasSFT)->(FT\_NFISCAL+FT\_SERIE+FT\_ESPECIE)

        Case  SFX->FX\_TIPSERV == '4'

            cCmpUti    :=    '5'+(cAliasSFT)->(FT\_NFISCAL+FT\_SERIE+FT\_ESPECIE)

        Case  SFX->FX\_TIPSERV == '9'

            cCmpUti    :=    '6'+(cAliasSFT)->(FT\_NFISCAL+FT\_SERIE+FT\_ESPECIE)

          EndCase

Para geração do campo de Classificação do item é pego dos campos FX\_GRPCLAS+FX\_CLASSIF

ITE->I\_CODCLIT    :=    Iif (!Empty(cCmpClIt),cCmpClIt,Iif(lCmpClIt, SB5->(FieldGet (FieldPos (&(SuperGetMv ("MV\_D5ICMS"))[5]))), Iif(cRotina == "CONV128","5099","0101")))

cCmpClIt    := SFX->( FX\_GRPCLAS+FX\_CLASSIF )
