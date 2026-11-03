---
article_id: 360018070412
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 8611b5c342482e0863f06e56a42f5d43d1dfd41797fb7adae3c8a5a1706e58d0
fetched_at: '2026-06-28T22:38:29.866133+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Parâmetros para Contrato
  de Parceria no Pedido e Orçamento de Vendas
type: support-article
updated_at: '2025-11-18T18:09:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018070412-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Par%C3%A2metros-para-Contrato-de-Parceria-no-Pedido-e-Or%C3%A7amento-de-Vendas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36420278599575)** **Tempo aproximado para leitura:****00:01:00 min**

**Dúvida**  
Quais parâmetros validam critérios do Contrato de Parceria (FATA400) no Pedido e Orçamento de Vendas?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.

**Solução**

Para controlar a edição do preço unitário após a aprovação ou remessa do Contrato de Parceria, utilize os parâmetros abaixo:

* **MV\_HBLCONT** - Indica se o bloqueio de campos será realizado na geração do pedido de venda do contrato de parceria.

1a.Pos = Aprov.;

2a Pos = Rem.

sendo 1=Sim; 2=Não

Exemplo: MV\_HBLCONT= 11

* **MV\_HBLORC -**Indica se permite a alteração do pedido de venda na efetivação do orçamento ou Contrato de Parceria - 1=Permite / 2=Não permite
* **MV\_CPOCONT** - Indica quais os campos do pedido de venda serão bloqueados para o usuário na aprovação ou remessa do contrato de parceria.

**Exemplo:** C6\_QTDVEN|C6\_QTDLIB|C6\_PRCVEN|C6\_PRUNIT|C6\_PRODUTO|C6\_TOTAL

**Outros parâmetros:**

* **MV\_PRCCTR** - Para que não seja obrigatório o pedido de vendas com o mesmo produto e cliente do contrato de parceria exigir o vínculo.
* **MV\_ALTCTR** - Indica se é possível a alteração de preços em pedidos de venda que possuem contrato de parceria.
* **MV\_ACRSDUP** - Indica se o acréscimo financeiro será considerado independente do TES estar configurado com Gera Duplicata igual a Sim ou Não. Este parâmetro pode ser utilizado para que o acréscimo financeiro do Contrato de Parceria seja calculado no Documento de Saída de Remessa, na situação em que a condição de pagamento do Contrato de Parceria considere acréscimo financeiro (E4\_ACRSFIN).

**Saiba mais:**

[Parcerias (FATA400 - SIGAFAT)](https://tdn.totvs.com/x/NBLAFQ)
