---
content_hash: 00e063553aab4ff73196751ab92310c0ef860dc7c9272b930e3db1d4f1f9fc71
fetched_at: '2026-06-29T00:09:21.043602+00:00'
page_id: '422545776'
product: rm
source: tdn-rm
title: Pasta Serviços (Apuração do ISS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545776
version: 6
---

**Serviços por Projeto**  
Ao encerrar o período do ISS, o sistema calculará os saldos do imposto por Obra/Projeto executado com base nos lançamentos de Entrada de Materiais e Serviços e as Notas Fiscais de Saída da Prestação do Serviço. Será calculado o valor do imposto devido / Crédito a transportar para o período seguinte e o valor total das deduções, e irá inserir ou alterar os registros desta pasta com estes dados para cada obra movimentada no período. Estes lançamentos deverão conter as obras associadas na Pasta Outros Dados dos  Lançamentos de  Entrada/Saída.  
Esta pasta somente será habilitada se o Tributo associado ao Período for do Tipo ISS e o parâmetro Emite Livros Construção Civil estiver habilitado.

Seleção por filialSaoPauloSão Paulo

Ao encerrar o período para as filiais do Estado de **São Paulo**, o sistema irá calcular o imposto devido em função de cada Serviço prestado para cada Obra e adicionar nesta pasta.   
Para os lançamentos de entrada, além da parametrização por ISS e emissão de livro de construção civil, é necessário preencher a data de dedução dentro do intervalo das datas do período de apuração.

**Serviços Diversos**  
Ao Encerrar o Período o sistema irá calcular o imposto devido em função de cada Serviço prestado e adicionar nesta pasta. O valor total do imposto devido será gravado no campo Saldo Credor/Devedor, Pasta Outros Dados, Cadastro de Período. Para efeito de cálculo do imposto devido, serão consideradas todas as Notas Fiscais de Entrada ou Saída com incidência de ISS.

***Observação:*** Para Notas Fiscais cujo o Código de Serviço não tenha sido informado, será usado o valor "**00000**" para agrupar os valores.

Serviços Diversos

**Serviços por Alíquota**  
Ao encerrar o período de ISS o sistema irá totalizar as operações por alíquota e colocar nessa pasta. O sistema faz as totalizações da seguinte forma:

* Totaliza o ISS Devido na Saída por Alíquota, sendo que para casa alíquota totaliza por município.
* Totaliza o ISS Retido na Entrada por Alíquota.
* Totaliza o ISS Retido por Terceiros.

Para que esta totalização seja realizada corretamente, é muito importante que o campo Tipo de Recolhimento da tela de Outros Tributos do Lançamento seja preenchido.   
O campo Código de município da tela de Lançamento Pasta Outros Dados | Prestação de Serviços também deve ter sido preenchido.  
***Observação:***Quando necessário a reabertura do período  é importante deletar as informações desta pasta, pois, não será possível alterar lançamentos com dados.
