---
article_id: 360044460314
category: RH - Provisão
content_hash: a72ba17d07964bb28dbb11c67d47df8deb59019d4dd9f5ad1adcef82112bff7e
fetched_at: '2026-06-28T22:43:55.721157+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Calcular Provisão com adicional de Periculosidade
  Sobre Salário
type: support-article
updated_at: '2025-06-17T20:29:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044460314-RH-Linha-Protheus-GPE-Como-Calcular-Provis%C3%A3o-com-adicional-de-Periculosidade-Sobre-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17714133079063) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como Calcular Provisão com Adicional de Periculosidade Sobre Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Na versão 12, os **Adicionais** (periculosidade, insalubridade, ATS, Ad. Cargo Confiança, Adic. Transferência, entre outros) mesmo que Incorporado ao Salário são considerados como Adicionais, sendo demonstrados em verbas especificas e não somados aos valores de férias e 13º. Sendo assim as baixas também serão dadas como Adicionais.

Para que o adicional seja calculado corretamente faça as seguintes configurações:

No cadastro do funcionário na aba adicionais deixar conforme o campo abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061576933)

No cadastro do sindicato na aba de periculosidade/ insalubridade deixar conforme abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060631834)

No cadastro de verbas verifique se existem cadastradas as seguintes verbas:

Verba com **ID 0318**  verba de base provento que  leva a base salarial do mês

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061577093)

Verba com **ID 0673** verba de base provento que leva a base da periculosidade do mês

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060632054)

Verba com **ID 0036** verba de periculosidade

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060632154)

Aba incidências deixar conforme figura abaixo:

O campo Base de calculo : leva a informação se a periculosidade é calculada sobre salário base ou salário ou incorporado.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060632234)

Ao calcular a folha note que existe a verba 318 **(ID 0318)** aonde trás o valor do salário  juntamente com o valor do adicional de periculosidade 916 **(ID 0673)** trás o valor do adicional de periculosidade do mês

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061577493)

Ao calcular a provisão note que no cabeçalho vem o salário sem o adicional, e na coluna de adicionais o valor do adicional proporcional aos dias de direito ( 453/30\*5=75,50)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061577533)

**Saiba Mais:**

[RH - Linha Protheus - GPE - Cálculo de Periculosidade sobre Salário e Faltas para Funcionário Mensalista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020755291-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Periculosidade-sobre-Sal%C3%A1rio-e-Faltas-para-Funcion%C3%A1rio-Mensalista?source=search)

[RH - Linha Protheus - GPE - Como configurar o cálculo de periculosidade sobre Salário + Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038877614-RH-Linha-Protheus-GPE-Como-configurar-o-c%C3%A1lculo-de-periculosidade-sobre-Sal%C3%A1rio-Verbas?source=search)

[RH - Linha Protheus - GPE - Como configurar periculosidade e insalubridade para que sejam calculadas pelas horas informadas e não pelas horas do cadastro do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000044628-RH-Linha-Protheus-GPE-Como-configurar-periculosidade-e-insalubridade-para-que-sejam-calculadas-pelas-horas-informadas-e-n%C3%A3o-pelas-horas-do-cadastro-do-funcion%C3%A1rio?source=search)
