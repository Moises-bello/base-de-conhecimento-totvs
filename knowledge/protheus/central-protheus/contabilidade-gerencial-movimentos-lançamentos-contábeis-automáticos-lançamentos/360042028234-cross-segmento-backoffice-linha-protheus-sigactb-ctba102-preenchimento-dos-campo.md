---
article_id: 360042028234
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: dd1edf1bca3ce8651c430c7d694ffa06fff309fb25b8c65b3bcd4bcf9b411862
fetched_at: '2026-06-28T22:40:32.459391+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 PREENCHIMENTO
  DOS CAMPOS CT2_MANUAL E CT2_ROTINA '
type: support-article
updated_at: '2022-05-31T17:21:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042028234-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-PREENCHIMENTO-DOS-CAMPOS-CT2-MANUAL-E-CT2-ROTINA
---

**Ocorrência**Sistema está gravando Contabilização TXT(CTBA500) com o campo CT2\_MANUAL =1 e CT2\_ROTINA =CTBA500

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056031874/mceclip0.png)  
   
 **Ambiente**Microsiga Protheus – Contabilidade – A partir da versão 11.80  
   
 **Causa**

O Lançamento Contábil, no módulo de Contabilidade Gerencial (**SIGACTB**), contem dois status: Manual e Automático**.**

Esses status podem ser identificados verificando o valor do campo: **CT2\_MANUAL - Lcto Manual, "1**" identifica que o lançamento é manual e "**2**" que é um lançamento de integração.

Ou seja, o campo **CT2\_MANUAL** será gravado com "**2**" sempre que o lançamento contábil for gerado por integração com outros módulos, permitindo a rastreabilidade da origem.

E será gravado com "**1**" quando cadastrado/digitado diretamente nas rotinas do módulo de Contabilidade Gerencial.

Rotinas consideradas como lançamento manual:

* Lançamentos Contábeis (**CTBA101**) ;
* Lançamentos Contábeis Automático (**CTBA102**);
* Lançamentos Contábeis Parametrizado (**CTBA103**);
* Contabilização TXT (**CTBA500**).

**Solução**

Existe o ponto de entrada **CTBGRV** utilizado após a gravação do lançamento contábil (inclusão, alteração ou estorno)  para manipular os dados gravados.

[CTBGRV - Executa procedimento](https://tdn.totvs.com/display/public/PROT/CTBGRV+-+Executa+procedimento+--+38076)
