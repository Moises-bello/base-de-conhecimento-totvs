---
article_id: 8504363847703
category: Gestão de Transportes (TMS)
content_hash: fd90067bf955d3eac7b47752f55979d2623f058444f54b737b2bba7324f5cee0
fetched_at: '2026-06-28T22:45:32.577042+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: 'Logística - Linha Protheus - TMS - Rejeição 481 - IE deve ser informada para
  tomador Contribuinte '
type: support-article
updated_at: '2022-08-29T21:32:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8504363847703-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-481-IE-deve-ser-informada-para-tomador-Contribuinte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min****Ocorrência** **Rejeição 481** na transmissão de **CT-e - Conhecimento de Transporte Eletrônico**.  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**Parametrização/Cadastro inconsistente.  
  
**Solução**Conforme manual do **CT-e** disponibilizado pela **SEFAZ - Secretaria da Fazenda**, se indicador de tomador for igual a **Contribuinte**, *tag* **indIEToma = 1**, será rejeitado o **CT-e** se o tomador indicado, *tag* **toma3** ou **toma4** não possuir informação da **IE - Inscrição Estadual** ou se estiver informado **ISENTO.**Na rotina de cadastro de **Clientes - MATA030**, é necessário verificar os campos **Inscrição Estadual - A1\_INSCR**e **Contribuinte - A1\_CONTRIB** do cliente devedor.  
Se o cliente for contribuinte, campo **Contribuinte - A1\_CONTRIB** igual a **1 - Sim,** será necessário preencher o campo **Inscrição Estadual - A1\_INSCR**com a **IE** do cliente devedor. Caso o cliente não seja contribuinte, campo **Contribuinte - A1\_CONTRIB** igual a **2 - Não**, o campo **Inscrição Estadual - A1\_INSCR** pode ficar em branco ou ser preenchido como **ISENTO.**Após realizar o ajuste necessário no cadastro do cliente, estorne o calculo do documento, calcule-o novamente e transmita novamente.
