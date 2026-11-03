---
content_hash: 2002c1a4a45db1f560a3beeae0277982d31db37c4d8cb44ff070714277ad0430
fetched_at: '2026-06-29T00:08:29.722320+00:00'
page_id: '272161126'
product: rm
source: tdn-rm
title: Execução de Sequência de Fórmulas Visuais em um Gatilho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272161126
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.16 e superiores |
| **Ocorrência:** | Descrição da execução de fórmulas visuais em sequência e as opções de execução |
| **Ambiente:** |  |
| **Passo a passo:** | Este documento tem a finalidade de descrever a execução de fórmulas visuais em sequência e as opções de execução    Acessando o gerenciamento de fórmulas visuais via visão (Processos - Fórmula Visual - Gerenciar), na aba gatilhos, é possível inserir várias fórmulas visuais em quantos gatilhos desejarmos.  No exemplo acima, inserimos 3(três) fórmulas ao gatilho "Após Salvar o Registro". Após a inserção as colunas "Tipo" e "Prioridade" ficam disponíveis para edição.  **Prioridade**   O item prioridade define a ordem em que as fórmulas serão executadas e o sistema respeita a ordem decrescente. No exemplo acima a ordem de execução das fórmulas seria: 2 - SEMPRE ERRO, 1 - TESTE EXCEÇÃO e 0 - TESTE PRIME.   **Tipo**   Esse campo define o tipo de vinculação no gatilho a que a fórmula será submetida. Atualmente existem 4 (quatro) tipos que podem ser utilizados:   * **Desativado** - Desabilita a vinculação sem removê-la, na ordem de execução, essa fórmula será ignorada. * **Ativado com Exceções** - A vinculação fica ativa e exibe possíveis erros que venham a ocorrer durante a execução da Fórmula Visual. Mesmo que ocorra erro em alguma das fórmulas as outras serão executadas normalmente. * **Ativado Ignorando Exceções** - Os erros que possam vir a ocorrer na execução das fórmulas são ignorados e não são exibidos ao usuário. Não interfere na execução das demais fórmulas. * **Ativado Parando Execução em Caso de Exceções -** Quando ocorre erro em alguma Fórmula Visual, esse erro é exibido ao usuário e a fila de execução de fórmulas é interrompida. |
| **Observações:** |  |
