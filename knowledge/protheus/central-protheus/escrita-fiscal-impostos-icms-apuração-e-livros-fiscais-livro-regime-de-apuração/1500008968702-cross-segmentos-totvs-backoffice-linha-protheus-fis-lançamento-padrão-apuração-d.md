---
article_id: 1500008968702
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 12791b8a622081844ca28d3b863c94e4f21dcfee0643585cb8377c204f6721f5
fetched_at: '2026-06-28T22:39:22.187882+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS Lançamento  Padrão
  Apuração de ICMS
type: support-article
updated_at: '2021-07-15T17:51:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008968702-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Lan%C3%A7amento-Padr%C3%A3o-Apura%C3%A7%C3%A3o-de-ICMS
---

**Dúvida**Qual lançamento padrão utilizar para Apuração de ICMS?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para geração correta Contabilização da Apuração de ICMS será necessário utilizar os lançamentos padronizados 710 e 711. Sistema buscará as informações da tabela SE2

O Lançamento Padrão para Apuração de ICMS busca da Tabela SE2, o Saldo Devedor,

LP 712, busca informações da 5ª aba da Apuração de ICMS ( Apuração-ICMS)

Linhas: 004 e 010

VALOR := aCols5[ Ascan(aCols5,{|x|x[1]=="004"}) ,04]  
VALOR2 := aCols5[ Ascan(aCols5,{|x|x[1]=="010"}) ,04]

Não existe lançamento Padrão para buscar as informações da CDH
