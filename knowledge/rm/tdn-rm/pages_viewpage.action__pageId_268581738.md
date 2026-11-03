---
content_hash: 9739fb89c18ac48878e458c923b7177c971877be0b5eb9a529230370e9ed4e83
fetched_at: '2026-06-29T00:08:20.634421+00:00'
page_id: '268581738'
product: rm
source: tdn-rm
title: ER_SAURM02-72 - Reclassificação da senha de atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268581738
version: 2
---

|  |
| --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | Gestão Hospitalar - RM | Módulo | Classificação de risco |
| Segmento Executor | Saúde |  |  |
| Projeto¹ | R\_SAU\_HRM1617 | IRM¹ | SAURM02-72 |
| Requisito¹ | SAURM02-73 | SubTarefa¹ | SAURM02-120 |
| Chamado² |  |  |  |
| Release de Entrega Planejada |  | Réplica |  |
| País | (x  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

Permitir a alteração do tipo de senha pela Recepção após escolha da mesma no Toten de Atendimento – NORMAL ou PRIORITÁRIO.

# \_Toc355276664Definição da Regra de Negócio

**RN001** – Atualmente o sistema não dispõe de processo de alteração de tipo de prioridade após a emissão da mesma.  
 O Sistema deverá permitir que o usuário da recepção possa fazer este tipo de alteração quando uma senha for impressa erroneamente.  
 Criar um menu suspenso que permita marcar a senha como prioritário ou desmarcar a senha tirando a mesma de situação de prioritária.  
 Ver exemplo na telas 1 .

# Fora do Escopo

N/A

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Atendimento | Alteração | Painel de Classificação de Risco/Registro de Atendimento |

\_Toc355276665

# Protótipo de Tela

\_Toc355276666

|  |  |
| --- | --- |
| **Regras da Interface** |  |
|  |  |
|  |  |
| **RI-001** | Tela 1 – Neste exemplo podemos observar que a aba Prioritário esta marcado.   O Sistema deve permitir a retirada da situação prioritário ou incluir a situação prioritário.\_GoBack |
|  |  |

# \_Toc355276667Fluxo do Processo

* Não necessário para o desenvolvimento deste requisito

# Dicionário de Dados

* Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

* Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

* Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

* Não necessário para o desenvolvimento deste requisito.
