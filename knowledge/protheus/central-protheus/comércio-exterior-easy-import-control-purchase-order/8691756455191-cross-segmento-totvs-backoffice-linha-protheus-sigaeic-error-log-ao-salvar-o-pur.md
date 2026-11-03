---
article_id: 8691756455191
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: bf72959bc1bd263b2c85a6484a8cc5b39163eaa297bca56f78ea3c69e5b081fc
fetched_at: '2026-06-28T22:39:41.256070+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Error Log ao salvar
  o purchase order
type: support-article
updated_at: '2022-11-23T10:53:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8691756455191-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Error-Log-ao-salvar-o-purchase-order
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao gravar um purchase order, o erro  "type mismatch on + on BUSCA\_NCM(EICXFUN.PRW)" é exibido.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8691079802135/mceclip1.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
**Solução**

Foi efetuada uma correção na função Busca\_NCM, para que ao ser acionada para um item sem ncm informada, a mesma não gere erro, desta forma mesmo com itens sem ncm, o purchase order será gravado corretamente.

Vale lembrar que a ncm é uma informação obrigatório a partir do processo de Desembaraço, sendo necessário que esta informação seja gravada para os itens.

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1082656>; 12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1082654>; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1082655>;

**Saiba mais**

<https://tdn.totvs.com/display/public/PROT/14881043+DTRADE-8239+DT+Problema+ao+gravar+um+Purchase+Order+com+itens+sem+NCM>
