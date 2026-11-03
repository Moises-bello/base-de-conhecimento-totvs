---
content_hash: 7c411a25ee2d52288fa2ca018141e8bc6a785c3ca2c23f693d689309e12f441f
fetched_at: '2026-06-29T00:08:31.026863+00:00'
page_id: '272711630'
product: rm
source: tdn-rm
title: ER SAUHRM02-964 Cópia de valores de porte CBHPM Com acréscimo de valores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272711630
version: 2
---

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | GESTÃO HOSPITALAR - RM | Módulo | **CADASTROS** |
| Segmento Executor | Saúde |  |  |
| Projeto¹ | R\_SAU\_HRM1617 | IRM¹ | SAUHRM02-965 |
| Requisito¹ | SAUHRM02-964 | SubTarefa¹ | SAUHRM02-966 |
| Chamado² | ***186097, 188154*** |  |  |
| Release de Entrega Planejada | Não definido | Réplica | Não necessário |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

# \_Toc355276661\_Toc355276662Objetivo

\_Toc355276664Ao criar uma nova condição financeira com convênio o cliente poderá copiar dados de portes de CBHPM de outras fontes ao invés de digitar os mesmos.

# Definição da Regra de Negócio

* Será desenvolvido um **Processo** para possibilitar a cópia dos dados de Porte CBHPM.
  + As Oriegns da copia poderão ser;
    - Tabela geral de Portes CBHPM – Se esta opção for a escolhida o sistema irá buscar os dados da tabela de Portes CBHPM;

* + - Condição Financeira – Se esta opção for escolhida o cliente deverá informar de qual convênio, Unidade de faturamento e a Vigência da condição a qual os dados se encontram.

* % Acréscimo – Se o cliente informar este campo o sistema ao copiar a tabela de portes irá acrescer o valor calculado no valor do porte. Se este campo ficar em branco o sistema somente irá fazer a cópia, sem alterar os valores originais do porte copiado.

|  |  |  |  |
| --- | --- | --- | --- |
| Rotinas Envolvidas |  |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Condição Financeira com Convênio | Inclusão | Faturamento/Condição Financeira com Convênio/Anexos/Valores porte CBHPM |

# Escopo Negativo

# \_Toc355276665Protótipo de Tela

|  |  |
| --- | --- |
| \_Toc355276666**Regras da Interface** |  |
| **RI-001** | Tela 1 – Em condição financeira, Anexos, escolher Valores de Porte CBHPM.            Tela 2 – Nesta tela atualmente o sistema já permite a inclusão de valores para o porte.   Porém, será implementado a opção de cópia de portes já cadastrados em outros convênios ou de portes cadastrados na tabela de portes.   Na aba **Processos** será implementado a chamada da tela de cópia. |
| **RI-002** | Tela 3 – Nesta nova tela serão apresentados as seguintes opções;   * Origem dos dados a serem copiados;     + - Tabela geral de Portes CBHPM – Se esta opção for a escolhida o sistema irá buscar os dados da tabela de Portes CBHPM;     - Condição Financeira – Se esta opção for escolhida o cliente deverá informar de qual convênio, Unidade de faturamento e a Vigência da condição a qual os dados se encontram. * % Acréscimo – Se o cliente infor\_GoBackmar este campo o sistema ao copiar a tabela de portes irá acrescer o valor calculado no valor do porte.           Tela 4 – Resultado da cópia. O sistema facilitará o trabalho do cliente, fazendo a inserção dos portes para a nova condição financeira do convênio em questão. |

# \_Toc355276667Fluxo do Processo

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.
