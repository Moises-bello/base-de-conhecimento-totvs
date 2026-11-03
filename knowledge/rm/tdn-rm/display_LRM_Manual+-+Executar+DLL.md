---
content_hash: fc7b0b36c743d547f855dfc4e531dfb4dba902048ba2ffd4b035f5799e647930
fetched_at: '2026-06-29T00:08:47.218446+00:00'
page_id: '319787268'
product: rm
source: tdn-rm
title: Manual - Executar DLL
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Executar+DLL
version: 3
---

Utilize esta opção para executar um método de uma DLL .NET. Esta DLL deverá conter uma classe com um construtor público vazio, e o método a ser executado deverá ser publico e conter apenas parâmetros de tipos básicos (string, int, datetime, decimal, etc).

O método será executado após a geração do arquivo e pode ser utilizado para automatizar tarefas complementares após a geração.

![](/download/attachments/319787268/executar_dll.png?version=1&modificationDate=1512921827000&api=v2)

1Nome do Assembly

Selecione uma DLL .NET válida que contenha o método a ser executado.

2Classe

Selecione a classe para execução do método. A classe deverá ter um construtor padrão sem parâmetros que será utilizado para criação da sua instância pelo gerador de saídas.

3Método

Selecione o método da classe que deverá ser executado.

4Parâmetros

Informe aqui os parâmetros necessários para execução do método. Todos os parâmetros devem ter seus valores informados obrigatóriamente. Podem ser utilizados valores a partir de dados do contexto, valores fixos ou expressões. Para mais informações consulte a [Ligação do Campo](/pages/viewpage.action?pageId=319787278).
