---
article_id: 10264858652311
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 17e331f015ba49c712b1a1d236a5bcf462d69eeb2e922139e7426b32adf01ae4
fetched_at: '2026-06-28T22:39:41.262825+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Geração de título
  PR ao eliminar saldo do PO
type: support-article
updated_at: '2023-01-02T17:31:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10264858652311-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Gera%C3%A7%C3%A3o-de-t%C3%ADtulo-PR-ao-eliminar-saldo-do-PO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00min****Dúvida**Ao utilizar a rotina Eliminar Saldo no *Purchase Order*, o sistema está gerando o título PR mesmo com o sistema parametrizado para não gerar títulos provisórios.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – A partir da versão 12.1.27  
  
**Solução**Foi feita uma alteração para, antes de chamar a função responsável por gerar um título provisório, verificar se o parâmetro **MV\_EASYFPO** está ou não habilitado. Em caso afirmativo, o título será gerado.

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1087426>; 12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1087424>; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1087425>;

**Saiba mais**[DTRADE-8449 DT Parametrização na geração de título PR ao eliminar saldo de PO](https://tdn.totvs.com/pages/releaseview.action?pageId=721022391)
