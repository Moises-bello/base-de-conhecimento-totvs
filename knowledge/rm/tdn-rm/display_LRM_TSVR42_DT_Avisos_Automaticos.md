---
content_hash: 544e3b5a56189990e8d31042af7859ae0e44941841ed9e8d65dc11f2f7644599
fetched_at: '2026-06-29T00:06:03.237244+00:00'
page_id: '198951928'
product: rm
source: tdn-rm
title: TSVR42_DT_Avisos_Automaticos
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVR42_DT_Avisos_Automaticos
version: 3
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
| **Chamados relacionados:** | *TSVR42* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.40* |
