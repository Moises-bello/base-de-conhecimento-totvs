---
content_hash: d38505f97c3171b0691408ff6be2e520011cac9febfca987ac91cec808f093b2
fetched_at: '2026-06-29T00:11:13.343041+00:00'
page_id: '658741228'
product: rm
source: tdn-rm
title: DCTF (Declaração de Débitos e Créditos Tributários Federais)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=658741228
version: 48
---

#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Com o objetivo de proporcionar uma melhor experiência e alinhamento às atualizações mais recentes dos nossos produtos, informamos que a funcionalidade **DCTF (Declaração de Débitos e Créditos Tributários Federais)****,** já disponível no Módulo Gestão Fiscal, não será mais suportada no produto **RM Liber.exe** a partir da **versão 12.1.2502**

Reforçamos que essa alteração faz parte do nosso processo de evolução tecnológica, com a descontinuidade gradual de funcionalidades no **RM** **Liber.exe**. Para garantir a continuidade do uso e acesso à funcionalidade DCTF, recomendamos que a geração seja feita diretamente no **Módulo Gestão Fiscal**.

# Conteúdo

1Conteúdo

# 01. Visão Geral

A **DCTF (Declaração de Débitos e Créditos Tributários Federais)** é uma obrigação acessória enviada à Receita Federal do Brasil. Por meio dela, a Receita recebe informações sobre débitos e créditos tributários, além de como o contribuinte realizou o pagamento desses tributos, seja via pagamento direto, compensação, suspensão ou parcelamento.

No **Módulo Gestão Fiscal** do ERP, a rotina de geração da DCTF está disponível no [Gerador de Saídas](https://tdn.totvs.com/pages/viewpage.action?pageId=237383341) e para utilizá-la basta baixar o layout disponível no [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816).

# 02. Alterações de Layout DCTF

Atualmente, existem dois layouts principais da DCTF disponíveis:

* **FISLAY0026 - DCTF-Antes\_2024.TotvsGen**
* **FISLAY0031 - DCTF.TotvsGen**

Ambos podem ser acessados e baixados no **TOTVS Compartilhamento**. É importante que as empresas acompanhem as atualizações de layout para garantir que as declarações sejam geradas corretamente.

#### Mais detalhes sobre as alterações de layout:

# 03. Como realizar a Apuração e gerar a guia DARF?

Com a introdução da **EFD-Reinf** (Escrituração Fiscal Digital de Retenções e Informações da Contribuição Previdenciária Substituída), a apuração de tributos federais passou a ser realizada automaticamente pelo governo por meio do portal **DCTFWeb**.

No entanto, desenvolvemos um mecanismo na linha RM que permite às empresas espelharem os valores apurados pelo governo em seus **Lançamentos Financeiros**.

Para mais informações detalhadas, consulte a nossa documentação: 

# 04. Registros

Nesta seção, estão detalhados todos os registros que fazem parte da estrutura da DCTF e são gerados pelo Módulo Gestão Fiscal.

01lefttrue01\_1Visão Geral dos Registros

**Tipos de Registros:**

Registro Tipo **Header -** Header da Declaração  
Registro Tipo **R01** - Ficha Dados Iniciais  
Registro Tipo **R02** - Ficha Dados Cadastrais do Estabelecimento Matriz  
Registro Tipo **R03** - Ficha Dados dos Responsáveis pela Pessoa Jurídica  
Registro Tipo **R10** - Ficha Débito Apurado e Créditos Vinculados  
Registro Tipo **R11** - Ficha Pagamento  
Registro Tipo **R12** - Ficha Compensações  
Registro Tipo **R14** - Ficha Suspensão  
Registro Tipo **R20** - Ficha Débito Apurado e Créditos Vinculados do Trimestre Anterior  
Registro Tipo **R21** - Ficha Pagamento do Trimestre Anterior  
Registro Tipo **R30** - Ficha Quotas  
Registro Tipo **R31** - Ficha Pagamento da Quota  
Registro Tipo **T9** - Ficha Trailler da Declaração

true1Header01\_1true01\_2CamposHeader da Declaração

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Sistema | Automático | Valor Fixo "DCTFM" |
| 02 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 03 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 04 | Ano de Competência da Declaração | Ano do fato gerador | Gerado conforme a Data Inicial informado na Tela de Geração da Rotina |
| 05 | Reservado | Automático | Valor Fixo "1930" |
| 06 | Tipo de Declaração | "0" - Original  "1" - Retificadora | Gerado conforme o Tipo de Declaração informado na Tela de Geração da Rotina |
| 07 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 08 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 09 | Versão | - | Valor preenchido com a versão informada na tela de geração da rotina |
| 10 | Nome Empresarial | Obrigatório. Tamanho mínimo de 3 posições e não pode conter somente dígitos | Gerado conforme o Nome Oficial da Filial Matriz |
| 11 | UF Domicílio | Obrigatório e válido | Gerado conforme o Estado da Filial Matriz |
| 12 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 13 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 14 | Situação | “00” – Normal  “01” – Extinção  “02” – Fusão  “03” – Incorporação/ Incorporada  “04” – Incorporação/ Incorporadora  “05” – Cisão Total  “06” – Cisão Parcial | Gerado conforme a Situação informada na Tela de Geração da Rotina |
| 15 | Ano de Competência da Declaração | Ano do fato gerador | Gerado conforme a Data Inicial informado na Tela de Geração da Rotina |
| 16 | Mês de Competência da Declaração | Mês do fato gerador | Gerado conforme a Data Inicial informado na Tela de Geração da Rotina |
| 17 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 18 | Período Base Inicial | Data Inicial do fato gerador | Gerado conforme a Data Inicial informado na Tela de Geração da Rotina |
| 19 | Período Base Final | Data Final do fato gerador | Gerado conforme a Data Final informado na Tela de Geração da Rotina |
| 20 | Data de Ocorrência do Evento | Data de Ocorrência do Evento  Se valor do Campo 14 = “00”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 21 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 22 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 23 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 24 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 25 | Delimitador de Registro | Quebra de linha do Registro | - |

true2R0102\_1true02\_2CamposFicha Dados Iniciais

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R01" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Início do Período | Data Inicial do Fato Gerador | Gerado conforme a Data Inicial informado na Tela de Geração da Rotina |
| 07 | Final do Período | Data Final do Fato Gerador | Gerado conforme a Data Final informado na Tela de Geração da Rotina |
| 08 | Declaração Retificadora | "0" - Não  "1" - Sim | Gerado conforme o campo "Declaração Retificadora" informado na Tela de Geração da Rotina |
| 09 | Número do Recibo de entrega da DCTF a ser retificada | Se Campo 08 = 0, preencher com zeros  Se Campo 08 = 1, preencher com o Número do Recibo de entrega da DCTF a ser retificada | - |
| 10 | Forma de Tributação do Lucro | "0" – Real/Trimestral  "1" – Real/Estimativa  "2" – Presumido  "3" – Arbitrado  "4" – Imune do IRPJ  "5" – Isenta do IRPJ  "8" – Declarante não é Contribuinte do IRPJ  "9" – Não preenchido  Se Qualificação da Pessoa Jurídica (Campo 11) = "10", preencher com "8"  Se PJ optante pelo Simples Nacional (Campo 14) = "1", preencher com "9"  Se PJ inativa no mês da declaração (Campo 16) = "1", preencher com "9" | Gerado conforme o campo "Forma de Tributação do Lucro" informado na Tela de Geração da Rotina |
| 11 | Qualificação da Pessoa Jurídica | "01" – Agências de Fomento e demais entidades elencadas no § 1° do art. 22 da Lei n° 8.212/1991  "02" – Sociedade Seguradora e de Capitalização ou Entidade Aberta de Previdência Complementar (com fins lucrativos)  "03" – Sociedade Corretora de Seguros  "04" – Cooperativa de Crédito  "05" – Entidade Fechada de Previdência Complementar ou Entidade Aberta de Previdência Complementar (sem fins lucrativos)  "06" – Sociedade Cooperativa  "07" – PJ em Geral  "08" – Sociedade Cooperativa de Produção Agropecuária ou de Consumo  "09" – Autarquia ou Fundação Pública  "10" – Estado, Distrito Federal, Município ou Órgão Público da Administração Direta  "11" – Empresa Pública, Sociedade de Economia Mista e demais PJ de que trata o inc. III do art. 34 da Lei n° 10.833/2003  "12" – Mais de uma qualificação durante o mês  Se PJ optante pelo Simples Nacional (Campo 14) = "1", preencher com "07" | Gerado conforme o campo "Qualificação da Pessoa Jurídica" informado na Tela de Geração da Rotina |
| 12 | PJ levantou balanço/balancete de suspensão no mês | "0" - Não  "1" - Sim | Gerado conforme o campo "PJ levantou balanço/balancete de suspensão no mês" informado na Tela de Geração da Rotina |
| 13 | PJ com débitos de SCP a serem declarados | - | - |
| 14 | PJ optante pelo Simples Nacional | "0" - Não  "1" - Sim  Se Ano do fato gerador = 2014, preencher com zero.  Se Ano do fato gerador = 2015 e Mês do fato gerador diferente de 12, preencher com zero.  Se PJ inativa no mês da declaração (Campo 16) = "1", preencher com zero. | Gerado conforme o campo "PJ optante pelo Simples Nacional" informado na Tela de Geração da Rotina |
| 15 | PJ optante pela CPRB | "0" - Não  "1" - Sim  Se Ano do fato gerador = 2014, preencher com zero.  Se Ano do fato gerador = 2015 e Mês do fato gerador diferente de 12, preencher com zero.  Se Qualificação da Pessoa Jurídica (Campo 11) = ["09","10"], preencher com zero.  Se PJ optante pelo Simples Nacional (Campo 14) = "1", preencher com "1".  Se PJ inativa no mês da declaração (Campo 16) = "1", preencher com zero. | Gerado conforme o campo "PJ optante pela CPRB" informado na Tela de Geração da Rotina |
| 16 | PJ inativa no mês da declaração | "0" - Não  "1" - Sim  Se Ano do fato gerador < 2016, preencher com zero. | Gerado conforme o campo "PJ inativa no mês da declaração" informado na Tela de Geração da Rotina |
| 17 | Critério de Reconhecimento das Variações Monetárias dos Direitos de Crédito e das Obrigações do Contribuinte, em Função da Taxa de Câmbio | 0 – Não preenchido  1 – Regime de Caixa  2 – Regime de Competência  3 – Regime de Caixa – Elevada oscilação da taxa de câmbio  4 – Não se aplica  5 – Sem alteração do regime  Se PJ optante pelo Simples Nacional (Campo 14) = "1", preencher com "0".  Se PJ inativa no mês da declaração (Campo 16) = "1", preencher com "0". | Gerado conforme o campo "Critério de Reconhecimento" informado na Tela de Geração da Rotina |
| 18 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 19 | Regime de Apuração da Contribuição para o PIS/Pasep e/ou da Cofins | 0 – Não preenchido  1 – Não-cumulativo  2 – Cumulativo  3 – Não-cumulativo e Cumulativo  4 – Não se aplica | Gerado conforme o campo "Regime de Apuração da Contribuição para o PIS/Pasep e/ou da Cofins" informado na Tela de Geração da Rotina |
| 20 | Situação da PJ no mês da declaração | "1" - PJ teve sua inscrição no CNPJ efetivada ou entrou em atividade no mês da declaração  "2" - PJ foi excluída do Simples no mês da declaração  "3" - Surgimento de nova PJ em razão de fusão ou cisão no mês da declaração  "4" - PJ não se enquadra em nenhuma das situações anteriores no mês da declaração | Gerado conforme o campo "Situação da PJ no mês da declaração" informado na Tela de Geração da Rotina |
| 21 | Opções referentes à Lei n° 12.973/2014 para o ano-calendário de 2014 | "0" - Não preenchido  "1" - Aplicação das disposições contidas nos arts. 1º e 2º e 4º a 70  "2" - Aplicação das disposições contidas nos arts. 76 a 92  "3" - Aplicação das disposições contidas nos arts. 1º e 2º e 4º a 70 e 76 a 92  "4" - Não optante | Gerado conforme o campo "Opções referentes à Lei n° 12.973/2014 para o ano-calendário de 2014" informado na Tela de Geração da Rotina |
| 22 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 23 | Delimitador de Registro | Quebra de linha do Registro | - |

true3R0203\_1true03\_2CamposFicha Dados Cadastrais do Estabelecimento Matriz

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R02" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Nome Empresarial | Obrigatório. Tamanho mínimo de 3 posições e não pode conter somente dígitos | Gerado conforme o Nome Oficial da Filial Matriz |
| 07 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 08 | Logradouro | - | Gerado conforme Logradouro da Filial Matriz |
| 09 | Número | - | Gerado conforme Número da Filial Matriz |
| 10 | Complemento | - | Gerado conforme Complemento da Filial Matriz |
| 11 | Bairro/Distrito | - | Gerado conforme Bairro da Filial Matriz |
| 12 | Município | - | Gerado conforme Município da Filial Matriz |
| 13 | UF | - | Gerado conforme UF da Filial Matriz |
| 14 | CEP | - | Gerado conforme DEP da Filial Matriz |
| 15 | DDD do Telefone | - | Gerado conforme DDD do Telefone da Filial Matriz |
| 16 | Telefone | - | Gerado conforme Telefone da Filial Matriz |
| 17 | DDD do Fax | - | Gerado conforme DDD do Fax da Filial Matriz |
| 18 | Fax | - | Gerado conforme Fax da Filial Matriz |
| 19 | Caixa Postal | - | Gerado conforme Caixa Postal da Filial Matriz |
| 20 | UF da Caixa Postal | - | Gerado conforme UF da Caixa Postal da Filial Matriz |
| 21 | CEP da Caixa Postal | - | Gerado conforme CEP da Caixa Postal da Filial Matriz |
| 22 | Correio Eletrônico | - | Gerado conforme E-mail da Filial Matriz |
| 23 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 24 | Delimitador de Registro | Quebra de linha do Registro | - |

true4R0304\_1true04\_2CamposFicha Dados dos Responsáveis pela Pessoa Jurídica

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R03" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Nome do Representante | - | Gerado conforme Nome do Representante da Filial Matriz |
| 07 | CPF - Representante | - | Gerado conforme CPF do Representante da Filial Matriz |
| 08 | DDD do Telefone - Representante | - | Gerado conforme DDD do Telefone do Representante da Filial Matriz |
| 09 | Telefone - Representante | - | Gerado conforme Telefone do Representante da Filial Matriz |
| 10 | Ramal - Representante | - | Gerado conforme Ramal do Representante da Filial Matriz |
| 11 | DDD do Fax - Representante | - | Gerado conforme DDD do Fax do Representante da Filial Matriz |
| 12 | Fax - Representante | - | Gerado conforme Fax do Representante da Filial Matriz |
| 13 | Correio Eletrônico - Representante | - | Gerado conforme E-mail do Representante da Filial Matriz |
| 14 | Nome do Responsável | - | Gerado conforme Nome do Responsável da Filial Matriz |
| 15 | CPF - Responsável | - | Gerado conforme CPF do Responsável da Filial Matriz |
| 16 | CRC - Responsável | - | Gerado conforme CRC do Responsável da Filial Matriz concatenado com o Dígito do CRC |
| 17 | UF do CRC - Responsável | - | Gerado conforme UF do CRC do Responsável da Filial Matriz |
| 18 | DDD do Telefone - Responsável | - | Gerado conforme DDD do Telefone do Responsável da Filial Matriz |
| 19 | Telefone - Responsável | - | Gerado conforme Telefone do Responsável da Filial Matriz |
| 20 | Ramal - Responsável | - | Gerado conforme Ramal do Responsável da Filial Matriz |
| 21 | DDD do Fax - Responsável | - | Gerado conforme DDD do Fax do Responsável da Filial Matriz |
| 22 | Fax - Responsável | - | Gerado conforme Fax do Responsável da Filial Matriz |
| 23 | Correio Eletrônico - Responsável | - | Gerado conforme E-mail do Responsável da Filial Matriz |
| 24 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 25 | Delimitador de Registro | Quebra de linha do Registro | - |

true5R1005\_1true05\_2CamposFicha Débito Apurado e Créditos Vinculados

Para cada guia DARF cadastrada no Sistema de Gestão Fiscal relacionada aos tributos deste registro, será gerada uma ficha R10.

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R10" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Grupo de Tributo | 01 – IRPJ  02 – IPI  03 – IOF  04 – CSLL  05 – PIS/PASEP  06 – COFINS  07 – CPMF  08 – CIDE  09 – RET/PAGAMENTO UNIFICADO DE TRIBUTOS | Gerado conforme o tipos de Tributos listados na Rotina. |
| 07 | Código da Receita | "Código da Receita" + "Variação" | Gerado conforme o Código da Receita da Guia e a Variação do Tributo |
| 08 | Periodicidade | - | Gerado conforme o período de Apuração do Tributo |
| 09 | Ano do Período de Apuração | - | Gerado conforme o Ano do Período de Apuração do Tributo |
| 10 | Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração | - | Gerado conforme o Mês do Período de Apuração do Tributo |
| 11 | Dia/Semana/Quinzena/Decêndio do Período de Apuração | Se a Apuração do tributo for diferente de Mensal o campo deve ser preenchido, caso contrário, preencher com zeros | Gerado conforme o Dia do Período de Apuração do Tributo |
| 12 | Ordem do Estabelecimento | Se aplica somente ao IPI e CIDE, preencher com zeros para os demais | Gerado conforme os últimos 6 caracteres do CNPJ da Filial Matriz |
| 13 | CNPJ da Incorporação/Matrícula CEI | Se RET, preencher com informação relativa ao CNPJ da Incorporação OU se Código da Receita (campo 07) = 2985-06, preencher com informação relativa à Matrícula CEI | Gerado conforme o CNPJ da Filial Matriz |
| 14 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 15 | Valor do Débito | Campo Valor do Débito preenchido com o Valor Principal das guias | Gerado conforme valor apurado da guia (ValorApurado), em casos de guias acumuladas, gerado com valor acumulado (ValorGNR) |
| 16 | Balanço de Redução | “0” – Sem Balanço de Redução  “1” – Com Balanço de Redução | Gerado conforme o campo Balanço de Redução informado na Tela de Geração da Rotina |
| 17 | O saldo deste débito será dividido em quotas | “0” – Sem divisão em quotas  “1” – Com divisão em quotas | Gerado conforme o campo "O saldo deste débito será dividido em quotas" informado na Tela de Geração da Rotina |
| 18 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 19 | Débito de SCP/INC | “0” – Não é SCP nem INC  “1” – SCP  "2" – INC | Gerado conforme à condição se a Filial é SCP, INC ou nenhuma das duas |
| 20 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 21 | Delimitador de Registro | Quebra de linha do Registro | - |

05\_3ConsistênciaCampos

| Campo | Regra |
| --- | --- |
| DebitoSCP\_INC | SE Tipo Tributo RET = 2  SE Filial SCP = 1  SENÃO = 0 |
| CodigoReceita | O registro R10 é agrupado pelo código de receita do respectivo tributo. |

true6R1106\_1true06\_2CamposFicha Pagamento

Cada registro informado na ficha R11 corresponde a uma guia DARF cadastrada no sistema. Se esta guia estiver integrada ao RM Fluxus, o Lançamento Financeiro associado deve estar baixado.

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R11" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Grupo de Tributo | 01 – IRPJ  02 – IRRF  03 – IPI  04 – IOF  05 – CSLL  06 – PIS/PASEP  07 – COFINS  08 – CPMF  09 – CIDE  10 – RET/PAGAMENTO UNIFICADO DE TRIBUTOS  11 – CSRF  12 – COSIRF | Gerado conforme o tipos de Tributos listados na Rotina  Observação: O tributo CSLLRF é gerado com o código 11 - CSRF por pertencer a esse grupo no validador da rotina. |
| 07 | Código da Receita | "Código da Receita" + "Variação" | Gerado conforme o Código da Receita e a Variação do Tributo |
| 08 | Periodicidade | - | Gerado conforme o período de Apuração do Tributo |
| 09 | Ano do Período de Apuração | - | Gerado conforme o Ano do Período de Apuração do Tributo |
| 10 | Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração | - | Gerado conforme o Mês do Período de Apuração do Tributo |
| 11 | Dia/Semana/Quinzena/Decêndio do Período de Apuração | Se a Apuração do tributo for diferente de Mensal o campo deve ser preenchido, caso contrário, preencher com zeros | Gerado conforme regra:  - diário, dia do período de apuração. - semanal, 1 a 5 conforme dia do fato gerador. - decendial, decêndio 1 a 3 em que ocorreu o fato gerador. - quinzenal, quinzena 1 ou 2 em que ocorreu o fato gerador. - mensal 00 (preenchido automaticamente pelo programa). |
| 12 | Ordem do Estabelecimento | Se aplica somente ao IPI e CIDE, preencher com zeros para os demais | Gerado conforme os últimos 6 caracteres do CNPJ da Filial Matriz |
| 13 | CNPJ da Incorporação/Matrícula CEI | Se RET, preencher com informação relativa ao CNPJ da Incorporação OU se Código da Receita (campo 07) = 2985-06, preencher com informação relativa à Matrícula CEI | Gerado conforme o CNPJ da Filial Matriz |
| 14 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 15 | Período de Apuração | - | Gerado conforme o período de Apuração do Tributo |
| 16 | CNPJ do DARF | - | Gerado conforme o CNPJ da Filial Matriz |
| 17 | Código da Receita do DARF | Apenas o Código da Receita | Gerado conforme o Código da Receita do Tributo |
| 18 | Data de Vencimento | - | Gerado conforme Data de Vencimento da Guia |
| 19 | Nº de Referência | Se o Código de Receita do DARF for "4028" (IOF-ouro), preencher com o código do município | - |
| 20 | Valor do Principal | Campo Valor do Débito preenchido com o Valor Principal das guias | Gerado conforme valor apurado da guia (ValorApurado), em casos de guias acumuladas, gerado com valor acumulado (ValorGNR) |
| 21 | Valor da Multa | - | Gerado conforme o Valor das Multas das Guias |
| 22 | Valor dos Juros | - | Gerado conforme o Valor dos Juros das Guias |
| 23 | Valor Pago do Débito | - | Gerado conforme o Valor Principal das Guias |
| 24 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 25 | Delimitador de Registro | Quebra de linha do Registro | - |

true7R1207\_1true07\_2CamposFicha Compensações

Esta ficha deverá ser gerada para todas as Guias do período que sofreram Compensação, seja total ou parcial.

Para gerar a guia, é necessário realizar o processo de Compensação de Tributos.

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R12" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Grupo de Tributo | 01 – IRPJ  02 – IPI  03 – IOF  04 – CSLL  05 – PIS/PASEP  06 – COFINS  07 – CPMF  08 – CIDE  09 – RET/PAGAMENTO UNIFICADO DE TRIBUTOS | Gerado conforme o tipos de Tributos listados na Rotina |
| 07 | Código da Receita | "Código da Receita" + "Variação" | Gerado conforme o Código da Receita e a Variação do Tributo |
| 08 | Periodicidade | - | Gerado conforme o período de Apuração do Tributo |
| 09 | Ano do Período de Apuração | - | Gerado conforme o Ano do Período de Apuração do Tributo |
| 10 | Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração | - | Gerado conforme o Mês do Período de Apuração do Tributo |
| 11 | Dia/Semana/Quinzena/Decêndio do Período de Apuração | Se a Apuração do tributo for diferente de Mensal o campo deve ser preenchido, caso contrário, preencher com zeros | Gerado conforme o Dia do Período de Apuração do Tributo |
| 12 | Ordem do Estabelecimento | Se aplica somente ao IPI e CIDE, preencher com zeros para os demais | Gerado conforme os últimos 6 caracteres do CNPJ da Filial Matriz |
| 13 | CNPJ da Incorporação/Matrícula CEI | Se RET, preencher com informação relativa ao CNPJ da Incorporação OU se Código da Receita (campo 07) = 2985-06, preencher com informação relativa à Matrícula CEI | Gerado conforme o CNPJ da Filial Matriz |
| 14 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 15 | Valor Compensado do Débito | - | Gerado conforme o Valor Compensado do Tributo das Guias |
| 16 | Formalização do Pedido | “1” – Processo Administrativo  “3” – Dcomp  “4” – Dcomp com Direito Creditório Reconhecido em Processo | Gerado conforme o valor do campo "Formalização do Pedido de Crédito" dentro das Compensações de Tributos Federais |
| 17 | Número da DComp ou Processo | - | Gerado conforme o valor do campo "Número do Pedido" dentro das Compensações de Tributos Federais |
| 18 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 19 | Delimitador de Registro | Quebra de linha do Registro | - |

true8R1408\_1true08\_2CamposFicha Suspensão

Esta Ficha deve ser gerada sempre que houver Debito Discutido Judicialmente. Quando no Período de Apuração (Anexo | Darf | Sub Pasta | Outros Dados) estiver informado o processo e o campo Valor Suspensão estiver preenchido, o registro **R14** deverá ser gerado.

Dentro do cadastro do Processo Judicial e Administrativo, o campo Natureza da Ação Judicial deve ser preenchida com uma natureza adequada para geração da ficha.

| Nº | Natureza Judicial |
| --- | --- |
| 3 | Decisão judicial oriunda de liminar em mandado de segurança. |
| 4 | Decisão judicial oriunda de liminar em medida  cautelar |
| 5 | Decisão judicial oriunda de antecipação de tutela. |
| 7 | Medida judicial em que a pessoa jurídica não é o  autor. |
| 9 | Decisão judicial oriunda de liminar em mandado de  segurança coletivo. |
| 10 | Sentença ação ordinária favorável contribuinte confirmada TRF |
| 11 | Acórdão do TRF favorável ao contribuinte |
| 20 | Acórdão STJ recurso especial favorável Contribuinte |
| 21 | Acordão STF recurso Extraordinário Favorável Contribuinte |

O Motivo da Suspensão deve respeitar as opções informadas em Campos, caso contrário, o registro não será gerado.

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R14" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Grupo de Tributo | 01 – IRPJ  02 – IPI  03 – IOF  04 – CSLL  05 – PIS/PASEP  06 – COFINS  07 – CPMF  08 – CIDE  09 – RET/PAGAMENTO UNIFICADO DE TRIBUTOS | Gerado conforme o tipos de Tributos listados na Rotina |
| 07 | Código da Receita | "Código da Receita" + "Variação" | Gerado conforme o Código da Receita da Guia e a Variação do Tributo |
| 08 | Periodicidade | - | Gerado conforme o período de Apuração do Tributo |
| 09 | Ano do Período de Apuração | - | Gerado conforme o Ano do Período de Apuração do Tributo |
| 10 | Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração | - | Gerado conforme o Mês do Período de Apuração do Tributo |
| 11 | Dia/Semana/Quinzena/Decêndio do Período de Apuração | Se a Apuração do tributo for diferente de Mensal o campo deve ser preenchido, caso contrário, preencher com zeros | Gerado conforme o Dia do Período de Apuração do Tributo |
| 12 | Ordem do Estabelecimento | Se aplica somente ao IPI e CIDE, preencher com zeros para os demais | Gerado conforme os últimos 6 caracteres do CNPJ da Filial Matriz |
| 13 | CNPJ da Incorporação/Matrícula CEI | Se RET, preencher com informação relativa ao CNPJ da Incorporação OU se Código da Receita (campo 07) = 2985-06, preencher com informação relativa à Matrícula CEI | Gerado conforme o CNPJ da Filial Matriz |
| 14 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 15 | Valor Suspenso do Débito | Preencher com Valor > 0 | Gerado conforme o campo Valor Suspenso da Guia |
| 16 | Motivo da Suspensão | “01” – Liminar em Mandado de Segurança  “02” – Depósito Judicial do Montante Integral  “03” – Antecipação de Tutela  “04” – Liminar em Medida Cautelar  “07” – Medida Judicial em que o declarante não é o autor  “08” – Sentença em Mandado de Segurança favorável ao contribuinte  “09” – Sentença em Ação Ordinária favorável ao contribuinte e confirmada pelo TRF  “10” – Acórdão do TRF favorável ao contribuinte  “11” – Acórdão do STJ em Recurso Especial favorável ao contribuinte  “12” – Acórdão do STF em Recurso Extraordinário favorável ao contribuinte | Gerado conforme o campo Natureza Judicial, dentro do Processo Judicial e Administrativo |
| 17 | Depósito | Automático | Valor Fixo preenchido com "0"  Sem Depósito |
| 18 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 19 | Número do Processo | Obrigatório se Motivo da Suspensão (campo 16) diferente de “07”  Preencher com brancos se Motivo da Suspensão (campo 16) = “07” | Gerado conforme o campo Número, dentro do Processo Judicial e Administrativo |
| 20 | Vara | Obrigatório se Motivo da Suspensão (campo 16) diferente de “07”  Preencher com brancos se Motivo da Suspensão (campo 16) = “07” | Gerado conforme o campo Vara, dentro do Processo Judicial e Administrativo |
| 21 | Município | Obrigatório se Motivo da Suspensão (campo 16) diferente de “07”  Preencher com brancos se Motivo da Suspensão (campo 16) = “07” | Gerado conforme o campo Cod Município, dentro do Processo Judicial e Administrativo |
| 22 | UF | Obrigatório se Motivo da Suspensão (campo 16) diferente de “07”  Preencher com brancos se Motivo da Suspensão (campo 16) = “07” | Gerado conforme o campo Cod Etd, dentro do Processo Judicial e Administrativo |
| 23 | Identificação do Depósito | Preencher se Depósito (campo 17) = "1" | Valor Fixo preenchido com Branco(s) |
| 24 | Período de Apuração | Preencher se Depósito (campo 17) = "1" | Valor Fixo preenchido com Zero(s) |
| 25 | CPF/CNPJ | Preencher se Depósito (campo 17) = "1" | Valor Fixo preenchido com Branco(s) |
| 26 | Código da Receita | Preencher se Depósito (campo 17) = "1" | Valor Fixo preenchido com Zero(s) |
| 27 | Data do Vencimento | Preencher se Depósito (campo 17) = "1" | Valor Fixo preenchido com Zero(s) |
| 28 | Valor do Principal | Preencher se Depósito (campo 17) = "1" | Valor Fixo preenchido com Zero(s) |
| 29 | Valor da Multa | Preencher se Depósito (campo 17) = "1" | Valor Fixo preenchido com Zero(s) |
| 30 | Valor dos Juros | Preencher se Depósito (campo 17) = "1" | Valor Fixo preenchido com Zero(s) |
| 31 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 32 | Delimitador de Registro | Quebra de linha do Registro | - |

08\_3ConsistênciaCampos

| Campo | Regra |
| --- | --- |
| Motivo da Suspensão | “01” – Liminar em Mandado de Segurança  “02” – Depósito Judicial do Montante Integral  “03” – Antecipação de Tutela  “04” – Liminar em Medida Cautelar  “07” – Medida Judicial em que o declarante não é o autor  “08” – Sentença em Mandado de Segurança favorável ao contribuinte  “09” – Sentença em Ação Ordinária favorável ao contribuinte e confirmada pelo TRF  “10” – Acórdão do TRF favorável ao contribuinte  “11” – Acórdão do STJ em Recurso Especial favorável ao contribuinte  “12” – Acórdão do STF em Recurso Extraordinário favorável ao contribuinte |

true11R2011\_1true11\_2CamposDébito Apurado e Créditos Vinculados do Trimestre Anterior

**Ficha Débito Apurado e Créditos Vinculados do Trimestre Anterior**

Contém o valor líquido do débito apurado no trimestre anterior e a quantidade de quotas que foi dividido (Quantidade de quotas em que foi dividido o valor do tributo, 2 ou 3).

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R20" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Grupo de Tributo | 01 – IRPJ  02 – IRRF  03 – IPI  04 – IOF  05 – CSLL  06 – PIS/PASEP  07 – COFINS  08 – CPMF  09 – CIDE  10 – RET/PAGAMENTO UNIFICADO DE TRIBUTOS  11 – CSRF  12 – COSIRF | Gerado conforme o tipos de Tributos listados na Rotina |
| 07 | Código da Receita | "Código da Receita" + "Variação" | Gerado conforme o Código da Receita e a Variação do Tributo |
| 08 | Periodicidade | - | Gerado conforme o período de Apuração do Tributo |
| 09 | Ano do Período de Apuração | - | Gerado conforme o Ano do Período de Apuração do Tributo |
| 10 | Trimestre do Período de Apuração | - | Gerado conforme o Trimestre do Período de Apuração do Tributo |
| 11 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 12 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 13 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 14 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 15 | Valor do Débito | Valor > 2000 | Soma dos valores de débitos das quotas |
| 16 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 17 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 18 | Quantidade de Quotas | - | Valor preenchido conforme a quantidade de quotas geradas |
| 19 | Débito de SCP/INC | “0” – Não é SCP nem INC  “1” – SCP  "2" – INC | Gerado conforme à condição se a Filial é SCP, INC ou nenhuma das duas |
| 20 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 21 | Delimitador de Registro | Quebra de linha do Registro | - |

true12R2112\_1true12\_2CamposPagamento do Trimestre Anterior

**Ficha Pagamento do Trimestre Anterior**

Neste registro devem ser informadas as guias DARFs referentes aos pagamentos dos débitos do IRPJ ou à CSLL **antes** da divisão em quotas, ou seja, as guias que estão com o novo indicador como “0” (zero) no período de apuração.

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R21" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Grupo de Tributo | 01 – IRPJ  02 – IRRF  03 – IPI  04 – IOF  05 – CSLL  06 – PIS/PASEP  07 – COFINS  08 – CPMF  09 – CIDE  10 – RET/PAGAMENTO UNIFICADO DE TRIBUTOS  11 – CSRF  12 – COSIRF | Gerado conforme o tipos de Tributos listados na Rotina |
| 07 | Código da Receita | "Código da Receita" + "Variação" | Gerado conforme o Código da Receita e a Variação do Tributo |
| 08 | Periodicidade | - | Gerado conforme o período de Apuração do Tributo |
| 09 | Ano do Período de Apuração | - | Gerado conforme o Ano do Período de Apuração do Tributo |
| 10 | Trimestre do Período de Apuração | - | Gerado conforme o Trimestre do Período de Apuração do Tributo |
| 11 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 12 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 13 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 14 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 15 | Período de Apuração | - | Gerado conforme o Período de Apuração |
| 16 | CNPJ do DARF | - | Gerado conforme o CNPJ da Filial no Período de Apuração |
| 17 | Código da Receita do DARF | "Código da Receita" + "Variação" | Gerado conforme o Código da Receita e a Variação do Tributo |
| 18 | Data Vencimento | - | Gerado conforme a Data de Vencimento da Guia |
| 19 | Nº de Referência | Se o Código de Receita do DARF for "4028" (IOF-ouro), preencher com o código do município | - |
| 20 | Valor do Principal | Campo Valor do Débito preenchido com o Valor Principal das Guias | Gerado conforme o Valor Principal das Guias (Valor Apurado) |
| 21 | Valor da Multa | - | Gerado conforme o Valor das Multas das Guias |
| 22 | Valor dos Juros | - | Gerado conforme o Valor dos Juros das Guias |
| 23 | Valor pago do Débito | Valor antecipado | Gerado conforme o Valor Principal da Guia |
| 24 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 25 | Delimitador de Registro | Quebra de linha do Registro | - |

true16R3016\_1true16\_2CamposQuotas

**Pagamento do imposto trimestral em quotas**

As empresas que realizam a apuração do IRPJ e CSLL trimestral, podem optar pelo pagamento do valor devido em três quotas, conforme dispõe a Lei nº 9.430, de 27 de dezembro de 1996. Para atender esta disposição, o usuário deverá, primeiramente encerrar o Período de Apuração e Gerar a Guia DARF normalmente, seja através do Processo de geração automática, ou manualmente.  Neste registro devem ser informadas todas as guias referentes às quotas, ou seja, aquelas guias cujo novo indicador seja “1”, “2” ou “3”, independente da mesma estar baixada ou não.

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R30" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Grupo de Tributo | 01 – IRPJ  02 – IRRF  03 – IPI  04 – IOF  05 – CSLL  06 – PIS/PASEP  07 – COFINS  08 – CPMF  09 – CIDE  10 – RET/PAGAMENTO UNIFICADO DE TRIBUTOS  11 – CSRF  12 – COSIRF | Gerado conforme o tipos de Tributos listados na Rotina |
| 07 | Código da Receita | "Código da Receita" + "Variação" | Gerado conforme o Código da Receita e a Variação do Tributo |
| 08 | Periodicidade | - | Gerado conforme o período de Apuração do Tributo |
| 09 | Ano do Período de Apuração | - | Gerado conforme o Ano do Período de Apuração do Tributo |
| 10 | Trimestre do Período de Apuração | - | Gerado conforme o Trimestre do Período de Apuração do Tributo |
| 11 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 12 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 13 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 14 | Número da Quota | 1, 2 ou 3 | Informar número referente à Quota da Guia gerada. |
| 15 | Reservado | Automático | Valor Fixo preenchido com Branco(s) |
| 16 | Delimitador de Registro | Quebra de linha do Registro | - |

016\_3Parametrização no SistemaDocumentação

[Geração de Guias Automaticamente (Quotas)](https://tdn.totvs.com/pages/viewpage.action?pageId=658427821)

true17R3117\_1true17\_2CamposPagamento da Quota

**Ficha Pagamento da Quota**

Neste registro devem ser informados os dados referente aos pagamentos das guias informadas no Registro R30, ou seja, aquelas guias cujo novo indicador seja “1”, “2” ou “3” **E** que estejam baixadas.

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "R31" |
| 02 | CNPJ do Contribuinte | - | Gerado conforme o CNPJ da Filial Matriz |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação | "0" – Normal  "1" – Extinção  "2" – Fusão  "3" – Incorporação/ Incorporada  "4" – Incorporação/ Incorporadora  "5" – Cisão Total  "6" – Cisão Parcial | Gerado conforme o campo "Situação" informada na Tela de Geração da Rotina |
| 05 | Data do Evento | Data de Ocorrência do Evento  Se Situação = “0”, preencher com zeros | Gerado conforme a Data de Ocorrência do Evento informado na Tela de Geração da Rotina |
| 06 | Grupo de Tributo | 01 – IRPJ  02 – IRRF  03 – IPI  04 – IOF  05 – CSLL  06 – PIS/PASEP  07 – COFINS  08 – CPMF  09 – CIDE  10 – RET/PAGAMENTO UNIFICADO DE TRIBUTOS  11 – CSRF  12 – COSIRF | Gerado conforme o tipos de Tributos listados na Rotina |
| 07 | Código da Receita | "Código da Receita" + "Variação" | Gerado conforme o Código da Receita e a Variação do Tributo |
| 08 | Periodicidade | - | Gerado conforme o período de Apuração do Tributo |
| 09 | Ano do Período de Apuração | - | Gerado conforme o Ano do Período de Apuração do Tributo |
| 10 | Trimestre do Período de Apuração | - | Gerado conforme o Trimestre do Período de Apuração do Tributo |
| 11 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 12 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 13 | Reservado | Automático | Valor Fixo preenchido com Zero(s) |
| 14 | Número da Quota | 1, 2 ou 3 | Informar número referente à Quota da Guia gerada. |
| 15 | Período de Apuração | - | Gerado conforme o Período de Apuração do Tributo |
| 16 | CNPJ do DARF | - | Gerado conforme o CNPJ da Filial no Período de Apuração |
| 17 | Código da Receita do DARF | "Código da Receita" + "Variação" | Gerado conforme o Código da Receita e a Variação do Tributo |
| 18 | Data de Vencimento | - | Gerado conforme a Data de Vencimento da Guia |
| 19 | Nº de Referência | Se o Código de Receita do DARF for "4028" (IOF-ouro), preencher com o código do município | - |
| 20 | Valor do Principal | Campo Valor do Débito preenchido com o Valor Principal das Guias | Gerado conforme o Valor Principal das Guias (Valor Apurado) |
| 21 | Valor da Multa | - | Gerado conforme o Valor das Multas das Guias |
| 22 | Valor dos Juros | - | Gerado conforme o Valor dos Juros das Guias |
| 23 | Valor pago da Quota | - | Gerado conforme o Valor Pago da Quota |
| 24 | Reservado | Automático | Valor Fixo preenchido com Brancos(s) |
| 25 | Delimitador de Registro | Quebra de linha do Registro | - |

true19T919\_1true19\_2CamposTrailler da Declaração

| ORDEM | CAMPOS | OBSERVAÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | Tipo | Automático | Valor Fixo "T9" |
| 02 | CNPJ do Contribuinte | - | - |
| 03 | MOFG - Mês de Ocorrência do Fato Gerador | Ano do fato gerador - Mês do fato gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 04 | Situação |  |  |
| 05 | Data de Ocorrência do Evento | Data do Fato Gerador | Gerado conforme a Data Inicial informada na Tela de Geração da Rotina |
| 06 | Quantidade de Registros | - | - |
| 07 | Reservado | - | - |
| 08 | Hashcode | - | - |
| 09 | Delimitador de Registro | Quebra de linha do Registro | - |

# 05. Vídeos

Para facilitar o entendimento do processo de geração da DCTF, confira nossos vídeos abaixo:

VideosleftFicha 30

648432

Webinar

648432
