---
content_hash: e75a4c8509d008d19c2a75551e0cde13fe2aea2209d151c1cc5aca13f6f9c975
fetched_at: '2026-06-29T00:08:33.865288+00:00'
page_id: '274329817'
product: rm
source: tdn-rm
title: SAUHRM02-10037 - Mudança de categoria por perfil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274329817
version: 2
---

|  |
| --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |

Nenhuma anotação efetuada a mão ou rasura no documento será considerada válida.

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| **Produto** | HIS | **Módulo** | PERFIL USUÁRIO |
| **Segmento Executor** | Saúde |  |  |
| **Projeto¹** |  | **IRM¹** |  |
| **Requisito¹** | SAUHRM02-1002 | **SubTarefa¹** | SAUHRM02-1003 |
| **Chamado²** |  |  |  |
| **Release de Entrega Planejada** | V12.1.17\_GoBack | **Réplica** | Não necessário |
| **País** | **(**X **) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador**   **(  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_.** |  |  |
| **Outros** |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

Possibilitar o controle na alteração do convênio/categoria de um atendimento com base no perfil de acesso do usuário.  
 \_Toc355276664

# Definição da Regra de Negócio

**RN001 –** Deverá ser incluído o parâmetro para alteração de convênio/categoria de atendimento no cadastro de perfil de acesso;   
 **RN002 –** O controle será baseado no convênio destino da alteração.

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Configuração de perfil de usuário | Alteração | Cadastros > Segurança > Perfis:Outras informações |
| Mudança de categoria/plano/subplano | Alteração | Faturamento > Mudança da categoria do paciente |

# \_Toc355276665Protótipo de Tela

As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema, devem ser utilizadas apenas para exemplificar a forma de iteração que os usuários possuirão ao acessar o HIS, o fluxo de negócio e a forma em que os dados e informações serão manipuladas.

## \_Toc355276666Configuração de Ordenação de Leitos por Unidade

|  |  |
| --- | --- |
| **Função** | Troca de convênio/categoria |
| **Objetivo** | Criar no cadastro de perfil a opção para indicação do tipo de alteração de convênio/categoria permitida ao perfil. |
| **Módulo** | Cadastros |
| **Menu** | Cadastros > Segurança > Perfil |

|  |
| --- |
| **Protótipos** |
| A tela de parâmetros, apresentada como complemento no cadastro de perfil, terá a inclusão do grupo TROCA DE CONVÊNIO/CATEGORIA na sua aba GERAL |

|  |  |
| --- | --- |
|  | **Regras de Interface** |
| **RI-001** | Nesta tela a seleção deverá indicar o tipo de convênio para o qual será possível a alteração, quando o usuário se enquadrar no perfil selecionado.   * Origem convênio: Somente é permitida a alteração para convênios do tipo CONVÊNIO; * Origem particular: Somente é permitida a alteração para convênios do tipo PARTICULAR; * Ambos: É permitida a alteração para convênios de ambos os tipos – Opção default da tela. |

# \_Toc355276667Fluxo do Processo

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
| Heriton Mascarelo | Analista de Negócio |  | Autor |  |
| Braian Bastos | Analista de Negócio |  | Revisor |  |
| Diorgenes Tavares | Líder de Equipe de Desenvolvimento |  | Aprovador |  |
| Gabriela Bassaneto | Consultora Especialista |  | Aprovadora |  |
| Mariana Cruz | Líder de Equipe de Engenharia |  | Aprovadora |  |
| Daniel Solari | Coordenador de Desenvolvimento |  | Revisor |  |
