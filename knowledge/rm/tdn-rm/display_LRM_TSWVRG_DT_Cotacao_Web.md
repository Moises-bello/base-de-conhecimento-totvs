---
content_hash: 118230e51cd8f446588a840a77d28642d63ad5c10fcc95d91ff613a91d193773
fetched_at: '2026-06-29T00:06:01.153132+00:00'
page_id: '198937008'
product: rm
source: tdn-rm
title: TSWVRG_DT_Cotacao_Web
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWVRG_DT_Cotacao_Web
version: 1
---

# Exportar Cotação para Web

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de compras, estoque e Faturamento* |
| **Função:** | *Exportar cotação para web* |
| **Situação/Requisito:** | Durante o cálculo do quadro comparativo, o sistema não exibe algumas informações, como por exemplo: Preço Total Negociado. |
| **Solução/Implementação:** | Foi realizado um ajuste na rotina responsável por exportar cotação para a Web, o campo QUANTIDADEORC não estava sendo copiado da tabela TCITMORCAMENTO para TWCITMORCAMENTO,  dessa forma, durante o cálculo do quadro comparativo algumas informações não estavam sendo geradas. |
| **Conversores e Parâmetros:** | *Não se Aplica* |
| **Chamados relacionados:** | *Não se Aplica* |
| **Requisito (ISSUE):** | *Não se Aplica* |
| **Versões/Release:** | *12.1.7* |
