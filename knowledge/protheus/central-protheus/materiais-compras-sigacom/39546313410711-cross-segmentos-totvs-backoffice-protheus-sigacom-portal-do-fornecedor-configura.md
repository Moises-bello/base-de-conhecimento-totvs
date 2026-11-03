---
article_id: 39546313410711
category: Materiais - Compras (SIGACOM)
content_hash: 6412980d909a80db2fc1d61e233d76ddc59b7a12be99ec752362a37e798dc8d6
fetched_at: '2026-06-28T22:41:23.992913+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Portal do Fornecedor
  - Configuração do WebServices e Portais;
type: support-article
updated_at: '2026-04-06T18:38:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39546313410711-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Portal-do-Fornecedor-Configura%C3%A7%C3%A3o-do-WebServices-e-Portais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39546313376407) Tempo aproximado para leitura: **07:00:00 min**  
  
**Dúvida**

Como configurar o WebServices e Portais?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Todas as Versões

**Solução**

Acesse o Portal do Cliente e realize o download dos arquivos WEBFILES utilizando o filtro indicado abaixo.

Após concluir o download, copie os arquivos selecionados para a pasta *Systemload*.

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39546315077655)

[Baixe o Arquivo Aqui!](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads)

**Configuração do WebServices e Portais;**

Para habilitar os portais do Protheus, é necessário que o serviço de WebServices esteja ativo.

Tanto os WebServices quanto os Portais dependem do serviço HTTP do Protheus, responsável por disponibilizar as informações na web.

Portanto, o primeiro passo é habilitar o serviço HTTP e configurar a porta que será utilizada pelos demais serviços.

1. Parâmetro inicial: SRVWIZARD :

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39546315079063)

2.Serviço de HTTP : Em Servidor Internet (HTTP/FTP), verifique se o serviço de HTTP já existe, confirme se está habilitado e para qual porta está configurada. Pois estas são informações indispensáveis para o correto funcionamento dos WS e Portais.

* Caso não tenha o Servidor Internet <HTTP> criado, é necessário seguir o procedimento abaixo:
* Selecionar a opção: <HTTP> e clicar na barra superior <Editar>

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39546315081751)

3. Selecione a opção HTTP : Clique em Editar para criar/configurar;

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39546807501335)

4. Habilitar o WebService. Adicione um novo módulo Web;

![7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39549976283159)

5. Configure o WebService conforme exemplo abaixo.

*Atentar para os caminhos do ambiente.*

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39550035684887)

6. Selecione a opção de descompactar o pacote http:

![8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39549976284823)![9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39550035686551)

 6. Defina a quantidade mínima e máxima de usuários.   Exemplo: mínimo 10 e máximo 10.

![10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39549976287639)

7. Configuração do Portal (PP). As configurações realizadas no WebService, conforme os itens 4, 5 e 6, também devem ser aplicadas ao Portal (PP).

#### [**Configuração App.Server. Ini Consulte Aqui!**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/39551469256087/live_preview/01KNHYTD4VA4W30JSZ8HRRJSEJ)

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
