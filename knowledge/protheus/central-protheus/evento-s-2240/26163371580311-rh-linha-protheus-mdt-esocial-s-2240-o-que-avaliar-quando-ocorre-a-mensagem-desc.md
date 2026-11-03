---
article_id: 26163371580311
category: Evento S-2240
content_hash: cd06c12e527bb1f6f2be9e20e31a5dc404d496e670ff20d5c4d00e56f95d75b8
fetched_at: '2026-06-28T22:45:23.479615+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - S-2240 - O que avaliar quando ocorre
  a mensagem "Descrição das atividades realizadas: em branco" com o parâmetro MV_NG2TDES=
  1 Tarefa'
type: support-article
updated_at: '2024-09-05T18:00:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26163371580311-RH-Linha-Protheus-MDT-eSocial-S-2240-O-que-avaliar-quando-ocorre-a-mensagem-Descri%C3%A7%C3%A3o-das-atividades-realizadas-em-branco-com-o-par%C3%A2metro-MV-NG2TDES-1-Tarefa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26163371558935) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O que avaliar quando ocorre a mensagem "Descrição das atividades realizadas: em branco" com o parâmetro MV\_NG2TDES= 1 Tarefa?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Quando a descrição das atividades esta configurada via parâmetro para ser a descrição da tarefa, então quando o risco é criado com data anterior a tarefa, a data do evento é a data do risco quando o funcionário ainda não começou a tarefa, portanto, não pode ser buscada a descrição da tarefa, no caso o funcionário não possui nenhuma outra tarefa na data do evento.  
Neste cenário, é possível alterar o parâmetro MV\_NG2TDES= 3 para buscar a descrição da função.  
  
No módulo SIGACFG (Configurador), acesse o menu Ambiente > Cadastros > Parâmetros, busque pelo parâmetro MV\_NG2TDES e efetue a alteração conforme necessidade.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26165676864407)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
