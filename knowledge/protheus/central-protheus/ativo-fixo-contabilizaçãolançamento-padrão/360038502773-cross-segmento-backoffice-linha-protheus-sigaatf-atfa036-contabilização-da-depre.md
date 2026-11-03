---
article_id: 360038502773
category: Ativo Fixo - Contabilização/Lançamento padrão
content_hash: 774396b1f5a4d5d0dd3e295b694c2b522fc51d8ca5b40b30e4dc10cf92c9ab23
fetched_at: '2026-06-28T22:41:42.344419+00:00'
product: protheus
section_id: 1500001536421
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAATF -  ATFA036 - Contabilização  da
  depreciação na baixa ONLINE e OFF-LINE com LP810 e LP820
type: support-article
updated_at: '2026-04-02T17:19:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038502773-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-Contabiliza%C3%A7%C3%A3o-da-deprecia%C3%A7%C3%A3o-na-baixa-ONLINE-e-OFF-LINE-com-LP810-e-LP820
---

O LP 810 contabiliza operações na baixa do bem, incluindo depreciação, sendo necessário criar uma sequência para contabilização online da depreciação. O LP 820 é usado no cálculo da depreciação, mas só pode ser usado na baixa offline via rotina CTBAATF. O processo é customizável, com diretrizes distintas para uso online e offline, e a TOTVS não oferece suporte para expressões customizadas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39478115724695) **Tempo aproximado para leitura: 00:04:00 min**  
  
**Dúvida**  
Na baixa do ativo com depreciação, não ocorre a contabilização da depreciação.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - A partir da versão 12.

**Solução**  
**O LP 810** – É destinado a contabilizar as operações ocorridas na baixa do bem (inclusive sua depreciação). Pois a contabilização da baixa se comporta de maneira distinta em relação às tabelas Saldos e Valores (SN3) e Movimentos dos bens (SN4).

Para geração da contabilização da depreciação de forma online, é necessário criar uma sequência do LP 810 para contabilização da depreciação, posicionando-a no movimento de depreciação.

**O LP 820** – É utilizado pela rotina de cálculo da depreciação (ATFA050), não sendo possível utilizá-lo no processo de contabilização online da baixa. É possível utilizar o LP 820 para contabilização de depreciação da baixa apenas na contabilização offline, por meio da rotina Contabilizações Offline CTBAATF, pois a rotina aciona os dois LPs.  
   
As expressões recomendadas para esse processo estão disponíveis no documento oficial:   
[Guia TOTVS - Lançamento Padrão 810](https://tdn.totvs.com/pages/releaseview.action?pageId=390399164)  
**Importante****:** O LP possui diretrizes distintas para uso **ONLINE e OFFLINE**, conforme descrito na documentação.  
   
Para totalizar o lançamento com o valor da baixa, utilize:

* **Processo Online: Campo base:** SN3->N3\_VORIG1
* **Processo Offline: Campo base:** SN4->N4\_VLROC1

 Se necessário, é possível **formular condições** para atender a cenários específicos. Exemplo:

```
IIF(FWISINCALLSTACK("ATFA036") .AND. SN3->N3_TIPO=='01',SN3->N3_VORIG1, 
IIF(SN4->N4_TIPOCNT=='1' .AND. SN4->N4_TIPO=='01',SN4->N4_VLROC1,0))
```

**Atenção****:** como se trata de um **processo customizável**, é essencial seguir as orientações acima para obter o resultado esperado.  **A TOTVS não presta suporte para criação ou validação de expressões customizadas**, pois elas variam conforme a estrutura de cada cliente.

**Saiba mais**  
[**EXEMPLO\_LP\_820\_825\_DEPRECIACAO\_P12.**](https://tdn.totvs.com/pages/viewpage.action?pageId=273990370)  
[**CTBAATF - CONTABILIZAÇÃO OFFLINE**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021848932-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-CTBAATF-CONTABILIZA%C3%87%C3%83O-OFFLINE)
