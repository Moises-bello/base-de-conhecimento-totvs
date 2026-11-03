---
content_hash: e33f2288dd9d05574c967f6ab2480f64f9ce1470b739d79746c8814d6019ae2a
fetched_at: '2026-06-29T00:08:47.205833+00:00'
page_id: '319787265'
product: rm
source: tdn-rm
title: Manual - Configuração do Layout
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787265
version: 3
---

As configurações do Layout definem as propriedades que são válidas para todo o Layout, entre elas qual a base de dados de origem e qual a formatação padrão para cada tipo de dado suportado pelo gerador.

![](/download/attachments/319787265/configuracao_do_layout.png?version=1&modificationDate=1512921819000&api=v2)

1ID

Exibe o código identificador do Layout do gerador no sistema RM.

2Nome

Informe um nome para o Layout.

3Descrição

Informe um texto que descreve a funcionalidade do Layout. Este texto será utilizado para geração do arquivo de documentação do Layout.

4Modo do Log

Selecione o nível de detalhe do Log do gerador, esta opção será utilizada principalmente para identificar problemas de performance na geração. As opções disponíveis são:

* Parâmetros e Erros
* Inicialização dos Contextos
* Leitura dos Items
* Processamento dos Items
* Leitura de Todos os Items
* Processamento de Todos os Items

5Diretório Padrão

Informe qual será o diretório padrão para geração, esta opção só poderá ser utilizada se a opção "Usa diretório padrão" estiver marcada.

6Conexão

Informe os dados para conexão com o banco de dados que será utilizado pelos contextos do gerador. Esta informação é obrigatória e deve ser informada antes de configurar qualquer opção que utilize o banco, como os contextos de Fonte de Dados e as opções de executar Stored Procedures. No caso do RM é utilizada a base de dados do contexto e esta opção não é exibida. Para mais informações consulte a [Configuração da Conexão](/pages/viewpage.action?pageId=319787266).

7Outras Propriedades

Nestas abas são informadas as demais propriedades do Layout, como a formatação padrão e a opção de executar uma DLL .NET. Para mais informações consulte [Formatação Padrão](/pages/viewpage.action?pageId=319787267) e [Executar](/display/LRM/Manual+-+Executar+DLL).

8Usa diretório padrão

Selecione esta opção para definir o diretório padrão onde os arquivos do Layout serão gerados. As finalizar a geração dos arquivos, os mesmos serão copiados automaticamente a pasta informada.
