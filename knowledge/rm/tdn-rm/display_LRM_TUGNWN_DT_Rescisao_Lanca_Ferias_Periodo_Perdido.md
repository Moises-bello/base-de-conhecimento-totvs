---
content_hash: 531027004cc433825be61babd6550d6fa64957ce79e7ff70123091b96060ece2
fetched_at: '2026-06-29T00:06:28.849105+00:00'
page_id: '233763216'
product: rm
source: tdn-rm
title: TUGNWN_DT_Rescisao_Lanca_Ferias_Periodo_Perdido
type: documentation
url: https://tdn.totvs.com/display/LRM/TUGNWN_DT_Rescisao_Lanca_Ferias_Periodo_Perdido
version: 2
---

# RESCISÃO ESTÁ LANÇANDO AVOS DE FÉRIAS DE PERIODO PERDIDO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | *No cálculo da rescisão com aviso prévio indenizado, quando o parâmetro "Soma avos de aviso após o cálculo" está marcado, não está sendo levado em consideração a perda do periodo aquisitivo devido a Licença Remunerada por mais de 30 dias.*  *Com o parâmetro desmarcado, o cálculo é feito corretamente.* |
| **Solução/Implementação:** | *Ajuste na rescisão, para não lançar avos de periodo aquisitivo perdido devido a mais de 30 dias de Licença Remunerada, mesmo quando o parâmetro "Soma avos de aviso após o cálculo" está marcado.* |
| **Chamados   relacionados:** | *TUGNWN, TULZAB* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
