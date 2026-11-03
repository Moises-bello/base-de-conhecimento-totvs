---
article_id: 360016285091
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 7df97c9a0093c6ca623639f1d0459b067a18f6990ea81e6ccb466aa6d91aeb68
fetched_at: '2026-06-28T22:42:05.189014+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Error log: invalid field name in Alias SCGN000013->CF4_BASPIS on PRINTSFT(FISR101.PRW)'
type: support-article
updated_at: '2023-01-04T17:23:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016285091-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Error-log-invalid-field-name-in-Alias-SCGN000013-CF4-BASPIS-on-PRINTSFT-FISR101-PRW
---

**Ocorrência**Na **apuração da EFD Contribuições**, ao tentar gerar o **Relatório de Conferência** (FISR101) é apresentado o error log abaixo:

"invalid field name in Alias SCGN000013->CF4\_BASPIS on PRINTSFT(FISR101.PRW)"  
   
 **Ambiente**Microsiga Protheus – Livros fiscais – A partir da versão 11.80.

**Causa**Este incidente ocorre na rotina **Relatório de Conferência da Apuração**(FISR101) para notas fiscais que possuem Devolução dentro do período de emissão onde quando processada a Apuração (FISA001) o sistema grava as informações na tabela CF4.

O error log é apresentado quando o relatório FISR101 é gerado com a pergunta:

* Movto. Reducao Base de Cálculo:= Sim // Indica se as movimentações que reduziram base de cálculo no período serão demonstradas no relatório.

**Solução**  
 1. Para solucionar essa ocorrência, aplique o pacote de correção abaixo:  
12.1.16: <https://suporte.totvs.com/portal/p/10098/download?e=688396> ;  
12.1.17: <https://suporte.totvs.com/portal/p/10098/download?e=688398> ;
