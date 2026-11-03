---
content_hash: f9a8409f7f2dba460b90cf57538bb4c79298a1f6de68327a8f06644477806faf
fetched_at: '2026-06-29T00:06:07.349759+00:00'
page_id: '201736347'
product: rm
source: tdn-rm
title: DT_Cadastro_Banca_Estagio
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Cadastro_Banca_Estagio
version: 6
---

# Banca do estágio

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Totvs Educacional |
| **Módulo:** | Educacional |

## Descrição

Foi implementado a opção do professor cadastrar a banca após aprovação da avaliação final, e o estágio esteja caracterizado com 'Defesa'.

Essa funcionalidade pode ser acessada através do portal no menu Professor | Estágio | Banca, e no sistema em Atividades acadêmicas | Estágio | Termo de compromisso | (Anexo Banca do estágio).

**Cadastro da banca**:

* Data e hora da banca
* Local da banca
* Termo de compromisso referente

**Cadastro de participantes da banca**:

Depois de cadastrar a banca, é permitido inserir os participantes da banca. O participante da banca, poderá ser um professor ou um funcionário da empresa do termo de compromisso.

* Professor da instituição
* Funcionário da empresa do termo de compromisso do estágio
* Tipo de participante

Ao término da apresentação da banca, o usuário responsável pelo setor de estágio deverá acessar o sistema e informar as notas fornecidas pelos participantes da banca.

Como forma de consumir essas informações referentes as notas lançadas pelos participantes da banca, foram criadas quarto novas funções de fórmulas:

* SomaNotaNumericaEstagio: Soma todas as notas numéricas concedidas pelos avaliadores da banca de estágio.
* MediaNotaNumericaEstagio: Média das notas numéricas concedidas pelos avaliadores da banca de estágio.
* MaiorNotaNumericaEstagio: Maior nota numérica concedida pelos avaliadores da banca de estágio.
* MaiorNotaConceitualEstagio: Maior nota conceitual concedida pelos avaliadores da banca de estágio.
