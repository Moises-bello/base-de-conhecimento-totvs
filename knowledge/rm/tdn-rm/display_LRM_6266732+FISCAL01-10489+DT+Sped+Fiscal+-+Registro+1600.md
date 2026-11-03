---
content_hash: 4a57003f4190c09ade2a5c40e6a0baa5d153ced28410072fd5bac119797ad92a
fetched_at: '2026-06-29T00:10:27.939629+00:00'
page_id: '517131073'
product: rm
source: tdn-rm
title: 6266732 FISCAL01-10489 DT Sped Fiscal - Registro 1600
type: documentation
url: https://tdn.totvs.com/display/LRM/6266732+FISCAL01-10489+DT+Sped+Fiscal+-+Registro+1600
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Sped Fiscal |
| Ticket: | 6266732 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10489 |

## **02. SITUAÇÃO/REQUISITO**

Cliente solicita melhoria na geração do Registro 1600 do arquivo SPED Fiscal, para que o mesmo possa ser gerado considerando a data de emissão do movimento, atualmente o sistema considera a data da baixa do lançamento financeiro gerado pela forma de pagamento "Cartão de Crédito".

## **03. SOLUÇÃO**

Foi alterado a geração do Registro 1600, do SPED Fiscal.  Elas são:

* O registro será gerado considerado todas das VENDAS realizadas com Cartão de Credito ou Debito no período da Rotina, independente se foi “Baixado ou não”. (Essa consistência estará considerando a “Data de Emissão” do Lançamento);

* O Lançamento fiscal deve ser escriturado no NUCLEUS (Gestão de Estoques, Compras e Faturamentos);

* O Movimento do NUCLEUS deve ser integrado com o Financeiro, possuindo "Forma de Pagamento";

* Meios de pagamentos que não possuírem Cliente/Fornecedor, não serão gerados no Registro 1600. No Log da execução do processo de geração do SPED Fiscal, esses meios de pagamentos serão destacados

Criado uma mensagem ao entrar no SPED Fiscal com as alterações acima.
