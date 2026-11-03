---
article_id: 360010318251
category: Contabilidade Gerencial - IRPJ e CSLL no FINA960
content_hash: 5ea3da548ef4954d6185fbbcf016decc6b8c1ee68bc99fa011427234a8fd868d
fetched_at: '2026-06-28T22:40:56.076405+00:00'
product: protheus
section_id: 1500001537481
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB-  IRPJ e CSLL COMO CONFIGURAR
  O LUCRO PRESUMIDO NO TAF '
type: support-article
updated_at: '2024-05-13T12:27:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010318251-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-IRPJ-e-CSLL-COMO-CONFIGURAR-O-LUCRO-PRESUMIDO-NO-TAF
---

**Dúvida**LUCRO PRESUMIDO TAF - TELAS PARA PREENCHIMENTO.  
Lucro presumido – Apuração manual.

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Requisitos Imprescindíveis**

* [Atualização do ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-MP-SIGACTB-ECF-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ECF-?source=search)
* [Atualização TAF Completo.](https://tdn.totvs.com/pages/viewpage.action?pageId=374311673)

* [Orientações Consultoria de Segmentos](http://tdn.totvs.com/pages/releaseview.action?pageId=236430090)
* **O lalur não exporta o [plano de contas (J050)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search) e o [Bloco K](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search) para o TAF, diante disso se faz necessário :**
* **Antes de gerar o Lalur é necessário****exportar a ECF****para o TAF, pois a través da exportação da ECF será gerado o Plano de contas**
* CTBS001 Rotina de escrituração -  Exportação ECF para que o sistema exporte o plano de contas
* Realizar a [Apuração de resultado Trimestralmente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
* Possuir o [Calendário Contábil trimestra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024569414-MP-SIGACTB-ECF-CADASTRO-DE-CALEND%C3%81RIO-CONTABIL?source=search)l
* **Importante** : [Recuperação de ECD Com Encerramento do Exercício Diferente dos Encerramentos da ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026080413-MP-SIGACTB-ECF-Recupera%C3%A7%C3%A3o-de-ECD-Com-Encerramento-do-Exerc%C3%ADcio-Diferente-dos-Encerramentos-da-ECF?source=search)
* Para gerar com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search) necessário está devidamente cadastrado e apurado
* Para gerar com Centro de custo veja :[LALUR - COM CENTRO DE CUSTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046640714-MP-SIGACTB-LALUR-COM-CENTRO-DE-CUSTO?source=search)

**Solução**

Em caso de tratar os valores de Apuração de Lucro Presumido segue os passos das rotinas que devem ser preenchidas .

* Gerar a [ECF para o Lucro presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
* **Obs : necessário que a exportação da ECF seja realizada sem nenhum erro de importação , caso  apresentado algum erro, necessário corrigir ,para que assim conclua a exportação da ECF**
* Verifique se o saldo **[Bloco K](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)  - (Rotina TAFA311 - Saldos das Contas Contábeis e Referenciais)**foi gerado para a contas que serão posteriormente relacionadas na rotina [TAFA433 Rotina Eventos Tributários ,](https://tdn.totvs.com/pages/viewpage.action?pageId=248578386)caso o Bloco K não tenha sido gerado veja [Bloco K COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search)

* [Rotina - TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) (Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23441136762903)

 Cadastro Lalur-  [CTBS300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015738232-MP-SIGACTB-CTBS300-ONDE-CADASTRAR-FILTRO-LALUR-?source=search)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23441136772631)

 Exportação Lalur- CTBS001 - Realiza a exportação do Lalur

Obs. Caso o plano de contas ou alguma conta NOVA não tenha sido integrada com o TAF , deverá haver primeiramente a exportação da ECF, para integração do plano de contas, e posteriormente a exportação do Lalur.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23441090929047)

* Verifique se os [Lançamentos Contábeis do Lalur Rotina TAFA331](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209)foram gerado para a contas que serão posteriormente relacionadas na rotina [TAFA433 Rotina Eventos Tributários](https://tdn.totvs.com/pages/viewpage.action?pageId=248578386)
* [ECF Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23441136795799)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23441136801431)

[Cadastro de Tributo (TAFA430](https://tdn.totvs.com/display/public/TAF/Cadastro+de+Tributos+-+TAFA430+-+TAF+-+P12)) - Informe os campos obrigatórios

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043093754)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043094934)

 Em seguida, no Cadastro do [Período de Apuração (TAFA444),](https://tdn.totvs.com/pages/releaseview.action?pageId=269087163) amarrar ao cadastro de tributo, informando os campos obrigatórios

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043936333)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043095534)

[EVENTO TRIBUTÁRIO (TAFA433)](https://tdn.totvs.com/pages/releaseview.action?pageId=248578386)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043936773)

Na Aba Identificação preencher os campos obrigatórios

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043937093)

Nas Abas "Regras Tributárias" serão definidas todas as bases de cálculos necessárias para correta apuração do lucro Presumido (deverá ser cadastrado manualmente).

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043936873)

[Vigência (TAFA438)](https://tdn.totvs.com/pages/releaseview.action?pageId=245170511)

Nesta rotina será definido o período vigente, para o cálculo da apuração, informe os campos obrigatórios

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043096654)

Na rotina Cadastro do [Período de Apuração (TAFA444),](https://tdn.totvs.com/pages/releaseview.action?pageId=269087163) em Ações Relacionadas, Encerramento Período. Para então apurar os valores.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043937413)

Em Outras ações:

Gerar guia arrecadação.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043937533)

Visualize na aba Guia de foi gerado

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043937573)

Veja mais :

[MP\_SIGACTB LALUR/LACS: CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)

[MP-SIGACTB - ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)

[MP - SIGACTB - ECF - Bloco M - Apuração IRPJ/CSLL para Lucro Real (TAFA322)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004874591-MP-SIGACTB-ECF-Bloco-M-Apura%C3%A7%C3%A3o-IRPJ-CSLL-para-Lucro-Real-TAFA322-?source=search).

[MP- SIGACTB :TAF LALUR AJUSTE ANUAL ROTINA TAFA444 NÃO EXISTE UMA VIGÊNCIA CADASTRADA ABRANGENDO ESTE PERIODO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025396692-MP-SIGACTB-TAF-LALUR-AJUSTE-ANUAL-ROTINA-TAFA444-N%C3%83O-EXISTE-UMA-VIG%C3%8ANCIA-CADASTRADA-ABRANGENDO-ESTE-PERIODO?source=search)

[MP\_SIGACTB LALUR E LACS: LUCRO PRESUMIDO REGIME DE CAIXA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018333372-MP-SIGACTB-LALUR-E-LACS-LUCRO-PRESUMIDO-REGIME-DE-CAIXA-?source=search)

[MP - Cálculo de CSLL e IRPJ - Empresa Lucro Presumido - Trimestral - SIGACTB X SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133373-MP-C%C3%A1lculo-de-CSLL-e-IRPJ-Empresa-Lucro-Presumido-Trimestral-SIGACTB-X-SIGATAF?source=search)

[MP - SIGACTB - ECF TAFA433 - Compensação do Prejuízo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035081174-MP-SIGACTB-ECF-TAFA433-Compensa%C3%A7%C3%A3o-do-Preju%C3%ADzo?source=search)

[MP\_SIGACTB :TAF-Controle do PAT na Parte B do LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037249374-MP-SIGACTB-TAF-Controle-do-PAT-na-Parte-B-do-LALUR?source=search)
