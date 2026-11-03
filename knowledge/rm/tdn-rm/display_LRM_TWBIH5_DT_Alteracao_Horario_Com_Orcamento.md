---
content_hash: d55d3cce502ad33219fe9b0b713c551e0857c0aa9dc284e63e1afdcbcc79fa7a
fetched_at: '2026-06-29T00:08:20.959506+00:00'
page_id: '268798369'
product: rm
source: tdn-rm
title: TWBIH5_DT_Alteracao_Horario_Com_Orcamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TWBIH5_DT_Alteracao_Horario_Com_Orcamento
version: 110
---

# ALTERAÇÃO DE HORÁRIO QUANDO EXISTE ORÇAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construções e Projetos |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Alterar Cadastro de horário.* |
| **Situação/Requisito:** | Uma vez gerado a Lotação para alimentar o Orçamento de Pessoal. E posteriormente tentar alterar um horário ao funcionário que foi incluído no orçamento, o sistema apresenta erro de violação de chave estrangeira, pois nas tabelas de orçamento existem referencias para a tabela AINDHOR, e o processo do chronus deleta o indicie e cria o mesmo novamente.  Desta forma não poderia existir referência das tabelas do orçamento para a tabela AINDHOR pois quando o processo de alterar o índice for realizado o sistema irá deletar o índice e gerar o mesmo novamente. |
| **Solução/Implementação:** | *Foi realizada a criação de um script para remover as chaves estrangeiras das tabelas PORCAMENTOLOTACAOFUNC, PORCAMENTOLOTACAOCADHST, PORCAMENTOADMISSAO , PORCAMENTOLOTACAOCAD referente a tabela AINDHOR para que ao realizar o processo de alteração de jornada planejada o erro não ocorra mais.* |
| **Chamados relacionados:** | TWBIH5 |

divs
