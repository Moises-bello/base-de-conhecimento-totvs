---
article_id: 4473980561431
category: Evento S-2240
content_hash: 8f435335fe4d9f6c4126ab0866ad15d452f32ace92056069ebd0837c5b7ef572
fetched_at: '2026-06-28T22:45:23.670679+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Não foi encontrado um ambiente
  relacionado ao departamento do funcionário
type: support-article
updated_at: '2025-03-11T18:46:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4473980561431-RH-Linha-Protheus-MDT-eSocial-S-2240-N%C3%A3o-foi-encontrado-um-ambiente-relacionado-ao-departamento-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25305444681623) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**O que verificar quando apresentar a mensagem: "Não foi encontrado um ambiente relacionado ao departamento do funcionário."  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Verificar no cadastro do **Funcionário** qual o **Departamento** apontado, rotina (*GPEA010*) campo a ser avaliado (**RA\_DEPTO**) através do caminho:  
**Atualizações - Funcionário - Funcionário** (*SIGAGPE*), ou  
**Atualizações - Cadastros Gerais - Funcionário** (*SIGAMDT*).  
  
Após esta verificação certifique-se que no cadastro do **Ambiente Físico** rotina (*MDTA1*65), tem o relacionamento do Departamento do Funcionário. Caso não tenha inclua e salve o cadastro, conforme exemplo a seguir:  
  
![gy0m2JOymq.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4474001646359)  
  
Para mais informações sobre as entidades relacionadas ao ambiente físico acesse a documentação  
[RH - Linha Protheus - MDT - eSocial - S-2240 - Novas Entidades de Relacionamento ao Ambiente Físico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409384342679-RH-Linha-Protheus-MDT-eSocial-S-2240-Novas-Entidades-de-Relacionamento-ao-Ambiente-F%C3%ADsico)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
