---
content_hash: 715cb02354d72c659544bb1c0607315f0b71be70919c5c255be85dc8eb749fcb
fetched_at: '2026-06-29T00:10:21.772722+00:00'
page_id: '493638718'
product: rm
source: tdn-rm
title: 1294765 FISCAL01-1469 DT Lançamento Outros Débitos/Crédito - Tratar campo Observação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493638718
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Lançamento Outros Débitos/Creditos |
| Ticket: | 1294765 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-1469 |

## **02. SITUAÇÃO/REQUISITO**

Cliente solicita que ao gerar o Lançamento de Outros Débitos e Créditos automático referente ao Diferencial de alíquotas para a filial de SP, seja preenchido a seguinte expressão no campo Descrição "Inciso I do Art. 117 do RICMS".

Trecho da legislação:  
Artigo 117 - Em caso de entrada, real ou simbólica, de mercadoria oriunda de outro Estado, destinada a uso, consumo ou integração no ativo imobilizado, ou de utilização de serviço cuja prestação se tiver iniciado fora do território paulista e não estiver vinculada a operação ou prestação subseqüente alcançada pela incidência do imposto, sendo a alíquota interna superior à interestadual, o contribuinte deverá escriturar no livro Registro de Apuração do ICMS, no período em que a mercadoria tiver entrado ou tiver sido tomado o serviço (Lei 6.374/89, art. 59):

I - como crédito, no quadro "Crédito do Imposto - Outros Créditos", com a expressão "Inciso I do Art. 117 do RICMS", o valor do imposto pago em outro Estado, relativo à respectiva operação ou prestação;  
II - como débito, no quadro "Débito do Imposto - Outros Débitos", com a expressão "Inciso II do Art. 117 do RICMS", o valor do imposto decorrente da aplicação da alíquota interna sobre a base de cálculo correspondente à operação ou prestação aludida no inciso anterior.

## **03. SOLUÇÃO**

O texto do campo "**Observação**" do lançamentos de Outros Débitos/Créditos inserido através do processo "**Inserir Lançamentos Diferencial de Alíquota**".

Lançamento de Débito: "*Débito Diferencial de Alíquota - Inciso I do Art. 117 do RICMS/SP*"

Lançamento de Crédito: "*Crédito Diferencial de Alíquota - Inciso II do Art. 117 do RICMS/SP*"

OBS.: Caso o processo seja utilizado para outro Estado, colocar condição para que o novo texto seja aplicado apenas para Filiais de São Paulo.
