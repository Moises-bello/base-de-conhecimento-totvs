---
content_hash: f6c35b639a12622421eab0e676a90b6c6e7128ba3e8d5429bcb6993184b71d8c
fetched_at: '2026-06-29T00:06:18.406621+00:00'
page_id: '215484763'
product: rm
source: tdn-rm
title: ER_PCREQ-8592_Periodo_letivo_encerrado_geracao_lancamento
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8592_Periodo_letivo_encerrado_geracao_lancamento
version: 2
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | [R\_EDU\_EDU015](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_EDU_EDU015) | **IRM1** | [PCREQ-8592](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-8592) |
| **Requisito1** | [PCREQ-8593](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-8593) | **Subtarefa1** | [PDR\_EDU\_EDU015-17](http://jira.totvs.com.br/browse/PDR_EDU_EDU015-17) |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Explicar a necessidade dos clientes e detalhar o comportamento do TOTVS Educacional com o novo parâmetro do cadastro do período letivo para a geração de lançamentos.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Geração de Lançamentos | Alteração | Financeiro/Contábil > Geração > Financeiro | - |
| Geração de Lançamentos | Alteração | Contrato > Parcela > Geração de lançamento | - |
| Parâmetros Educacionais por Perfil | Alteração | Perfil de Usuário (Globais) > anexo Parâmetros educacionais | - |
| Cadastro de Período Letivo | Alteração | Menu Currículo e Oferta > Período Letivo |  |

**Período Letivo encerrado para geração de lançamentos**

Surgiu a necessidade dos clientes do TOTVS Educacional realizarem a geração de lançamentos para contratos de períodos letivos já encerrados, seja por inadimplência dos alunos ou outro motivo.

Para atender esta demanda, será adicionado mais um campo ao cadastro de período letivo, de nome “Período letivo encerrado para geração de lançamentos”.

Este novo campo, terá impacto somente em rotinas financeiras (Geração de Lançamento em massa e geração de lançamento por parcela).

**Detalhamento das alterações**

1. Será criado o parâmetro “Período letivo encerrado para geração de lançamentos” no cadastro do Período letivo. Quando o parâmetro estiver **habilitado,** não será possível gerar lançamentos financeiro para parcelas de contratos vinculados ao período letivo que teve o parâmetro habilitado. Em algumas funcionalidades o mesmo não estará disponível para seleção.  
   Quando o parâmetro estiver **desabilitado**, será possível gerar lançamentos financeiro para parcelas de contratos vinculados ao período letivo que está com o parâmetro desabilitado.

   Observações:

   * O parâmetro “Período letivo encerrado” não será mais responsável por validar a permissão/bloqueio da geração de lançamentos financeiro, essa funcionalidade sai do seu conjunto de validações e passa a ser do parâmetro “Período letivo encerrado para geração de lançamentos”.
   * O nome “Período encerrado para pagamento” será alterado para “Período letivo encerrado para pagamento de professores”, para instruir melhor ao usuário o comportamento do sistema.
   * Todas as outras validações que o parâmetro “Período letivo encerrado” trata quando está habilitado continuarão sendo tratadas.
2. Será criado o parâmetro “Permitir gerar lançamentos para períodos letivos encerrados para geração financeira” no cadastro de parâmetros educacionais do perfil de usuário.  
   Esse parâmetro, quando habilitado, permitirá usuários vinculados ao perfil gerar lançamentos financeiros para períodos letivos encerrados para geração financeira.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
