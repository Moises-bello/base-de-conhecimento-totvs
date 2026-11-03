---
article_id: 360035133373
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: 99d3b2bd735a445348ac3c786c484f3686391dfc706b10df09d415444388d361
fetched_at: '2026-06-28T22:40:40.199361+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB  Cálculo de CSLL e IRPJ
  - Empresa Lucro Presumido trimestral
type: support-article
updated_at: '2025-05-14T18:00:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133373-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-C%C3%A1lculo-de-CSLL-e-IRPJ-Empresa-Lucro-Presumido-trimestral
---

**Dúvida**Como Calcular a CSLL e IRPJ de uma empresa lucro presumido trimestral  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução:**

**Premissa:** O módulo SIGATAF ([Totvs Automação Fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-MP-SIGACTB-ECF-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ECF-?source=search)) esteja implantado, atualizado e comunicando com o ERP Protheus, caso contrário os dados não serão integrados.

**Apuração do IRPJ e CSLL**

**[Roteiro de cadastros e parametrizações para apuração do LALUR/LACS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404191850135-Cross-Segmento-Backoffice-Linha-Protheus-TAF-Roteiro-de-cadastros-e-parametriza%C3%A7%C3%B5es-para-apura%C3%A7%C3%A3o-do-LALUR-LACS?source=search)**

* **O lalur** **NÃO** **exporta o** [**plano de** **contas J050**](https://tdn.totvs.com/pages/releaseview.action?pageId=284465420) **para o TAF, diante disso se faz necessário :**
* **Antes** de gerar o Lalur é necessário **exportar a ECF** para o TAF, pois a través da exportação da ECF será gerado o Plano de contas
* Realize a [exportação ECF Regime tributário Lucro Presumido para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)  
  Obs : necessário que a exportação da ECF seja realizada sem nenhum erro de importação , caso  apresentado algum erro, necessário corrigir ,para que assim conclua a exportação da ECF
* [Veja rotinas e Tabelas (Clique Aqui)](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoP-LucroPresumido)
* Para gerar com Centro de custo veja : [ECF - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search)
* [CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)

**1. CTBS001 -** Necessário importar revisão da ECF para  o TAF através da Rotina de escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32103025946263)

# 

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19225194408855)Caso esteja gerando [LUCRO PRESUMIDO REGIME DE CAIXA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018333372-MP-SIGACTB-LALUR-E-LACS-LUCRO-PRESUMIDO-REGIME-DE-CAIXA-?source=search)****-**

* Veja no manual da receita o conceito e conseguencias ao preencher a perguntas abaixo, ao gerar a ECF

[TIP\_ESP\_PRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125451-MP-SIGACTB-ECF-Bloco-Q?source=search)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32103009817879)

IND\_REC\_RECEITA

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32103009819159)

 

**2. CTBS300** - Rotina Cadastro Lalur

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044911174)

Esse cadastro deverá ocorrer por período de apuração. É o cadastro que será responsável em levar os movimentos do período para o TAF(TAFA331), através da rotina CTBS001.

**3. CTBS001** - Gerar uma revisão para o Lalur e para a ECF

* Necessário importar revisão do Lalur para TAF através da Rotina de escrituração (CTBS001)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32103009819927)

* Tabelas alimentadas ao exportar o lalur [CSA e CSB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)
* na Tabela TAFST1 o registro importado é o  T124
* posteriormente o sistema alimenta a rotina TAFA331

Quando gerar essas revisões e integrar ao TAF, o Lalur irá gerar os [movimentos(TAFA331)](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) e a ECF os cadastros básicos(TAFA372, TAFA060, TAFA061, [TAFA311)](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209). Esse procedimento será feito trimestralmente, para garantir que todos os saldos e movimentos sejam integrados ao TAF e componham a base de cálculo da CSLL e do IRPJ.

Obs.: Recomendo ter um calendário contábil para cada período de forma separada, assim iremos garantir que somente os saldos(TAFA311) do respectivo trimestre seja integrado para o TAF.

Esse procedimento terá que ser feito trimestralmente.

**4. TAFA430** - Cadastro Manual, deve ser inserido diretamente no TAF. Esse cadastro será a base para a definição da presunção e da alíquota do imposto, além do excedente no caso do IRPJ. Deverá ter um cadastro para cada imposto.

Abaixo a CSLL de uma empresa de comércio, com alíquota de 9% e presunção de 12%.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044915854)

**IRPJ -** No caso do IRPJ é possível calcular o valor do imposto com base na presunção de 8% e o excedente, quando essa presunção ultrapassar R$60.000,00. Quando ultrapassar, deverá calcular 10% ao excedente. ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045775893)

**5. TAFA444** - Rotina de Cadastro de Período de Apuração - Esse cadastro deve ocorrer de forma manual, por trimestre, e por imposto. Ao final de 1 ano, teremos 8 registros, 4 para CSLL e 4 para o IRPJ.

**CSLL**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044917694)

**IRPJ -** Nesse caso, é possível cadastrar a presunção(8%), alíquota(15%) e adicional(10%) caso a presunção ultrapasse R$60.000,00. Observe que os R$60.000,00 esta representado em valor mensal, ou seja, R$20.000,00, perfazendo o total de 60.000,00 ao final do trimestre:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045777593)

**6. [TAFA433 Rotina Eventos Tributários](https://tdn.totvs.com/pages/viewpage.action?pageId=248578386)** -Inclusão manual, por imposto e por período. É nesse rotina que serão informadas as contas que irão compor a base de cálculo para os impostos e a sua origem, se Parte B ou Conta Contábil. Como estamos tratando de empresa de Lucro Presumido, não existe Parte B do Lalur, ou seja, informe Conta Contábil:

* **Ao informa as contas  no TAF deve informar contas  analíticas  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19225194408855)**
* Deve ser amarrada somente conta analítica as conta sintéticas não deve ser amarradas
* Verifique se a contas que serão relacionadas aqui possui saldo na rotinas [Lançamentos Contábeis do Lalur Rotina TAFA331](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) e **[Bloco K (ECF)](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)**[Rotina - TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209)
* Porem caso a conta esteja cadastrada aqui necessário que tenha saldo na duas rotinas  : [Lançamentos Contábeis do Lalur Rotina TAFA331](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) e **[Bloco K (ECF)](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)**[Rotina - TAFA311 ,](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209)caso o Bloco K não tenha sido gerado veja [Bloco K COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044927434)

Caso seja necessário informar alguma exclusão da receita, é nessa rotina que deve ser feito.

**7. TAFA438** - Cadastro da Vigência do Evento Tributário - Cadastro por imposto e por período. Estará associado ao Evento Tributário(TAFA433). A rotina só tem a finalidade de delimitar o período considerado para o cálculo dos impostos.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045804013)

**Simulação de Cálculo dos Impostos:**

**TAFA433** - Em Outras Ações é possível simular de apuração dos impostos.

**Simulação de calculo da CSLL com base em uma receita de R$900.000,00**

Presunção: 900.000 \* 12% = 108.000

CSLL: 108.000 \* 9% = 9.720

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045814893)

**Simulação de calculo da IRPJ com base em uma receita de R$900.000,00**

Presunção: 900.000 \* 8% = 72.000

IRPJ: 72.000 \* 15% = 10.800

IRPJ do excedente = 72.000 - 60.000 = 12.000 \* 10% = 1.200

Total de IRPJ = 10.800 + 1.200 = 12.000

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044953614)

Estando tudo correto, através da rotina TAFA444, em Outras Ações, é possível Encerrar Período e Gerar Documento de Arrecadação. Só é possível gerar o Documento de Arrecadação caso o período esteja encerrado.

É na geração do documento de arrecadação que o Código de Receita será informado. No caso do IR código 2089 e CSLL 2372.

Os valores e guias estarão detalhados ao visualizar o período de apuração nas abas "Apuração" e "Guias"

**CSLL:**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045816473)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044954534)

**IRPJ:**

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045816653)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044954794)

Algumas considerações importante: Os dados acima são fictícios, baseados em um cenário de uma empresa de comércio. Para cada ramo de atividade existem suas regras e peculiaridades. Portanto, sempre consulte seu contador.

Saiba mais :

[MP - SIGACTB - COMO CONFIGURAR O LUCRO PRESUMIDO NO TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010318251-MP-SIGACTB-COMO-CONFIGURAR-O-LUCRO-PRESUMIDO-NO-TAF-?source=search)

[MP-SIGACTB - ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)

[MP\_SIGACTB LALUR/LACS: CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)

[MP - SIGACTB - ECF TAFA433 - Compensação do Prejuízo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035081174-MP-SIGACTB-ECF-TAFA433-Compensa%C3%A7%C3%A3o-do-Preju%C3%ADzo?source=search)

[MP-SIGACTB - ECF Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)

[MP - SIGACTB - ECF/TAF - Apuração IRPJ e CSLL não grava lançamentos das regras tributárias. O que fazer?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012563511-MP-SIGACTB-ECF-TAF-Apura%C3%A7%C3%A3o-IRPJ-e-CSLL-n%C3%A3o-grava-lan%C3%A7amentos-das-regras-tribut%C3%A1rias-O-que-fazer-?source=search)
