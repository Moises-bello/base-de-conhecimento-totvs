---
article_id: 4404720962071
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f3af23676fc7bb35ecf1e1cda7d36f7b2459b8475b52ffe9430114ab5ed58e6e
fetched_at: '2026-06-28T22:38:38.646164+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Nota sobre o
  campo C5_KM
type: support-article
updated_at: '2021-07-21T19:10:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404720962071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-o-campo-C5-KM
---

**Dúvida**Nota de uso do campo C5\_KM.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

O campo **C5\_KM**, apesar de estar no pedido de vendas (**MATA410**) do faturamento, não é de uso do módulo e sim, do módulo **TMS**, pois, é para uso do tratamento de **Pauta de Frete** (**mata545**).  
  
O campo não tem travas e é de preenchimento manual .  
  
Quando cadastrado a pauta de frete na tabela **DV9**, ao preencher a **Dist.entrega** (**C5\_KM**) é preenchido automaticamente o valor de frete de pauta, este é o conceito de uso do campo em questão, para tratar valores de frete por trechos, conceitos de uso TMS e GFE, e não do módulo Faturamento, por isso, não é tratado na **Geração da** **Nota de Saída** (**mata461**).  
  
Segue documentação do assunto e com exemplo do seu uso: **[Exemplo de Cálculo de Impostos ICMS de Pauta - Uso por Eixo/KM Legislação UF Pará (TMSA200 - SIGATMS)](https://tdn.totvs.com/x/mDNvHw)**
