---
content_hash: ae5a07e74c6887a6eb7fc314eefe8d10a61e8046e93dd6b4010b523250d8aeae
fetched_at: '2026-06-29T00:09:12.160297+00:00'
page_id: '415716315'
product: rm
source: tdn-rm
title: Como Fazer - Assistente de Associação de Perfis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415716315
version: 1
---

Assistente de Associação de Perfis

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Segurança e Saúde Ocupacional |
| **Módulo:** | Assistente de Associação de Perfis |
| **Função:** | PCMSO | Perfil de Exames |

**Criação de um Perfil de Exame**

Totvs Segurança e Saúde Ocupacional

PCMSO | Perfil de Exames.

Incluir um novo perfil de exames e informar os dados solicitados como Identificador e Nome (que são obrigatórios), Anotações Médicas e Observação.

No aba “Bateria de Exames” selecionar os exames desejados, informar o tipo e a data inicial de exigência do exame.

**Campos:**

* **Exame:** informe os exames desejados pré-cadastrados no menu “Segurança e Saúde Ocupacional | PCMSO | Exames | Exames”;
* **Tipos de Exame:** os tipos possíveis conforme NR7 são ‘Admissional’, ‘Demissional’, ‘Periódico’, ‘Mudança de Função’ e ‘Retorno ao Trabalho’;
* **Exigido a partir de:** permite que o perfil de exames seja exigido somente a partir de uma determinada data. Se o usuário não preencher o campo, será considerada como data para verificação se o exame está ou não pendente para o funcionário a data de admissão ou de mudança de função do mesmo. Ou seja, conforme o Perfil de Exame associado para a função do funcionário, serão exibidos no prontuário todos os exames que possuem uma periodicidade e que não foram realizados pelo funcionário.
* **Periodicidade:** caso o tipo de exame informado seja ‘Periódico’, é obrigatório informar a quantidade de dias ou uma fórmula para o cálculo da periodicidade.

É possível acessar o menu de bateria de exames, através da tela principal em “Anexos | Bateria de Exames”.

**Associação de Perfis**

No “Assistente de Associação de Perfis de Exames” o perfil de exames poderá ser associado a uma Função, Seção, Lotação ou Consulta SQL. Caso a opção seja por “Lotação”, deverá selecionar se o sistema deverá agrupar os funcionários por ‘Função’ ou ‘Seção’.

Ao clicar sobre o botão “Avançar”, será exibida a tela para informar as funções a serem associadas aos perfis.

O assistente exibe os perfis já associados e permite que outros perfis sejam adicionados ou excluídos.

Para novas associações, clique sobre o perfil de exame desejado e arraste-o até a função/seção a ser associada. Para desassociar o perfil à função/seção, basta clicar sobre o perfil e apertar a tecla “Del” (ou “Delete”).

**Geração de Exames Pendentes do Funcionário**

Para visualizar o processo de geração dos exames pendentes, acesse o Boletim Técnico "Geração de Exames Pendentes" no link abaixo:

[Geração de Exames Pendentes](http://tdn.totvs.com/pages/viewpage.action?pageId=4812916)
