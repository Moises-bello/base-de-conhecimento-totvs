---
article_id: 360028247351
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: a4b6b6158c9d92ce3f874ff8162b25f8d50106d90a00337a06666f05342d65d4
fetched_at: '2026-06-28T22:40:44.525209+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como configurar o DRE,
  registro J150, da ECD
type: support-article
updated_at: '2021-11-29T17:25:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-configurar-o-DRE-registro-J150-da-ECD
---

**Dúvida**

Como é gerado o DRE e o Registro J150    
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Contabilidade gerencial  – A partir da versão 11.80  
  
**Solução**

* Caso esteja gerando o arquivo com**[Centro de Custo (Clique Aqui)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search)**
* Veja a melhoria**[ORDENAÇÃO RELATÓRIO (DRE e BALANÇO) X ECD (J00 e J150)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023832631-MP-SIGACTB-CTBA161-ORDENA%C3%87%C3%83O-RELAT%C3%93RIO-DRE-e-BALAN%C3%87O-X-ECD-J00-e-J150-?source=search)**
* Através da rotina Lançamento contábeis**(CTBA102)**Verifique os lançamento Contábeis

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028184372/mceclip0.png)

* Emita o relatório DRE  e verifique os valores

![](https://totvssuporte.zendesk.com/attachments/token/OOsbKrtuFVfE5rkJUOO8wQyKH/?name=inline-218009853.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/ctWlI1L1PcCaluAjjFZ2mgTlO/?name=inline517725344.png)​  
  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/CIiVoUyJErDnd2EDmRArfPUs3/?name=inline412447964.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/gpqudJOitx478HFv0zRH8ydxm/?name=inline-1405694202.png)​

Exemplo de estrutura para a DRE :

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091550633/mceclip0.png)

* Através do cadastro da visão gerencial (CTBA161) Verifique os campos abaixo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072101973/mceclip0.png)

* Entidade sintética /totalizadora
* Verifique se a natureza (Débito ou Credito ) está informada corretamente

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070952334/mceclip1.png)

* Entidade sintética
* Verifique se a natureza (Débito ou Credito ) está informada corretamente

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072102033/mceclip2.png)

* Entidade analítica amarrada a sintética
* Verifique se a natureza (Débito ou Credito ) está informada corretamente

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072102073/mceclip3.png)

* Entidade analítica amarrada a sintética
* Verifique se a natureza (Débito ou Credito ) está informada corretamente

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070952434/mceclip4.png)

* Entidade Sintética amarrada a sintética totalizadora
* Verifique se a natureza (Débito ou Credito ) está informada corretamente

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070952454/mceclip5.png)

* Entidade analítica amarrada a sintética
* Verifique se a natureza (Débito ou Credito ) está informada corretamente

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072102193/mceclip6.png)

* Entidade analítica amarrada a sintética
* Verifique se a natureza (Débito ou Credito ) está informada corretamente

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070952474/mceclip7.png)

* Não Informe "Formula" no cadastro da visão gerencial , informe total geral nas sintéticas
* Verifique se a natureza (Débito ou Credito ) está informada corretamente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028182251/mceclip2.png)

* Para que o sistema considere o campo CVF\_ORDEM necessário configurar o parâmetro[MV\_GRVISOR ORDEM= T](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026127292-MP-SIGACTB-ECD-J100-e-J150-MV-GRVISOR-ORDEM-DA-VISAO-GERENCIAL?source=search)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070751074/mceclip0.png)

* Través do cadastro de plano de contas (CTBA020) verifique a natureza da conta e a natureza da conta superior

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028185972/mceclip3.png)

* Ao gerar o arquivo da ECD através da rotina de escrituração contábil(CTBS001) , verifique a Visão gerencial que esta sendo informada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028190552/mceclip4.png)

* Gere o arquivo e veja se o Valor apresentado corresponde ao mesmo valor apresentado no DRE

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072103133/mceclip8.png)

 Verifique se o nível de aglutinação criada na Visão segue "(mesmo conceito do plano de contas – Registro I050)"

* [MP-SIGACTB-ECD I050 : 5 - NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)
* Veja o que o manual da receita descreve sobre o NIVEL\_AGL do J150(DRE)

![](https://totvssuporte.zendesk.com/attachments/token/1J5VKiIo6b2E8d21ZKT5Sp1WP/?name=inline-735632808.png)

Veja mais :

[Visão gerencial e os relatórios contábeis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013555431-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA161-Conta-Cont%C3%A1bil-em-relat%C3%B3rios-cont%C3%A1beis-com-vis%C3%A3o-gerencial-)

[MP\_SIGACTB - ECD - J150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006972612-MP-SIGACTB-ECD-J150-?source=search)

[MP-SIGACTB: CTBA161 ORDENAÇÃO RELATÓRIO (DRE e BALANÇO) X ECD (J00 e J150)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023832631-MP-SIGACTB-CTBA161-ORDENA%C3%87%C3%83O-RELAT%C3%93RIO-DRE-e-BALAN%C3%87O-X-ECD-J00-e-J150-?source=search)

[MP-SIGACTB ECD NAO EXISTE NENHUM REGISTRO J800 COM J800.TIPO\_DOC= 10, 11, 12 OU 99 ATRELADO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025419031-MP-SIGACTB-ECD-NAO-EXISTE-NENHUM-REGISTRO-J800-COM-J800-TIPO-DOC-10-11-12-OU-99-ATRELADO?source=search)

[MP\_SIGACTB\_ECD RELATORIO J150 (DRE) NO PGE NÃO CORRESPONDE AO EMITIDO NO PROTHEUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026626772-MP-SIGACTB-ECD-RELATORIO-J150-DRE-NO-PGE-N%C3%83O-CORRESPONDE-AO-EMITIDO-NO-PROTHEUS?source=search)

[MP- SIGACTB : ECD : J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)

[MP- SIGACTB : ECD : Deve existir pelo menos um registro J100 (Balanço) e um J150 (DRE) para cada registro J005 (Demonstração Contábil) informado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049318233-MP-SIGACTB-ECD-Deve-existir-pelo-menos-um-registro-J100-Balan%C3%A7o-e-um-J150-DRE-para-cada-registro-J005-Demonstra%C3%A7%C3%A3o-Cont%C3%A1bil-informado-?source=search)
