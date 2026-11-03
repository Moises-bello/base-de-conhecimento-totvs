---
content_hash: 0984255ee5532a220fd9bf183c977d60d0b403c40a402982ca11af4c08f9b67c
fetched_at: '2026-06-29T00:06:12.929946+00:00'
page_id: '205921874'
product: rm
source: tdn-rm
title: TTL289_DT_Lancamento_Inscricao_Anonima_Valor_Diferente_AreaOfertada_ProcessoSeletivo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTL289_DT_Lancamento_Inscricao_Anonima_Valor_Diferente_AreaOfertada_ProcessoSeletivo
version: 1
---

# IMPORTAR INSCRIÇÕES ANÔNIMAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Importar inscrições anônimas* |
| **Situação/Requisito:** | *Ao gerar inscrições anônimas em um processo seletivo que tenha áreas ofertadas com valor de inscrição diferente do processo seletivo, o sistema gera o lançamento da inscrição com o valor do processo seletivo, sendo que é possível que a área ofertada tenha um valor diferente do processo seletivo.* |
| **Solução/Implementação:** | *No momento da importação das inscrições, o sistema não permite alterar o lançamento pois os boletos já estão gerados, como não é possível alterar o lançamento, foi adicionado um alerta no momento de gerar as inscrições, que caso existam áreas ofertadas com valor diferente do processo seletivo o sistema alerta para o usuário e pergunta se quer continuar ou não com o processo, caso opte por não prosseguir o processo é cancelado, caso queira avançar os lançamentos serão gerados com base no valor do processo seletivo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** | *12.1.8* |
| **Versão Expedida:** | *12.1.8* |

divs
