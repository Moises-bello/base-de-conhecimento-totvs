---
article_id: 32696289251351
category: eConsignado (Crédito do Trabalhador)
content_hash: b41b1f011bacaf19ba6b3cbb9944421a9cf71b92f0e14a89f154b909d25ab4fd
fetched_at: '2026-06-28T22:43:07.220927+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Como deduzir outras verbas de desconto da margem
  de consignação do Programa Crédito Trabalhador eConsignado (MP 1.292/2025)
type: support-article
updated_at: '2025-06-11T11:15:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32696289251351-RH-Linha-Protheus-GPE-Como-deduzir-outras-verbas-de-desconto-da-margem-de-consigna%C3%A7%C3%A3o-do-Programa-Cr%C3%A9dito-Trabalhador-eConsignado-MP-1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32696272530327) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como deduzir outras verbas de desconto da margem de consignação do Programa Crédito Trabalhador eConsignado (MP 1.292/2025)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que seja possível realizar o abatimento de outras verbas de desconto da margem de consignação do eConsignado, foi criado o mnemônico **P\_DEDCONS**. Esse mnemônico foi criado, devido a inexistência de informações completas sobre as verbas que deveriam ser consideradas na formação da base. Para utilizar o mnemônico, realize os seguintes passos:  
  
**1.** Para configurar o mnemônico acesse **Atualizações > Definições de Cálculos > Mnemônicos (GPE300)** > **Pesquise pelo mnemônico P\_DEDCONS > Clique em Alterar > Configure com a verba que deseja deduzir da margem de consignação > clique em Confirmar** (as verbas informadas no mnemônico devem ser entre aspas duplas e caso tenha mais que uma devem ser separadas com Barras. Exemplo: "001/002/003");

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696272531351)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696289226007)  
  
**2.** Realize o calculo da folha de pagamento em **Miscelânea > Cálculos > Por Roteiros (GPEM020)**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696289226775)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696272534935)  
  
**3.** Visualize o cálculo em **Consultas > Cadastros > Recibo de Pagamento (GPEA630)**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32696272535703)  
  
**Cálculo:**

Base da Margem Consignável= Proventos - INSS - IRRF - Verbas de desconto com SIM para INSS - Verbas do P\_DEDCONS

Base da Margem Consignável= R$6500 - R$ 564,91 - R$ 437,40 - R$ 1083,35 - R$ 650,00

Base da Margem Consignável= R$3761,34

Máximo de desconto para o eConsignado= R$3761,34 \* 35%= R$1316,47

**Observação:** Verbas de desconto com SIM para INSS, não precisam ser incluídas no mnemônico P\_DEDCONS

**Saiba mais:**

[eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)

[Manual Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)
