---
article_id: 22982867760663
category: Originação de Grãos (OG)
content_hash: 64403d179f7e7be20e8a6a8f7b4ca2baa1b39bb81001443de63e37eb2dc71be9
fetched_at: '2026-06-28T22:45:43.752919+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Procedimento para Utilização em Venda a Ordem
type: support-article
updated_at: '2025-06-25T11:16:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22982867760663-Agro-Linha-Protheus-AGR-Procedimento-para-Utiliza%C3%A7%C3%A3o-em-Venda-a-Ordem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22982877913239) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual é o **Procedimento para Utilização** **em Venda a Ordem**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Acesse em **SIGAAGR > Atualizações > Originação > Comercialização > Controle de Negócios > Registro de Negócios**: Criar um contrato mercado interno, a partir de um registro de negócios. Pode ser feito com grãos ou algodão;

**2.** Observe nas regras fiscais do contrato, indicar que é operação triangular **= SIM**, informar um cliente para o faturamento, **TES** para venda, uma entidade de entrega para a remessa, e uma **TES** para a remessa;

**3.** Veja caso seja algodão, efetuar a reserva **take-up**;

**4.** Acesse em **Consultas > Originação > Painel de Instrução.** Fazer uma **IE**, utilizado a regra fiscal do contrato com operação triangular;

**5.** Selecione os fardos na **IE** para algodão;

**6.** Acesse em **Atualizações > Originação > Movimentos Internos > Romaneio c/ Pesagem**: Criar um romaneio, informar a IE, se for algodão, informar fardos e efetuar pesagens;

**7.** Verifique ao atualizar o romaneio, deve gerar na pastar **Comercialização** dois registros para cada regra fiscal da **IE** vinculada, com os sub-tipos: **(E) VENDA A ORDEM e (E) REMESSA POR VENDA A ORDEM**;

![VEN.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22996388693527)

**8.**  Caso seja utilizada a opção **Reabrir ou Cancelar**  do romaneio, o registro de comercialização do tipo **(S) Remessa** por **Venda a Ordem** será excluído;

**9.** Verifique ao confirmar o romaneio, serão geradas dois **Pedidos de Venda** e duas Notas Fiscais;

* - Uma nota fiscal para o cliente de faturamento e TES da Regra Fiscal;
* - Uma nota fiscal para o local de entrada e TES de Remessa da Regra Fiscal.

**10.** Acesse em **Atualizações > Originação > Controle de Vendas > Contrato de Venda: nas regras fiscais**, verificar que deve ter atualizado o campo **Qtd NF** apenas para um dos registros de comercialização, sem duplicar devido ao fato de existirem dois registros;

**11.** Acesse em **Atualizações > Originação > Movimentos Internos > Romaneio c/ Pesagem**, foi criada uma nova ação relacionada **“Informar Docto Referência”**. Essa funcionalidade tem o objetivo de permitir ao usuário informar, na nota fiscal de remessa à ordem, os dados da NF do cliente para que as mesmas sejam inclusas nos dados adicionais da DANFE.

* Para informar esses dados o Romaneio já deve ter sido confirmado, o Status de envio da NF de remessa para o SEFAZ não pode ser Autorizado/Transmitido e  o Status de envio da NF de venda para o SEFAZ deve estar Autorizado.
* Atendendo à essas condições, para cada Item de Comercialização do Romaneio que for do **sub-tipo (E) REMESSA POR VENDA A ORDEM**, o usuário poderá informar os seguintes campos:
* Número Documento Referência: Preencher com o número da **NF** do cliente. **Campo obrigatório**.
* Série Documento Referência: Preencher com o número de **Série da** **NF** do cliente. Não **obrigatório**.
* Data de Emissão Referência: Preencher com a **Data de Emissão da NF** do cliente.

![VEN1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22996388718999)

A sequência de geração do romaneio da operação triangular é primeira a nota de remessa e após a nota de venda.

Caso o usuário, na rotina de transmissão da **NF (SPEDNFE)**, informe uma **NF** de remessa venda a ordem que não tenha os dados do documento de referencia o sistema não irá transmitir a **NF** apresentando na tela o motivo.
