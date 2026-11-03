---
article_id: 360058147293
category: RH - Definições de Cálculo
content_hash: e8689734e3e4911e51172f55cac9e2fd15f18532dccbd44060dc5e9555dbffe1
fetched_at: '2026-06-28T22:43:22.506205+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Percentual de terceiros está sendo calculado a
  menor, quando tem cadastro para outras entidades na S038
type: support-article
updated_at: '2025-01-15T23:49:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058147293-RH-Linha-Protheus-GPE-Percentual-de-terceiros-est%C3%A1-sendo-calculado-a-menor-quando-tem-cadastro-para-outras-entidades-na-S038
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26196274226199) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Percentual de terceiros está sendo calculado a menor, quando tem cadastro para outras entidades na S038  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quando existe cadastro para outras entidades, o percentual de terceiros é calculado somente sobre a diferença, ou seja, no exemplo abaixo está sendo calculado sobre 0,8%, pois o sistema faz o seguinte cálculo:  
% Terceiros - % SENAI - %SESI = 3,3 - 1 - 1,5 = 0,8  
![](https://totvssuporte.zendesk.com/attachments/token/YF5IacMtPG4LQj5yoy4tozgAo/?name=inline-1915494081.png)  
Para que calcule sobre um total de 3,3%, deve-se incluir no campo % Terceiros na tabela S038 ​o valor de 5,8%, dessa forma abaterá os valores de SENAI e SESI e calculará sobre 3,3%.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Cálculo Terceiros não considera informação da tabela S038](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051271693-RH-Linha-Protheus-GPE-C%C3%A1lculo-Terceiros-n%C3%A3o-considera-informa%C3%A7%C3%A3o-da-tabela-S038)  
[RH - Linha Protheus - GPE - Atenção: Tabelas S037 e S038 não estão cadastradas para o período de cálculo na Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13854639857175-RH-Linha-Protheus-GPE-Aten%C3%A7%C3%A3o-Tabelas-S037-e-S038-n%C3%A3o-est%C3%A3o-cadastradas-para-o-per%C3%ADodo-de-c%C3%A1lculo-na-Provis%C3%A3o)  
[RH - Linha Protheus - GPE - Como cadastrar os percentuais de INSS terceiros rateados pelas entidades na Tabela S038](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13008616340887-RH-Linha-Protheus-GPE-Como-cadastrar-os-percentuais-de-INSS-terceiros-rateados-pelas-entidades-na-Tabela-S038)  
[RH - Linha Protheus - GPE - Quais possíveis rotinas para cadastro dos Encargos da Empresa ( % de Acidente de Trabalho, Terceiros e INSS Empresa)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049697274-RH-Linha-Protheus-GPE-Quais-poss%C3%ADveis-rotinas-para-cadastro-dos-Encargos-da-Empresa-de-Acidente-de-Trabalho-Terceiros-e-INSS-Empresa)
