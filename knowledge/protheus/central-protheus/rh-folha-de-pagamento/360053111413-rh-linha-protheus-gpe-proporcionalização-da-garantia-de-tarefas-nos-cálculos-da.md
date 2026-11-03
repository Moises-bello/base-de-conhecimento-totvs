---
article_id: 360053111413
category: RH - Folha de Pagamento
content_hash: d3af04972d9e0da2eb30c36ff067f66b3523f08ea5bebbe2494d1257b3f726d9
fetched_at: '2026-06-28T22:44:16.191307+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Proporcionalização da garantia de tarefas nos cálculos
  da Folha de Pagamento, do 13º salário e da Rescisão
type: support-article
updated_at: '2024-09-06T19:28:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053111413-RH-Linha-Protheus-GPE-Proporcionaliza%C3%A7%C3%A3o-da-garantia-de-tarefas-nos-c%C3%A1lculos-da-Folha-de-Pagamento-do-13%C2%BA-sal%C3%A1rio-e-da-Rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26196008622487) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Proporcionalização da garantia de tarefas nos cálculos da Folha de Pagamento, do 13º salário e da Rescisão.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O Mnemônico LGTARPROP para alterado para P\_LGTARPRO para que o usuário consiga alterar o seu conteúdo para que o calculo seja proporcionalizado ou não.  
  
**Solução**

O tratamento da proporcionalização da garantia de tarefas, ocorre para permitir:

• A proporcionalização da garantia de tarefas no **Cálculo da Folha de Pagamento de Tarefeiros**, atendendo especificação de alguns Sindicatos;  
• A geração da garantia de tarefas no **Cálculo da Rescisão**, sendo que, a garantia de tarefas do mês da demissão é proporcional aos dias trabalhados (somam-se, também, aos dias trabalhados, os 15 primeiros dias de afastamento dos tipos **O** **acidente de trabalho** e **P- doença**, por serem de encargo da empresa, além dos dias de afastamento tipo **8** **licença remunerada**).

Para que seja efetuado o cálculo proporcional da garantia de tarefas, o conteúdo do Mnemônico P\_LGTARPRO deve ser alterado para **.T.** (True - Verdadeiro),

**Importante!**  
Observe as modificações efetuadas no sistema com a alteração do Mnemônico:

• No cálculo da **Folha e da Rescisão**, a garantia de tarefas é proporcional aos dias trabalhados (somam-se também aos dias trabalhados, os 15 primeiros dias de afastamento dos tipos **O** **acidente de trabalho** e **P** **doença**, por serem de encargo da empresa, além dos dias de afastamento tipo **8 licença remunerada**).

• Nos cálculos da 1ª e 2ª parcelas do 13º salário a garantia de tarefas é proporcional aos **avos** de 13º de direito do funcionário.

**Procedimentos para implementação/utilização:**

1. No ambiente **Gestão de Pessoal**, opção **Atualizações/Definições Cálculo/Mnemônico** (GPEA300), localize o mnemônico P\_LGTARPRO e selecione a opção **Alterar**.  
2. No campo **Conteúdo** informe **.T.** (True - Verdadeiro).  
3. Confira os dados e confirme a alteração. Quando calculados a Folha, a 1ª e 2ª parcelas do 13º salário, e a Rescisão de Funcionários Tarefeiros, cujo mnemônico P\_LGTARPRO seja utilizado, será realizada a proporcionalização.  
  
**Observação**

• Se o conteúdo do Mnemônico P\_LGTARPRO for mantido como **.F.** (False - Falso), o cálculo da garantia de tarefas continua sendo efetuado sem a proporcionalização das situações mencionadas.

• A partir desta implementação, será sempre gerada a garantia de tarefas no **Cálculo da Rescisão**, e somente a funcionários que não atingiram o valor mínimo de pagamento das tarefas e que tenham direito à garantia de tarefas.

• Aos tarefeiros com pagamento semanal, consideram-se, além dos dias trabalhados, os dias de DSR para proporcionalizar a garantia de comissão.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Cálculo para tarefeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037394713-RH-Linha-Protheus-GPE-C%C3%A1lculo-para-tarefeiro)

[RH - Linha Protheus - GPE - Como calcular DSR para Tarefeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021010632-RH-Linha-Protheus-GPE-Como-calcular-DSR-para-Tarefeiro)

[RH - Linha Protheus - GPE - Cálculo de Hora extra para Tarefeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411789546903-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Hora-extra-para-Tarefeiro)

[RH - Linha Protheus - GPE - Cálculo de Folha para tarefeiro com Garantia](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25261755516567-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Folha-para-tarefeiro-com-Garantia)
