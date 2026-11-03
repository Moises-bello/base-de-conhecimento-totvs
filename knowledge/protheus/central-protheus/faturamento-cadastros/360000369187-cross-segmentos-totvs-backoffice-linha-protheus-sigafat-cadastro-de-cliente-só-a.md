---
article_id: 360000369187
category: Faturamento - Cadastros
content_hash: dbedfe539af694294c6735da98d7ce0db7c5e660070ba433733295800f6b7def
fetched_at: '2026-06-28T22:38:36.850414+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Cadastro de
  cliente só apresenta a aba Outros
type: support-article
updated_at: '2021-11-17T12:36:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000369187-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Cadastro-de-cliente-s%C3%B3-apresenta-a-aba-Outros
---

**Ocorrência**

A tela de cadastro de clientes, no módulo faturamento perdeu as abas e os campos estão todos em uma mesma aba "outros", conforme abaixo:

![](/attachments/token/mJT2A3uLMvwecpWXU4EFhOlmn/?name=inline-793685825.png)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da versão 12.1.17.  
  
**Causa**A problema foi causado na migração da versão 11 para a 12, onde o layout existente na tabela **SXA** da tabela SA1 não foi reconhecido pelo sistema.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realize a atualização do Dicionário de Dados mais recente disponível no Portal do Cliente;  
2. Execute o UPDDISTR: [**Atualizador de Dicionário de Dados (UPDDISTR)**](https://tdn.totvs.com/x/nJLYCg)

Observação: O processo em questão deve ser realizado por um analista que detenha conhecimentos técnicos da estrutura Protheus, em ambiente de homologação, caso não detenha o conhecimento, o ideal é que um analista in loco efetue o processo. Em caso de dúvidas quanto ao procedimento, entre em contato com a equipe de FrameWork.
