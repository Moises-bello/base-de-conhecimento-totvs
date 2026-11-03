---
content_hash: ba14aaa77cee397ead1f4ed43c3a09a5953f7178d6687ac425b1144c3fdce40b
fetched_at: '2026-06-29T00:08:08.258278+00:00'
page_id: '238029343'
product: rm
source: tdn-rm
title: TUQBTD_DT_PARAMETRIZACAO_PIS_PASEP_SPED_FOLHA_REGISTRO_M350
type: documentation
url: https://tdn.totvs.com/display/LRM/TUQBTD_DT_PARAMETRIZACAO_PIS_PASEP_SPED_FOLHA_REGISTRO_M350
version: 112
---

# PIS/PASEP para SPED Folha Registro M350

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Construção e Projetos** |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Obtenção dos valores para os campos "Total da Folha de Salários" e "Total das Exclusões à Base de Cálculo" referente ao Registro M350 do SPED Folha* |
| **Situação/Requisito:** | *Reestruturar a parametrização para o calculo e obtenção dos campos *"Total da Folha de Salários" e "Total das Exclusões à Base de Cálculo" referente ao Registro M350 do SPED Folha** |
| **Solução/Implementação:** | Foi criado os campos "PIS" e "Estorna PIS" no cadastro de evento para informar se o valor do evento constante no envelope de pagamento para uma determinada competência irá compor os campos "Total da Folha de Salários" ou "Total das Exclusões à Base de Cálculo" do registro M350 para o PIS SPED Folha.  O Conversor de Dados além de criar os campos  "PIS SPED Folha" e "Estorna PIS SPED Folha" os configura automaticamente conforme regra a antiga regra, a saber: Marca o campo "PIS SPED Folha" para todos os proventos; Marca o campo  "Estorna PIS SPED Folha" para todos os eventos cadastrado no cadastro do parâmetro  "Eventos para Exclusões à Base de Cálculo PIS/PASEP". |
| **Conversores e Parâmetros:** | *Informe os conversores/parâmetros.* |
| **Chamados relacionados:** | TUQBTD |
| **Requisito (ISSUE):** |  |

divs
