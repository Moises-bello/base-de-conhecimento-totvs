---
article_id: 360028453332
category: RH - Dissídio
content_hash: 7b3fd6f213f5ca07bb9a45179acecaaa845862b2dc6ce3840dc473ffffc57019
fetched_at: '2026-06-28T22:43:43.300525+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como fazer dissidio parcelado
type: support-article
updated_at: '2025-08-07T15:09:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028453332-RH-Linha-Protheus-GPE-Como-fazer-dissidio-parcelado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34015677293079)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como fazer dissidio parcelado?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.

**Solução**Primeiramente efetuar o cálculo do dissidio retroativo, realizar a conferência dos valores e após estar correto, efetuar a geração para a folha de pagamento.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029258052)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029258732)

Nos parâmetros de geração atente-se aos campos **Número de Parcelas** e **Atualiza Lançamento**, pois são esses campos que configuram o parcelamento.

Preencher o campo Número de parcelas, com a **quantidade de meses que deseja parcelar** o valor total da verba de **diferença de dissidio**.  
O campo Atualiza Lançamento deve estar com Valores Futuros, para que o sistema possa levar o parcelamento à **rotina de valores futuros** e realizar o parcelamento na folha de pagamento de acordo com a quantidade de parcelas.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18030474831255)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18030509056279)

Abaixo vamos verificar os valores gerados em dissídio e como serão tratados nos lançamentos futuros no cálculo de folha de pagamento. Vamos tratar a verba 001 - Salário Mensalista, uma vez que este valor será acompanhado pela verbas de base de INSS e base de FGTS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18047698771479)

Também temos o relatório de conferência que nos apresentada o valor de R$ 600,00 para pagamento e conforme configuração na geração , efetuaremos o pagamento do valor em 3 parcelas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18030322553239)[RH - Linha Protheus - GPE - Há relatório de conferência do dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034535374-RH-Linha-Protheus-GPE-H%C3%A1-relat%C3%B3rio-de-confer%C3%AAncia-do-diss%C3%ADdio)

Após geração para folha , ao acessar **Atualizações -> Lançamentos -> Valores futuros**, veremos as verbas com os valores totais , quantidade de parcelas , número de parcelas já pagas e saldo a pagar, além das demais informações conforme print:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18031216799127)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18031205081111)

Já no cálculo da competência 04/2023, que será o pagamento da primeira parcela os valores são apresentados com a respectiva verba:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18044736131607)

Após o encerramento do período 04/2023 , ao consultar os lançamentos em valores futuros, já visualizamos a alteração do número de parcelas pagas , valor já pago e saldo a pagar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18044913337367)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18045260361367)

Cálculo de folha na competência 05/2023:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18045297612055)

Novamente, após o encerramento do período 05/2023 , ao consultar os lançamentos em valores futuros, temos a alteração do número de parcelas pagas , valor já pago e saldo a pagar conforme pagamento da 2ª parcela:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18045360810519)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18045459346583)

Na competência 06/2023, temos o último pagamento das parcelas de dissídio em folha:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18045502185623)

Após o fechamento de período 06/2023, os lançamentos futuros apresentarão a quantidade de parcelas pagas (3), valor pago (R$ 600,00), saldo devedor (R$ 0,00) e altera a situação de ATIVO para PAGO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18046080541847)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18047176680983)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Cálculo, geração e conferência do dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056146513-RH-Linha-Protheus-GPE-C%C3%A1lculo-gera%C3%A7%C3%A3o-e-confer%C3%AAncia-do-diss%C3%ADdio-retroativo)

[RH - Linha Protheus - GPE - Como parametrizar e calcular o dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034578653-RH-Linha-Protheus-GPE-Como-parametrizar-e-calcular-o-diss%C3%ADdio-retroativo)

[Artigos Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
