---
article_id: 17920655041047
category: MDT - eSocial
content_hash: 560609823f4fe6daefeca74b74f502f4e2d28015bf920bb48663d249c783d09e
fetched_at: '2026-06-28T22:44:29.280584+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: RH - Linha Protheus - MDT - Quais as integrações entre o Módulo Medicina e
  Segurança do Trabalho e o Módulo Automação Fiscal TAF
type: support-article
updated_at: '2025-08-05T16:50:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17920655041047-RH-Linha-Protheus-MDT-Quais-as-integra%C3%A7%C3%B5es-entre-o-M%C3%B3dulo-Medicina-e-Seguran%C3%A7a-do-Trabalho-e-o-M%C3%B3dulo-Automa%C3%A7%C3%A3o-Fiscal-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17920649502231) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Quais as integrações entre o Módulo Medicina e Segurança do Trabalho e o Módulo Automação Fiscal TAF?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Existe a integração entre o MDT e TAF para os eventos do SST, sendo eles:  
[Como gerar o evento S-2210](https://tdn.totvs.com/display/public/PROT/S-1.0-+eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2210#como_gerar-how_tos)  
[Como gerar o evento S-2220](https://tdn.totvs.com/display/public/PROT/S-1.0-+eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2220#como_gerar-how_tos)

[Como gerar o evento S-2221](https://tdn.totvs.com/display/PROT/S-1.2-+eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2221)  
[Como gerar o evento S-2240](https://tdn.totvs.com/display/public/PROT/S-1.0-+eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2240#como_gerar-how_tos)

Para saber como gerar cada evento citado basta clicar no link de cada um para maiores informações.  
  
Em alguns casos após excluir um cadastro relacionado aos eventos citados acima, pode ser gerado o evento de exclusão **S-3000** que é um comportamento padrão de todos os eventos não sendo exclusivo do Módulo de Medicina e Segurança do Trabalho  
  
Para que esses eventos sejam integrados com módulo TAF é necessário que o parâmetro **MV\_NG2ESOC** esteja com valor **'S'(Sim)** no configurador do Protheus **(SIGACFG)**.  
  
**Observação:** É possível que o Módulo MDT, dependendo de condições pré-determinadas pelo GPE, possa gerar o evento **S-2230 (Afastamento Temporário)** ao cadastrar uma **CAT**. Ressaltando que ao gerar o evento **S-2210** a empresa não esta desobrigada de enviar o evento S-2230 (em alguns casos).

Maiores informações sobre a geração deste evento consulte:

[Acidente de Trabalho que resulte em afastamento preciso enviar apenas o evento S-2210?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406754977687)  
  
**Saiba mais**[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20)  
[ChatBot Carol](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
