---
article_id: 360026414073
category: Controle de Documentos (SIGAQDO)
content_hash: f545ed63335cbdf50bbc54be54b23e25e6464fb921095869471602bf59c4fc2c
fetched_at: '2026-06-28T22:42:29.207744+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Numeração automática do código do documento
type: support-article
updated_at: '2021-05-26T11:58:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026414073-Manufatura-Linha-Protheus-SIGAQDO-Numera%C3%A7%C3%A3o-autom%C3%A1tica-do-c%C3%B3digo-do-documento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:00 min****Dúvida**Como gerar a numeração automática para o documento na rotina **QDOA050 - Cadastro de Documentos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Para que o campo **Cod Doc** **- QDH\_DOCTO** seja preenchido automaticamente, com um código sequencial é necessário:

* Alterar o parâmetro **MV\_QNSEQDC - Define se o número do Documento será sequencial, e de acordo com a sequencia especificada no Cadastro de Tipo de Document**o para **S**;
* Informar o sequencial no campo **Qtde Num Seq - QD2\_QSEQ** e a sigla no campo **Sigla Doc - QD2\_SIGLA** na rotina **QDOA020 - Tipo de Documento**.
