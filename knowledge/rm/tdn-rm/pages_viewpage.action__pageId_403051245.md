---
content_hash: c1e8fb930bd24ec210987fbd0652a5d07721de4ae6107a17c620eb66de8d0e73
fetched_at: '2026-06-29T00:09:10.884872+00:00'
page_id: '403051245'
product: rm
source: tdn-rm
title: DT Gerar Plano de Contas Paralelo a partir do Plano de Contas Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403051245
version: 5
---

# Gerar Plano de Contas Paralelo a partir do Plano de Contas Contábil

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Contábil |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Processo | Gerar o Plano de Contas Paralelo a partir do Plano de Contas Contábil |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Planos de contas paralelos | Tipos de Planos de Contas Paralelos | | Contas Paralelas | Contas Paralelas | |
| **Cadastros Iniciais:** | Plano de Contas Paralelo |
| **Parâmetro(s):** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [http://jiraproducao.totvs.com.br/browse/](http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7687)[CONTROLADORIA01-1882](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1882) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |
| **Tabelas Utilizadas:** | CPARALELO, CCONTA2, CCTACTA2 |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.22 |

## Descrição

O processo tem como objetivo gerar o plano de contas paralelo a partir de um plano de contas contábil que possua máscara. Além de gerar o novo plano paralelo ainda existe a possibilidade de mapear automaticamente as contas contábeis que foram utilizadas como modelo para geração das contas paralelas.

A tela possui os seguintes campos:

1 - Coligada do Plano de Contas Contábil: Esta opção lista todas as coligadas disponíveis para ser utilizada no processo de geração do novo plano paralelo.

2 - Código do Plano Paralelo: Código do novo plano de contas paralelo. O código deve ser diferente de um já cadastrado para coligada que está executando o processo.

3 - Descrição do Plano Paralelo: Descrição do plano de contas paralelo. O campo pode conter no máximo 40 carácteres.

4 - Grupo de Contas: Grupo de contas que serão utilizados para serem a base das novas contas paralelas que serão criadas.

5 - Instituição Responsável / Finalidade: Esta opção lista todos os tipos de plano paralelo que podem ser utilizados pelo processo.

6 - Associar a coligada selecionada ao Mapeamento do Plano Paralelo: Esta opção define se a coligada que foi utilizada no campo será mapeada automaticamente ou não as contas paralelas criadas.

Vale ressaltar que os campos acima são obrigatórios exceto o campo 6 (Associar a coligada selecionada ao Mapeamento do Plano Paralelo).

## Procedimento para Utilização

1 - Acesse o cadastro de plano de contas paralelos.

2 - Selecione o processo "Gerar o Plano de Contas Paralelo a partir do Plano de Contas Contábil".

3 - Selecione as opções desejadas, preenchas os campos.

4 - Execute o processo.
