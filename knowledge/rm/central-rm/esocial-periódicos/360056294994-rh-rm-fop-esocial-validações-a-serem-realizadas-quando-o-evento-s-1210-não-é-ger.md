---
article_id: 360056294994
category: esocial - Periódicos
content_hash: d01d7d708ff4f45703055a218bb19dae9a4a6af7360d96393d5a254ebb239a47
fetched_at: '2026-06-28T22:47:09.512235+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Validações a serem realizadas quando o evento S-1210
  não é gerado para funcionário cadastrado no RM Labore
type: support-article
updated_at: '2024-12-26T16:02:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056294994-RH-RM-FOP-eSocial-Valida%C3%A7%C3%B5es-a-serem-realizadas-quando-o-evento-S-1210-n%C3%A3o-%C3%A9-gerado-para-funcion%C3%A1rio-cadastrado-no-RM-Labore
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15669654183959)** Tempo aproximado para leitura: **00:01:00 min****Dúvida**O que validar quando o evento S-1210 não é gerado para funcionário cadastrado no RM Labore?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**As validações a serem realizadas sobre a geração do evento S-1210 são:

**1.** Data de pagamento dos eventos: Para geração do evento S-1210 o sistema considera a data de pagamento das verbas, sendo assim caso não haja verba paga no mês de apuração, não será gerado o evento S-1210;  
**2.** Verifique o período de apuração que está sendo gerado o evento S-1210.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17153539717271)**

**3.** Caso a verba seja paga dentro do mês de apuração, acesse **Administração de Pessoal | Funcionários | Ficha Financeira** e verifique se o **Mês Caixa** do período cadastrado está de acordo com o mês de pagamento do evento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15669603868055)

**4.** Além disto, dê duplo clique no período e identifique se o **Ano Caixa** também consta preenchido e com a informação correta.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15669626090263)

   **5.**Em caso que o S-1210 é referente à **rescisão**, será necessário conferir se a **data de pagamento** corresponde ao período que está sendo gerado o S-1210. Caso necessário realize o ajuste da data de pagamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21540108196119)

**6.** Para lançamentos do **Fluxus** é utilizado a **Data da Baixa.  
    7.** O valor das **férias** será levado pela data de pagamento da mesma, onde o sistema irá validar pelo **recibo de férias**.

**Exemplo:** Competência setembro/2023  
                          Inicio de gozo de férias =  01/10/2023  
                          Data de pagamento das férias = 28/09/2023  
                          O valor será levado no período de apuração de setembro/2023

**Saiba mais**  
Para mais informações sobre o evento S-1210 acesse:  
      • [Mapeamento evento S-1210](https://tdn.totvs.com/display/public/LRM/Evento+S-1210)
