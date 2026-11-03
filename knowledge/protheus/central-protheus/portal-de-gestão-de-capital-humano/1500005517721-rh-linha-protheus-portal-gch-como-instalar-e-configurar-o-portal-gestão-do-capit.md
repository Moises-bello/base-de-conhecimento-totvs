---
article_id: 1500005517721
category: Portal de Gestão de Capital Humano
content_hash: 810aabc2353ea3ca809db0b233946a0403317d95893d6cef377755a6d2c21045
fetched_at: '2026-06-28T22:42:58.949976+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Como instalar e configurar o Portal Gestão
  do Capital Humano
type: support-article
updated_at: '2023-06-03T22:00:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005517721-RH-Linha-Protheus-PORTAL-GCH-Como-instalar-e-configurar-o-Portal-Gest%C3%A3o-do-Capital-Humano
---

**Dúvida**Como instalar e configurar o Portal Gestão do Capital Humano?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Portal Gestão Capital Humano – Todas as versões  
  
**Solução**O **Portal Gestão do Capital Humano**, oferece acesso à uma ferramenta web para agilizar processos para seus participantes a fim de facilitar ações, tais como: Espelho de Ponto, Extrato de FGTS, Banco de Horas, Dados Cadastrais, Tabela de Honorário, Férias Programadas, Login, Avaliação de Desempenho, Consulta de Artefatos e Mapa de Treinamento.  
  
Para configuração deste módulo seguir os seguintes passos:  
  
**1-** Executar download do arquivo **WEB\_FILES** no Portal do Cliente e descompactar na pasta “**systemload**”, conforme orientações do artigo:  
[MP - PORTAL GCH - Como Atualizar os arquivos do Portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044250613-MP-PORTAL-GCH-Como-Atualizar-os-arquivos-do-Portal)  
  
**2-** Acessar o**“SRVWIZARD”**para abrir o visualizador oficial de **appserver.ini:**![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007936282/mceclip17.png)   
  
**3-** Na sessão**“Servidor Internet (HTTP/FTP)”** para configurar a porta de acesso:  
  
Os dados da configuração abaixo é apenas exemplo, será necessário configurar o ambiente, porta de conexão e link de acesso que utilizará o Portal.  
  
- Esta porta será a definição do URL de acesso no futuro.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007922802/mceclip2.png)

**4-** Acessar a pasta **“módulos web”****,**clicar em incluir e selecionar a opção**WS - Microsiga Protheus Web Services:****Módulo Web:** Será inserido o nome do módulo que será configurado, sendo neste caso o **WEB SERVICE**;

**Nome da Instância:** Nome da pasta que será criada para guardar os arquivos;

**Diretório Raiz das imagens ( Web Path):** Diretório raiz é preenchido automaticamente a partir do nome da instância;

**Selecione o Enviroment:** Nome do ambiente que será configurado o **WEB SERVICE;  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007923422/mceclip3.png)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007923502/mceclip4.png)**Após a configuração e clicar em avançar, será demonstrado o relacionamento de URL de acesso e empresas:  
Neste momento será incluso um link utilizando a porta que configuramos antes e relacionaremos com um vínculo de empresa/ filial.  
**Observação**: Sempre será necessário configurar um **web service** para cada empresa/filial e para acesso ao portal existem licenças específicas que necessitam da contratação do cliente.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007923602/mceclip5.png)  
  
Configurar a quantidade de usuários por consumo de licença por job de serviço do porta:  
Esses dados são avaliados pelo ESN (Executivo Serviços e Negócios) para efetuar a mensuração junto com a Infraestrutura da empresa para configurar a quantidade de acesso necessários.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007923782/mceclip6.png)  
  
**"WS" (Web Service)** Criado:  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008113001/mceclip7.png)  
  
**5-** Acessar novamente a pasta **“módulos web”,**clicar em incluir e selecionar a opção**Portal Protheus (PP):**A única diferença é que agora você deverá informar o URL do **web service** contendo**“HTTP://”** para que o job encontre as informações do **web service.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007923422/mceclip3.png)  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008115241/mceclip8.png)  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007927402/mceclip9.png)  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008115421/mceclip10.png)  
  
"PP" (Portal Protheus)** criado:  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007927562/mceclip11.png)  
  
**6-** Reiniciar o Server:  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007934742/mceclip12.png)  
 **7-** Observar que no **appserver.ini** será criado automaticamente a configuração do Portal:  
  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008123141/mceclip13.png)  
  
**8-** Acessar e testar aos links de Web Service e Portal Protheus:  
  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007934982/mceclip14.png)  
  
![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008123321/mceclip15.png)  
  
**9-** Será necessário descompactar o arquivo MSRELRDZ.ini na pasta system, no artigo abaixo consta o arquivo e orientação:  
[MP - PORTAL GCH - Arquivo MSRELRDZ.ini](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059317533-MP-PORTAL-GCH-Arquivo-MSRELRDZ-ini)  
  
Será criado o arquivo de configuração **MSRELRDZ.INI**- Este arquivo garante o relacionamento entre os funcionários (SRA) e os participantes (RD0) pelo código do CPF.  
  
**Observação:** Necessário verificar o compartilhamento das tabelas AI3, AI6 (mesmo compartilhamento), AI7, AI8 e AI9 (mesmo compartilhamento, porém podem ser diferentes da AI3 e AI6).  
  
**10-** Acesse o Protheus, no módulo SIGATCF (terminal de consulta do funcionários) e entre na rotina Atualizações > Configurações > Web Services.  
Clique na opção “Automático” para que sejam carregados todos os métodos do WEB SERVICE:  
  
![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007936902/mceclip18.png)  
  
**11-** Crie um usuário para os Participantes no módulo SIGATCF - Terminal de consulta do Funcionário. Entre na rotina Atualizações > Configurações > Usuários > Genéricos, consulte o artigo para orientações:   
[Criação de usuário para acesso ao Portal RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052354513-RH-Linha-Protheus-PORTAL-GCH-Como-criar-usu%C3%A1rio-para-relacionar-os-Participantes-no-Portal-GCH#:~:text=Como%20criar%20usu%C3%A1rio%20para%20relacionar%20os%20Participantes%20no%20Portal%20GCH%3F&text=Clique%20na%20op%C3%A7%C3%A3o%20Outras%20A%C3%A7%C3%B5es,Portal%20Gest%C3%A3o%20do%20Capital%20Humano)  
  
**12-** Ainda no módulo SIGATCF, entre na rotina Atualizações > Configurações > Menus, somente para carregar os menus do Portal:  
  
![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008125401/mceclip19.png)  
  
**13-** Agora acesse o módulo SIGAAPD (Avaliação e Pesquisa de Desempenho), entre na rotina atualizações > Participantes > Cadastro.  
  
Esta rotina efetua o relacionamento dos participantes, onde será criado um vínculo de todos os funcionários e os colocarão como participantes.  
Vale lembrar que poderão relacionar somente os funcionários ativos ou todos. Verifique o artigo com orientações:   
[MP - PORTAL GCH - Como associar o Usuário do Portal ao Cadastro de Participante para acesso ao Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051581834-MP-PORTAL-GCH-Como-associar-o-Usu%C3%A1rio-do-Portal-ao-Cadastro-de-Participante-para-acesso-ao-Portal-GCH)  
  
**14-** Volte no módulo SIGATCF (Terminal Consulta do Funcionário) e acesse a rotina Atualizações > Configurações > Usuários > Manutenção:  
  
Nesta opção será gerado a primeira senha de acesso do usuário a partir dos dois últimos dígitos do ano de nascimento do funcionário + dia de admissão + 2 últimos dígitos do CPF. Verifique o artigo com orientações:  
[MP - PORTAL GCH - Como “Iniciar usuário” e “Gerar Senhas” para o primeiro acesso ao Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051582414-MP-PORTAL-GCH-Como-Iniciar-usu%C3%A1rio-e-Gerar-Senhas-para-o-primeiro-acesso-ao-Portal-GCH)  
  
Após realizar todas as configurações acima, acesse o Portal GCH e entre com Usuário e Senha criados, no primeiro acesso ao portal será apresentado a tela de Login Unificado, verifique o artigo:  
[MP - PORTAL GCH - Ao realizar o login no portal pela primeira vez apresenta a mensagem \*Ret001\* : Informe novo login unificado de acesso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045692813-MP-PORTAL-GCH-Ao-realizar-o-login-no-portal-pela-primeira-vez-apresenta-a-mensagem-Ret001-Informe-novo-login-unificado-de-acesso)  
  
**15-** Ao entrar no Portal GCH será apresentado desta forma:  
  
![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008123761/mceclip16.png)  
  
**Saiba Mais**[Artigos Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano#)
