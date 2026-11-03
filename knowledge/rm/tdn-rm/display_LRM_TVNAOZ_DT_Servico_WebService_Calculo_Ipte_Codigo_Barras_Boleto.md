---
content_hash: 22b58daa5a19869fd8b1cacc80f0b28edb7f420863922010c5c21c44d4e3e515
fetched_at: '2026-06-29T00:08:19.212445+00:00'
page_id: '266979389'
product: rm
source: tdn-rm
title: TVNAOZ_DT_Servico_WebService_Calculo_Ipte_Codigo_Barras_Boleto
type: documentation
url: https://tdn.totvs.com/display/LRM/TVNAOZ_DT_Servico_WebService_Calculo_Ipte_Codigo_Barras_Boleto
version: 117
---

# SERVIÇO WEBSERVICE PARA CÁLCULO DOS CÓDIGOS DE BARRAS E IPTE DE UM BOLETO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *WebService WsEdu - Cálculo dos código de barras e Ipte do Boleto* | *WebService WsEdu - Cálculo dos código de barras e Ipte do Boleto* | |
| **Cadastros Iniciais:** | *1) Boleto gerado;* |
|  |  |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | TVXKWI |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7* |

## Descrição

Disponibilização de serviço, via webservice, para cálculo dos códigos de Barras e Ipte do boleto.

## Procedimento para Implantação

Atualização do sistema com o Patch 11.82.45.107, ou superior, referente a implementação realizada e a instalação do TBC, caso se deseje utilizar o IIS.

## Configuração WebService

Os serviços disponibilizados poderão ser acessados via WebService através da instalação do TBC e utilizando o IIS ou através do WebService disponibilizado pelo Host.

* Acesso ao WebService disponibilizado pela instalação do TBC:

[Como expor os Web Services do RM através do IIS](http://tdn.totvs.com.br/pages/releaseview.action?pageId=82477609)

 

* Acesso ao WebService disponibilizado pelo serviço do Host:

[Como Expor os Web Services do RM através do Host](http://tdn.totvs.com.br/pages/releaseview.action?pageId=89620766)

## Procedimento para Utilização

Com a necessidade de um serviço para calcular os códigos de Barras e Ipte dos boletos gerados pelo Educacional, foram disponibilizados os serviços: CalculaCodigoBarrasBoleto e CalculaCodigoIpteBoleto através do WebService do Educacional.

Os dois serviços, para cálculo dos códigos, estão disponíveis através do WebService WsEdu:

Os parâmetros necessários para a utilização dos serviços são:

Cálculo do código de Barras:

| Nome | Tipo | Descrição |
| --- | --- | --- |
| IdBoleto | Id. do Boleto | Inteiro |
| CodColigada | Código da coligada | Short |
| CodUsuario | Código do usuário do RM | String |
| DataCalculo | Data utilizada para cálculo do código de barras | DateTime |

Cálculo do Ipte:

| Nome | Tipo | Descrição |
| --- | --- | --- |
| IdBoleto | Id. do Boleto | Inteiro |
| CodColigada | Código da coligada | Short |
| CodUsuario | Código do usuário do RM | String |
| DataCalculo | Data utilizada para cálculo do código de barras | DateTime |

Exemplo de XML para consumo do serviço para cálculo do código de barras do boleto:

xmlCódigo de Barras




17149

1

mestre

2016-10-06
]]>

Exemplo de XML para consumo do serviço para cálculo do código de barras do boleto:

xmlCódigo Ipte




17149

1

mestre

2016-10-06
]]>

O retorno dos dois serviços será um valor string com o código solicitado:

xmlResultado


34191.75009 01714.940549 65432.160003 1 66660000049980
 

34191666600000499801750001714940546543216000
]]>

divs
