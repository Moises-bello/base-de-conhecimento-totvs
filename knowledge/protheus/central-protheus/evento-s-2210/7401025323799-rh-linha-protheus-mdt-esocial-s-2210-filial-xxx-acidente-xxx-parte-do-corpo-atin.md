---
article_id: 7401025323799
category: Evento S-2210
content_hash: 1133b559f4634d71d9307293234c17280224955dc4bde86074f0b9a950580f77
fetched_at: '2026-06-28T22:45:24.474491+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - S-2210 - Filial: XXX / Acidente: XXX
  / Parte do Corpo Atingida deve ser um código válido e existente na tabela 13 do
  eSocial'
type: support-article
updated_at: '2025-03-03T18:14:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7401025323799-RH-Linha-Protheus-MDT-eSocial-S-2210-Filial-XXX-Acidente-XXX-Parte-do-Corpo-Atingida-deve-ser-um-c%C3%B3digo-v%C3%A1lido-e-existente-na-tabela-13-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372776850839) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Relatório de inconsistência na geração do evento S-2210: Filial: XXX / Acidente: XXX / Parte do Corpo Atingida deve ser um código válido e existente na tabela 13 do eSocial, o que conferir?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**A parte do corpo atingida (TYF\_LATERA) deve ser um código válido e existente na tabela 13 do eSocial, que faz referência à tabela "C8I" do SIGATAF.  
  
No módulo SIGAMDT (Medicina e Segurança do Trabalho), acesse o menu Atualizações - Acidente Trabalho - Acidentes (MDTA640), localize o acidente e na aba "Parte Corpo Atingida", verifique se o campo **Lateralidade** (TYF\_LATERA) esta preenchido de acordo com as tabelas 13 do layout eSocial.   
  
Se as informações estiverem em desacordo com o layout eSocial, é necessário atualizar o Ambiente com o pacote Acumulado MDT e Acumulado TAF e executar autocontidas, veja documentação:   
[Atualização das tabelas autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034479973-TAF-CONFIGURA%C3%87%C3%83O-Atualiza%C3%A7%C3%A3o-das-tabelas-autocontidas)  
[Como fazer o download do pacote Acumulado MDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773-RH-Linha-Protheus-MDT-Como-fazer-o-download-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-para-atualizar-o-modulo-medicina-e-seguran%C3%A7a-do-trabalho)  
[Acumulado TAF](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/TAF_EXPEDICAO_CONTINUA.ZIP)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7400952700311)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
