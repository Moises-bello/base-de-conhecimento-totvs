---
article_id: 360013051051
category: Materiais - Compras (SIGACOM)
content_hash: ff9fb82bff4cfae5bec1c9ffd0c7eead3c69fc1b98d1caf9a8cdd6e31d5c9241
fetched_at: '2026-06-28T22:41:10.118670+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ocorrência do Erro
  Cannot insert duplicate key row in object 'dbo.FJV010' with unique index 'FJV010_UNQ'
  no Documento de Entrada MATA103
type: support-article
updated_at: '2022-05-13T11:42:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013051051-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ocorr%C3%AAncia-do-Erro-Cannot-insert-duplicate-key-row-in-object-dbo-FJV010-with-unique-index-FJV010-UNQ-no-Documento-de-Entrada-MATA103
---

**Dúvida**

O que fazer quando mostrar error.log referente a duplicidade na rotina FJV no nota de entrada ou mesmo na inclusão de títulos no financeiro?

" DB error (Insert): -37 File: FJV010 - Error : 2601 (23000) (RC=-1) - [Microsoft][ODBC SQL Server Driver][SQL Server]Cannot insert duplicate key row in object 'dbo.FJV010' with unique index 'FJV010\_UNQ'. The duplicate key value is (01, 000000000003, 0). ( From tISAMFile::Write "

**Ambiente**Protheus – Compras e Financeiro – A partir da versão 12.17  
  
**Solução**

Acesse ao ambiente Configurador (SIGACFG)

Localize as tabelas (FIV, FJV e FIW)

Valide o modo de compartilhamento dessas tabelas.

Todas devem possuir o mesmo modo de compartilhamento (Exclusivas ou Compartilhadas)

Estas tabelas no padrão, devem obrigatoriamente possuir o mesmo nível de compartilhamento.

**Antes de ajustar o compartilhamento de Tabelas supra citadas, avalie:**

Compartilhamento das tabelas de movimentações do Financeiro (SE1, SE2 e SE5) ,

O compartilhamento das tabelas (FIV, FJV e FIW) deverão acompanhar o compartilhamento das tabelas de Movimentação.

Caso o erro ocorra apenas na inclusão titulo pelo financeiro e os ajustes acima não resolver poderá entrar em contato com a equipe de financeiro.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
