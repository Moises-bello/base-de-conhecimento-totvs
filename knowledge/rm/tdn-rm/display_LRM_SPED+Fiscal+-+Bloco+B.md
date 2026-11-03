---
content_hash: e5229823b33d3bdb5738d64decc80d726cfd3a98dfff4727494547aea0bf0faf
fetched_at: '2026-06-29T00:09:54.235374+00:00'
page_id: '444596785'
product: rm
source: tdn-rm
title: SPED Fiscal - Bloco B
type: documentation
url: https://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+B
version: 50
---

Este bloco é destinado à declaração das informações da apuração do ISSQN (Imposto Sobre Serviços de Qualquer Natureza). É exclusivo para os contribuintes do Distrito Federal, para os não domiciliados é obrigatória a geração somente dos registros B001 e B990.

A partir da versão 12.1.2302 este bloco é gerado conforme o parâmetro de geração que consiste em 3 opções:

**Não gerar:**Somente os registros B001 e B990 são gerados.

**Gerar Somente Registro B470 Vazio:**São gerados os registros B001, B990 e o B470 é gerado com seus valores zerados.

**Todos os Registros - Completo:** Geração completa do bloco.

ParâmetroImportante ! 

Foi realizada uma evolução na geração do Bloco B para ser considerado os parâmetros de seleção de datas do ISS localizados em:

Ambiente | Parâmetros | Totvs Gestão Fiscal | Apuração de Tributos | ISS | Apur. ISS por Filial | Parametrizar a Filial desejada | Etapa - Datas de Apuração.

As Datas Parametrizáveis conforme o tipo de lançamento são:

Data de Emissão

Data de Entrada/Saída

Data de Pagamento/Vencimento

4RegistrosBlocoBlefttrueB020B020

**Notas Fiscais**

Serão gravados nestes registros as parcelas referentes a serviços para os seguintes modelos de documento: 01 - Nota Fiscal, 03 - Nota Fiscal de Serviço, 3B - Nota Fiscal de Serviço Avulsa, 04 - Nota Fiscal de Produtor Rural, 08 - Conhecimento de Transporte de Cargas, 55 - NF-e e 65 - NFC-e

Serão selecionados Lançamentos Fiscais de Entrada e Saída que possuam em suas parcelas Naturezas de Operação não Fiscal e o Tributo ISS com suas devidas informações.

B025B025

**Detalhamento por Combinação de Alíquota e item da Lista de serviços da LC 116/2003**

Este registro será gerado com base nas informações constantes nos itens dos Lançamentos Fiscais. Para a correta geração deste registro as informações abaixo devem constar no cadastro do Produto/Serviço:

* Tipo: Deve ser Serviço
* Último nível deve estar habilitado
* Anexo Dados Fiscais do Produto: Tipo de Tributação: Tributação pelo ISS
  + Código do Serviço Federal: Deve constar um código válido extraído da LC 116/2003 (Tabela 4.6.3 do SPED)
  + Situação da Mercadoria: Deve ser Serviços
* No item do Lançamento Fiscal
  + O Tributo ISSQN (TIPOTRIBFISC ISS) deve existir no ítem
* As informações de Município, Estado de Prestação de Serviço e Código do Serviço devem estar corretamente preenchidos.
B030B030

**Nota Fiscal de Serviços Simplificada (Modelo 3A)**

Será gravado neste registro as parcelas com serviços sujeitas a ISS cujo modelo de documento seja 3A.

Serão selecionados Lançamentos Fiscais de Saída que possuam no item o Tributo ISS devidamente preenchido. Este registro será agrupado caso os Lançamentos tenham Serie e Data de emissão iguais, ao agrupar será preenchido o menor número de lançamento no campo número inicial (NUM\_DOC\_INI) e o maior número no campo número final (NUM\_DOC\_FIN) mesmo que a numeração não seja sequencial.

B035B035

**Detalhamento por combinação de alíquota de item da lista de serviço da LC 116/2003**

Este registro será gerado com base nas informações constantes nos itens dos Lançamentos Fiscais selecionados para o Registro B030. Para a correta geração as informações abaixo devem constar no cadastro do Produto/Serviço:

* Tipo: Deve ser Serviço
* Último nível deve estar habilitado
* Anexo Dados Fiscais do Produto: Tipo de Tributação: Tributação pelo ISS
  + Código do Serviço Federal: Deve constar um código válido extraído da LC 116/2003 (Tabela 4.6.3 do SPED)
  + Situação da Mercadoria: Deve ser Serviços
* No item do Lançamento Fiscal
  + O Tributo ISSQN (TIPOTRIBFISC ISS) deve existir no ítem
  + Este registro não considera ISS retido.

O registro será agrupado se os campos Alíquota do ISS (ALIQ\_ISS) e código do Serviço foram iguais(COD\_SERV).

Este registro não será gerado para Lançamentos Fiscais cancelados.

B350B350

**Serviços prestados por instituições financeiras**

Este registro não será gerado.

B420B420

**Totalização dos valores de serviços prestados por combinação de alíquota e item da lista de serviços da LC 116/2003**

Este registro é um resumo dos registros B020, B030, B350 (somente as prestações de serviço) totalizados por Alíquota do tributo ISS e Código de Serviço da LC 116/2003. Aplicam-se a eles todos os filtros aplicados aos registros citados.

B440B440

**Totalização dos valores retidos**

Este registro será gerado com base nos valores retidos de ISSQN nas entradas e saídas. Será totalizado por Tipo de Operação (Aquisição ou Prestação) e por Participante.

No campo VL\_CONT\_RT serão totalizados os valores contábeis dos Lançamentos Fiscais combinados por tipo de operação e Participante sem considerar o tipo de recolhimento.

No campo VL\_BCISS\_RT serão totalizados somente a Base de Cálculo do Tributo que foi retido na Aquisição ou Prestação (Tipo de recolhimento: Retido e Retido Deduzido) de serviço pelo declarante.

No campo VL\_ISS\_RT serão totalizados somente os valores retidos de ISS.

B460B460

**Deduções do ISS**

Este registro será gerado conforme lançamento de Outros Débitos\Créditos do Tipo Dedução para o Tributo do Tipo ISS.

Informações sobre o processo devem ser preenchidas no Cadastro de Processos Judiciais e Administrativos.

No campo IND\_DED (Indicador do tipo de dedução) será gerado com os valores:

"0 - Compensação do ISSQN Calculado a Maior" - para lançamentos de outros Débitos/Créditos do tipo Dedução e subtipo Compensação de Crédito que referenciam um lançamento a que esteja associado tributo do tipo ISS.

"2 – Decisão Administrativa ou Judicial” - Lançamento de Outros Débitos/Créditos do tipo Dedução que tenha Processo associado.

"9 - Outros" - Caso oposto às condições acima.

No campo VL\_DED (Valor da dedução) será gerado conforme campo de dedução do lançamento de Outros Débitos\Crédito.

No campo NUM\_PROC (Número do processo ao qual o ajuste está vinculado, se houver) será gerado com o número do processo associado ao Lançamento de Outros Débitos/Créditos

No campo IND\_PROC (Indicador da origem do processo) gerado com o tipo do processo associado ao lançamento.

No campo COD\_INF\_OBS (Código da observação do lançamento fiscal) gerado conforme campo 02 do Registro 0460.

No campo IND\_OBR (Indicador da obrigação onde será aplicada a dedução) gerado conforme campo "Indicador de origem/aplicação das deduções".

0 - ISS Próprio;

1 - ISS Substituto (devido pelas aquisições de serviços do declarante).

2 - ISS Uniprofissionais. (Gerar sob demanda)

B470B470

**Apuração do ISS**

Informações sobre ISSQN a recolher no período.

No campo VL\_CONT (Valor total referente às prestações de serviço do período) irá receber o somatório do campo 02 "VL\_CONT" dos registros B420.

No campo VL\_MAT\_TERC (Valor total do material fornecido por terceiros na prestação do serviço) soma do campo 13 "VL\_MAT\_TERC" de todos os regstros B020 "Pai".

No campo VL\_MAT\_PROP (Valor do material próprio utilizado na prestação do serviço) não será gerado, conforme Rotina do Ato Cotepe.

No campo VL\_SUB (Valor total das subempreitadas) soma do campo 14“VL\_SUB”, de todos os Registros B020 “Pai”.

No campo VL\_ISNT (Valor total das operações isentas ou não-tributadas pelo ISS), irá receber o valor do campo "VL\_ISNT\_ISS" dos registros B420.

No campo VL\_DED\_BC (Valor total das deduções da base de cálculo) o registro será calculado desta forma VL\_MAT\_TERC + VL\_MAT\_PROP + VL\_SUB + VL\_ISNT.

No campo VL\_BC\_ISS (Valor total da base de cálculo do ISS) gerado conforme Campo 03 “VL\_BC\_ISS” dos registros B420.

No campo VL\_BC\_ISS\_RT (Valor total da base de cálculo de retenção do ISS referente às prestações do declarante) gerado conforme campo 05 “VL\_BC\_ISS\_RT” dos registros B440 (referentes às prestações do declarante, ou seja, com o campo IND\_OPER = “1”).

No campo VL\_ ISS (Valor total do ISS destacado) gerado conforme campo 06 “VL\_ ISS” dos registros B420.

No campo VL\_ISS\_RT (Valor total do ISS retido pelo tomador nas prestações do declarante) gerado conforme campo 06 “VL\_ISS\_RT” dos registros B440 (referentes às prestações do Declarante, ou seja, com o campo IND\_OPER = “1”)

No campo VL\_DED (Valor total das deduções do ISS próprio) gerado conforme campo 03 “VL\_DED” dos registros B460 referentes ao ISS Próprio (ou seja, com o campo IND\_OBR= “0”).

No campo VL\_ ISS\_REC (Valor total apurado do ISS próprio a recolher) o registro será calculado desta forma VL\_ ISS - VL\_ISS\_RT - VL\_ ISS\_REC, Se o resultado for maior ou igual a zero, caso o resultado for negativo, o mesmo será gerado como zero.

No campo VL\_ ISS\_ST (Valor total do ISS substituto a recolher pelas aquisições do tomador) o registro será calculado com a diferença entre o somatório dos valores informados no campo “VL\_ISS\_RT” dos registros B440 (com o campo IND\_OPER = “0”) e o somatório dos valores informados nos campos “VL\_DED” dos registros B460 (com o Campo IND\_OBR= “1”), se o resultado for maior ou igual a zero, caso o resultado for negativo, o mesmo será gerado como zero.

No campo VL\_ ISS\_REC\_UNI (Valor do ISS próprio a recolher pela Sociedade Uniprofissional) será gerado sob demanda.

B500B500

**Apuração do ISS Sociedade UNIPROFISSIONAL**

Este registro não será gerado.

B510B510

**UNIPROFISSIONAL - Empregados e Sócios**

Este registro não será gerado.
