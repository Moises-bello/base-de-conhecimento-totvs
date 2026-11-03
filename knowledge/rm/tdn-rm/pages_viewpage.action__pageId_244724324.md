---
content_hash: 75b85897bf4d587701b1f525a0b07d00eb23ba7f6a04a4c9f9fb816abc9ef327
fetched_at: '2026-06-29T00:08:14.999032+00:00'
page_id: '244724324'
product: rm
source: tdn-rm
title: ER_SAUHRM01-288_Período de Retorno Consultas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244724324
version: 3
---

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | TOTVS GESTÃO HOSPITALAR - RM | Módulo | FATURAMENTO |
| Segmento Executor | Saúde |  |  |
| Projeto¹ | R\_SAU\_RM\_V12\_1516 | IRM¹ |  |
| Requisito¹ |  | SubTarefa¹ |  |
| Chamado² |  |  |  |
| Release de Entrega Planejada | Não definido | Réplica | Não necessário |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

Possibilitar a parametrização de dias de retorno de consulta por unidade de atendimento.  
 Para tanto, a solicitação é que se inclua a unidade de atendimento na tela de "Retorno de Consulta".

# \_Toc355276664Definição da Regra de Negócio

**RN001** – Em cadastros/Faturamento/Condições contratuais com convênios na tela de Reotorno de consulta incluir o campo onde será informado a unidade de atendimento.  
 Premissas:   
 **A****)** Permitir o cadastro do campo "RETORNO EM DIAS" sem a necessidade de informação da Unidade de Atendimento.

* Esta parametrização aplicará os dias de retorno para todas as Unidades(Função já existente no sistema)

**B**)Para as unidades que forem cadastradas neste parâmetro, o sistema aplicará os dias informados para mesmas.  
 As que não estiverem cadastradas o sistema buscará as informações contidas na premissa **A****.**

* Esta parametrização permitirá que mais de uma unidade possa ter sua própria negociação em dias para retorno da consulta.

\_GoBack

|  |  |  |  |
| --- | --- | --- | --- |
| Rotinas Envolvidas |  |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Cadastros | Alteração | cadastros/Faturamento/Condições contratuais com convênios em Anexos/Retorno de consulta |
|  |  |  |

# Escopo Negativo

Não se aplica

# \_Toc355276665Protótipo de Tela

|  |  |
| --- | --- |
| \_Toc355276666**Regras da Interface** |  |
| **RI-001** | Incluir o campo Unidade de Atendimento.   Com esta informação preenchida, o sistema deve respeitar o parâmetro de retorno em dias para a unidade em questão. |
|  |  |

# \_Toc355276667Fluxo do Processo

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.
