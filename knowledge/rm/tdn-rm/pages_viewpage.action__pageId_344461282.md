---
content_hash: 22c96717bda92806f8d9d4c8636ebbb836e1d2ef0707ab08acdf004ec87c5734
fetched_at: '2026-06-29T00:08:53.183461+00:00'
page_id: '344461282'
product: rm
source: tdn-rm
title: Guia de atualização via TOTVS Developer Studio - TAF (TOTVS Automação Fiscal)
  e TSS (TOTVS Service SOA)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344461282
version: 34
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é auxiliar os clientes da linha RM na atualização do **TAF - TOTVS Automação Fiscal** e **TSS - TOTVS Service SOA** utilizando a ferramenta **TOTVS Developer Studio**.

# Tipos de Arquivos disponíveis para atualização

---

       Existem três extensões de arquivos para atualização do TAF e do TSS:

* RPO
* PTM
* TXT

       Antes de realizar a atualização, identifique a qual aplicativo a mesma está relacionada.

# Atualização do RPO

---

Se o seu arquivo de atualização possuir a extensão **.rpo**, verifique a qual aplicativo ele pertence, antes de prosseguir com a atualização.

**Importante:** No momento da atualização, os serviços pertinentes ao TAF e ao TSS deverão estar parados nos serviços do Windows.

Atualização RPOVerificação de sistema TAF

Na tela de download é possível identificar o sistema que será atualizado. Veja o **exemplo** abaixo:

Download arquivo TAF:

Atualização RPO - TAF

Após certificar-se que se trata de um RPO do TOTVS Automação Fiscal, acesse o diretório apo na pasta de instalação do sistema (C:\totvs\TAF\apo) e crie uma pasta com o nome "Backup".

Mova o arquivo antigo para este diretório (C:\totvs\TAF\apo\Backup). Em seguida coloque o novo arquivo no diretório (C:\totvs\TAF\apo).

Verificação de sistema TSS

Na tela de download é possível identificar o sistema que será atualizado. Veja o **exemplo** abaixo:

Download arquivo TSS:

Atualização RPO - TSS

Após certificar-se que se trata de um RPO do TSS - TOTVS Service SOA, acesse o diretório apo na pasta de instalação do sistema (Por padrão, o mesmo é instalado em C:\totvssped\apo, porem alguns clientes utilizaram o caminho C:\totvs\TAF\totvssped\apo, como consta no documento de instalação) e crie uma pasta com o nome "Backup".

Mova o arquivo antigo para este diretório (...totvssped\apo\Backup). Em seguida coloque o novo arquivo no diretório (...totvssped\apo).

# Atualização do TAF utilizando o Devstudio.exe - Arquivo .ptm

---

**Importante:** Antes de realizar a atualização, certifique-se que o arquivo que será utilizado corresponde ao ambiente utilizado.

Recomendamos que seja utilizado o arquivo com o nome igual ou terminado em ...**TTTP120.PTM** para ambientes em português da linha RM.

Atualização TAF1º Passo

Crie uma pasta com o nome “Atualização” (ou outro de sua preferência) no caminho C:\totvs\TAF e extraia os arquivos que serão utilizados para a atualização do sistema.

2º Passo

Pare o serviço do TAF-WS nos serviços do Windows.

Caso o serviço não seja parado automaticamente, apresentando a mensagem abaixo, realize o procedimento indicado na aba “Dica!” antes de prosseguir:

Dica!

Procedimento para parar o serviço através do DOS:

Acesse o “Gerenciador de tarefas do Windows” > aba “Serviços” e localize o código PID do mesmo.

No prompt de comando do DOS (cmd) digite: taskkill /pid XXXX /f (onde XXXX é o PID do serviço) e tecle “Enter”. Neste momento o serviço será interrompido.

Realizado o procedimento de parada do serviço, voltamos para a atualização do sistema.

3º Passo

Acesse o diretório C:\totvs\TAF\bin\smartclient, localize o aplicativo devstudio.exe no diretório C:\totvs\TAF\bin\smartclient e execute. A tela abaixo será apresentada. Clique em “Ok” para que o sistema seja executado.

4º Passo

Neste momento o sistema que será utilizado para a atualização será aberto. Caso a informação referente ao “Ambiente” a ser atualizado esteja em branco, conforme imagem abaixo, siga os procedimentos para a configuração do mesmo. Caso já esteja preenchida com a informação “TAF”, vá para o "9º Passo".

5º Passo

Acesse o menu “Arquivo > Configurações” para que a tela de apontamento do ambiente seja apresentada.

6º Passo

Na tela de “Configurações de Compilação”, clique em “Adicionar” e preencha as informações exatamente como no exemplo abaixo clique em “Ok”:

7º Passo

Após a realização da configuração anterior, a tela abaixo será apresentada, clique em “Ok” para finalizar a configuração:

8º Passo

Verifique se a informação referente a configuração realizada será apresentada na parte superior no sistema. Caso não tenha sido apresentada automaticamente, utilize o seletor para selecionar o Alias criado:

9º Passo

Após o preenchimento da informação referente ao ambiente a ser atualizado, acesse o menu “Ferramentas > Atualização de Repositório” para que o processo de atualização seja iniciado.

10º Passo

A tela para digitação de usuário e senha será apresentada.

**Importante**: Mesmo que tenha sido cadastrada uma senha para o usuário “admin” no sistema, neste momento não será necessário informa-la.

Digite o usuário “admin” e clique em “Ok”:

11º Passo

Neste momento será apresentada a tela referente ao diretório raiz do servidor para atualização. O sistema automaticamente irá direcionar para a pasta TAF, apresentando as pastas contidas neste diretório.

Conforme indicado no início do manual, selecione a pasta criada “Atualização” para que o arquivo a ser utilizado para atualização do sistema seja apresentado.

12º Passo

Selecione o arquivo a ser utilizado para que o botão “Ok” seja ativado:

13º Passo

Após clicar em “Ok”, o sistema validará o arquivo selecionado e apresentará a tela informando que alguns fontes estão mais atualizados do que os que estão no RPO atual.

Selecione a opção “Aceito somente fontes atualizados”

14º Passo

Neste momento será apresentada uma mensagem informando que as informações referentes a este procedimento serão gravadas no arquivo RPO para posterior auditoria.

Clique em “Ok” para prosseguir.

15º Passo

O sistema executará a atualização e apresentará na aba mensagens (canto inferior) o status da operação e a finalização da conexão com o serviço.

16º Passo

Após a atualização, reinicie o serviço TAF-WS nos serviços do Windows.

# Atualização do TSS utilizando o Devstudio.exe - Arquivo .ptm

---

**Importante:** Antes de realizar a atualização, certifique-se que o arquivo que será utilizado corresponde ao ambiente utilizado.

Recomendamos que seja utilizado o arquivo com o nome igual ou terminado em ...**TTTP120.PTM** para ambientes em português da linha RM.

Atualização TSS1º Passo

Crie uma pasta com o nome “Atualização” (ou outro de sua preferência) no caminho de instalação do TSS (Por padrão, o mesmo é instalado em C:\totvssped, porem alguns clientes utilizaram o caminho C:\totvs\TAF\totvssped, como consta no documento de instalação) e extraia os arquivos que serão utilizados para a atualização do sistema.

2º Passo

Pare o serviço do TSS-Appserver12 nos serviços do Windows.

Caso o serviço não seja parado automaticamente, apresentando a mensagem abaixo, realize o procedimento indicado na aba “Dica!” antes de prosseguir:

Dica!

Procedimento para parar o serviço através do DOS:

Acesse o “Gerenciador de tarefas do Windows” > aba “Serviços” e localize o código PID do mesmo.

No prompt de comando do DOS (cmd) digite: taskkill /pid XXXX /f (onde XXXX é o PID do serviço) e tecle “Enter”. Neste momento o serviço será interrompido.

Realizado o procedimento de parada do serviço, voltamos para a atualização do sistema.

3º Passo

Acesse a pasta appserver (...bin\appserver) no diretório de instalação do TSS (Por padrão, o mesmo é instalado em C:\totvssped, porem alguns clientes utilizaram o caminho C:\totvs\TAF\totvssped, como consta no documento de instalação) e localize o arquivo appserver.ini. Edite este arquivo com um editor de texto, localize a tag [ONSTART], comente a mesma e salve o arquivo.

Após este procedimento, inicie o serviço TSS-Appserver12.

4º Passo

Após comentar a tag e iniciar o serviço, acesse o diretório smartclient (...\bin\smartclient), localize o aplicativo devstudio.exe e execute. A tela abaixo será apresentada. Clique em “Ok” para que o sistema seja executado.

5º Passo

Neste momento o sistema que será utilizado para a atualização será aberto. Caso a informação referente ao “Ambiente” a ser atualizado esteja em branco, conforme imagem abaixo, siga os procedimentos para a configuração do mesmo. Caso já esteja preenchida com a informação “SPED”, vá para o 10º passo.

6º Passo

Acesse o menu “Arquivo > Configurações” para que a tela de apontamento do ambiente seja apresentada.

7º Passo

Na tela de “Configurações de Compilação”, clique em “Adicionar” e preencha as informações **exatamente** como no exemplo abaixo clique em “Ok”:

8º Passo

Após a realização da configuração anterior, a tela abaixo será apresentada, clique em “Ok” para finalizar a configuração:

9º Passo

Verifique se a informação referente a configuração realizada será apresentada na parte superior no sistema. Caso não tenha sido apresentada automaticamente, utilize o seletor para selecionar o Alias criado:

10º Passo

Após o preenchimento da informação referente ao ambiente a ser atualizado, acesse o menu “Ferramentas > Atualização de Repositório” para que o processo de atualização seja iniciado.

11º Passo

A tela para digitação de usuário e senha será apresentada.

**Importante**: Mesmo que tenha sido cadastrada uma senha para o usuário “admin” no sistema, neste momento não será necessário informa-la.

Digite o usuário “admin” e clique em “Ok”:

12º Passo

Neste momento será apresentada a tela referente ao diretório raiz do servidor para atualização. O sistema automaticamente irá direcionar para a pasta totvssped, apresentando as pastas contidas neste diretório.

Conforme indicado no início do manual, selecione a pasta criada “Atualização” para que o arquivo a ser utilizado para atualização do sistema seja apresentado.

13º Passo

Selecione o arquivo a ser utilizado para que o botão “Ok” seja ativado:

14º Passo

Após clicar em “Ok”, o sistema validará o arquivo selecionado e apresentará a tela informando que alguns fontes estão mais atualizados do que os que estão no RPO atual.

Selecione a opção “Aceito somente fontes atualizados”

15º Passo

Neste momento será apresentada uma mensagem informando que as informações referentes a este procedimento serão gravadas no arquivo RPO para posterior auditoria.

Clique em “Ok” para prosseguir.

16º Passo

O sistema executará a atualização e apresentará na aba mensagens (canto inferior) o status da operação e a finalização da conexão com o serviço.

17º Passo

Acesse novamente o diretório appserver no diretório de instalação do TSS (...bin\appserver) e localize o arquivo appserver.ini. Edite este arquivo com um editor de texto, localize a tag [ONSTART], retire o comentário da mesma e salve o arquivo.

18º Passo

Após a alteração, reinicie o serviço TSS-Appserver12.

# Atualização do Dicionário - Arquivos .txt

---

A atualização do dicionário é composta por três fases:

1º - Substituição dos arquivos

2º - Execução do UPDDISTR

3º - Execução do UPDTAF

Para que a atualização seja realizada com sucesso, execute todos os procedimentos listados.

## Backup e aplicação dos novos arquivos:

Para atualizar o "Dicionário de Dados" do TAF, realize os procedimentos abaixo:

Atualização Dicionário de Dados1º Passo

Na tela de download é possível identificar que o arquivo que será baixado se trata de um "Dicionário Diferencial" do TAF. Veja abaixo:

2º Passo

Após certificar-se que se trata de um Dicionário do TAF - TOTVS Automação Fiscal, acesse o diretório systemload na pasta de instalação do sistema (C:\totvs\TAF\systemload) e crie uma pasta com o nome "Backup".

3º Passo

Pare o serviço do TAF-WS nos serviços do Windows

Caso o serviço não seja parado automaticamente, apresentando a mensagem abaixo, realize o procedimento indicado na aba “Dica!” antes de prosseguir:

Dica!

Procedimento para parar o serviço através do DOS:

Acesse o “Gerenciador de tarefas do Windows” > aba “Serviços” e localize o código PID do mesmo.

No prompt de comando do DOS (cmd) digite: taskkill /pid XXXX /f (onde XXXX é o PID do serviço) e tecle “Enter”. Neste momento o serviço será interrompido.

Realizado o procedimento de parada do serviço, voltamos para a atualização do dicionário.

4º Passo

Mova os arquivos antigos (hlpdfpor.txt e sdfbra.txt) para este diretório (C:\totvs\TAF\systemload\Backup). Em seguida coloque o novo arquivo no diretório (C:\totvs\TAF\systemload).

5º Passo

Coloque o novo arquivo no diretório C:\totvs\TAF\systemload.

  

## Execução do UPDDISTR e UPDTAF

---

**Importante:** Antes de executar estes procedimentos, certifique-se que o **serviço TAF-WS** está **parado**.

### UPDDISTR

UPDDISTR e UPDTAF1º Passo

Acesse o diretório C:\totvs\TAF\bin\smartclient e localize o aplicativo “smartclient.exe” e execute o mesmo:

2º Passo

Na tela de parâmetros iniciais, digite UPDDISTR na opção “Programa Inicial” e confira as demais informações. As mesmas deverão estar de acordo com a imagem abaixo.

Clique em “Ok” para iniciar o processo de atualização das informações:

3º Passo

Neste momento, a tela referente a atualização das informações presentes no dicionário será apresentada. Realize o backup dos diretórios informados antes de prosseguir.

Clique em “Avançar” para continuar o wizard:

4º Passo

A tela de termo de aceite será apresentada. Clique em “Avançar” par a prosseguir com a atualização.

5º Passo

Marque a opção aceite das alterações realizadas na versão que será aplicada pelo wizard e clique em “Avançar”.

6º Passo

Marque a opção referente a realização dos backups sugeridos anteriormente e clique em “Avançar”.

7º Passo

Marque a opção referente a validação de possíveis customizações existentes e clique em “Avançar” para prosseguir:

8º Passo

Clique novamente em “Avançar” para prosseguir com a atualização ou em “Cancelar” para sair do atualizador:

9º Passo

A tela de início do processo de atualização será exibida:

10º Passo

Neste momento, caso tenha alterado a senha do usuário “Administrador”, informe a mesma e clique em “Avançar”.

Caso a senha não tenha sido alterada/cadastrada, utilize a tecla “Tab” para habilitar o botão “Avançar” e clique no mesmo para prosseguir:

11º Passo

Nesta tela, verifique se as informações referentes ao diretório de dados se encontram vazias (conforme imagem abaixo). Caso estejam preenchidas, dê um duplo clique no campo, apague as informações e utilize a tecla “Tab” para salvar a alteração.

Clique em “Avançar” para prosseguir:

12º Passo

Na tela referente aos logs do processo de atualização, deixe somente a opção “” desmarcada e clique em “Avançar”:

13º Passo

Todas as validações que serão realizadas pela atualização serão apresentadas neste momento. Clique em “Avançar” para iniciar o processamento:

14º Passo

O sistema iniciará a atualização das informações do ambiente.

15º Passo

Este processo pode levar alguns minutos. Aguarde até a conclusão da atualização.

16º Passo

Ao final do processo, será exibida a tela de conclusão do mesmo. Clique em finalizar para concluir a atualização.

17º Passo

A tela abaixo será exibida para informar que o sistema será finalizado.

### UPDTAF

UPDTAF1º Passo

Acesse o diretório C:\totvs\TAF\bin\smartclient e localize o aplicativo “smartclient.exe” e execute o mesmo.

2º Passo

Na tela de parâmetros iniciais, digite UPDTAF na opção “Programa Inicial” e confira as demais informações. As mesmas deverão estar de acordo com a imagem abaixo.

Clique em “Ok” para iniciar o processo de atualização das informações (a apresentação da tela de UPDATE pode levar alguns minutos).

3º Passo

Selecione as atualizações que estiverem como “Pendente” e clique em “Processar”.

4º Passo

Neste momento serão apresentadas as atualizações que serão realizadas. Clique em "Finalizar para" concluir a atualização do “Dicionário de dados”.

5º Passo

Após a execução de todos os passos da atualização (UPDDISTR e UPDTAF), reinicie o serviço TAF-WS nos serviços do Windows.

# Atualização de Schemas

---

Atualização de Schemas

**Importante:** Antes de iniciar o procedimento, faça o backup das pastas schemas e semaforo**.**

1º Passo

Na área de "Downloads" efetue o filtro conforme imagem abaixo para realizar o download dos Schemas a serem atualizados no TSS.

2º Passo

Acesse a pasta schemas (...totvssped\schemas) no diretório de instalação do TSS (Por padrão, o mesmo é instalado em C:\totvssped, porem alguns clientes utilizaram o caminho C:\totvs\TAF\totvssped, como consta no documento de instalação), copie o arquivo baixado (procedimento realizado no 1º Passo) e extraia o conteúdo do mesmo, substituindo os já existentes na pasta e mesclando o conteúdo da eSocial e da REINF.

3º Passo

Após realizar os procedimentos anteriores, siga as instruções abaixo:

* Apague o conteúdo da pasta semaforo, localizada em C:\totvssped
* Reinicie o serviço do TSS (TSS-Appserver12)

falsefalse

**Produto:** TAF e TSS

false

**Versão:** 12.1.XX

false

**Processo:** Atualização via Devstudio.exe do TAF - TOTVS Automação Fiscal e TSS - TOTVS Service SOA.

falsefalse

**Status:** Publicado

false

**Data:**

false

**Autor:**
