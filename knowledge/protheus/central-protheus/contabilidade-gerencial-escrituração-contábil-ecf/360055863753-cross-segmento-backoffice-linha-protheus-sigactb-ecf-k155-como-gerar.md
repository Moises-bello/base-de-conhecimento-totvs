---
article_id: 360055863753
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 55818bbaca6a51da3c5e955bfd86d3c3b01dfd429b2ec6d9f047beae19119478
fetched_at: '2026-06-28T22:40:47.378044+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - K155 COMO GERAR
type: support-article
updated_at: '2021-11-18T14:21:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055863753-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-K155-COMO-GERAR
---

**Dúvida**Procedimento para gerar o K155  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Requisito**

Necessário gerar a ECF com base no regime tributário de  empresa

* [Como gerar o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
* [IMUNE OU ISENTA COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search)

**Solução**

* Ao gerar a revisão através da rotina de escrituração (CTBS001)veja os parâmetros abaixo

FORMA\_TRIB : Forma de Tributação:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403566619159/mceclip0.png)**

[FORMA\_APUR Indicador do Período de Apuração do IRPJ e da CSLL:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403566448279)

COD\_QUALIF\_PJ

FORMA\_TRIB\_PER

MES\_BAL\_RED

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403574867735/mceclip1.png)**

Através da rotina de escrituração CTBS001  verifique se o Registro K155 foi gerado na tabela [CSC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093217633/mceclip1.png)

Blocos/Registros – geração no TAF ou na integração

[**Registro K155 - Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoK-SaldosdasContasCont%C3%A1beiseReferenciais)

* Tabela - CAD (Saldos Cont Encerram. Periodo)
* Registro do Layout TOTVS - T087AA
* Rotina - TAFA311 (Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL)

Registro            [Tabela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)             [TAFST1/TAFST2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)  
Reg K155          CSC                  T087AA

Na tabela [TAFST1 e TAFST2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

- no registro da conta verifique [T087AA](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoJ-PlanodeContaseMapeamento)

  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração

     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada

   Ex: |[T087AA|21101001||0|1|0|590|590|2|](https://tdn.totvs.com/pages/releaseview.action?pageId=187534666)

- Verifique o TAFSTATUS = 3

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093218193/mceclip3.png)

Através da rotina [TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) e verifique se o bloco foi gerado

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093219933/mceclip4.png)

* Altere o Diretório do arquivo
* Altere o nome do arquivo destino

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091081454/mceclip6.png)

* Selecione o bloco K para que seja processado

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041290853/mceclip5.png)

* Ao gerar o arquivo verifique se foi gerado corretamente

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091081394/mceclip5.png)

Saiba Mais:

[MP - SIGACTB - ECF : K156 Quantidade de campos incorreta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029075352-MP-SIGACTB-ECF-K156-Quantidade-de-campos-incorreta?source=search)
