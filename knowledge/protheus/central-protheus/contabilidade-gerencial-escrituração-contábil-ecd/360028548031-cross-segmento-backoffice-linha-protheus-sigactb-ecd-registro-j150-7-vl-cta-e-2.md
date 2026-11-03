---
article_id: 360028548031
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 136b1e81a6b4b256df3fd366b0c3f7f0d4184d589f587c9ffd8a3ad2fb09bb5f
fetched_at: '2026-06-28T22:40:44.351912+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD registro J150 -
  7-VL_CTA  e 2-COD_AGL
type: support-article
updated_at: '2022-04-18T17:59:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548031-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-registro-J150-7-VL-CTA-e-2-COD-AGL
---

**Dúvida**

Validador apresenta os erros abaixo ao validar o arquivo da ECD

J150  7-VL\_CTA "O valor do saldo(VL\_CTA) informado na linha de detalha da Demonstração de Resultado(J150.IND\_COD\_AGL=’D’) é diferente do resultado calculado com base nos registros de saldos periódicos (I155) e de saldos das contas de resultado(I355) na mesma data." 

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028739031/mceclip0.png)*

I052 COD\_AGL O código de aglutinação de uma linha detalhe da demonstração contábil deve ser informado em pelo menos um registro I052

* Veja que o J150 é apresentado com saldo

***![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028741331/mceclip1.png)***  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

* Realize a conciliação dos blocos[J150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-COMO-GERAR-O-REGISTRO-J150-?source=search) , [I350 ,I355 , I150 e I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016508952-MP-SIGACTB-N%C3%83O-GERA-REGISTROS-I350-I355-I150-I155?source=search)
* Veja como [I052 COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047840094-MP-SIGACTB-ECD-registro-I052-COMO-GERAR?source=search)
* situação pode estar sendo apresentada , pois esta gerando a ECD com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search) e o centro de custo possui saldo anterior ou movimento no período  , pois não foi zerado corretamente junto as contas de receita e despesa
* Para gerar o ECD com Centro de Custo é necessário primeiramente, que o Centro de Custo esteja apurado.Veja como realizar a [APURAÇÃO DAS ENTIDADES CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)
* Obs: caso esteja gerando com centro de custo, necessário verificar se o centro de custo esta devidamente zerado caso contrario o registro I052 não será gerado
* Veja se o  [Nivel\_AGL está correto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048123714-MP-SIGACTB-ECD-J150-Nivel-AGL-N%C3%A3o-deve-existir-mais-de-uma-linha-de-n%C3%ADvel-igual-a-1-na-DRE?source=search)
* Veja se o  [VL\_CTA e COD\_AGL estão corretamente cadastrados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548031-MP-SIGACTB-ECD-registro-J150-7-VL-CTA-e-2-COD-AGL?source=search)
* Veja como esta a **[ORDENAÇÃO RELATÓRIO (DRE e BALANÇO) X ECD (J00 e J150)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023832631-MP-SIGACTB-CTBA161-ORDENA%C3%87%C3%83O-RELAT%C3%93RIO-DRE-e-BALAN%C3%87O-X-ECD-J00-e-J150-?source=search)**
* Verifique se esta correto o "despesa gerais e administrativa" ser gerado Igual a "D" ou deveria gerar "C".
* Verifique se a situação ocorre somente para algum a conta "conta Ini e Conta Final" especifica. ex.: conta dedutora
* Verifique através do cadastro da visão o "Identific" esta como subtrai , deve ser informado "soma"

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028748751/mceclip5.png)

* Através do cadastro da visão verifique se o "Cond Normal" foi informado com a mesma natureza informado no cadastro da conta contábil
* Não Informe "Formula" no cadastro da visão gerencial

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028745372/mceclip3.png)

​

* Realize um teste mudando através do cadastro da visão "Identific" de subtrai para soma
* Gere um novo arquivo e veja se o erro "(J150.IND\_COD\_AGL="D")" continua sendo apresentado
* Acesse o cadastro da conta contábil e verifique  se a natureza da contas esta correta. Ex.: Dedutora , gere a revisão e veja se o saldo o J150 é gerado correto em comparação com relatório de DRE do Protheus

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028745092/mceclip2.png)​

* Verifique se a natureza "Cond normal " informada na conta está compatível com a informada na visão gerencial

![](https://totvssuporte.zendesk.com/attachments/token/0pPUAgLSWeDf0ryV6JEgzVFmu/?name=inline-570899655.png)

* Verifique se o nível de aglutinação criada na Visão segue "(mesmo conceito do plano de contas – Registro I050)"
* [MP-SIGACTB-ECD I050 : 5 - NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)
* Veja o que o manual da receita descreve sobre o NIVEL\_AGL do J150(DRE)

![](https://totvssuporte.zendesk.com/attachments/token/1J5VKiIo6b2E8d21ZKT5Sp1WP/?name=inline-735632808.png)

Realize as atualizações :

* Aplique [**Pacotes de Atualização - Contabilidade**](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777) seguindo as instruções [Aqui descritas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-MP-SIGACTB-Como-atualizar-o-ECD-?source=search)

Saiba mais :

[MP- SIGACTB : ECD : J150 ​](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-J150-LAYOUT-6?source=search)

[MP- SIGACTB : ECD : J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)
