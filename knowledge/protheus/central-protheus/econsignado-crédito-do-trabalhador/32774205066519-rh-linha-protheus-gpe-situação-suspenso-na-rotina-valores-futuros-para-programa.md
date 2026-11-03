---
article_id: 32774205066519
category: eConsignado (Crédito do Trabalhador)
content_hash: 663cf3349d8333d930d3fac7dc8212b655576ad1c214c65007462edfc6cd2dec
fetched_at: '2026-06-28T22:43:07.396302+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Situação Suspenso na rotina valores futuros para
  Programa Crédito do Trabalhador após fechamento período - Econsignado (MP 1.292/2025)
type: support-article
updated_at: '2025-10-24T17:12:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32774205066519-RH-Linha-Protheus-GPE-Situa%C3%A7%C3%A3o-Suspenso-na-rotina-valores-futuros-para-Programa-Cr%C3%A9dito-do-Trabalhador-ap%C3%B3s-fechamento-per%C3%ADodo-Econsignado-MP-1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32774210585495) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Por que o lançamento do Programa Crédito do Trabalhador fica com Situação Suspenso após fechamento período?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Essa alteração do campo Situação de **Ativo** para **Suspenso** após o fechamento da folha, ocorre pois para o Programa Crédito do Trabalhador, temos a possibilidade de haver alterações nos valores das parcelas de um mês para o outro.

Existe uma validação para a importação do arquivo Portal Emprega Brasil, onde é verificado se existe dados na RUO - Histórico de Importação para o mês seguinte ao fechamento, e caso não tenham dados na RUO antes do fechamento é realizada a alteração da situação para Suspenso na rotina de Valores futuros.

Para os lançamentos manuais direto na rotina Valores Futuros existe a mesma validação, como não existem dados na RUO - Histórico de importação para o mês seguinte o campo Situação é alterado para Suspenso.

No exemplo abaixo temos um lançamento para o período 05/2025 sem dados na RUO - Histórico de Importação, e ao fechar o período 05/2025 o campo Situação foi alterado para Suspenso.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32774210586903)  
  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Acesse a rotina Conta Corrente Valores Futuros em **Atualizações > Lançamentos > Conta Corrente Valores Futuros (GPEA415)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32774210587799)  
  
**2.** Selecione o funcionário desejado e **clique** em **Alterar**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32774205043607)  
  
**3.** Na parte superior selecione o lançamento que deseja alterar, procure pelo campo **Situação** e altere para a opção de **Ativo** e clique em **Salvar**;

![](https://i.imgur.com/H0238fu.png)

![](https://i.imgur.com/ryf1ziN.png)

**Observação:** Para alterar o campo Situação de Suspenso para Ativo podemos realizar a importação do arquivo em .CSV ou .JSON baixado do Portal Emprega Brasil para o mês de calculo da folha. [RH - Linha Protheus - GPE - Importação do arquivo Crédito trabalhador mês atual com mais de um contrato- eConsignado MP(1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33072630601751-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-do-arquivo-Cr%C3%A9dito-trabalhador-m%C3%AAs-atual-com-mais-de-um-contrato-eConsignado-MP-1-292-2025)

Todos os meses será necessário realizar a importação para o calculo do eConsignado ou realizar a alteração do campo Situação na rotina valores futuros para Ativo.

Para maior entendimento assista nosso vídeo HOW TO

**Saiba mais:**

[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)

[eConsignado (Crédito Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)
