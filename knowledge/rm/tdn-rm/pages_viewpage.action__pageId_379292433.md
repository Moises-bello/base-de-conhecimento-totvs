---
content_hash: ba13f973ee6d9ad24222ed8f992b7754a61bb4f78d39955389b041f481bd4832
fetched_at: '2026-06-29T00:09:02.168228+00:00'
page_id: '379292433'
product: rm
source: tdn-rm
title: DT Data Continuidade de Afastamento - Histórico de Afastamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379292433
version: 1
---

# Continuidade de Afastamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cadastro de Funcionário | Continuidade de Afastamento |
| **Situação/Requisito:** | O cliente quer ter a possibilidade de cadastrar continuidade de afastamento manualmente. |
| **Solução/Implementação:** | Foi implementado uma alternativa na forma como continuidades de afastamentos são feitos. Agora é possível que o usuário configure, em algumas situações, manualmente os afastamentos que são continuidade um do outro. Isso é feito através de uma data, campo "Dt. Inicial da Continuidade de Aft.", que serve para associar um afastamento a outro previamente cadastrado. |
| **Documento de Referência:** | <http://wikihelp.totvs.com.br/WikiHelp/RHU/FOP.HistoricoSAfastamentos.aspx> |

No cadastro de Histórico de Afastamentos, anexo do Funcionário, foi criado um campo do tipo "lookup", para a ligação dos registros que terão a continuidade do período de Atestado Médico.

Na lista para seleção desse "lookup", são exibidos todos os registros de afastamento com tipos P (Previdência), T (Acidente de Trabalho) e O (Doença Ocupacional) que podem iniciar uma continuidade. Para ser candidato a um registro que dá início a uma continuidade, além de possuir um dos tipos listados anteriormente, o campo de relacionamento do afastamento em questão deve estar vazio. Dessa forma, os afastamentos que iniciam a sequência de continuidade, chamados de registro Pai, não possuem valores no componente "Dt. Inicial da Continuidade de Aft." (lookup para associar afastamentos).

Na tabela de Histórico de Afastamentos foi criado um campo para armazenar a Data de Início do afastamento selecionado pelo usuário. Esta informação ficará gravada em todos os registros que participarem da sequência de continuidade, chamados de registros Filhos.

Não será permitida a exclusão de períodos de afastamento que forem selecionados em outros registros como o afastamento inicial da sequência. Para isso, o usuário deverá acessar todos os registros Filhos e limpar o campo de relacionamento, para então excluir o registro Pai.
