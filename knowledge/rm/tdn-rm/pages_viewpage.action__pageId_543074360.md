---
content_hash: d0407ebc65a0dd39c7b421753227d9469abd3987dc3b65f5e9b25029bd78a88c
fetched_at: '2026-06-29T00:10:37.886689+00:00'
page_id: '543074360'
product: rm
source: tdn-rm
title: Importar Tabela de Preço -  Processo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543074360
version: 2
---

Este recurso permite ao usuário importar tabelas de preço através de planilhas Excel ou Planilha Net.

## **Processo de “Importar uma nova tabela de preço através de planilha”**

Menu de acesso: Venda -> Tabela de Preço -> **Importar preço por planilha**

Para criar um **novo cadastro** através de uma planilha, na visão de Tabela de Preço, o Usuário deve executar o Processo de “**Importar Tabela de Preço por Planilha**” **sem selecionar nenhum cadastro.**

Conforme imagem abaixo:

Atenção!

Caso o Usuário execute este Processo **selecionando** qualquer Tabela de Preço existe (conforme imagem abaixo), o sistema tentará **sobrescrever** o Valor das Subunidades nesta tabela, mesmo que esta não tenha nenhuma Subunidade associada e apresentará uma exceção informando que não foi encontrada nenhuma Subunidade para gerar/alterar o Valor.

**Criando a Planilha:**

A Planilha pode ser criada utilizando Microsoft Excel ou Planilha Net.  
  
O arquivo da planilha deverá conter os campos que compõem a chave da Subunidade:

- Código do Empreendimento

- Código da Unidade

- Código da Subunidade

- E o campo do preço da Subunidade.

Importante:

* Para utilizar planilha em Excel é necessário que no servidor de aplicação exista o Microsoft Excel instalado, caso contrario será necessário utilizar a Planilha Net.
* Como cadastrar um Planilha Net:
* O código do empreendimento e o código da unidade são necessários para que o sistema possa identificar que o usuário selecionou um arquivo errado e interromper o processo.
* Devido o sistema não possuir um padrão para o código do apartamento no banco de dados, por exemplo, podemos ter na mesma unidade, uma Subunidade “102”, “000102” ou “0102”, o código da Subunidade na planilha deve ser “exatamente” igual ao código da Subunidade gravado no banco de dados (considerando os zeros a esquerda).

Exemplo de uma planilha:

**Parâmetros necessários para importação:**

Para a correta importação da planilha é necessário preencher os parâmetros de importação, considerando a planilha cadastrada.

* Nome da tabela de Preço: O nome informado será utilizado para a tabela importada.
* Empreendimento: Necessário informar qual o empreendimento que irá utilizar a tabela de preço.
* Data inicio da Vigência: E a data de inicio da Vigência da tabela de preço.
* Forma Seleção Arquivo: Informe o Tipo de Planilha que será utilizado.

* Registro de Preço Inicial: Deve ser verificado na planilha as células onde a informação está armazenada.

Caso a célula seja “fixa”, como o código do Empreendimento e o código da Unidade, o usuário deverá informar a célula com cifrão:

Exemplo: $b$2

Caso a célula seja “variável”, como o código da Subunidade e o preço, o usuário deverá informar a célula inicial sem cifrão:

Exemplo: B6

* Tabela de Preço: No campo 'Nome da planilha' deve ser informado o nome atribuído a aba da planilha cadastrada.

Com o objetivo de facilitar o processo de importação de planilhas, o Checkbox “Manter configuração de importação” indica que as configurações realizadas nesta tela serão mantidas para a próxima importação de planilha, considerando que todas as planilhas de tabela de preço do cliente tenham o mesmo formato.
