---
content_hash: 35d424159b39255265915a4ff95d6a0d5b4d7ff071b5bdb0f38119de2f285ecd
fetched_at: '2026-06-29T00:08:36.223378+00:00'
page_id: '284468032'
product: rm
source: tdn-rm
title: ER_SAURMH02-1957 - Vinculo Produto  em Restricoes do contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAURMH02-1957+-+Vinculo+Produto++em+Restricoes+do+contrato
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
| **Requisito¹** | SAU\_BACKLOG-1957 | **SubTarefa¹** |  |
| **Chamado²** |  |  |  |
| **Release de Entrega Planejada** |  | **Réplica** | Não necessário |
| **País** | **(**X **) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador**   **(  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_.** |  |  |
| **Outros** |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

\_Toc355276664Em condições contratuais, para restringir um item o sistema deverá ter como base o Código do Produto (IDPRD) e não código(ESPECIFICO). Atualmente a referencia é o código especifico, isso faz com que haja um retrabalho nas restrições quando este código muda.

# Definição da Regra de Negócio

**RN001 –** Internamente o código base nas restrições de contrato deve fazer a referência ao código de produto(IDPRD) ver tela.  
**RN002 –** Na tela de restrições de contrato o campo "Faixa Final" será suprimido para Materiais e Medicamentos, visto que o IDPRD é um campo sequencial e poderá haver espaçamentos entre um restrito e outro.  
**RN003 –** Criação de script para o cliente poder fazer esta alteração em sua base atual.  
**RN004 –** Para novos códigos a inserção não poderá mais ser por faixa e sim código a código(IDPRD).  
**RN005 –** Verificar em outros pontos do sistema onde estas alterações terão reflexo.

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Faturamento | Alteração | Condições Contratuais>anexos>restrições do contrato |
|  |  |  |
|  |  |  |

# \_Toc355276665Protótipo de Tela

As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema, devem ser utilizadas apenas para exemplificar a forma de iteração que os usuários possuirão ao acessar o RM\_GoBack, o fluxo de negócio e a forma em que os dados e informações serão manipuladas.  
\_Toc355276666

|  |
| --- |
| **Protótipos** |
| Internamente no sistema deixar como código principal o IDPRD.   Não haverá necessidade de alteração na tela. |

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
