---
content_hash: 26e10de0155394c20cc33a7a2eebf27b80e5e4110c2ba5364962aa90004bcc33
fetched_at: '2026-06-29T00:09:38.721336+00:00'
page_id: '429197828'
product: rm
source: tdn-rm
title: DT Histórico Escolar - Ensino Básico - Partes do Histórico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=429197828
version: 84
---

# HISTÓRICO ESCOLAR - ENSINO BÁSICO - PARTES DO HISTÓRICO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de disciplinas do histórico* | **Cadastro de disciplinas do histórico** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Digitação do histórico* | **Digitação do histórico** | | *Processo geração do histórico* | *Processo geração do histórico* | | *Geração de relatório - EDUREL0001 - Histórico Escolar - Ensino Fundamental* | *Geração de relatório - EDUREL0001 - Histórico Escolar - Ensino Fundamental* | | *Geração de relatório - EDUREL0002 - Histórico Escolar - Ensino Médio* | *Geração de relatório - EDUREL0002 - Histórico Escolar - Ensino Médio* | | *Geração de relatório - EDUREL0063 - Histórico Escolar - Ensino Fundamental I e II* | *Geração de relatório - EDUREL0063 - Histórico Escolar - Ensino Fundamental I e II* | |
| **Cadastros Iniciais:** | * *Cursos do histórico;* * *Grupo de séries;* * *Disciplinas do histórico;* * *Partes do histórico.*   *Link referente aos cadastros básicos para se gerar um histórico: <http://tdn.totvs.com/x/MJglE>* |
| **Parâmetro(s):** | *Em Configurações | Parâmetros | Secretaria:*   * *Utilizar disciplinas de mesmo grupo de série em partes de histórico diferentes* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-2489* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *SHISDISCCOL* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

Foi criado um parâmetro (*Utilizar disciplinas de mesmo grupo de série em partes de histórico diferentes*) do TOTVS Educacional para flexibilizar que disciplinas de mesmo grupo de série possa estar configurada para partes diferentes do histórico. Quando parametrizado para permitir, o sistema ecoa uma mensagem de aviso, pedindo ao usuário que confirme tal inserção. Caso o parâmetro esteja negando essa permissão o sistema continuará com o comportamento atual, bloqueando esta inserção.

**Importante**: o *default* para esse parâmetro é não permitir que disciplinas de mesmo grupos de serie possa estar em partes de histórico diferentes.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.19.

## Cadastrando uma disciplina no histórico de mesmo grupos em partes do histórico diferentes

Para cadastrar uma disciplina no histórico, deve-se seguir os seguintes passos:

* Acessar o cadastro do aluno em em Currículo e Oferta | Aluno | anexo Histórico | selecionar um histórico e ir no anexo Disciplinas do histórico.
* Criar uma nova disciplina e informar a parte do histórico diferente da já cadastrada. Ao tentar salvar o sistema irá alertar o usuário conforme abaixo, caso o sistema esteja configurado para isso, ou seja, com o parâmetro *Utilizar disciplinas de mesmo grupo de série em partes de histórico diferentes*marcado.
* Caso o sistema não esteja configurado para deixar isso acontecer, uma mensagem de bloqueio será exibida, conforme abaixo.

O mesmo comportamento acima terá a digitação do histórico em Currículo e Oferta | Aluno | anexo Digitação de histórico.

## Geração do histórico com uma disciplina de mesmo grupo em partes do histórico diferentes

No processo de geração de histórico em Matrícula e Avaliação | Rotinas periódicas | Geração de histórico, um log será exibido no final do processo informando que aquela disciplina já foi cadastrada no grupo de série com parte do histórico diferente, entretanto se o parâmetro estiver marcado a disciplina será cadastrada no histórico, caso não estiver marcado a disciplina não será cadastrada.

## Geração do relatório EDUREL0001 - Histórico Escolar - Ensino Fundamental com uma disciplina de mesmo grupo em partes do histórico diferentes

Observação: procedimento para geração do histórico - <http://tdn.totvs.com/x/MJglE>.

divs
