---
content_hash: db5a11d7e77101ea00a750de4c485736b8f51bf7c489c74910298daf8971b006
fetched_at: '2026-06-29T00:08:16.566075+00:00'
page_id: '248578966'
product: rm
source: tdn-rm
title: ER_SAUHRM01-565_Entrega de resultados de exames_novo_status
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM01-565_Entrega+de+resultados+de+exames_novo_status
version: 2
---

|  |  |  |  |
| --- | --- | --- | --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |  |  |  |
| Especificação |  |  |  |
| Produto | GESTÃO HOSPITALAR - RM | Módulo | CONTROLE DE PEDIDOS DE EXAMES/CONTROLE DE DOCUMENTOS |
| Segmento Executor | Saúde |  |  |
| Projeto¹ | R\_SAU\_HRM1516 | IRM¹ |  |
| Requisito¹ | SAUHRM01-36 | SubTarefa¹ | SAUHRM01-689 |
| Chamado² | **TTJMYC** |  |  |
| Release de Entrega Planejada | Não definido | Réplica | Não necessário |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

# \_Toc355276661\_Toc355276662Objetivo

Criação de um status que indique que o exame está "Ok" para a área que irá fazer a entrega do mesmo. Para tanto será criado um parâmetro que permitirá o fluxo do sistema com este novo status.

# \_Toc355276664Definição da Regra de Negócio

**RN001** – Criação de Parâmetros para habilitar o novo status de "Liberado Recepção". São eles;

* Utiliza status Liberado Recepção" estiver com a opção "Antes da impressão do Resultado"
* Utiliza status Liberado Recepção" estiver com a opção "Depois da impressão do Resultado"
* Utiliza status Liberado Recepção" estiver com a opção "Não"

**RN002** – Se o parâmetro "Utiliza status Liberado Recepção" estiver com a opção "Antes da impressão do Resultado" marcado após status de liberado = "L" o sistema habilitará o Status "O" = "Liberado Recepção" Assim, a recepção terá o controle da Impressão do exame.  
 Poderá haver a reversão deste status. Neste Caso o sistema retornará o laudo para correção e o fluxo do sistema será retomado a partir deste status.   
 **RN003** – Se o parâmetro "Utiliza status Liberado Recepção" estiver com a opção "Depois da impressão do Resultado" marcado após status de liberado = "E" o sistema habilitará o Status "O" = "Liberado Recepção" Assim, o resultado será impresso no setor de exames.  
 Poderá haver a reversão deste status. Neste Caso o sistema retornará o laudo para correção e o fluxo do sistema será retomado a partir deste status.   
   
 **RN004** – Se o parâmetro "Utiliza status Liberado Recepção" estiver com a opção "Não" marcado o sistema seguirá o fluxo atual, não habilitando o status "O".

|  |  |  |  |
| --- | --- | --- | --- |
| Rotinas Envolvidas |  |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Preenchimento de Resultado | Alteração | Controle de pedidos de Exames/Preenchimento de resultados |
| Parâmetros Gerais | Inclusão | Opções\Parâmetros\Parâmetros Gerais\Unidade Diagnostico II |

# Escopo Negativo

# \_Toc355276665Protótipo de Tela

|  |  |
| --- | --- |
| \_Toc355276666**Regras da Interface** |  |
|  |  |
| **RI-001** | Tela 1 – Tela de Parâmetros com as opções para utilização ou não do novo status.   Caminho: Opções\Parâmetros\Parâmetros Gerais\Unidade Diagnostico II |
| **RI-002** | Tela 2 – Controle de Pedidos de Exames com o parâmetro "Utiliza status Liberado Recepção" estiver com a opção "Antes da impressão do Resultado" marcado.        O sistema Após status "L" apresentará o novo processo "Liberado Recepção" Status = "O".        Antes da Impressão o sistema Mostrará o Status "O" = Liberado para Recepção        Na recepção o cliente poderá imprimir o Resultado ou Retorna-lo para correção. |
| **RI-003** | Tela 3 – Controle de Pedidos de Exames com o parâmetro "Utiliza status Liberado Recepção" estiver com a opção "Depois da impressão do Resultado" marcado.                           Após impressão do resultado o sistema Mostrará Status "E"        Após impressão o cliente fará a alteração do Status para "O" = Liberado Recepção.      Neste ponto a recepção poderá fazer um filtro por este status e dar continuidade no fluxo normal do sistema.\_GoBack |

# \_Toc355276667Fluxo do Processo

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.
