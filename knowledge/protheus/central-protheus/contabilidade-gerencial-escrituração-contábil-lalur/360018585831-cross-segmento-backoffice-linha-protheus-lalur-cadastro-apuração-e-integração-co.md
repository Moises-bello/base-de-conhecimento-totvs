---
article_id: 360018585831
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: 6ffcbe3b3ef99151772b19888614a90bcb71091ad644f82832548e6722bfbe3b
fetched_at: '2026-06-28T22:40:40.271060+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Lalur - Cadastro, apuração e integração
  com o ecf
type: support-article
updated_at: '2025-06-24T18:22:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-Cross-Segmento-Backoffice-Linha-Protheus-Lalur-Cadastro-apura%C3%A7%C3%A3o-e-integra%C3%A7%C3%A3o-com-o-ecf
---

**Dúvida**Passo a passo para cadastrar LALUR?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80

**Solução**  
**Apuração do IRPJ e CSLL**

* [Orientações Consultoria de Segmentos](http://tdn.totvs.com/pages/releaseview.action?pageId=236430090)
* [ECF LALUR (vídeos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)
* O lalur não exporta o [plano de contas (J050)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search) e o [Bloco K](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search) para o TAF, diante disso se faz necessário :
* Antes de gerar o Lalur é necessário exportar a ECF para o TAF, pois a través da exportação da ECF será gerado o Plano de contas
* CTBS001 Rotina de escrituração -  Exportação ECF para que o sistema exporte o plano de contas  
  + [Como gerar o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
  + [Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)
  + [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
  + Após importar a revisão da ECF  Verifique se a contabilidade importou  os parâmetros corretamente o [Registro 0010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-MP-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO?source=search) através da rotina [TAFA372 Cadastro de parâmetros de Abertura ECF](https://tdn.totvs.com/pages/viewpage.action?pageId=200904478) :
  + Para gerar com Centro de custo veja :[LALUR - COM CENTRO DE CUSTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046640714-MP-SIGACTB-LALUR-COM-CENTRO-DE-CUSTO?source=search)
* Obs : necessário que a exportação da ECF seja realizada sem nenhum erro de importação , caso  apresentado algum erro, necessário corrigir ,para que assim conclua a exportação da ECF
* Verifique se o saldo [Bloco K](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)  - (Saldos das Contas Contábeis e Referenciais) foi gerado para a contas que serão posteriormente relacionadas na rotina [TAFA433 Rotina Eventos Tributários](https://tdn.totvs.com/pages/viewpage.action?pageId=248578386),caso o Bloco K não tenha sido gerado veja [Bloco K COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search)
* [Rotina - TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) (Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090934713)

1. Cadastro Lalur-  [CTBS300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015738232-MP-SIGACTB-CTBS300-ONDE-CADASTRAR-FILTRO-LALUR-?source=search)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013917331)

2. Exportação Lalur- CTBS001

* Tabelas [CSA e CSB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)são alimentadas ao exportar o lalur para o TAF

Obs. Caso o plano de contas ou alguma conta NOVA não tenha sido integrada com o TAF , deverá haver primeiramente a exportação da ECF, para integração do plano de contas, e posteriormente a exportação do Lalur.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013934672)

* Verifique se os [Lançamentos Contábeis do Lalur Rotina TAFA331](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209)foram gerado para a contas que serão posteriormente relacionadas na rotina [TAFA433 Rotina Eventos Tributários](https://tdn.totvs.com/pages/viewpage.action?pageId=248578386)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088794774)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088794814)

3. [TAFA430 Rotina Cadastro de tributos](https://tdn.totvs.com/display/TAF/Cadastro+de+Tributos+-+TAFA430+-+TAF+-+P12)

Obs: deve ser informada contas analística , pois ao informar as contas sintéticas o sistema não irá realizar a apuração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013950911)

4. [TAFA444 Rotina Cadastro do período de apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=269087163)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013934912)

* **Ao informa as contas  no TAF deve informar contas  analíticas  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16244107216023)**

5. [TAFA433 Rotina Eventos Tributários](https://tdn.totvs.com/pages/viewpage.action?pageId=248578386)

* Deve ser amarrada somente conta analítica as conta sintéticas não deve ser amarradas
* Verifique se a contas que serão relacionadas aqui possui saldo na rotinas [Lançamentos Contábeis do Lalur Rotina TAFA331](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) e **[Bloco K (ECF)](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)**[Rotina - TAFA311](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209)
* Porem caso a conta esteja cadastrada aqui necessário que tenha saldo na duas rotinas  : [Lançamentos Contábeis do Lalur Rotina TAFA331](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) e **[Bloco K (ECF)](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)**[Rotina - TAFA311 ,](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209)caso o Bloco K não tenha sido gerado veja [Bloco K COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013935072)

6. [TAFA433 Rotina Eventos Tributários](https://tdn.totvs.com/pages/viewpage.action?pageId=248578386)

- Parte B

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013951631)

7. [TAFA438 Cadastro de Vigência do Evento tributário](https://tdn.totvs.com/pages/viewpage.action?pageId=245170511)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013935172)

8. [TAFA443 Cadastro de Eventos Especiais](http://tdn.totvs.com/display/public/TAF/Cadastro+de+Eventos+Especiais+-+TAFA443+-+TAF+-+P12)

Para que o sistema permita a inclusão de um Evento Especial (Cisão, fusão, incorporação..) na rotina de Cadastro de Apuração (TAFA444) é necessário o cadastro de Evento Especial (TAFA443).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013935432)

**Importante para o ECF**

10. [TAFA436 Rotina cadastro plano de contas B](http://tdn.totvs.com/display/public/TAF/Conta+da+Parte+B+-+TAFA436+-+TAF+-+P12)

Cadastrar somente o período.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013936692)

Obs: O Bloco M - Identificação da Conta na Parte B do e-Lalur e do e-Lacs trata-se de um cadastro de informações referentes a identificação das Contas na Parte B do e-Lalur e do e-Lacs para empresas enquadradas pelo Lucro Real previstos pelo Ato Declaratório Executivo Cofis nº 60, de 26 de agosto de 2015, através do Manual de Orientação da ECF.

Para mais detalhes : [Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=201730475) e [Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=244434240)

11. [Gerar Documento de Arrecadação](https://tdn.totvs.com/pages/releaseview.action?pageId=269087163#) ou através da rotina [Documento de Arrecadação - TAFA027.](http://tdn.totvs.com.br/pages/viewpage.action?pageId=271166621)

**Outras Ações/ Gerar Documento de Arrecadação**

Posicione sobre o registro que deseja gerar e clique nessa opção.

O sistema mostra a tela com os campos:

* **Cod. Receita,** que dará opção de escolha dos códigos ( F3 )
* **Vencimento,** deverá ser preenchido conforme data de vencimento da guia.

O sistema exibe a tela de progresso da ação e ao término clique em **Finalizar.**

Obs.: Essa opção gera uma guia de recolhimento que poderá ser visualizada, baixada ou estornada na opção "Visualizar/Aba Guias" da tela principal do programa.

![](https://totvssuporte.zendesk.com/attachments/token/LISPwCrVnIqOhPYrHf5AqFYr6/?name=inline1297666067.png)

![](https://totvssuporte.zendesk.com/attachments/token/4ro5NPYsIsS7I4UWDHNwn0y06/?name=inline-868549507.png)  
![](https://totvssuporte.zendesk.com/attachments/token/s9TQl7h1ygNz893xR7Kj9fbKG/?name=inline-1769585424.png)  
![](https://totvssuporte.zendesk.com/attachments/token/Hmpmf6AXfgtFiuAVv0eUvD6ft/?name=inline202965775.png)  
   
Realize a baixa  
![](https://totvssuporte.zendesk.com/attachments/token/C7vPSeMN6oa385YbQLcab7P0u/?name=inline-734143595.png)  
![](https://totvssuporte.zendesk.com/attachments/token/D9WhMEX3cKuEAEF5I9H6Oxr57/?name=inline800215747.png)  
![](https://totvssuporte.zendesk.com/attachments/token/ymGSzxy4eD4Xy0FKOQUuYVmgJ/?name=inline-563307192.png)![](https://totvssuporte.zendesk.com/attachments/token/Mi9WElLQVNjHtiLagQuYdOCcW/?name=inline-1921563461.png)

12. [TAFA444 Rotina Cadastro do período de apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=269087163)

Ações relacionadas + Encerrar período

Ações relacionadas + Enviar para ECF

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013936832)

13. [TAFA322 Identificação dos períodos e formas de apuração do IRPJ](https://tdn.totvs.com/pages/viewpage.action?pageId=189308187)

Sistema irá integrar automaticamente a rotina  após realizar os passos abaixo :

Através da Rotina Cadastro Período de apuração (TAFA444) (Encerramento > Enviar para ECF )

* O sistema irá criar  os registros   (A01, A02... Ou T01,T02...) automaticamente na rotina [TAFA322](https://tdn.totvs.com/pages/viewpage.action?pageId=189308187)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013935532)

14. Apuração IRPJ/CSLL- TAFA319

Sistema irá integrar automaticamente a rotina  após realizar os passos abaixo :

Através da Rotina Cadastro Período de apuração (TAFA444) (Encerramento > Enviar para ECF )

* O sistema irá criar os registros  (A01, A02... Ou T01,T02...) automaticamente na rotina TAFA319.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013952031)

 

 Veja mais :

* Rotina de cada bloco :

[Obrigação ECF - Escrituração Contábil Fiscal](http://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoP-LucroPresumido)

* [Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)
* [Apuração do IRPJ e da CSLL(LALUR e LACS)](http://tdn.totvs.com/pages/releaseview.action?pageId=274832267)
* [ECF Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)
* [Cálculo de CSLL e IRPJ - Empresa Lucro Presumido - Trimestral - SIGACTB X SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133373-MP-C%C3%A1lculo-de-CSLL-e-IRPJ-Empresa-Lucro-Presumido-Trimestral-SIGACTB-X-SIGATAF?source=search)
* [ECF TAFA433 - Compensação do Prejuízo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035081174-MP-SIGACTB-ECF-TAFA433-Compensa%C3%A7%C3%A3o-do-Preju%C3%ADzo?source=search)
* [LALUR - COM CENTRO DE CUSTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046640714-MP-SIGACTB-LALUR-COM-CENTRO-DE-CUSTO?source=search)

**Saiba mais**

[MP-SIGACTB - ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)

[Tabelas Relacionadas a Apuração IRPJ CSLL no TAF (Lalur)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034815894-MP-SIGACTB-ECF-Tabelas-Relacionadas-a-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-Lalur-?source=search)

[Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)

[TAFA433 apuração  de IRPJ e CSLL o TAF saldo "Imposto Devido Meses Anteriores" cumulativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035535754-MP-SIGACTB-ECF-TAFA433-apura%C3%A7%C3%A3o-de-IRPJ-e-CSLL-o-TAF-saldo-Imposto-Devido-Meses-Anteriores-cumulativo-?source=search)

[Controle do PAT na Parte B do LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037249374-MP-SIGACTB-TAF-Controle-do-PAT-na-Parte-B-do-LALUR?source=search)

[COMPARTILHAMENTO TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-TABELAS-ECD-E-ECF-COMPARTILHAMENTO)

**Vídeos How to :**

**[How To CONTABILIDADE GERENCIAL - Suporte Técnico Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=758499600)**

[HOW TO - Protheus ECF - Cadastro Filtro LALUR](https://www.youtube.com/watch?v=PQQQ8lloVXI)

[HOW TO - Protheus ECF - Gerando Escrituração Lalur](https://www.youtube.com/watch?v=aAmoeGyp7YE)

[HOW TO - TAF - Cadastrando períodos de apuração](https://www.youtube.com/watch?v=202OeC_OYJU)

[HOW TO - TAF - Configurando os tributos](https://www.youtube.com/watch?v=iX4R909qT6Q)

[HOW TO - TAF - Cadastrando a vigência](https://www.youtube.com/watch?v=VskAPLWZ_dU)

[HOW TO - TAF - Cadastrando contas parte B](https://www.youtube.com/watch?v=XZ-np41TSzI)

[HOW TO - TAF - Incluindo lançamentos automáticos - Contas Lalur parte B](https://www.youtube.com/watch?v=1gi8X7IMCSo)

[HOW TO - TAF - Cadastrando Evento Tributário - parte 01](https://www.youtube.com/watch?v=DgtRxdJIGpg)

[HOW TO - TAF - Cadastrando Evento Tributário - parte 02](https://www.youtube.com/watch?v=riiecnHCtIc)

[HOW TO - TAF - Cadastrando Evento Tributário - parte 03](https://www.youtube.com/watch?v=JvCELDsXFf0)

[HOW TO - TAF - Apurando IRPJ para fins de ECF](https://www.youtube.com/watch?v=pcTIKDhaeSc)
