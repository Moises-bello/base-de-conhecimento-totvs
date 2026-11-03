---
content_hash: a3dbb57396bb75033eb2341b18e51c035caabdce274ac4465ac5fded657b585a
fetched_at: '2026-06-29T00:06:14.583883+00:00'
page_id: '210047956'
product: rm
source: tdn-rm
title: DT_Formula_Situacao_Funcionario_Data
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Formula_Situacao_Funcionario_Data
version: 4
---

# FUNÇÃO DE FÓRMULA QUE RETORNA A SITUAÇÃO DO FUNCIONÁRIO EM UM DATA OBSERVANDO A SITUAÇÃO DO DIA

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Administração de Pessoal* | *-* | |
| **Versões/Release:** | **12.1.4** |

## Descrição

Uma nova fórmula chamada **“SFUNCDATA”**  possui o objetivo de **retornar** a situação do funcionário na data informada.

## Procedimento para Utilização

Para que o usuário tenha acesso a nova fórmula, siga o seguinte passo:

Acesse **RH / Folha de Pagamento / Administração de Pessoal / Fórmulas**

• Deve ser passado como parâmetro para a nova fórmula, a data em que desejada verificar a situação do funcionário.

**Possíveis retorno**

• “A” para funcionário **Ativo.**• “D” para funcionário **demitido.**• “F” para funcionário **em férias.**• Se a data informada for anterior à data de admissão do funcionário, **não irá retornar nada.**• Se o funcionário estiver afastado, o retorno será o **tipo de afastamento.**• Caso o funcionário possua histórico de situação, o retorno será a **situação encontrada na histórico.**
