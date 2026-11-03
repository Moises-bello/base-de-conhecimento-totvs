---
content_hash: a9768569772c0d129fef9f0abd114080d2eccdf8d7d8498bb3817c3b27d9be87
fetched_at: '2026-06-29T00:10:22.672520+00:00'
page_id: '498700240'
product: rm
source: tdn-rm
title: Configuração Plug and Play
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498700240
version: 10
---

## 

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

É possível  instalar o TGM em um ambiente RM já configurado e funcional, mesmo com os Hosts em execução.

Para configurar, siga os passos do próximo tópico.

## **02. EXEMPLO DE UTILIZAÇÃO**

1. Na máquina onde o TGM será instalado, abra o RM.Host.Service, clique na aba 'Totvs Gateway Manager' e clique em Instalar:

2. Verifique a mensagem de confirmação da instalação:

3. Depois de instalar, será necessário configurar/aplicar as portas que o TGM utilizará para se comunicar.

Levando em consideração que já existem Hosts cadastrados na aba RM Host Service, instalados ou não, por padrão, as portas do TGM serão preenchidas com as mesmas portas do primeiro Host.

LembreteO TGM utiliza as portas que o Host utilizava para que não seja necessário alterar nos arquivos de configuração (.config), ou serviços existentes (APIs, WebServices...) as portas que o RM se comunica.

4. Clique em Aplicar.

Para que as portas que o Host utiliza sejam alteradas automaticamente, clique em 'Sim'.

Isso fará com que as portas do Host que foram utilizadas pelo TGM sejam trocadas de acordo com a regra abaixo e o host será reiniciado automaticamente. Depois de inicializado, ele se cadastrará no TGM:

* Porta WCF: Última porta WCF + 1
* Porta WebService e WebAPI: Porta WCF + 1

Exemplo:

a. Configuração inicial - Host funcionando com as portas:

* Porta WCF: 8050
* Porta WebService e WebAPI: 8051

b.TGM instalado, com as portas do host. O TGM passa a responder nas portas:

* Porta WCF: 8050
* Porta WebService e WebAPI: 8051

c. O Host passa a utilizar as portas:

* Porta WCF: 8052
* Porta WebService e WebAPI: 8053

Importante:

As portas que o Host irá utilizar precisam estar liberadas antes de aplicar as configurações no TGM.

Caso não estejam liberadas, o host não conseguirá se cadastrar automaticamente no TGM.

Veja mais informações sobre a reserva de porta no documento (<http://tdn.totvs.com/x/HoFXBQ>)

Se o ambiente possuísse 3 hosts, as portas do primeiro host seriam substituídas pela maior porta existente + 1.

5. Nesse processo o(s) host(s) foram cadastrados no TGM.

Percebe-se que as tags abaixo foram adicionadas no arquivo de configuração do host:

* <add key="TGMADDRESS" value="BHD050101853:8040" />
* <add key="HttpPort" value="8053" />
* <add key="ApiPort" value="8053" />
* <add key="TGMGROUPFORTCP" value="RM\_WCF" />
* <add key="TGMGROUPFORHTTP" value="RM\_WEBSERVICE" />
* <add key="TGMGROUPFORAPI" value="RM\_WEBSERVICE" />

6. A partir de então, todo o host que for instalado ou inicializado, será cadastrado automaticamente no TGM. Caso algum erro da rede tenha impedido o Host de se cadastrar, basta reiniciá-lo que ele será cadastrado.

Para mais informações sobre como alterar as portas WebApi ou WebService, .

Acesse para configurar o [TOTVS Gateway Manager (TGM) com Config Global](https://tdn.totvs.com/display/LRM/TOTVS+Gateway+Manager+%28TGM%29+com+Config+Global).
