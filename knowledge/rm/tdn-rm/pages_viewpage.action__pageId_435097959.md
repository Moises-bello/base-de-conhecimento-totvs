---
content_hash: cc2b2ffbd4fec38179efcaabb694c952b4583bbd3b1bd2b31a3dd330cee5c44e
fetched_at: '2026-06-29T00:09:45.866660+00:00'
page_id: '435097959'
product: rm
source: tdn-rm
title: 4338732 DEDUINTEGRACOES-3748 DT Os campos de valores opcionais estão vindo
  bloqueados quando criamos uma nova coligada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435097959
version: 2
---

# Parametrização dos Valores Opcionais no Educacional

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Parametrização dos valores opcionais e valor de integração para controlar os valores financeiros |
| **Situação/Requisito:** | Temos algumas coligadas que possuem lançamentos gerados, com isso os campos de valores opcionais ficam bloqueados o que está correto, porém criamos uma nova coligada onde a mesma não contém lançamentos gerados, mas mesmo assim os campos de valores opcionais estão vindo já bloqueados para essa nova coligada.  Por se tratar de uma nova coligada o sistema deveria vir com os campos desabilitados para que possamos realizar a parametrização. |
| **Solução/Implementação:** | Para parametrizações em coligadas novas daremos opção do cliente escolher se irá utilizar o valor opcional ou valor de integração. Neste caso ajustamos para que o valor opcional fique habilitado quando não houver movimentação para o campo parametrizado, e quando o valor de integração não estiver preenchido. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
| **Pacote:** | Informe o [linkdopacote] |
