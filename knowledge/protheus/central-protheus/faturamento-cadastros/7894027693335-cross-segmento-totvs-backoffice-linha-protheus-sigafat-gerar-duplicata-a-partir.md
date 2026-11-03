---
article_id: 7894027693335
category: Faturamento - Cadastros
content_hash: 96cda0592b0198260c3ec8e0cec8aa9c2c34c1057c4d614f9660f04614c25a5c
fetched_at: '2026-06-28T22:38:35.282069+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Gerar duplicata
  a partir da data de entrega do pedido
type: support-article
updated_at: '2023-08-15T18:27:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7894027693335-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Gerar-duplicata-a-partir-da-data-de-entrega-do-pedido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16764072305815) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar duplicata a partir da data de entrega (C6\_ENTREG) do pedido?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Os títulos, por padrão, são gerados com base na condição de pagamento a partir data de emissão da nota fiscal, no momento do faturamento.

Na planilha financeira do pedido de vendas é possível ter uma prévia dos vencimentos dos títulos e seus valores, porém a planilha ainda não tem a informação da data de emissão da nota, então ela pode demonstrar as datas de duas formas, de acordo com a configuração do parâmetro **MV\_DPDTEMI**:

* **MV\_DPDTEMI = .T.**

Indica que na planilha financeira do pedido de venda, as duplicatas serão consideradas pela data mais antiga inserida nos campos "DT Emissão" (C5\_EMISSAO) e "Entrega" (C6\_ENTREG).

Ao alterar o campo o "Entrega" (C6\_ENTREG), para uma data inferior ao "DT Emissão" (C5\_EMISSAO), o sistema passa a contar os dias de vencimento do título a partir da data do campo "Entrega" (C6\_ENTREG).

Caso o campo "Entrega" (C6\_ENTREG) tenha data superior ao "DT Emissão" (C5\_EMISSAO), o sistema considera a data do campo "DT Emissão" (C5\_EMISSAO) para contagem dos dias da condição de pagamento na Planilha financeira.

* **MV\_DPDTEMI = .F.**

Indica que na planilha financeira do pedido de venda, as duplicatas serão consideradas pela data de entrega,  campo "Entrega" (C6\_ENTREG). Ao realizar a parametrização pela data de entrega, o sistema leva em consideração a data inserida no campo "Entrega" (C6\_ENTREG), sendo superior ou não ao campo de "DT Emissão" (C5\_EMISSAO).

O campo "Entrega" (C6\_ENTREG) é automaticamente preenchido com a data base do sistema, no momento da inclusão do pedido de vendas, mas pode ser modificado manualmente.

Outra possibilidade de alterar as duplicatas na planilha financeira, seria a utilização do ponto de entrada M410VCT. A finalidade do ponto de entrada M410VCT é permitir que seja alterado o vencimento e valor das parcelas na aba de duplicatas da Planilha Financeira. Ponto de entrada: **[M410VCT - Alteração das duplicatas na Planilha Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=237396627)**

O parâmetro **MV\_TIPCPDT** ajusta o preenchimento do campo "Entrega" (C6\_ENTREG) ao efetuar a cópia do Pedido de Venda: **[MV\_TIPCPDT - Preenchimento da Data de Entrega na Cópia do Pedido de Venda](https://tdn.totvs.com/pages/viewpage.action?pageId=59441683)**

**Saiba mais:** [Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)
