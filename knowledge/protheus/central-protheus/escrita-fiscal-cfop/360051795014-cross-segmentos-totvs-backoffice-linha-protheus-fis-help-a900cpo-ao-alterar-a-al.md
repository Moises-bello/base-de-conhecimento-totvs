---
article_id: 360051795014
category: Escrita Fiscal - CFOP
content_hash: 75be7e7ab23b81921266616ccf3161ca9c255facee9a3afe281be755c8d1a0cb
fetched_at: '2026-06-28T22:39:35.918642+00:00'
product: protheus
section_id: 1500001538541
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Help "A900CPO" ao
  alterar a alíquota do ICMS na rotina de acertos fiscais MATA900
type: support-article
updated_at: '2021-07-01T13:25:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051795014-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Help-A900CPO-ao-alterar-a-al%C3%ADquota-do-ICMS-na-rotina-de-acertos-fiscais-MATA900
---

**Dúvida**Help "A900CPO" ao alterar a alíquota do ICMS na rotina de acertos fiscais MATA900  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12  
  
**Solução**Excluir Nota e fazer novo lançamento;

Alguns campos como Série, CFOP, Aliq. ICMS, o sistema não permite a alteração pois a nota precisa ter vínculo com a origem em outras tabelas, sendo elas (SFT/SD2/SF2/SD1/SF1). Por este motivo a rotina recomenda que o lançamentos sejam excluídos e refeitos de forma correta para que não tenhamos reflexos em outras rotinas, como por exemplo, relatório, arquivos magnéticos e outras obrigações acessórias.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083699513/mceclip0.png)

**Para maiores informações;**

Verificando no fonte, existe uma validação de bloqueio para que não possa ser possível alterar o campo.  
Onde no casos de vocês é campo Aliq. ICMS.

Portanto, em acertos fiscais é possível ajustar determinados campos porém outros não.  
  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027494872-MP-FIS-Acertos-Fiscais>
