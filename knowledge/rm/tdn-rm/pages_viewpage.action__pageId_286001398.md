---
content_hash: b897e4b238c71d57f90144b06ed6921040aa8f69ef274d8ab1f9fe202e91e67f
fetched_at: '2026-06-29T00:08:38.948527+00:00'
page_id: '286001398'
product: rm
source: tdn-rm
title: ER SAUHRM02-1400 - Cópia de itens de débito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286001398
version: 8
---

|  |
| --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |

Nenhuma anotação efetuada a mão ou rasura no documento será considerada válida.

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Faturamento |
| **Segmento Executor** | Saúde |  |  |
| **Projeto¹** | R\_SAU\_HRM1617 | **IRM¹** | SAUHRM02-1400 |
| **Requisito¹** | SAU\_BACKLOG-1958 | **SubTarefa¹** |  |
| **Chamado²** | 775050 |  |  |
| **Release de Entrega Planejada** | Não definido | **Réplica** | Não necessário |
| **País** | **(**X **) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador**   **(  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_.** |  |  |
| **Outros** |  |  |  |

# Objetivo

Permitir  a cópia da relação entre itens de débito e tabela de preço, quando houver atualização na tabela de preço indicada nas condições contratuais com convênio.

# Definição da Regra de Negócio

**RN001 –** Permitir que com a criação de uma nova condição contratual, onde haja alteração na tabela utilizada para PROCEDIMENTOS, DTS( Diárias, taxas e serviços) e ESPECIAL, o sistema rastreie os códigos de procedimento dos itens de débito que se mantém da tabela antiga para a nova.   
 **RN002 –** Ao identificar itens de débito com código mantido, o sistema deverá dispor de uma rotina para a atualização dos relacionamentos. Replicando os relacionamentos entre da tabela antiga com procedimentos, porém alterando o a identificação da tabela, indicando a nova tabela utilizada.   
 **RN003 –** Ao término do processo de atualização dos relacionamentos entre os itens de débito à nova tabela, o sistema deverá permitir que o usuário acesse uma listagem com os itens que não se mantiveram com a alteração da tabela. Ou seja, itens contidos na tabela antiga, para os quais não foi possível se identificar correspondência na nova tabela.

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
|  |  |  |
|  |  |  |

# Regras de interface

As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema, devem ser utilizadas apenas para exemplificar a forma de iteração que os usuários possuirão ao acessar o sistema, o fluxo de negócio e a forma em que os dados e informações serão manipuladas.

## Atualização automática de itens de débito

|  |  |
| --- | --- |
| **Função** | Atualização automática de itens de débito |
| **Objetivo** | Atualização automática de itens de débito |
| **Módulo** | Cadastros |

|  |  |
| --- | --- |
|  | **Regras de Interface** |
| **RI-001** | Criar uma nova opção nos processos da tela de condições contratuais chamada ATUALIZAÇÃO DE ITENS DE DÉBITO. |
| **RI-002** | Através deste processo o usuário poderá realizar a "cópia" dos itens de débito vinculados á tabela antiga, porém com o código da tabela nova. |
| **RI-003** | Identificação de itens com código mantido na atualização da tabela (mesmo código na tabela antiga e nova). Posteriormente deverá ser realizada a "cópia" dos relacionamentos, porém alterando o código da tabela. |
| **RI-004** | Esta rotina deverá afetar todas as telas onde é realizada precificação de itens de débito com base na tabela de preço.   Sendo identificadas preliminarmente:   -Itens de lançamento (Cadastros / Cuidados com Paciente / Prescrição Médica / Itens de Enfermagem)  -Exames e serviços (Cadastros / Unidade Diagnóstico / Exames e Serviços, Item de Débito)  -Condições contratuais de convênio (Cadastros / Faturamento / Condições Contratuais / Divisão de Honorário)  -Procedimentos cirúrgicos (Cadastros / Cuidados com Paciente / Cirurgias ) |

# Fluxo do Processo

Não necessário para o desenvolvimento deste requisito.

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.

# Assinaturas

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Cargo | Data | Ação | Assinatura |
| Cleber Correa | Analista de Negócio |  | Autor |  |
| Joji Tamekuni | Líder de Equipe de Desenvolvimento |  | Aprovador |  |
| Daniel Solari | Coordenador de Desenvolvimento |  | Revisor |  |
