---
article_id: 360007125451
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: f96d19f0e12fdea74c3612aab767afb2afff2bb40d6c1684ef556e23f09ffa0a
fetched_at: '2026-06-28T22:40:47.250205+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGACTB - ECF - Bloco Q
type: support-article
updated_at: '2024-05-22T11:25:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125451-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Bloco-Q
---

**Dúvida**

* Geração do Bloco Q
* Ao gerar Livro caixa o sistema só gera o blocos de abertura

**Ambiente**Protheus – TAF – A partir da versão 11.8

**Causa**

Manual da receita descreve :

(...) Para as pessoas jurídicas tributadas pelo lucro presumido e imunes ou isentas não obrigadas a entregar a ECD, o campo escrituração – “**TIP\_ESC\_PRE**” – do registro 0010 deve ser preenchido  
com **“L”** (não obrigada a entregar a ECD). Nessa situação, os blocos **C, E, J e K não serão** preenchidos.(...)

Quando o contribuinte estiver nessas condições e dispensado da entrega da ECD, não será necessário o preenchimento do plano de contas e plano referencial. Somente apresentar o Bloco Q e blocos de abertura e encerramento na ECF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23659292160791)

**Solução**

* Para gerar o bloco Q precisa  
   Obrigatório se 0010. TIP\_ESP\_PRE = “L” N Senão, não deve existir.
* Para gerar o bloco P precisa  
  Obrigatório se 0010. TIP\_ESP\_PRE = “C” N Senão, não deve existir

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007722351)

* IND\_REC\_RECEITA =1

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007722371)

Bloco Q: Livro Caixa. A rotina de contabilidade não integra o Bloco Q.  
  
Assim, se torna necessário preencher o dados diretamente no TAF, através da [Rotina  - TAFA429](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoQ-LivroCaixa)

Segue link com documentação:

* [ECF0006\_Empresas\_obrigadas\_a\_entregar\_o\_ECF\_e\_não\_obrigadas\_a\_entregar\_o\_ECD](http://tdn.totvs.com/pages/viewpage.action?pageId=240308035)
* [Bloco Q: Livro Caixa](http://tdn.totvs.com/pages/releaseview.action?pageId=192094180#Blocos/Registros-blocoq)
* [Registro Q990: Encerramento do Bloco Q](http://tdn.totvs.com/pages/releaseview.action?pageId=192089512#ECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoQ-LivroCaixa)
* [MP-SIGACTB - ECF - VALIDAÇÃO 14- IND\_REC\_RECEITA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008385052-MP-SIGACTB-ECF-VALIDA%C3%87%C3%83O-14-IND-REC-RECEITA)
* [ERRO PVA -TIP\_ESC\_PRE.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006982951-MP-SIGACTB-ECF-ERRO-PVA-TIP-ESC-PRE?source=search)

* Rotina de escrituração integrar os blocos de abertura

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007722391)
