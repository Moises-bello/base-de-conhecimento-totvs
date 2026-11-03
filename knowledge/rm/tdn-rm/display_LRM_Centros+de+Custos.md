---
content_hash: 963a169705b1a73eab3ea033bf9369bddf3ab6d3ecd10c8c9415bce965351c67
fetched_at: '2026-06-29T00:09:28.011301+00:00'
page_id: '423938620'
product: rm
source: tdn-rm
title: Centros de Custos
type: documentation
url: https://tdn.totvs.com/display/LRM/Centros+de+Custos
version: 21
---

Para cumprir as principais necessidades contábeis ou fiscais de distribuição de custos da empresa, os Centros de Custos poderão ser cadastrados e vinculados às filiais, permitindo que as contas de despesas sejam devidamente distribuídas em seus respectivos centros de custo.

Os dados cadastrais poderão ser incluídos e/ou atualizados a partir da janela de edição própria, que reúne todos os centros de custos cadastrados, podendo ser acessado através do menu no item Cadastros | Centros de Custos, ou através do ícone respectivo na barra superior, abaixo do menu principal do sistema.

Os centros de custos cadastrados serão apresentados a partir do formato tree-view. Deverão ser criados hierarquicamente conforme as definições da empresa. Para acessá-los, basta clicar sobre o sinal "+" apresentado à esquerda de cada grupo e subgrupo de centros de custo.

A opção "Enviar para o SPED Contábil" permite que o cento de custo seja enviado para o arquivo referente ao SPED Contábil. Para que ela esteja disponível deve-se selecionar em Ambiente\Parâmetros\TOTVS Gestão Contábil\Rotinas Legais\SPED Contábil\SPED Contábil 1/2, no parâmetro Considerar para o Centro de Custo, a opção Próprio Centro de Custo.

**Observações**

Caso existam associações de contas contábeis e contas gerenciais ao plano de contas referencial (SPED Contábil), ao selecionar a opção "Próprio Centro de Custo" e concluir a parametrização, elas serão perdidas. Para desmarcar a opção "Enviar para o SPED Contábil" de um centro de custo deve-se verificar se o mesmo não está associado a alguma conta paralela (SPED Contábil).

Consumo via API

A integração com o cadastro de Centros de Custo está disponível também através de APIs. No [Guia de APIs da TOTVS](https://api.totvs.com.br/) são descritas todas as APIs disponíveis, suas características e funcionalidades. Assim como as visões, a API também pode ser configurada para retornar somente um número X de registros ao ser consultada. Essa configuração é feita no  com a parametrização do Número Máximo de Registros. No caso da API de Centro de Custo o DataServer a ser utilizado é o **CtbCostCenterDataApi.**

Definição de API

      API é um conjunto de rotinas e padrões de programação para acesso a um aplicativo de software ou plataforma baseado na Web. A sigla API refere-se ao termo em inglês "Application Programming Interface" que significa em tradução para o português "Interface de Programação de Aplicativos".

      Uma API é criada quando uma empresa de software tem a intenção de que outros criadores de software desenvolvam produtos associados ao seu serviço. Existem vários deles que disponibilizam seus códigos e instruções para serem usados em outros sites da maneira mais conveniente para seus usuários.

      Através das APIs, os aplicativos podem se comunicar uns com os outros sem conhecimento ou intervenção dos usuários. Elas funcionam através da comunicação de diversos códigos, definindo comportamentos específicos de determinado objeto em uma interface. A API liga as diversas funções em um site de maneira que possam ser utilizadas em outras aplicações. De modo geral, a API é composta de uma série de funções acessíveis somente por meio de programação.

      Recentemente, a utilização das APIs tem se espalhado nos plugins, que complementam a funcionalidade de um determinado programa. Os desenvolvedores de um programa principal criam uma API específica e fornecem a outros criadores, que desenvolvem plugins para aumentar o potencial e as funcionalidades do programa.

      Os sistemas operacionais também possuem suas APIs com as mesmas funções descritas acima. Por exemplo, o Windows possui APIs como a Telephony API, Win16 API e Win32 API. Quando um usuário executa um programa que envolva algum processo do sistema operacional, é bem provável que o Windows faça uma conexão entre o software e alguma de suas APIs.

Anexos


Processos




* [Alteração de múltiplos registros de centro de custo](https://tdn.totvs.com/x/wNBAIg)
Veja também

* [Defaults Contábeis](http://tdn.totvs.com/pages/viewpage.action?pageId=423938732)
* [Rateio por centro de custo](http://tdn.totvs.com/pages/viewpage.action?pageId=4811902)
