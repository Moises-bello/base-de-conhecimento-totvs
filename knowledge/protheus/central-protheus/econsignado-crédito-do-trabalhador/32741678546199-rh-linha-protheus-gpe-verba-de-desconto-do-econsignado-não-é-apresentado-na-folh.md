---
article_id: 32741678546199
category: eConsignado (Crédito do Trabalhador)
content_hash: d45e9700868d3f63ed5bded192d386a0c8a639fbe0b39dfcbca3d9577c660025
fetched_at: '2026-06-28T22:43:07.154564+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH  - Linha Protheus - GPE - Verba de desconto do econsignado não é apresentado
  na folha de pagamento - Econsignado MP(1.292/2025)
type: support-article
updated_at: '2026-06-26T14:36:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32741678546199-RH-Linha-Protheus-GPE-Verba-de-desconto-do-econsignado-n%C3%A3o-%C3%A9-apresentado-na-folha-de-pagamento-Econsignado-MP-1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32741678515351) Tempo aproximado para leitura: **02:00:00min**  
  
**Dúvida**  
Verba de desconto do Econsignado não é apresentada no Provisionamento de férias , Adiantamento e no calculo da Folha de pagamento.   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Isso ocorre quando no mês anterior o empréstimo econsignado foi lançado de forma manual e na competência atual não foi feita a importação do arquivo.  
  
Após o calculo da folha e fechamento do período, o sistema atualiza na SRK os seguintes campos conforme abaixo, deixando o campo Status como SUSPENSO, até que a importação do mês de calculo seja realizado e com isso o sistema atualiza para ATIVO  
**Numero parcela paga /Valor Pago /Dt Prox Vencimento /Saldo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32741694308631)  
**Situação**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32741678517911)**  
  
Quando a empresa opta pelo lançamento manual, após o fechamento de cada período é necessário ir em **Atualizações >Lançamentos > Consta Corrente** e ajustar o campo Status de Suspenso para **ATIVO**, assim o sistema irá enxergar a verba para os cálculos de férias / ADI e Folha

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32741694312855)**

**Saiba Mais**  
[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)
