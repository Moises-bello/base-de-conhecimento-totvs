---
article_id: 360019925672
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: ae33421ef61f9af99b94f289efa5edaef99050c56d6268354e504205cf870fc2
fetched_at: '2026-06-28T22:40:32.451385+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 Lançamento contábil
  Automático não exibe todas as colunas no browse
type: support-article
updated_at: '2022-09-28T14:51:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019925672-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Lan%C3%A7amento-cont%C3%A1bil-Autom%C3%A1tico-n%C3%A3o-exibe-todas-as-colunas-no-browse
---

**Dúvida**No browse da rotina ctba102 não exibe todas as colunas da tabela.   
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
  
**Solução**

1 - Na rotina Lançamento Contábil Automático (CTBA102) no parâmetro F12 tem a pergunta: **Modo Exibição?**

A pergunta define o modo de exibição dos registros na tela inicial da rotina.

Opção 1 : Cabeçalho Lançamento Contábil. Serão exibidos os registros dos documentos com base na tabela de Saldos Contábeis por Documento.   
Opção 2 : Detalhe Lançamento Contábil. Serão exibidos os registros dos documentos com base na tabela de Lançamentos Contábeis.

2 - No módulo SIGACFG em base de dados, dicionário de dados, ao acessar a tabela de lançamentos, posicionando no campo desejado ao editar, existe a opção ao acessar a aba USO da flag BROWSE ao desmarcar, não aparecerá a coluna na tela também.
