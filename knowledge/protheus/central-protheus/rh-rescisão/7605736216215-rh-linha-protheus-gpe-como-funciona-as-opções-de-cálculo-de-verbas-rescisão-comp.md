---
article_id: 7605736216215
category: RH - Rescisão
content_hash: 247b6cc59c46946ff80ef7e2f09ec5fd47c2bfb947d4b0aa39f9c6cd01f18a13
fetched_at: '2026-06-28T22:43:52.093626+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona as opções de cálculo de Verbas rescisão
  complementar no cadastro do sindicato
type: support-article
updated_at: '2025-06-16T18:20:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7605736216215-RH-Linha-Protheus-GPE-Como-funciona-as-op%C3%A7%C3%B5es-de-c%C3%A1lculo-de-Verbas-rescis%C3%A3o-complementar-no-cadastro-do-sindicato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como funciona as opções de cálculo de Verbas rescisão complementar do cadastro do sindicato?  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7605639943319/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O campo **Vb. Res.Comp.** só tem efeito em casos onde a data base do dissídio é em meses posteriores ao mês da rescisão, mas a projeção do aviso esta dentro do mês da data base, por exemplo:  
  
Data demissão 15/05/2022  
Data final projeção aviso: 13/08/2022  
Data base dissídio 01/07/2022  
  
Então, como a data base do dissídio é em 01/07/2022, que é após o mês da rescisão, mas a projeção do aviso prévio passa essa data, o sistema permite escolher quais verbas serão reajustadas na rescisão complementar, conforme abaixo:  
  
**1-Todas:** Todas as verbas da rescisão serão reajustadas  
**2-Somente aviso:** Somente as verbas de aviso serão reajustadas (aviso prévio, ferias sobre aviso, 13º sobre aviso, suas médias e adicionais)  
**3-Aviso+verbas rescisórias:** Todas as verbas da rescisão original serão reajustadas menos saldo de salário
