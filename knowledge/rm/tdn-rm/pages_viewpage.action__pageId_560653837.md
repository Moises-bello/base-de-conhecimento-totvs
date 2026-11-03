---
content_hash: a1bf33b04ce4a080c4ebb6fbc175007625b275f82588b9c92270ec7f85145bfe
fetched_at: '2026-06-29T00:10:47.776843+00:00'
page_id: '560653837'
product: rm
source: tdn-rm
title: Totais monetários e alíquotas aplicadas ao documento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653837
version: 27
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| valores | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | G | 1-1 | Tag raíz para os valores totais do documento. |  |  |
| iss | valores | E | 1-1 | Valor total de ISS do documento. | SOMA(Servico.valiss de todos os itens da nota) | Para o município de Brasília é possível cadastrar ISS devido e retido simultaneamente na mesma nota, por tanto para o tributo ISS o valor considerado será apenas os valores de ISS cujo tipo de retenção seja "Devido" ou "Depósito Juízo". |
| issret | valores | E | 1-1 | Valor total de ISS retido do documento. | SOMA(Servico.valissret de todos os itens da nota) |  |
| outrret | valores | E | 1-1 | Valor total de outras retenções do documento. | SOMA(Servico.valoutasret de todos os itens da nota) |  |
| pis | valores | E | 1-1 | Valor total de PIS do documento. | SOMA(Servico.valpis de todos os itens da nota) |  |
| cofins | valores | E | 1-1 | Valor total de COFINS do documento. | SOMA(Servico.valcof de todos os itens da nota) |  |
| inss | valores | E | 1-1 | Valor total de INSS do documento. | SOMA(Servico.valinss de todos os itens da nota) |  |
| ir | valores | E | 1-1 | Valor total de IR do documento. | SOMA(Servico.valir de todos os itens da nota) |  |
| csll | valores | E | 1-1 | Valor total de CSLL do documento. | SOMA(Servico.valcsll de todos os itens da nota) |  |
| aliqiss | valores | E | 1-1 | Alíquota de ISS do documento. | TTRBMOV.ALIQUOTA | Aliquota do ISS |
| aliqpis | valores | E | 1-1 | Alíquota de PIS do documento. | TTRBMOV.ALIQUOTA | Aliquota do PIS |
| aliqcof | valores | E | 1-1 | Alíquota de COFINS do documento. | TTRBMOV.ALIQUOTA | Aliquota do COFINS |
| aliqinss | valores | E | 1-1 | Alíquota de INSS do documento. | TTRBMOV.ALIQUOTA | Aliquota do INSS |
| aliqir | valores | E | 1-1 | Alíquota de IR do documento. | TTRBMOV.ALIQUOTA | Aliquota do IR |
| aliqcsll | valores | E | 1-1 | Alíquota de CSLL do documento. | TTRBMOV.ALIQUOTA | Aliquota do CSLL |
| valtotdoc | valores | E | 1-1 | Valor total do documento. |  | SOMA(servico.valtotal de todos os itens da nota) |
| valcartri | valores | E | 0-1 | Valor da carga tributaria | TITMMOVFISCAL.VLRTOTTRIB |  |
| valpercartri | valores | E | 0-1 | Percentual da carga tributaria |  | Soma dos campos do serviço utilizado:  TPRDCODFISCAL.ALIQIBPTFEDERAL,   TPRDCODFISCAL.ALIQIBPTESTADUAL,                                          TPRDCODFISCAL.ALIQIBPTMUNICIPAL |
| valfoncartri | valores | E | 0-1 | Fonte da carga tributaria |  | Informação Fixa : IBPT |
| outdesp | valores | E | 0-1 | Outras Despesas. |  | soma as despesas do serviço utilizado:  TITMMOV.VALORDESP |
| basiss | valores | E | 0-1 | Base ISS. |  | Se: Tributo no movimento possui tributo com tipotribfisc = ISS  Então: base de calculo do movimento  Senão: Somatório da base de calculo dos tributos com tipotribfisc = ISS |
| bascsll | valores | E | 0-1 | Base CSLL. |  | Se: Tributo no movimento possui tributo com tipotribfisc = CSLLRF  Então: base de calculo do movimento  Senão: Somatório da base de calculo dos tributos com tipotribfisc = CSLLRF |
| baspis | valores | E | 0-1 | Base PIS. |  | Se: Tributo no movimento possui tributo com tipotribfisc = PISRF  Então: base de calculo do movimento  Senão: Somatório da base de calculo dos tributos com tipotribfisc = PISRF |
| bascfis | valores | E | 0-1 | Base COFINS. |  | Se: Tributo no movimento possui tributo com tipotribfisc = COFINSRF  Então: base de calculo do movimento  Senão: Somatório da base de calculo dos tributos com tipotribfisc = COFINSRF |
| basir | valores | E | 0-1 | Base IR. |  | Se: Tributo no movimento possui tributo com tipotribfisc = IRRF  Então: base de calculo do movimento  Senão: Somatório da base de calculo dos tributos com tipotribfisc = IRRF |
| basinss | valores | E | 0-1 | Base INSS. |  | Se: Tributo no movimento possui tributo com tipotribfisc = INSS  Então: base de calculo do movimento  Senão: Somatório da base de calculo dos tributos com tipotribfisc = INSS |
| piscofins | valores | G | 1-1 |  |  |  |
| piscofinsApu | valores | G | 0-1 |  |  |  |
| vReceb | valores | E | 0-1 | Valor Recebido. |  | Não será gerado |
| tribISSQN | valores | E | 0-1 | Tributação ISSQN. |  | Gerado conforme o parâmetro "Regime de ISS" (disponível em Filial > Anexos > Dados Fiscais, conforme [documentação](https://tdn.totvs.com/display/public/LRM/Dados+Fiscais#1-1563551098)).  2 - Imune  3 - Exportação Serviço  4 - Isenta de ISSQN  Para qualquer outra opção será gerado o valor 1 - Operação Tributável |
| cPaisResult | valores | E | 0-1 | País Resultado. |  | Não será gerado |
| tpImunidade | valores | E | 0-1 | Tipo Imunidade. | DFILIAL.TIPOIMUNIDADE | Gerado quando o Regime Tributário da filial for igual a Imune e o tipo de imunidade (disponível em Filial > Anexos > Dados Fiscais, conforme [documentação](https://tdn.totvs.com/display/public/LRM/Dados+Fiscais#1-1563551098)) estiver preenchido.  0 - Imunidade (tipo não informado na nota de origem); 1 - Patrimônio, renda ou serviços, uns dos outros (CF88, Art 150, VI, a); 2 - Templos de qualquer culto (CF88, Art 150, VI, b); 3 - Patrimônio, renda ou serviços dos partidos políticos, inclusive suas fundações, das entidades sindicais dos trabalhadores, das instituições de educação e de assistência social, sem fins lucrativos, atendidos os requisitos da lei (CF88, Art 150, VI, c); 4 - Livros, jornais, periódicos e o papel destinado a sua impressão (CF88, Art 150, VI, d); 5 - Fonogramas e videofonogramas musicais produzidos no Brasil contendo obras musicais ou literomusicais de autores brasileiros e/ou obras em geral interpretadas por artistas brasileiros bem como os suportes materiais ou arquivos digitais que os contenham, salvo na etapa de replicação industrial de mídias ópticas de leitura a laser.   (CF88, Art 150, VI, e); |
| totret | valores | E | 0-1 | Total das retenções |  | Gerado a partir do somatório dos valores dos seguintes tributos:  IRRF + IRRFPJ +  INSS + CSLLRF + PISRF+ COFINSRF + ISS (tipo de recolhimento: Retido na Fonte ou Retido na Fonte deduzido). |
| valorliqfinal | valores | E | 0-1 | Valor liquido final da nota |  | Gerado com o valor liquido do movimento. |
| BM | valores | G | 0-1 |  |  |  |
| tpRetISSQN | valores | E | 0-1 | Tipo Retenção ISSQN. |  | Gerado de acordo com o tipo de recolhimento do ISS no item do movimento.  A tag é gerada com o valor 2 - Retido pelo Tomador para os seguintes tipos de retenção:  Nenhum, Isento, Imune, Devido e Deposito Juizo.  A tag é gerada com o valor 1 - Não Retido para os seguintes tipos de retenção:  Retido Fonte e Retido Fonte Deduzido.  Se não houver ISS com base de cálculo maior que 0 a tag também é gerada com o valor 1 - Não Retido.  O valor 3 - Retido pelo Intermediário não é gerado. |
| tribMun | valores | G | 0-1 |  |  |  |
