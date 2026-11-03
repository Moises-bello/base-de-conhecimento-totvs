---
article_id: 4412596290455
category: MDT - Atendimento Médico
content_hash: 4cc8deda3dc3c5f716e99350855420397f402ead9c9ad4ff85faf72100acb2b6
fetched_at: '2026-06-28T22:44:20.513834+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Ao gravar o atestado médico Erro campo Valor atribuído
  diferente do tamanho do campo Nome
type: support-article
updated_at: '2025-03-03T17:04:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412596290455-RH-Linha-Protheus-MDT-Ao-gravar-o-atestado-m%C3%A9dico-Erro-campo-Valor-atribu%C3%ADdo-diferente-do-tamanho-do-campo-Nome
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19250934230679)**Tempo aproximado para leitura: **00:02:00 min****Ocorrência**  
Ao gravar o atestado médico Erro campo Valor atribuído diferente do tamanho do campo (Nome), o que avaliar?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Causa**Esse erro ocorre quando o tamanho do campo (TNY\_NOMUSU) está diferente do tamanho do campo (TNP\_NOME).  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesso o modulo Configurador (SIGACFG) no caminho: Base de Dados > Base de Dados, busque pela tabelas TNY e TNP e verifique o tamanho do campo (TNY\_NOMUSU) e (TNP\_NOME) .  
  
2. Para ajustar esse erro é necessário deixar o tamanho de ambos campos com 80.   
  
**Observação**Em caso de dúvidas em como fazer a alteração do tamanho de campos entre em contato com o suporte do Framework;  
Recomendamos que efetue o backup da base antes de qualquer modificação.  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/9198712823575-Assistente-Virtual-Carolina)
