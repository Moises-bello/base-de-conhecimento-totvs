---
article_id: 360053637214
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: 9dd14a58901e8af7199f2e87edd8c61b5bad9d819c7a9a3743a97f789769c586
fetched_at: '2026-06-28T22:40:40.250203+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - LALUR: M030 COMO GERAR'
type: support-article
updated_at: '2024-10-18T12:31:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053637214-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-LALUR-M030-COMO-GERAR
---

**Dúvida**  
Como gerar Registro M030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**

[CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)  
  
[ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)

* [Orientações Consultoria de Segmentos](http://tdn.totvs.com/pages/releaseview.action?pageId=236430090)
* **O lalur não exporta o [plano de contas (J050)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search) e o [Bloco K](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search) para o TAF, diante disso se faz necessário :**
* **Antes de gerar o Lalur é necessário exportar a****ECF****para o TAF, pois a través da exportação da ECF será gerado o Plano de contas**

1º  CTBS001 Rotina de escrituração -  Exportação ECF para que o sistema exporte o plano de contas e o bloco K  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089646554)

* [Como gerar ECF para o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
* Para gerar com Centro de custo veja :[LALUR - COM CENTRO DE CUSTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046640714-MP-SIGACTB-LALUR-COM-CENTRO-DE-CUSTO?source=search)
* **Obs : necessário que a exportação da ECF seja realizada sem nenhum erro de importação , caso  apresentado algum erro, necessário corrigir ,para que assim conclua a exportação da ECF**
* Para gerar com Centro de custo veja : [ECF - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search)
* [Bloco M - Geração Centro de Custo M300/M310 (Clique aqui)](https://tdn.totvs.com/pages/releaseview.action?pageId=822682054)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27159931632023)

* Verifique se o saldo **[Bloco K](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)  - (Saldos das Contas Contábeis e Referenciais)**foi gerado para a contas que serão posteriormente relacionadas na rotina [TAFA433 Rotina Eventos Tributários](https://tdn.totvs.com/pages/viewpage.action?pageId=248578386)
* [Rotina - TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) (Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL)  
    

  [**Registro K030 - Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoM-e-Laluree-Lacs)

  + Tabelas - CAC (Per.Formas Apur. do IRPJ e CSLL)  / CAH (Período de Apuração)
  + Registro do Layout TOTVS - T087
  + [Rotina - TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) (Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL)

* verifique que ao processar a [ECF o sistema alimento o bloco K](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search)  
    
  + a conta 38010011 possui saldo

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091804153)

* a conta 38010013 possui saldo

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089651014)

2º TAFA060 Rotina de Plano de contas  – Verifique se a contabilidade importou o plano de contas corretamente  
[Veja rotinas e Tabelas (Clique Aqui)](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoP-LucroPresumido)  
3º TAFA050 Rotina Cadastro complemento de empresa  - verifique o cadastro [Parâmetros de Integração CTB/TAF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-?source=search)  
4º [CTBS300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015738232-MP-SIGACTB-CTBS300-ONDE-CADASTRAR-FILTRO-LALUR-?source=search) Rotina Cadastro Lalur- deve ser realizado manualmente

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091805293)

5º CTBS001 Rotina de escrituração -  Exportação Lalur para que o sistema exporte o saldos para o TAF  
6º [TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) – Lançamento contábeis (Do lalur) – sistema integra da rotina de escrituração  verifique se o sistema importou o lançamentos.

O sistema deve levar para a rotina [TAFA331](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209)  o que foi importado no bloco T124AA, na tabela TAFST1

* [Rotina TAFA331](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) sistema levou o saldos

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089652214)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091805333)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089652334)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091805373)

6º [TAFA372 Rotina Cadastro de parâmetros de Abertura ECF](https://tdn.totvs.com/pages/releaseview.action?pageId=379293739) : Verifique se a contabilidade ao gerar  ECF importou  os parâmetros corretamente

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089652674)

7º [TAFA430 Rotina Cadastro de tributos](https://tdn.totvs.com/display/TAF/Cadastro+de+Tributos+-+TAFA430+-+TAF+-+P12) –  realize o cadastrar os impostos manualmente no TAF (Indicado não alterar) 

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089652734)

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089653074)

8º  [TAFA444 Rotina Cadastro do período de apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=269087163) - Realize o cadastro dos períodos manualmente 

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089654314)

9º [TAFA436 Rotina cadastro plano de contas B](http://tdn.totvs.com/display/public/TAF/Conta+da+Parte+B+-+TAFA436+-+TAF+-+P12) - Realize o cadastro  cadastro parte B manualmente (lucro Real)

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091807473)

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091807493)

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089654734)

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091807693)

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089654814)

* **Ao informa as contas  no TAF deve informar contas  analíticas  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404618504471)**

10º [TAFA433 Rotina Eventos Tributários](https://tdn.totvs.com/pages/releaseview.action?pageId=248578386) - Realize o cadastro dos eventos tributários manualmente ,revisar todos os campos e abas 

![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091807793)

![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091807853)

* Relacione as conta que tiveram saldo do lalur  e no bloco K, onde vimos na rotina [TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) que o sistema alimentou   
  38010013  
  38010011
* Informe nas abas os dados necessário (Filial,conta analítica, código Lalur..)

![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089654994)

* Conta aqui cadastrada possui saldo no Lalur e no bloco K

![mceclip25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089655094)

![mceclip26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089655194)

![mceclip27.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091808493)

11º   [TAFA438 Cadastro de Vigência do Evento tributário](https://tdn.totvs.com/pages/viewpage.action?pageId=245170511) : Realize o cadastro manualmente 

![mceclip28.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091809373)

12º [TAFA433 Rotina cadastro de eventos tributário](https://tdn.totvs.com/pages/releaseview.action?pageId=248578386) : Realize a simulação da apuração (outras ações > simulação) e verifique se a apuração simulada esta correta 

![mceclip29.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089656654)

* Confira se os saldos apresentados estão corretos

![mceclip30.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089656694)

![mceclip31.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091809873)

![mceclip32.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091809893)

13º [TAFA444 Rotina Cadastro do período de apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=269087163) : Realize o encerramento do período , posteriormente (outras ações >gerar documento de arrecadação) e baixar

* Realizei o encerramento

![mceclip33.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091809953)

![mceclip34.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089656894)

* Status vai mudar para encerrado

![mceclip39.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089657174)

* Gere o documento de arrecadação

![mceclip35.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091810013)

* Selecione o Cod.Receita

![mceclip36.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091810053)

![mceclip37.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089657014)

* Realize a baixa

![mceclip38.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089657054)

![mceclip40.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089658374)

![mceclip41.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089658514)

14º [TAFA444 Rotina Cadastro do período de apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=269087163) :Realize o envio do dados para a ECF (Outras ações > enviar para ECF) (será gerado do [TAFA322](https://tdn.totvs.com/pages/viewpage.action?pageId=189308187))

* Acessei a rotina [TAFA322](https://tdn.totvs.com/pages/viewpage.action?pageId=189308187) antes de enviar para a ECF - veja que não existe dados lá dessa apuração

![mceclip42.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091812053)

* Realizei o envio para a ECF

![mceclip43.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091812093)

![mceclip44.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091812153)

* Acessei a rotina [TAFA322](https://tdn.totvs.com/pages/viewpage.action?pageId=189308187) após de enviar para a ECF - veja que o sistema gerou

![mceclip45.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089658754)

* Através da rotina TAFOBRIG  gere a  revisão  e veja que o sistema gerou na ECF bloco do LALUR

![mceclip46.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089658834)
