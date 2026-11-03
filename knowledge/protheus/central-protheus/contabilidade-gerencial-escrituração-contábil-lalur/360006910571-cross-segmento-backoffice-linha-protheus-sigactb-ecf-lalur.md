---
article_id: 360006910571
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: d454bb57334dfc01539e24b72e9fc97d892af5fb99ec818e134ab01fbfcaa187
fetched_at: '2026-06-28T22:40:40.220323+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF  LALUR
type: support-article
updated_at: '2024-08-05T19:33:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-LALUR
---

**COMO GERAR LALUR**

**Ocorrência**

Os dados extraídos no modulo Contábil serão referente ao lançamento da parte A do  lalur para tratamento da parte B, com relação a parte B será necessário cadastrar manualmente no TAF.

 “M300 – Lançamentos da Parte 'A' do e-Lalur” / “M350 – Lançamentos da Parte 'A' do e-Lacs”.

* [Orientações Consultoria de Segmentos](http://tdn.totvs.com/pages/releaseview.action?pageId=236430090)
* **O lalur não exporta o [plano de contas (J050)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search) e o [Bloco K](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search) para o TAF, diante disso se faz necessário :**
* **Antes de gerar o Lalur é necessário exportar a** **ECF** **para o TAF, pois a través da exportação da ECF será gerado o Plano de contas**
* **Obs : necessário que a exportação da ECF seja realizada sem nenhum erro de importação , caso  apresentado algum erro, necessário corrigir ,para que assim conclua a exportação da ECF**

* [Como gerar ECF para o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
* [Como realizar ECF para o Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)
* [Como realizar ECF  o Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
* [ECF IMUNE OU ISENTA COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search)  
    
  **Ambiente**  
  Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

**Modulo SIGACTB:** LALUR

* Cadastro de Lançamentos a serem integrados para o TAF  Referente ao processo de apuração do IRPJ/CSLL - LALUR
* [Help\_Integração\_LALUR](http://tdn.totvs.com/pages/releaseview.action?pageId=286205428)

Rotinas

* [MECANISMO\_CENTRAL\_ESCRITUR\_DADOS\_CONTABEIS\_LALUR\_TAF](http://tdn.totvs.com/display/public/PROT/MSERV-5740_DT_FILTRO_MECANISMO_CENTRAL_ESCRITUR_DADOS_CONTABEIS_LALUR_TAF)
* [FILTRO\_EXTRACAO\_DADOS\_CONTABEIS\_LALUR\_TAF](http://tdn.totvs.com/display/public/PROT/MSERV-5740_DT_FILTRO_EXTRACAO_DADOS_CONTABEIS_LALUR_TAF)
* [MP - SIGACTB - ECF - Geração do BLOCO M no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008506768-MP-SIGACTB-ECF-Gera%C3%A7%C3%A3o-do-BLOCO-M-no-TAF)

**Modulo SIGATAF** : Apuração do IRPJ e CSLL (Lalur/LACS)

* Abaixo link contendo informações sobre Apuração IRPJ e CSLL no TAF , contendo também vídeo demonstrando o processo do cadastro da parte B.

* [Apuração do IRPJ e da CSLL (LALUR/LACS) (Vídeo)](http://tdn.totvs.com/pages/releaseview.action?pageId=274320876)
* [Geração BLOCO M](http://tdn.totvs.com/pages/releaseview.action?pageId=244434240)

Para maiores informações, acessar os links

Rotina abaixo as informações são gerada automaticamente pelo modulo contábil para o TAF

* [Lançamentos Contábeis - TAFA331](http://tdn.totvs.com.br/pages/releaseview.action?pageId=269067209)

Rotinas abaixo necessário cadastrar manualmente

* [Bloco 0 - Parâmetros de Abertura ECF ( TAFA372 )](http://tdn.totvs.com/pages/viewpage.action?pageId=200904478)
* [Bloco M - Identificação da Conta na Parte B do e-Lalur e do e-Lacs ( TAFA330 ) da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=201730475)
* [Bloco M - Apuração IRPJ/CSLL para Lucro Real ( TAFA322 ) da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=200904478)
* [Bloco M - Apuração IRPJ/CSLL para Lucro Real ( TAFA322 ) da ECF ( Nova Versão )](http://tdn.totvs.com/pages/viewpage.action?pageId=200904419)
* [Cópia de Bloco M - Apuração IRPJ/CSLL para Lucro Real ( TAFA322 ) da ECF ( Nova Versão )](http://tdn.totvs.com/pages/viewpage.action?pageId=284882713)
* [Cadastro de Tributos - TAFA430](http://tdn.totvs.com.br/display/public/TAF/Cadastro+de+Tributos+-+TAFA430+-+TAF+-+P12)
* [Cadastro de Períodos de Apuração - TAFA444](http://tdn.totvs.com.br/pages/releaseview.action?pageId=269087163)
* [Documento de Arrecadação - TAFA027](http://tdn.totvs.com.br/pages/viewpage.action?pageId=271166621)
* [Cadastro de Eventos Especiais - TAFA443](http://tdn.totvs.com.br/display/public/TAF/Cadastro+de+Eventos+Especiais+-+TAFA443+-+TAF+-+P12)
* [Evento Tributário - Vigência - TAFA438](http://tdn.totvs.com.br/pages/releaseview.action?pageId=245170511)
* [Evento tributário - TAFA433](http://tdn.totvs.com.br/pages/viewpage.action?pageId=248578386)

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

**Saiba mais**

[MP\_SIGACTB LALUR/LACS: CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)

[MP-SIGACTB - ECF Tabelas Relacionadas a Apuração IRPJ CSLL no TAF (Lalur)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034815894-MP-SIGACTB-ECF-Tabelas-Relacionadas-a-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-Lalur-?source=search)

[MP-SIGACTB - ECF Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)

[MP - Cálculo de CSLL e IRPJ - Empresa Lucro Presumido - Trimestral - SIGACTB X SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133373-MP-C%C3%A1lculo-de-CSLL-e-IRPJ-Empresa-Lucro-Presumido-Trimestral-SIGACTB-X-SIGATAF?source=search)

[MP\_SIGACTB LALUR E LACS: LUCRO PRESUMIDO REGIME DE CAIXA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018333372-MP-SIGACTB-LALUR-E-LACS-LUCRO-PRESUMIDO-REGIME-DE-CAIXA-?source=search)

[MP - SIGACTB - COMO CONFIGURAR O LUCRO PRESUMIDO NO TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010318251-MP-SIGACTB-COMO-CONFIGURAR-O-LUCRO-PRESUMIDO-NO-TAF-?source=search)

[MP-SIGACTB - ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)

[MP - SIGACTB - ECF TAFA433 - Compensação do Prejuízo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035081174-MP-SIGACTB-ECF-TAFA433-Compensa%C3%A7%C3%A3o-do-Preju%C3%ADzo?source=search)

[MP-SIGACTB - ECF Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)

[MP-SIGACTB - ECF :TAFA433 apuração  de IRPJ e CSLL o TAF saldo "Imposto Devido Meses Anteriores" cumulativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035535754-MP-SIGACTB-ECF-TAFA433-apura%C3%A7%C3%A3o-de-IRPJ-e-CSLL-o-TAF-saldo-Imposto-Devido-Meses-Anteriores-cumulativo-?source=search)

[MP\_SIGACTB :TAF-Controle do PAT na Parte B do LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037249374-MP-SIGACTB-TAF-Controle-do-PAT-na-Parte-B-do-LALUR?source=search)

[Cross Segmento - Backoffice Linha Protheus - TAF - TAFA433- Simulação apuração LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402387769623-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Simula%C3%A7%C3%A3o-apura%C3%A7%C3%A3o-LALUR?source=search)

[Cross Segmento - Backoffice Linha Protheus - TAF- Roteiro de cadastros e parametrizações para apuração do LALUR/LACS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404191850135-Cross-Segmento-Backoffice-Linha-Protheus-TAF-Roteiro-de-cadastros-e-parametriza%C3%A7%C3%B5es-para-apura%C3%A7%C3%A3o-do-LALUR-LACS?source=search)

[Cross Segmento - Backoffice Linha Protheus - TAF - TAFA438 - Cadastro de vigência do evento tributário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404413683351-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA438-Cadastro-de-vig%C3%AAncia-do-evento-tribut%C3%A1rio?source=search)

[MP-SIGACTB - CTBS300 - Onde cadastrar filtro do lalur](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015738232-MP-SIGACTB-CTBS300-Onde-cadastrar-filtro-do-lalur-?source=search)

[MP-SIGACTB - ECF Tabelas Relacionadas a Apuração IRPJ CSLL no TAF (Lalur)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034815894-MP-SIGACTB-ECF-Tabelas-Relacionadas-a-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-Lalur-?source=search)

[MP-SIGACTB - ECF :TAFA433 apuração  de IRPJ e CSLL o TAF saldo "Imposto Devido Meses Anteriores" cumulativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035535754-MP-SIGACTB-ECF-TAFA433-apura%C3%A7%C3%A3o-de-IRPJ-e-CSLL-o-TAF-saldo-Imposto-Devido-Meses-Anteriores-cumulativo-?source=search)

[TAF\_LALUR Porque o TAF só permite apuração de uma filial por Empresa?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053727454-TAF-LALUR-Porque-o-TAF-s%C3%B3-permite-apura%C3%A7%C3%A3o-de-uma-filial-por-Empresa-?source=search)

[MP- SIGACTB :TAF LALUR AJUSTE ANUAL ROTINA TAFA444 NÃO EXISTE UMA VIGÊNCIA CADASTRADA ABRANGENDO ESTE PERIODO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025396692-MP-SIGACTB-TAF-LALUR-AJUSTE-ANUAL-ROTINA-TAFA444-N%C3%83O-EXISTE-UMA-VIG%C3%8ANCIA-CADASTRADA-ABRANGENDO-ESTE-PERIODO?source=search)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS300/ TAFA331 Base de calculo para apuração e simulação do Lalur e diferença de saldos nos lançamentos exportados para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063097093-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS300-TAFA331-Base-de-calculo-para-apura%C3%A7%C3%A3o-e-simula%C3%A7%C3%A3o-do-Lalur-e-diferen%C3%A7a-de-saldos-nos-lan%C3%A7amentos-exportados-para-o-TAF?source=search)

[MP - SIGACTB - LALUR - COM CENTRO DE CUSTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046640714-MP-SIGACTB-LALUR-COM-CENTRO-DE-CUSTO?source=search)

[MP - SIGACTB - IRPJ e CSLL COMO CONFIGURAR O LUCRO PRESUMIDO NO TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010318251-MP-SIGACTB-IRPJ-e-CSLL-COMO-CONFIGURAR-O-LUCRO-PRESUMIDO-NO-TAF-?source=search)

[Cross Segmento - Backoffice Linha Protheus - TAF - TAFA436 - Lalur Compensação de prejuízo parte B com reflexo na parte A](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037921673-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA436-Lalur-Compensa%C3%A7%C3%A3o-de-preju%C3%ADzo-parte-B-com-reflexo-na-parte-A?source=search)

[MP - SIGACTB - TAFA344 Cálculo de CSLL e IRPJ - Empresa Lucro Presumido trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133373-MP-SIGACTB-TAFA344-C%C3%A1lculo-de-CSLL-e-IRPJ-Empresa-Lucro-Presumido-trimestral-?source=search)

[MP - SIGACTB - LALUR: M030 COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053637214-MP-SIGACTB-LALUR-M030-COMO-GERAR?source=search)

[Escrituração Contábil Fiscal - ECF - Modificações Leiaute 10](https://tdn.totvs.com/pages/releaseview.action?pageId=821186345#Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscalECFModifica%C3%A7%C3%B5esLeiaute10-08.RegistroN)
