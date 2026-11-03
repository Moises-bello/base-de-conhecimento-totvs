---
article_id: 360017422212
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0eaec6db6e3abba8e9b2512aa77ec280bd1166da772f59b226c57d3dc21d8296
fetched_at: '2026-06-28T22:38:39.738902+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como vincular ou Desvincular
  RA no Pedido de Vendas pela Rotina MATA410
type: support-article
updated_at: '2026-03-05T20:17:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017422212-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-vincular-ou-Desvincular-RA-no-Pedido-de-Vendas-pela-Rotina-MATA410
---

**Dúvida**

Como vincular ou Desvincular RA no Pedido de Vendas pela Rotina **MATA410**?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**  
No ambiente de faturamento, rotina **MATA410** (Pedido de Vendas), é possível incluir um RA - Recebimento Antecipado (Adiantamento) em casos em que o cliente antecipe determinado valor e o mesmo necessite ser informado na preparação do Pedido de Vendas.

**1 - Vincular / Incluir um RA:**

* Como primeiro ponto, é necessário informar uma **condição de pagamento** que permita o uso de RA, o mesmo é informado no campo “Adiantamento” (**E4\_CTRADT**) no cadastro da Condição;
* Em “Outras Ações” é possível selecionar a opção “Adiantamento”;
* O Sistema abrira uma tela onde é possível escolher “**Incluir Adiantamento**” ou “**Relacionar Adiantamentos**”;
* Pela opção “**Incluir Adiantamento**” o sistema abre a tela de cadastro da Rotina Contas a Receber para inclusão do título;
* Pela opção “**Relacionar Adiantamentos**” serão listados os Adiantamentos cadastrados para o cliente (unicamente para este cliente) no financeiro, permitindo a seleção do título;
* Ao selecionar o adiantamento a ser vinculado ao Pedido de vendas, o sistema permite selecionar o valor a ser utilizado deste RA.

**2 - Desvincular o RA:**

Caso necessite **desvincular** o Adiantamento de um pedido em aberto, Selecione o **Pedido de venda- MATA410** e clique em alterar, em “Outras Ações” -> “Adiantamento”, selecione a opção “Relacionar Adiantamentos”, retire a marcação do Adiantamento que deseja desvincular e ele será desvinculado.

Caso o **Pedido de Venda-MATA410** já tenha sido **faturado total** ou **parcialmente**, **não é permitido** desvincular o Adiantamento, sendo necessária a **exclusão** do documento de saída pela rotina de "Exclusão de Documento de Saída (**MATA521A**)", e após a exclusão, será possível desvincular o Adiantamento.

Caso o Adiantamento foi parcial na geração do Titulo Financeiro Exemplo:

Pedido de Venda R$1.000

RA relacionado R$500

Foi gerado o titulo de baixa parcial de R$500

Foi realizada a baixa pelo Financeiro destes R$500

Ao acessar a rotina de exclusão do documento "**MATA521A"** e excluir o documento, ocorre a mensagem **"****FA040BAIXA"** para realizar a exclusão é necessário acessar o Financeiro, localizar o titulo deste documento de saída ir em Outras Ações >> Baixas >> Cancelar Baixas com isso o titulo vai ficar baixa parcial novamente e pode voltar na rotina de Exclusão de Documento **MATA521A** e excluir o documento.

**Lembrete;** Não é permitido **excluir** ou **estornar** a **Compensação** do Adiantamento através do módulo **Financeiro**.

**Observação;** Após a transmissão do Documento de Saída, não é possível **Desvincular o Adiantamento** do Titulo Financeiro, sem o **cancelamento da transmissão** ou a **exclusão do documento de saída;**

**Saiba Mais:**

[**Recebimento Antecipado (RA/Adiantamento) no Pedido de Venda (MATA410)**](https://tdn.totvs.com/x/GkD2Dw)

[**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Na exclusão do documento de saída, aparece o Help: FA040BAIXA**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012501602-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Na-exclus%C3%A3o-do-documento-de-sa%C3%ADda-aparece-o-Help-FA040BAIXA)

[**Cross Segmentos - Backoffice Protheus - SIGAFAT - Como emitir uma nota de Pagamento / Recebimento Antecipado (tpNFDebito = 06)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37326686645143-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-emitir-uma-nota-de-Pagamento-Recebimento-Antecipado-tpNFDebito-06)
