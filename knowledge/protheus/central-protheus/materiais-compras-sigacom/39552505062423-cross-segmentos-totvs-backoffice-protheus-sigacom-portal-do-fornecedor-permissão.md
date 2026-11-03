---
article_id: 39552505062423
category: Materiais - Compras (SIGACOM)
content_hash: bd298b5ab3b64bf92cb82f47ca03d8db75144729627b02ba84f58b432d942dd0
fetched_at: '2026-06-28T22:41:23.998891+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Portal do Fornecedor
  - Permissão de Usuários
type: support-article
updated_at: '2026-04-06T18:44:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39552505062423-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Portal-do-Fornecedor-Permiss%C3%A3o-de-Usu%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39552538534679) Tempo aproximado para leitura: **03:00:00 min**  
  
**Dúvida**

Como configurar os acessos do Portal do Fornecedor

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Solução**

Acesse o Protheus:

1. Módulo **Faturamento -> Atualizações ->  Portal ->  Web Service** e clique em **Automático**

Serão carregados os Web Services:

![15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39552505044119)

 2. **Atualizações ->  Portal  -> Menu dos Portais;**

Verifique se os menus estão carregados, caso negativo saia do sistema e acesse novamente a rotina:

![16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39552505044503)

3. **Atualizações -> Portal -> Usuários;**

* Clique em **Incluir**
* Digite o nome, senha e como usuário interno vincule o código do Fornecedor;

![17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39552538537495)

4. Na aba direitos e clique em **Ações relacionadas / Direitos**

* São carregados todos os direitos:

![18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39552538537751)

**Dúvidas frequentes:**

**Quanto a  segurança do portal no ambiente do cliente, no tocante a infraestrutura :**

Sobre possibilidade de implementar o Portal do Fornecedor em servidor apartado do Protheus, portas diferentes, DMZ, e outras questões de segurança e infraestrutura ficam a critério do cliente de acordo com sua necessidade e preferência. Não há uma especificação que determine a obrigatoriedade por parte do produto.

**Como aumentar o tempo de acesso do fornecedor ao portal do fornecedor ?**

Para atender tal necessidade, basta acrescentar no appserver.ini, a tag SESSIONTIMEOUT na sessão HTTP. Abaixo documento que explica sobre a TAG.

<https://tdn.totvs.com/display/tec/SessionTimeOut>

**O Portal do fornecedor pode ser configurado com o protocolo HTTPS ?**

Recentemente fizemos uma consulta à nossa equipe de produto referente a essa situação e, onde obtivemos o retorno abaixo :

*Devido a uma limitação técnica na aplicação Portal do Fornecedor, atualmente não é possível utilizar configuração com o protocolo HTTPS.*

*Sendo assim, iremos abrir uma ocorrência interna para realizar um estudo e verificar a possibilidade e viabilidade, para atualizar todas as rotinas e formulários que são utilizados pelo Portal do Fornecedor, para que sejam compatíveis com o protocolo HTTPS.*

Porém não temos como informar uma data para início deste estudo

**Configurações do portal do fornecedor para mais de uma empresa ou filial.**

O portal do fornecedor em sua configuração é muito semelhante ao portal do vendedor, por isso sempre que houver mais de uma empresa/filial em seu ambiente, será necessário configurar um WS para cada filial como informa o documento abaixo :

[Portal com mais de uma filial](https://tdn.totvs.com/pages/releaseview.action?pageId=236596491)

![22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39552505045655)

**Licença a ser consumida pelo sistema no acesso ao portal do fornecedor.**

Para que o portal do fornecedor funcione corretamente no ambiente do cliente é necessário ter a licença TOTVS i. Sem ela o portal não funcionará. Caso não a possua, a sugestão é procurar o ESN junto a Totvs para aquisição da mesma.

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
