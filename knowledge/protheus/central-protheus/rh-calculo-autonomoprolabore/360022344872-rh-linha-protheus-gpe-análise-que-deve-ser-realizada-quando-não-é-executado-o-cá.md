---
article_id: 360022344872
category: RH - Calculo Autonomo/Prolabore
content_hash: 1a0570a1b494ac2dde5691f4e2f17f5c43567fa85fb198c2bf52ba087c0567a8
fetched_at: '2026-06-28T22:43:15.054410+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Análise que deve ser realizada quando não é executado
  o cálculo para autônomo
type: support-article
updated_at: '2025-08-20T19:52:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022344872-RH-Linha-Protheus-GPE-An%C3%A1lise-que-deve-ser-realizada-quando-n%C3%A3o-%C3%A9-executado-o-c%C3%A1lculo-para-aut%C3%B4nomo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24996613310999) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**O que analisar quando não é executado o cálculo para autônomo?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34327459507095)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**- Verifique se a Data de Admissão no cadastro do Autônomo em **Atualizações > Funcionários > Contribuinte Individual (GPEA265)**, não é posterior a data de pagamento do período que está sendo utilizado para cálculo;  
  
- Verifique o conteúdo do parâmetro **MV\_AUTOSRC**, realize testes com o parâmetro desativado configurando com **.F.** via **Configurador SIGACFG** em **Ambiente > Cadastros > Parâmetros (CFGX017).**  
Para mais informações sobre este parâmetro [Clique Aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=234613717).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34327459510935)

-Verifique o parâmetro **MV\_CALCINF**. Execute o teste com este parâmetro com o conteúdo **N** via **Configurador SIGACFG** em **Ambiente > Cadastros > Parâmetros (CFGX017)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34327445518487)  
  
-Execute os procedimentos do *link* abaixo para recriar as fórmulas e os Roteiros de Cálculo em ambiente de testes:   
[RH - Linha Protheus - GPE - Como executar cálculos da folha de pagamento sem customizações (mnemônicos, roteiros, fórmulas e pontos de entrada)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018448392)

**Saiba Mais**

[RH - Linha Protheus - GPE - Como cadastrar um Autônomo ou Pró-labore](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052067393-RH-Linha-Protheus-GPE-Como-cadastrar-um-Aut%C3%B4nomo-ou-Pr%C3%B3-labore)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
