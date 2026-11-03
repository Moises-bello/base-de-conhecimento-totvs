---
content_hash: ecd764dd8958b2d8e948543d408e5d1526004ae2b9e4c126af72a94cc3bb10c4
fetched_at: '2026-06-29T00:08:46.396002+00:00'
page_id: '317293544'
product: rm
source: tdn-rm
title: DT Log de Alteração de Campus/Polo no Curso/Habilitação do Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317293544
version: 121
---

# LOG DE ALTERAÇÃO DE CAMPUS/POLO NO CURSO/HABILITAÇÃO DO ALUNO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Log de Campus/Polo* | *Log de Campus/Polo* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Cadastro de Curso/Habilitação do Aluno** | ***Cadastro de Curso/Habilitação do Aluno*** | |
| **Cadastros Iniciais:** | *Campus/Polo em Currículo e Oferta | Auxiliares;*  *Curso/Habilitação do Aluno em Currículo e Oferta | Aluno | Anexo Cursos/Habilitações* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-2849* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *SLOGCAMPUS* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

O log de Campus/Polo presente na tela de Log de Movimentações do Aluno tem por finalidade registra qualquer mudança de Campus/Polo do Curso/Habilitação do Aluno, ou seja, ao se alterar/inserir/remover o campus/polo é feito o registro desta informação neste log.

Além disso, foi incluído neste log a informação da Matriz Aplicada (irá conter *Nome do Curso - Nome da Habilitação - Código da Matriz Curricular - Nome do Turno*) do aluno.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.19.

## Procedimento para Utilização

* Acessar o cadastro de Campus/Polo em Currículo e Oferta | Campus/Polo;
* Criar um novo Campus/Polo que será utilizado no Curso/Habilitação do Aluno;
* Vincular este Campus/Polo na Matriz Aplicada em Currículo e Oferta | Matriz Curricular | Selecionar uma Matriz e ir em Anexo Matriz Aplicada | Selecionar uma Matriz Aplicada e ir em Anexo Campus/Polo da Matriz Aplicada e inserir o Campus/Polo criado;
* Acessar o Curso/Habilitação do Aluno em Currículo e Oferta | Aluno, ir no anexo Cursos/Habilitações | Criar um Curso/Habilitação para este aluno e informar o Campus, ao salvar é gravado no Log de Movimentações de Campus/Polo esta operação;

  | Inserindo um Curso/Habilitação informando um Campus/Polo | Log de Movimentação do Campus do Curso/Habilitação do Aluno |
  | --- | --- |
  |  |  |

* Ainda neste mesmo Curso/Habilitação ao alterar o campus/polo para outro diferente, a informação é gravada no log;

  | Alterando um Campus/Polo no Curso/Habilitação do Aluno | Log de Movimentação do Campus do Curso/Habilitação do Aluno |
  | --- | --- |
  |  |  |

* Por último ao remover o campus/polo do Curso/Habilitação do Aluno, também é gravada no log tal movimentação.

  | Removendo um Campus/Polo no Curso/Habilitação do Aluno | Log de Movimentação do Campus do Curso/Habilitação do Aluno |
  | --- | --- |
  |  |  |

divs
