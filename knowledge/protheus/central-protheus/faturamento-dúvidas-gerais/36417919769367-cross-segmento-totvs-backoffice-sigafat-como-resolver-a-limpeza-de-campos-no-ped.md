---
article_id: 36417919769367
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b1663562bc4a41fe52e4856b80a483ad4a023ce6675394216234ec6ea7d639f7
fetched_at: '2026-06-28T22:38:28.722032+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice - SIGAFAT - Como resolver a limpeza de campos
  no pedido de venda vinculados a um contrato de parceria (FATA400)
type: support-article
updated_at: '2025-11-18T18:03:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36417919769367-Cross-Segmento-TOTVS-Backoffice-SIGAFAT-Como-resolver-a-limpeza-de-campos-no-pedido-de-venda-vinculados-a-um-contrato-de-parceria-FATA400
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36417919756951) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**

No Pedido de Vendas que possui contrato de parceria, ao alterar a condição de pagamento, alguns campos do pedido de venda são limpos/zerados.

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Causa**

Caso seja informada uma condição de pagamento que não esteja vinculada a um contrato de parceria no Pedido de Vendas (MATA410) gerado a partir desse contrato, os campos "Preço Unitário (**C6\_PRCVEN**)", "Tipo Saída (**C6\_TES**)", "No. Contrato (**C6\_CONTRAT**)" e "Item Contr (**C6\_ITEMCON**)" deverão ser limpos automaticamente.

Essa verificação é realizada pelo gatilho do campo Condição de Pagamento (C5\_CONDPAG), por meio das validações da rotina, que identifica se a condição de pagamento informada possui vínculo com algum contrato de parceria.

O parâmetro **MV\_PRCCTR**, responsável pela captação do Contrato de Parceria, quando configurado para ".T.", faz com que o sistema entenda que o pedido de venda é um novo registro, resultando na limpeza dos campos associados. Esse comportamento é desenvolvido para assegurar que o Pedido respeite as informações do Cliente X Contrato de Parceria.

**Solução**

Para solucionar essa ocorrência, basta desativar o parâmetro MV\_PRCCTR

1. Acesse o módulo de Configurador (SIGACFG) no Protheus;
2. Localize o parâmetro MV\_PRCCTR;
3. Altere o parâmetro MV\_PRCCTR para .F.;
4. Salve as configurações;
5. Teste a alteração do pedido de venda novamente para verificar se os campos permanecem preenchidos.

**Saiba mais:**

* [Parcerias (FATA400 - SIGAFAT)](https://tdn.totvs.com/x/NBLAFQ)
* [Cross Segmentos - Backoffice Protheus - SIGAFAT - Parâmetros para Contrato de Parceria no Pedido e Orçamento de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018070412-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Par%C3%A2metros-para-bloqueio-de-contrato-de-parceria)
