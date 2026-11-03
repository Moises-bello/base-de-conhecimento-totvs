---
article_id: 360038025373
category: MDT - Atendimento Médico
content_hash: ca44a28d2de0608eef14d2fd76fb81fc9114695282fb7e68da4b594e0f934848
fetched_at: '2026-06-28T22:44:20.523952+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Ao lançar afastamento por Licença Maternidade na
  rotina Atestado Médico (MDTA685) e informar o horário, o sistema está considerando
  119 dias de atestado ao invés de 120 dias
type: support-article
updated_at: '2025-03-03T18:16:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038025373-RH-Linha-Protheus-MDT-Ao-lan%C3%A7ar-afastamento-por-Licen%C3%A7a-Maternidade-na-rotina-Atestado-M%C3%A9dico-MDTA685-e-informar-o-hor%C3%A1rio-o-sistema-est%C3%A1-considerando-119-dias-de-atestado-ao-inv%C3%A9s-de-120-dias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372804519191)** Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao lançar afastamento por Licença Maternidade na rotina Atestado Médico (MDTA685) e informar o horário, o sistema está considerando **119** dias de atestado ao invés de **120** dias.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Esse problema ocorre devido aos dias informados no parâmetro **MV\_NG2LICE** estarem incorretos, ou o horário inicial e final do atestado não está totalizando 24 horas.  
  
**Solução**Para o sistema gerar as informações corretamente verifique no modulo Configurador (SIGACFG) no caminho: Ambiente > Cadastro > Parâmetro, se o parâmetro **MV\_NG2LICE** está com **120**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8496165379351)  
  
E no modulo SIGAMDT acesse o caminho: Atualizações > Atendimento Médico > Atestado Médico (MDTA685), entre no atestado de maternidade, e verifique se e o horário informado do atestado está com "Hora Inicial : **00:00**" e "Hora Fim: **23:59**".   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050112093)  
  
**Observação**  
O parâmetro **MV\_NG2LICE** que tem por objetivo tratar se a licença maternidade será de 120 ou 180 dias.   
 **Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
