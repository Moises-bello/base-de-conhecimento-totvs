---
article_id: 360039212114
category: PMS - Projetos
content_hash: 6e7b1a508cd0869ce97bae2d2997d5dbf79d37e0be2dcd7d3ccc3c0b740ce947
fetched_at: '2026-06-28T22:37:14.931819+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Help PMSQTNF no Documento
  de Entrada
type: support-article
updated_at: '2024-02-23T12:35:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039212114-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Help-PMSQTNF-no-Documento-de-Entrada
---

**Ocorrência**

Sistema apresenta help **PMSQTNF**, como corrigir?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 11.80  
  
**Causa**

O sistema avalia o conteúdo da quantidade dos campos **AFN\_QUANT** e **D1\_QUANT**, caso estas informações estejam diferentes ou se utilizar mais de duas casas decimais e não estiver adaptadas nestas duas tabelas **AFN**, **SD1**, ocorre a mensagem - **PMSQTNF** - não permitindo concluir o Documento de Entrada.  
  
**Solução**

Para correção realize o procedimento:

     1° Verifique se os campos **AFN\_QUANT** e **D1\_QUANT**estão com as mesmas quantidades;  
     2° Se utilizar mais de duas casas decimais no campo **D1\_QUANT,**adapte também ao campo **AFN\_QUANT** .

![Gravar-_426.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4411703431703)
