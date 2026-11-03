---
article_id: 360027708192
category: Materiais - Compras (SIGACOM)
content_hash: 5b94cd53e55c8a22eda268e90b07b7650e8ab11bf710931cb27c3b73f4a7ad0f
fetched_at: '2026-06-28T22:41:10.274744+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - PORTAL FORNECEDOR -
  Configuração básica e demais ocorrências
type: support-article
updated_at: '2025-10-06T20:15:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027708192-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-PORTAL-FORNECEDOR-Configura%C3%A7%C3%A3o-b%C3%A1sica-e-demais-ocorr%C3%AAncias
---

**Dúvida**

Qual o exemplo da configuração básica para o Portal Fornecedor?  
  
**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

Acessar o Portal do Cliente e fazer o download de arquivos WEBFILES conforme exemplo de filtro abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085089874)

Verifique conforme seu ambiente e coloque os arquivos demonstrados abaixo na pasta **Systemload**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089797214)

Passo a passo básico para configuração do Portal Fornecedor

**1 - Configurando WebServices e Portais**

Para habilitar os Portais Protheus, é necessário que o serviço de WebServices esteja ativo.  Ambos serviços dependem do serviço HTTP do Protheus, ao qual permite que as informações sejam publicadas na WEB.

Assim, a configuração inicia-se habilitando o serviço HTTP e configurando a porta aos quais todos os outros serviços dependentes deste irão utilizar para a publicação das informações.

Parâmetros iniciais: **SRVWIZARD**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027829651)

**2 - Serviço de HTTP**

Em Servidor Internet (HTTP/FTP), verifique se o serviço de HTTP já existe, confirme se está habilitado e para qual porta está configurada. Pois estas são informações indispensáveis para o correto funcionamento dos WS e Portais.

* Caso não tenha o Servidor Internet <HTTP> criado, é necessário seguir o procedimento abaixo:
* Selecionar a opção: <HTTP> e clicar na barra superior <Editar>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027830091)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027841892)

**3 -Para habilitar o WebService: Adicione um novo módulo Web**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027830671)

**4 - Configure o WebService conforme exemplo abaixo.**

*Atentar para os caminhos do ambiente.*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027830691)

**5 - Selecione a opção de descompactar o pacote http**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027831511)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027830831)

**6 - Informe usuários Mínimos e Máximo. No exemplo abaixo estou informando 10 e 10.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027830891)

**7 - Wizard para o WebService devem ser realizadas para o Portal**

As mesmas configurações feitas no Wizard para o WebService devem ser realizadas para o Portal - <PP>. Lembrando sempre de informar o mesmo ambiente e apontar na URL do WebService a informação correta do WebService, exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027830931)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027842512)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027831631)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027842572)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027842632)

**8 - APPSERVER.INI**

Confira o arquivo INI do Server. Deverá ficar semelhante ao descrito abaixo, caso não esteja, complemente-o:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027843312)

***A chave SECURITY = 1 se tornou obrigatória na configuração do Ini, a partir da release 12.1.2310***

Configurar a chave **SECURITY=1** nos jobs **ws** e **pp** conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32047795640343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32047832465943)

***Observaç**ão1!***

Caso apresenta a mensagem AUTHENTICATION: USER NOT AUTHORIZED ao acessar Portal Fornecedor ,em releases igual ou inferir a release **12.1.2210** acessar o arquivo appserver.ini e adicionar a chave **SECURITY=0** nos jobs ws e pp no Ini do Appserver.

***Observaç**ão2*!**

No JOB do Portal deve ser inserido o caminho do diretório onde ficam disponíveis os arquivos registrados como anexo *(conhecimento),* conforme exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093475513)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091321594)

Caso contrário o sistema pode apresentar o alerta abaixo na consulta:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091321834)

**9 - Serviço do WebService**

Após as configurações apontadas acima, reinicie o Server do Protheus e verifique se o serviço do WebService subiu de forma correta no Browser, exemplo:

<http://spod2503:9192/ws/>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027843592)

**10 - PORTAL FORNECEDOR**

Acesse o ambiente Protheus

* Módulo **Faturamento / Atualizações / Portal / Web Service** e clique em **Automático**
* Serão carregados os Web Services:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027844132)

 Módulo **Faturamento / Atualizações / Portal  /Menu dos Portais**

* Verifique se os menus estão carregados, caso negativo saia do sistema e acesse novamente a rotina:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027832811)

* Em **Faturamento / Atualizações / Portal / Usuários**
* Clique em **Incluir**
* Digite o nome, senha e como usuário interno vincule o código do Fornecedor:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027833811)

Na aba direitos e clique em **Ações relacionadas / Direitos**

* São carregados todos os direitos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027845772)

**11 - Verifique se o serviço do WebService - <PP> subiu de forma correta no Browser, exemplo:**

*ATENÇÃO: O Portal Fornecedor é intitulado como **PORTAL PROTHEUS***

[http://spod2503:9192/pp/](http://spod2503:9192/pp/W_PWSX010.APW)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027845892)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027846052)

**12 - Quanto a  segurança do portal no ambiente do cliente, no tocante a infraestrutura :**

Sobre possibilidade de implementar o Portal do Fornecedor em servidor apartado do Protheus, portas diferentes, DMZ, e outras questões de segurança e infraestrutura ficam a critério do cliente de acordo com sua necessidade e preferência. Não há uma especificação que determine a obrigatoriedade por parte do produto.

**13- Como aumentar o tempo de acesso do fornecedor ao portal do fornecedor ?**

Para atender tal necessidade, basta acrescentar no appserver.ini, a tag SESSIONTIMEOUT na sessão HTTP. Abaixo documento que explica sobre a TAG.

<https://tdn.totvs.com/display/tec/SessionTimeOut>

**14- O Portal do fornecedor pode ser configurado com o protocolo HTTPS ?**

Recentemente fizemos uma consulta à nossa equipe de produto referente a essa situação e, onde obtivemos o retorno abaixo :

*Devido a uma limitação técnica na aplicação Portal do Fornecedor, atualmente não é possível utilizar configuração com o protocolo HTTPS.*

*Sendo assim, iremos abrir uma ocorrência interna para realizar um estudo e verificar a possibilidade e viabilidade, para atualizar todas as rotinas e formulários que são utilizados pelo Portal do Fornecedor, para que sejam compatíveis com o protocolo HTTPS.*

Porém não temos como informar uma data para início deste estudo

**15- Configurações do portal do fornecedor para mais de uma empresa ou filial.**

O portal do fornecedor em sua configuração é muito semelhante ao portal do vendedor, por isso sempre que houver mais de uma empresa/filial em seu ambiente, será necessário configurar um WS para cada filial como informa o documento abaixo :

[Portal com mais de uma filial](https://tdn.totvs.com/pages/releaseview.action?pageId=236596491)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12549486221207)

**16- Licença a ser consumida pelo sistema no acesso ao portal do fornecedor.**

Para que o portal do fornecedor funcione corretamente no ambiente do cliente é necessário ter a licença TOTVS i. Sem ela o portal não funcionará. Caso não a possua, a sugestão é procurar o ESN junto a Totvs para aquisição da mesma.

**Help Online:**

* [Clique aqui para verificar informações básicas sobre utilização do Portal Fornecedor](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/portais_portal_do_fornecedor.htm)

  |  |  |
  | --- | --- |
  | • | [Configuração de Portais](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/portais_configuracao_dos_portais.htm). |

  |  |  |
  | --- | --- |
  | • | [Infra-estrutura necessária](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/portais_infra_estrutura_necessaria.htm). |

  |  |  |
  | --- | --- |
  | • | [Roteiro para Configuração](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/portais_roteiro_para_configuracao.htm). |

  |  |  |
  | --- | --- |
  | • | [Web Service](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/fata230.htm). |

  |  |  |
  | --- | --- |
  | • | [Menu dos Portais](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/fata240.htm). |

  |  |  |
  | --- | --- |
  | • | [Portal de Usuários / Direitos](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/fata220.htm). |

**Vídeos relacionados:**

* [Clique aqui para verificar configuração relacionada ao HTTP](https://www.youtube.com/watch?v=5SJYfhcIvec)
* [Clique aqui para verificar o processo acessando pelo WebBrowser](https://www.youtube.com/watch?v=KJaecXPMNhE)

**FAQs Relacionadas:**

* Pontos de Entrada: [MP - SIGACOM - Pontos de Entrada Portal Fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034178834-MP-SIGACOM-Pontos-de-Entrada-Portal-Fornecedor)
* Inserir logotipo: [MP - SIGACOM - Logotipo no Portal Fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025998371-MP-SIGACOM-Logotipo-no-Portal-Fornecedor)

#### **Helps**

* [MP - SIGACOM - PORTAL FORNECEDOR - PUTQUOTE - NVAZIO](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7CjoHaWRsKwh699zUUwA6CXR5cGVJIgxhcnRpY2xlBjoGRVQ6CHVybEkid2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzUzNjYzNC1NUC1TSUdBQ09NLVBPUlRBTC1GT1JORUNFRE9SLVBVVFFVT1RFLU5WQVpJTwY7B1Q6DnNlYXJjaF9pZEkiKTMyNDY1YzFkLTk3OWEtNDk2OS1hODkyLWE4YWIxMGM3NTc4YwY7B0Y6CXJhbmtpBg%3D%3D--eadb64b9a45224c1db70600daa0c702c4a43bc79)
* [MP - SIGACOM - PORTAL FORNECEDOR - PUTQUOTE - A150PRO0](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7CjoHaWRsKwhS99zUUwA6CXR5cGVJIgxhcnRpY2xlBjoGRVQ6CHVybEkieWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzUzNjU5NC1NUC1TSUdBQ09NLVBPUlRBTC1GT1JORUNFRE9SLVBVVFFVT1RFLUExNTBQUk8wBjsHVDoOc2VhcmNoX2lkSSIpYmFkZjhlOTMtMTA5OC00MGMwLTk4YWYtNjlmYjNkMTIxNTQ2BjsHRjoJcmFua2kG--4b6616d0f01948aea595aa5d92bce7bce1f9f3ad)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Erro AUTHENTICATION: USER NOT AUTHORIZED ao acessar Portal Fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5103668680727-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Erro-AUTHENTICATION-USER-NOT-AUTHORIZED-ao-acessar-Portal-Fornecedor?source=search)

***Saiba Mais:***

* [PCOM01002 - Opção Banco de Conhecimento Portal e Fornecedor na rotina MATA150](https://tdn.totvs.com/pages/releaseview.action?pageId=627977653)
* [Configuração de portais e Webservices - FrameWork](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026453811-MP-FRAME-Configura%C3%A7%C3%A3o-de-Portais-e-WebServices?source=search)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
