---
content_hash: 466a3ef232c5731ec95531619104de26d41efc2a86acdcbf2cae8dbfc71feb21
fetched_at: '2026-06-29T00:06:00.859531+00:00'
page_id: '196812964'
product: rm
source: tdn-rm
title: TSVBBF_DT_SEFIP_Sem_Verba_FGTS_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVBBF_DT_SEFIP_Sem_Verba_FGTS_Rescisao
version: 8
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração do relatório da SEFIP* |
| **Situação/Requisito:** | Ao gerar o SEFIP, com um funcionário transferido tipo 5 - Transferência sem ônus p/ Cedente, sendo para mesma coligada ou uma coligada diferente, ao executar o arquivo é gerado a seguinte inconsistência:  300567 - Para Categoria indicada deve ser informada Remuneração sem 13º Salário ou Remuneração 13º Salário |
| **Solução/Implementação:** | *Ajustado  a geração do arquivo SEFIP para realizar validação correta não sendo necessárias intervenções  manuais. O valor será carregado corretamente para funcionários transferidos com tipo 5 ou 6 não causando erros devido a falta da base de FGTS no mês da transferência.* |
| **Chamados relacionados:** | **TSVBBF** |
| **Versões/Release:** | *12.1.6* |
