---
content_hash: 6ba62d6a371d9b466c79ee080921b21ca766951875daa0abed6b8e5410008605
fetched_at: '2026-06-29T00:08:26.623140+00:00'
page_id: '271185560'
product: rm
source: tdn-rm
title: Cadastro Tipo de Títulos (Protheus) / Tipo de Documento (RM) - (Integração
  RM TCGI x Backoffice Protheus - EAI2)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271185560
version: 117
---

# Integração - Alinhamento do tipo de documento RM com o tipo de título do Protheus.

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Totvs Incorporação* |
| **Função:** | *Geração de lançamentos financeiros* |
| **Situação/Requisito:** | *Cliente necessita que seja disponibilizado a utilização de todos os tipos de títulos que são possíveis de utilização no Protheus no momento da geração de títulos quando gerados pelo TIN, até o momento somente era possível a geração de títulos do tipo NF ou PR quando integrado com backoffice Protheus.* |
| **Solução/Implementação:** | * Será efetuado a criação de parâmetro (USESDOCUMENTTYPE) da integração para determinar se irá utilizar o código do tipo de documento do lançamento gerado no RM pelo TIN para enviar ao Protheus ou se utiliza o parâmetro já existente (GERARTITULONF). O novo parâmetro terá como default será criado desabilitado para manter o padrão de utilização do parâmetro já existente e não obrigar o usuário a cadastrar os tipos idênticos * Caso o usuário opte por utilizar o tipo de documento para o tipo de título que será enviado ao Protheus, deverá ser cadastrado no RM os tipos de documentos alinhados com a documentação dos tipos de títulos que podem ser gerados no Protheus, se for cadastrado um novo tipo de título, este deverá também ser cadastrado no RM para o tipo de documento. * Quando o usuário utilizar um tipo de documento cadastrado no RM que não exista no Protheus o mesmo irá subir exceção informando que tipo de título não existe. * Os tipos de títulos default existentes no protheus segue no link: [Tipos de títulos protheus](https://www.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/fina015_tabela_de_tipos_de_titulos.htm) |
| **Conversores e Parâmetros:** | *12.1.14* |
| **Tickets relacionados:** | *MCP-75* |
| **Requisito (informe o requisito relacionado):** |  |

divs
