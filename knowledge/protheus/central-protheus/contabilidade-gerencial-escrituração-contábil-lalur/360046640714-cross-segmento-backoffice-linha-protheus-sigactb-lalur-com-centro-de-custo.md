---
article_id: 360046640714
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: 49785afda290c682d197f05518c14577350327043e0093a610995bad5caca5a0
fetched_at: '2026-06-28T22:40:40.233261+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - LALUR - COM CENTRO DE
  CUSTO
type: support-article
updated_at: '2024-11-14T14:19:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046640714-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-LALUR-COM-CENTRO-DE-CUSTO
---

**Dúvida**

Com gerar o Centro de custo no Lalur  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Requisitos Imprescindíveis**

* [Atualização do ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-MP-SIGACTB-ECF-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ECF-?source=search)
* [Atualização TAF Completo.](https://tdn.totvs.com/pages/viewpage.action?pageId=374311673)
* [Bloco M - Geração Centro de Custo M300/M310 (Clique aqui)](https://tdn.totvs.com/pages/releaseview.action?pageId=822682054)  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27159981131543)

**Solução**

**1-**  Realize os passos : [ECF - Centro de Custo ,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-MP-SIGACTB-ECF-Centro-de-Custo?source=search)pois para gerar o centro de custo do Lalur necessário gerar o centro de custo no ECF

**2-** Ao fazer a importação dos arquivos LALUR para o TAF,  necessário que no  cadastro na rotina  CTBS300  tenha sido informado centro de custo  
  
![](https://totvssuporte.zendesk.com/attachments/token/bfxYQQklKJI7lLlUkT4avdrbG/?name=inline-1123647185.png)  
  
**3-** Ao fazer a importação dos arquivos LALUR para o TAF, deve-se selecionar a pergunta "Processa C. Custo" como Sim na rotina de Central de Escrituração(CTBS001), conforme imagem abaixo  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072087173)​​  
  
**4-** CTBS300 Rotina Cadastro Lalur- Realize o cadastro e informe o centro de custo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069781534)  
**5-**CTBS001 Rotina de escrituração -  Exportação ECF para que o sistema exporte o plano de contas

* [Como gerar o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)

Ao fazer a importação dos arquivos ECF para o TAF, deve-se selecionar a pergunta "Processa C. Custo" como Sim na rotina de Central de Escrituração(CTBS001), conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27161306021783)

**6-**TAFA050 Rotina Cadastro complemento de empresa  - verifique o cadastro  :[ECF - Parâmetros de Integração CTB/TAF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-?source=search)  
**7-** TAFA060 Rotina de Plano de contas  – Verifique se a contabilidade importou o plano de contas e o **centro de custo** corretamente  
![](https://totvssuporte.zendesk.com/attachments/token/sfYzVPe6PWtv8uUyKvO4aPFTw/?name=inline1603700287.png)​  
**8-** CTBS001 Rotina de escrituração -  Exportação Lalur para que o sistema exporte o saldos para o TAF

Ao fazer a importação dos arquivos LALUR para o TAF, deve-se selecionar a pergunta "Processa C. Custo" como Sim na rotina de Central de Escrituração(CTBS001), conforme imagem abaixo

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072087173)  
**9-**[TAFA331 – Lançamento contábeis (Do lalur)](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) – sistema integra da rotina de escrituração  verifique se o sistema importou o lançamentos com **centro de custo,** caso possua mais de um centro de custo informe mais de uma linha  
  
**![](https://totvssuporte.zendesk.com/attachments/token/5PJoKr4FtmY2yVD07cuC3cURB/?name=inline-451938166.png)​****10-**[TAFA372 Rotina Cadastro de parâmetros de Abertura ECF](https://tdn.totvs.com/pages/viewpage.action?pageId=200904478) : Verifique se a contabilidade importou  os parâmetros corretamente ( [Reg 0010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-MP-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO?source=search)  
**11-** [TAFA430 Rotina Cadastro de tributos](https://tdn.totvs.com/display/TAF/Cadastro+de+Tributos+-+TAFA430+-+TAF+-+P12) –  realize o cadastrar os impostos manualmente no TAF (Indicado não alterar)   
**12-[TAFA444 Rotina Cadastro do período de apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=269087163)**- Realize o cadastro dos períodos manualmente   
**13-** [TAFA436 Rotina cadastro plano de contas B](https://tdn.totvs.com/display/TAF/Conta+da+Parte+B+-+TAFA436+-+TAF+-+P12) - Realize o cadastro  cadastro parte B manualmente   
**14-** [TAFA433 Rotina Eventos Tributários](https://tdn.totvs.com/pages/viewpage.action?pageId=248578386)-  Foi implementado um facilitador, para que não seja necessário cadastrar todas as combinações Conta Contábil + Centro de Custo no Evento Tributário (TAFA433). Basta informar somente a linha com a conta contábil com o centro de custo vazio, que o sistema irá buscar todos os centros custos cadastrados em Saldos Contábeis (TAFA311) x Lançamentos Contábeis (TAFA331), dessa forma irá compor na apuração e no arquivo final  da ECF a quebra por centro de custo no bloco M310 

[Para mais detalhe Veja:Bloco M - Geração Centro de Custo M300/M310](https://tdn.totvs.com/pages/releaseview.action?pageId=822682054)

Diante não é necessário o preenchimento do campo de centro de custo no cadastro , porem caso ja possua o cadastro o sistema irá ter o comportamento correto também.  
  
![](https://totvssuporte.zendesk.com/attachments/token/8ipUfQziSHExw0ter7kEUimJE/?name=inline-892605904.png)​​  
**15-**  [TAFA438 Cadastro de Vigência do Evento tributário](https://tdn.totvs.com/pages/viewpage.action?pageId=245170511)  : Realize o cadastro manualmente   
**16-** [TAFA433 Rotina Cadastro de Eventos Tributários](https://tdn.totvs.com/pages/viewpage.action?pageId=248578386) : Realize a [Simulação da Apuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search) (outras ações > simulação) e verifique se a apuração simulada esta correta   
Veja mais :   
  
**17-** **[TAFA444 Rotina Cadastro do período de apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=269087163)** : Realize o encerramento do período , posteriormente (outras ações >gerar documento de arrecadação) e baixar

**18-[TAFA444 Rotina Cadastro do período de apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=269087163)** :Realize o envio do dados para a ECF (Outras ações > enviar para ECF) (será gerado do TAFA322)

 Saiba mais:

* [MP\_SIGACTB LALUR/LACS: CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)
* [Obrigação ECF - Escrituração Contábil Fiscal](http://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoP-LucroPresumido)
* [Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)
* [Apuração do IRPJ e da CSLL(LALUR e LACS)](http://tdn.totvs.com/pages/releaseview.action?pageId=274832267)
* [ECF Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)
* [Cálculo de CSLL e IRPJ - Empresa Lucro Presumido - Trimestral - SIGACTB X SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133373-MP-C%C3%A1lculo-de-CSLL-e-IRPJ-Empresa-Lucro-Presumido-Trimestral-SIGACTB-X-SIGATAF?source=search)
* [ECF TAFA433 - Compensação do Prejuízo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035081174-MP-SIGACTB-ECF-TAFA433-Compensa%C3%A7%C3%A3o-do-Preju%C3%ADzo?source=search)
* **[MP-SIGACTB - ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)**
* [Tabelas Relacionadas a Apuração IRPJ CSLL no TAF (Lalur)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034815894-MP-SIGACTB-ECF-Tabelas-Relacionadas-a-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-Lalur-?source=search)
* [Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)
* [TAFA433 apuração  de IRPJ e CSLL o TAF saldo "Imposto Devido Meses Anteriores" cumulativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035535754-MP-SIGACTB-ECF-TAFA433-apura%C3%A7%C3%A3o-de-IRPJ-e-CSLL-o-TAF-saldo-Imposto-Devido-Meses-Anteriores-cumulativo-?source=search)
* [Controle do PAT na Parte B do LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037249374-MP-SIGACTB-TAF-Controle-do-PAT-na-Parte-B-do-LALUR?source=search)
