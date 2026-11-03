---
article_id: 7345360456343
category: TAF - eSocial - Relatório
content_hash: 14c0cd704a7f1191c4f57b78a4cd62e92873f106a6a6208a6085ee3a9de622cf
fetched_at: '2026-06-28T22:45:19.977399+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Relatório - O valor calculado pelo eSocial
  (DCTFWEB), no relatório de INSS, está errado
type: support-article
updated_at: '2024-05-23T19:59:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7345360456343-RH-Linha-Protheus-TAF-eSocial-Relat%C3%B3rio-O-valor-calculado-pelo-eSocial-DCTFWEB-no-relat%C3%B3rio-de-INSS-est%C3%A1-errado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23699518547991) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Gerei o relatório de INSS, pelo TAF do Futuro, verificamos que o valor retornado pelo governo está errado, divergente do valor calculado na Folha, e apresentado na coluna do TAF.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório INSS (TAFA552) - Todas as versões  
  
**Como analisar:**

1. Identifique um colaborador com o problema, para ter como estudo de caso.

2. Gere o XML de retorno, referente ao evento S-5001 - Informações das contribuições sociais consolidadas por trabalhador;

*\*\*O S-5001 é retornado para eventos de remuneração, que são: S-1200, S-2299 ou S-2399*

[Automação - Configuração - Gerar XML de retorno dos eventos no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046869313)

3. Verifique no relatório de INSS, gerado pela rotina Esocial do Futuro, os valores apresentados nas colunas: ***"Valor INSS - Calculado pelo eSocial (Valor da DCTFWEB)"** e **"Valor INSS - Descontado do Colaborador em Folha (enviado)"***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7371221068695)

4. Se identificado que os valor apresentados nas respectivas colunas, estão diferentes do esperado: abra o XML de retorno do Governo, o S-5001:

5. Localize o grupo com T**AG** **<InfoCpCalc>,** dentro deste grupo, estará especificado o valor calculado e descontado pela Folha:

**TAG <vrCpSeg>** = Trata-se da informação calculada pelo Governo, e que será utilizada para recolhimento efetivo do imposto.

**TAG <****vrDescSeg>** = Valor efetivamente descontado do segurado, somado, por Tipo de valor <tpCR>;

*Exemplo de XML de retorno S-5001, onde localizar as TAGS e os valores:*

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7372167573911)

6. Compare o valor das TAG **<vrCpSeg>,** retornadas no XML, com o valor da coluna ***"Valor INSS - Calculado pelo eSocial (Valor da DCTFWEB)"*** apresentado no relatório de INSS:

**Valor no XML =** R$ 265,459 arredondando **R$ 265,46**

***![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7373728734231)***

***X***

**Valor na coluna "Valor INSS - Calculado pelo eSocial (Valor da DCTFWEB)" do relatório:** R$ 265,46

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7376488110103)

7. O mesmo processo pode ser realizado para a tag **<****vrDescSeg>.** Compare com a coluna ***"Valor INSS - Descontado do Colaborador em Folha (enviado)"*** do relatório.

**Valor no XML =** R$ 251,27

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7378199687575)

***X***

***Valor na coluna "Valor INSS - Descontado do Colaborador em Folha (enviado)":***

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7378883002775)

**Resultado da análise:**

***1. Valores entre XML de retorno e relatório de INSS estão iguais, como o exemplo citado acima:***

Neste caso,  é necessário que o cliente analise as rubricas referentes ao INSS, envolvidas no XML de origem (S-1200, S-2299 ou S-2399), entender, se estão com as configurações corretas no governo (Portal do eSocial), para que sejam consideradas.

Identificando erro de rubrica no Portal do eSocial, é necessário a correção desta rubrica, e depois, realizar a transmissão novamente dos eventos de origem.

[Automação Fiscal - Relatório - Como as rubricas (verbas) referentes ao INSS, devem estar configuradas, para que sejam consideradas no Relatório de Conferência de INSS ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7451051867031)

***2. Valores entre XML de retorno e relatório de INSS estão diferentes:***

Neste caso, orientamos:

\* Reavalie os totalizadores, para que o valor de retorno do governo seja atualizado:

[Automação Fiscal - MONITORAMENTO - Como reavaliar totalizadores](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052778534)

\* Mesmo reavaliando totalizadores, o valor está divergente:

Abra um ticket para o suporte padrão TAF, com as seguintes informações:

a) Relate se existe alguma particularidade nos registros retornados errados;

b) Informe qual dos valores estão corretos, se é o valor retornado no XML do evento S-5001, ou o valor apresentado no relatório do TAF.

c) Encaminhe as informações de um colaborador que identificou erro:

XML do evento S-5001; ([Automação - Configuração - Gerar XML de retorno dos eventos no TAF)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046869313)

XML do evento que o originou (S-1200, S-2299 ou S-2399);

g) Encaminhe uma cópia da tabela V3N, filtrada pelo período de apuração em questão.

h) Encaminhe uma cópia da tabela C8R.

**Documentações relacionadas ao assunto:**

Painel de Conferência de INSS (documentação que explica como gerar o relatório, e as informações contidas nele.)

<https://tdn.totvs.com/pages/releaseview.action?pageId=528452133>
