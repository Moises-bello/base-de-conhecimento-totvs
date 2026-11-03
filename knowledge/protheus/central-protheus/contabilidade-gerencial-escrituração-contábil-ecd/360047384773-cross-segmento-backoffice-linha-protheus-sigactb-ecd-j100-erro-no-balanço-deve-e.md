---
article_id: 360047384773
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: ec5bef8d4ff4dd4363f1b2459646f5c9fc0436c4f8bfc73777e43bd25b6520bb
fetched_at: '2026-06-28T22:40:44.294664+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD -  J100 ERRO NO
  BALANÇO DEVE EXISTIR DUAS LINHAS DE NIVEL 1,UMA DE ATIVO E OUTRA DE PASSIVO
type: support-article
updated_at: '2022-04-11T12:11:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047384773-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-J100-ERRO-NO-BALAN%C3%87O-DEVE-EXISTIR-DUAS-LINHAS-DE-NIVEL-1-UMA-DE-ATIVO-E-OUTRA-DE-PASSIVO
---

**Dúvida**

Erro no J100    
No Balanço deve existir duas linhas de nível 1, uma de Ativo e outra de Passivo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067278674/mceclip0.png)  
  
  
**Ambiente**Microsiga Protheus– Contabilidade gerencial  – A partir da versão 11.80  
  
**Solução**

Veja o arquivo esta gerando as J100 do Passivo com A  
  
​

Veja o destalhes dos campos  
  
![](https://totvssuporte.zendesk.com/attachments/token/U2YdlDY568d21acYeCkWzipRn/?name=inline1184031366.png)​  
  
Veja como o manual da receita descreve sobre o campo 06 IND\_GRP\_BAL  
  
![](https://totvssuporte.zendesk.com/attachments/token/WygnLaDbGc026Yki38fZyWwto/?name=inline2067075327.png)​  
  
Veja no validador o campo está como Ativo  
  
![](https://totvssuporte.zendesk.com/attachments/token/DAEdYaSVPHVlsc5cLF6hS9UyU/?name=inline-2060336644.png)​

* Para que o sistema gere P (Passivo) necessário realizar o procedimento descrito na documentação abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072138114/mceclip1.png)

* Estrutura do Registro com base no manual da receita

|J100|001211|D|3|00121|**P**|FORNECEDORES|0,00|C|2500,00|C||

Campo 01 – Tipo de Registro: J100  
Campo 02 – Código de Aglutinação: 001211  
Campo 03 – Indicador do Tipo de Código de Aglutinação: D  
Campo 04 – Nível do Código de Aglutinação: 3  
Campo 05 – Código de Aglutinação de Nível Superior: 00121  
Campo 06 – Indicador de Grupo do Balanço: **P (Passivo**)  
Campo 07 – Descrição do Código de Aglutinação: FORNECEDORES  
Campo 08 – Valor Inicial do Código de Aglutinação: 0,00 (0,00)  
Campo 09 – Indicador da Situação do Saldo Informado no Campo Anterior: C (Credito)  
Campo 10 – Valor Final do Código de Aglutinação: 2500,00 (2.500,00)  
Campo 11 – Indicador da Situação do Saldo Informado no Campo Anterior: C (Credito)  
Campo 12 – Referência à Numeração das Notas Explicativas: Não há

* Quando passivo "Coluna =2" , para mais detalhes [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072138174/mceclip2.png)

* Para que a situação não seja apresentada necessário revisar a estrutura da visão gerencial , veja que existe nível "total geral"
* Para mais detalhe  [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006972612-MP-SIGACTB-ECD-J150-?source=search)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072107953/mceclip4.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070961574/mceclip0.png) :

* Verifique se o nível de aglutinação criada na Visão segue "(mesmo conceito do plano de contas – Registro I050)"
* [MP-SIGACTB-ECD I050 : 5 - NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)
* Veja o que o manual da receita descreve sobre o NIVEL\_AGL do J100 (Balanço)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081467634/mceclip0.png)

Veja se o nível do ativo e do passivo estão corretas

Ex.: Ativo possui 3 níveis

1 Ativo (Sintética) - Primeiro nível

->11  Circulante (Sintética) - Segundo nível

     ->111 (Analítica) - Terceiro nível

     ->112 (Analítica) - Terceiro nível

     ->113 (Analítica) - Terceiro nível

     ->114 (Analítica) - Terceiro nível

     ->115 (Analítica) - Terceiro nível

     ->116 (Analítica) - Terceiro nível

->12 Não Circulante (Sintética) - Segundo nível 

Veja o conceito para J150(DRE) [J150 Nivel\_AGL Não deve existir mais de uma linha de nível igual a 1 na DRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048123714-MP-SIGACTB-ECD-J150-Nivel-AGL-N%C3%A3o-deve-existir-mais-de-uma-linha-de-n%C3%ADvel-igual-a-1-na-DRE?source=search)
