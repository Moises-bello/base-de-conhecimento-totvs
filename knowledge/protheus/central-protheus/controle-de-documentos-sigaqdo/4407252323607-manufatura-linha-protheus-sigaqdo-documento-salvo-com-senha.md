---
article_id: 4407252323607
category: Controle de Documentos (SIGAQDO)
content_hash: c230392f6c3340acfa2d22a0a13ed1688aa2cfc942eb0e5140eca3431f118c15
fetched_at: '2026-06-28T22:42:29.024440+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Documento salvo com senha
type: support-article
updated_at: '2021-08-27T13:07:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407252323607-Manufatura-Linha-Protheus-SIGAQDO-Documento-salvo-com-senha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Qual parametrização faz com que o documento seja salvo com senha na rotina **QDOA050 - Cadastro de Documentos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Quando o documento é criado, o Sistema verifica 2 parâmetros:

* **MV\_QSAVPSW - Define se os documentos elaborados pelo Modulo Controle de Documentos serão gravados com senha**, onde aceita os valores **1 - Sim** ou **2 - Não**;
* **MV\_QSAVEDC - Define se os documentos elaborados pelo Modulo Controle de Documentos serão gravados no formato DOC ou em RTF**, onde aceita os valores **1-Doc** ou **2-RTF**.

E conforme a combinação do conteúdo destes parâmetros, o Sistema poderá salvar tanto o documento quanto o arquivo gerado no servidor com extensão **.CEL** com senha, onde:

* Se os parâmetros **MV\_QSAVPSW** e **MV\_QSAVEDC** estiverem com conteúdo igual a **1**, tanto o arquivo **.CEL** quanto o **.DOC** serão gravados **com senha**;
* Se o parâmetro **MV\_QSAVPSW** estiver com conteúdo igual à **1** e o parâmetro **MV\_QSAVEDC** com conteúdo igual à **2**, somente o arquivo **.CEL s**erá gravado **com senha**;
* Se os parâmetros **MV\_QSAVPSW** e **MV\_QSAVEDC** estiverem com conteúdo igual à **2**, os arquivos serão gravados **sem senha**;
* Se o parâmetro **MV\_QSAVPSW** estiver com conteúdo igual à **2** e o parâmetro **MV\_QSAVEDC** com conteúdo igual à **1**, os arquivos serão gravados **sem senha**.
