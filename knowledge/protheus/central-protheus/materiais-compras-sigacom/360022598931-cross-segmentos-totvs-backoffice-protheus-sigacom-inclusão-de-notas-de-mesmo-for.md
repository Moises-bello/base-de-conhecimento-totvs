---
article_id: 360022598931
category: Materiais - Compras (SIGACOM)
content_hash: 604d32a5030cd5be11e4fd8887dfb217a7113b2781f693325ba6be0e6a7ff322
fetched_at: '2026-06-28T22:41:08.959487+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Inclusão de notas de
  mesmo fornecedor / número de NF / série e loja. Única informação que difere é a
  espécie, porém o sistema "Não" valida a espécie não permitindo que a nota de entrada
  seja lançada.
type: support-article
updated_at: '2025-11-26T16:41:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022598931-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Inclus%C3%A3o-de-notas-de-mesmo-fornecedor-n%C3%BAmero-de-NF-s%C3%A9rie-e-loja-%C3%9Anica-informa%C3%A7%C3%A3o-que-difere-%C3%A9-a-esp%C3%A9cie-por%C3%A9m-o-sistema-N%C3%A3o-valida-a-esp%C3%A9cie-n%C3%A3o-permitindo-que-a-nota-de-entrada-seja-lan%C3%A7ada
---

**Dúvida**Inclusão de notas de mesmo fornecedor / número de NF / série e loja. Única informação que difere é a espécie, porém o sistema "Não" valida a espécie não permitindo que a nota de entrada seja lançada.  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**Para que o sistema permita e não gere chave duplicada na inclusão da segunda NF Eletrônica com o mesmo número, série da nota, código e loja do cliente/fornecedor, adicione um zero à esquerda no número da série.

Conforme análise o sistema atualmente não permite que seja incluída uma mesma numeração de documento de entrada, pois existe uma integridade (chave única) na tabela SF1 (F1\_FILIAL+F1\_DOC+F1\_SERIE+F1\_FORN+F1\_LOJA) que não permite tal processo. Porém como solução o cliente poderá incluir o documento de entrada seguindo o exemplo abaixo:

Nota 1:  
• Numero: 1  
• Série: 1  
• Fornecedor: F01  
• Loja:01

Nota 2:

• Numero: 1   
• Série: 01 --> Adicionando um zero a esquerda  
• Fornecedor: F01  
• Loja:01

Nota 3:

• Numero: 1   
• Série: 001 --> Adicionando dois zeros a esquerda  
• Fornecedor: F01  
• Loja:01

Nota 4: Caso não seja possível incluir mais zeros a esquerda o cliente poderá realizar o seguinte procedimento.

• Numero: 1  
• Série: 111  
• Fornecedor: F01  
• Loja:02 - Incluir o mesmo fornecedor informando a loja 02 ou utilizar um novo código de fornecedor.

***Saiba Mais :***

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
