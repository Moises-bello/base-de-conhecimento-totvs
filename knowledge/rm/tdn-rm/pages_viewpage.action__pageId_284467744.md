---
content_hash: 50dbe4423525692f89871900034752f8b432797693cfa2a0c433c0edd765c94f
fetched_at: '2026-06-29T00:08:36.213045+00:00'
page_id: '284467744'
product: rm
source: tdn-rm
title: ER_SAUHRM02-1966- Geracao de XML de contas de Internação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284467744
version: 1
---

|  |
| --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |

Nenhuma anotação efetuada a mão ou rasura no documento será considerada válida.

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| **Produto** | RM | **Módulo** | FATURAMENTO |
| **Segmento Executor** | Saúde |  |  |
| **Projeto¹** |  | **IRM¹** |  |
| **Requisito¹** | SAU\_BACKLOG-1966 | **SubTarefa¹** |  |
| **Chamado²** |  |  |  |
| **Release de Entrega Planejada** |  | **Réplica** | Não necessário |
| **País** | **(**X **) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador**   **(  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_.** |  |  |
| **Outros** |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

\_Toc355276664Possibilitar a escolha de número de Guias por arquivo XML até o limite de 100 que é o determinado pelas regras TISS
  
**RN001 –** Sistema deverá manter como default o número máximo de Guias por xml que é 100 porém o usuário poderá alterar para colocar uma fatura por XML.
  
**RN002** – Se a opção for de 1 Guia por arquivo XML o sistema deverá respeitar a regra de 1 arquivo uma fatura.  
Exemplo: Na hora de gerar os XML o sistema deverá quebrar quebrar por conta cada XML e cada XML conter um número de fatura diferente.
  
  
**RN003** – Esta opção será para atendimentos externos e Internos.  
**RN004 –** Respeitar o parâmetro informações especificas (Unimed Chapeco)  
Gerar xml para terceiro – Se tiver marcado (lembrando que é para honorários de terceiro).

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Faturamento | Inclusão | Faturamento / condições contratuais com convênios /Eletrônico III – TISS/Geral II |
|  |  |  |
|  |  |  |

# \_Toc355276665Protótipo de Tela

As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema, devem ser utilizadas apenas para exemplificar a forma de iteração que os usuários possuirão ao acessar o RM, o fluxo de negócio e a forma em que os dados e informações serão manipuladas.  
\_Toc355276666

|  |
| --- |
| **Protótipos** |
| Tela 1 – O default será sempre o quantidade determinada pela TISS. O cliente poderá optar por quantidades inferiores.   Esta será por tipo de atendimento.   Caminho: Faturamento / condições contratuais com convênios /Eletrônico III – TISS/Geral II |

|  |  |
| --- | --- |
|  | **Regras de Interface** |
|  |  |

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

\_GoBack
