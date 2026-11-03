---
article_id: 6504175290263
category: MDT - Atendimento Médico
content_hash: b7883dc264653049889476216863b55e786db19b4c034539639fe7ae31d80051
fetched_at: '2026-06-28T22:44:20.505142+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Ao alterar o cadastro de funcionários no módulo
  SIGAMDT ocorre mensagem Usuário sem acesso aos campos necessários ao eSocial
type: support-article
updated_at: '2025-07-25T20:08:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6504175290263-RH-Linha-Protheus-MDT-Ao-alterar-o-cadastro-de-funcion%C3%A1rios-no-m%C3%B3dulo-SIGAMDT-ocorre-mensagem-Usu%C3%A1rio-sem-acesso-aos-campos-necess%C3%A1rios-ao-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25287442453655)**Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Ao alterar cadastro de funcionários no módulo SIGAMDT ocorre mensagem "Usuário sem acesso aos campos necessários ao eSocial, não será possível incluir e alterar funcionários. Contate o administrador do Sistema".  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**A rotina de **Cadastro de Funcionário (GPEA010)**pode ser acionada através do menu do módulo de **Medicina e Segurança do Trabalho (SIGAMDT)**, contudo as regras aplicadas a essa rotina são definidas pelo produto de **Gestão Pessoal (SIGAGPE).**

A Mensagem de atenção: **Usuário sem acesso aos campos necessários ao eSocial, não será possível incluir e alterar funcionários. Contate o administrador do Sistema.** é disparada por conta de uma regra do módulo Gestão Pessoal, que valida caso o usuário não tenha acesso ao campo ou o campo não esteja disponível para o módulo.

A orientação é utilizar o cadastro através do módulo de Gestão Pessoal (SIGAGPE).  
  
**Saiba Mais**[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico?page=1#articles)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
