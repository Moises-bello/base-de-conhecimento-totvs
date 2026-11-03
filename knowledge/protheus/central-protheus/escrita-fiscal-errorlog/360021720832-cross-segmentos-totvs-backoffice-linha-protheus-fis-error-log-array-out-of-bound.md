---
article_id: 360021720832
category: Escrita Fiscal - Error.log
content_hash: ebb47ac7976d199b680e32a24efb48b8fda7dfe72486a65bed07e085bafe5e0a
fetched_at: '2026-06-28T22:39:32.833139+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Error log array out
  of bounds ( 1 of 0 )  on A953APURA(MATA953.PRX)
type: support-article
updated_at: '2021-07-08T13:02:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021720832-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Error-log-array-out-of-bounds-1-of-0-on-A953APURA-MATA953-PRX
---

**Dúvida**Ao gerar apuração de ICMS (MATA953) está ocorrendo os seguintes error logs.

array out of bounds ( 1 of 0 ) on A953APURA(MATA953.PRX) 16/11/2018 08:03:11 line : 8295

array out of bounds ( 1 of 0 ) on A953APURA(MATA953.PRX) 10/10/2018 18:03:01 line : 8278

**Ambiente**Protheus – Livros Fiscais– A partir da versão 12.1.17  
  
  
**Solução**

O error log ocorre devido a Estrutura errada da Tabela CCF ou campo criado incorretamente.

Para ajuste siga o processo descrito abaixo para solução deste incidente.

1. É importante que o processo seja executado primeiramente em ambiente homologação (teste);  
  
2. Baixar dicionario, esse é o dicionário da versão 12.1.17. (em anexo);  
  
3. Descompactar arquivo e extrair sdfbra e sx2.unq na pasta systemload;  
  
4. Rode UPDDISTR na base de homologação;  
  
5. Realize teste;

Caso não possa executar o procedimento do Upddistr no ambiente de produção, compare os dados da tabela CCF, nas tabelas, SX2, SX3 e SIX.

Todos os passos acima, devem ser executados por um profissional capacitado no ambiente Protheus com conhecimentos em sua estrutura.

\* Dicionario de dados 12.1.17; <https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/360026438171/19-04-09-BRA_DICIONARIO_FISCAL_MANUTENCAO__1_.ZIP>

\* Dicionario de dados 12.1.23; <https://suporte.totvs.com/portal/p/10098/download#detail/737186>
