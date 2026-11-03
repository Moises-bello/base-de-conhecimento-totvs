---
content_hash: 477de1004f7469af2d3a27bacd8a4796478dcbbdf4636da8ff33f064f5b88302
fetched_at: '2026-06-29T00:06:03.271634+00:00'
page_id: '198952601'
product: rm
source: tdn-rm
title: TSZGVL_DT_Avisos_Automaticos
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZGVL_DT_Avisos_Automaticos
version: 2
---

# AVISOS AUTOMÁTICOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Totvs Folha de Pagamento* |
| **Função:** | *Avisos Automáticos* |
| **Situação/Requisito:** | *Ao criar um aviso automático agrupando por Chefes e clicar em "Enviar Mensagem" ocorre erro de número de parâmetros divergente na sentença sql* |
| **Solução/Implementação:** | *Ajustes em número de parâmetros de sentença SQL. Sentença esperava 5 parâmetros e eram passados 8 parâmetros.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSZGVL* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
