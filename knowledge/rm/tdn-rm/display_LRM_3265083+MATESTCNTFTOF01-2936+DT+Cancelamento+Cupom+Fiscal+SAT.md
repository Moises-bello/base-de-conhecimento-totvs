---
content_hash: 16545b694d954398e105df3c9cbf542f3d556ab992672a87378197de5d6a33d9
fetched_at: '2026-06-29T00:09:07.566788+00:00'
page_id: '384578574'
product: rm
source: tdn-rm
title: 3265083 MATESTCNTFTOF01-2936 DT Cancelamento Cupom Fiscal SAT
type: documentation
url: https://tdn.totvs.com/display/LRM/3265083+MATESTCNTFTOF01-2936+DT+Cancelamento+Cupom+Fiscal+SAT
version: 84
---

# Cancelamento Cupom Fiscal SAT

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Cancelamento Cupom Fiscal SAT. |
| **Situação/Requisito:** | Na parametrização de cupom fiscal SAT e NFCe deve-se desmarcar a opção “Emite Cupom Fiscal” na configuração do tipo de movimento.  No entanto com essa configuração, ao consumir o serviço de inclusão de cupom fiscal (Integração PDV Protheus)  e posteriormente o cancelamento, o cancelamento do cupom não é realizado. |
| **Solução/Implementação:** | Melhoria relacionada ao cupom fiscal (SAT e NFCe), esses não emitem cupom fiscal, passam a utilizar chave de acesso para recuperar o movimento, com isso o cancelamento funciona corretamente. SAT e NFCe devem ficar com a opção “Emite Cupom Fiscal” desmarcado na configuração do tipo de movimento. |
| **Conversores e Parâmetros:** | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.09 - Tipo de Movimento | Etapa 62 - Fiscal - Dados Fiscais| **Emite Cupom Fiscal**. |
| **Tickets relacionados:** | 3265083. |
| **Requisito:** | MATESTCNTFTOF01-2936 |

divs
