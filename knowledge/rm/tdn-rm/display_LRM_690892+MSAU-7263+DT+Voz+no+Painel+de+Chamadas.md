---
content_hash: 443326d21646f8cdfeb103b4282f50eb14f370e7e0e184613753d78d42e76e45
fetched_at: '2026-06-29T00:08:37.153956+00:00'
page_id: '284877003'
product: rm
source: tdn-rm
title: 690892 MSAU-7263 DT Voz no Painel de Chamadas
type: documentation
url: https://tdn.totvs.com/display/LRM/690892+MSAU-7263+DT+Voz+no+Painel+de+Chamadas
version: 106
---

# Voz no Painel de Chamadas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Painel de Chamadas | | Painel de Classificação de Risco | | Painel de Atendimentos Eletivos | |
| **Parâmetro(s):** | Habilita Voz no Painel de Chamadas |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada melhoria no Painel de Chamadas que possibilita que ao chamar uma senha no Painel de Classificação de Risco ou eletivos, a senha seja chamada por uma voz ao invés do tradicional bipe.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **TOTVS Gestão Hospitalar (RM Saúde)**, acesse **Opções/Parâmetros/Parâmetros Gerais**. Na aba classificação de risco crie/configure o parâmetro a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Habilita Voz no Painel de Chamadas |
| **Tipo:** | Checkbox |
| **Cont. Por.:** | Desmarcado (Bipe tradicional) |
| **Descrição:** | Ao marcar o parâmetro a senha será chamada pela voz do painel onde será dito por extenso o valor da senha. |

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (RM Saúde), acesse o Atendimento > Pronto Atendimento / Ambulatório > Toten de Pronto Atendimento .

Chamar uma senha para classificação de risco ou Painel de Atendimentos Eletivos.

       2.            Acesse a Classificação de Risco ou o Painel de Eletivos e Chame uma senha.

       3.            No painel de chamadas se o parâmetro estiver marcado ao chamar a senha a mesma será dita por extenso indicando o local da chamada e a senha que foi chamada.

       4.           Até o momento é possível chamar no máximo 999 senhas com essa funcionalidade.

divs
