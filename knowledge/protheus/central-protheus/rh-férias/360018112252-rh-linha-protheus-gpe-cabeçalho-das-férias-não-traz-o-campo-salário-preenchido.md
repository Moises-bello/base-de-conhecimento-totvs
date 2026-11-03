---
article_id: 360018112252
category: RH - Férias
content_hash: 0fc47ba2e5618db8216f25b67d729868e5544bf3529d410e00ee86cae4dc6e98
fetched_at: '2026-06-28T22:43:57.969809+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Cabeçalho das Férias não traz o campo Salário preenchido
type: support-article
updated_at: '2025-08-20T17:05:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018112252-RH-Linha-Protheus-GPE-Cabe%C3%A7alho-das-F%C3%A9rias-n%C3%A3o-traz-o-campo-Sal%C3%A1rio-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26594292277015) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**O cabeçalho das férias não traz o campo salário preenchido. O que verificar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.   
  
**Solução**Na versão 12, as informações referente ao salário **não serão carregadas** automaticamente no preenchimento do cabeçalho. Isso ocorre porque foi introduzido o novo parâmetro **MV\_DIASPER,** que permite ao cliente escolher se o cálculo do salário deve considerar **os dias do mês** ou uma **base fixa de 30 dias.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32066467231127)

Após o preenchimento do **cabeçalho** (início das férias) e a **execução do cálculo** (F6), o sistema verificará o parâmetro configurado. Somente então será realizado o cálculo do "Salário Dia" e do "Salário Mês" no cabeçalho.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32066474423959)

Para **conferir/alterar** o parâmetro **MV\_DIASPER**, realize os seguintes passos:  
1. Acesse ambiente Configurador - **SIGACFG**;  
2. Busque relação deparâmetros do sistema através do menu **Ambiente > Cadastros > Parâmetros**;  
3. Busque através do ícone da lupa o parâmetro **MV\_DIASPER**;  
4. Informe **conteúdo = 1**, para que sistema utilize a**quantidade de dias do mês como divisor**, ou **conteúdo = 2** para que sistema utilize **30 dias como divisor**(para **exemplo**, utilizamos conteúdo = 2).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26611154161815)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26611154164375)

**Saiba Mais:**

[RH - Linha Protheus - GPE - Férias Proporcionais dividindo por 31 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003366622-RH-Linha-Protheus-GPE-F%C3%A9rias-Proporcionais-dividindo-por-31-dias)  
[RH - Linha Protheus - GPE - Como configurar o parâmetro MV\_DIASPER para definir regra de calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059317953-RH-Linha-Protheus-GPE-Como-configurar-o-par%C3%A2metro-MV-DIASPER-para-definir-regra-de-calculo)  
[RH - Linha Protheus - GPE - Como sistema calcula folha de pagamento para funcionário afastado, com MV\_DIASPER igual a 2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015099431-RH-Linha-Protheus-GPE-Como-sistema-calcula-folha-de-pagamento-para-funcion%C3%A1rio-afastado-com-MV-DIASPER-igual-a-2)
