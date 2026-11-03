---
article_id: 40251557425943
category: Gestão de Transportes (TMS)
content_hash: 9b981e4fcd5db249669b7a75a068b0695b7b84ee7421068c869db2fd81022ce4
fetched_at: '2026-06-28T22:45:27.192250+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Novas regras de CIOT
type: support-article
updated_at: '2026-05-21T15:09:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40251557425943-Log%C3%ADstica-Linha-Protheus-TMS-Novas-regras-de-CIOT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40251519053591) Tempo aproximado para leitura: **00:01:55 min**  
  
**Dúvida**  
Quais são as novas regras de **CIOT** e como o **TMS** irá atuar sobre essas novas regras?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Atualmente o **TMS** já realiza a geração de **CIOT** através de integrações nativas com as Operadoras de Frotas **Repom**, **Pamcard** e **PagBem.** Também é possível preencher o **CIOT** de forma manual na viagem, caso gere-o por outra **IPEF**, conforme demonstrado nesta documentação[**Logística - Linha Protheus - TMS - Formas de vincular CIOT e Vale-Pedágio**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042456114-Log%C3%ADstica-Linha-Protheus-TMS-Formas-de-vincular-CIOT-e-Vale-Ped%C3%A1gio)**.**  
  
Entretanto, a geração, retificação, cancelamento e encerramento do CIOT passará por mudanças, conforme regras de validações descritas em:

* [MEDIDA PROVISÓRIA Nº 1.343, DE 19 DE MARÇO DE 2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/mpv/mpv1343.htm)
* [RESOLUÇÃO ANTT Nº 6.078, DE 24 DE MARÇO DE 2026](https://www.in.gov.br/web/dou/-/resolucao-antt-n-6.078-de-24-de-marco-de-2026-695432632)
* [PORTARIA SUROC Nº 6 DE 23 DE ABRIL DE 2026](https://anttlegis.antt.gov.br/action/ActionDatalegis.php?acao=abrirTextoAto&tipo=POR&numeroAto=00000006&seqAto=000&valorAno=2026&orgao=SUROC/ANTT/MT&cod_modulo=623&cod_menu=9230)

Para atender às novas regras, o time de produto **Protheus TMS** está atuando nesta adequação sob a *issue* **DLOGTMS02-30791** para tratar os seguintes assuntos sobre **CIOT**:

* Adequação para envio dos novos parâmetros **ANTT** para geração de **CIOT** em todas as **IPEFS** que integram com Protheus TMS, sendo **Pamcard, Repom e Pagbem;**
* Ainda em**fase de análise para possível implementação -** Utilização do **DCS/CIOT** à partir de serviço disponibilizado pela **ANTT** para operações do próprio **ETC**. Apesar de não ser uma obrigação da TOTVS, estamos atuando fortemente para auxiliar os clientes, conforme retorno de nossa consultoria de segmentos: [ANTT - CIOT - Obrigatoriedade de Implementação de Webservice](https://tdn.totvs.com/pages/releaseview.action?pageId=1068175998)

Para receber as orientações e atualizações dessa *issue* quando ela for expedida, entre em contato com nosso time de suporte **Protheus TMS** solicitando que seu ticket seja associado a esta *issue*. Assim que a equipe de produto possuir um posicionamento, você será informado por meio do ticket associado.  
  
  
  
O time de produto também está atualizando constantemente as seguintes documentações com as novidades sobre esse assunto:  
[Alterações na lei 11442/2007, que estabelece o CIOT Universal](https://tdn.totvs.com/pages/viewpage.action?pageId=1066136216)  
[TMS PROTHEUS X MUDANÇAS NA EMISSÃO DO CIOT 2026](https://tdn.totvs.com/pages/viewpage.action?pageId=1068203960)  
  
**Saiba mais**  
Notícias **ANTT** sobre **CIOT**:[Notícias - CIOT](https://www.gov.br/antt/pt-br/search?origem=form&SearchableText=CIOT)  
[BLOG TOTVS - 25 março de 2026 - ANTT regulamenta nova sistemática do transporte e operacionaliza MP](https://www.totvs.com/blog/fiscal-clientes/antt-publica-resolucoes-que-regulamentam-nova-sistematica-do-transporte-de-cargas-e-operacionalizam-medida-provisoria/)  
[BLOG TOTVS - 24 abril de 2026 - ANTT publica novas regras para o CIOT no transporte rodoviário de cargas](https://www.totvs.com/blog/fiscal-clientes/antt-publica-novas-regras-para-o-ciot-no-transporte-rodoviario-de-cargas/)  
  
**Glossário**  
**ANTT**- Agência Nacional de Transportes Terrestres  
**CIOT** - Código Identificador da Operação de Transporte  
**DCS** - Documento de Contrato de Serviço  
**ETC -** Empresa de Transporte Rodoviário de Cargas  
**IPEF** - Instituição de Pagamento Eletrônico de Frete
