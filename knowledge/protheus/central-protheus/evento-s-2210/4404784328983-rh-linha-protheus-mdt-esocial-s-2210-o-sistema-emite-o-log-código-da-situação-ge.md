---
article_id: 4404784328983
category: Evento S-2210
content_hash: ad1ad159bfdd5f1ce8b81d03b8578bf5130d6f0c4af59c1509898924ca8e9645
fetched_at: '2026-06-28T22:45:24.421732+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - S-2210 - O sistema emite o log "Código
  da Situação Geradora: Em branco" ao tentar gerar a CAT com o evento S-2210 (Comunicação
  de Acidentes de Trabalho)'
type: support-article
updated_at: '2025-03-03T18:00:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404784328983-RH-Linha-Protheus-MDT-eSocial-S-2210-O-sistema-emite-o-log-C%C3%B3digo-da-Situa%C3%A7%C3%A3o-Geradora-Em-branco-ao-tentar-gerar-a-CAT-com-o-evento-S-2210-Comunica%C3%A7%C3%A3o-de-Acidentes-de-Trabalho
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372186949271)**Tempo aproximado para leitura: **00:02:00 min****Ocorrência**O sistema emite o log "**Código da Situação Geradora: Em branco**" ao tentar gerar a CAT com o evento S-2210 (Comunicação de Acidentes de Trabalho).  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Isso ocorre quando o sistema está fazendo integração com o eSocial para geração do evento S-2210 (Acidente de Trabalho) e o motivo eSocial da situação geradora não foi cadastrado.  
  
**Solução**1. Acesse no modulo SIGAMDT o caminho: **atualizações > Acidente Trabalho > Tipos de Acidentes** (MDTA600). Nessa rotina é necessario que esteja cadastrado o tipo de acidente com os campos **Cod. eSocial** (TNG\_ESOC) e **Cod. eSoc. 1** (TNG\_ESOC1) preenchidos.  
  
![2021-07-22_14-04-55.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4404784242839)  
  
2. Após preencher esses campos ao cadastrar a CAT no caminho: **atualizações > Acidente Trabalho > Acidentes** (MDTA640), preencha o campo Tipo Acid. (TNC\_TIPACI).  
  
![2021-07-22_14-06-49.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4404784225431)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
