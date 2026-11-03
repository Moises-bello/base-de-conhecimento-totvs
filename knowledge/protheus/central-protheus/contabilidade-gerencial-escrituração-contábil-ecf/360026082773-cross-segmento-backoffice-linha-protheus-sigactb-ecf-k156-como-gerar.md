---
article_id: 360026082773
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 45e2df7f127ed67e4366c57de69cc1928e786308305ca5fe5830890dca6e7739
fetched_at: '2026-06-28T22:40:48.774547+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF : K156  COMO GERAR'
type: support-article
updated_at: '2022-06-03T19:36:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-K156-COMO-GERAR
---

**Dúvida**Procedimento para gerar o K156  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12

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

Através da rotina de escrituração CTBS001  verifique se o Registro K156  foi gerado na tabela [CSK](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041290393/mceclip2.png)

Blocos/Registros – geração no TAF ou na integração

**[Registro K156 - Mapeamento Referencial do Saldo Fina](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)l**

* Tabela - CAE (Map. Referencia do Saldo Final)
* Registro do Layout TOTVS - T087AB
* Rotina - TAFA311 (Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL)

Registro            [Tabela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)             [TAFST1/TAFST2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)  
Reg K156          CSK                  T087AB

Na tabela [TAFST1 e TAFST2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

- no registro da conta verifique [T087AB](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoJ-PlanodeContaseMapeamento)

  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração

     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada

   Ex: |T087AB|01|1.01.01.01.02|6688|2|0|1|2500|9188|

- Verifique o TAFSTATUS = 3

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040458854/mceclip3.png)

Através da rotina [TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) e verifique se o bloco foi gerado

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041290753/mceclip4.png)

* Altere o Diretório do arquivo
* Altere o nome do arquivo destino

![](https://totvssuporte.zendesk.com/attachments/token/6wBKU4qL5wwjoKCFBsMTNjktw/?name=inline244680701.png)

* Selecione o bloco K para que seja processado

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041290853/mceclip5.png)

* Ao gerar o arquivo verifique se foi gerado corretamente

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040459234/mceclip6.png)

Veja também :[MP - SIGACTB - ECF : K156 Quantidade de campos incorreta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029075352-MP-SIGACTB-ECF-K156-Quantidade-de-campos-incorreta?source=search)
