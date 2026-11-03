---
article_id: 360048614074
category: RH - Rescisão
content_hash: 07a4d926186ea19597b8fdf0ebe28691517c8f0161752f255b0020f39810f2e0
fetched_at: '2026-06-28T22:43:51.078687+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao calcular rescisão complementar por dissídio
  gera a mensagem: Foi selecionada rescisão complementar por dissídio, mas não foi
  encontrado calculo de dissídio, a rescisão não sera gerada.'
type: support-article
updated_at: '2025-05-07T21:15:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048614074-RH-Linha-Protheus-GPE-Ao-calcular-rescis%C3%A3o-complementar-por-diss%C3%ADdio-gera-a-mensagem-Foi-selecionada-rescis%C3%A3o-complementar-por-diss%C3%ADdio-mas-n%C3%A3o-foi-encontrado-calculo-de-diss%C3%ADdio-a-rescis%C3%A3o-n%C3%A3o-sera-gerada
---

**Ocorrência**  
Na rotina de rescisão, ao calcular Rescisão Complementar por Dissídio apresenta a mensagem: Foi Selecionado rescisão complementar por dissídio, mas não foi encontrado calculo de dissídio, a rescisão não será gerada.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12.  
  
**Causa**Esse incidente ocorre porque o compartilhamento da tabela RHH não esta preenchido.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19541112573591)

**Solução:**Esta inconsistência do compartilhamento em branco pode ser encontrada em algumas bases, principalmente em migração ou implantação.

Para solucionar essa ocorrência, em ambiente de testes, realize a manutenção no dicionário para a RHH, pois esta tabela deve ficar totalmente exclusiva, e na tabela RHH em que estão os registros do acumulado do dissídio, avalie se o compartilhamento está de acordo com o conteúdo do campo filial.

Caso tenha dúvidas para execução do procedimento acima, é necessário agendamento de analista *in loco*.

[MP - GPE - Exclusão do cálculo de dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037259774-MP-GPE-Exclus%C3%A3o-do-c%C3%A1lculo-de-diss%C3%ADdio-?source=search)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073370053)

**Obs:  O preenchimento incorreto das tabelas S50 e S126 podem causar inconsistência no cálculo.**

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

[RH - Linha Protheus - GPE - eSocial - S-1200 - Ao gerar os Eventos Periódicos o sistema apresenta no log a mensagem "Preenchimento incorreto das tabelas S050/S126. As informações de dissídio não foram geradas"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017971692-RH-Linha-Protheus-GPE-eSocial-S-1200-Ao-gerar-os-Eventos-Peri%C3%B3dicos-o-sistema-apresenta-no-log-a-mensagem-Preenchimento-incorreto-das-tabelas-S050-S126-As-informa%C3%A7%C3%B5es-de-diss%C3%ADdio-n%C3%A3o-foram-geradas-?source=search)
