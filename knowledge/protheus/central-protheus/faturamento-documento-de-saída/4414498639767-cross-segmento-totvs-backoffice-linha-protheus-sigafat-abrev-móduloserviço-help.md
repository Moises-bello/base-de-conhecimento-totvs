---
article_id: 4414498639767
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 61e6742c06cb39dffd2c124549f369db1b1b74c5c7e562b4c642abea76c8516b
fetched_at: '2026-06-28T22:38:43.835624+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Abrev. Módulo/Serviço
  - Help MV_CFOVEND
type: support-article
updated_at: '2021-11-30T16:04:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414498639767-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Abrev-M%C3%B3dulo-Servi%C3%A7o-Help-MV-CFOVEND
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao emitir o documento de saída o sistema informa uma help com o nome do parâmetro **MV\_CFOVEND**.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

O parâmetro **MV\_CFOVEND** é o Parâmetro que contém os **CFOP´s** de **INSS AgroIndústria**, o mesmo é chamado de um rdmake de exemplo através do ponto de entrada **SF2460I.**

A utilização do parâmetro está logo abaixo dentro do fonte:

**\_cParam := alltrim(getmv("MV\_CFOVEND",.F.,""))**

***//Este parâmetro é do tipo caractere que receberá número de CFOP** **INSS AgroIndústria***

**// Totaliza Valor do INSS do item (verifica se é CFO p/ INSS AgroIndústria)  
  
        if SD2->D2\_VALINS<>0 .and.\_cfoVend$\_cParam  
            \_nTotINSS := \_nTotINSS + SD2->D2\_VALINS   
  
        dbselectarea("SD2")  
        reclock("SD2",.f.)  
        SD2->D2\_VALINS := 0  
        SD2->D2\_ALIQINS:= 0  
        msUnlock()             
        endif  
  
        dbselectarea("SD2")  
        dbSkip()**

Todavia, este rdmake de ponto de entrada, ***não funciona em ambiente Brasil***, o mesmo foi desenvolvido para tratar apenas o **ambiente do país localizado México**, por isso, se tentar compilar o rdmake  no Vs-CODE, poderá gerar  erro de falta do parâmetro ou de falta do campo **F4\_MSEGURA**, ***que no dicionário Brasil não existe e não é utilizado***.  
  
O ponto de entrada **SF2460I** é chamado tanto pelo **mata461** e **mata468N,** mas para o uso de INSS Agroindustria**,  somente será utilizado no país localizado México,** conforme trecho da chamada na rotina **mata461**:  
  
**//³Para a localização México, será processada a função do ponto de entrada SF2460I no padrao.³**  
**//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ**  
**If cPaisLoc == "MEX"**  
**RcFatMex()**  
**Endif**  
  
Neste caso, se precisar utilizar um ponto de entrada na geração da nota, deverá avaliar outro que trabalhe em RPO ambiente Brasil ou terá que adaptar o rdmake para a necessidade do ambiente.

Na documentação abaixo, tem os pontos mais utilizados e o link geral para demais pontos de entrada do módulo:

**[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Lista de Pontos de Entrada (customização) do Modulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028794472)**
