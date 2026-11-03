---
content_hash: 5898ee145a3dd0cd08031927b00ac7fc04b295be26307dbc5c59bb73f854b648
fetched_at: '2026-06-29T00:08:07.009688+00:00'
page_id: '236600551'
product: rm
source: tdn-rm
title: TUOCH1_DT_Nao_Atualizar_Situacao_Matric_Disciplina_Matricula_Online
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOCH1_DT_Nao_Atualizar_Situacao_Matric_Disciplina_Matricula_Online
version: 116
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Gestão Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Matrícula online* | *Matrícula online* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Matrícula em disciplina** | *Alteração de situação de matrícula em disciplina* | |  |  | |
| **Cadastros Iniciais:** | *Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito.* |
| **Parâmetro(s):** | *- Educacional | RM Portal - Matrícula | Geral 1/4 | Situação de matrícula após a matrícula na disciplina* |
| **Ponto de Entrada:** | *Portal Educacional | Acadêmico | Matrícula Online* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *SQL Server e ORACLE* |
| **Tabelas Utilizadas:** | *SSTATUS* |
| **Sistema(s) Operacional(is):** | *Ver documento de portabilildade RM nesta versão* |

## Descrição

Criação do parâmetro "Não alterar situação de matrícula (apenas para matrícula on-line)" no cadastro de situações de matrícula na pasta "Situação de matrícula na disciplina".

Ao habilitar este parâmetro, o sistema não permite alterar a situação de matricula do aluno nas disciplinas quando a matricula for feita pelo portal mesmo quando no perfil do usuário, o parâmetro "Permite alterar situação de matrícula na disciplina" estiver habilitado.

Esta parâmetro está disponível apenas para o nível de ensino superior e é liberada apenas após a execução de script.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado e aplicação do script (enviado mediante solicitação).

1. Aplique o patch do chamado e o script mencionado
2. Após executar o login no RM, selecione o módulo Educacional
3. Abra o cadastro *de situação de matrícula* (Currículo e Oferta | Acadêmico).
4. Verifique que o parâmetro *Não altera a situação de matrícula na disciplina (apenas para matrícula on-line)* é criado conforme especificações abaixo:

|  |  |
| --- | --- |
| **Nome da Variável:** | *Não altera a situação de matrícula na disciplina (apenas para matrícula on-line)* |
| **Tipo:** | *Boleano* |
| **Descrição:** | *Não altera a situação de matrícula na disciplina (apenas para matrícula on-line)* |
| **Valor Padrão:** | *False* |

## Procedimento para Utilização

       1.            No módulo Educacional, acesse Currículo e Oferta/ Acadêmico / Situação de Matrícula.

O sistema apresenta as situações de matrículas cadastradas.

       2.            Selecione para edição a situação de matrícula configurada no parâmetro *Educacional | RM Portal - Matrícula | Geral 1/4 | Situação de matrícula após a matrícula na disciplina*.

       3.            Na pasta Status na Disciplina marque a parâmetro *Não alterar situação de matrícula (apenas para matrícula on-line)*  e clique em Salvar.

       4.           Após esta configuração, qualquer inclusão de matrícula em disciplinas para um aluno pelo Portal não atualizará a situação de matrícula das disciplinas em que ele já estiver matriculado.

divs
