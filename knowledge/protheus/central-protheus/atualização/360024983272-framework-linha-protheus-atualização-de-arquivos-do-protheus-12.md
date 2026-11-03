---
article_id: 360024983272
category: Atualização
content_hash: f459a7533cc4b06c424984caeb9287b72aceb7c223be8a74a9ebbba603e46c58
fetched_at: '2026-06-28T22:42:21.306928+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus - Atualização de arquivos do Protheus 12
type: support-article
updated_at: '2026-01-27T19:50:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024983272-Framework-Linha-Protheus-Atualiza%C3%A7%C3%A3o-de-arquivos-do-Protheus-12
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23632344255255)*** Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Como efetuar a atualização básica dos arquivos do **Protheus**?  
  
**Ambiente**  
Totvs Backoffice - Cross Segmentos (Linha Protheus) - Atualização - Todas as versões.  
  
**Solução**  
Segue abaixo caminho para baixar as principais atualizações do **Protheus**, baseando-se em uma base **Protheus** **12 Top Connect** em Português. Se sua base for diferente, selecionar as pastas conforme sua base.  
  
1- Binário;  
2- **LIB**;  
3- *Patches* acumulados.  
  
Os *patches* são atualizações pontuais dos módulos. É necessário verificar com cada módulo a necessidade e disponibilidade dessas atualizações.  
  
Na eventual necessidade de recompilar fontes no **RPO - Repositório de Objetos Protheus**, deve-se atualizar os Includes, conforme caminho abaixo:  
  
**BAIXAR**  
Acesse o site do Suporte: [Downloads e Atualizações](https://suporte.totvs.com/download) > Linha **Protheus** > **TOTVSTEC-FRAMEWORK** > **INCLUDES** > Baixar o pacote **INCLUDES VERSÃO 12.**  
  
**ATUALIZAR**  
Localize a pasta de **Includes** do seu ambiente > faça um *backup* desta pasta > descompacte o pacote nesta pasta, substituindo os arquivos.  
  
Para baixar os arquivos, acesse: [Downloads e Atualizações](https://suporte.totvs.com/download)  
  
**CERTIFIQUE-SE SEMPRE QUE ESTÁ BAIXANDO O ARQUIVO REFERENTE A SUA VERSÃO DE SISTEMA E LOCALIZAÇÃO.**  
  
**DOWNLOAD Binário - AppServer**  
Linha **Protheus** > **TOTVSTEC-FRAMEWORK** > **APPSERVER** > Baixar o binário referente ao seu Sistema operacional.  
  
**ATUALIZAR**  
Fazer um *backup* da pasta **BIN** > descompactar o arquivo baixado > copiar o conteúdo da pasta **Appserver\_x32** do arquivo baixado para dentro da pasta **Appserver\_x32** do **Protheus**, substituindo os arquivos quando solicitar.  
  
**DOWNLOAD Binário Lobo Guará - AppServer 64 bits**  
 Necessário ao utilizar a *Release* 12.1.23  
Acesse o portal: [Central de Relacionamento TOTVS](https://suporte.totvs.com) > Clique em *downloads* > na opção **Outras Linhas de Produto** selecione **Protheus** > seleciona na lista ao lado **TOTVSTEC-FRAMEWORK** > selecione **Appserver** > no canto superior direito da página, na opção **Filtro de Pacotes**, clique em **Todos Pacotes** **Disponíveis** > baixe o **Appserver LOBO GUARA VERSÃO 12** de acordo com seu Sistema operacional > volte um nível e selecione **Smartclient** > baixe o **Smartclient** **VERSÃO 12X64** de acordo com seu Sistema operacional.  
  
**ATUALIZAR**  
Fazer um backup da pasta **BIN** > na pasta **BIN**, renomear a pasta **APPSERVER** e **SMARTCLIENT** > descompactar os arquivos baixados > copiar o arquivo **appserver.ini** da pasta **APPSERVER** renomeada e colar na pasta **APPSERVER** descompactada > copiar o arquivo **smartclient.ini** da pasta **SMARTCLIENT** renomeada e colar na pasta **SMARTCLIENT** descompactada.  
  
**DOWNLOAD Binário - SmartClient**  
Linha **Protheus** > **TOTVSTEC-FRAMEWORK** > **SMARTCLIENT** > baixar o binário referente ao seu Sistema operacional.  
  
**ATUALIZAR**  
Fazer um *backup* da pasta **BIN** > descompactar o arquivo baixado > copiar o conteúdo da pasta **Smartclient** do arquivo baixado para dentro da pasta **Smartclient** do **Protheus** e de cada estação *client*, substituindo os arquivos quando solicitar > copiar o conteúdo da pasta **smartclientActiveX** do arquivo baixado para dentro da pasta **SmartClientActivex** do **Protheus**, substituindo os arquivos quando solicitar.  
  
**DOWNLOAD Patch de Programa - LIB**  
Linha **Protheus** > **TOTVSTEC-FRAMEWORK** > **LIB** > Em **Idioma** selecione o idioma do seu Sistema, para filtrar os arquivos apenas da sua linguagem > baixar a **LIB\_P12** referente ao seu tipo de base, se utilizar banco de dados relacional, deverá utilizar o arquivo **LIB\_P12 - TOPCONNECT**.  
  
**ATUALIZAR**  
Descompactar esse arquivo em alguma pasta dentro do diretório **Protheus\_Data** e efetuar a aplicação do mesmo via **TOTVS Developer Studio**.  
  
**DOWNLOAD Patches Acumulados:**  
[MP - BD0086 - Qual o link direto para pesquisar e baixar o pacote acumulado do Portal do Cliente?](http://tdn.totvs.com/pages/viewpage.action?pageId=286519628)  
  
**DOWNLOAD DBAccess**  
[DBAccess: Como atualizar](https://tdn.totvs.com/display/PROT/DBAccess%3A+Como+atualizar)  
  
**DOWNLOAD SmartClient para MAC**  
Linha **Protheus** > **TOTVSTEC-FRAMEWORK** > **SMARTCLIENT** > baixar o **SmartClient** para Sistema **MAC OSX AA-MM-DD-P12-SMARTCLIENT\_MAC.ZIP.**  
  
**DOWNLOAD SmartClient HTML**  
Linha **Protheus** >**TOTVSTEC-FRAMEWORK** > **SMARTCLIENT** > baixar o **SmartClient HTML** referente ao seu Sistema operacional e versão do binário **AA-MM-DD\_SMARTCLIENT\_HTML\_Release\_SistemaOperacional.ZIP.**  
  
**ATUALIZAR**  
Para atualizar, basta desinstalar a versão atual, se houver e efetuar a instalação da nova versão baixada através do instalador executável.  
  
**Importante**  
Efetuar *backup* do diretório principal do Sistema **C:\TOTVS12**, por exemplo, antes de iniciar o procedimento, com todos os serviço parados.  
Caso ninguém na empresa já tenha efetuado esse procedimento, recomendamos o agendamento de um analista da **TOTVS**.
