---
article_id: 1500012467782
category: Escrita Fiscal - Impostos - ICMS
content_hash: bdd1ff517c906207749cea83ecb3ba78f6b42ef3979e70de8517303a7a5d7fea
fetched_at: '2026-06-28T22:39:26.048491+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: MP - FIS - Gravação dos Valores dos Impostos FUST e FUNTTEL Na Apuração do
  ICMS - MATA953
type: support-article
updated_at: '2021-05-28T21:17:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012467782-MP-FIS-Grava%C3%A7%C3%A3o-dos-Valores-dos-Impostos-FUST-e-FUNTTEL-Na-Apura%C3%A7%C3%A3o-do-ICMS-MATA953
---

**Dúvida**  
Em qual tabela e campo são gravados os valores referente os impostos FUST e FUNTTEL?  
  
**Ambiente**  
Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**

Os valores dos impostos FUST e FUNTTEL são gravados na tabela CDH - Apuração de ICMS no campo Valor Ajuste (CDH\_VALOR).  
  
Ao gerar a apuração do ICMS (MATA953) são apresentados os valores dos impostos FUST e FUNTTEL em tela na Aba "Informações Complementares" nas linhas 033 (FUST) e 034 (FUNTTEL) e, somente são gravados no campo Valor Ajuste (CDH\_VALOR), após confirmar a apuração do ICMS.  
  
Conforme documentação abaixo, o sistema calcula as contribuições no momento da apuração, efetuando o lançamento na coluna Outros Débitos e na pasta Informações Complementares."

<https://tdn.totvs.com/display/public/PROT/FUST+e+FUNTTEL+-+MP11+--+116983>
