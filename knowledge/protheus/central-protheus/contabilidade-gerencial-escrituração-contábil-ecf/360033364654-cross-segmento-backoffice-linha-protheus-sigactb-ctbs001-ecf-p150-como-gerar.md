---
article_id: 360033364654
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 838dc0e6f3ce37be5eba439d3b105308e0f472f611149f36d6644a40e8022bc0
fetched_at: '2026-06-28T22:40:47.697209+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 -ECF – P150
  COMO GERAR
type: support-article
updated_at: '2024-07-18T12:19:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033364654-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-P150-COMO-GERAR
---

**Dúvida**Como gerar o registro P150   
  
**Ambiente**  
Microsiga Protheus – Contabilidade  – A partir da versão 11.80  
  
**Requisito**

* Regime tributário Lucro presumido
* apuração trimestral
* plano referencial amarrado do Lucro presumido
* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
* [É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)

**Solução**

* Ao gerar a revisão através da rotina de escrituração (CTBS001)veja os parâmetros abaixo

FORMA\_TRIB : Forma de Tributação:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15669578340759)**

[FORMA\_APUR Indicador do Período de Apuração do IRPJ e da CSLL:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403566448279)

COD\_QUALIF\_PJ

FORMA\_TRIB\_PER

MES\_BAL\_RED

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15669524636055)**

* Para gerar o Balanço Patrimonial (Registros P100)  e Demonstrativo de Resultado ( Registros P150 ) o sistema considera a visão gerencial informada  ou caso **não**informe a visão gerencial ,o sistema **considera o plano referencial amarrado ao plano de contas**

Reg P150          CSC / CSK         T092AC quando **não** utilizado Visão Gerencial,o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg P150          CSD / CSE         T092AC quando utilizado Visão Gerencial. 

* **Caso esteja utilizando**visão gerencial Verifique a amarração da visão , veja se ao emitir relatório com a visão gerencial (CTBR510) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo erro  está na configuração da visão gerencial

![](https://totvssuporte.zendesk.com/attachments/token/uo4hyCmxrncRhOwArQLDmeNQP/?name=inline-658591959.png)​

* Caso **não** esteja informado visão gerencial o sistema irá considerar **o plano referencial amarrado ao plano de contas para gerar o P150(DRE)**diante dissoverifique as amarrações se estão corretas através da**CVD**

**![](https://totvssuporte.zendesk.com/attachments/token/qeA1StKy3oD2O8JMKqIteP8KY/?name=inline2099722983.png)​**

**Lançamentos contabeis**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978852433431)**

**[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)**

* Através do Modulo Contábil  são populadas as Tabela Cs
* [Compartilhamento das tabelas CS's (ECD e ECF)](http://tdn.totvs.com/pages/releaseview.action?pageId=287077842)
* Através da rotina CTBS001 é possível visualizar se as tabelas foram populadas
* Diante disso verifique se a

Reg P150          CSC / CSK         T092AC quando **não** utilizado Visão Gerencial,o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg P150          CSD / CSE         T092AC quando utilizado Visão Gerencial. 

* CSC

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978852435223)​

* **CSK**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978879084311)**

**Registro P150 - Demonstrativo do Resultado do Exercício**

* Tabelas - CHA (Código de Conta Referencial) / C2R (Natureza Conta/Grupo Contab.) / CHE (Demonst Resultado Exercício)
* Registro do Layout TOTVS - T092AC
* Rotina - TAFA321 (Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido)

<http://tdn.totvs.com/pages/releaseview.action?pageId=192089512>

-Verifique se a tabela TAFST1 e TAFST2 foram  alimentadas :

**SEGUE OS BLOCOS**

Registro        Tabela CTB   TASFST1/TAFST2

Reg P150          CSC / CSK         T092AC 

Reg P150          CSD / CSE         T092AC 

Na tabela **TAFST1** e **TAFST2**

- no registro da conta verifique T092

  \*posicione o Mouse no  "TAFKEY"  o registro T092 que possui T092AC

     \* Editar >Editar -  Verifique  se a conta referencial está sendo apresentada

   Ex:

|T092AC|3.01.01.01.01|3500|1|

- Verifique o TAFSTATUS = 3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978852450199)​

Acesse as rotinas abaixo para verificar se os foram alimentados:

TAFA321-Verifique se registro foi gerado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978852453783)​

Gere o arquivo ECF  e veja se o registro foi gerado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24978879092375)​
