---
article_id: 17521386007831
category: Evento S-2220
content_hash: f9434a1b4b7571be70fa4bf7943dbfc22d6db05546816b0f85ba84f89c7ad8f7
fetched_at: '2026-06-28T22:45:25.466536+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2220 - Ao gerar o ASO o nome não é
  impresso O que avaliar quando o ASO é impresso sem o nome do funcionário/candidato
type: support-article
updated_at: '2025-03-03T18:22:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17521386007831-RH-Linha-Protheus-MDT-eSocial-S-2220-Ao-gerar-o-ASO-o-nome-n%C3%A3o-%C3%A9-impresso-O-que-avaliar-quando-o-ASO-%C3%A9-impresso-sem-o-nome-do-funcion%C3%A1rio-candidato
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17521409466903)**Tempo aproximado para leitura: **03:00:00 min** **Dúvida**Ao gerar o ASO o nome do funcionário/candidato não esta saindo: "O que avaliar quando o ASO é impresso sem o nome do funcionário/candidato"?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**A geração do ASO tem por base o numero da ficha médica do funcionário/candidato, as informações da FICHA MÉDICA ficam na tabela TM0 que por padrão tem o modo de acesso E E E totalmente exclusiva, será preciso validar o campo TM0\_NOMFIC que precisa esta com tamanho = 40 e contexto Real; deste campo que vem o nome na geração do ASO.

**No configurador Acesse: Base de dados>Dicionário>base de dados>abra a TM0 e busque o campo TM0\_NUMFIC**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17521198024727)

Para acessar a rotina no SIGAMDT**>Atualizações>Atendimento Medico>Atestado Aso**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17521304740631)

**Aso impresso:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17521330627479)  
  
Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20)  
[ChatBot Carol](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
