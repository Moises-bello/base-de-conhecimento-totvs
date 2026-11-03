---
content_hash: 6927574ff6a5901ccd493ce0f6a68e932c23eb582b4e90b8c453a792979ab479
fetched_at: '2026-06-29T00:08:52.686027+00:00'
page_id: '342299982'
product: rm
source: tdn-rm
title: 1774082 FISCAL01-2714 DT NF-e Layout Sefaz - CEP
type: documentation
url: https://tdn.totvs.com/display/LRM/1774082+FISCAL01-2714+DT+NF-e+Layout+Sefaz+-+CEP
version: 91
---

# NF-e Layout Sefaz - CEP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio NS-e |
| **Situação/Requisito:** | NF-e - Layout Sefaz - CEP Conteúdo do campo não obedece ao Esquema da NF-e Ao realizar envio de NF-e com o campo CEP do cliente/fornecedor  não preenchido, é apresentada a seguinte mensagem de inconsistência:  Não foi possível enviar a nota. Enviar NF-e: Erro no envio da NF-e.  TSS - Erro na validação desta nota. Motivo:Campo: CEP': Conteúdo do campo não obedece ao Esquema da NF-e. O valor ''  não é aceito pelo padrão estabelecido pela SEFAZ: '[0-9]{8}'. Campo: CEP': '' não é um valor válido. |
| **Solução/Implementação:** | Ajuste para que quando o campo CEP não esteja preenchido no cliente/fornecedor a Tag não seja gerada no XML |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | Não se Aplica |
| **Requisito:** | Não se Aplica |

divs
