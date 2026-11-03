---
article_id: 360051274194
category: Gestão de Transportes (TMS)
content_hash: 151b74bf4949b562b3cb4a15ca3f7b28e381324faf74c4bab43d171d4636f6be
fetched_at: '2026-06-28T22:45:27.640462+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - CTE de Redespacho
type: support-article
updated_at: '2021-12-14T17:19:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051274194-Log%C3%ADstica-Linha-Protheus-TMS-CTE-de-Redespacho
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como emitir **CT-e - Conhecimento de Transporte eletrônico** de **Redespacho**no **TOTVS Logística TMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O **CT-e de Redespacho** é utilizado quando uma transportadora contrata uma segunda transportadora para atender parte do trecho do transporte de um frete. Esse tipo de situação se faz necessário quando a transportadora que iniciou a prestação do serviço não pode finalizá-lo por motivos operacionais.Para gerar um **CT-e de Redespacho**no **TOTVS Logística TMS,**é necessário efetuar os seguintes cadastros:

* Acesse a rotina no menu **Atualizações/Doctos e Regras/Regras Por Cliente - TMSA600**, e inclua uma regra por cliente da seguinte maneira:   
    
  + **Cliente - DV1\_CODCLI** = Cliente genérico;
  + **Docto Transp. - DV1\_DOCTMS** = **2 - CTRC**;
  + **Regra Trib. - DV1\_REGTRI** = Selecione a regra de tributação definida para o **CT-e**;
  + **Tipo da NFC - DV1\_TIPNFC** = **5 - Redespacho**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080444634/mceclip0.png)

* Acesse a rotina no menu **Atualizações/Cadastros/Clientes - MATA030 - Clientes**e cadastre o despachante e o destinatário do documento como clientes;
* Acesse a rotina no menu **Atualizações/S.A.C./Solicitantes - TMSA440** e cadastre o destinatário como solicitante.
* Acesse a rotina no menu **Atualizações/S.A.C./Endereços de Solicitante - TMSA450**e vincule o destinatário ao despachante. É importante preencher o campo **Cd. Município - DUL\_CODMUN** pois esta informação é utilizada na montagem do **CT-e**.

Para gerar o documento, é necessário incluir um documento na rotina **Entrada de Documentos - TMSA050**, atentando-se aos campos:

* Preencher o campo **DTC\_SQEDES - Seq. End. Dest.** selecionando os dados do despachante ou recebedor;
* Preencher o campo **DTC\_TIPNFC - Tipo Nf Cliente** = **05 - Redespacho.**

Ao gerar o **CT-e,** verifique no **XML** do **CT-e** que a *tag***<tpServ>** estará com conteúdo 2 e a *tag* **<receb>** estará informando os dados da transportadora contratada. Essas informações são exigidas na validação para autorização do **CT-e** de **Redespacho** pelos órgãos autorizadores.
