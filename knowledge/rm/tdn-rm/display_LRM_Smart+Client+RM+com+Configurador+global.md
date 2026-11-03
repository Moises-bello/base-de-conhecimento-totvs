---
content_hash: 1343b42cdaae8a09418b5e0cdfceee834df9ed3c5bbdf95a645e6148ed978051
fetched_at: '2026-06-29T00:08:16.920871+00:00'
page_id: '248582547'
product: rm
source: tdn-rm
title: Smart Client RM com Configurador global
type: documentation
url: https://tdn.totvs.com/display/LRM/Smart+Client+RM+com+Configurador+global
version: 39
---

# Índice

---

.\*ndice:

# Objetivo

---

O objetivo deste documento é trazer uma visão de como configurar o Smart Client RM utilizando o configurador global de forma com o que a configuração esteja praticamente toda no servidor.

Isso facilita muita a gestão de configuração de ambiente, alem de tornar mais transparente as configurações de servidor.

# Introdução

---

        Para utilizar o Smart Client com o Configurador Global, é necessário informar somente o endereço HTTP do servidor de aplicação ou o caminho do arquivo de configuração global no arquivo **.config**dos aplicativos,conforme exemplos abaixo.

        Será necessário criar um arquivo de configuração unificada. Mais detalhes ao longo desta documentação.

# Arquivo [Aplicação].config

---

[Aplicação] é o nome do EXE que está sendo configurado, seja ele RM.exe, RM.Host.Service.exe, RM.AliasManager.exe, etc.

       Seu arquivo **.config** deverá conter somente o caminho do arquivo de configuração global. Essa informação estará na tag ***configpath***. Onde, ***ENDEREÇOEXTERNO*** será substituído pelo endereço ou IP do servidor de aplicação onde o arquivo de configuração global está hospedado.

       O Caminho do arquivo global configuracaorm.config deve estar definido na tag CONFIGPATH, no arquivo de configuração do seu aplicativo.

xml]]>

       O caminho pode ser definido de forma absoluta ou relativa.  
       Como exemplo, adicionamos o arquivo configuracaorm.config no caminho    c:/RM/Atual/Release/bin/arquivo/configuracaorm.config

       A forma absoluta é quando o caminho do arquivo é adicionado por completo:

xml]]>

        Na forma relativa, o caminho do arquivo é adicionado a partir do local de instalação do aplicativo:

xml]]>

        O arquivo **RM.EXE.Config** terá o seguinte layout:

xml




]]>

# Arquivo de Configuração Global ou Unificada

---

false**Veja detalhes do arquivo de configuração unificada**[neste link](http://tdn.totvs.com/display/LRM/Gerenciador+de+Config).

       O configurador global tem capacidade de receber diferentes grupos de configuração, podendo ser divididos em aplicação, domínio e nome da máquina. O \_ é utilizado para separa cada identificador desses grupos.

        Por exemplo:

        <RM.EXE\_BH01.LOCAL\_NOTEBOOK1> - Neste caso a configuração será aplicada para a aplicação RM.exe, domínio BH01.LOCAL e o computador NOTEBOOK1.

        <RM.EXE\_BH01.LOCAL\_DEFAULT> - Neste caso a configuração será aplicada para a aplicação RM.exe, domínio BH01.LOCAL e qualquer máquina.

        <RM.HOST.EXE\_TODOS\_DEFAULT> - Neste caso a configuração será aplicada para a aplicação RM.exe, qualquer domínio e qualquer computador.

        <RM\_TODOS\_DEFAULT> - Neste caso a configuração será aplicada a qualquer aplicativo, domínio e máquina.

A configuração mais especifica sempre sobrepõe a configuração mais genérica, caso haja este cenário no arquivo de configuração global.

       No exemplo acima, na tag **<RM.EXE\_BH01.LOCAL\_DEFAULT>**, foi definido que máquinas que estiverem no domínio **BH01.LOCAL**, acessarão o host localmente.                       A tag **Host** deve identificar o endereço da rede interna, onde o host responderá.

       O arquivo deve conter também, os dados de conexão do host que será utilizado quando a conexão for feita por **uma máquina fora do domínio especificado anteriormente**:

       No exemplo acima, na tag **<RM\_TODOS\_DEFAULT>**, foi definido que todas as máquinas que não estiverem no domínio BH01, acessarão o host de forma pública.                         A tag **Host**deve identificar o endereço IP onde o host responderá.

       Lembre-se de alterar o nome do domínio no cabeçalho do arquivo de configuração unificada:

falseObservação:

O usuário do IIS e do Host precisa ter acesso ao arquivo de configuração global.

Acesse nos links abaixo os arquivos de configuração com configurações padrão que podem ser utilizado em qualquer instalação.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Configurar Totvs Update para acesso local e remoto

falsefalse

**Status:** Finalizado

false

**Data:** 11/01/2019

false

**Autores:**

**Daniel Santos Campos**
