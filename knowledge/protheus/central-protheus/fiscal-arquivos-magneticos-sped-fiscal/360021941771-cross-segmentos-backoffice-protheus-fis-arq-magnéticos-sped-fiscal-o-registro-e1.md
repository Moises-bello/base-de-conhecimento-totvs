---
article_id: 360021941771
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 5470762e5c6273f7405c37b4280496c9c578f72c8350b4017816ebe471cfa338
fetched_at: '2026-06-28T22:42:02.363849+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - O registro E111 do Sped Fiscal não está sendo gerado.
type: support-article
updated_at: '2025-02-11T21:24:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021941771-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-O-registro-E111-do-Sped-Fiscal-n%C3%A3o-est%C3%A1-sendo-gerado
---

**Ocorrência**O registro E111 do Sped Fiscal não está sendo gerado.  
   
 **Ambiente**Microsiga Protheus - Livros fiscais - A partir da versão 11.80.

**Solução**1. Verifique se já foi importada a tabela de AJUSTES - tabela CDO preenchida;

2. Verifique se o parâmetro MV\_USASPED está como T (se estiver como F não é possível inserir código de lançamento no momento da apuração);

3. Gere a apuração de ICMS com os parâmetros da seguinte maneira:

 Livro = \*  
Apuração = Mensal  
Período = 1º

 Feito a apuração com os códigos de lançamento, verifique se os dados foram salvos na tabela CDH, pois os dados do SPED são informados a partir desta tabela.
