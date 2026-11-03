---
article_id: 360052632133
category: RH - Calculo Autonomo/Prolabore
content_hash: 86318e5eff68b48f69a396974c4c03e28201ea29e2410ca4f107d7293e433d24
fetched_at: '2026-06-28T22:43:15.139336+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar a separação do desconto de SEST e
  SENAT no cálculo de autônomo carreteiro
type: support-article
updated_at: '2025-04-15T18:03:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052632133-RH-Linha-Protheus-GPE-Como-efetuar-a-separa%C3%A7%C3%A3o-do-desconto-de-SEST-e-SENAT-no-c%C3%A1lculo-de-aut%C3%B4nomo-carreteiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18882607963159) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como efetuar a separação do desconto de SEST e SENAT no cálculo da folha de autônomo carreteiro?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Como o  layout do eSocial possui códigos de incidência tributária da rubrica para previdência social para cada entidade, o sistema efetuará do desconto de SEST e SENAT em verbas separadas no cálculo de autônomo carreteiro.

O desconto do SEST será efetuado na verba de **Id de cálculo 0437**, através do percentual cadastrado no **mnemônico P\_SEST**, e o desconto do SENAT será efetuado na verba de **Id de cálculo 1456,** através do percentual cadastrado no **mnemônico P\_SENAT.**

Para cadastrar as verbas com os id's 0437 e 1456 acesse **Atualizações > Definições de Cálculos> Verbas (GPEA040)** e clique em **Incluir**. [RH - Linha Protheus - GPE - Como cadastrar verbas no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411677253783-RH-Linha-Protheus-GPE-Como-cadastrar-verbas-no-Protheus?source=search)

Para configurar os mnemônicos acesse **Atualizações > Definições de Cálculos > Mnemônicos (GPEA300)** pesquise pelo mnemônico desejado e clique em **Alterar** e configure conforme a necessidade.

Exemplo de preenchimento dos mnemônicos:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18882601705623)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18882601713687)**

**Observação:** Informe os percentuais nos mnemônicos citados acima utilizando ponto e não vírgula.

**Saiba mais:**[Separação do desconto de SEST e SENAT](https://tdn.totvs.com/pages/viewpage.action?pageId=364924146)  
[RH - Cálculo Autônomo](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
