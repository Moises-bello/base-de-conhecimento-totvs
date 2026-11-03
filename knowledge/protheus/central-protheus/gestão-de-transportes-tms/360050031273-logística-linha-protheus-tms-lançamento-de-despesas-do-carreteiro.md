---
article_id: 360050031273
category: Gestão de Transportes (TMS)
content_hash: 1f323a7f859712a93aed4992b74111912f50886a4ddc46ef707ed9c162be343b
fetched_at: '2026-06-28T22:45:29.376514+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Lançamento de Despesas do Carreteiro
type: support-article
updated_at: '2021-08-31T21:55:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050031273-Log%C3%ADstica-Linha-Protheus-TMS-Lan%C3%A7amento-de-Despesas-do-Carreteiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como lançar despesas do contrato de carreteiro?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Na rotina **TMSA070 - M****ovimento de Custo de Transporte** podemos lançar despesas geradas pelo prestador de serviço, como abastecimento, instalação de rastreador, compra de pneu entre outras. Os valores das despesas **podem ser parcelados**.   
  
Estas despesas podem ser associadas às viagens que serão realizadas pelo prestador de duas formas:  
  
Para gerar uma viagem com despesa que não movimenta banco:

* Em **Gestão de Transportes - SIGATMS,**acesse **Atualizações/Viagens/Rodoviário Entrega/Viagem-mod.2 - TMSA144**;
* Incluir a viagem informando **Rota**, documentos e complemento de viagem;
* Dentro do complemento da viagem, selecione **Ações Relacionadas,** **Adiantam/ Desp**. e informe a despesa e seu valor;

**![adiant_despesa.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407542915095/adiant_despesa.png)**  
![viagem_despesa.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407542945175/viagem_despesa.png)

* Confira os dados e **Confirme**.

Para uma despesa pela rotina **TMSA070 - M****ovimento de Custo de Transporte:**

* Em **Gestão de Transportes - SIGATMS,**acesse **Atualizações/Transporte/Movto custo Transp. - TMSA070**;
* Informar o código da despesa, veículo, viagem e o valor cobrado.
* Clique em **Confirmar**.

![movimento_custo_transp.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407539557015/movimento_custo_transp.png)

Quando o contrato de carreteiro é gerado, o Sistema gera títulos do tipo **NDF** - **Non-Deliverable Forward** no financeiro. Desta forma é possível abater estes títulos pela compensação financeira.
