---
article_id: 20264650366359
category: SIGAEST - LEGAIS
content_hash: 41a8f844e95deede4894ab5d0df3a4cd48af9bd55a34b0969bb395160d4290f5
fetched_at: '2026-06-28T22:38:51.674588+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Produções utilizando
  ora matéria prima importada, ora matéria prima nacional
type: support-article
updated_at: '2026-05-18T18:26:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20264650366359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-FCI-Produ%C3%A7%C3%B5es-utilizando-ora-mat%C3%A9ria-prima-importada-ora-mat%C3%A9ria-prima-nacional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20264650345111) Tempo aproximado para leitura: **00:01:57min**  
  
**Dúvida**  
Tenho um produto acabado que hora utiliza matéria prima importada e hora utiliza matéria prima nacional, ao rodar a apuração do FCI (FISA061) o calculo está considerando a matéria prima nacional abatendo na parcela importada do Produto Acabado  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O objetivo da apuração da FCI é identificar, em média, qual a parcela de valor importado existente nas produções realizadas para determinado produto durante um período. Desse modo, se houveram duas ordens de produção, uma utilizando componentes importados e outra não, o esperado é que a rotina execute uma média entre essas duas produções para estabelecer o percentual de importação daquele produto acabado durante o mês, visto que trata-se de um código único para o produto acabado e que esse único código será enviado na entrega da obrigação acessória.

Essa mesma lógica é aplicada em todos os pontos da apuração da FCI dentro do sistema; o tratamento para as entradas de matéria prima também ocorre de maneira análoga, com a apuração de todas as compras do período com seus respectivos percentuais de parcela importada, de acordo com a origem do produto naquela operação, para obtenção do valor médio de parcela importada dentro do período calculado.

Caso se tenha um entendimento diferente do comportamento atual, se faz necessário envio do embasamento legal para avaliação interna por meio de chamado ao Suporte Técnico.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Como interpretar o cálculo do Valor Importado (A8\_VLRVI) em Produções?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9129246051479)

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
