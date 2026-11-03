---
content_hash: 1d44d32f9ea4aa4e178dd2c5e4c8613ffc47b34354717cfdf903ce470f36a8ed
fetched_at: '2026-06-29T00:08:35.456337+00:00'
page_id: '280735768'
product: rm
source: tdn-rm
title: 740213 FOPCALCULO01-45 DT Alterar Situação de Férias por Fórmula Visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=280735768
version: 105
---

# Alterar Situação de Férias por Fórmula Visual

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Alterar Situação de Férias por Fórmula Visual |
| **Situação/Requisito:** | Cliente informa que possuí uma fórmula visual desenvolvida e funcionando perfeitamente na versão 11.82. Porém ao migrar para a versão 12.1.15, a Fórmula Visual passou a apresentar o seguinte erro:  Fórmula Visual: 'PROPAY - Altera Status de Ferias'.   Erro na execução da Atividade: 'Expressao'   Erro: Column 'SITUACAOFERIAS' is read only.  Basicamente essa Fórmula Visual utiliza o data server "FopFuFeriasPerDataBR" e é executada no portal quando o gestor aprova, ela já altera  automaticamente a SITUAÇÃO das férias. |
| **Solução/Implementação:** | Ajuste realizado ao setar o Props do DataSet onde estava alterando a coluna 'SITUACAOFERIAS' para somente leitura |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | 740213 |
| **Requisito:** | Informe o requisito relacionado. |

divs
