---
content_hash: a2f95b021f111112a8cb9fa9a0bf7a2411a4dcc1bf4c2b962c92437e26533a7d
fetched_at: '2026-06-29T00:09:07.786674+00:00'
page_id: '385848404'
product: rm
source: tdn-rm
title: 222006 DSAUGCIH-21 DT Cultura Parcial - Validação da Data da Coleta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385848404
version: 1
---

# Cultura Parcial - Validação da Data da Coleta

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Controle de Infecção Hospitalar (CIH) |
| **Função:** | Regra de validação do campo Data da Coleta no cadastro de Cultura Parcial. |
| **Situação/Requisito:** | No lançamento manual da cultura parcial, quando o campo [Data Coleta] for idêntica à Data da Internação ou Alta, a ferramenta deve solicitar o lançamento do campo [Hora Coleta]. |
| **Solução/Implementação:** | Regra de validação criada na tela de Cultura Parcial. |

Detalhes sobre a regra de validação:

1º Na tela de Cultura Parcial preencha o Campo [Data Coleta] com a mesma data da Internação ou da Alta sem preencher o campo [Hora Coleta] e após clique na opção salvar.

2º Conforme preenchimento anterior agora o módulo CIH valida o campo [Hora Coleta] conforme o detalhe da imagem abaixo.
