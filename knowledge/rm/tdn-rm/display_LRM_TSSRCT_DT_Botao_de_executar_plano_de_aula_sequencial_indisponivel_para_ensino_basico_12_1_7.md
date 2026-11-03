---
content_hash: 19d03783a7082ca4f48b6697b546549fe71dee7a044a2ddcfdaf0dea42f79774
fetched_at: '2026-06-29T00:06:02.910988+00:00'
page_id: '198950060'
product: rm
source: tdn-rm
title: TSSRCT_DT_Botao_de_executar_plano_de_aula_sequencial_indisponivel_para_ensino_basico_12_1_7
type: documentation
url: https://tdn.totvs.com/display/LRM/TSSRCT_DT_Botao_de_executar_plano_de_aula_sequencial_indisponivel_para_ensino_basico_12_1_7
version: 2
---

# PLANO DE AULA SEQUENCIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Gerar plano de aula sequencial.* |
| **Situação/Requisito:** | *Botão de executar plano de aula sequencial indisponível quando o nível de ensino é básico. O botão estava desabilitado devido a uma validação da*  *carga horária, que para o nível de ensino básico não vinha preenchida.* |
| **Solução/Implementação:** | *A busca da carga horária para o nível de ensino básico estava errada. Como solução, foi incluída verificação do nível de ensino para a busca da carga*  *horária: quando o nível de ensino for básico, utiliza o campo CH da tabela SDISCGRADE; e quando o nível de ensino for superior, utiliza o campo CH*  *da tabela SDISCIPLINA.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.7.* |
