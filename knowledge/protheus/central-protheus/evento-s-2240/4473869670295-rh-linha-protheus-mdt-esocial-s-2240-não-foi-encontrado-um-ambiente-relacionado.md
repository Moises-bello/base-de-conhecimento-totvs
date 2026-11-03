---
article_id: 4473869670295
category: Evento S-2240
content_hash: f7d9553c079b5e94c0a1695ab31f4c1f9a7c10f6a18101581ce4070b40a0b757
fetched_at: '2026-06-28T22:45:23.666600+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Não foi encontrado um ambiente
  relacionado ao centro de custo do funcionário
type: support-article
updated_at: '2025-03-11T18:46:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4473869670295-RH-Linha-Protheus-MDT-eSocial-S-2240-N%C3%A3o-foi-encontrado-um-ambiente-relacionado-ao-centro-de-custo-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25305430282135) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**O que verificar quando apresentar a mensagem: " Não foi encontrado um ambiente relacionado ao centro de custo do funcionário"?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**  
Verificar no cadastro do **Funcionário** qual o **Centro de Custo** apontado, rotina (*GPEA010*) campo a ser avaliado (**RA\_CC**) através do caminho:  
**Atualizações - Funcionário - Funcionário** (*SIGAGPE*), ou   
**Atualizações - Cadastros Gerais - Funcionário** (*SIGAMDT*).  
  
Após esta verificação certifique-se que no cadastro do **Ambiente Físico** rotina (*MDTA165*), tem o relacionamento do Centro de Custo do Funcionário. Caso não tenha inclua e salve o cadastro, conforme exemplo a seguir:  
  
![R52UZzBXgS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4473928208535)

Para mais informações sobre as entidades relacionadas ao ambiente físico acesse a documentação  
[RH - Linha Protheus - MDT - eSocial - S-2240 - Novas Entidades de Relacionamento ao Ambiente Físico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409384342679-RH-Linha-Protheus-MDT-eSocial-S-2240-Novas-Entidades-de-Relacionamento-ao-Ambiente-F%C3%ADsico)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
