---
article_id: 33072704997271
category: eConsignado (Crédito do Trabalhador)
content_hash: e09bcf70a5fa07e8f4aa44907611aa649eb2beef44799d30da09b8b9d3e24e93
fetched_at: '2026-06-28T22:43:07.368133+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Provisionamento no Adiantamento mais de um contrato
  referente ao Econsignado (Programa Crédito do Trabalhador MP1.292/2025)
type: support-article
updated_at: '2025-07-16T20:56:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33072704997271-RH-Linha-Protheus-GPE-Provisionamento-no-Adiantamento-mais-de-um-contrato-referente-ao-Econsignado-Programa-Cr%C3%A9dito-do-Trabalhador-MP1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33072704982679) Tempo aproximado para leitura: **00:02:00min**

**Dúvida**  
Como é feito o provisionamento no Adiantamento referente ao eConsignado quando se tem mais de um contrato?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para realizar o cálculo de adiantamento com o **provisionamento** de todos os empréstimos eConsignado , siga os passos abaixo:

**1.** Realize a importação da parcela para valores futuros ou realize o lançamento da verba de natureza 9253 - No exemplo abaixo foi realizado a importação do arquivo para valores futuros.   
Obs. Caso opte pelo lançamento manual, é necessário criar uma verba para cada novo contrato.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33518792296983)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33518832448279)

2. Lançamentos Futuros   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33518792304151)

**3.** Para possibilitar o provisionamento do empréstimo referente ao Programa Crédito do Trabalhador no cálculo de adiantamento, foram criados três novos identificadores de calculo, sendo necessário a criação das verbas conforme artigo: [Como cadastrar as verbas de Provisionamento nas Férias e Adiantamento referente ao eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32292447017239-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-Provisionamento-nas-F%C3%A9rias-e-Adiantamento-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador);

4. Realize o calculo pela rotina de lançamentos por funcionários (GPEA580) ou pela rotina de Cálculos por roteiros (GPEM020).

5. Após o calculo o sistema vai fazer a soma de todos os contratos e aplicar o mesmo percentual do Adiantamento, no exemplo em questão o Adiantamento é de 40%.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33518832450711)

Soma dos contratos da SRK = 311,89+ 172,09 + 197,22 + 77,16 = R$ 758,36 \* 40% = 303,34 desconto do Provisionamento.  
  
6. Calculo do Folha após o fechamento do roteiro ADI.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33518832451607)  
  
O valor que está sendo apresentado na verba de 501 - DESC ADIANTAMENTO é o valor provisionado de R$ 303,34 + Liquido do ADI R$ 2.697,00, então o sistema apenas lança a verba de Provento no ID 1975 pra devolver o valor descontado de provisionamento no ADI.   
  
  
**Saiba mais:**  
[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
[RH - Linha Protheus - GPE - eConsignado - Informações e atualizações sobre Credito do Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-eConsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-do-Trabalhador-MP1-292-2025)  
[Econsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=944703898>
