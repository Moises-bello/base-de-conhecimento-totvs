---
content_hash: db3434a058a3500c3e441e036ec22bc6426a155a1ae5ba42e60363e4974977bf
fetched_at: '2026-06-29T00:06:25.825796+00:00'
page_id: '224448059'
product: rm
source: tdn-rm
title: TTUPRJ_DT_Acerta_Periodo_Aquisitivo_Limpa_Dados_PFUNC
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUPRJ_DT_Acerta_Periodo_Aquisitivo_Limpa_Dados_PFUNC
version: 2
---

# ROTINA PARA ACERTAR PERIODO AQUISITIVO ESTÁ LIMPANDO DADOS DE FÉRIAS DA PFUNC

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Acerta Período Aquisitivo* |
| **Situação/Requisito:** | *Na execução da rotina de Acerta Periodo Aquisitivo está sempre limpando os dados de férias da PFUNC, que são utilizados para a manter a compatibilidade com o modelo de férias antigo do Delphi, que ainda é usado em alguns relatórios de cliente.* |
| **Solução/Implementação:** | *Ajuste para limpar os dados de férias da PFUNC somente no caso de ser perdido o periodo aquisitivo devido a afastamentos.*  *Caso haja apenas a extensão da data final do periodo, os dados devem ser mantidos para não atrapalhar os relatórios do cliente.*  *Neste caso deve ser atualizado somente a data de vencimento das férias, que foi alterada.* |
| **Chamados   relacionados:** | *TTUPRJ, TUGBCB* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
