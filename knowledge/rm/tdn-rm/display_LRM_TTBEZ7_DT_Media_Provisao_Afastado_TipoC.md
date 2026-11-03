---
content_hash: 3a6eace865b64b4354fd086868e8b026eac34582f1864879d0a267b62339fb4d
fetched_at: '2026-06-29T00:06:04.700717+00:00'
page_id: '200910491'
product: rm
source: tdn-rm
title: TTBEZ7_DT_Media_Provisao_Afastado_TipoC
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBEZ7_DT_Media_Provisao_Afastado_TipoC
version: 2
---

# PROVISÃO AFASTADO TIPO C

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Provisão de Férias* |
| **Situação/Requisito:** | *Na geração do histórico de provisões não está calculando corretamente as médias de funcionário com afastamento do tipo C - "Contrato de Trabalho Suspenso", sem data de retorno.* |
| **Solução/Implementação:** | *Quando o funcionário está afastado pelo tipo C - "Contrato de Trabalho Suspenso", ocorre uma pausa na vigência do periodo aquisitivo.*  *Como o afastamento ainda não tem retorno, no cálculo da provisão é necessário fazer uma simulação da extensão do periodo aquisitivo.*  *O ajuste deverá ocorrer nesta simulação, que não estava apurando corretamente o periodo para o cálculo das médias.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTBEZ7* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
