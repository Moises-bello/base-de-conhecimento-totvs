---
article_id: 360020133751
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 2d7811807612854add1fd97f64480f263a23b6bd2db7ea1d204ed23442e42ae1
fetched_at: '2026-06-28T22:37:19.782870+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como aplicar Fórmulas
  para Multas ou Bonificações no Gestão de Contratos ?
type: support-article
updated_at: '2025-07-28T13:52:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020133751-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-aplicar-F%C3%B3rmulas-para-Multas-ou-Bonifica%C3%A7%C3%B5es-no-Gest%C3%A3o-de-Contratos
---

**Dúvida**Como aplicar Fórmulas para Multas ou Bonificações no Gestão de Contratos ?  
  
**Ambiente**

Microsiga Protheus - Release 12.1.17

**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1 - Efetue o cadastros:

```
- Tipo de Revisão: Multa/Bonificações (CNTA010)  
  
- Tipo de Multas/Bonificações (CNTA050)  
CN4_DESVAL = (CNF->CNF_PRUMED)<(DDATABASE)  - Vinda da Formula Vinculada  
CN4_DESFOR = CNF->CNF_VLPREV*0.2  - Vinda da Fórmula Vinculada
```

Exemplo dos cadastros de Tipo de Multa/Bonificação e Formulas inseridas neste cadastro:

- Fórmulas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33763478176791)

- Tipo de Multa Bonificação (CNTA050):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33763478178711)

2 - Cadastre um novo Contrato de Compra com Cronograma Financeiro;

2.1 - Na aba Multas/Bonificações, vincule o Tipo de Multa (1) e deixe-o Vigente;

3 - Caso o cadastro do contrato já esteja realizado sem Tipo de Multa vinculado, pode-se gerar a Revisão de Multa/Bonificação para vincular o Tipo de Multa ao contrato.

3.1 - Na aba Multa/Bonificações, vincule o Tipo de Multa (1) e aprove a revisão;

4. Com o Tipo de Multa vinculado ao contrato, acesse o módulo SIGAGCT com uma "**Data Base"** acima da **"Data Prevista da Medição"** da parcela a ser medida (***CNF->CNF\_PRUMED***, conforme fórmula cadastrada/vinculada da validação) e efetue a medição desta parcela do Cronograma Financeiro;

4.1 - Verifique na aba "Multa/Bonificação da Planilha" da medição, que foi trazida a multa conforme a fórmula de valor cadastrada;

5. Encerre a medição e verifique a aplicação da multa em Pedido de Compras (C7\_DESPESA) ou Títulos (E2\_DECRESC) gerados (caso o Tipo de Multa possuir configurado campo (CN4\_FLGPED) para "Interf Pedido = Sim").

**Saiba Mais:**

[GCT0079\_Multa\_Bonificacao\_Contrato\_GCT](http://tdn.totvs.com/display/PROT/GCT0079_Multa_Bonificacao_Contrato_GCT)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Formas de geração da Multa ou Bonificação em pedidos de compra ou venda gerado por medição - Parâmetro MV\_MULTMED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028877851-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Formas-de-gera%C3%A7%C3%A3o-da-Multa-ou-Bonifica%C3%A7%C3%A3o-em-pedidos-de-compra-ou-venda-gerado-por-medi%C3%A7%C3%A3o-Par%C3%A2metro-MV-MULTMED)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
