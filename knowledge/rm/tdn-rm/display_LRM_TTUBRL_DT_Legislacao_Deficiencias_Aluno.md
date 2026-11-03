---
content_hash: 03157b0d825f710145922eb26565f30cebc69ac5c6b483345aece27b6b28aec3
fetched_at: '2026-06-29T00:06:21.622950+00:00'
page_id: '223173753'
product: rm
source: tdn-rm
title: TTUBRL_DT_Legislacao_Deficiencias_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUBRL_DT_Legislacao_Deficiencias_Aluno
version: 1
---

# ALUNO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Gestão Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Aluno* | *Cadastro de Aluno* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Censo Escolar** | *Processo de envio de informações do Censo*  *Anexo Dados do Censo Escolar e SISTEC* | |  |  | |
| **Cadastros Iniciais:** | *Pessoa e Aluno* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *Currículo e Oferta | Aluno e Professor | Alunos* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e ORACLE* |
| **Tabelas Utilizadas:** | *SALUNO, SALUNOMEC, PPESSOA* |
| **Sistema(s) Operacional(is):** | *N/A* |
| **Versões/Release:** | *12.1.9* |

## Descrição

Nesta implementação foi realizada uma reformulação dos campos referentes a deficiências do Aluno para possibilitar maior flexibilidade ao usuário no cadastro destas informações no Sistema.

Foram criadas duas novas abas no cadastro do Aluno, Pessoa com Deficiência (PCD) e Atendimento Especial.

Além disso, os campos com informações de deficiências do cadastro de Aluno e do anexo Dados do Censo Escolar e SISTEC foram unificados.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado e a execução de script específico (enviado mediante solicitação).

1. Aplique o patch do chamado, execute o script na base de dados e acesse uma vez a rotina *Cadastro de Alunos*.
2. Após isto, estarão disponíveis duas novas abas na pasta Identificação: Pessoa com Deficiência (PCD) e Atendimento Especial.
3. Acesse também o anexo Dados do Censo Escolar e SISTEC. Os campos de deficiências enviadas para o Censo são os mesmos exibidos na nova aba criada no cadastro do Aluno.

## Procedimento para Utilização

       1.            No módulo Educacional, acesse Currículo e Oferta | Aluno e Professor | Alunos.

Após a execução de um filtro, o sistema apresenta a janela de alunos cadastrados para o contexto selecionado.

       2.            Posicione o cursor em um aluno e clique em Alterar.

       3.            Na pasta Identificação selecione a aba Pessoa com Deficiência.

       4.            Informe os dados dos novos campos.

       6.            Confira os dados e confirme.

       7.            Selecione um aluno e abra para edição o anexo Dados do Censo Escolar e SISTEC.

                      Os mesmo campos com dados referentes a deficiências do Aluno são exibidos.

       8.            Confira os dados e confirme.

divs
