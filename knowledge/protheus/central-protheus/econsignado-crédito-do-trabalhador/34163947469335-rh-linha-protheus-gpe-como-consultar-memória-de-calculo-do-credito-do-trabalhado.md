---
article_id: 34163947469335
category: eConsignado (Crédito do Trabalhador)
content_hash: f7ad00f6e2494d3a35f6cd66816ed3a3245228984b1c1fbdd2a90b3f677bf58b
fetched_at: '2026-06-28T22:43:07.208462+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Como consultar memória de calculo do Credito do
  trabalhador Econsignado
type: support-article
updated_at: '2026-06-18T11:26:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34163947469335-RH-Linha-Protheus-GPE-Como-consultar-mem%C3%B3ria-de-calculo-do-Credito-do-trabalhador-Econsignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34163986879639) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como consultar memória de calculo do Credito de Trabalhador eConsignado?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para consultar a memória de calculo do fonte padrão referente o Credito do Trabalhador (eConsignado), é necessário configurar o mnemônico **P\_LMEMCALC com .T., em Atualizações > Definições de Cálculo > Mnemônicos (GPEA300)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34163947447959)

Após ativação do mnemônico P\_LMEMCALC, realizamos o calculo da folha de pagamento em **Miscelânea > Cálculos > Por roteiro (GPEM020)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34163986880407)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34163986882199)

Verificamos o calculo em **Atualizações > Lançamentos > Por Funcionários (GPEA090)** > selecionando o funcionário desejado, clicamos em **Visualizar > Outras Ações > Consultar calculo > Outras Ações > Consultar memória de calculo > duplo clique em cima do calculo desejado**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34163947451159)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34163986885527)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34163986892951)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34174454188183)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40582481003287)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40582481004311)  
Não havendo margem disponível, não ocorrerá o desconto da parcela do empréstimo.  
         Essa situação será demonstrada na memória de cálculo, incluindo:

* A ausência de margem consignável;
* Os valores das verbas de empréstimo zerados.

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40582481005847)

  **Importante:** A consulta da memória de calculo só será possível se o mnemônico **P\_LMEMCALC** estiver habilitado no momento do calculo.

Para melhor entendimento assista nossos vídeos How To abaixo sobre memória de cálculo eConsignado:

**Saiba mais:**  
[eConsignado](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)  
https://tdn.totvs.com/pages/releaseview.action?pageId=1035885821
