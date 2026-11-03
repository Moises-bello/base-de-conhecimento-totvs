---
content_hash: fb85dadd78ca915a2da22444978abbdb8685fb571e23e091670db0b7f08abadd
fetched_at: '2026-06-29T00:09:12.133024+00:00'
page_id: '415715055'
product: rm
source: tdn-rm
title: RMPES00002_Como fazer - Lançamento de Atestados - Data Continuidade de Afastamento.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415715055
version: 4
---

# Continuidade de Atestados

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Gestão de Pessoas |
| **Módulo:** | Segurança e Medicina do Trabalho |
| **Função:** | Visão de Funcionários | Anexos | Segurança e Medicina | Atestados |
| **Situação/Requisito:** | O cliente quer ter a possibilidade de cadastrar atestados com continuidade de afastamento manualmente. |
| **Solução/Implementação:** | Foi implementado uma alternativa na forma como continuidades de atestados são feitos. Agora é possível que o usuário configure, em algumas situações, manualmente os atestados que são continuidade um do outro. Isso é feito através de uma data, campo "Data Inicial da Continuidade de Afastamento.", que serve para associar um atestado a outro previamente cadastrado. |
| **Documento de Referência:** |  |

Na visão de Funcionários, acesse 'Anexos', em seguida 'Segurança e Medicina', e então na opção 'Atestados'.

Ao selecionar a opção de cadastrar novo atestado, caso o Motivo do Afastamento do Atestado seja dos tipos P (Previdência), T (Acidente de Trabalho) e O (Doença Ocupacional), um lookup (Data inicial da continuidade de Afastamento) permitirá que seja cadastrada uma continuidade de afastamento gerados por atestados inseridos anteriormente.

Detalhe do lookup (Data inicial da continuidade de Afastamento):

Ao clicar no botão do lookup, a janela de seleção de atestados é aberta, listando atestados cadastrados COM DATA ANTERIOR à data INÍCIO do novo atestado:

Ao selecionar um Atestado e salvar, é criada a continuidade relacionada ao Atestado "Pai".

Não será permitida a exclusão de atestados que forem selecionados em outros registros como o atestado inicial de continuidade da sequência. Para isso, o usuário deverá acessar todos os registros Filhos e limpar o campo de relacionamento, para então excluir o registro Pai.

Páginas Relacionadas:

* # Continuidade de Afastamento
