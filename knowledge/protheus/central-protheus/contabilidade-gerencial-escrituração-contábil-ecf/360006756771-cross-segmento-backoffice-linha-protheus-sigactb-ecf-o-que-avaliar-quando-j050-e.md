---
article_id: 360006756771
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 5bb45b38dd6c7669ef3984b9f435b465ee9940f012a2416ee7e08e50854f6b13
fetched_at: '2026-06-28T22:40:48.811329+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF – O que avaliar
  quando J050 e J051 não é gerado
type: support-article
updated_at: '2022-06-10T11:17:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado
---

**Dúvida**

Plano de contas e plano referencial não esta sendo gerado no Arquivo TXT

* CS3 e CS4 - não estão sendo alimentadas
* T010 e T010AA na tabela TAFST1 - não estão sendo alimentados
* TAFA060 não esta sendo gerado conta contábil e Conta referencial
* J050 e J051 não esta sendo gerado no arquivo TXT

**Ambiente**  
Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**

* Verifique  
  [MP - SIGACTB - ECF - J051 não esta sendo gerado no arquivo TXT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005033352-MP-SIGACTB-ECF-J051-n%C3%A3o-esta-sendo-gerado-no-arquivo-TXT)

* Verifique os passos abaixo   
  [MP - SIGACTB - ECF - J050 e J051 COMO GERAR](http://tdn.totvs.com/pages/releaseview.action?pageId=284465420)

* Realize o procedimento abaixo  
  [MP - SIGACTB - ECF - O que fazer quando as Tabelas TAFST1 , TAFST2 ou TAF não são](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689072-MP-SIGACTB-ECF-O-que-fazer-quando-as-Tabelas-TAFST1-TAFST2-ou-TAF-n%C3%A3o-s%C3%A3o-Alimentado-ou-Recriados) [Alimentado ou Recriados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689072-MP-SIGACTB-ECF-O-que-fazer-quando-as-Tabelas-TAFST1-TAFST2-ou-TAF-n%C3%A3o-s%C3%A3o-Alimentado-ou-Recriados)

* Revise os parâmetros abaixo  
  [MP - SIGACTB - ECF - Parâmetros de Integração CTB/TAF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-)

* Verifique se as tabelas, e rotinas foram alimentadas   
  [MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)

* Veja tratamento das Autocontidas

[MP - SIGACTB - CTBS001 - Atualização das Tabelas Autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006985071-MP-SIGACTB-CTBS001-Atualiza%C3%A7%C3%A3o-das-Tabelas-Autocontidas-)

* Verifique o preenchimento da Wizard na rotina de escrituração

<http://tdn.totvs.com/display/public/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF>

* Lucro Presumido

[MP - SIGACTB - ECF – Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido)

* Lucro Real /Apuração Anual

[MP - SIGACTB - ECF – Como gerar o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-)

* Verifique o compartilhamento das tabela

# [Compartilhamento das tabelas CS's](http://tdn.totvs.com/pages/releaseview.action?pageId=287077842)

* Tabelas envolvidas

CT1 - PLANO DE CONTA  
CVD - Plano referencial  
CVN - Plano de contas X plano referencial.

CS3 Plano de contas   
CS4 Plano de conta referencial

Obs: necessário que as tabelas  mencionada esteja com o compartilhamento correto :[compartilhamento de tabelas no Contabilidade Gerencial (SIGACTB)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search)e o compartilhamento das [TABELAS ECD E ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF?source=search)
