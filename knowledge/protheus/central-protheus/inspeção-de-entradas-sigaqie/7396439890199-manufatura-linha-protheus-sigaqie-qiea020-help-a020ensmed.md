---
article_id: 7396439890199
category: Inspeção de Entradas (SIGAQIE)
content_hash: 3b300af296b86456689403e3c182641dbd5f1d705fe86698db47ced19776bd06
fetched_at: '2026-06-28T22:42:27.141375+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - QIEA020 - Help A020ENSMED
type: support-article
updated_at: '2022-07-12T19:38:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7396439890199-Manufatura-Linha-Protheus-SIGAQIE-QIEA020-Help-A020ENSMED
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo **SIGAQIE - Inspeção de Entradas**, ao tentar alterar um determinado ensaio na rotina **QIEA020 - Ensaios** é exibido o *help* **A020ENSMED - Ensaio apresenta medições cadastradas**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**Este *help* é exibido quando o ensaio que está sendo alterado já está sendo utilizado por uma especificação de produto.  
  
**Solução**Verifique por meio da rotina **QIEA010 - Especificação do Produto**, qual especificação está utilizando o ensaio em questão. Somente é permitido alterar um ensaio quando este ensaio não esteja sendo utilizado por nenhuma especificação de produto.  
Também é possível realizar esta verificação via **APSDU**, consultando as tabelas **QE7 - Ensaios Mensuráveis Produtos** e **QE8 - Ensaios Textos dos Produtos**, validando os campos **QE7\_ENSAIO - Código do Ensaio** e **QE8\_ENSAIO - Código do Ensaio**.
