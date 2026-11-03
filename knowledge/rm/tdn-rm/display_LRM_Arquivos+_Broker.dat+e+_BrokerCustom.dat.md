---
content_hash: 283bc831c7de47c3ad04f37cfc811306103bfa2500d47b771226134fb6e5495f
fetched_at: '2026-06-29T00:05:56.481001+00:00'
page_id: '152110285'
product: rm
source: tdn-rm
title: Arquivos _Broker.dat e _BrokerCustom.dat
type: documentation
url: https://tdn.totvs.com/display/LRM/Arquivos+_Broker.dat+e+_BrokerCustom.dat
version: 6
---

O arquivo ***\_Broker.dat*** é responsável por listar todos os componentes de software que se comunicam remotamente dentro da Linha RM. Ele pode ser encontrado dentro da pasta *RM.NET* do diretório de instalação.

Nele estão presentes os componentes da parte Cliente:

* Actions
* Forms

Também presentes os componentes da parte Servidor:

* Servers
* DataServers
* Modules

As informações deste arquivo são utilizadas para registrar os componentes sob-demanda e definir as chamadas remotas.

A partir da versão **12.1.24**, foi criado o arquivo ***\_BrokerCustom.dat*** que tem a mesma finalidade do ***\_Broker.dat***, mas nele estão contidas informações dos assemblies de Customização, geralmente localizados dentro da pasta *Custom* do diretório de instalação. Nas versões anteriores, todas as informações se encontravam no mesmo arquivo.

Caso o(s) arquivo(s) não existam na pasta, o Host os gera na inicialização do serviço.
