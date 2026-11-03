---
content_hash: c098254d57a8ae65904283b7b2bc1a2d3d41829ea9d9459473edf7118a69295c
fetched_at: '2026-06-29T00:05:55.309423+00:00'
page_id: '129270008'
product: rm
source: tdn-rm
title: RMFIS00003_Bloco I
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00003_Bloco+I
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52.60.xx |
| **Processo** | **:** | EFD Contribuições |
| **Subprocesso** | **:** | Geração do Bloco I |
| **Data da publicação** | **:** | 19/03/2014 |

**Introdução**

A escrituração do Bloco I só é de natureza obrigatória em relação aos fatos geradores a ocorrer à partir de 01 de janeiro de  2014, conforme disposto na IN RFB nº 1.387, de 2013.

**Procedimento para implantação do processo para geração do Bloco I**

Recomendamos que esse procedimento seja realizado primeiramente EM AMBIENTE E BASE DE TESTE (backup da oficial) e somente após a validação, na base oficial:

1-  Rodar o script (Liberado apenas quando for solicitado).

2-  Atualizar a versão da Biblioteca para a **11.52.60.xxx** e superiores .

3-  Versão do Aplicativo TOTVS Gestão Fiscal **11.52.60.xx** e superiores.

4-  Importar o último Layout disponível da Rotina.

5-  Realizar a parametrização do processo no Menu **Opção |Processo | EFD Contribuições PIS/COFINS – BLOCO I**

6-  Gerar a Rotina EFD PIS/COFINS.

**5.1** **Opção | Parametros | Processos**

**EFD | PIS/COFINS** –  “Grupos/SubGrupos”

Bloco I – Ícone “Novo”

* Identificação

  Grupo: Bloco I

  SubGrupos: Tabelas de Contas Contábeis – Coligada

  Tabela: Contas Contábeis

  Data Inicial: Deve ser informada manualmente

  Data Final: Deve ser informada

* Sub Pasta Tributos

  CST

  Tributo

  NAT\_REC - Natureza da Receita (Campo necessário para gerar os registros M410 e M810).

**Observação**:

Natureza da Receita, relação constante nas Tabelas de Detalhamento da Natureza da Receita por Situação Tributária abaixo:

- Tabela 4.3.10: Produtos Sujeitos à Incidência Monofásica da Contribuição Social – Alíquotas Diferenciadas (CST 04 - Revenda);

- Tabela 4.3.11: Produtos Sujeitos à Incidência Monofásica da Contribuição Social – Alíquotas por Unidade de Medida de Produto (CST 04 - Revenda);

- Tabela 4.3.12: Produtos Sujeitos à Substituição Tributária da Contribuição Social (CST 05 - Revenda);

- Tabela 4.3.13: Produtos Sujeitos à Alíquota Zero da Contribuição Social (CST 06);

- Tabela 4.3.14: Operações com Isenção da Contribuição Social (CST 07);

- Tabela 4.3.15: Operações sem Incidência da Contribuição Social (CST 08);

- Tabela 4.3.16: Operações com Suspensão da Contribuição Social (CST 09).

* Sub Pasta Tributos –

Pasta Contas: onde será informado os seguintes campos:

  Conta Contábil: Neste campo deve ser informado as Contas Contábeis Analíticas (Global ou não)

  Tipo:   Faturamento ou Receita Bruta

          Deduções e Exclusões de Caráter Geral

          Deduções e Exclusões de Caráter Específico

 Tipo de Totalização das Contas:  Informe que tipo de totalização será feita, com base nas Contas Contábeis, ou seja, o que será considerado para totalização e composição dos Campos (Faturamento ou Receita Bruta\Deduções e Exclusões de Caráter Geral\ Deduções e Exclusões). As opções são:

Débito:

Crédito:

Movimentação:

Saldo Anterior:

Saldo Atual:

 Código do tipo de detalhamento: neste campo deve ser informado os códigos conforme Tabelas “7.1.1 – Composição das Receitas” e/ou Tabela “7.1.2 – Composição das Deduções e Exclusões”. (Necessário para gerar o Registro I200).

 Código Visão Analítica\Referenciada: neste campo deve ser informado os Códigos conforme Tabelas “7.1.3 Receitas” e/ou “7.1.4 Deduções e Exclusões” (Necessário para gerar o Registro I300).

Sub Pasta Tributos - Pasta Histórico Padrão\Fechamento: nesta pasta poderá definir os Históricos Padrões que deverão ser desconsiderados no cálculo dos valores (das contas contábeis).

**Observação**:

Conforme orientação da Equipe responsável pelo Aplicativo Gestão Contábil, o Histórico Padrão do Tipo de “Fechamento” é o mais correto a ser utilizado para ser desconsiderado no cálculo dos valores das contas Contábeis.

**Tela de Geração da Rotina**

* **Rotinas Legais | Rotinas Federais | EFD PIS/COFINS**

  Selecionar o Layout da Rotina: “ EFD\_CONTRIBUICOES\_B”.

  Selecionar o Diretório Destino: Informar onde deseja salvar o arquivo gerado – Como default o aplicativo traz o seguinte caminho: "C:\totvs\CorporeRM\RMLiber\Saídas".

  Gerar arquivo no Servidor: Habilitar caso deseja que o arquivo seja gerado no servidor.

* Tela de Parametrização de Geração da Rotina “**Gerador de Saídas**”:

  Data do Layout do Gerador de Saídas: Sempre que liberamos um layout atualizamos este campo automaticamente.

  Coligada:

  Filial Matriz:

  Considera operações das Filiais SCP: Deixar desmarcado.

  Considera Data Leitura para Seleção de Lançamentos de Energia Eletrica: Deixar desmarcado.

  Versão do Layout: Default 2.00.

  Indicador de situação especial: Não se aplica.

  Número do Recibo declaração anterior (somente para retificadora).

  Data Inicial:

  Data Final:

  Gerar Bloco D: Deixar o *Default*

  Gerar Registro M350: Deixar o *Default*

  Indicador de Atividade Preponderante: No caso do Bloco I deve ser gerado a “3 Atividade Financeira”.

  Contribuição Previdenciária apurada Exclusivamente com base na Receita Bruta: Deixar o Default.

  Lucro Presumido: Não se Aplica.

  Lucro Presumido com base nas informações do Lançamento Fiscal ou Movimento: Deixar desmarcado.

  Cenário Patrimônio: Não é necessário informar.

  Tipo de Escrituração: 0 – Original ou 1 – Retificadora.

  Indicador da Natureza da Pessoa Jurídica: 00 – Pessoa jurídica em geral; 01 – Sociedade cooperativa; 02 – Entidade sujeita ao PIS/Pasep exclusivamente com base na Folha de Salários.

  Rotina:

  Classificação de Municipio: Informar IBGE.

  Classificação do País – SISCOMEX.

  Classificação de Países (Comércio Exterior) I SISCOMEX.

  Código indicador da incidência tributária no período : 2 Com incidência no regime Cumulativo – conforme o manual.  (Registro específico para escrituração pelas pessoas jurídicas referidas nos §§ 6º, 8º e 9º do art. 3º da Lei nº 9.718, sujeitas ao regime cumulativo de apuração das contribuições, conforme definido nas Leis nº 10.637/2002 (PIS/Pasep) e nº 10.833/2003 (Cofins)).

  Código indicador de método de apropriação de créditos: 1 Métodos de Apropriação Direta.

  Operações Institucionais Realizadas no período: Indicador de operações realizadas no período: Com as seguintes opções:

N – Não se Aplica

01 – Exclusivamente operações de Instituições Financeiras e Assemelhadas.

02 – Exclusivamente operações de Seguros Privados.

03 – Exclusivamente operações de Previdência Complementar.

04 – Exclusivamente operações de Capitalização.

05 – Exclusivamente operações de Planos de Assistência à Saúde.

       06 – Realizou operações referentes a mais de um dos indicadores acima.

**Observação**: Utilizando a opçõa “N - Não se aplica” não será gerada informações do Bloco I.

**Arquivo Gerado**

O arquivo deve ser gerado com os dados da Filial Matriz, detalhando as informações por Filais.

**Observação**:

O Bloco I somente será gerado para os clientes que tem integração com o Gestão Contábil, pois utilizamos informações deste aplicativo para gerar os valores.

Neste Bloco temos as seguintes opções de Geração:

  Contabilização Centralizada na Filial Matriz.

  Descentralizada: Detalhada por Filial.

Neste primeiro momento optamos internamente por gerar somente na forma *descentralizada*. Futuramente vamos disponibilizar opção para que o usuário possa escolher forma deseja gerar:

Para o ano de 2013 não será gerado o **Registro I300**.

**Registro I100**

Quando os CST for igual a 04, 05, 06, 07, 08, 09, o campo Alíquota dos Tributos PIS/COFINS será gerada zerada. Pois estes tipos de CST não tem Alíquota.

Estrutura sistemática dos registros:

**REGISTRO I001: ABERTURA DO BLOCO I**

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo "I001" |  |
| 02 | IND\_MOV | Indicador de movimento:  0 - Bloco com dados informados  1 - Bloco sem dados informados |  |

**REGISTRO I010: IDENTIFICAÇÃO DA PESSOA JURIDICA/ESTABELECIMENTO**

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo “I010” |  |
| 02 | CNPJ | Número de inscrição da pessoa jurídica no CNPJ | Gerado com o CNPJ informado no Cadastro da Filial |
| 03 | IND\_ATIV | Indicador de operações realizadas no período:  01 – Exclusivamente operações de Instituições Financeiras e Assemelhadas  02 – Exclusivamente operações de Seguros Privados  03 – Exclusivamente operações de Previdência Complementar  04 – Exclusivamente operações de Capitalização  05 – Exclusivamente operações de Planos de Assistência à Saúde  06 – Realizou operações referentes a mais de um dos indicadores acima | Campo a ser criado na Tela de Geração da Rotina |
| 04 | INFO\_COMPL | Informação Complementar | Escriturar neste campo informações complementares referente aos campos 02 ou 03, a critério e interesse da pessoa jurídica.  Obs: Este campo será gerado em branco, pois não temos Campo para Observação no Cadastro da Filial. |

**REGISTRO I100: CONSOLIDAÇÃO DAS OPERAÇÕES DO PERÍODO**

Este registro deve ser gerado um para cada Combinação de CST, Alíquota PIS e Alíquota Cofins. Chaves do registro: CST + ALIQ\_PIS + ALIQ\_COFINS + INFO\_COMPL

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo "I100" |  |
| 02 | VL\_REC | Valor Total do Faturamento/Receita Bruta no Período | Será gerado com o valor retornado do RM Saldus,que nos processo foi parametrizado como: “Faturamento/Receita Bruta” |
| 03 | CST\_PIS\_COFINS | Código de Situação Tributária referente à Receita informada no Campo 02 (Tabelas 4.3.3 e 4.3.4) | Será gerado com o CST informado nos Processo |
| 04 | VL\_TOT\_DED\_GER | Valor Total das Deduções e Exclusões de Caráter Geral | Será gerado com o valor retornado do RM Saldus,que nos processo foi parametrizado como:” Deduções e Exclusões de Caráter Geral” |
| 05 | VL\_TOT\_DED\_ESP | Valor Total das Deduções e Exclusões de Caráter Específico | Será gerado com o valor retornado do RM Saldus,que nos processo foi parametrizado como:” Deduções e Exclusões de Caráter Específico” |
| 06 | VL\_BC\_PIS | Valor da base de cálculo do PIS/PASEP | Calculado:   Campo 02 – Campo 04 – Campo 05 |
| 07 | ALIQ\_PIS | Alíquota do PIS/PASEP (em percentual) | Será gerado com a Alíquota Cadastrada no Tributos, informado no Processo |
| 08 | VL\_PIS | Valor do PIS/PASEP | Calculado: Campo 06 \* campo 07 |
| 09 | VL\_BC\_COFINS | Valor da base de cálculo da Cofins | Calculado:   Campo 02 – Campo 04 – Campo 05 |
| 10 | ALIQ\_COFINS | Alíquota da COFINS (em percentual) | Será gerado com a Alíquota Cadastrada no Tributos, informado no Processo |
| 11 | VL\_COFINS | Valor da COFINS | Calculado: Campo 09 \* campo 10 |
| 12 | INFO\_COMPL | Informação Complementar dos dados informados no registro | Escriturar neste campo informações Informar neste campo as informações complementares relacionadas ao registro, necessárias ou adequadas para tornar a escrituração mais completa e Transparente.  Obs: Este campo será gerado em branco. |

**REGISTRO I199: PROCESSO REFERENCIADO**

**Neste Primeiro instante este Registro não será gerado.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo "I199" |  |
| 02 | NUM\_PROC | Identificação do processo ou ato concessório |  |
| 03 | IND\_PROC | Indicador da origem do processo:  1 - Justiça Federal;  3 – Secretaria da Receita Federal do Brasil  9 – Outros. |  |

**REGISTRO I200: COMPOSIÇÃO DAS RECEITAS, DEDUÇÕES E/OU EXCLUSÕES DO PERÍODO**

As informações deste registro deve ser delhadas de forma sintéticas, por isto vamos utilizar os código das contas Contabeis sintéticos. Deve ser preenchido um registro para cada tipo de receita e/ou deduções e exclusões, codificadas nas Tabelas 7.1.1 e 7.1.2,  conforme o caso. Chaves do registro: NUM\_CAMPO + COD\_DET + COD\_CTA + INFO\_COMPL

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo "I200" |  |
| 02 | NUM\_CAMPO | Número do campo do registro “I100” (Campos 02, 04 ou 05), objeto de informação neste registro. |  |
| 03 | COD\_DET | Código do tipo de detalhamento, conforme Tabelas 7.1.1 e/ou 7.1.2 | Gerado como o Código informado no processo – Campo será criado |
| 04 | DET\_VALOR | Valor detalhado referente ao campo 03 (COD\_DET) deste registro | Gerado conforme o Valor da Conta Contábil |
| 05 | COD\_CTA | Código da conta contábil referente ao valor informado no campo 04 (DET\_VALOR) | No processo será parametrizado como a Conta Contábil Analítica, neste campo será gerado com a Conta Contábil do nível anterior. (Código Sintético). |
| 06 | INFO\_COMPL | Informação Complementar dos dados informados no registro | Escriturar neste campo informações Informar neste campo as informações complementares relacionadas ao registro, necessárias ou adequadas para tornar a escrituração mais completa e Transparente.  Obs: Este campo será gerado em branco. |

**REGISTRO I299: PROCESSO REFERENCIADO**

**Neste Primeiro instante este Registro não será gerado.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo "I299" |  |
| 02 | NUM\_PROC | Identificação do processo ou ato concessório |  |
| 03 | IND\_PROC | Indicador da origem do processo:  1 - Justiça Federal;  3 – Secretaria da Receita Federal do Brasil  9 – Outros. |  |

**REGISTRO I300: COMPLEMENTO DAS OPERAÇÕES – DETALHAMENTO DAS RECEITAS, DEDUÇÕES E/OU EXCLUSÕES DO PERÍODO**

As informações deste registro deve ser delhadas de forma Analítica, por isto vamos utilizar os código das contas Contábeis analíticas. Deve ser preenchido um registro para cada tipo de receita e/ou deduções e exclusões, codificadas nas Tabelas 7.1.1 e 7.1.2, conforme o caso. Chaves do registro: COD\_COMP + COD\_CTA + INFO\_COMPL.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo "I300" |  |
| 02 | COD\_COMP | Código das Tabelas 7.1.3 (Receitas – Visão Analítica/Referenciada) e/ou 7.1.4 (Deduções e exclusões – Visão Analítica/Referenciada), objeto de complemento neste registro | Gerado como o Código informado no processo – Campo será criado |
| 03 | DET\_VALOR | Valor da receita, dedução ou exclusão, objeto de  complemento/detalhamento neste registro, conforme código informado no campo 02 (especificados nas tabelas analíticas  7.1.3 e 7.1.4) ou no campo 04 (código da conta contábil) | Gerado conforme o Valor da Conta Contábil |
| 04 | COD\_CTA | Código da conta contábil referente ao valor informado no campo 03 | Gerado com o Código da Conta Contábil parametrizada no processo (Código da Conta Analítica) |
| 05 | INFO\_COMPL | Informação Complementar dos dados informados no registro | Escriturar neste campo informações Informar neste campo as informações complementares relacionadas ao registro, necessárias ou adequadas para tornar a escrituração mais completa e Transparente.  Obs: Este campo será gerado em branco. |

**REGISTRO I399: PROCESSO REFERENCIADO**

**Neste Primeiro instante este Registro não será gerado.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo "I399" |  |
| 02 | NUM\_PROC | Identificação do processo ou ato concessório |  |
| 03 | IND\_PROC | Indicador da origem do processo:  1 - Justiça Federal;  3 – Secretaria da Receita Federal do Brasil  9 – Outros. |  |

**REGISTRO I990: ENCERRAMENTO DO BLOCO I**

|  |  |  |  |
| --- | --- | --- | --- |
| **NNº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 01 | REG | Texto fixo contendo "I990" |  |
| 02 | QTD\_LIN\_I | Quantidade total de linhas do Bloco |  |

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ApuracaoTribuosRetidos.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
