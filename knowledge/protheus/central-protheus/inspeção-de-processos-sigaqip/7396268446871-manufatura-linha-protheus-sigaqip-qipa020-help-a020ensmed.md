---
article_id: 7396268446871
category: Inspeção de Processos (SIGAQIP)
content_hash: 9422049158ec3567b2b70178135a2b241579281c8c8acf8730d65d03afd9670e
fetched_at: '2026-06-28T22:42:25.918479+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - QIPA020 - Help A020ENSMED
type: support-article
updated_at: '2024-04-24T20:09:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7396268446871-Manufatura-Linha-Protheus-SIGAQIP-QIPA020-Help-A020ENSMED
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo **SIGAQIP - Inspeção de Processos**, ao tentar alterar um determinado ensaio na rotina **QIPA020 - Ensaios** é exibido o *help* **A020ENSMED - Ensaio apresenta medições cadastradas**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**Este *help* é exibido quando o ensaio que está sendo alterado já está sendo utilizado por uma especificação de produto.  
  
**Solução**Verifique por meio da rotina **QIPA010 - Especificação do Produto**, qual especificação está utilizando o ensaio em questão. Somente é permitido alterar um ensaio quando este ensaio não esteja sendo utilizado por nenhuma especificação de produto.  
Também é possível realizar esta verificação via **APSDU**, consultando as tabelas **QP7 - Ensaios Mensuráveis Produtos** e **QP8 - Ensaios Textos dos Produtos**, validando os campos **QP7\_ENSAIO - Ensaio** e **QP8\_ENSAIO - Ensaio**.
