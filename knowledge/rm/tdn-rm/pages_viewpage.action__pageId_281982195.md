---
content_hash: 87f4c325678da340d57820a4fa27ec048f98f9edba18d2b1ffbe5d62a6d9f2e2
fetched_at: '2026-06-29T00:08:35.563773+00:00'
page_id: '281982195'
product: rm
source: tdn-rm
title: DT Filtrar Especialidades do Plantão no Registro de Atendimento pelo Médico
  Responsável
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=281982195
version: 109
---

# Filtrar Especialidades do Plantão no Registro de Atendimento pelo Médico Responsável

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Atendimento | |
| **Cadastros Iniciais:** | Painel de Classificação de Risco com Plantão Configurados |
| **Parâmetro(s):** | Filtra especialidades do plantão no registro de atendimento  Filtra especialidades do médico responsável no registro de atendimento |
| **Ponto de Entrada:** | Painel de Classificação de Risco |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Tabelas Utilizadas:** | SZPLANTAODETALHES, SZPLANTAO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Adicionado no sistema a opção de filtrar, no registro de atendimento, somente as especialidades informadas no plantão da classificação de risco do médico responsável.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **TOTVS Gestão Hospitalar (RM Saúde)**, acesse **Opções/Parâmetros/Parâmetros Gerais**. Na aba Classificação de risco configure o parâmetro a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Filtra especialidades do médico responsável no registro de atendimento |
| **Tipo:** | Checkbox |
| **Cont. Por.:** | Desmarcado |
| **Descrição:** | Filtra especialidades do médico responsável no registro de atendimento, parâmetro só é habilitado quando o parâmetro Filtra especialidades do plantão no registro de atendimento estiver marcado. |

Procedimento para Utilização

       1.            No TOTVS Gestão Hospitalar (RM Saúde), acesse Classificação de Risco / Plantão / Adicione o médico e as especialidades do médico e as da unidade de atendimento.

       2.            Acesse o Toten e chame uma nova senha para cair no painel de classificação de risco.

       3.            Ao chamar a senha na classificação e registrar o atendimento do paciente, informe o médico responsável o mesmo do plantão na classificação de risco.

       4.            No componente das especialidades da tela serão listadas somente as especialidades cadastradas para o médico no plantão e na configuração do plantão da unidade.

divs
