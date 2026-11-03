---
article_id: 360057161673
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 9c8e211642c782a0d8dbfd6c28f71735b3942d0ded1f7e3f7e6492a377395f15
fetched_at: '2026-06-28T22:42:10.736243+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIEF-PA - Anexo
  III - Errado - Não existe esse código de Receita na base de dados
type: support-article
updated_at: '2022-08-17T20:18:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057161673-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIEF-PA-Anexo-III-Errado-N%C3%A3o-existe-esse-c%C3%B3digo-de-Receita-na-base-de-dados
---

**Dúvida**Ao importar o arquivo da DIEF PA é apresentando o erro abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/hOiWKRPjdaeroTuA5mLOISjqF/?name=inline-208341973.png)  
  
Anexo III - Errado

Não existe esse código de Receita na base de dados

**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**O código de receita gravado no Anexo III é obtido através do campo Cod. Receita (F6\_CODREC) gravado na rotina da Guia Nacional de Recolhimento (MATA960).

Para correção do erro acima referente o código de receita, será necessário acessar a rotina da Guia Nacional de Recolhimento (MATA960) correspondente ao erro apresentando no anexo III e verificar se foi preenchido o código de receita no campo Cod. Receita (F6\_CODREC), caso esteja preenchido, verificar se o código é valido e aceito pela DIEF PA.
