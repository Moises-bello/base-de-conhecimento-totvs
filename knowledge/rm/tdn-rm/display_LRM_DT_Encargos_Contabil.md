---
content_hash: d201fbdbe84ba779419d9b065f47b78d4154102a0306edaee39900aeb5788c7d
fetched_at: '2026-06-29T00:06:25.061016+00:00'
page_id: '224129924'
product: rm
source: tdn-rm
title: DT_Encargos_Contabil
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Encargos_Contabil
version: 1
---

# Geração de Encargos/Provisões na Contabilização

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Contabilização* | *Contabilização de Encargos* | |
| **Versão/Release:** | *12.1.4* |

## Descrição

Foi implementado no processo de contabilização uma opção para geração automática dos Encargos e Histórico de Provisões antes da execução da contabilização.

## Procedimento para Utilização

Foi criando um novo passo no Wizard do processo de Geração de Lançamentos Contábeis para parametrizar a Geração de Encargos e Histórico de Provisões. **Este novo passo fica disponível apenas quando a contabilização for executada para a competência atual e o parâmetro “Contabilizar Encargos” estiver marcado**. Ao executar o processo, o sistema primeiramente irá executar o processo de Geração de Histórico de Provisões, em seguida o processo de Geração de Encargos e depois a Contabilização. Em caso de erros na Geração do Histórico de Provisões e/ou Encargos, o sistema verifica se o parâmetro “Prosseguir com a contabilização em caso de erros na geração” está marcado. Se estiver marcado o sistema irá prosseguir com o processo de Contabilização, caso contrário o processo será abortado. No final da execução é exibido além dos log’s do processo de contabilização, os mesmos log’s que são exibidos no processo de Geração de Encargos e Histórico de Provisões. Para identificá-los será acrescentado na frente do nome do log os prefixos “\_Encargos” e “\_Provisões”.
