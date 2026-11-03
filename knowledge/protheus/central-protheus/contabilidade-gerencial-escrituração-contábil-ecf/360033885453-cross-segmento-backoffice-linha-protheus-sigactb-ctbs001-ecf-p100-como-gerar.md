---
article_id: 360033885453
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: c2c518042024518b754a2cbc00acffa0986ecbcbd73744611045a0a637a1fe29
fetched_at: '2026-06-28T22:40:47.685835+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - ECF P100 COMO
  GERAR
type: support-article
updated_at: '2024-07-18T12:18:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033885453-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-P100-COMO-GERAR
---

**Dúvida**Como gerar o registro P100 ?  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade  – A partir da versão 11.80  
  
**Requisitos**

* Regime tributário Lucro presumido
* apuração trimestral
* plano referencial amarrado do Lucro presumido
* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
* [É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)

**Solução**

* Ao gerar a revisão através da rotina de escrituração (CTBS001)veja os parâmetros abaixo

FORMA\_TRIB : Forma de Tributação:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15669611952663)**

[FORMA\_APUR Indicador do Período de Apuração do IRPJ e da CSLL:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403566448279)

COD\_QUALIF\_PJ

FORMA\_TRIB\_PER

MES\_BAL\_RED

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15669611959447)**

* Para realizar a conferencial dos saldo :

* Ao geral arquivo sem visão

* Para gerar o Balanço Patrimonial (Registros P100)  e Demonstrativo de Resultado ( Registros P150 ) o sistema considera a visão gerencial informada  ou caso **não**informe a visão gerencial ,o sistema **considera o plano referencial amarrado ao plano de contas**

Reg P100          CSC / CSK         T092AA quando **não** utilizado Visão Gerencial, o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg P100          CSD / CSE         T092AA quando utilizado Visão Gerencial. 

**Para conciliação dos saldos**

* **Caso esteja utilizando**visão gerencial Verifique a amarração da visão , veja se ao emitir relatório com a visão gerencial (CTBR500,CTBR040 ) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado ,  será necessário avaliar a configuração da visão gerencial
* **Caso Não utilizando**visão gerencial verifique a amarração do plano referencial , veja se ao emitir relatórios relatórios Plano ref. X plano de contas (CTBR025 ,CTBR404,CTBR049) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado,  será necessário avaliar a  amarração da conta contabil com a conta referencial

![](https://totvssuporte.zendesk.com/attachments/token/uo4hyCmxrncRhOwArQLDmeNQP/?name=inline-658591959.png)​

* Caso **não** esteja informado visão gerencial o sistema irá considerar **o plano referencial amarrado ao plano de contas para gerar o P100(BALANÇO)**diante dissoverifique as amarrações se estão corretas através da**CVD**

**![](https://totvssuporte.zendesk.com/attachments/token/qeA1StKy3oD2O8JMKqIteP8KY/?name=inline2099722983.png)​**

**Lançamentos contabeis**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978657565079)**

**[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)**

* Através do Modulo Contábil  são populadas as Tabela Cs
* [Compartilhamento das tabelas CS's (ECD e ECF)](http://tdn.totvs.com/pages/releaseview.action?pageId=287077842)
* Através da rotina CTBS001 é possível visualizar se as tabelas foram populadas
* Diante disso verifique se a

Reg P100          CSC / CSK         T092AA quando **não** utilizado Visão Gerencial, o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg P100          CSD / CSE         T092AA quando utilizado Visão Gerencial. 

* CSC

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978657567255)

* CSK

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978657568663)​

* **Registro P100 - Balanço Patrimonial**

  + Tabelas - CHA (Código de Conta Referencial) / C2R (Natureza Conta/Grupo Contab.) / CEH (Balanço Patrimonial)
  + Registro do Layout TOTVS - T092AA
  + Rotina - TAFA321 (Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido)

<http://tdn.totvs.com/pages/releaseview.action?pageId=192089512>

-Verifique se a tabela TAFST1 e TAFST2 foram  alimentadas :

**SEGUE OS BLOCOS**

Registro        Tabela CTB   TASFST1/TAFST2

Reg P150          CSC / CSK        T092AA

Reg P150          CSD / CSE        T092AA

Na tabela **TAFST1** e **TAFST2**

- no registro da conta verifique T092

  \*posicione o Mouse no  "TAFKEY"  o registro T092 que possui T092AA

     \* Editar >Editar -  Verifique  se a conta referencial está sendo apresentada

   Ex:

[|T092AA|1.01.01.01.01|0|1|1500|1|1500|0|](https://tdn.totvs.com/pages/releaseview.action?pageId=187534666)

[|T092AA|2.01.01.01.05|0|1|150|2|0|150|](https://tdn.totvs.com/pages/releaseview.action?pageId=187534666)

[|T092AA|2.03.04.01.90|0|1|1350|2|150|1500|](https://tdn.totvs.com/pages/releaseview.action?pageId=187534666)

- Verifique o TAFSTATUS = 3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978657572375)​

Acesse as rotinas abaixo para verificar se os foram alimentados:

TAFA321-Verifique se registro foi gerado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978614155287)​

Gere o arquivo ECF  e veja se o registro foi gerado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978657579927)​
