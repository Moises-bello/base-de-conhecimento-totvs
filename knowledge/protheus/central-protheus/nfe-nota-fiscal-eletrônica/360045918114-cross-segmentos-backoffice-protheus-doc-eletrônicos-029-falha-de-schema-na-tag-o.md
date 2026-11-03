---
article_id: 360045918114
category: NFe - Nota Fiscal Eletrônica
content_hash: bff091b72f1fd3bdec7393dcc744857e533796eb513fa36c655793ba59d2ecce
fetched_at: '2026-06-28T22:40:03.746085+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029: Falha de schema
  na Tag orig'
type: support-article
updated_at: '2025-06-12T15:01:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045918114-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-orig
---

**Dúvida**Como solucionar a falha de Schema referente a TAG orig ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**1 - Ao gerar falha de Schema referente ao **orig** verifique se o seu XML gerou conforme o exemplo abaixo:  
  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064840994)  
  
2- Conforme o XML acima não foi preenchido a **origem do produto** que é obrigatória.

**0 -** Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8;  
**1 -** Estrangeira - Importação direta, exceto a indicada no código   
6;  
**2 -** Estrangeira - Adquirida no mercado interno, exceto a   
indicada no código 7;  
**3 -** Nacional, mercadoria ou bem com Conteúdo de Importação   
superior a 40% e inferior ou igual a 70%;  
**4 -** Nacional, cuja produção tenha sido feita em conformidade   
com os processos produtivos básicos de que tratam as   
legislações citadas nos Ajustes;  
**5 -** Nacional, mercadoria ou bem com Conteúdo de Importação   
inferior ou igual a 40%;  
**6 -** Estrangeira - Importação direta, sem similar nacional,   
constante em lista da CAMEX e gás natural;  
**7 -** Estrangeira - Adquirida no mercado interno, sem similar   
nacional, constante lista CAMEX e gás natural.  
**8 -** Nacional, mercadoria ou bem com Conteúdo de Importação   
superior a 70%;  
  
3- Para a correção preencher a origem, campo no cadastro de Produto deve estar preenchido **B1\_ORIGEM "Origem"**  
  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065821393)  
  
4- Após isso, exclua a nota e gere novamente. Se for utilizar o mesmo pedido digite novamente  **produto** para que a **origem** fique correta no pedido.

* **Saiba mais:**

Caso seja emitente do Simples Nacional o procedimento é o mesmo.

1- Verifique se está correto o campo C6\_CLASFIS "**Sit. trib"**este campo deve estar como **exemplo 000**, O primeiro número é referente a **origem do produto e os outros dois referente a situação tributária do ICMS.**

2- Exclua essa nota no pedido de **vendas ou compra digite novamente o TES** e verifique se irá atualizar o campo Sit. trib. com**exemplo 000** conforme abaixo:  
  
  
​![C6_CLASFIS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17429022030999)  
  
3- Se não estiver atualizando é possível **alterar manualmente.**

4- Após isso, gere o **documento e transmita.**
