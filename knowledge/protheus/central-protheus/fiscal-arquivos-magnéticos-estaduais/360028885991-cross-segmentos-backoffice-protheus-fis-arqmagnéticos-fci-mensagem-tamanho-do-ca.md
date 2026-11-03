---
article_id: 360028885991
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 280b87ee60af6790c1af5d7d07f722ff80e14a1412108486142b5a3f3e0a19d2
fetched_at: '2026-06-28T22:42:10.876709+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - FCI - Mensagem
  tamanho do campo conteúdo importação
type: support-article
updated_at: '2022-08-17T20:30:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028885991-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-FCI-Mensagem-tamanho-do-campo-conte%C3%BAdo-importa%C3%A7%C3%A3o
---

**Ocorrência**Ao executar a apuração do FCI, aparece uma mensagem dizendo que o campo CFD\_CONIMP é maior que o permitido pelo layout.

![image.png](https://mail.google.com/mail/u/1?ui=2&ik=23df2e4086&attid=0.1&permmsgid=msg-a:r-9151119396813087852&th=1697206b9a6fd5f7&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ_SSqIi15aEzyCGrpkl3mSFXi8tlPRIysLvPxD9efcK8n2aJ7ja0Np74KHHcBZGTAWxwDOpY4iNiEzyiurdv8LVw_MMzmCLF4QKaph4I6wzXB_nvBNxlIDdGkM&disp=emb&realattid=ii_jt5skdp60)

**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**Este erro acontece porque o conteúdo gravado no campo CFD\_CONIMP é maior que o permitido pelo layout.

**Solução**

O CFD\_CONIMP é preenchido com o resultado do seguinte cálculo:

CFD\_CONIMP= (CFD\_VPARIM/CFD\_VSAIIE) \* 100

No exemplo acima:

CFD\_VPARIM = 114.86

CFD\_VSAIIE = 6.79

Logo:

CFD\_CONIMP = (114.86 / 6.79) \* 100

CFD\_CONIMP =1691.61 -> Este conteúdo é maior que o tamanho do campo.

O Campo CFD\_CONIMP é um percentual e portanto NÃO pode ultrapassar 100

Para correção do erro,  é preciso avaliar qual valor está errado:

- Se o CFD\_VPARIM está mais alto do que deveria, então deverá ser avaliado as produções e as compras de matérias primas deste produto para chegar ao valor correto

- Se o CFD\_VSAIIE está menor do que deveria, então deverá ser avaliado o documento de saída se está com o valor correto.
