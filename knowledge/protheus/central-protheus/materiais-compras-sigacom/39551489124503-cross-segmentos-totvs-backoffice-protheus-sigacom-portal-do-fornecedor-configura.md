---
article_id: 39551489124503
category: Materiais - Compras (SIGACOM)
content_hash: d96bc30a28df99770f72e7f2844075de62baa6ed1e30b3fab0e74bcd710ae8f7
fetched_at: '2026-06-28T22:41:23.986811+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Portal do Fornecedor
  - Configuração Appserver.INI
type: support-article
updated_at: '2026-04-06T18:49:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39551489124503-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Portal-do-Fornecedor-Configura%C3%A7%C3%A3o-Appserver-INI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39551489112471) Tempo aproximado para leitura: **04:00:00 min**  
  
**Dúvida**

Qual a configuração necessária no Appserver.Ini para o uso do Portal do Fornecedor?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS compras - Todas as Versões

**Solução**

A chave **SECURITY=1** passou a ser obrigatória na configuração do arquivo INI a partir da release 12.1.2310.

Configure a chave **SECURITY=1** nos jobs **ws** e **pp**, conforme o exemplo abaixo:

![12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39551469320215)

Observação :  No JOB do Portal deve ser inserido o caminho do diretório onde ficam disponíveis os arquivos registrados como anexo *(conhecimento),* conforme exemplo abaixo:

![13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39551489115031)

Após as configurações apontadas acima, reinicie o Server do Protheus e verifique se o serviço do WebService subiu de forma correta no Browser, exemplo:

![14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39551469322135)

***Saiba Mais:***

* [SIGACOM - PORTAL FORNECEDOR - AUTHENTICATION: USER NOT AUTHORIZED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/39544478522519-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-PORTAL-FORNECEDOR-AUTHENTICATION-USER-NOT-AUTHORIZE)
* [Clique aqui para verificar configuração relacionada ao HTTP](https://www.youtube.com/watch?v=5SJYfhcIvec)
* [Clique aqui para verificar o processo acessando pelo WebBrowser](https://www.youtube.com/watch?v=KJaecXPMNhE)
* [MP - SIGACOM - Pontos de Entrada Portal Fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034178834-MP-SIGACOM-Pontos-de-Entrada-Portal-Fornecedor)
* [MP - SIGACOM - Logotipo no Portal Fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025998371-MP-SIGACOM-Logotipo-no-Portal-Fornecedor)
* [MP - SIGACOM - PORTAL FORNECEDOR - PUTQUOTE - NVAZIO](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7CjoHaWRsKwh699zUUwA6CXR5cGVJIgxhcnRpY2xlBjoGRVQ6CHVybEkid2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzUzNjYzNC1NUC1TSUdBQ09NLVBPUlRBTC1GT1JORUNFRE9SLVBVVFFVT1RFLU5WQVpJTwY7B1Q6DnNlYXJjaF9pZEkiKTMyNDY1YzFkLTk3OWEtNDk2OS1hODkyLWE4YWIxMGM3NTc4YwY7B0Y6CXJhbmtpBg%3D%3D--eadb64b9a45224c1db70600daa0c702c4a43bc79)
* [MP - SIGACOM - PORTAL FORNECEDOR - PUTQUOTE - A150PRO0](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7CjoHaWRsKwhS99zUUwA6CXR5cGVJIgxhcnRpY2xlBjoGRVQ6CHVybEkieWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzUzNjU5NC1NUC1TSUdBQ09NLVBPUlRBTC1GT1JORUNFRE9SLVBVVFFVT1RFLUExNTBQUk8wBjsHVDoOc2VhcmNoX2lkSSIpYmFkZjhlOTMtMTA5OC00MGMwLTk4YWYtNjlmYjNkMTIxNTQ2BjsHRjoJcmFua2kG--4b6616d0f01948aea595aa5d92bce7bce1f9f3ad)
* [PCOM01002 - Opção Banco de Conhecimento Portal e Fornecedor na rotina MATA150](https://tdn.totvs.com/pages/releaseview.action?pageId=627977653)
* [Configuração de portais e Webservices - FrameWork](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026453811-MP-FRAME-Configura%C3%A7%C3%A3o-de-Portais-e-WebServices?source=search)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
