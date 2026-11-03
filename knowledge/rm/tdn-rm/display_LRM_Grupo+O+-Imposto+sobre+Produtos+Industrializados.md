---
content_hash: 0b702ee30b8d574b3e1a87be21d614d22ac10a72940b5f1279f9e20d2b90dc42
fetched_at: '2026-06-29T00:12:10.619198+00:00'
page_id: '953002910'
product: rm
source: tdn-rm
title: Grupo O -Imposto sobre Produtos Industrializados
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+O+-Imposto+sobre+Produtos+Industrializados
version: 2
---

| **Grupo O - Imposto sobre Produtos Industrializados** | | | | | | | | | | | | |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocorrência | Tamanho | Observação | **Campo de Origem** | **Campo na Aplicação** | Mais Informações |
| 246 | O01 | IPI | Grupo IPI | CG | M01 |  | 0-1 |  | Informar apenas quando o item for sujeito ao IPI. | Não será Gerado para Produtos do tipo serviço |  |  |
| ~~247~~ | ~~O02~~ | ~~clEnq~~ | ~~Classe de enquadramento do IPI para Cigarros e Bebidas~~ | ~~E~~ | ~~O01~~ | ~~C~~ | ~~0-1~~ | ~~1-5~~ | ~~Preenchimento conforme Atos Normativos editados pela Receita Federal (Observação 2).~~ |  |  |  |
| 248 | O03 | CNPJProd | CNPJ do produtor da mercadoria, quando diferente do emitente. Somente para os casos de exportação direta ou indireta. | E | O01 | N | 0-1 | 14 | Preenchimento conforme Anexo II-A da Instrução Normativa RFB Nº 770/2007. | TFAB.CGC | CNPJ |  |
| 249 | O04 | cSelo | Código do selo de controle IPI | E | O01 | C | 0-1 | 1-60 | | TIPO DE SELO | CÓDIGO | COR DO SELO | | --- | --- | --- | | Produto Nacional | 9710-01 | Verde combinado com marrom | | Produto Nacional para Exportação - Tipo "1" | 9710-10 | Verde Escuro combinado com marrom | | Produto Nacional para Exportação - Tipo "2" | 9710-11 | Verde Escuro combinado com marrom | | Produto Nacional para Exportação - Tipo "3" | 9710-12 | Verde Escuro combinado com marrom | | Produto Estrangeiro | 8610-09 | Vermelho combinado com azul | | TPRDFISCAL.CODIGOSELOIPI | Código do selo de Controle IPI |  |
| 250 | O05 | qSelo | Quantidade de selo de controle | E | O01 | N | 0-1 | 1-12 |  | prod.qtrib(TITMMOV.QUANTIDADETRIBUTAVEL ou TITMMOV.QUANTIDADE) |  |  |
| 251 | O06 | cEnq | Código de Enquadramento Legal do IPI. | E | O01 | N | 1-1 | 1-3 | Preenchimento conforme Anexo XIV da Nota Técnica 2015.002. | TTRBMOV.CODENQIPI | Código de Enquadramento IPI | Item do movimento, pasta Tributos, na linha do tributo. |
| 252 | O07 | IPITrib | Grupo do CST 00, 49, 50 e 99 | CG | O01 |  | 1-1 |  | Informar apenas um dos grupos O07 ou O08 com base valor atribuído ao campo O09 – CST do IPI |  |  |  |
| 253 | O09 | CST | Código da situação tributária do IPI | E | O07 | N | 1-1 | 2 | 00=Entrada com recuperação de crédito 49=Outras entradas 50=Saída tributada 99=Outras saídas | DREGRAIPI.SITTRIBUTARIAIPIENT, DREGRAIPI.SITTRIBUTARIAIPISAI | Regra de ICMS | Regra de ICMS vinculada a natureza selecionada no movimento da NF-e. |
| 253.1 | O09.1 | -x- | Sequência XML | CG | O07 |  | 1-1 |  | Informar os campos O10 e O13 se o cálculo do IPI for por alíquota. |  | Alíquota | Será gerado somente se o campo TTRBMOV.ALIQUOTAPORVALOR não estiver com valor > 0 |
| 254 | O10 | vBC | Valor da BC do IPI | E | O09.1 | N | 1-1 | 13v2 | TTRBMOV.BASEDECALCULO | Base de Cálculo |  |
| 257 | O13 | pIPI | Alíquota do IPI | E | O09.1 | N | 1-1 | 3v2-4 | TTRBMOV.ALIQUOTA |  |  |
| 257.1 | O13.1 | -x- | Sequência XML | CG | O07 |  | 1-1 |  | Informar os campos O11 e O12 se o cálculo do IPI for de valor por unidade. | Será gerado somente se o campo TTRBMOV.ALIQUOTAPORVALOR estiver com valor > 0 |  |  |
| 255 | O11 | qUnid | Quantidade total na unidade padrão para tributação (somente para os produtos tributados por unidade). | E | O13.1 | N | 1-1 | 12v0-4 | qTrib |  |  |
| 256 | O12 | vUnid | Valor por Unidade Tributável | E | O13.1 | N | 1-1 | 11v0-4 | vUnTrib |  | Caso o IPI, o COFINS e o PIS sejam pautados no Produto, o sistema levará para essa TAG os valores cadastrados na pauta do Produto (Alíquota Débito ou Crédito). |
| 259 | O14 | vIPI | Valor do IPI | E | O07 | N | 1-1 | 13v2 |  | TTRBMOV.VALOR |  |  |
| 260 | O08 | IPINT | Grupo CST 01, 02, 03, 04, 51, 52, 53, 54 e 55 | CG | O01 |  | 1-1 |  |  |  |  |  |
| 261 | O09 | CST | Código da situação tributária do IPI | E | O08 | C | 1-1 | 2 | 01=Entrada tributada com alíquota zero 02=Entrada isenta 03=Entrada não-tributada 04=Entrada imune 05=Entrada com suspensão 51=Saída tributada com alíquota zero 52=Saída isenta 53=Saída não-tributada 54=Saída imune 55=Saída com suspensão | DREGRAIPI.SITTRIBUTARIAIPIENT, DREGRAIPI.SITTRIBUTARIAIPISAI |  |  |
