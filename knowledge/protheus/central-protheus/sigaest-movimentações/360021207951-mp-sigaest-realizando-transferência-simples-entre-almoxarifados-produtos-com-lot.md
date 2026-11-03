---
article_id: 360021207951
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 193086adc0c4a812caf4d99b9f8a0f8fbd1d48274f9921b968b00c0006ebcd30
fetched_at: '2026-06-28T22:38:54.190332+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - Realizando Transferência Simples entre Almoxarifados (produtos
  com lote) MATA260
type: support-article
updated_at: '2021-04-28T15:45:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021207951-MP-SIGAEST-Realizando-Transfer%C3%AAncia-Simples-entre-Almoxarifados-produtos-com-lote-MATA260
---

**Dúvida**Como realizar transferência entre Almoxarifados para produtos com lote?

**Ambiente**

Protheus - Estoque/Custos - Release 12.1.17

**Solução**

Para solucionar essa dúvida, vamos exemplificar em passos:  
  
Partindo da premissa que exista saldo para o produto nos dois armazéns envolvidos (não necessariamente precisa ter Lote no armazém destino):

**1. Acesse a rotina Transferência Simples (MATA260)**

```
- Selecione o PRODUTO \ Código do Armazém na Origem;  
- Preencha o campo "Armazém Destino" com o Código do Armazém Destino;  
- Defina, Lote e Quantidade Primária para a transferência e confirme a tela.
```

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000624622/mceclip1.png)

**2. Acesse a rotina  Saldo\ Atual (MATA225)**

```
- Pesquise pelo PRODUTO-01;  
- Verifique os Resultados em ambos armazéns.
```

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101726393/mceclip2.png)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
