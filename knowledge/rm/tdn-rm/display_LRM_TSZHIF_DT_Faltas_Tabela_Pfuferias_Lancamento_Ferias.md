---
content_hash: 0729f18e95d9977fb38afea0693ae42648032b6b3403cb77eca90f739d943b94
fetched_at: '2026-06-29T00:06:03.275546+00:00'
page_id: '198952605'
product: rm
source: tdn-rm
title: TSZHIF_DT_Faltas_Tabela_Pfuferias_Lancamento_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZHIF_DT_Faltas_Tabela_Pfuferias_Lancamento_Ferias
version: 2
---

# CAMPO FALTAS DA TABELA PFUFERIAS GRAVADO NO LANÇAMENTO DAS FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração do Histórico de Provisões* |
| **Situação/Requisito:** | *A coluna Faltas da tabela PFUFERIAS só é preenchida quando as férias são finalizadas, porém assim que as férias são lançadas ao envelope já deveria registrar a quantidade de faltas na tabela.* |
| **Solução/Implementação:** | *Alterar o momento da gravação da quantidade de faltas que o funcionário teve no periodo aquisitivo corrente.*  *O conteúdo do campo Faltas da tabela PFUFERIAS passará a ser gravado no processo de Lançamento das Férias.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSZHIF* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
