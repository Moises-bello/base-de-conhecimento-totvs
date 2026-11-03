---
article_id: 360026414351
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 39a82185edef8e704472abb7c04318f54f4a02ba86a2c06d957e52ad6c1cd6b5
fetched_at: '2026-06-28T22:39:22.216188+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Nota fiscal de serviços
  constando na apuração do ICMS
type: support-article
updated_at: '2025-02-11T18:25:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026414351-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nota-fiscal-de-servi%C3%A7os-constando-na-apura%C3%A7%C3%A3o-do-ICMS
---

**Dúvida**

Nota fiscal de serviços constando na apuração do ICMS  
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

O sistema valida o campo **F3\_TIPO = S** para identificar que a nota fiscal é de serviço, sendo necessário o preenchimento dos campos **Cód. Serv. ISS** (**B1\_CODISS)**e **L. Fiscal ISS(F4\_LFISS) = diferente de "Não"**.  
  
Outro detalhe a ser observado é o campo **"L Fiscal ICMS(F4\_LFICM)"**, em notas de serviços esse campo deverá ser "**Não**"  
  
Após conferencia dos campos acima, caso seja necessário alguma alteração, após as mesmas, deve-se executar a rotina de reprocessamento para que o livro fiscal possa ser recriado de maneira correta. Com essas configurações as notas de serviços não serão levadas para a apuração de ICMS.
