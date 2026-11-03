---
content_hash: e46448e7a247fec202b579a53b33d4e2da34df5af189bdfe8c64a23ec062b26b
fetched_at: '2026-06-29T00:06:03.245684+00:00'
page_id: '198952046'
product: rm
source: tdn-rm
title: TSRDA0_DT_Faltas_Tabela_PFUFERIAS_Lancamento_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/TSRDA0_DT_Faltas_Tabela_PFUFERIAS_Lancamento_Ferias
version: 1
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
| **Chamados relacionados:** | *TSRDA0* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
