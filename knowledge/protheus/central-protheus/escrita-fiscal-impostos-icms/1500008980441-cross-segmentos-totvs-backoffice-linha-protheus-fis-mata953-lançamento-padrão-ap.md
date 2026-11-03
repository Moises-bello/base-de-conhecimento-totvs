---
article_id: 1500008980441
category: Escrita Fiscal - Impostos - ICMS
content_hash: 420299606fba33d3239b1b35f4a4210c1ae5d2070eac53e42d28f5dc650525a2
fetched_at: '2026-06-28T22:39:25.973919+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- MATA953/ Lançamento
  padrão apuração de ICMS
type: support-article
updated_at: '2021-07-20T12:53:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008980441-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-MATA953-Lan%C3%A7amento-padr%C3%A3o-apura%C3%A7%C3%A3o-de-ICMS
---

**Dúvida**Qual lançamento padrão utilizar pela Apuração de ICMS?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIS - Todas as versões  
  
**Solução**

Para geração correta Contabilização da Apuração de ICMS será necessário utilizar os lançamentos padronizados 710 e 711. Sistema buscará as informações da tabela SE2

O Lançamento Padrão para Apuração de ICMS busca da Tabela SE2, o Saldo Devedor,

LP 712, busca informações da 5ª aba da Apuração de ICMS ( Apuração-ICMS)

Linhas: 004 e 010

VALOR := aCols5[ Ascan(aCols5,{|x|x[1]=="004"}) ,04]  
VALOR2 := aCols5[ Ascan(aCols5,{|x|x[1]=="010"}) ,04]

Não existe lançamento Padrão para buscar as informações da CDH
