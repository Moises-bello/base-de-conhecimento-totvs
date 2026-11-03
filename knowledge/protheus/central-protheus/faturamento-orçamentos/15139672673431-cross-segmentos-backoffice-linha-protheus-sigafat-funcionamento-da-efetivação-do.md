---
article_id: 15139672673431
category: Faturamento - Orçamentos
content_hash: 363d923ed4b4ee6d1b8db5ece9829e27a10194cd7ece4ecc68b2ca8a345ccf31
fetched_at: '2026-06-28T22:38:25.030867+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Funcionamento da
  efetivação do orçamento de venda (MATA416)
type: support-article
updated_at: '2023-06-07T21:16:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15139672673431-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Funcionamento-da-efetiva%C3%A7%C3%A3o-do-or%C3%A7amento-de-venda-MATA416
---

**Dúvida**

Como funciona a efetivação do orçamento de venda?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Ao selecionar a opção "**Efetivar**", o sistema efetiva o **Orçamento de Venda** (MATA415) gerando um **Pedido de Venda** (MATA410).

Pode gerar também uma **Ordem de Produção**, dependendo da configuração de **Sugestão de Orçamentos** (MATA405) e pré-configurações ao pressionar a tecla **[F12]** da rotina **Aprovação de Vendas** (MATA416).

Caso esteja configurado para gerar **Ordem de produção** será gerado apenas para o componente que tenha **Estrutura**(Montagem de Produtos - MATA200), **TES** que movimenta estoque e não possuem **Saldo.**  
  
Caso o componente não tenha **Estrutura**(Montagem de Produtos - MATA200) pode ser gerado**1 - Solicitação de Compras** ou **2 - Ordem de Produção** conforme definido no pergunte ao pressionar a tecla **[F12]** da rotina **Aprovação de Vendas** (MATA416).

Para saber mais a respeito da geração de **Ordens de Produção** a partir da efetivação do **Orçamento de Venda**, consulte o link: [Sugestão de Orçamentos (MATA405)](https://tdn.totvs.com/pages/viewpage.action?pageId=560647995)

**OBSERVAÇÃO 1:** Caso queira **inibir a visualização** da tela do **Pedido de Vendas** (MATA410) ao efetivar o Orçamento, consulte a configuração do parâmetro **MV\_FATTEPO**.

**OBSERVAÇÃO 2:** Uma vez o **orçamento efetivado**, o mesmo é **encerrado pelo sistema**, não sendo possível trabalhar a aprovação de forma parcial como ocorre com a liberação do pedido de venda.

**OBSERVAÇÃO 3:** Caso seja necessário a continuação da negociação com os dados do orçamento encerrado, será necessário copiar o orçamento e informar apenas os itens que deseja gerar o novo pedido.

**Saiba mais:**

* **TDN:**[FAT0172 Aprovação de Orçamentos (MATA416)](https://tdn.totvs.com/x/UzJxIQ)
