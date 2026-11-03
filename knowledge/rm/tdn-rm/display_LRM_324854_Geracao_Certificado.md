---
content_hash: e414cdb7182e6c958e80ed4791c0642ac156b64a87b80cb7e120e51ae457b57c
fetched_at: '2026-06-29T00:08:26.528809+00:00'
page_id: '271182611'
product: rm
source: tdn-rm
title: 324854_Geracao_Certificado
type: documentation
url: https://tdn.totvs.com/display/LRM/324854_Geracao_Certificado
version: 110
---

# Certificado e Diploma

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Certificado e Diploma | *Geração de certificado* | |
| **Cadastros Iniciais:** | *Necessário que o aluno tenha concluído o curso para que seja possível gerar o certificado.* |
| **Parâmetro(s):** | Gerar um novo certificado para o aluno, que já possui certificado registrado para a mesma habilitação filial |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito (informe o requisito relacionado):** | N/A |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *SCERTIFICADO* |
| **Sistema(s) Operacional(is):** | *Todos* |

## Descrição

Conforme legislação, alguns cursos é necessário que por algum motivo o aluno renove o seu certificado, sendo necessário cursar o curso inteiro novamente e no final do curso receba um novo certificado.

Por este motivo, foi criado um parâmetro nos parâmetros gerais do sistema que quando marcado possibilita emitir um novo certificado para o aluno mesmo que ele já possua certificado gerado para aquela habilitação filial.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Nos Parâmetros do sistema Secretaria, marcar o parâmetro "Gerar um novo certificado para o aluno, que já possui certificado registrado para a mesma habilitação filial":

## Procedimento para Utilização

       1.            Acessar o processo de Geração de Certificados / Diplomas:

       2.            Selecionar o aluno que deseja gerar o certificado baseado nos filtros necessários:

       3.            Selecionar o tipo Certificado:

       4.            Executando o processo normalmente, ao final do processo se o aluno não possuir para aquela habilitação filial um certificado com a mesma data de registro o sistema irá gerar um novo certificado:

       5.            Se o aluno possuir para aquela habilitação filial certificado cadastrado com a mesma data de registro, o processo não irá gerar um novo certificado e irá informar ao usuário:

divs
