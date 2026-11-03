---
content_hash: 6fb4ed6b7655cbf75cf484d914f070a4080e096b56364727a9c1f56bac23b0a8
fetched_at: '2026-06-29T00:08:25.719621+00:00'
page_id: '270924370'
product: rm
source: tdn-rm
title: 357460 MEDU-1979 DT Quadro Horário Aluno Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270924370
version: 110
---

# QUADRO DE HORÁRIO DO ALUNO NO PORTAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Quadro de Horário do Aluno no Portal* | *Quadro de Horário do Aluno no Portal* | |
| **Cadastros Iniciais:** | *1) Turma/Disciplina cadastrada com horário, prédio, bloco e sala;*  *2) Aluno matriculado na turma/disciplina do item 1 e com usuário para acessar o portal.* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *357460* |
| **Requisito (informe o requisito relacionado):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

Ajustes para que seja exibido o código concatenado com a descrição (melhoria realizada) para prédio, bloco e sala. Além de incluir a coluna bloco na grid das disciplinas exibidas.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(11.83.55)* deste ticket.

## Procedimento para Utilização

1. Necessário uma turma/disciplina com horário cadastrado, prédio, bloco, sala bem como aluno matriculado nesta turma/disciplina e com acesso no portal;
2. Acessar o portal e ir em Acadêmico | Quadro de Horários;
3. Será exibido o código - descrição concatenados para as colunas prédio, bloco e sala conforme imagem abaixo.

divs
