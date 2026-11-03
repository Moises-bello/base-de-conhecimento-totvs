---
article_id: 21746957789463
category: Materiais - Compras (SIGACOM)
content_hash: 2bd3a2aaadc030036e28f037ccbf96163d68112f938d489ca1a3f275fd69862a
fetched_at: '2026-06-28T22:41:14.526453+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o SmartView
  ?
type: support-article
updated_at: '2024-10-21T21:12:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21746957789463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-o-SmartView
---

Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como fazer para configurar o SmartView?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**Já temos disponível um passo a passo em vídeo:

* [How To: Configuração do Smart View - Parte 1/3 (Rest + Instalação)](https://youtu.be/YIwdqo1Ix9s?si=kVwE54yuhKfIq9Ug)
* [How To:](https://youtu.be/YIwdqo1Ix9s?si=kVwE54yuhKfIq9Ug) [Configuração do Smart View - Parte 2/3 (Dados de Conexão)](https://youtu.be/QAiWcWKwjyk?si=Hnkx6rnTtLWbdE4Z)
* [How To:](https://youtu.be/YIwdqo1Ix9s?si=kVwE54yuhKfIq9Ug) [Configuração do Smart View - Parte 3/3 (Conectores + Token Protheus)](https://youtu.be/-Ui6W2gc3Pg?si=5i1l9nq1fIy5By2-)

**1º passo: Configurar o REST**

Caso você ainda **NÃO** tenha o REST configurado no seu ambiente, siga as orientações da documentação: [Configuração básica REST do protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045401793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Configura%C3%A7%C3%A3o-b%C3%A1sica-REST-do-protheus)

*Não se esqueça de ajustar o parâmetro ENVIRONMENT para o nome do seu ambiente.*

 

Para confirmar que o REST está no ar, acesse seu navegador e basta inserir o caminho do rest (Contendo o IP e a Porta) e validar se o sistema exibe a tela:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22020059752471)

Essa validação de usuário e senha só vai aparecer quando a chave SECURITY = 1, conforme print abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22020059783447)

 

**2º passo: Instalação do SmartView**

* Faça o download do instalador do **SmartView** neste [link](https://smart-view.totvs.app/api/update-manager/releases/treports.agent-installer/win-x64/latest/download)
* 2. Extrair todo o conteúdo do arquivo zip e executar o arquivo **SMARTVIEW.AGENTINSTALLER.EXE** ;
* 3. Selecione o diretório de instalação e prossiga para a próxima etapa. Recomendamos que a instalação seja feita no diretório **C:\TOTVS** ;
* 4. O instalador irá realizar a instalação na pasta **SMART-VIEW**, criada automaticamente no diretório selecionado;
* 5. Caso o diretório **SMART-VIEW** já exista, o instalador perguntará se deseja sobrescrever a instalação anterior, caso não queira, um novo diretório deverá ser informado;
* 6. Após a instalação o **SmartView** encontra-se pronto para configuração no próximo passo.

**3º passo: Configurar o SmartView**

Acesse o endereço *http://{ip cadastrado}:7019/startup* no seu navegador (por exemplo: *http://localhost:**7019**/startup ou http:/162.1.111:**7019**/startup*). Irá abrir a tela abaixo.

*\*7019 é uma porta padrão para startup escolhida pelo desenvolvimento*

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22020081154071)

 

Ao clicar em "Vamos lá?", vai ir para a página do print abaixo. Nessa página, teremos que informar os dados de acesso ao **Smart View**, *o provedor de segurança*:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22020081168151)

* **Nome do Provedor:** Pode escolher qualquer nome. (exemplo protheus)
* **Endereço de Descoberta:** Insira o endereço de seu REST + o texto: /.well-known/treports/security  
  (por exemplo http://localhost:8085/rest/.well-known/treports/security. No lugar de localhost pode ser digitado também o ip cadastrado. A porta digitada nesse endereço deve ser a mesma que foi cadastrada no parâmetro Port da tag [HTTPREST] no appserver.ini )
* **Recuperar Emissor:** Clique nessa opção, após os preenchimentos acima, e preencha o usuário e senha de acesso. Precisa ser um usuário Administrador e a senha não pode ser em branco.

Após as confirmações basta "Avançar"

Na próxima tela, terá que preencher os dados do *servidor de licença* do SmartView

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22020081198103)

* **Ip do servidor:** Ip do License Client que possui configurado em seu AppServer.ini dentro da tag [LICENSESERVER]
* **Porta:** Porta do License Client que possui configurado em seu AppServer.ini dentro da tag [LICENSESERVER]
* **CNPJ**: CNPJ da empresa

 Após as confirmações basta "Avançar"

 

Na próxima tela, irá preencher as informações referente o *Armazenamento de Dados:*

Primeiro selecione o banco que deseja e clique em "Configurar"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22020081210135)

Na tela abaixo vamos indicar o Banco de Dados do seu ambiente, mas terá que possuir a senha do sa ou de um usuário com permissão de administrador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22020081218327)

Campos a preencher:

* Data Source: Nome do Servidor do seu Banco de Dados, pode ser obtido Acessando o Banco;
* Initial Catalog: Esse é o nome do seu Banco de dados, pode ser obtido Acessando seu Banco;
* User Id: Nome do Usuário administrado do seu Banco de Dados (Exemplo: sa);
* Password: Senha do usuário administrador do Banco de Dados.

Após a configuração, basta clicar em "Concluir"

 

Realize a configuração abaixo para a nova interface de visualização do Protheus.

* Acesse seu AppServer.ini e abra o arquivo;
* Na seção [ Drivers ] insira as chaves [MULTIPROTOCOLPORT=1 e MULTIPROTOCOLPORTSECURE=0](https://tdn.totvs.com/download/attachments/817636770/Drivers.png?version=1&modificationDate=1704226787577&api=v2)
* Na seção [ General ] insira a chave [APP\_ENVIRONMENT=Nome do seu ambiente](https://tdn.totvs.com/download/attachments/817636770/General.png?version=1&modificationDate=1704226960827&api=v2)

Após esses ajustes, será necessário reiniciar o Server.

 

**4º passo: Conectores**

Clique no botão "Abrir o Smart View" do print acima ou acesse <http://localhost:7017/login> *(http://{ip configurado}:7017/login)*

*\*7017 é uma porta padrão para login escolhida pelo desenvolvimento*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22020081262871)

 

Logue usando o usuário administrador e a senha *(não pode ser em branco)* e clique em "Conectores".

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22020081276695)

Após isso, clique em uma das duas opções abaixo para incluir.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22020081283735)

Campos a preencher:

* Nome: Nome do Conector Nativo, pode ser qualquer nome;
* Endereço: Inserir o [endereço do REST](https://tdn.totvs.com/download/attachments/817636770/Conector%20REST.png?version=1&modificationDate=1704229170820&api=v2) configurado no ambiente; *exemplo http://[host]:[porta do rest]/[uri protheus] (http://localhost:8085/rest)*
* Testar Conexão: Clique nesta opção para que o Conector valide o [acesso ao REST](https://tdn.totvs.com/download/attachments/817636770/Conector%20Funcionando.png?version=1&modificationDate=1704229359373&api=v2);

Clique em "Salvar".

 

**5º passo: SIGACFG**

Acesse o SIGACFG para configurar o "Tipo de Autenticação" e a "URL Base Smart View". Selecione a opção "**Ambiente**", depois a Opção "**Cadastros**" e por fim a opção "**[Configuração Smart View](https://tdn.totvs.com/download/attachments/817636770/Config%20SIGACFG.png?version=1&modificationDate=1704229699447&api=v2)**" (Caso esteja no Release 2210, provavelmente estará com o nome "**Configuração TReport**", mas é a mesma rotina).

* **Tipo de Autenticação:** Selecione a opção ["Token Protheus"](https://tdn.totvs.com/download/attachments/817636770/Tipo%20de%20Autentica%C3%A7%C3%A3o.png?version=1&modificationDate=1704229867910&api=v2) e vai avançar;
* **URL Base Smart View:** Informe o endereço cadastrado no **4º passo: Conectores (<http://localhost:7017>)**
* **Testar Conexão:** Ao clicar nessa opção, o sistema deve apresentar a mensagem ["Teste da conexão realizado com sucesso!"](https://tdn.totvs.com/download/attachments/817636770/Teste%20Conex%C3%A3o.png?version=1&modificationDate=1704230147300&api=v2)

Após isso, basta "Confirmar".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22559348757911)

 

***6º passo: Conclusão***

Após estas configurações, basta acessar o módulo que deseja visualizar a visão no Smart View e selecionar a opção "Consultas" e a opção "Smart View", basta selecionar a visão que deseja acessar!

As visões já disponibilizadas no padrão (A partir do Release 12.1.2310) podem ser consultados na página:

* [Smart View - Compras](https://tdn.totvs.com/x/x_b0L)

   
***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
