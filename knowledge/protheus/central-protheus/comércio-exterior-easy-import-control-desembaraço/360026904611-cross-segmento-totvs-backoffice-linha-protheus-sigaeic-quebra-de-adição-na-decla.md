---
article_id: 360026904611
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 014123728340a8602979e424662aa9aa8718cb742b7f16489eadb08ef58a81e5
fetched_at: '2026-06-28T22:39:50.188484+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Quebra de adição
  na declaração de importação
type: support-article
updated_at: '2021-10-25T13:46:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026904611-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Quebra-de-adi%C3%A7%C3%A3o-na-declara%C3%A7%C3%A3o-de-importa%C3%A7%C3%A3o
---

**Dúvida**Como realizar a quebra de adição na declaração de importação(DI)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Existe um parâmetro que define qual a quantidade de itens que podem estar em uma L.I, trata-se do MV\_NR\_ISUF. Se o sistema está deixando uma adição para cada item, por certo, está ocorrendo um dos seguintes fatos:

1 - No parâmetro MV\_NR\_ISUF o número máximo está configurado como: 1. No conteúdo no parâmetro, deve-se informar a quantidade máxima que o Siscomex admite: 78.  
  
2- Informações do processo de importação que quebram as adições:

|  |
| --- |
| Nro Li - Para este cenário é necessário que  acesse a opção:  Atualizações -> Licença de Import. -> Manutenção L.I. e informe o número da licença para a PLI gerada; desta forma o sistema irá considerar esta diferença de informação para realização da quebra da adição. |
| Fornecedor |
| Fabricante |
| NCM |
| Ex NCM |
| EX NBM |
| Condição de pagamento |
| Dias da condição de pagamento |
| Moeda |
| Incoterm |
| Regime Tributário ( II ) |
| Fundamento legal |
| Motivo de admissão temporária |
| Tipo de Acordo |
| Acordo Tarifário |
| Tab. N.V.E. |
| Operação ( CFO) |
| Regime tributário ( Pis /Cofins) |
| Fundamento legal ( Pis/Cofins) |
| Fundamento legal para redução de base de PIS e Cofins |
| Alíquota específica de IPI |
| NALADI |
| NALADI SH |
| Ato concessório |
| Regime de tributação |

**Saiba mais**  
[Opções do Desembaraço (EICDI502 - SIGAEIC)](https://tdn.totvs.com/pages/releaseview.action?pageId=312158980)  
[Qual é a quantidade de itens que podem estar em uma L.I.](https://tdn.totvs.com/pages/releaseview.action?pageId=6806685)
