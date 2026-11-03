---
content_hash: 3ca239d1b63eed6111292b5d8f1ebbf758e437e0eec8312fcf1fcab99a1d88bd
fetched_at: '2026-06-29T00:09:04.026274+00:00'
page_id: '382543797'
product: rm
source: tdn-rm
title: 3292748 FOPCALCULO01-4220 - SEFIP
type: documentation
url: https://tdn.totvs.com/display/LRM/3292748+FOPCALCULO01-4220+-+SEFIP
version: 1
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | SEFIP |
| **Situação/Requisito:** | Ao gerar SEFIP, e realizar a parametrização em Encargos>Parâmetros/INSS/SEFIP, para alguns tomadores de serviço, o sistema apresenta na pasta CEI, o cadastro do próprio Tomador de Serviço, sendo que o mesmo não possui nenhum CEI vinculado ao cadastro.  Foi constatado que essa situação ocorre, quando por algum motivo, no cadastro do funcionário, tem uma sujeira no campo CEI.  Quando o cliente vai gerar a SEFIP e informa o valor da retenção, o sistema não alimenta o arquivo da SEFIP. |
| **Solução/Implementação:** | Ajuste nos parâmetros do SEFIP para não inserir CEI no tomador quando estiver com o CEI vazio no cadastro. |
| **Tickets relacionados:** | 3292748 |
