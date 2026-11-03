---
content_hash: aa602a7699dc36d808d2b661861ceb2df9b1344f12ae13794533f5f34bc9496e
fetched_at: '2026-06-29T00:08:06.051102+00:00'
page_id: '236431180'
product: rm
source: tdn-rm
title: TUIVNO_DT_Associacao_Materiais_Turma_Gerencial_Gerenciada
type: documentation
url: https://tdn.totvs.com/display/LRM/TUIVNO_DT_Associacao_Materiais_Turma_Gerencial_Gerenciada
version: 119
---

# ASSOCIAÇÃO DE MATERIAIS NO PORTAL PARA TURMA GERENCIAL/GERENCIADA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Associação de Material no Portal para Turma Gerencial/Gerenciada* | *Associação de Material no Portal para Turma Gerencial/Gerenciada* | |
| **Cadastros Iniciais:** | *1) Aluno cadastrado com usuário no portal;*  *2) Professor cadastrado com usuário no portal;*  *3) Turma gerencial e gerenciada cadastrada, com professor vinculado;*  *4) Material postado pelo professor.* |
| **Parâmetro(s):** | *Educacional | Secretaria | Geral 1/5 | Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, freqüência diária, plano de aula e upload de materiais no portal* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *SWEBMATERIALSEC* |
| **Sistema(s) Operacional(is):** | *Windows 7* |

## Descrição

Ajuste na rotina de upload de materiais, para que ao associar um material a uma turma gerencial, o mesmo será associado as suas respectivas turmas gerenciadas.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(12.1.10.115)* deste chamado.

## Procedimento para Utilização

Para a rotina Associação de Material no Portal para Turma Gerencial/Gerenciada:

1. Acessar o Portal Educacional com usuário do professor;
2. Acessar Menu | Professor | Upload de Materiais;
3. Marcar material postado e clicar em Associar turma;
4. Se parâmetro "Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, freqüência diária, plano de aula e upload de materiais no portal" estiver **marcado**, serão exibidas as turmas/disciplinas Gerenciais e normais para serem selecionadas;  
   4.1 Ao associar o material a uma turma Gerencial, o mesmo será associado a ela e as suas respectivas Gerenciadas.
5. Se parâmetro "Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, freqüência diária, plano de aula e upload de materiais no portal" estiver **desmarcado**, serão exibidas as turmas/disciplinas Gerenciadas e as normais para serem selecionadas;  
   5.1 Ao associar o material a uma turma Gerenciada, o mesmo somente será associada a ela;
6. Acessar o Portal Educacional com o usuário do aluno;
7. Acessar Menu | Materiais | Arq. por disciplina;
8. O aluno somente verá os arquivos que foram associados às turmas gerenciadas que ele está matriculado.

Parâmetro: Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, freqüência diária, plano de aula e upload de materiais no portal.

**Importante: O aluno somente visualizará turmas/disciplinas gerenciadas. Por outro lado, o professor poderá visualizar turmas/disciplinas gerenciadas (se parâmetro estiver desmarcado) e gerenciais (se parâmetro estiver marcado), nunca as duas juntas.**

divs
