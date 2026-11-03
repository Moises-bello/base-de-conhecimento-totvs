---
article_id: 32730193438999
category: eConsignado (Crédito do Trabalhador)
content_hash: ad8460fa21635ae9b01d9392feb66fe32b3b4832662319129abf5dbc5fd75c05
fetched_at: '2026-06-28T22:43:07.087324+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH  - Linha Protheus - GPE - Como é realizado o desconto do Econsignado quando
  a margem consignável fica menor que o valor da parcela a ser descontado   - Econsignado
  MP(1.292/2025)
type: support-article
updated_at: '2026-06-25T18:44:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32730193438999-RH-Linha-Protheus-GPE-Como-%C3%A9-realizado-o-desconto-do-Econsignado-quando-a-margem-consign%C3%A1vel-fica-menor-que-o-valor-da-parcela-a-ser-descontado-Econsignado-MP-1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32730141914263) Tempo aproximado para leitura: **02:00:00min**  
  
**Dúvida**  
Como é realizado o desconto do Econsignado na folha de pagamento quando a margem consignável fica menor que o valor da parcela a ser descontado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

O sistema realizará apenas o desconto permitido dentro da margem consignável disponível. O valor excedente não poderá ser descontado em folha, cabendo ao trabalhador entrar em contato diretamente com a instituição financeira para negociar o saldo restante.  
  
Exemplo:  
Lançamentos Futuros - Parcela R$ 1.181,81  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32730141914775)

Mnemônico **P\_DEDCONS**, deduz as verbas informadas da Margem Consignável (Verbas sem Incidência para o INSS) - [RH - Linha Protheus - GPE - Como deduzir outras verbas de desconto da margem de consignação do Programa Crédito Trabalhador eConsignado (MP 1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32696289251351-RH-Linha-Protheus-GPE-Como-deduzir-outras-verbas-de-desconto-da-margem-de-consigna%C3%A7%C3%A3o-do-Programa-Cr%C3%A9dito-Trabalhador-eConsignado-MP-1-292-2025)  
OBS. nesse exemplo a verba indicada no mnemônico não possui ID de calculo e nem incidências para INSS e IRRF  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32735540532119)  
  
Calculo da Folha   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32735556683671)  
**Composição da Margem consignável**   
Salario + Insalubridade - faltas - INSS - verba 575  
2.517,11 + 612,00 - 251,71 - 600,00 - 238,69 = **2.038,71 \* 35% = R$ 713,55**  
  
  
**Para um maior conhecimento assista os videos How To abaixo:**

**Saiba mais:**  
[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
[Orientação consultoria de segmentos - Credito do Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-3.3Reten%C3%A7%C3%A3odoempr%C3%A9stimonaFolhadePagamento)  
[eConsignado (Credito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)
