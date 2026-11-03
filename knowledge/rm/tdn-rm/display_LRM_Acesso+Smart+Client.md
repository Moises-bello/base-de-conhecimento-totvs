---
content_hash: b4d84d90e90bff019b2efac44475c56f4910295246cb295ca7594b77ccff7e61
fetched_at: '2026-06-29T00:08:09.257808+00:00'
page_id: '239031645'
product: rm
source: tdn-rm
title: Acesso Smart Client
type: documentation
url: https://tdn.totvs.com/display/LRM/Acesso+Smart+Client
version: 14
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é trazer uma visão do que é, como funciona e como configurar o Smart Client RM.

# Introdução

---

        O Smart Client RM nada mais é que o mesmo RM.exe utilizado nos ambientes locais e três camadas, e utiliza protocolo TCP ou HTTP para se comunicar com o servidor de aplicação, o Host.

Versões anteriores à 12 é necessário o uso do TS com o RM, pelos motivos:

1. Algumas telas ainda estão em Delphi.
2. A comunicação entre o RM.exe e o Host é muito pesada e exige muito em relação ao consumo de banda.
3. A atualização da parte client é manual, ou seja, a cada atualização de patch ou release, as estações de trabalho precisam ser atualizadas manualmente.

   A versão 12 trouxe novas implementações que eliminam a necessidade do uso de TS, são elas:

   1. \*Mais telas foram migradas para tecnologia .NET, a mesma do RM.exe.
   2. \*\*A comunicação entre o RM.exe e o Host sofreu bastante evolução, como a redução considerável do tamanho dos pacotes, compactação eficaz dos dados trafegados e otimização das chamadas ao servidor de aplicação.
   3. Criação do mecanismo de download do client RM sem a necessidade de instalador.
   4. Criação do mecanismo de update automático do servidor de aplicação e do client (RM.exe).
   5. Melhorias no cockpit para trabalhar em ambientes distribuídos e remotos.

   **\* Não é possível utilizar o Smart Client RM para funcionalidades ainda em Delphi.**

   **\*\* Para uma boa experiência de uso, é recomendado que a latência máxima de rede entre a estação de trabalho e o servidor seja de no máximo 60 milissegundos.**

Segue uma simples ilustração do resultado dessa evolução:

* Nas versões anteriores a 12 havia a necessidade da camada de TS, conforme ilustração abaixo:

* Na versão 12 a camada de TS não se faz necessária, caso desejado pelo cliente, desde que a rede atenda aos requisitos mínimos:

* Desta forma o RM.exe se comunica diretamente com o Host sem a necessidade de um protocolo RDP:

# Instalação do SmartCliente

Para instalação realize os procedimentos abaixo:

* Acesse o link [http://servidor\_de\_aplicacao:porta/wsUpdate/](http://187.94.63.227:8051/wsUpdate/) (onde o servidor e a porta devem ser substituídos de acordo com as configurações do ambiente, exemplo: <http://187.94.63.227:8051/wsUpdate/>) e realize o download do instalador para sua estação de trabalho, lembrando que é importante verificar se o firewall ou antivírus irá bloquear a execução do instalador.  
  A tag UpdateServerEnabled deve estar configurada = true, caso contrário o acesso a este link será desabilitado pelo Host.

* Concluído o download, execute o aplicativo *RM.Install.exe* em sua estação, informando o diretório que deseja salvar a aplicação.  
  Após a instalação ser 100% bem sucedida o RM será aberto.
* Caso durante o download ocorra algum erro de comunicação e falha ao baixar algum arquivo de instalação, será apresentado um alerta, informando a quantidade de arquivos que não foram baixados.  
    
  Ao selecionar "Repetir", será realizada uma nova tentativa de baixar os arquivos, caso ainda ocorra falha, este aviso será novamente exibido.  
  Ao selecionar "Cancelar" a instalação será interrompida e o RM não será aberto.

# Log de Download

* Para adicionar a opção de Log do Download do Smart Client, é necessário executar o aplicativo rm.install.exe.  
  Para isso, execute o seguinte comando no cmd: **rm.install.exe /APPPATH="c:\Nova pasta" /log=true** , substituindo o diretório do arquivo:  
  Ou de uma forma mais simplificada **rm.install.exe /log=true**  
  O Log apresentará o seguinte layout:  
  Registrando o que ocorreu com sucesso e falha.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Acesso Smart Client

falsefalse

**Status:** Finalizado

false

**Data:** 09/09/2016

false

**Autores:**
