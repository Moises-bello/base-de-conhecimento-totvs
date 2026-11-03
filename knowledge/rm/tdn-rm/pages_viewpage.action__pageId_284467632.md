---
content_hash: 8af3024cb6dffc7e20e6ac5c5de0263521a7972ff8a2791ee14fcaf7f638a46d
fetched_at: '2026-06-29T00:08:36.200541+00:00'
page_id: '284467632'
product: rm
source: tdn-rm
title: ER_SAUHRM02-1968 - Parametro de Impressão da  requisição direto na Farmacia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284467632
version: 1
---

|  |
| --- |
| \_GoBack**Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |

Nenhuma anotação efetuada a mão ou rasura no documento será considerada válida.

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| **Produto** | RM | **Módulo** | PRONTUARIIO ELETRONICO |
| **Segmento Executor** | Saúde |  |  |
| **Projeto¹** |  | **IRM¹** |  |
| **Requisito¹** | 1. SAU\_BACKLOG-1968 | **SubTarefa¹** |  |
| **Chamado²** |  |  |  |
| **Release de Entrega Planejada** |  | **Réplica** | Não necessário |
| **País** | **(**X **) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador**   **(  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_.** |  |  |
| **Outros** |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

Desabilitar o parâmetro Geral "Imprime requisição Direto na Farmácia ao concluir a prescrição" e vincular este parâmetro **por unidade de atendimento.**

# \_Toc355276664Definição da Regra de Negócio

**RN001 –** Criação de parâmetro "Imprime requisição Direto na Farmácia ao concluir a prescrição" no **cadastro de Unidade de atendimento (ver tela 1). Caminho:** Cadastros/ uso Geral/Unidade de Atendimento.

* **Desta forma o sistema passaria a controlar este parâmetro e não mais o parâmetro Geral.**

**RN002 –** Criar script para habilitar ou não o parâmetro da unidade de atendimento conforme a informação dos parâmetros Gerais;  
**Exemplo:** Se nos parâmetros gerais estiver marcado que "Imprime requisição Direto na Farmácia ao concluir a prescrição" todas unidades virão com esta marcação. Se alguma unidade não imprimir direto este deverá ser desmarcado manualmente após a execução do Script.
  
**RN003 –** Após criação do parâmetro por unidade de atendimento e execução do script, desabilitar está funcionalidade da tela de parâmetros gerais**. (Ver tela 2)**

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Cadastro | Inclusão | Cadastros/ uso Geral/Unidade de Atendimento |
|  |  |  |
|  |  |  |

# \_Toc355276665Protótipo de Tela

As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema, devem ser utilizadas apenas para exemplificar a forma de iteração que os usuários possuirão ao acessar o RM, o fluxo de negócio e a forma em que os dados e informações serão manipuladas.  
\_Toc355276666

|  |
| --- |
| **Protótipos** |
| Em unidades de atendimento na aba Parâmetros da Prescrição criar Parâmetro "Imprime requisição Direto na Farmácia ao concluir a prescrição".   **Tela 1** |

|  |  |  |
| --- | --- | --- |
|  | **Regras de Interface** |  |
| **RI001** | Se o parâmetro estiver desmarcado o sistema não imprimirá a requisição direto na Farmácia para a Unidade em questão. |  |
| Em unidades de atendimento na aba Parâmetros da Prescrição criar Parâmetro "Imprime requisição Direto na Farmácia ao concluir a prescrição".   **Tela 2** |  |
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
