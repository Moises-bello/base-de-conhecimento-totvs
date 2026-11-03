---
article_id: 1500007196661
category: Manutenção de Ativos (SIGAMNT)
content_hash: 46285ea0e4082f18a286b852f85d2f2eb43b4b5e83be1d1b5473c608794af58c
fetched_at: '2026-06-28T22:42:34.110280+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Histórico de ordens de serviço
type: support-article
updated_at: '2021-07-05T21:01:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007196661-Manufatura-Linha-Protheus-MNT-Hist%C3%B3rico-de-ordens-de-servi%C3%A7o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:20 min**  
**Dúvida**Como enviar **O.S. - Ordens de serviço** para histórico?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT)  - Versão 12  
  
**Solução**A rotina **Acum. Histórico Manutenção - MNTA825** copia todas as **O.S.** que estejam **Terminadas** até a data de manutenção escolhida através do parâmetro em tela, copiando também todos os seus relacionamentos como insumos, etapas, ocorrências e motivos de atraso. Todas essas informações estarão registradas em histórico, fazendo com que as tabelas inerentes a **Ordem de Serviço** fiquem menos populosas e melhorando o desempenho do Sistema.   
  
A seguir são apresentadas as tabelas originais cujos registros são excluídos no processo, e as tabelas cópias, que tem os registros incluídos.

| Original | Cópia |
| --- | --- |
| **STA - Problemas com Ordens de Serviço)** | **STV - Histórico de Problemas** |
| **STJ - Ordens de Serviço** | **STS - Histórico de Manutenção** |
| **STL - Insumos da Ordem de Serviço** | **STT - Histórico de Detalhes da Manutenção** |
| **STN - Ocorrências Retorno Manutenção** | **STU - Histórico de Ocorrências** |
| **STQ - Etapas Executadas** | **STX - Histórico de Etapas Executadas** |
| **TPL - Motivos de Atraso da O.S.** | **TQ6 - Histórico Motivos Atraso O.S** |
| **TPQ - Opções Respostas das Etapas)** | **TPX - Histórico de Opções Respostas da O.S** |

**Importante**  
Para garantir a integridade dos dados, é feito uma checagem de compatibilidade entre as tabelas envolvidas para avaliar se todos os campos existentes nas tabelas padrões existam também nas tabelas de histórico, haja visto, que por característica do Sistema, é possível ao usuário incluir campos específicos. Se for encontrada alguma incompatibilidade, o Sistema exibe na tela a **Descrição do Problema da Estrutura**, sinalizando o campo e o problema identificado.
