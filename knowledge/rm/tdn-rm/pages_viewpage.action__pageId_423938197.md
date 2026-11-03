---
content_hash: 01348066803d73d5b9fe69a685e803a955f7689a5004c2d07076af7045d88248
fetched_at: '2026-06-29T00:09:25.897890+00:00'
page_id: '423938197'
product: rm
source: tdn-rm
title: Atualização do Conceito de Importação de Cotação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938197
version: 31
---

Layout de Conceito descontinuado a partir da versão 12.1.2306.

Para realizar a importação da cotação utilize o processo **Importar Planilha de Orçamento/Negociação (Novo)!** disponível na visão do cadastro de Cotação.

Ao alterar o parâmetro 'Nome Marca', caso se utilize Exportação / Importação de planilha Excel, será necessário configurar novamente o conceito utilizado neste processo.

Caminho de acesso deste campo, no parametrizador do módulo.

Exemplo de possível alteração.

Para configurar o conceito, deve-se primeiro Exportar uma Cotação.

Nesse exemplo, após a execução bem sucedida do processo 'Comunicar Fornecedores', a planilha será enviada para o(s) Fornecedor(es) da Cotação, através do e-mail informado em seu(s) cadastro(s). Para dar continuidade à configuração do conceito, a Planilha exportada será necessária.

Acessar a visão de Conceitos, contida no módulo 'Integração'.

Localizar e editar o Conceito utilizado para importação de Orçamento / Negociação.

Deve-se acessar as configurações da 'Planilha\_Orcamento', localizada na árvore de Conexões de Origem.

Defina no campo "Data Source" o caminho para a planilha exportada.

Depois acesse a página "Tabelas", selecione "Item\_Orçamento" e marque os itens que aparecerão desmarcados. A primeira palavra de cada um deles deve refletir a alteração realizada no parâmetro "Nome Marca'", indicado no início deste documento. Salve as alterações clicando no botão "OK".

Acesse a página "Ligações".

Navegue até encontrar os campos que precisam ser alterados na tabela TCITMORCAMENTO. Os campos "MARCAS.." foram atualizados na referência à direta, mas também precisam ser atualizados na coluna origem.

Clicar em "Expressão" arrastar até o campo, vai ser exibido janela de ligação. Na janela de ligação selecione "Parâmetros" -> "Item\_Orçamento" e localize o campo MARCAS.

Acesse "Funções" e adicione o Trim e Split para ficar como no original

* Funções -> Texto -> Trim
* Funções -> Texto -> Split

[Trim(Split(Item\_Orcamento.QUANTIDADE\_\_ORÇADA,'|',0))]. Clique OK.

Após ajustar cada campo que seja necessário salve o conceito.
