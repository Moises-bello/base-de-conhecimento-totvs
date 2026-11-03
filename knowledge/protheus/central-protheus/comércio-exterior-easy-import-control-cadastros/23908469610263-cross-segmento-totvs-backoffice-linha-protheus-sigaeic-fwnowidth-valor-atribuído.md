---
article_id: 23908469610263
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: 48e10c592d9c2413c98e1989ea017dc4eafe68e5d7f879d4771aa894885f07a6
fetched_at: '2026-06-28T22:39:52.210123+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - FWNOWIDTH Valor
  Atribuído Difere do Tamanho de Campo (Descrição)
type: support-article
updated_at: '2024-10-09T16:49:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23908469610263-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-FWNOWIDTH-Valor-Atribu%C3%ADdo-Difere-do-Tamanho-de-Campo-Descri%C3%A7%C3%A3o
---

**Dúvida**Ao tentar gerar o catálogo de lote na rotina de **Catálogo de Produtos** **(EICCP400)** é exibida uma mensagem de Atenção:

"**FWNOWIDTH** **- Valor atribuído difere do tamanho de campo (Descrição)**".

![geração de catalogo em lote.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23908483833751)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – a partir da versão 12.1.27  
  
**Solução**Solicite ao responsável pela manutenção do Protheus em sua empresa verificar o tamanho do campo de descrição do produto nas tabelas **SB1,EKA, EK9** e **EKE** e manter o tamanho dos campos **EKA\_DESC\_I,EKE\_DESC\_I** e **EK9\_DESC\_I** iguais ao tamanho do campo **B1\_DESC**. Após ajustar o tamanho ao salvar o catálogo de produtos, a mensagem não será mais exibida.

**Observação:** A partir da release 12.1.2410, é relevante destacar que os campos **EKA\_DESC\_I,EKE\_DESC\_I** e **EK9\_DESC\_I** foram incluídos no grupo **171, denominado "Descrição do Produto".**  
  
**Saiba mais:**  
[Grupo de campos Release 12.1.2410](https://tdn.totvs.com/pages/releaseview.action?pageId=825927786)
