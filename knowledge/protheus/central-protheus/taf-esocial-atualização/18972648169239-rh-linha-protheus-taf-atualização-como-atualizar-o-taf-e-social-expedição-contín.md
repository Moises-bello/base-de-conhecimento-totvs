---
article_id: 18972648169239
category: TAF - eSocial - Atualização
content_hash: 4b5d2f4adfe8c0e73522a15e9fe0c9c41c32dfd32c806b7486a6ff764415af91
fetched_at: '2026-06-28T22:45:13.249465+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF  - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição
  Contínua)?
type: support-article
updated_at: '2025-12-29T15:57:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TAF-E-social-Expedi%C3%A7%C3%A3o-Cont%C3%ADnua
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18972603877143) Tempo aproximado para leitura: 00:20:00 min**

**Dúvida**  
Automação Fiscal - ATUALIZAÇÃO - Como atualizar o TAF E-social?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - ATUALIZAÇÃO - Como atualizar o TAF E-social?

**Solução em vídeo:**

**Solução (leitura):**

⚠ **Sempre realize um Backup da sua estrutura antes de realizar qualquer ação !** ⚠

Para atualização do TAF é necessário que você tenha o ambiente **igual ou posterior a Release 12.1.2210 ou Release 12.1.033** caso tenha [garantia estendida](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16164215483543-Garantia-Estendida-12-1-33-TOTVS-Linha-Protheus) ou utilize [TAF - Segregado](https://tdn.totvs.com/display/TAF/02.+TAF+SEGREGADO+ao+ERP).

**Caso tenha a Release inferior a 12.1.2210 e não tenha garantia estendida, faça o processo abaixo:**

* **Clientes TAF Segregado:** Realize a [migração de Release do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020127812-Automa%C3%A7%C3%A3o-Fiscal-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TAF-e-o-TSS-via-atualizador-SEGREGADO-) **se a sua Release for 12.1.27, 12.1.33 ou 12.1.2210** e depois atualize o ambiente seguindo a documentação.
* **Clientes Protheus:** Abra uma solicitação com a equipe do Protheus Framework solicitando o processo de migração de Release 12.1.033 para Release 12.1.2310 **caso não tenha a garantia estendia**.

Para saber qual é a sua release do TAF acesse a [tela de diagnóstico do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063/preview/eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MTc5ODg1NDUxNDMwNjMsInJldmlzaW9uX2lkIjoiMDFIRTVaQ04wS0tCS1k0UVJIN003UVYzNUUiLCJleHAiOjE2OTg4NjM4NTh9.ZcYnQ6vn-QpMdFSYS7sSgfx33u418J5mnFmhMyxqKhg).

Para ambientes em Cloud TOTVS, você pode [atualiza-lo utilizando o T-Cloud](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024948533-CLOUD-MP-Aplicar-pacote) ou [abrir uma solicitação de atualização para a equipe Cloud TAF/TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413617765783-Automa%C3%A7%C3%A3o-Fiscal-Como-solicitar-suporte-TOTVS-para-o-produto-TSS-ou-Cloud) e  informar o seu ambiente e a documentação de atualização do TAF que está visualizando.

**1. Links para download:**

Realize o download dos arquivos abaixo para fazer a atualização e **atente-se** **em baixar os arquivos da Release e Sistema Operacional corretos**:

**Downloads para Windows ![windows.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18972857489047):**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Arquivos** | ``` Release 12.1.2210 ``` | ``` Release 12.1.2310 ``` | ``` Release 12.1.2410 ``` | ``` Release 12.1.2510 ``` |
| Expedição Contínua e Dicionário | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1084563) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1126399) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1174332) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1228187) |
| LIB | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1050526) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1050526) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168735) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168735) |
| DBAccess | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168438) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168438) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168438) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168438) |
| Binário do TAF (Appserver) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112215) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112215) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168420) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168420) |
| Smart Client | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1112221) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1112221) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168455) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168455) |

**Download para LINUX :**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Arquivos** | ``` Release 12.1.2210 ``` | ``` Release 12.1.2310 ``` | ``` Release 12.1.2410 ``` | ``` Release 12.1.2510 ``` |
| Expedição Contínua e Dicionário | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1084563) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1126399) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1174332) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1228187) |
| LIB | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1050526) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1050526) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168735) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168735) |
| DBAccess | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168439) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168439) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168439) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168439) |
| Binário do TAF (Appserver) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112216) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112216) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168421) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168421) |
| Smart Client | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1112223) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1112223) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112226) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112226) |

**Downloads para MAC ![Mac logo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18972857506071):**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Arquivos** | ``` Release 12.1.2210 ``` | ``` Release 12.1.2310 ``` | ``` Release 12.1.2410 ``` | ``` Release 12.1.2510 ``` |
| Expedição Contínua e Dicionário | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1084563) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1126399) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1174332) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1228187) |
| LIB | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1050526) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1050526) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168735) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168735) |
| DBAccess | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168438) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168438) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168438) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168438) |
| Binário do TAF (Appserver) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112215) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112215) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168420) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1168420) |
| Smart Client | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1112224) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1112224) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112225) | [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112225) |

**OBS: O TAF não está homologado para rodar os artefatos em 32 bits, é necessário que o seu servidor onde o TAF está instalado esteja em 64 bits. Caso contrário, o TAF não irá funcionar.**

**Para** [**estações de trabalho**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043647533-Automa%C3%A7%C3%A3o-Fiscal-CONFIGURA%C3%87%C3%83O-Replicando-o-SmartClient-do-servidor-para-outras-esta%C3%A7%C3%B5es-de-trabalho) **onde o usuário tem uma máquina de 32 bits, realize o download do Smart Client 32 bits** [**Clicando aqui**](https://suporte.totvs.com/portal/p/10098/download#detail/1112222)**.**

**1.1 Documentação para SmartClient WebApp**

* Documentação Técnica:

[**WebApp - Configurando nativamente o Application Server como servidor Web**](https://tdn.totvs.com/display/tec/WebApp+-+Configurando+nativamente+o+Application+Server+como+servidor+Web)

* Comunicado TOTVS:

[**Substituição SmartClient Desktop - Comunicado**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24238264700695-Substitui%C3%A7%C3%A3o-SmartClient-Desktop-TOTVS-Linha-Protheus)

**2. Parando os serviços:**

Antes de atualizarmos os artefatos é necessário que você pare todos os serviços do seu TAF/Protheus.

OBS: Lembrando que o serviço do REST, normalmente chamado de "TAF-WS", ele não para automaticamente. Você deve finaliza-lo no Gerenciador de Tarefas.

![parar os serviços.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19030528030871)

**3. Atualização do DBACCESS**

Com os serviços parados, iremos realizar a [atualização do DBACCESS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18504207190039-TOTVS-Automa%C3%A7%C3%A3o-Fiscal-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-DBACCESS-do-TAF-).

Para fazer isso você deve descompactar o arquivo do DBACCESS que foi baixado, copiar todo o conteúdo dentro da pasta, depois colar e substituir pela sua estrutura do DBACCESS atual.

```
Exemplo de caminho: C:\TAF\TafDbaccess64
```

![Atualização DBAccess.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19030519694999)

**4. Atualizando os binários:**

Agora iremos [atualizar os binários do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17999573065367-Automa%C3%A7%C3%A3o-Fiscal-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-Bin%C3%A1rio-do-TAF-).

Para fazer isso você deve descompactar o arquivo do Binário que foi baixado, copiar todo o conteúdo dentro da pasta, depois colar e substituir nas pastas "APP" e "APPSERVER" do seu TAF.

```
Exemplos de caminhos: C:\TAF\bin\app e C:\TAF\bin\appserver
```

**OBS: Caso possua** [**Slaves**](https://tdn.totvs.com/pages/viewpage.action?pageId=6064504) **ou** [**Brokers**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040589613-MP-FRAME-Como-realizar-uma-configura%C3%A7%C3%A3o-b%C3%A1sica-de-Broker-) **faça o processo nas pastas respectivas aos serviços deles.**

![Atualização binários TAF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19033194561047)

**5. Atualizando a dbapi.dll:**

Após a atualização dos binários iremos atualizar a [dbapi.dll](https://tdn.totvs.com/display/tec/Melhoria+-+Arquivos+do+pacote+do+DBAccess) do DBACCESS para que não tenha incompatibilidade futuramente.

Copie o arquivo dentro da pasta "Client" do DBAccess e cole nos binários que acabou de atualizar (pasta APP e APPSERVER do TAF).

```
Exemplo de caminho: C:\TAF\TafDbacess64\Client
```

![GIF dbapi.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19033194575767)

**6. Atualizando o Smart Client (desktop):**

O próximo passo é realizar a atualização do Smart Client.

Extraia o arquivo do Smart Client que foi baixado, copie todo o conteúdo dentro da pasta, depois cole e substitua nas pastas "smartclient" e "smartclient\_update" do seu servidor do TAF.

```
Exemplos de caminhos: C:\TAF\bin\smartclient e C:\TAF\bin\smartclient_update
```

![Atualização Smartclient TAF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19044671735831)

**7. Reiniciando os serviços**:

Agora que já atualizamos os artefatos do TAF/Protheus precisamos iniciar os serviços do DBACCESS e depois o serviço do APPSERVER-TAF para rodarmos a aplicação em modo exclusivo.

**OBS: Caso esteja utilizando Broker ou Slaves inicie somente a master para acesso exclusivo.**

![Iniciando serviço em modo exclusivo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19056901290903)

Se você utiliza [schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035743413-Automa%C3%A7%C3%A3o-Fiscal-Configura%C3%A7%C3%A3o-Como-configurar-o-TAF-para-transmitir-eventos-automaticamente-Schedule-para-o-eSocial) ou qualquer outro [job](https://tdn.totvs.com/display/tec/Jobs) que está iniciando junto com o seu serviço principal do TAF/Protheus, comente a chave [[OnStart]](https://tdn.totvs.com/pages/viewpage.action?pageId=6064858) localizada dentro do arquivo "appserver.ini" da sua instância principal.

```
Exemplo de caminho: C:\TAF\appserver\appserver.ini
```

**OBS: Para comentar uma chave basta colocar um " ; " a frente da chave, salvar o ini configurado e reiniciar o serviço.**

![onstart.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19056901297943)

**8. Aplicando os pacotes/patcht´s pelo VSCode:**

**8.1 Instalando o VScode (para clientes que ainda não possuem o VScode instalado):**

Com os serviços iniciados em modo exclusivo o próximo passo é instalar o VScode para aplicação dos pacotes.

Realize o download do VScode [Clicando aqui](https://code.visualstudio.com) e depois faça a instalação seguindo os passos abaixo:

Execute o programa do VScode baixado como administrador, aceite os termos e condições, escolha o local onde deseja instalar e depois avance até o término da instalação.

![Instalação VSCODE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19044671748887)

**8.2 Configurando o VScode:**

Depois da instalação do VScode iremos configura-lo para fazer a aplicação dos pacotes.

O primeiro passo é criar uma pasta para salvar suas configurações feitas no VScode.

Abra o VScode, acesse a opção "**arquivos**" ou "**files**", depois escolha a opção "**abrir pasta**" ou "**open folder**" e selecione a pasta onde deseja salvar as configurações.

**Recomendamos que você crie uma pasta dentro da sua estrutura do TAF chamada de "ADVPL".**

![Selecionar pasta VScode.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19067050903319)

Ao selecionar a pasta no VScode, será necessário baixar a [extensão da TOTVS](https://marketplace.visualstudio.com/items?itemName=totvs.tds-vscode).

Basta clicar no ícone ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19067063135127) e digitar no campo de pesquisa a palavra "TOTVS".

Instale a primeira opção chamada de **"TOTVS Developer Studio for VSCode (AdvPL, TLPP e 4GL)"** e abra a extensão após o término do download.

**OBS: A instalação pode demorar alguns minutos dependendo do desempenho da sua máquina.**

**![Baixando a extensão TOTVS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19067584393367)**

Ao abrir a extensão da TOTVS será necessário informar o seu Smart Client do ambiente que deseja aplicar os pacotes.

Selecione a primeira opção de "**escolher arquivo**" e abra o executável do seu Smart Client que está no seu servidor ou na estação de trabalho.

**OBS: Normalmente o executável está localizado no caminho padrão do sistema.**

```
Exemplos de caminhos: C:\TAF\bin\smartclient
```

**![Selecionando Smartclient no VSCODEgif.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19068623022103)**

Agora será necessário criar a conexão do seu servidor com o VScode.

Para isso, clique no botão ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19068623036183) do VScode e preencha os campos de acordo com as configurações do seu TAF.

![Configuração de conexão.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19068602282391)

Para saber quais são as configurações do seu TAF você deve acessar o seu arquivo "appserver.ini" e localizar o [nome do seu ambiente](https://tdn.totvs.com/pages/viewpage.action?pageId=6064764) e a [porta TCP](https://tdn.totvs.com/pages/viewpage.action?pageId=135496000).

```
Exemplo de caminho: C:\TAF\appserver\appserver.ini
```

**OBS: Normalmente o nome do seu ambiente é a primeira chave do seu ini e a porta TCP fica no final do arquivo ini.**

![Porta TCP e ambiente.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19068602286999)

Localizando o nome do seu ambiente e a porta TCP você deve preencher nos campos do VScode conforme exemplo abaixo:

![Exemplo de configuração VSCode.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19068623054871)

Ao preencher os campos conforme suas configurações basta clicar no botão "**Salvar/Fechar**".

Você notará que será criada uma conexão no canto superior esquerdo do VScode onde você deve clicar no ícone ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19069130312855) para realizar a comunicação entre sua aplicação e o VScode.

Ao clicar, será exibido um campo onde você deve preencher primeiro o **nome do seu ambiente** e depois o **usuário e senha do TAF**.

![Conexão VScode.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19069109360407)

Após o preenchimento, valide se o ícone da conexão ficou verde ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19069130339607) indicando que há conexão entre o VScode e o seu ambiente.

**8.3 Aplicando o pacote/patch pelo VScode:**

Agora basta clicar com o botão direito em cima da conexão, escolher a opção "Aplicar Pacote" ou "Patch Apply", selecionar os arquivos **.ptm** da pasta da LIB e Expedição contínua que foram baixados e clicar no botão **Aplicar/Apply** no VScode.

Você consegue validar se o pacote realmente foi aplicado visualizando a mensagem

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19069212607383)

![Aplicação de patch.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19069109374103)

**9. Atualizando o dicionário de dados (UPDDISTR):**

Depois da aplicação dos pacotes vamos atualizar o dicionário de dados do TAF.

Acesse a pasta "expedição contínua" que foi baixado, abra a pasta **SDF/BRA**, copie todo o conteúdo dentro desta pasta, depois cole e substitua os arquivos na pasta **Systemload** da sua estrutura do TAF.

```
Exemplo de caminho: C:\TAF\systemload
```

![SDF cópia.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19069376193175)

Após a substituição dos arquivos, acesse o UPDDISTR para realizar a atualização do dicionário do TAF.

Basta digitar UPDDISTR em Programa inicial na execução do SmartClient.

![Execução do UPDDISTR.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19069928735767)

Na tela do UPDDISTR você deve avançar e aceitar todos os termos, preencher o campo de usuário e senha do administrador do TAF e nas "**configurações de log**" você deve deixar marcado as opções abaixo:

![Usuário e senha do TAF.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19069942305559)

![Configurações de log UPDDISTR.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19070071381655)

**OBS: A atualização do dicionário pode demorar horas dependendo do tamanho do seu ambiente e do desemprenho do seu servidor.**

![Rodando o UPDDISTR.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19069942323607)

Pronto, seu TAF está atualizado !

**10. Atualizando as autocontidas (Wizard de Configuração do TAF):**

No primeiro acesso do TAF, após atualização, será necessário rodar as autocontidas, Wizard de Configuração TAF, siga as orientações da documentação abaixo:

[atualização das tabelas AUTOCONTIDAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034479973-Automa%C3%A7%C3%A3o-Fiscal-CONFIGURA%C3%87%C3%83O-Atualiza%C3%A7%C3%A3o-das-tabelas-autocontidas)

Caso ocorra algum erro nos processos passados, [entre em contato com o suporte do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18029297135127-Automa%C3%A7%C3%A3o-Fiscal-ROTINA-Como-entrar-em-contato-com-o-suporte-do-TAF-).
