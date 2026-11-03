---
content_hash: d6828bacd7b4031440df522ddb6802a7f06b6eb3a9c49a6ba346ac33d59fa6c9
fetched_at: '2026-06-29T00:06:23.590217+00:00'
page_id: '224106454'
product: rm
source: tdn-rm
title: ER_Apuração ICMS Difal_FCP e Geração do Sped Fiscal (EC 87_15)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224106454
version: 17
---

# Apuração ICMS Difal\_FCP e Geração do Sped Fiscal (EC 87\_15)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *Linha RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Fiscal* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Sped Fiscal* | Sped Fiscal - Geração do Arquivo |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Período de Apuração ICMS* | *Encerramento Período de Apuração* | | *Sped Fiscal* | *Geração de Arquivo* | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Chamados Relacionados** | TTLDQQ |
| **Requisito (ISSUE):** | FIS000212 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** | DPERIODO, DPERIODODIFAL, DLAF, DITEM |
| **Sistema(s) Operacional(is):** |  |
| **Versões/Release:** | *11.82.43 e 12.1.10* |
| **Versão Corrigida:** | *11.82.42, 11.82.43, 12.1.8, 12.1.9, 12.1.10* |
| **Versão Expedida:** | *11.82.43 e 12.1.10* |

# **Legislação**

[Link da Legislação](http://pesquisa.in.gov.br/imprensa/jsp/visualiza/index.jsp?jornal=1&pagina=20&data=23/10/2015)

**Apuração**

A apuração do valor do Diferencial de Alíquota referente as vendas destinadas a "**não contribuinte e consumidor final**" deve ser feita em separado das demais apurações.   
 Nesta apuração devem ser selecionados lançamentos fiscais com as seguintes regras:

* Lançamentos de Saída interestadual e
* Lançamento de Entrada de devolução de venda
* Que estejam com o Campo "**Operação Consumidor Final**" habilitado
* Que a Regra do ICMS da Natureza Fiscal associada ao lançamento possua o Tipo de Tributação "**Diferencial de Alíquota**".
* Não serão selecionados lançamentos fiscais **Cancelados** ou **Estornados**

**O Recolhimento**

A obrigação tributária de recolhimento do ICMS relativo ao Consumidor Final cabe ao contribuinte remetente do bem ou prestador do serviço, inclusive quando optante pelo Simples Nacional.  
 O Valor do Diferencial de Alíquota devido à UF de destino, bem como o valor do Fundo de Combate à Pobreza - FCP, se houver, será recolhido por meio de GNRE ou outro documento de arrecadação, de acordo com a legislação da UF de destino.

O Recolhimento do valor do Diferencial de Alíquota pode ser:

1. **Por Operação**: Aplica-se aos contribuintes não inscritos na UF de localização do destinatário, que devem recolher o Diferencial de Alíquota na saída do bem ou no início da prestação, em relação a cada operação ou prestação. O recolhimento por OPERAÇÃO é pela emissão da guia "GNRE" ou guia interna e recolhimento antes da saída da mercadoria ao Estado de Destino, devendo ser vinculada na guia o nº da NF-e emitida, e após recolhida deverá acompanhar o transporte da mercadoria até o destino final.
2. **Por Apuração**: Destina-se ao os contribuintes inscritos na UF de localização do destinatário e que possuem inscrição como contribuinte substituto. Os Estados e o Distrito Federal, permitem aos estabelecimentos sediados em outras Unidades da Federação, que realizando o cadastro para Inscrição Estadual, recolher via apuração do ICMS até o dia 15 do mês subsequente conforme orientação dos Estados.

## Implementações Necessárias - Gestão Fiscal

**Escrituração**

Será necessário alteração nas regras do processo de escrituração para habilitar o calculo do FECP e ICMS Partilhado de movimento de entrada:

* Serão considerados os movimentos de Entrada de Outros Estados
* Flag Tipo de Devolução da Natureza igual a Devolução
* Flag Operação Consumidor Final marcado no movimento
* Flag Operação Tributária da Regra de ICMS marcado como Diferencial de Alíquota

**Lançamento Fiscal**

Habilitar para os Lançamentos de Entrada\Devolução de Venda o cálculo dos campos:

* % UF Destinatário
* Valor Partilha Destinatário
* Valor Partilha Remente
* %FCP
* Valor ICMS FCP UF Destinatário

Estes campos devem aparecer somente para os lançamentos de Entrada que possuírem **Natureza de Devolução** (2.xxx) e com o Tipo de Tributação "**Diferencial de Alíquota**".

**Período de Apuração do ICMS**

No Período de Apuração do ICMS foi criada a pasta "**Valores Diferencial de Alíquota**" contendo os seguintes campos:

* UF
* Valor Débito Diferencial de Alíquota
* Outros Débitos
* Estorno de Crédito
* Crédito Diferencial de Alíquota
* Outros Créditos
* Estorno de Débito
* Valor Deduções
* Valor Débitos Especiais
* Valor FECP Saídas
* Valor FECP Entradas
* Saldo Credor/Devedor Anterior
* Saldo Credor/Devedor antes das Deduções
* Saldo Credor/Devedor

No encerramento do Período de Apuração do ICMS, o sistema irá preencher a nova pasta, incluindo um registro para cada UF movimentada pelas operações, com as regras abaixo. Afetam esse processo:

1. Lançamentos de Saída interestadual (CFOP 6.xxx) e
2. Lançamento de Entrada (CFOP 2.xxx) que sejam de devolução de venda (Cadastro de Naturezas, pasta Outros Dados, campo Tipo de Devolução = "**Devolução**")
3. Que estejam com o flag "**Operação destinada a Consumidor Final**" habilitado (Lançamento Fiscal | Guia Informações Adicionais | Outros) e
4. Que a Regra do ICMS da Natureza Fiscal associada ao lançamento possua a Operação Tributária "**Diferencial de Alíquota**".
5. Fornecedor "Não Contribuinte do ICMS".

OBS.: As regras 3,4 e 5 se aplicam tanto às saídas como às entradas.

Os campos de cada registro inserido pelo processo de encerramento serão preenchidos considerando as regras que seguem:

* **UF**: Será gerado um registro para cada UF que será preenchida com a UF da Filial e com as UF's de cada Cliente/Fornecedor associado aos lançamentos de entrada e saída que atendam às condições citadas logo acima.
* **Valor Débito Diferencial de Alíquota**: A regra de preenchimento deste campo depende da UF:
  + UF da Filial (Remente): Será preenchido com o total do campo "**Valor Partilha UF Remetente**" informado nos itens dos Lançamentos de Saída.
  + Demais UF's (Destinatário): Será preenchido com o total do campo "**Valor Partilha UF Destinatário**" informado nos itens dos Lançamentos de Saída.
* **Outros Débitos**: Total dos lançamentos de Outros Débitos\Créditos com o Tipo "**Outros Débitos**" e o Sub Tipo "**DIFAL – Origem\Destino**" associados à UF que está sendo processada.
* **Estorno de Crédito**: Total dos Lançamentos de Outros Débitos\Créditos com o Tipo "**Estorno de Crédito**" e o Sub Tipo "**DIFAL – Origem\Destino**" associados à UF que está sendo processada.
* **Crédito Diferencial de Alíquota**: A regra de preenchimento deste campo depende da UF:
  + UF da Filial (Destinatário na devolução): Será preenchido com o total do campo "**Valor Partilha UF Destinatário**" informado nos itens dos Lançamentos de Entrada.
  + Demais UF's (Remetente na Devolução é o Cliente/Fornecedor): Será preenchido com o total do campo "**Valor Partilha UF Remetente**" informado nos itens dos Lançamentos de Entrada.
* **Outros Créditos**: Total dos lançamentos de Outros Débitos\Créditos com o Tipo "**Outros Créditos**" e o Sub Tipo "**DIFAL – Origem\Destino**".
* **Estorno de Débito**: Total dos lançamentos de Outros Débitos\Créditos com o Tipo "**Estorno de Crédito**" e o Sub Tipo "**DIFAL – Origem\Destino**".
* **Valor Deduções**: Total dos lançamentos de Outros Débitos\Créditos com o Tipo "**Dedução**" e o Sub Tipo "**DIFAL – Origem\Destino**".
* **Valor Débitos Especiais**: Total dos lançamentos de Outros Débitos\Créditos com o Tipo "**Débitos Especiais**" e o Sub Tipo "**DIFAL – Origem\Destino**".
* **Valor FECP Saídas**: Total do campo "**Valor ICMS FECP Item**" informado nos itens dos Lançamentos de Saída.
* **Valor FECP Entradas**: Total do campo "**Valor ICMS FECP Item**" informado nos itens dos Lançamentos de Entrada.
* **Saldo Credor/Devedor Anterior**: A regra de preenchimento deste campo depende da UF:
  + UF da Filial: Esse campo sempre será preenchido com 0 (zero) porque o valor do saldo credor/devedor apurado no período de apuração anterior foi processado junto com a apuração do ICMS próprio; os dois valores são pagos juntos.
  + Demais UF's: Será preenchido com o valor do campo "**Saldo Credor/Devedor**" do período de apuração anterior ao que está sendo encerrado.
* **Saldo Credor/Devedor antes das Deduções**: Esse campo é calculado pelo sistema. Corresponde à fórmula: (Crédito Diferencial de Alíquota + Outros Créditos + Estorno de Débito) - (Valor Débito Diferencial de Alíquota + Outros Débitos + Estorno de Crédito).
* **Saldo Credor/Devedor**: Esse campo é calculado pelo sistema. Corresponde à fórmula: (Saldo Credor/Devedor antes das Deduções – Valor Deduções).

**Rotina do Sped Fiscal**

Registros novos que foram implementados:

* Registro C101 na tabela 2.6.1.2 – Bloco C

* Registro D101 na tabela 2.6.1.3 – Bloco D:

* Registros E300, E310, E311, E312, E313 e E316 na tabela 2.6.1.4 – Bloco E.

**Mapeamento dos Campos**

REGISTRO 0015: DADOS DO CONTRIBUINTE SUBSTITUTO OU RESPONSÁVEL PELO ICMS DESTINO

|  |  |  |
| --- | --- | --- |
| Campo | Descrição | ORIGEM DOS DADOS |
| REG | Texto fixo contendo "0015" |  |
| UF\_ST | Sigla da unidade da federação do contribuinte substituído ou unidade de federação do consumidor final não contribuinte - ICMS Destino EC 87/15. | Gerado conforme o cadastro da Filial – Sub Pasta Inscrição Estadual ST |
| IE\_ST | Inscrição Estadual do contribuinte substituto na unidade da federação do contribuinte substituído ou unidade de federação do consumidor final não contribuinte – ICMS Destino EC 87/15. | Gerado conforme o cadastro da Filial – Sub Pasta Inscrição Estadual ST |

REGISTRO C101: INFORMAÇÃO COMPLEMENTAR DOS DOCUMENTOS FISCAIS QUANDO DAS OPERAÇÕES INTERESTADUAIS DESTINADAS A CONSUMIDOR FINAL NÃO CONTRIBUINTE EC 87/15 (CÓDIGO 55)

Este Registro deve ser gerado para os Lançamentos de Saída e de Entrada Interestaduais com Consumidor Final e cujo cliente é Não Contribuinte, exceto os Lançamentos Extemporâneo e Complementar Extemporâneo.

|  |  |  |
| --- | --- | --- |
| Campo | Descrição | ORIGEM DOS DADOS |
| REG | Texto fixo contendo "C101" |  |
| VL\_FCP\_UF\_DEST | Valor total relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino | Gerar Conforme o Campo FCP dos Itens dos Lançamentos Fiscais |
| VL\_ICMS\_UF\_DEST | Valor total do ICMS Interestadual para a UF de destino | Gerar conforme o Campo Valor Partilha UF Destinatário do Item do Lançamento Fiscal |
| VL\_ICMS\_UF\_REM | Valor total do ICMS Interestadual para a UF do remetente | Gerar conforme o Campo Valor Partilha UF Remetente do Item do Lançamento Fiscal |

REGISTRO D101: INFORMAÇÃO COMPLEMENTAR DOS DOCUMENTOS FISCAIS QUANDO DAS PRESTAÇÕES INTERESTADUAIS DESTINADAS A CONSUMIDOR FINAL NÃO CONTRIBUINTE EC 87/15 (CÓDIGO 57).

Este Registro deve ser gerado para os Lançamentos de Saída e de Entrada Interestaduais com Consumidor Final e cujo cliente é Não Contribuinte, exceto os Lançamentos Extemporâneo e Complementar Extemporâneo.

|  |  |  |
| --- | --- | --- |
| Campo | Descrição | ORIGEM DOS DADOS |
| REG | Texto fixo contendo "D101" |  |
| VL\_FCP\_UF\_DEST | Valor total relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino | Gerar Conforme o Campo FCP dos Itens dos Lançamentos Fiscais |
| VL\_ICMS\_UF\_DEST | Valor total do ICMS Interestadual para a UF de destino | Gerar conforme o Campo Valor Partilha UF Destinatário do Item do Lançamento Fiscal |
| VL\_ICMS\_UF\_REM | Valor total do ICMS Interestadual para a UF do remetente | Gerar conforme o Campo Valor Partilha UF Remetente do Item do Lançamento Fiscal |

REGISTRO E300: PERÍODO DE APURAÇÃO DO ICMS DIFERENCIAL DE ALÍQUOTA – UF ORIGEM/DESTINO EC 87/15

Deve ser gerado um registro para cada UF processada pelo encerramento do Período de Apuração e que foi gravado na pasta "**Valores Diferencial de Alíquota**".

|  |  |  |
| --- | --- | --- |
| Campo | Descrição | ORIGEM DOS DADOS |
| REG | Texto fixo contendo "E300" |  |
| UF | Sigla da unidade da federação a que se refere a apuração do ICMS Diferencial de Alíquota da UF de Origem/Destino | Campo criado na pasta "**Valores Diferencial de Alíquota**" do Período de Apuração |
| DT\_INI | Data Inicial a que a apuração se refere | Gerado com a Data Início do Período de Apuração do Tributo ICMS |
| DT\_FIN | Data Final a que a apuração se refere | Gerado com a Data Final do Período de Apuração do Tributo ICMS |

REGISTRO E310: APURAÇÃO DO ICMS DIFERENCIAL DE ALÍQUOTA – UF ORIGEM/DESTINO EC 87/15

Registro gerado conforme as informações do Período de Apuração, pasta "**Valores Diferencial de Alíquota**".

|  |  |  |
| --- | --- | --- |
| Campo | Descrição | ORIGEM DOS DADOS |
| REG | Texto fixo contendo "E310" |  |
| IND\_MOV\_DIFAL | Indicador de movimento:   0 – Sem operações com ICMS Diferencial de Alíquota da UF de Origem/Destino   1 – Com operações de ICMS Diferencial de Alíquota da UF de Origem/Destino | Gerado conforme pasta "**Valores Diferencial de Alíquota**". |
| VL\_SLD\_CRED\_ANT\_DIFAL | Valor do "Saldo credor de período anterior – ICMS Diferencial de Alíquota da UF de Origem/Destino" | Gerado conforme campo no Período de Apuração "**Saldo Credor/Devedor Anterior**" – pasta nova "**Valores Diferencial de Alíquota**" |
| VL\_TOT\_DEBITOS\_DIFAL | Valor total dos débitos por "Saídas e prestações com débito do ICMS referente ao diferencial de alíquota devido à UF do Remetente/Destinatário" | Gerado conforme campo no Período de Apuração "**Valor Débito Diferencial de Alíquota**"– pasta nova "**Valores Diferencial de Alíquota**" |
| VL\_OUT\_DEB\_DIFAL | Valor Total dos ajustes "Outros débitos ICMS Diferencial de Alíquota da UF de Origem/Destino" " e "Estorno de créditos ICMS Diferencial de Alíquota da UF de Origem/Destino" | Gerado conforme campo no Período de Apuração "**Outros Débitos**" e "**Estorno de Crédito**" - pasta nova "**Valores Diferencial de Alíquota**" |
| VL\_TOT\_DEB\_FCP | Valor total dos débitos FCP por "Saídas e prestações" | Gerado conforme campo no Período de Apuração "**Valor FECP Saídas**"– pasta nova "**Valores Diferencial de Alíquota**" |
| VL\_TOT\_CREDITOS\_DIFAL | Valor total dos créditos do ICMS referente ao diferencial de alíquota devido à UF dos Remetente/ Destinatário | Gerado conforme campo no Período de Apuração "**Crédito Diferencial de Alíquota**"– pasta nova "**Valores Diferencial de Alíquota**" |
| VL\_TOT\_CRED\_FCP | Valor total dos créditos FCP por Entradas | Gerado conforme campo no Período de Apuração "**Valor FECP Entradas**"– pasta nova "**Valores Diferencial de Alíquota**" |
| VL\_OUT\_CRED\_DIFAL | Valor total de Ajustes "Outros créditos ICMS Diferencial de Alíquota da UF de Origem/Destino" e "Estorno de débitos ICMS Diferencial de Alíquota da UF de Origem/Destino" | Gerado conforme campo no Período de Apuração "**Outros Créditos**" e "**Estorno de Débito**" - pasta nova "**Valores Diferencial de Alíquota**" |
| VL\_SLD\_DEV\_ANT\_DIFAL | Valor total de Saldo devedor ICMS Diferencial de Alíquota da UF de Origem/Destino antes das deduções | Gerado conforme campo no Período de Apuração "**Saldo Credor/Devedor antes das Deduções**" - pasta nova "**Valores Diferencial de Alíquota**". |
| VL\_DEDUÇÕES\_DIFAL | Valor total dos ajustes "Deduções ICMS Diferencial de Alíquota da UF de Origem/Destino" | Gerado conforme campo no Período de Apuração "**Valor Deduções**" - pasta nova "**Valores Diferencial de Alíquota**". |
| VL\_RECOL | Valor recolhido ou a recolher referente a FCP e Imposto do Diferencial de Alíquota da UF de Origem/Destino (10-11) | Gerado conforme campo no Período de Apuração "**Saldo Credor/Devedor**" SE NEGATIVO - pasta nova "**Valores Diferencial de Alíquota**". |
| VL\_SLD\_CRED\_TRANSPORTAR | Saldo credor a transportar para o período seguinte referente a FCP e Imposto do Diferencial de Alíquota da UF de Origem/Destino | Gerado conforme campo no Período de Apuração "**Saldo Credor/Devedor**" SE POSITIVO - pasta nova "**Valores Diferencial de Alíquota**". |
| DEB\_ESP\_DIFAL | Valores recolhidos ou a recolher, extra-apuração. | Gerado conforme campo no Período de Apuração "**Valor Débitos Especiais**" - pasta nova "**Valores Diferencial de Alíquota**". |

REGISTRO E311: AJUSTE/BENEFÍCIO/INCENTIVO DA APURAÇÃO DO ICMS DIFERENCIAL DE ALÍQUOTA UF ORIGEM/DESTINO EC 87/15

Neste Registro será considerado os lançamentos de Outros Débitos\Créditos que o Sub Tipo é igual a "DIFAL – Origem\Destino".

|  |  |  |
| --- | --- | --- |
| Campo | Descrição | ORIGEM DOS DADOS |
| REG | Texto fixo contendo "E311" |  |
| COD\_AJ\_APUR | Código do ajuste da apuração e dedução, conforme a Tabela indicada no item 5.1.1 | Gerado conforme o Campo Código de Ajuste do Lançamento de Outros Débitos\Créditos |
| DESCR\_COMPL\_AJ | Descrição complementar do ajuste da apuração | Gerado conforme o campo Histórico do Lançamento de Outros Débitos\Créditos. |
| VL\_AJ\_APUR | Valor do ajuste da apuração | Gerado conforme o campo valor do Lançamento de Outros Débitos\Créditos |

REGISTRO E312: INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO ICMS DIFERENCIAL DE ALÍQUOTA UF ORIGEM/DESTINO EC 87/15

Neste Registro será considerado os lançamentos de Outros Débitos\Créditos que o Sub Tipo é igual a "DIFAL – Origem\Destino", referente ao Número de Processo associado ao lançamento.

|  |  |  |
| --- | --- | --- |
| Campo | Descrição | ORIGEM DOS DADOS |
| REG | Texto fixo contendo "E312" |  |
| NUM\_DA | Número do documento de arrecadação estadual, se houver |  |
| NUM\_PROC | Número do processo ao qual o ajuste está vinculado, se houver | Gerado conforme o Campo Processo Judicial\Administrativo informado no Lançamento de Outros Débitos\Créditos |
| IND\_PROC | Indicador da origem do processo:   0- Sefaz;   1- Justiça Federal;   2- Justiça Estadual;   9- Outros | Gerado conforme o cadastro do processo associado ao lançamento de Outros Débitos\Créditos |
| PROC | Descrição resumida do processo que embasou o lançamento | Gerado conforme o cadastro do processo associado ao lançamento de Outros Débitos\Créditos |
| TXT\_COMPL | Descrição complementar | Gerado conforme o campo Observação do lançamento de Outros Débitos\Créditos |

REGISTRO E313: INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO ICMS DIFERENCIAL DE ALÍQUOTA UF ORIGEM/DESTINO EC 87/15 IDENTIFICAÇÃO DOS DOCUMENTOS FISCAIS.

Registro gerado quando, nos lançamentos de Outros Débitos\Créditos, existir Lançamento Fiscal informado na Pasta Referência.

|  |  |  |
| --- | --- | --- |
| Campo | Descrição | ORIGEM DOS DADOS |
| REG | Texto fixo contendo "E313" |  |
| COD\_PART | Código do participante (campo 02 do Registro 0150) | Gerado conforme campo do Cli\For do Lançamento Fiscal associado (ou Referenciado). |
| COD\_MOD | Código do modelo do documento fiscal, conforme a Tabela 4.1.1 | Gerado conforme campo do Espécie do Lançamento Fiscal associado (ou Referenciado). |
| SER | Série do documento fiscal | Gerado conforme campo Série do Lançamento Fiscal associado (ou Referenciado). |
| SUB | Subsérie do documento fiscal | Gerado conforme campo Sub Série do Lançamento Fiscal associado (ou Referenciado). |
| NUM\_DOC | Número do documento fiscal | Gerado conforme campo Número do Documento do Lançamento Fiscal associado (ou Referenciado). |
| CHV\_DOCe | Chave do Documento Eletrônico | Gerado conforme campo chave de acesso do Lançamento Fiscal associado (ou Referenciado). |
| DT\_DOC | Data da emissão do documento fiscal | Gerado conforme campo Data Emissão do lançamento Fiscal associado (ou Referenciado). |
| COD\_ITEM | Código do item (campo 02 do Registro 0200) | Não será gerado |
| VL\_AJ\_ITEM | Valor do ajuste para a operação/item | Gerado conforme a Tabela DLDCNF campo Valor Total |

REGISTRO E316: OBRIGAÇÕES DO ICMS RECOLHIDO OU A RECOLHER – DIFERENCIAL DE ALÍQUOTA UF ORIGEM/DESTINO EC 87/15.

Este Registro é gerado com as informações da Guia de Recolhimento gerado no Período de Apuração.

|  |  |  |
| --- | --- | --- |
| Campo | Descrição | ORIGEM DOS DADOS |
| REG | Texto fixo contendo "E316" |  |
| COD\_OR | Código da obrigação recolhida ou a recolher, conforme a Tabela 5.4 | DGUIAPERIODO.CODIGOOBRIGACAO |
| VL\_OR | Valor da obrigação recolhida ou a recolher | DGUIAPERIODO.VALORGNR |
| DT\_VCTO | Data de vencimento da obrigação | DGUIAPERIODO.DATAVENC |
| COD\_REC | Código de receita referente à obrigação, próprio da   unidade da federação da origem/destino, conforme   legislação estadual. | DGUIAPERIODO.CODRECEITA |
| NUM\_PROC | Número do processo ou auto de infração ao qual a   obrigação está vinculada, se houver | DPROCESSOJUDICIAL.NUMERO |
| IND\_PROC | Indicador da origem do processo:   0- SEFAZ;   1- Justiça Federal;   2- Justiça Estadual;   9- Outros | DPROCESSOJUDICIAL.TIPO |
| PROC | Descrição resumida do processo que embasou o   lançamento | DPROCESSOJUDICIAL.DESCRICAO |
| TXT\_COMPL | Descrição complementar das obrigações recolhidas ou a   recolher | DGUIAPERIODO.OBSERVACAO |
| MES\_REF\* | Informe o mês de referência no formato "mmaaaa" | Mês e ano do período de apuração |

\_GoBack
