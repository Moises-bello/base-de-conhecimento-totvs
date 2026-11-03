---
content_hash: ac0c6a7b99feaf838eaf2a5fcc781efe6622041f8e95f2c67283a43999bd3b4a
fetched_at: '2026-06-29T00:12:10.343202+00:00'
page_id: '953002365'
product: rm
source: tdn-rm
title: Grupo K - Detalhamento Específico de Medicamento e de Matérias-primas Farmacêuticas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953002365
version: 1
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo K - Detalhamento Específico de Medicamento e de Matérias-primas Farmacêuticas** | | | | | | | | | | | | |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocorrência | Tamanho | Observação | **Campo de Origem** | **Campo da Aplicação** | Mais Informações |
| 152 | K01 | med | Detalhamento de Medicamentos e de matérias-primas farmacêuticas | CG | I90 |  | 1-500 |  | Informar apenas quando se tratar de medicamentos ou de matérias-primas farmacêuticas, permite ocorrências. |  | - | - |
| 152a | K01a | cProdANVISA | Código de Produto da ANVISA | E | K01 | C | 1-1 | 13 | Utilizar o número do registro ANVISA Obs.: Para medicamento isento de registro na ANVISA, utilizar o número da decisão que o isenta, como por exemplo o número da Resolução da Diretoria Colegiada da ANVISA (RDC). | Gerado com a Informação do cadastro do Produto\Anexo Sub Pasta Informações RM Saude. SZPRD.REGISTROANVISA. Se o campo anterior não estiver sido preenchido a tag será preenchida com o valor do campo TPRODUTODEF.REGISTROANVISA. |  | Script: NU.2018.08\_01 |
| 153 | K02 | ~~nLote~~ | ~~Número do Lote de medicamentos ou de matérias-primas farmacêuticas~~ | ~~E~~ | ~~K01~~ |  | ~~1-1~~ | ~~1-20~~ | ~~-~~ |  |  |  |
| ~~154~~ | ~~K03~~ | ~~qLote~~ | ~~Quantidade de produto no Lote de medicamentos ou de matérias-primas farmacêuticas~~ | ~~E~~ | ~~K01~~ | ~~N~~ | ~~1-1~~ | ~~8v3~~ | - |  |  |  |
| ~~155~~ | ~~K04~~ | ~~dFab~~ | ~~Data de fabricação~~ | ~~E~~ | ~~K01~~ | ~~D~~ | ~~1-1~~ |  | ~~Formato: “AAAA-MM-DD”~~ |  |  |  |
| ~~156~~ | ~~K05~~ | ~~dVal~~ | ~~Data de validade~~ | ~~E~~ | ~~K01~~ | ~~D~~ | ~~1-1~~ |  | ~~Formato: “AAAA-MM-DD”~~ |  |  |  |
| 157 | K06 | vPMC | Preço máximo consumidor | E | K01 | N | 1-1 | 13v2 | - | TPRDCODFISCAL.PRECOSUGERIDO ou TLOTEPRD.PRECOSUGERIDO | Preço Sugerido Consumidor | Cadastro do produto, em Anexos | Dados Fiscais por UF | Identificação da Codificação Fiscal do Produto. |
