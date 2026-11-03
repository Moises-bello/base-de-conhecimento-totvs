---
content_hash: 94791e8c59bbfc68d3a11aef237e493995462ded135424466927aba8ae69d320
fetched_at: '2026-06-29T00:08:59.423037+00:00'
page_id: '362452365'
product: rm
source: tdn-rm
title: DT Log Cadastro de Aviso Prévio Coletivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362452365
version: 2
---

# Aviso Prévio Coletivo - Log Consolidado

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Folha de Pagamento |
| **Módulo:** | Rescisão |
| **Função:** | Aviso Prévio Coletivo |
| **Situação/Requisito:** | Log de Cadastro de Aviso Prévio Coletivo. |
| **Solução/Implementação:** | Implementação de um log consolidado que retorna todas as chapas processadas, informando as inconsistências encontradas por chapa e agrupadas por quebra seção e por todo processo. |
| **Documento de Referência:** | <http://fwrm-wiki:9999/WikiHelp/FOP/FOP.AvisoPrevio.aspx> |

**Funcionamento do Processo:**

Acesse o menu de Aviso Prévio Coletivo

Preencher os campos do aviso prévio coletivo conforme desejado e marcar o parâmetro 'Gerar Log Consolidado' e informar um caminho onde irá salvar.

Avançar o processo até concluir. Na pasta informada na etapa acima, será gerado um arquivo .txt, com as informações dos funcionários processados, conforme o exemplo abaixo:

Marcando o checkbox 'Abrir arquivo ao final da execução', quando o processo finalizar a execução, irá abrir o log consolidado no formato .txt para o usuário, não sendo necessário fazer a busca do arquivo na pasta informada. O arquivo continua salvo na pasta para consulta posterior.
