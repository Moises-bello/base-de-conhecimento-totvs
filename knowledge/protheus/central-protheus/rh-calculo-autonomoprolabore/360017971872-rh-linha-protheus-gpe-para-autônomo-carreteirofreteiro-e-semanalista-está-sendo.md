---
article_id: 360017971872
category: RH - Calculo Autonomo/Prolabore
content_hash: fb7d6779f886a41f21bec4fdbf132e13e1e2aa41f1c2ebe147099a43e6fb68a7
fetched_at: '2026-06-28T22:43:15.248448+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Para autônomo carreteiro/freteiro e semanalista
  está sendo calculando incorretamente o IRRF de freteiro a partir da segunda semana
  e não traz a verba de Dedução de INSS da base de IR
type: support-article
updated_at: '2025-05-07T14:28:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017971872-RH-Linha-Protheus-GPE-Para-aut%C3%B4nomo-carreteiro-freteiro-e-semanalista-est%C3%A1-sendo-calculando-incorretamente-o-IRRF-de-freteiro-a-partir-da-segunda-semana-e-n%C3%A3o-traz-a-verba-de-Dedu%C3%A7%C3%A3o-de-INSS-da-base-de-IR
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24997918528791) Tempo aproximado para leitura:* **00:01:00 min**

**Ocorrência**

No módulo Gestão de Pessoal, para **autônomo carreteiro/freteiro** e **semanalista** está sendo calculando incorretamente o **[IRRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017975092)** de freteiro a partir da segunda semana e **não traz a verba de Dedução de INSS da base de IR.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 12.1.17  
  
**Solução**Ajustado o cálculo para apurar corretamente a base de IRRF de Autônomos carreteiros/freteiros semanalistas e ajustada a geração da verba de dedução de INSS da base de IR para esta categoria de trabalhadores.  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realizar o *backup* prévio;  
2. Aplicar o pacote acumulado do RH;  
3. Refaça o teste.  
  
**Observação**: Para o sistema, autônomo carreteiro/freteiro é aquele que no cadastro de autônomo possui o campo RA\_CATEG preenchido com 15 ou 16 ou o campo RA\_CATEFD preenchido com 711 ou 712.   
Este ajuste é baseado no desmembramento do cálculo verbas de autônomo freteiro carreteiro, documentação disponível em:

[RH - Linha Protheus - GPE - Autônomo Carreteiro/Freteiro - Desmembramento do Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016300812-RH-Linha-Protheus-GPE-Aut%C3%B4nomo-Carreteiro-Freteiro-Desmembramento-do-C%C3%A1lculo?source=search)

**Saiba Mais**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
