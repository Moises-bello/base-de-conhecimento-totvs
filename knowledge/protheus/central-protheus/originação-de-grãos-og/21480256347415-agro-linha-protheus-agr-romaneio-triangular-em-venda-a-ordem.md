---
article_id: 21480256347415
category: Originação de Grãos (OG)
content_hash: 2ad29c0b40bdaa4ea6e4b42b529dcdb0b819fb6a9a952e2b501976d932e5b9c2
fetched_at: '2026-06-28T22:45:44.852657+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Romaneio Triangular em Venda a Ordem
type: support-article
updated_at: '2025-06-24T20:36:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21480256347415-Agro-Linha-Protheus-AGR-Romaneio-Triangular-em-Venda-a-Ordem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21480256317463) Tempo aproximado para leitura: **00:01:15 min** **Dúvida**Como gerar uma movimentação de **Romaneio Triangular em Venda a Ordem**?

**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12.1.23  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

**1.** Verifique em **SIGAAGR > Atualizações > Originação > Comercialização > Controle de Negócios > Registro de Negócios.** Criar um contrato mercado interno, a partir de um registro de negócios. Pode ser feito com grãos ou algodão;

**2.** Analise, nas regras fiscais do contrato, indicar que é operação **triangular =** **SIM**, informar um cliente para o faturamento, **TES** para venda, uma entidade de entrega para a remessa, e uma **TES** para a remessa;

**3.** Observe, caso seja algodão, efetuar reserva **take-up**;

**4.** Analise em **Consultas > Originação > Painel de Instrução**. Fazer uma **IE**, utilizado a regra fiscal do contrato com operação triangular;

**5.** Veja para algodão selecionar fardos na **IE**.

**6.** Verifique em **Atualizações > Originação > Movimentos Internos > Romaneio c/ Pesagem**. Criar um romaneio, informar a **IE**, se for algodão informar fardos, e efetuar pesagens;

**7.** Observe ao atualizar o romaneio, deve gerar na pasta **Comercialização** dois registros para cada regra fiscal da **IE** vinculada, com os sub-tipos: **(E) VENDA A ORDEM e (E) REMESSA POR VENDA A ORDEM**;

![TRIAN.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21480256324247)

**8.** Verifique, caso seja utilizada a opção **Reabrir ou Cancelar**  do romaneio, o registro de comercialização do tipo **(S) Remessa por Venda a Ordem** será excluído;

**9.** Veja ao confirmar o romaneio, serão geradas dois Pedidos de Venda e duas Notas Fiscais;

- Uma nota fiscal para o cliente de faturamento e TES da Regra Fiscal;  
- Uma nota fiscal para o local de entrada e TES de Remessa da Regra Fiscal.

**10.** Acesse em **Atualizações > Originação > Controle de Vendas > Contrato de Venda**, nas regras fiscais, verificar que deve ter atualizado o campo **Qtd NF** apenas para um dos registros de comercialização, sem duplicar devido ao fato de existirem dois registros;

**11.** Analise em **Atualizações > Originação > Movimentos Internos > Romaneio c/ Pesagem**, foi criada uma nova ação relacionada **Informar Docto Referência**. Essa funcionalidade tem o objetivo de permitir ao usuário informar, na nota fiscal de remessa à ordem, os dados da **NF** do cliente para que as mesmas sejam inclusas nos dados adicionais da **DANFE**.

**12.** Informe esses dados do Romaneio, pois eles devem ser confirmados, o Status de envio da NF de remessa para o SEFAZ não pode ser Autorizado/Transmitido e  o Status de envio da NF de venda para o SEFAZ deve estar Autorizado.  
  
**Observação:**  
Atendendo a essas condições, para cada Item de Comercialização do Romaneio que for do sub-tipo **(E) REMESSA POR VENDA A ORDEM**, o usuário poderá informar os seguintes campos:

**- Número Documento Referência:** Preencher com o número da NF do cliente. Campo obrigatório.

**- Série Documento Referência:** Preencher com o número de Série da NF do cliente. Não obrigatório.

**- Data de Emissão Referência:** Preencher com a Data de Emissão da NF do cliente.

![TRIAN1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21480256326295)
