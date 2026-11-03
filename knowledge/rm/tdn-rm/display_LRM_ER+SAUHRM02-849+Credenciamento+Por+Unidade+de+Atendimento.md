---
content_hash: 86a17d62864645e4646346979c73c2a8d56cb50efc19b12d90460650d68b09db
fetched_at: '2026-06-29T00:08:30.197560+00:00'
page_id: '272411458'
product: rm
source: tdn-rm
title: ER SAUHRM02-849 Credenciamento Por Unidade de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+SAUHRM02-849+Credenciamento+Por+Unidade+de+Atendimento
version: 2
---

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | TOTVS Gestão Hospitalar | Módulo | Cadastro |
| Segmento Executor | Saúde |  |  |
| Projeto¹ | SAUHRM02 | IRM¹ | SAUHRM02-848 |
| Requisito¹ | SAUHRM02-849 | SubTarefa¹ | SAUHRM02-887 |
| Chamado² | 372813 |  |  |
| Release de Entrega Planejada | Não definido | Réplica | Não necessário |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

Possibilitar o credenciamento de médicos por unidade de atendimento.

# \_Toc355276664Definição da Regra de Negócio

**RN001** – **CADASTROS/PRESTADOR** –Permitir que o usuário escolha **a unidade, vigência** e **tipo de credenciamento**   
 no momento do cadastramento/Alteração do prestado(Tela 1).

* Em cadastros/Prestador escolher um prestador ou cadastrar um novo.
  + Ir na aba "Anexos" e escolher o menu "Credenciamento"
    - Em credenciamento escolher novamente a aba "Anexos" (telas 2) e escolher as unidades para credenciamento e a vigência deste credenciamento(Tela 3);

**RN002** – No sistema RM serão verificado os impactos e adequações em todos os processos que requeiram o credenciamento do profissional por unidade de atendimento. Exemplo: Adequação na geração de XML, no encerramento da conta e demais processos internos do sistema.

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Cadastros | Inclusão/alteração | Cadastros/Prestador. |
| Faturamento | Geração XML | Faturamento para convênios |
| Faturamento | Encerramento parcial | Faturamento particular /convênios |
| Faturamento | Resumo da conta | Elaboração de Contas |
| Faturamento SUS | Geração do arquivo | Faturamento SUS |
| Guias TISS | Geração das Guias TISS | Imprimir Extrato / Conta |
| Médico Responsável | Credenciamento | Registro de Atendimento |

# Escopo Negativo

* Esta implementação será por unidade de atendimento. Independente da especialidade médica.  
   \_GoBack  

  # \_Toc355276665Protótipo de Tela

  |  |  |
  | --- | --- |
  | \_Toc355276666**Regras da Interface** |  |
  | **RI-001** | Tela 1 – Escolher a opção credenciamento. |
  | **RI-002** | Tela 2 – Na tela de Credenciamento escolher novamente o botão "Anexos"      Tela 2.1 – Escolher a opção Credenciamento por Unidade de Atendimento. |
  | **RI-003** | Tela 3 – Permitir o cadastro de várias Unidades de atendimentos vinculadas ao credenciamento do prestador com data de vigência associada. |
  | **RI-004** |  |
  | **RI-005** |  |

  # \_Toc355276667Fluxo do Processo

    

  # Dicionário de Dados

  Não necessário para o desenvolvimento deste requisito.   

  # Grupo de Perguntas

  Não necessário para o desenvolvimento deste requisito.

  # **Consulta Padrão**

  Não necessário para o desenvolvimento deste requisito.

  # Estrutura de Menu

  Não necessário para o desenvolvimento deste requisito.
