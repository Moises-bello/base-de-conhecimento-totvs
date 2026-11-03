---
article_id: 360049725333
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 6f7c097ef4bf659b2dfd867a3be1fa1ea73dd0724f7a9d5d1e8c89d3c0dde894
fetched_at: '2026-06-28T22:38:32.990312+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Mensagem
  HELP: A100USARF4 no faturamento'
type: support-article
updated_at: '2022-09-22T14:59:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049725333-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Mensagem-HELP-A100USARF4-no-faturamento
---

**Ocorrência**

No módulo Faturamento, ao tentar realizar **Retorno de Beneficiamento** o sistema apresenta: Help: **A100USARF4**  
A quantidade informada para o retorno deste documento não está correta.

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.

**C****ausa**

Essa mensagem é apresentada quando a primeira movimentação seja ela saída ou entrada, usou algum  TES que controla Poder de Terceiros (**F4\_PODER3**) **igual a Devolução**ou **Remessa**, com isso, o sistema alimentou o estoque com saldo de terceiros, e ao fazer o retorno, o TES utilizado não está controlando Poder de Terceiros (**F4\_PODER3 = N**),  ou **não existe saldo** em Poder de Terceiro para o produto utilizado. 

Se no TES, o campo **F4\_PODER3 não for igual a D** ("Devolução") e a identificação do **SB6** que vem no campo**C6\_IDENTB6** for igual a **Zero,** o help será apresentado.

Se o campo **F4\_PODER3 estiver igual D** e a identificação do **B6  seja diferente de zero**, o sistema **verificará** se essa identificação do**SB6** não está **vazia**, e **compara** com **D1\_IDENTB6 da NF de entrada** para validarem se**são iguais**, sendo iguais, gera o **retorno**, caso **contrário**, **exibirá o help A100USARF4.**

**Solução**

**1.** Verifique se**D1\_IDENTB6** da **NF** **de entrada** está preenchido e está carregando a informação para **C6\_IDENTB6**;

**2.** Verifique se a quantidade informada para retorno de poder de terceiros não é maior que o saldo existente de poder de terceiros, e se o campo **F4\_PODER3 está igual a D** para **devolução de Poder de Terceiros**;

**3.** Se estiver utilizando a função de **cópia do Pedido de Vendas**, verifique se é alimentado dado no campo **C6\_IDENTB6,** que precisa ser **eliminado** se a operação não tiver relação com o movimento de Poder de Terceiro;

**4.** Se **for necessário,** vá em **Miscelanea > Ajustes > Refazer Acumulados (MATA215)** e **Refazer Poder de Terceiros (MATA216)**, rode em**modo exclusivo** para ajuste dos saldos em aberto e realize o processo de devolução novamente;

**5.**Verifique se foram atendidas **todas as premissas** para o procedimento de retorno **conforme a documentação:** [FAT0057\_Emissão\_de\_Nota\_de\_Devolução\_de\_Terceiros\_Retorno](https://tdn.totvs.com/pages/viewpage.action?pageId=236431772)  
Para validação, com finalidade de **teste** inclua uma **nova Nota de Entrada** seguindo as especificações e em seguida realize o retorno;
