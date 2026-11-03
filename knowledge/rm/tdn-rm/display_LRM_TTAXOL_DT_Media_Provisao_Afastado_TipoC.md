---
content_hash: 4db7298d7c8e0d6da595209cf8a11e822701abc08f0a9b9608bee674b61349bc
fetched_at: '2026-06-29T00:06:04.684023+00:00'
page_id: '200910330'
product: rm
source: tdn-rm
title: TTAXOL_DT_Media_Provisao_Afastado_TipoC
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAXOL_DT_Media_Provisao_Afastado_TipoC
version: 1
---

# PROVISÃO AFASTADO TIPO C

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Provisão de Férias* |
| **Situação/Requisito:** | *Na geração do histórico de provisões não está calculando corretamente as médias de funcionário com afastamento do tipo C - "Contrato de Trabalho Suspenso", sem data de retorno.* |
| **Solução/Implementação:** | *Quando o funcionário está afastado pelo tipo C - "Contrato de Trabalho Suspenso", ocorre uma pausa na vigência do periodo aquisitivo.*  *Como o afastamento ainda não tem retorno, no cálculo da provisão é necessário fazer uma simulação da extensão do periodo aquisitivo.*  *O ajuste deverá ocorrer nesta simulação, que não estava apurando corretamente o periodo para o cálculo das médias.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTAXOL* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.83.55* |
