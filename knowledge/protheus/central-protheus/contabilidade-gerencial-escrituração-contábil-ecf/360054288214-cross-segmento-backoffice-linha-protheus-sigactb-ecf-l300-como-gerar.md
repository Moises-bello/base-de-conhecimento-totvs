---
article_id: 360054288214
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: e5353621c55066b088b88d74a99263a1cc1292dd000c7c53b0cc5ca5872f60bf
fetched_at: '2026-06-28T22:40:47.554869+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus- SIGACTB - ECF – L300 COMO GERAR
type: support-article
updated_at: '2022-06-03T22:28:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054288214-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-L300-COMO-GERAR
---

**Dúvida**

Como gerar o L300 (DRE) ?

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Requisitos**

* [Como gerar ECF para o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)
* Para gerar com Centro de custo veja : [ECF - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search)
* [Não É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD),para entrega da ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)

**Solução**

* Verifique a [NATUREZA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006887272-MP-SIGACTB-CTBA020-NATUREZA-CONTA-CONTABIL-ECD-ECF?source=search) das contas contábeis

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093880533/mceclip0.png)

* Veja o lançamento criado

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091716974/mceclip1.png)

* Veja ao emitir o relatório

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091722074/mceclip2.png)

* Ao gerar a revisão através da rotina de escrituração (CTBS001)veja os parâmetros abaixo

FORMA\_TRIB : Forma de Tributação:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403566619159/mceclip0.png)**

[FORMA\_APUR Indicador do Período de Apuração do IRPJ e da CSLL:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403566448279)

COD\_QUALIF\_PJ

FORMA\_TRIB\_PER

MES\_BAL\_RED

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403574867735/mceclip1.png)**

* Ao gerar a ECF sem visão gerencial (Balanço e DRE) o sistema considera também a contas aqui informadas

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091722654/mceclip4.png)

* verifique se  ao  gerar o arquivo esta sendo informado a [Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search) de DRE

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091722154/mceclip3.png)

Reg L300          [CSC / CSK](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)        [T088AD](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) quando **não** utilizado Visão Gerencial, o sistema irá considerar a amarração do plano de contas com o plano referencial ([CVD, CVN, CT1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search))  
Reg L300          [CSD / CSE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)         [T088AD](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) quando utilizado Visão Gerencial. ([CTS, CVE, CVF, CTN)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)

**Para conciliação dos saldos**

* **Caso esteja utilizando**visão gerencial Verifique a amarração da visão , veja se ao emitir relatório com a visão gerencial (CTBR500,CTBR040) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado ,  será necessário avaliar a configuração da visão gerencial
* **Caso Não utilizando**visão gerencial verifique a amarração do plano referencial , veja se ao emitir relatórios relatórios Plano ref. X plano de contas (CTBR025 ,CTBR404,CTBR049) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado,  será necessário avaliar a  amarração da conta contabil com a conta referencial

* Veja CSC e CSK

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091726894/mceclip0.png)

* Verifique se o sistema apresenta o Bloco T088AD e se gerou os valores corretos

|T088AD|1|3.12.01.01.01.01|1000|2||T088AD|1|3.12.01.01.01.11|20|1|

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093887473/mceclip5.png)

* Verifique  se os valores estão corretos
* [Conheça o Layout de Integração](https://tdn.totvs.com/pages/releaseview.action?pageId=498722271)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093888193/mceclip6.png)

* Através modulo TAF os Blocos T são populadas nas tabelas  TAFST1 e TAFST2  com o saldos corretos
* Diante disso verifique se na tabela TAFST1 e TAFST2 se o bloco T088AA está correto o saldo apresentado está correto

Na tabela **TAFST1** e **TAFST2**

- no registro da conta verifique T088  
-Verifique se o STATUS das tabelas estão "3"

  \*posicione o Mouse no  "TAFKEY"  o registro T088 que possui T088AD

     \* Editar >Editar -  Verifique  se a conta referencial está sendo apresentada

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091725094/mceclip7.png)

[**Registro L300 - Demonstração do Resultado Líquido no Período Fiscal**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoL-LucroL%C3%ADquido-LucroReal)

* Tabela - CAT (Dem. Result. Líq. Per. Fiscal)
* Registro do Layout TOTVS - T088AD
* Rotina - TAFA361 (Bloco L - Lucro Líquido)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093888973/mceclip8.png)

* Ao gerar o arquivo foi gerado L300

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093889433/mceclip9.png)
