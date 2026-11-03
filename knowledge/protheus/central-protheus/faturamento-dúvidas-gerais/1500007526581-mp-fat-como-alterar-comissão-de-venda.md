---
article_id: 1500007526581
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 3e90eb1cf1909b395a728d325b1e7af43820b0395fb1d292356d8bfa8bf1b83e
fetched_at: '2026-06-28T22:38:31.177890+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Como alterar comissão de venda
type: support-article
updated_at: '2021-04-28T15:52:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007526581-MP-FAT-Como-alterar-comiss%C3%A3o-de-venda
---

**Dúvida**

Como alterar comissão de venda.

**Ambiente**

Microsiga Protheus - todas as versões.  
  
**Solução**

A alteração de comissões de venda podem ser efetuadas :

 - Ajustando o percentual de comissão do pedido de venda (**mata410**) ainda sem faturamento, seja no cabeçalho do pedido (c5\_comis 1 a 5) ou no item (c6\_comis1 a 5);

- Após o faturamento da nota, sendo a comissão na emissão da nota ou após a baixa do título, deverá alterar as informações relacionadas a comissão através da rotina “Manutenção das Comissões” (**[MATA490](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/mata490_comissoes.htm)**).

Na rotina de manutenção de comissões também pode ser efetuado:

* Visualização das Comissões geradas;
* Realizar inclusão de comissões manualmente;
* Excluir comissões geradas.

Os valores de comissões apresentados no Relatório de Comissões (**MATR540**), são registrados na rotina "Manutenção das Comissões” (**MATA490**), caso existam inconsistências de comissões gravadas, podem ser verificadas nesta rotina.

**Observação :**Ao processar o Pagamento da Comissão, quando gerado Título no Contas a Pagar, a rotina registra o conteúdo do campo “**Proc. Com**.” (**E3\_PROCCOM**) com os dados do título gerado: Filial + Prefixo + Número + Parcela;

Saiba mais: **[Processo para configurar e gerar as comissões dos vendedores](https://tdn.totvs.com/pages/viewpage.action?pageId=235598457)**
