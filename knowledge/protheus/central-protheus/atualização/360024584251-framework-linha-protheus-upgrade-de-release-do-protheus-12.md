---
article_id: 360024584251
category: Atualização
content_hash: b3abaa93d4e99d46b3c65a0686b2eada4b61721ae333e379ace00ccb22522ecd
fetched_at: '2026-06-28T22:42:21.291712+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Upgrade de Release do Protheus 12
type: support-article
updated_at: '2026-01-27T19:46:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024584251-Framework-Linha-Protheus-Upgrade-de-Release-do-Protheus-12
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22339584893463)*** Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como efetuar o Upgrade entre *Releases* do **Protheus 12**?  
  
**Ambiente**  
Totvs Backoffice - Cross Segmentos (Linha Protheus) - AppServer - A partir da versão 12.  
  
**Solução**  
**1. Preparando a base para o upgrade**  
Faça uma cópia fria, com os serviços parados da pasta raiz do **Protheus**, ex.: **C:\TOTVS 12\** e do Banco de Dados.

**2. Checando duplicidades na base**  
Caso sua Base de Dados seja Relacional, utiliza **DBACCESS**, será necessário rodar o processo de verificação dos registros duplicados para todas as empresas. Assistente executado a partir da rotina **CHECKDUPL** via **Configurador**, que tem como pré-requisito a atualização do dicionário de dados padrão na pasta **SYSTEMLOAD**. Para fazer o download do dicionário, siga os procedimentos do seguinte *link*:  
[Atualizar o Dicionário de Dados do Protheus 12](http://tdn.totvs.com/pages/viewpage.action?pageId=271415266)  
  
Crie dentro da pasta **Protheus\_Data**, a pasta **UPGRADE** e nela descompacte o dicionário de dados Completo da release para a qual vai executar *upgrade*. Na verificação de duplicidade será solicitado o **SX2.UNQ**, utilize este como referência para a checagem.  
Vide Instruções para verificação de duplicidades no *link*: [Rotina CheckDupl – Verifica a Integridade de Registros Duplicados](http://tdn.totvs.com/pages/viewpage.action?pageId=242386686)  
  
**3. Atualizando os arquivos**  
É necessário atualizar os arquivos de dicionário de dados, Completo e Diferencial, da versão da *release* que deseja atualizar, e também o **RPO - Repositório de Objetos** da mesma versão. Para atualizar os dicionários, siga o procedimento do seguinte *link*: [Atualizar o Dicionário de Dados do Protheus 12](http://tdn.totvs.com/pages/viewpage.action?pageId=271415266)  
  
Para atualizar o **RPO**, siga o procedimento abaixo:  
1- Acesse o site do Suporte: [Downloads e Atualizações](https://suporte.totvs.com/download)  
2- Linha Protheus;  
3- **MICROSIGA PROTHEUS VERSÃO 12.1.XX**, onde XX é a versão da nova *release;*  
4- **PROTHEUS 12 TOPCONNECT PORTUGUES**;  
5- Categoria: **Repositório de objetos**;  
6- Baixar o repositório multiidioma **TTTM120**.  
  
**ATUALIZAR**  
1- Pare o serviço do **Protheus**;  
2- Na pasta **APO**, renomear o repositório anterior, ou mover para outra pasta;  
3- Copiar o novo arquivo para o diretório **APO** do sistema;  
4- Renomear o arquivo mantendo apenas os últimos 7 caracteres **Exemplo: tttm120.rpo**;  
  
 Após trocar o **RPO**, é necessário atualizar a **LIB** baixando e aplicando a mais recente do Portal. *Link* com os procedimentos de atualização: [Atualização básica do Protheus 12](http://tdn.totvs.com/pages/viewpage.action?pageId=271651871)

**Informação**  
Se você utilizar o **Appserver** em **Linux**, transfira o arquivo compactado para o **Linux**, e só descompacte-o no **Linux**. Descompactar o arquivo no **Windows** e depois transferir o **.txt** para o **Linux** pode causar erros.  
Ao preparar o ambiente para o *upgrade*, não é recomendável abrir o **Protheus** após atualizar os arquivos, mas sim, rodar direto o **compatibilizador - UPDDISTR**.  
  
**4. Executando o compatibilizador de upgrade de release**  
Abra o **Smartclient**, e no Programa Inicial, digite: **UPDDISTR**  
Maiores detalhes sobre a funcionalidade do **UPDDISTR** podem ser encontrados neste *link*: [Atualizador de dicionário e base de dados - UPDDISTR](http://tdn.totvs.com/pages/viewpage.action?pageId=181965468)

![](http://tdn.totvs.com/download/attachments/286020348/image2021-4-30_15-15-26.png?version=1&modificationDate=1632245721913&api=v2 "Linha Microsiga Protheus > Upgrade de Release do Protheus 12 > image2021-4-30_15-15-26.png")

A partir do pacote de **LIB** disponibilizado em 07/04/2016 será possível escolher quais Grupos de Empresas serão considerados na atualização. Será exibida uma janela onde é possível marcar os Grupos de Empresas desejados. Por padrão, todos os grupos já vem selecionados. Se desejar utilizar todos os grupos, basta clicar no botão **OK**.  
Caso uma dada migração seja reiniciada, deve-se escolher exatamente os mesmos grupos de empresas para retomar o processo.

![](http://tdn.totvs.com/download/attachments/286020348/image2021-4-30_15-16-5.png?version=1&modificationDate=1632245722793&api=v2 "Linha Microsiga Protheus > Upgrade de Release do Protheus 12 > image2021-4-30_15-16-5.png")

Algumas tabelas não possuem grupo de empresas em seu nome, logo essa configuração não terá efeito sobre elas. Os arquivos de **help**, por exemplo, são compartilhados por todos os Grupos de Empresas de dado **STARTPATH**. Dessa forma, o arquivo compartilhado será atualizado.  
Após a chamada, será exibido um assistente de atualização. A primeira tela traz um informativo dos requisitos para iniciar a atualização. As telas seguintes possuem um Termo de Aceite, que deve ser lido com atenção e marcadas as devidas caixinhas de confirmação. Atente-se também em selecionar a localização correta, país que será utilizada na atualização.

![](http://tdn.totvs.com/download/attachments/286020348/IMG_2990.gif?version=1&modificationDate=1632245723342&api=v2 "Linha Microsiga Protheus > Upgrade de Release do Protheus 12 > IMG_2990.gif")

Após o Termo de Aceite confirmado, será aberta a janela de login para confirmação de autorização a executar o **UPDDISTR**. A autorização só é concedida para o usuário Administrador do **Protheus**, ou para usuários do Grupo Administradores¹ que possuam o [acesso 194](https://tdn.totvs.com.br/pages/viewpage.action?pageId=221546134) habilitado. O usuário e senha serão validados ao clicar no botão **Avançar**.

¹ *Grupo Administradores com acesso 194 permitido a partir da LIB versão 20210517*

Também é possível nesta tela:

* Configurar se a execução será apenas uma Simulação, onde nenhuma alteração será efetivada na base;
* Determinar se o dicionário de índices é exclusivo por grupo de empresas, SIX ou se é utilizado o dicionário **SINDEX**.

![](http://tdn.totvs.com/download/attachments/286020348/2021-08-04_2997_10h24.png?version=1&modificationDate=1632245726737&api=v2 "Linha Microsiga Protheus > Upgrade de Release do Protheus 12 > 2021-08-04_2997_10h24.png")

Clique em **Avançar**. Na tela seguinte serão exibidas informações sobre o pacote de atualização encontrado na base, que será utilizado neste processo.

![](http://tdn.totvs.com/download/attachments/286020348/2021-08-04_2998_10h24.png?version=1&modificationDate=1632245726939&api=v2 "Linha Microsiga Protheus > Upgrade de Release do Protheus 12 > 2021-08-04_2998_10h24.png")

Clique em **Avançar**. Na próxima tela deve-se informar o diretório de dados **X2\_PATH** para cada Grupo de Empresas para as novas tabelas a serem inseridas pela atualização. No caso de Bases de Dados SQL - **Top Connect**, não é necessário informar o diretório.

![](http://tdn.totvs.com/download/attachments/286020348/image2021-4-30_15-53-59.png?version=1&modificationDate=1632245727331&api=v2 "Linha Microsiga Protheus > Upgrade de Release do Protheus 12 > image2021-4-30_15-53-59.png")

Avance novamente. Na tela de **Configuração de execução do Update**, deve-se marcar/desmarcar as configurações e arquivos de log que deseja utilizar durante o processo. Indicamos manter apenas as opções **Log de Atualização**,  **Log de Critical Error** e **Corrigir erros automaticamente**habilitadas, lembrando que a opção de corrigir os erros automaticamente executará as alterações de base pelo próprio Sistema. **NÃO** marque a opção **Manter o arquivo de log existente**.

![](http://tdn.totvs.com/download/attachments/286020348/image2021-5-3_10-45-11.png?version=1&modificationDate=1632245727788&api=v2 "Linha Microsiga Protheus > Upgrade de Release do Protheus 12 > image2021-5-3_10-45-11.png")

Ao avançar, será exibida uma janela confirmando quais grupos de empresas serão processados e quais operações serão executadas. Em seguida será efetuada uma análise da base de dados existente. A análise verificará diversos fatores, como por exemplo a consistência da base de dados em relação ao dicionário existente. Se forem encontrados problemas, os mesmos deverão ser corrigidos antes que a atualização possa prosseguir.

![](http://tdn.totvs.com/download/attachments/286020348/image2021-5-3_10-46-26.png?version=1&modificationDate=1632245728011&api=v2 "Linha Microsiga Protheus > Upgrade de Release do Protheus 12 > image2021-5-3_10-46-26.png")

Deve-se notar que nesta fase é analisado apenas o conteúdo da Base de Dados e do Dicionário já existente. Nesse momento não é efetuada nenhuma consulta ao dicionário de dados diferencial que se pretende aplicar.  
Caso não existam erros ou os mesmos já tenham sido corrigidos a atualização iniciará logo após o processo de verificação. Deve-se aguardar o final da atualização e encerrar.  
  
Atualização importante de Controle de aplicação de pacotes no **UPDDISTR**, a partir da **LIB** versão **20211004**, *Release* **33**: [Controle de aplicação de pacotes no UPDDISTR](https://tdn.totvs.com/pages/viewpage.action?pageId=631622379)  
  
Caso o **Upgrade** possua erros, será exibida uma janela com os logs dos erros, que devem ser corrigidos na base antes de continuar. Segue abaixo *link* com as correções de erros mais comuns em Migrações/Upgrades: [Erros críticos mais comuns em migrações](http://tdn.totvs.com/pages/viewpage.action?pageId=271414000)  
  
Caso o erro não esteja listado, é necessário abrir um ticket para o **Suporte Framework** através do Portal do Cliente.  
Ao final do **Upgrade**, será exibida uma janela com a informação "O processo de atualização foi finalizado com sucesso."

![](http://tdn.totvs.com/download/attachments/286020348/2017-08-08_15-42-24.png?version=1&modificationDate=1502287639000&api=v2 "Linha Microsiga Protheus > Upgrade de Release do Protheus 12 > 2017-08-08_15-42-24.png")

Para confirmar, acesse o **Configurador**, tecle **Shift+F6**, e confira a **Release do RPO**.

![](http://tdn.totvs.com/download/attachments/286020348/2017-08-08_15-43-43.png?version=1&modificationDate=1502287639000&api=v2 "Linha Microsiga Protheus > Upgrade de Release do Protheus 12 > 2017-08-08_15-43-43.png")

Segue link comdocumentação detalhada sobre o Upgrade de Release:

* [Upgrade de Release do Protheus 12](https://tdn.totvs.com/display/framework/Upgrade+de+Release+do+Protheus+12)
