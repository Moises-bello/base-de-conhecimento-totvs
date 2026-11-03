---
content_hash: f1e470f481acda7d9bc42d93712419a0f381cc9477268798cff57ee9a3326551
fetched_at: '2026-06-29T00:08:58.707325+00:00'
page_id: '361433647'
product: rm
source: tdn-rm
title: DT - Log Cadastro de Rescisão Coletiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361433647
version: 8
---

# Rescisão Coletiva - Log Cadastro de Rescisão Coletiva

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Folha de Pagamento |
| **Módulo:** | Rescisão |
| **Função:** | Rescisão Coletiva |
| **Situação/Requisito:** | Log de Cadastro de Rescisão Coletiva |
| **Solução/Implementação:** | Implementação de um log consolidado que retorna todas as chapas processadas, informando as inconsistências encontradas por chapa e agrupadas por quebra seção. |

**Funcionamento do Processo:**

Acesse o menu de Rescisão Coletiva

Preencher os campos da rescisão coletiva conforme desejado e, avançar o processo até a interface de Dados da Rescisão. Nesta interface, marcar o parâmetro 'Gerar Log Consolidado' e informar um caminho onde irá salvar.

Avançar o processo até concluir. Na pasta informada na etapa acima, será gerado um arquivo .txt, com as informações dos funcionários processados, conforme o exemplo abaixo:

Marcando o checkbox 'Abrir arquivo ao final da execução', quando o processo finalizar a execução, irá abrir o log consolidado no formato .txt para o usuário, não sendo necessário fazer a busca do arquivo na pasta informada. O arquivo continua salvo na pasta para consulta posterior.
