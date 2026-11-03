---
article_id: 1500012630022
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: c97d805c71cb3d40240c23b61bd08afc174bdf177afbbd7e22071df7c7166b23
fetched_at: '2026-06-28T22:40:48.907256+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001- ECF leiaute
  7 alterações
type: support-article
updated_at: '2021-06-15T19:47:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012630022-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-leiaute-7-altera%C3%A7%C3%B5es
---

**Dúvida**CTBS001- ECF leiaute 7 alterações.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS Contabilidade Gerencial- Todas as versões  
  
**Solução**

A Receita Federal disponibilizou um documento com as alterações do leiaute 7:

* Inclusão dos registros:

Inclusão de registros:  
X305 - Tipos de Ajustes do Preço Parâmetro da Exportação - Validação: OC (Se 0020. X300.AJ\_PAR = “S”)  - Relação: [0;N]

X325 - Tipos de Ajustes do Preço Parâmetro da Importação - Validação: OC (Se 0020. X320.AJ\_PAR = “S”) - Relação: [0;N]

[Como gerar o registro X305 e/ou X325 no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402647905303-Cross-Segmento-Backoffice-Linha-Protheus-TAF-ECF-Como-gerar-o-registro-X305-e-X325)

* Exclusão dos registros:

Y540 - Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica

Y550 - Vendas a Comercial Exportadora com Fim Específico de Exportação

Y560 - Detalhamento das Exportações da Comercial Exportadora

Y580 - Doações a Campanhas Eleitorais

Y671 - Outras Informações

Y690 - Informações de Optantes pelo Paes

* *Alterações de registros:*

*Registro 0000 - Novas opções criadas nos campos:*

*Campo 03 - COD\_VER* - Para ano calendário = 2020 e situações especiais de 2021, o layout é o 0007 (texto fixo)

*Campo 06 - IND\_SIT\_INI\_PER* - Adicionado a opção "3 – Resultante de Mudança de Qualificação da Pessoa Jurídica."

*Campo 07 - SIT\_ESPECIAL* - Adicionado a opção "7 - Mudança de Qualificação da PJ". Esta opção será utilizada quando a empresa mudar a qualificação da PJ (Campo 06 do registro 0010). Neste cenário, será entregue 2 ECFs: a primeira com a qualificação anterior com a data final = a data do evento e outra ECF com a data inicial = a data posterior ao evento. O campo 06 do registro 0000 deve ser "3".

CTBS001 + ECF:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402719360407/mceclip0.png)

* Registro 0010 - Exclusão de campos:

Campo 04 - Opt. PAES foi excluído.

Com isso o campo 05 - Forma\_Trib passou a ser o campo 04. O layout 007 possui 13 campos e não mais 14 como o layout 006 exigia.

Obs. A partir do leiaute 7 o campo ficará desabilitado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019967281/mceclip0.png)

* Registro 0020 - Exclusão de campos:

Campo 14 - IND\_DOA\_ELEIT foi excluído

Campo 16 - IND\_VEND\_EXP foi excluído

Campo 19 - IND\_COM\_EXP foi excluído

O campo 15 passa a ser apresentado na posição 14 e assim sucessivamente. O layout deverá ter 30 posições no layout 007.

* Registro L300: Demonstração do Resultado Líquido no Período Fiscal: Alteração de descrição de conta. (Tabela CHA)

L300A – Conta 3.01.01.07.28 – Alteração da descrição para “Provisão para Perda de Estoque de Livros”

* Registro M010: Identificação da Conta na Parte B do e-Lalur e do e-Lacs: Alteração de descrição e criação de conta no plano padrão da Parte B.

Plano Padrão da Parte B:

Alteração de descrição: 2.110 - Incentivo Fiscal - Depreciação Acelerada Incentivada – SUDENE

Novo Código: 2.115 - Incentivo Fiscal - Depreciação Acelerada Incentivada – SUDAM

* Registro M300: Demonstração do Lucro Real – Lançamentos da Parte A do e-Lalur: Alteração de descrição de linhas e criação de linhas das tabelas dinâmicas. (Tabela CH8)

M300A:

Alteração de descrição de linhas de códigos 89 e 164: Outros ajustes decorrentes de modificação ou adoção de métodos e critérios contábeis por meio de atos administrativos, conforme estabelecido no parágrafo único do art. 58 da Lei nº 12.973, de 2014.

Alteração de descrição: 43 - Incentivo fiscal - depreciação acelerada incentivada – SUDENE

Novo código: 43.01 - Incentivo fiscal - depreciação acelerada incentivada – SUDAM

Alteração de descrição: 122 - Incentivo fiscal - depreciação acelerada incentivada – SUDENE

Novo código: 122.01 - Incentivo fiscal - depreciação acelerada incentivada – SUDAM

M300R:

Alteração de descrição de linhas de códigos 263 e 338: Outros ajustes decorrentes de modificação ou adoção de métodos e critérios contábeis por meio de atos administrativos, conforme estabelecido no parágrafo único do art. 58 da Lei nº 12.973, de 2014.

Alteração de descrição: 218 - Incentivo fiscal - depreciação acelerada incentivada – SUDENE

Novo código: 218.01 - Incentivo fiscal - depreciação acelerada incentivada – SUDAM

Alteração de descrição: 296 - Incentivo fiscal - depreciação acelerada incentivada – SUDENE

Novo código: 296.01 - Incentivo fiscal - depreciação acelerada incentivada – SUDAM

M300B:

Alteração de descrição de linhas de códigos 89 e 196: Outros ajustes decorrentes de modificação ou adoção de métodos e critérios contábeis por meio de atos administrativos, conforme estabelecido no parágrafo único do art. 58 da Lei nº 12.973, de 2014.

M300C:

Alteração de descrição de linhas de códigos 76 e 135: Outros ajustes decorrentes de modificação ou adoção de métodos e critérios contábeis por meio de atos administrativos, conforme estabelecido no parágrafo único do art. 58 da Lei nº 12.973, de 2014.

* Registro M350: Demonstração da Base de Cálculo da CSLL – Lançamentos da Parte A do e-Lacs: Alteração de descrição de linhas da tabela dinâmica. (Tabela CH8)

M350A:

Alteração de descrição de linhas de códigos 89 e 164: Outros ajustes decorrentes de modificação ou adoção de métodos e critérios contábeis por meio de atos administrativos, conforme estabelecido no parágrafo único do art. 58 da Lei nº 12.973, de 2014.

M350R:

Alteração de descrição de linhas de códigos 263 e 338: Outros ajustes decorrentes de modificação ou adoção de métodos e critérios contábeis por meio de atos administrativos, conforme estabelecido no parágrafo único do art. 58 da Lei nº 12.973, de 2014.

M350B:

Alteração de descrição de linhas de códigos 89 e 196: Outros ajustes decorrentes de modificação ou adoção de métodos e critérios contábeis por meio de atos administrativos, conforme estabelecido no parágrafo único do art. 58 da Lei nº 12.973, de 2014.

M350C:

Alteração de descrição de linhas de códigos 76 e 135: Outros ajustes decorrentes de modificação ou adoção de métodos e critérios contábeis por meio de atos administrativos, conforme estabelecido no parágrafo único do art. 58 da Lei nº 12.973, de 2014.

* Registro N600: Demonstração do Lucro da Exploração: Exclusão de linhas da tabela dinâmica.

Exclusão de linhas de códigos: 35.10 e 46.10

35.10 Ajuste positivo em função de diferenças apresentadas nos termos do art. 58 da Lei nº 12.973/2014

46.10 Ajuste negativo em função de diferenças apresentadas nos termos do art. 58 da Lei nº 12.973/2014

* Registro P230: Cálculo da Isenção e Redução do Lucro Presumido: Inclusão de linha na tabela dinâmica.

Inclusão de linha:

38 – Redução por reinvestimento

* Registro W200: Declaração País-a-País: Atualização de texto.

Observação: Os campos numéricos do registro W200 devem ser informados sem casas decimais.

* Registro X280: Atividades Incentivadas – PJ em Geral: Exclusão, atualização e inclusão de regras, inclusão de campos e atualização da numeração.

Campo 3, IND\_CONCEDENTE, Opções: 

AM: Sudam – Superintendência de Desenvolvimento da Amanzônia 

NE: Sudene – Superintendência de Desenvolvimento do Nordeste 

Ou: Outros

Inclusão de campos: 

Campo 8 CNPJ\_INCENTIVO

CNPJ do Estabelecimento com Isenção/Redução/Redução por Reinvestimento Informar o CNPJ completo do estabelecimento.

Campo 9 NCM\_INCENTIVO

Código NCN do Produto Sujeito à Isenção/Redução/Redução por Reinvestimento.

Campo 10 REC\_LIQ\_INCENTIVO

Valor da Receita Líquida Relativa à Isenção/Redução/Redução por Reinvestimento.

Campo 11 VL\_INCENTIVO

Valor da Isenção/Redução/Redução por Reinvestimento.

Rotina TAFA325, Inclusão manual no TAF,

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402694970007/mceclip0.png)

* Registro X300: Operações com o Exterior – Exportações (Entradas de Divisas): Inclusão de campos, atualização de números dos campos e inclusão de regras.

11 OPER\_PAR

Descrição: Operações parâmetro: informar que tipo de operações foram selecionadas para a apuração do preço parâmetro, dentre as seguintes opções (art. 30 da Instrução Normativa RFB nº 1.312/2012): A – Operações realizadas entre a própria pessoa jurídica e outros clientes não vinculados. B – Operações realizadas entre outro exportador nacional e clientes não vinculados.

Tipo: Caracter

Tamanho: 1

Opções: [A; B]

Obrigatório: Não

*12 DESC\_BENS\_PAR*

Descrição: Descrição dos bens, serviços ou direitos idênticos ou similares selecionados para o cálculo do preço parâmetro nas operações de exportação utilizadas e informadas no campo X300.OPER\_PAR.

Tipo: Caracter

Obrigatório: Não

*13 ID\_PARTE\_PAR*

Descrição: Identificação das partes envolvidas nas operações de exportação utilizadas e informadas no campo X300.OPER\_PAR (informar nome, razão social e número de identificação).

Tipo: Caracter

Obrigatório: Não

*14 TIP\_PAR*

Descrição: Informar o tipo do bem, serviço ou direito utilizado para fins de apuração do preço parâmetro, dentre as seguintes opções: I – Idêntico S – Similar

Tipo: Caracter

Tamanho: 1

Valores válidos: [I; S]

Obrigatório: Não

*15 DAT\_UTIL*

Descrição: Data da cotação utilizada para o cálculo do preço parâmetro, podendo ser a data da transação (conforme dispõe o § 2º-A, art 16, da Instrução Normativa RFB nº 1312/2012). Escolher entre as seguintes opções: T – Data da Transação O - Data da Transação (art. 34, §17) E – Data do Embarque Caso escolhida a opção "T - Data da Transação", deverá ser informado no campo 18 "X300.DAT\_TRANS" a data em que o preço foi negociado, conforme art. 34, §16 da Instrução Normativa RFB 1.312/2012. A opção "O - Data da Transação (art. 34, §17) deve ser escolhida caso o contribuinte utilize cotações ou índices relativos a uma média de dias, conforme dispõe o art. 34, §17 da Instrução Normativa RFB 1.312/2012.

Tipo: Caracter

Tamanho: 1

Valores válidos: [T; O; E]

Obrigatório: Não

*16 CRIT\_PAR*

Descrição: Descrever a metodologia e os critérios utilizados para fixação do preço, relatando, inclusive, a existência de diferenças entre a data em que a operação foi contratada e aquela em que o preço foi estabelecido. Na hipótese em que o preço seja fixado com base em cotações ou índices relativos a uma média de dias, descrever o critério utilizado.

Tamanho: Caracter

Obrigatório: Não

*17 DAT\_TRANS*

Descrição: Informar a data em que o preço foi negociado (conforme art. 34, §16 da Instrução Normativa RFB 1.312/2012).

Tipo: Numérico

Tamanho: 8

Obrigatório: Não

*18 DAT\_EMB*

Descrição: Data do Embarque: informar a data do embarque da commodity negociada.

Tipo: Numérico 8

Obrigatório: Não

*19 ID\_FONT\_COT*

Descrição: Identificação da fonte da cotação utilizada para a o cálculo do preço parâmetro informado em X300.VL\_PAR (indicação da bolsa de mercadorias e futuros utilizada, dentre as listadas no Anexo II da Instrução Normativa RFB nº 1.312/2012; ou da instituição de pesquisa setorial, dentre as listadas no Anexo III da referida Instrução Normativa; ou da utilização de preços definidos por agências ou órgãos reguladores, conforme art. 36, inciso II da Instrução Normativa RFB nº 1.312/2012).  
Lista completa disponível no manual em anexo

Tipo: Numérico

Tamanho: 3

Valores Válidos: [101; 102; 103; 104; 105; 106; 107; 108; 109; 110; 111; 112; 113; 114; 115; 116; 117; 118; 119; 120; 121; 122; 123; 201; 202; 203; 204; 205; 206; 207; 208; 209; 210; 211; 212; 213]

Obrigatório: Não

*20 AJ\_PAR*

Descrição: Informar se foram realizados ajustes ao preço parâmetro, conforme disposto nos arts. 22 a 25 e no art. 34, §§7º e 10 da Instrução Normativa RFB nº 1.312/2012, a depender do método aplicado. S = Sim N = Não

Tipo Caracter

Tamanho: 1

Valores válidos: [S,N]

Obrigatório: Não

*23 QTDE\_AJ*

Descrição: Quantidade ajustada: informar neste campo a quantidade de bens ou insumos da mesma natureza exportados para pessoas vinculadas sujeitos a ajuste de preços de transferência no ano-calendário. Ou seja, a quantidade de bens ou insumos para os quais se verificou a necessidade de ajuste de preços de transferência após a aplicação de um dos métodos previstos na legislação para o cálculo do preço parâmetro e sua comparação com o preço praticado. Obrigatório somente quando TIP\_EXP = Bens

Tipo: Numérico

Tamanho 19, decimal 6

Obrigatório: Não

*25 VALOR\_COT*

Descrição: Valor médio diário da cotação do bem ou direito exportado (art. 34 da Instrução Normativa RFB nº 1.312/2012) utilizada no cálculo do preço parâmetro, sem a inclusão de eventuais ajustes efetuados, em reais, e na mesma unidade de medida utilizada no preço praticado.

Tipo: Numérico

Tamanho: 19, Decimal 2

Obrigatório: N

*26 NUM\_DEC\_EXP*

Descrição: Número da Declaração Única de Exportação (DUE).

Tipo Caracter

Tamanho 50

Obrigatório: Não

*27 DAT\_ENT\_PREV*

Descrição: Data da entrega prevista.

Tipo: Numérico

Tamanho 8

Obrigatório: Não

* Registro X310: Operações com o Exterior – Contratantes das Exportações: Inclusão de código em campo.

*5 COND\_PES - Nova opção de campo:*  
04 – Considerada vinculada e Residente/Domiciliada em País com Tributação Favorecida ou que goze de regime fiscal privilegiado.

* Registro X320: Operações com o Exterior – Importações (Saída de Divisas): Inclusão de campos, atualização de números dos campos e inclusão de regras.

*10 COD\_INV*

Descrição: Código de Inventário do Insumo ou Produto Importado: Informar o código de inventário do insumo ou produto importado. Caso um determinado insumo ou produto tenha mais de um código, informar o mais relevante em termos quantitativos.

Tipo Caracter

Tamanho 60

Obrigatório: Não

*11 UTIL\_INS\_PROD*

Descrição: Utilização do Insumo ou Produto Importado: Descrição da utilização do insumo ou produto importado: informar a destinação do insumo ou produto importado, dentre as seguintes opções: RV – Revenda IN – Industrialização RI – Revenda e industrialização AI - Ativo Imobilizado

Tipo: Caracter

Tamanho 2

Valores válidos: [RV; IN; RI; AI]

Obrigatório Não

*12 OPER\_PAR*

Descrição: Operações para a Apuração do Preço Parâmetro: Informar que tipo de operações foram selecionadas para a apuração do preço parâmetro, dentre as seguintes opções (art. 8º, parágrafo único, da IN 1.312/2012): E – operações realizadas entre a mesma pessoa jurídica exportadora e pessoas jurídicas não vinculadas. C – operações realizadas entre o próprio contribuinte e pessoas jurídicas não vinculadas. T – operações realizadas entre terceiros não vinculados entre si.

Tipo Caracter

Tamanho 1

Valores válidos: [E; C; T]

Obrigatório: Não

*13 DESC\_PAR*

Descrição: Itens Selecionados para a Apuração do Preço Parâmetro: Descrição dos bens, serviços ou direitos idênticos ou similares selecionados para o cálculo do preço parâmetro e identificação das partes envolvidas nas operações utilizadas para a apuração do preço parâmetro (informar dados como nome, razão social, número de identificação e país de residência).

Tipo Caracter

Tamanho: Não

*14 ID\_PARTE\_PAR*

Descrição: Identificação das Partes Envolvidas: Identificação das partes envolvidas nas operações de exportação utilizadas e informadas no campo X320.OPER\_PAR (informar nome, razão social e número de identificação).

Tipo: Caracter

Obrigatório: Não

*15 TIP\_PAR*

Descrição: Tipo dos Itens para o Cálculo do Preço Parâmetro: Informar o tipo do bem, serviço ou direito utilizado para fins de apuração do preço parâmetro, dentre as seguintes opções: – Idêntico S – Similar

Tipo Caracter

Tamanho 1

Valores válidos: [I; S]

Obrigatório: Não

*16 DAT\_UTIL*

Descrição: Data Utilizada no Cálculo do Preço Parâmetro: Data da cotação utilizada para o cálculo do preço parâmetro, podendo ser a data da transação (conforme dispõe o § 2º-A, art 16, da Instrução Normativa RFB nº 1312/2012). Escolher entre as seguintes opções: T – Data da Transação - preço negociado (art. 34, §16) O - Data da Transação - média de dias evento (art. 34, §17) E – Data do Embarque Caso escolhida a opção "T - Data da Transação", deverá ser informado no campo 18 "DAT\_TRANS" a data em que o preço foi negociado, conforme art. 34, §16 da Instrução Normativa RFB nº 1.312/2012. A opção "O - Data da Transação (art. 34, §17) deve ser escolhida caso o contribuinte utilize cotações ou índices relativos a uma média de dias, conforme dispõe o art. 34, §17 da Instrução Normativa RFB nº 1.312/2012.

Tipo Caracter

Tamanho 1

Valores válidos: [T; O; E]

Obrigatório: Não

*17 CRIT\_PAR*

Descrição: Critérios para Determinação do Preço Parâmetro: Descrever a metodologia e os critérios utilizados para fixação do preço, relatando, inclusive, a existência de diferenças entre a data em que a operação foi contratada e aquela em que o preço foi estabelecido.

Tipo: Caracter

Obrigatório: Não

*18 DAT\_TRANS*

Descrição: Data da Transação: Informar a data em que o preço foi negociado (conforme art.16, §15 da Instrução Normativa RFB nº 1.312/2012).

Tipo Numérico

Tamanho 8

Obrigatório: Não

*19 DAT\_DUIMP*

Descrição: Data do registro da Declaração Única de Importação (DUIMP): Informar a data do registro da DUIMP da commodity negociada.

Tipo Numérico

Tamanho 8

Obrigatório: Não

*20 ID\_FONT\_COT*

Descrição: Fonte da Cotação: Descrição da fonte utilizada para a busca do preço parâmetro informado em VL\_PAR (indicação da bolsa de mercadorias e futuros utilizada, dentre as listadas no Anexo II da Instrução Normativa RFB nº 1.312/2012, ou da instituição de pesquisa setorial, dentre as listadas no Anexo III da referida Instrução Normativa).

Lista completa no manual da ECF

Tipo Numérico

Tamanho 3

Valores válidos: [101; 102; 103; 104; 105; 106; 107; 108; 109; 110; 111; 112; 113; 114; 115; 116; 117; 118; 119; 120; 121; 122; 123; 201; 202; 203; 204; 205; 206; 207; 208; 209; 210; 211; 212; 213; 999]

Obrigatório: Não

*21 AJ\_PAR*

Descrição: Ajustes do Preço Parâmetro: Ajustes do preço parâmetro: informar se foram realizados ajustes ao preço parâmetro, conforme disposto nos art. 9º; 10; 11, §1º; 15, §7; e 16, §9º da Instrução Normativa RFB nº 1.312/2012, a depender do método aplicado. S – Sim N - Não

Tipo Caracter

Tamanho 1

Valores válidos [S; N]

Obrigatório: Não

*24 QTDE\_AJ*

Descrição: Quantidade Ajustada: Informar neste campo a quantidade de bens ou insumos da mesma natureza importados de pessoas vinculadas sujeitos a ajuste de preços de transferência. Ou seja, a quantidade de bens ou insumos para os quais se verificou a necessidade de ajuste de preços de transferência após a aplicação de um dos métodos previstos na legislação para o cálculo do preço parâmetro e sua comparação com o preço praticado.

Tipo: Numérico

Tamanho 23, decimal 6

Obrigatório Não

*26 VALOR\_COT*

Descrição: Valor da Cotação: Valor médio diário da cotação do bem ou direito importado (art. 16 da IN RFB 1.312/2012) utilizada no cálculo do preço parâmetro, sem a inclusão de eventuais ajustes efetuados, em reais, e na unidade de medida utilizada no preço praticado.

Tipo Numérico

Tamanho 19 decimal 2

Obrigatório Não

*27 NUM\_DEC\_IMP*

Número da Declaração Única de Importação (DUIMP).  
Tipo Caracter

Tamanho 50

Obrigatório: Não

*28 DAT\_ENT\_PREV*

Data de Entrega Prevista.  
Tipo Numérico

Tamanho 8

Obrigatório Não

* Registro X330: Operações com o Exterior – Contratantes das Importações: Inclusão de código em campo.

*5 COND\_PES*

 04 – Considerada vinculada e Residente/Domiciliada em País com Tributação Favorecida ou que goze de regime fiscal privilegiado.

* Registro Y720: Informações de Períodos Anteriores: Atualização de texto, inclusão de campos e regras.

Este registro é obrigatório para todas as pessoas jurídicas apenas por ocasião da entrega da escrituração em atraso. A sua obrigatoriedade será verificada na hora da validação para a transmissão. Para as pessoas jurídicas tributadas pelo lucro presumido, arbitrado ou imunes/isentas, apenas devem ser preenchidos os campos Y720.INTIMACAO e Y720.INT.ATRASO (de acordo com a regra prevista para o campo). Para as pessoas jurídicas tributadas pelo lucro real e para as formas de tributação mistas, além dos campos anteriormente citados e suas regras de obrigatoriedade, os demais campos do registro também serão preenchidos.

*Inclusão de campos:*

*5 INTIMACAO*

Descrição: Houve termo de intimação pela RFB para a entrega desta ECF? S – Sim N – Não

Tipo Caracter

Tamanho: 1

Valores válidos: [S; N]

Obrigatório: Sim

*6 INT\_ATRASO*

Descrição: A transmissão desta ECF está dentro do prazo previsto na intimação? S – Sim N – Não

Tipo Caracter

Tamanho 1

Valores válidos: [S; N]

Obrigatório: Não

* Importante: O novo signatário tratado na ECD- Auditor, (940) não está disponível para a ECF.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019731922/mceclip1.png)

**Saiba mais:**

[Como atualizar a ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-e-como-realizar-a-atualiza%C3%A7%C3%A3o-da-ECF-2021-leiaute-7)

[Composição dos Blocos/Registros ECF](https://tdn.totvs.com/pages/releaseview.action?pageId=192094180#Blocos/Registros-blocox)

[Como gerar o registro X305 e/ou X325 no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402647905303-Cross-Segmento-Backoffice-Linha-Protheus-TAF-ECF-Como-gerar-o-registro-X305-e-X325)

[Página centralizadora ECF](https://tdn.totvs.com/display/public/PROT/ECF)
