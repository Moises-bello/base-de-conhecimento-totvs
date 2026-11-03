---
article_id: 10068924744343
category: RH - Relatórios Folha
content_hash: 296a1515123cf1af17c63035c5d7fce0bd8a3208421b5b80f8e64141f4449635
fetched_at: '2026-06-28T22:43:17.430290+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Ao tentar imprimir Relatório de Recibo de Pagamento
  em PDF não gera arquivo
type: support-article
updated_at: '2025-08-04T12:04:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10068924744343-RH-Linha-Protheus-GPE-Ao-tentar-imprimir-Relat%C3%B3rio-de-Recibo-de-Pagamento-em-PDF-n%C3%A3o-gera-arquivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31424992056727) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que ao tentar imprimir Relatório de Recibo de Pagamento em PDF não gera arquivo?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.27. 

**Solução**

Este incidente ocorre pois alguns **arquivos lgrl.bmp**, na pasta SYSTEM, não estão com a configuração correta, impactando assim na impressão do recibo. É necessário verificar se na pasta SYSTEM existem **arquivos lgrl.bmp**, efetuar a exclusão destes arquivos e tentar gerar o recibo de pagamento em PDF.

Verifique também se o arquivo está correto para a filial, se necessário ajuste, ou troque pelo arquivo que impressão é feita corretamente apenas renomeie de acordo com a necessidade e tente imprimir novamente os recibos.  
  
**Saiba Mais:**

[RH - Linha Protheus - GPE - Como imprimir o logotipo da Empresa no Recibo de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007605732-MP-GPE-Como-imprimir-o-logotipo-da-Empresa-no-Recibo-de-Pagamento?source=search)

[RH - Linha Protheus - GPE - Error.log ao gerar o Relatório de Recibo de Pagamento - type mismatch on GPER030(GPER030.PRX)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404441521815-RH-Linha-Protheus-GPE-Error-log-ao-gerar-o-Relat%C3%B3rio-de-Recibo-de-Pagamento-type-mismatch-on-GPER030-GPER030-PRX-?source=search)

[RH - Linha Protheus - GPE - Como configurar uma mensagem no recibo de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016749491-RH-Linha-Protheus-GPE-Como-configurar-uma-mensagem-no-recibo-de-pagamento?source=search)

[RH - Linha Protheus - GPE - Como gerar o recibo de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403751793303-RH-Linha-Protheus-GPE-Como-gerar-o-recibo-de-pagamento?source=search)
