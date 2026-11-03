---
content_hash: 54dea5ff6cdf76f096bc9719f48d53d760a3882331adcd10214a6e194051e7e1
fetched_at: '2026-06-29T00:06:14.565872+00:00'
page_id: '210047837'
product: rm
source: tdn-rm
title: TTLTZS_DT_Data_Sistema_Geração_Movimento_Por_Boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210047837
version: 1
---

# DATA DE EMISSÃO ATUAL NA GERAÇÃO DE MOVIMENTO POR BOLETO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de movimento por boleto* | *Geração de movimento* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Geração de movimento* | *Geração de movimento* | |
| **Cadastros Iniciais:** | *N/A.* |
| **Parâmetro(s):** | *N/A .* |
| **Ponto de Entrada:** | *N/A.* |
| **Chamados relacionados** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *Todos.* |
| **Tabelas utilizadas:** | *N/A* |
| **Sistema(s) operacional(is):** | *Todos.* |
| **Versões/Release:** | *12.1.9* |

## Descrição

Foi realizada otimização do processo de geração de movimento por boleto de forma a permitir que o processo de geração de movimento possa gerar movimentos com a data de emissão igual a data da geração do movimento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da release *12.1.8* deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Processo de geração de movimento**, avance para o segundo passo e configure o(s) parâmetro(s) a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Histórico:** | *Data de emissão do movimento* |
| **Tipo:** | *RadioGroup .* |
| **Cont. Por.:** | *Falso* |
| **Descrição:** | *Data que será utilizada para a data de emissão do movimento.* |

## Procedimento para Utilização

**Exemplo:**

com o sistema devidamente parametrizado, basta gerar movimento para um determinado boleto, escolhendo, no segundo passo do processo de geração de movimento, a opção "Data atual do sistema" para a parametrização de data de emissão do movimento. O movimento deverá, portanto, ter a data de emissão igual a data em que foi gerado o movimento.
