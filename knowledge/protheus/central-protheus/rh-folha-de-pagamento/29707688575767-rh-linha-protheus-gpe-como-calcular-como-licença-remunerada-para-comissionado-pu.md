---
article_id: 29707688575767
category: RH - Folha de Pagamento
content_hash: 5ac567157cb1b0464556f728e57228b8e76cab1128f672edc35befc2058a6d8c
fetched_at: '2026-06-28T22:44:12.230290+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular como Licença Remunerada para Comissionado
  Puro
type: support-article
updated_at: '2025-08-12T13:58:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29707688575767-RH-Linha-Protheus-GPE-Como-calcular-como-Licen%C3%A7a-Remunerada-para-Comissionado-Puro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29707688560407) Tempo aproximado para leitura: **00:03:00min** **Dúvida**Como calcular como Licença Remunerada para Comissionado Puro   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quando é calculado Licença Remunerada nas férias, o sistema realiza o pagamento desses dias na Folha de pagamento.   
No exemplo abaixo, a Licença Remunerada é no mês seguinte, então apenas no calculo da Folha de Janeiro/2025 vai ocorrer o pagamento da Licença Remunerada na Folha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29707688561175)

Para isso, é necessário realizar a parametrização abaixo;

A verba de **ID 0103** - Licença Remunerada, deve ter o **campo REFFER = Não** no cadastro da verba

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29707703687319)

As verbas de **ID 0165 e 0166** (Comissão e DSR de Comissão) devem ter o **campo Incorpora Salario = SIM.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29707688562071)

No calculo da folha, o valor da Licença Remunerada será apurado da seguinte forma;

Quando houver o lançamento da verba de Comissão e DSR de comissão  
**soma das verbas 347 e 065** (6.000 + 888,89)= 6.888,89 / 30 \* 2.5 = **R$ 574,07**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29707895464983)

Quando não tiver lançamento das verbas de Comissão e DSR de Comissão, o sistema irá apurar o valor sobre a Garantia de Comissão definida no Cadastro do Sindicato -[RH - Linha Protheus - GPE - Garantia de comissão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058611233-RH-Linha-Protheus-GPE-Garantia-de-comiss%C3%A3o)

OBS.: O ID de calculo 0347 Garantia de Comissão deve possuir a mesma parametrização dos Ids 0165 e 0166.  
**Garantia de comissão 1.800,00** / 30 \* 2.5 = **R$ 150,00**   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29708035917591)

**Saiba Mais**

<https://www.youtube.com/watch?v=T7b4zMlphTI>  
[Página Centralizadora Férias Coletivas](https://tdn.totvs.com/pages/releaseview.action?pageId=219683846)
