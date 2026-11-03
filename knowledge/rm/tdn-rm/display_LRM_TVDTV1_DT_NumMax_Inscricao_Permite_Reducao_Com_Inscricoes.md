---
content_hash: c7ccee9e8a5639511c0083ae697d948a0199d30f8c2b40bbf4a2ab4dfee41d09
fetched_at: '2026-06-29T00:08:12.269983+00:00'
page_id: '243642178'
product: rm
source: tdn-rm
title: TVDTV1_DT_NumMax_Inscricao_Permite_Reducao_Com_Inscricoes
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDTV1_DT_NumMax_Inscricao_Permite_Reducao_Com_Inscricoes
version: 117
---

# PROCESSO SELETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Processo seletivo - número máximo de inscrições por candidato* |
| **Situação/Requisito:** | *Quando o processo seletivo possui datas de períodos preenchidas, o campo que limita o número máximo de inscrições por cliente fica desabilitado, porém se o processo seletivo não tiver datas preenchidas, o campo fica habilitado permitindo sua alteração em qualquer momento, esta alteração em qualquer momento ocorre sem nenhuma validação, ou seja, se o número máximo de inscrições for 3 e já existir uma pessoa com 3 inscrições, o sistema permite reduzir sem validar.* |
| **Solução/Implementação:** | *Foi feito uma alteração no campo para que sempre fique habilitado, exceto quando o processo seletivo estiver desativado, também foi feito uma alteração para que seja identificado alterações no valor do número máximo de inscrições, se este for maior que o valor atual o sistema permitirá a alteração, se for  menor, irá verificar a quantidade de inscrições por pessoa que já existe, se o valor alterado for menor que o número atual de inscrições por pessoa, o sistema irá emitir um alerta não concluindo a operação, sendo assim necessário excluir a inscrição que excede o limite definido pelo usuário do sistema.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
