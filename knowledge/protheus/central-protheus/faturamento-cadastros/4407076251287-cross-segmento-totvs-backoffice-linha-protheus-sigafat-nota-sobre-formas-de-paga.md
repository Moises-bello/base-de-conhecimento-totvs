---
article_id: 4407076251287
category: Faturamento - Cadastros
content_hash: c1e31aed19e151a3a51f40dbef96ad56b9fb5bb2cba29a11702158381f0fba98
fetched_at: '2026-06-28T22:38:35.320291+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Nota sobre formas
  de pagamento para a NT2020.006
type: support-article
updated_at: '2021-12-08T19:06:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407076251287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Nota-sobre-formas-de-pagamento-para-a-NT2020-006
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Nota sobre formas de pagamento para a NT2020.006.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- Todas as versões  
  
**Solução**

Por padrão, o módulo de Faturamento não faz uso da forma de pagamento, pois não há controle de uso de cartão de crédito, cheque, etc. Toda nota gerada no Faturamento (**MATA461**)sempre irá gerar título do tipo ***NF - Nota Fiscal.***

Quanto ao cadastro de formas de pagamento, não há uma rotina para o cadastro no Protheus, os registros estão contidos na ***tabela 24 da SX5 no configurador***, caso seja necessário criação de novas formas deve ser acrescido nesta tabela.

O ideal é utilizar apenas as formas de pagamentos disponibilizadas, as quais atendem a NT da Nfe layout 4.0.

Para adequação de formas de pagamento para a **NT2020.006**, siga as instruções da documentação da equipe SPED: **[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG tPag (forma de pagamento / duplicata / fatura)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004985571-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-tPag-forma-de-pagamento-duplicata-fatura-?source=search)**

**Saiba Mais :**

**[MP-FAT-Faturamento x Cartão de Crédito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028559112-MP-FAT-Faturamento-x-Cart%C3%A3o-de-Cr%C3%A9dito)**

**[FAT0105\_Formas de Pagamento no Faturamento](https://tdn.totvs.com/x/fMeFDg)**

**[MP-FAT-Forma-de-pagamento-na-Regra-de-Negócio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018499931-MP-FAT-Forma-de-pagamento-na-Regra-de-Neg%C3%B3cio)**

**[MP-FAT-NFe 4.0 - Novo Layout SEFAZ - Principais dúvidas em relação à operação no módulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016130991-MP-FAT-NFe-4-0-Novo-Layout-SEFAZ-Principais-d%C3%BAvidas-em-rela%C3%A7%C3%A3o-%C3%A0-opera%C3%A7%C3%A3o-no-m%C3%B3dulo-Faturamento)**

**[MP - FAT - Pedido de Venda - Código do Intermediador (Validações e Emissão da NF)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005084801-MP-FAT-Pedido-de-Venda-C%C3%B3digo-do-Intermediador-Valida%C3%A7%C3%B5es-e-Emiss%C3%A3o-da-NF-)**
