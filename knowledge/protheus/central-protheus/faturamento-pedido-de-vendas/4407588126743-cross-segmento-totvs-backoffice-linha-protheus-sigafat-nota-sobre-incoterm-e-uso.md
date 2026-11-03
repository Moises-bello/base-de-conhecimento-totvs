---
article_id: 4407588126743
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 261d1f34cfb304a32abd92efc76590556e0b8f2d81dadbfaddc106d172fb648d
fetched_at: '2026-06-28T22:38:38.584550+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Nota sobre Incoterm  e
  uso no pedido de venda do módulo Faturamento
type: support-article
updated_at: '2021-09-01T17:26:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407588126743-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Nota-sobre-Incoterm-e-uso-no-pedido-de-venda-do-m%C3%B3dulo-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00:min** **Dúvida**Nota sobre **Incoterm** e uso no pedido de venda do módulo Faturamento.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Solução**

***Incoterms - International Commercial Terms***: São termos internacionais de comércio criados pela **CCI – Câmara de Comércio Internacional**, Paris e são utilizados para facilitar as negociações entre as nações. Basicamente os ***Incoterms*** são siglas que designam as responsabilidades das partes envolvidas nas transações, Importador e Exportador. Algumas modalidades de incoterms:

* **FCA** - > INCOTERM :Existe a situação em que o comprador deseja arcar com as despesas do transporte principal, e consequentemente, com os riscos gerados durante esse transporte. Nessa condição, pode-se optar pelo  FCA, em  inglês significa “Free Carrier”, ou livre no transportador. Isso é, o vendedor vai disponibilizar a mercadoria em questão, em um local previamente acordado, ainda no país de origem, onde, a transportadora do comprador recepcionará a mercadoria e passará a se responsabilizar por ela.
* **EXW** -  Ex Works -  O comprador arca com todos os custos e riscos envolvidos em retirar a mercadoria no estabelecimento do vendedor, no qual, o frete é por conta do comprador.
* ***DDP - Delivered Duty Paid***: A entrega da mercadoria ao importador, com os direitos de entrada já pagos ocorre em ponto designado do território do importador.
* **DAP** - é a sigla de **Delivered at Place** este Incoterm foi criado para substituir os termos DAF, DES e DDU. Em português o **INCOTERM DAP, Delivered at Place,** significa: entregue no local, sendo assim, o vendedor deverá fazer o transporte internacional e levar a mercadoria até o local combinado com o comprador, Ou seja, o desembaraço de importação no local de destino, bem como a descarga da mercadoria, ficam a cargo do comprador, servindo para qualquer meio de transporte.
* **CIP** - é mais um dos Incoterms, sigla de **Carriage and Insurance Paid To**,  onde o transporte principal assim como o frete devem ser pagos pelo vendedor e a partir do momento em que a mercadoria é entregue ao transportador do seu destino a responsabilidade com relação a danos, perdas e roubos passa a ser inteiramente do comprador, caso o comprador queira ou então ache necessário pode contratar um seguro adicional para assim evitar . Pode ser usado em qualquer modalidade de transporte

Por padrão de sistema, **Incoterms** somente são tratados em módulos de **Comex** do Protheus como **SIGAEEC ou SIGAEIC**.

No **pedido de vendas(mata410)** do módulo Faturamento, independente se é uma nota de exportação ou não,  somente são tratadas as modalidades de frete abaixo:

* **C**=CIF
* **F**=FOB
* **T**=Por conta terceiros
* **R**=Por conta remetente
* **D**=Por conta destinatário
* **S**=Sem Frete

No caso do **incoterm** **FCA**, por exemplo, que é um tipo de incoterm, que é tratado apenas no SIGAEIC, sem o uso do módulo, o paliativo seria utilizar o ***Frete por conta do remetente*** e mensurar no campo informações adicionais o tipo de INCOTERM negociado no processo.

No caso do **incoterm EXW**, uma possibilidade seria utilizar o ***Frete por conta do destinatário*** e mensurar no campo informações adicionais o tipo de INCOTERM negociado no processo.

Não podendo utilizar da forma paliativa dentro do Faturamento, avalie a possibilidade de contratar os módulos de **COMEX** junto ao seu ESN - Executivo de Vendas na Totvs.

Também é possível sugerir melhoria para esse processo, para isso indique a sugestão na **Central Colaborativa** do portal do Cliente: **[Central-Colaborativa-Como-Acessar?source=search](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039467434-Central-Colaborativa-Como-Acessar?source=search)**

**Saiba mais sobre Incoterms:**

**[Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-INCOTERM-CFR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041677813-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-INCOTERM-CFR)**

**[MP-SIGAEIC-INCOTERM-2020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037384374-MP-SIGAEIC-INCOTERM-2020)**
