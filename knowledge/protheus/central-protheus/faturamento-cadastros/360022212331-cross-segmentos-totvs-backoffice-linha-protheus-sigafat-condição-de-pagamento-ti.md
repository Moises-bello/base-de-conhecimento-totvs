---
article_id: 360022212331
category: Faturamento - Cadastros
content_hash: 865f7dadae56258021e0f83af6a28a39ca577a6096261355e37bf854af5dff62
fetched_at: '2026-06-28T22:38:35.576999+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT-Condição de Pagamento
  Tipo A
type: support-article
updated_at: '2023-07-05T17:12:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022212331-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Condi%C3%A7%C3%A3o-de-Pagamento-Tipo-A
---

**Dúvida**Como utilizar a condição do tipo A?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

A condição de pagamento do **tipo A** somente é usada especificamente para os **módulos do DMS ( SIGAVEI, SIGAPEC e SIGAOFI )**, conforme tdn: **[Condição de Pagamento - Tipo A](http://tdn.totvs.com/pages/releaseview.action?pageId=6070566)**

A condição de pagamento do tipo A é usada para habilitar a escolha de novas formas de pagamento como CC = Cartão de Credito, CD = Cartão de Débito, FI = Financiado, CH = Cheque e entre outras formas de pagamento, com isso o tipo dos títulos serão gerados de acordo com a escolha como forma de pagamento.   
  
A mesma é usada no momento da negociação de pagamento, o usuário escolhe essa condição de pagamento Negociada do tipo A, com isso na linha abaixo onde serão gravado os tipos de pagamento, a mesma fica habilitada para escolha de novos tipos de pagamento.  
  
Também é usada para fechamento de tipo de tempo de garantia de peças John Deere, ao escolher uma condição de pagamento tipo A, a rotina utilizará a condição de pagamento informada neste novo parâmetro para montar as parcelas. Isto se faz necessário para que a nota fiscal de garantia de peças seja emitida contra o cliente, mas seu título a receber seja contra a fábrica John Deere.

**Obs: Caso utilize os módulos de DMS, entre em contato com a equipe de Automação Comercial para sanar dúvidas de uso.**
