---
content_hash: 80a771ea179b5260b477ca6e90dec80979795e14d1fb78626f76310142f33741
fetched_at: '2026-06-29T00:08:40.002726+00:00'
page_id: '286196871'
product: rm
source: tdn-rm
title: 1046294 MSAU-11691 DT Listar Somente Cuidados Prescritos no PEP do RM
type: documentation
url: https://tdn.totvs.com/display/LRM/1046294+MSAU-11691+DT+Listar+Somente+Cuidados+Prescritos+no+PEP+do+RM
version: 109
---

# Listar Somente Cuidados Prescritos no PEP do RM

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | PEP - Enfermagem | | PEP - Cuidados | |
| **Parâmetro(s):** | Exibe todos os cuidados caso não tenha prescrição de enfermagem criada. |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Adicionado o parâmetro "Exibe todos os cuidados caso não tenha prescrição de enfermagem criada", que ao desmarca-lo não será mais exibido todos os cuidados nas prescrições de Enfermagem do PEP do RM.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.14 deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **TOTVS Gestão Hospitalar(RM Saúde)**, acesse **Opções/Parâmetros/Parâmetros Gerais**. Configure o parâmetro a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Prontuário Eletrônico / Prescrição |
| **Nome:** | Exibe todos os cuidados caso não tenha prescrição de enfermagem criada |
| **Tipo:** | Checkbox |
| **Cont. Por.:** | Marcado |
| **Descrição:** | Exibe todos os cuidados caso não tenha prescrição de enfermagem criada |

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (RM Saúde), acesse o PEP do RM.

                      O sistema apresentará a janela do PEP, selecione um paciente.

       2.            Acesse a aba de Enfermagem.

       3.            Na aba de cuidados, se não possuir prescrição de enfermagem criada, e o parâmetro "Exibe todos os cuidados caso não tenha prescrição de enfermagem criada" desmarcado, o sistema não vai exibir todos os cuidados cadastrados no sistema.

divs
