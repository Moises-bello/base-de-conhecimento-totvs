---
article_id: 16242020095127
category: Evento S-2220
content_hash: 663dfdbbd2d7c785bef721648ebdeee49fac6d8ef75c304674ebf3a8a384e05e
fetched_at: '2026-06-28T22:45:25.539391+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2220 - O que avaliar quando apresentar
  a mensagem Erro na validação do campo dtAso
type: support-article
updated_at: '2024-08-13T14:07:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16242020095127-RH-Linha-Protheus-MDT-eSocial-S-2220-O-que-avaliar-quando-apresentar-a-mensagem-Erro-na-valida%C3%A7%C3%A3o-do-campo-dtAso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16242059647895) Tempo aproximado para leitura: **00:02:00min** **Dúvida**O que avaliar quando apresentar a mensagem Erro na validação do campo "dtAso" ?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**A Data de emissão do ASO deve ser uma data válida, igual ou anterior à data atual e igual ou posterior à data de início da obrigatoriedade deste evento para o empregador no eSocial.  
  
**Obs.:** A data de emissão pode ficar em branco e será preenchido de acordo com a data base do sistema ao efetuar a impressão do ASO.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25579565833879)  
  
Importante avaliar os campos:  
- A data de emissão do ASO (**TMY\_DTEMIS**), no módulo Medicina e a Data Base (**C8B\_DTASO**) no Módulo TAF.  
- Natureza do ASO.  
- Data de admissão do funcionário, é a data de obrigatoriedade de transmissão dos eventos SST, conteúdo informado através do parâmetro **MV\_NG2DTES**.

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
