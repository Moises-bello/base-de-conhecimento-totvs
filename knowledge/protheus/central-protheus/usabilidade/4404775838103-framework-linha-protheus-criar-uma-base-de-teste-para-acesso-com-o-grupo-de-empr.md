---
article_id: 4404775838103
category: Usabilidade
content_hash: 8a65ff96033205355350f83d08a27a8d1edc1d78dc81caa7740194a30636a1ed
fetched_at: '2026-06-28T22:42:17.253759+00:00'
product: protheus
section_id: 360000076807
source: central-protheus
title: Framework - Linha Protheus - Criar uma Base de Teste para acesso com o Grupo
  de Empresas 99
type: support-article
updated_at: '2025-12-16T12:36:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404775838103-Framework-Linha-Protheus-Criar-uma-Base-de-Teste-para-acesso-com-o-Grupo-de-Empresas-99
---

**Dúvida**

Como criar uma Base de Teste para acesso com o Grupo de Empresas 99 e com acesso de até dois usuários?

**Ambiente**  
Protheus - Configurador - A partir da Versão 12

**Solução**

Criação de uma Base de Teste para acesso com o Grupo de Empresas 99 e com acesso de até dois usuários.

**Introdução:**

A Totvs disponibiliza aos clientes a possibilidade de utilizar o ERP Protheus sem que haja consumo de licenças desde que a instalação utilize o grupo de empresas 99, dessa forma o uso da ferramenta fica limitado a duas conexões simultâneas, nessa documentação será apresentado o processo de instalação e configuração de um ambiente de Testes, para utilização do grupo de Empresas 99 sem o consumo de licenças e uma segunda modalidade de utilização do grupo de empresa 99 que consume da licença TOTVSDEVTEST.

Instalação do License Server Virtual.

 – Baixe o instalador do License Server Virtual correspondente ao seu Sistema Operacional.

Via **Portal**: [Home](https://suporte.totvs.com/portal/p/10098/download)/ [Protheus](https://suporte.totvs.com/portal/p/10098/download#000006/)/ [TOTVSTEC-FRAMEWORK](https://suporte.totvs.com/portal/p/10098/download#000006/368/)/ [INSTALADORES](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFINSTALL/)

Link direto: <https://suporte.totvs.com/portal/p/10098/download#000006/368/TFINSTALL/>

Instalação do License Server

– Efetue o processo de instalação, conforme orientações abaixo:

Windows: <https://tdn.totvs.com/display/framework/TOTVS+License+Server+Virtual#TOTVSLicenseServerVirtual-Instala%C3%A7%C3%A3oWindows>

Linux: <https://tdn.totvs.com/display/framework/TOTVS+License+Server+Virtual#TOTVSLicenseServerVirtual-Instala%C3%A7%C3%A3oLinux>

 – Na tela do Wizard de Configuração do TOTVS ID, clique em Cancelar:

- Como iremos instalar um ambiente para uso do Grupo de Empresa 99 e será apenas um ambiente de testes, não será necessário efetuar a configuração do TOTVS ID.

Instalação do Protheus

- Antes de executar o instalador é necessário ter criado/configurado ODBC e banco de dados previamente.

<https://tdn.totvs.com/display/tec/DBAccess+-+Como+criar+uma+fonte+de+dados+para+uso+com+Microsoft+SQL+Server>

– Efetue a instalação de acordo com as instruções da documentação abaixo:

<https://tdn.totvs.com/display/public/PROT/Instalador+Protheus+Windows+12.1.27>

Observações:

- Na tela do Wizard de Configuração do License Server, informe o endereço IP de instalação do License Server e a mesma porta informada durante o processo de instalação do License Server "Porta do serviço de licenciamento (conexão ERP)", o valor padrão é 5555.

- Caso não lembre qual a porta de licenciamento informada na instalação do License Server, acesse o diretório de instalação, pasta \bin\appserver, localize e abra o arquivo Appserver.ini.

Pesquise pela seção [LICENSESERVER], a porta está informada na Tag port.

No exemplo abaixo, a porta do serviço de Licenciamento do License Server é a 5555:

[LICENSESERVER]

Enable=1

Port=5555

ShowStatus=0

EnableNumber=1

LicenseFile=lsinitialize.inf

IPCGOTIMEOUT=45000

IPCRETURNTIMEOUT=90000

NUMBERVAL=1

STATELESSREUSECONN=60

AUTOSAVENUMBER=1

- Para criar filiais na Empresa Teste (99), sem a necessidade de consumir licenças realize os procedimentos abaixo

Na Lib esta chumbado a empresa teste como 99 filial 01 até a filial 03, sendo que os nomes delas tem que ser conforme abaixo.

01 - MATRIZ  
02-  FILIAL02  
03 - FILIAL03

Diferente disso ele não considera como empresa Teste, e será  necessário o apontamento para o serviço de licenças.

# - Não é necessário efetuar a instalação dos  Componentes Adicionais.
