---
content_hash: 3adad0976574e76ec7cf5b192840348d7ae4c4fb6476f5d89f0d8851657dc66d
fetched_at: '2026-06-29T00:08:55.499116+00:00'
page_id: '349186075'
product: rm
source: tdn-rm
title: FISCAL01-4186 DT Integração TAF WebService T001 e T001AB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=349186075
version: 3
---

# Integração RM x TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Integração RM x TAF |
| **Situação/Requisito:** | Na geração dos registros de integração com o TAF os registro T001 (Complemento da Filial) e T001AB (Processo Judicial) são sempre gerados impactando na geração da REINF onde é necessário o re-envio dos eventos R-1000 e R-1070 mesmo sem alterações. |
| **Solução/Implementação:** | Foi criado o controle de geração dos registros T001 e T001AB no layout de integração TAF e contexto que é feito através do processo "Integração TAF - WebService - Consulta" a partir da visão de Integração RM x TAF. Se o registro for consultado e a integração ocorrer com sucesso no TAF, então os registros T001 ou T001AB não serão mais gerados pelo processo "Geração de Registros - TAF Fiscal", desde que não passem por alterações no cadastro de Filial ou de processos judiciais.  Também foi criado o parâmetro "Gerar Processo Judicial\Administrativo Obrigatoriamente" na aba "Demais Parâmetros 3" no processo de Geração de Registros - TAF Fiscal.  Efeito do novo Parâmetro: Com este campo marcado o processo judicial\administrativo será gerado para o TAF mesmo se gerado anteriormente   Default do Novo Parâmetro: Desmarcado  Este novo parâmetro será utilizado no filtro do registro T001AB. |
| **Requisito:** | FIS000408 |
| **Documento de Referência:** |  |
