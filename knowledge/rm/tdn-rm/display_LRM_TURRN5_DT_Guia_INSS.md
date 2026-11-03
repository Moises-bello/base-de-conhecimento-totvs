---
content_hash: 120861ec1e56f7f24493cae378b91124008038f9689eca37778ebe253907756f
fetched_at: '2026-06-29T00:08:07.604591+00:00'
page_id: '237382847'
product: rm
source: tdn-rm
title: TURRN5_DT_Guia_INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/TURRN5_DT_Guia_INSS
version: 114
---

# GUIA DE INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Guia de Inss* |
| **Situação/Requisito:** | Ao acessar a guia de INSS e ficar mexendo na tela, o sistema está desmarcando o parâmetro: Gerar lançamentos rateados por centro de custo da seção do funcionário.  Além disto, este parâmetro está com a nomenclatura e funcionalidade incorreta, o mesmo caso marcado deve seguir a mesma funcionalidade do parâmetro Gerar lançamentos rateados por centro de custo que aparece somente quando o parâmetro utiliza cálculo por centro de custo está marcado. |
| **Solução/Implementação:** | Otimizado lançamento financeiro, de forma que o sistema também preencha a capa do lançamento financeiro ao ser marcado o parâmetro " Gerar lançamentos rateados por centro de custo da seção do funcionário".  A tela de geração do lançamento financeiro da guia de inss também sofreu alterações para que o sistema não perca o valor escolhido pelo usuário do parâmetro citado.  Além destas mudanças foi corrigido a regra para que o parâmetro "Ratear lançamento por centro de custo" fique invisível caso o rateio por centro de custo, dentro do fluxus, estiver marcado como "obrigatório sempre" |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TURRN5 |
| **Requisito (ISSUE):** |  |

divs
