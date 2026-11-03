---
article_id: 360054165034
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: ed0571e56f0b7afa7ee9f8834f53fe74bfb88883cc26a6b88b77798def6cf40c
fetched_at: '2026-06-28T22:40:47.479516+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF – L100 COMO GERAR
type: support-article
updated_at: '2022-08-11T17:39:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054165034-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-L100-COMO-GERAR
---

**Dúvida**

Como gerar o L100 (Balanço) ?  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Requisitos**

* [Como gerar ECF para o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)
* Para gerar com Centro de custo veja : [ECF - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search)
* [É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)

**Solução**

* Verifique a [NATUREZA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006887272-MP-SIGACTB-CTBA020-NATUREZA-CONTA-CONTABIL-ECD-ECF?source=search) das contas contábeis

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093545773/mceclip0.png)

* Veja o lançamento criado

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091387694/mceclip1.png)

* Veja ao emitir o relatório

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093547773/mceclip2.png)

* Ao gerar a revisão através da rotina de escrituração (CTBS001)veja os parâmetros abaixo

FORMA\_TRIB : Forma de Tributação:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403566619159/mceclip0.png)**

[FORMA\_APUR Indicador do Período de Apuração do IRPJ e da CSLL:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403566448279)

COD\_QUALIF\_PJ

FORMA\_TRIB\_PER

MES\_BAL\_RED

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403574867735/mceclip1.png)**

* Informar o parâmetro correto abaixo
* [MP - SIGACTB - ECF - J050 e J051 COMO GERAR](http://tdn.totvs.com/pages/releaseview.action?pageId=284465420)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093415354/mceclip0.png)

* verifique se  ao  gerar o arquivo esta sendo informado a [Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search) de balanço

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091388874/mceclip3.png)

* O Sistema permite gerar o Balanço ao informar a Visão  e sem informar a visão  
    
  Reg L100          [CSC / CSK](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)        [T088AA](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) quando não utilizado Visão Gerencial, será gerado com base na amarração do plano de contas com o plano referencial  
  Reg L100          [CSD / CSE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)         [T088AA](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) quando utilizado Visão Gerencial, será gerado com base na amarração da visão gerencial

**Para conciliação dos saldos**

* **Caso esteja utilizando**visão gerencial Verifique a amarração da visão , veja se ao emitir relatório com a visão gerencial (CTBR500,CTBR040 ) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado ,  será necessário avaliar a configuração da visão gerencial
* **Caso Não utilizando**visão gerencial verifique a amarração do plano referencial , veja se ao emitir relatórios relatórios Plano ref. X plano de contas (CTBR025 ,CTBR404,CTBR049) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado,  será necessário avaliar a  amarração da conta contabil com a conta referencial

* Veja CSC

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091390514/mceclip4.png)

* Veja CSK

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093550173/mceclip5.png)

* Verifique se o sistema apresenta o Bloco T088AA e se gerou os valores corretos

|T088AA|1|1.01.01.05.02|0|1|0|**1**|37727.35|37727.35|

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093551533/mceclip6.png)

* Verifique  se os valores estão corretos
* [Conheça o Layout de Integração](https://tdn.totvs.com/pages/releaseview.action?pageId=498722271)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093552673/mceclip7.png)

* Através modulo TAF os Blocos T são populadas nas tabelas  TAFST1 e TAFST2  com o saldos corretos
* Diante disso verifique se na tabela TAFST1 e TAFST2 se o bloco T088AA está correto o saldo apresentado está correto

Na tabela **TAFST1** e **TAFST2**

- no registro da conta verifique T088  
-Verifique se o STATUS das tabelas estão "3"

  \*posicione o Mouse no  "TAFKEY"  o registro T088 que possui T088AA

     \* Editar >Editar -  Verifique  se a conta referencial está sendo apresentada

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093553533/mceclip8.png)

* Através da Rotina - TAFA361  seja se o saldo gerado está correto e compatível com o saldo visto na tabela TAFST1 e TAFST2

[**Registro L100 - Balanço Patrimonial**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoL-LucroL%C3%ADquido-LucroReal)

* Tabela - CAQ (Balanço Patrimonial)
* Registro do Layout TOTVS - T088AA
* Rotina - TAFA361 (Bloco L - Lucro Líquido)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093553873/mceclip9.png)

* Ao gerar o arquivo foi gerado L100

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091394294/mceclip10.png)

Erro gerado para o bloco L100

[MP - SIGACTB - ECF - ( CAQ\_REGECF ) somado ao valor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006649692-MP-SIGACTB-ECF-CAQ-REGECF-somado-ao-valor?source=search)
