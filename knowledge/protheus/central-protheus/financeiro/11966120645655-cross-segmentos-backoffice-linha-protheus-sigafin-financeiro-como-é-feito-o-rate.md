---
article_id: 11966120645655
category: Financeiro
content_hash: 9fefb2bbfb5ba2d6a9071b2902168e15abfe9be9ff20d82406226ce3a9fb725e
fetched_at: '2026-06-28T22:38:03.229094+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Financeiro - Como
  é feito o rateio de IR entre CPF pessoas físicas para aluguel '
type: support-article
updated_at: '2023-09-22T17:41:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11966120645655-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Financeiro-Como-%C3%A9-feito-o-rateio-de-IR-entre-CPF-pessoas-f%C3%ADsicas-para-aluguel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17740825110295) Tempo aproximado para leitura: **00:10:00min** **Dúvida**  
Como realizar rateio de IR para CPF em caso de Divisão de aluguéis?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução****01. VISÃO GERAL**Para atender a legislação **IN RFB nº 1.500/2014** (possibilidade da divisão dos rendimentos conforme contrato de locação), por exemplo, uma imobiliária aluga um imóvel ao qual pertence a duas pessoas físicas, cada uma com o seu percentual de propriedade sobre o imóvel. É de direito de ambos os proprietários, a divisão do rendimento oriundo deste aluguel e consequentemente o rateio do imposto de renda (desde que constatado em contrato). Foi criado no **cadastro de Fornecedor** (**MATA020**) uma nova opção, em **"Outras Ações"**, o cadastro para o **rateio do IR** progressivo por CPF.  
Este cadastro de CPF's para o **IR progressivo**, será utilizado para o cálculo do **Imposto de Renda** para cada CPF conforme percentual de cada um.  
Além disso, no envio de dados para a **DIRF**(**FINA401**), a rotina também irá verificar se existe o **rateio do** **imposto de renda** para mais de um CPF, enviando o rendimento e o valor do tributo de cada um. Caso não exista o rateio entre mais de um CPF, o envio para a **DIRF** irá considerar o CPF cadastrado no **Fornecedor** (campo **A2\_CPFIRP**) como sendo o principal e único responsável pela **retenção do imposto de renda**.  
  
**02.****CADASTRO DOS CPF(S) PARA RATEIO****1.** No **Financeiro** **(SIGAFIN**), acesse **Atualizações / Cadastros / Fornecedor (MATA020)**. Cadastre um **Fornecedor do tipo Jurídico** (**A2\_TIPO**) com retenção de IRRF (**A2\_CALCIRF**). Informe o campo **IRRF Prog**= Sim (**A2\_IRPROG**) e informe o CPF principal no campo **CPF IR Progr**(**A2\_CPFIRP**). Uma vez preenchidos estes campos, será permitido acessar a opção "**CPFs IR Progr.**" em **"Outras** **Ações"**, caso contrário, será exibida a mensagem para preenchimento destes campos.  
  
**Importante**  
Quando o **tipo do Fornecedor** (**A2\_TIPO**) for **pessoa física**, não haverá a necessidade de preencher os campos **IRRF Prog** (**A2\_IRPOG**) e **CPF IR Progr**(**A2\_CPFIRP)**para acessar a opção "**CPF's IR Progr.**"  
  
**2.** Na tela para cadastros do **"CPFs IR Progr"**, o CPF informado na tela de Fornecedor já virá pré-preenchido. Informe o % de rateio e o nome para este CPF e cadastre os outros CPF(s) necessários.   
**Importante**A soma do percentual de todos os CPFs cadastrados deverá ser 100%.  
  
**3.** Confirme a tela de cadastro do**"CPFs IR Progr"**. Neste momento, a tabela **FKJ-Cadastro de CPF IR Progressivo** não foi gravada, a mesma será gravada somente na confirmação do **cadastro do Fornecedor**, idem para a exclusão. No caso de alteração, as informações já serão salvas ao confirmar a tela do **"CPFs IR Progr"**, sem a necessidade de confirmar a tela de **cadastro do Fornecedor.**

**4.** Para as alíquotas de **rateio por CPF**, devem ser adicionado na rotina de **Tabela IRRF no módulo Configurador**

**Processo a ser executado:**

No **Configurador,** acesse **AMBIENTE\ CADASTROS\ TABELA IRRF**e preencha a Tabela conforme abaixo:

Tabela **IRRF 2023** - A partir de maio de 2023.

| Base de cálculo | Alíquota | Dedução |
| --- | --- | --- |
| Até R$ 2.112,00 | - | - |
| De R$ 2.112,01 até R$ 2.826,65 | 7,5% | R$ 158,40 |
| De R$ 2.826,66 até R$ 3.751,05 | 15,0% | R$ 370,40 |
| De R$ 3.751,06 até R$ 4.664,68 | 22,5% | R$ 651,73 |
| Acima de R$ 4.664,68 | 27,5% | R$ 884,96 |

**Importante: Acima de 4664,68 informe 999999999.99.**

O compartilhamento das tabelas **FKJ** e **SA2**deve ser igual, conforme padrão do sistema, para garantir a consistência dos dados.  
  
**03.** **EXEMPLO DE UTILIZAÇÃO**[**IR na emissão (Contas a pagar)**](https://tdn.totvs.com/display/public/PROT/Cadastro+de+CPF%27s+rateio+de+IRRF+progressivo+enviado+a+DIRF#tabs-passo1)

[**IR na emissão (Documento de entrada)**](https://tdn.totvs.com/display/public/PROT/Cadastro+de+CPF%27s+rateio+de+IRRF+progressivo+enviado+a+DIRF#tabs-passo2)

[**IR na baixa**](https://tdn.totvs.com/display/public/PROT/Cadastro+de+CPF%27s+rateio+de+IRRF+progressivo+enviado+a+DIRF#tabs-passo3)

**1.** Cadastre o título a pagar pela rotina **Contas a Pagar** (**FINA050**) informe uma **Natureza** e **Fornecedor** que calculam **IR na emissão**.  
  
**2.** Ao informar o valor do título, será calculado o valor do **IR** considero 100% do valor para o **Fornecedor**. O **rateio do IR** somente irá ocorrer ao informar o campo **"Gera Dirf"**  = Sim (E2\_DIRF) e o **código de retenção** (**E2\_CODRET**) pertencente no parâmetro [**MV\_RETIRRT**](https://tdn.totvs.com/pages/releaseview.action?pageId=547241966)  
  
**3.** Ao realizar o recálculo considerando o rateio entre os CPF(s) cadastrados, o campo **Valor do IRRF** (**E2\_IRRF**) será preenchido com a somatória do valores calculados de **IR** para cada CPF. Para verificar os detalhes do cálculo de cada CPF, em **"Outras Ações"**, acesse a opção **"Rateio de IR Progressivo".**Será exibida a tela com as informações de base, alíquota utilizada, valor do **IR** calculado individualmente.  
  
**4.** Ao salvar o título, a geração dos títulos de **IR** será proporcional, ou seja, será gerado um **TX** de **IR** para cada CPF informado anteriormente.

**Importante**  
Caso seja informado um **código de retenção** que não pertence ao parâmetro **MV\_RETIRRT**, os títulos a pagar serão inclusos sem rateio, ou seja 100% do valor será retido para o **Fornecedor** em questão sem levar em consideração seus cadastros na tabela **FKJ**(**CADASTRO DE CPF IR PROGRESSIVO**).

A opção **"Rateio de IR Progressivo"** somente estará disponível quando houver o cálculo do **rateio de IR** por CPF.  
Ao gerar os dados para a **DIRF** **(FINA401)**, os títulos de imposto de renda deste **Fornecedor** serão enviados para a tabela **SR4-Itens DIRF/Informe Rendimento**, rateados conforme o percentual cadastrado para cada CPF.

**04.****EXEMPLO DE CÁLCULO COM RATEIO DE IR****Tabela Progressiva**:

A partir de maio de 2023.

| Base de cálculo | Alíquota | Dedução |
| --- | --- | --- |
| Até R$ 2.112,00 | - | - |
| De R$ 2.112,01 até R$ 2.826,65 | 7,5% | R$ 158,40 |
| De R$ 2.826,66 até R$ 3.751,05 | 15,0% | R$ 370,40 |
| De R$ 3.751,06 até R$ 4.664,68 | 22,5% | R$ 651,73 |
| Acima de R$ 4.664,68 | 27,5% | R$ 884,96 |

  
[**Inclusão de titulo com rateio do IR progressivo**](https://tdn.totvs.com/display/public/PROT/Cadastro+de+CPF%27s+rateio+de+IRRF+progressivo+enviado+a+DIRF#)

[**Cumulatividade de base entre fornecedores diferentes**](https://tdn.totvs.com/display/public/PROT/Cadastro+de+CPF%27s+rateio+de+IRRF+progressivo+enviado+a+DIRF#)

Cadastrado o **Fornecedor** abaixo:  
FOR001 - Fornecedor PJ  
Nome: LOCAIMOVEIS LTDA  
CGC 01.002.003/0001-01  
Para este Fornecedor, informado o **IR Prog = Sim** (**A2\_IRPROG**) e o **CPF IR Progr = 80619067756** (**A2\_CPFIRP**).  
Além deste proprietário, possui mais um proprietário, logo acesse o cadastro de **"CPFs IR Progr."** em "**Outras** **Ações"**, informando o percentual de cada CPF:  
CPF 1: 806.190.677-56 - 60% - Nome: José da Silva  
CPF 2: 704.371.144-49 - 40% - Nome: Maria da Silva  
  
Incluso um **título a pagar** com **código de retenção** 3208 (Aluguéis e royalties) no valor de R$10.000,00 que reterá o **IR**. O cálculo de **IR** (tanto na emissão como na baixa), considerando o rateio de CPF será conforme abaixo :  
**1)** **Código retenção** 3208  
CPF 1: 806.190.677-56 - Nome: Jose da Silva  
Rendimento: 60% de R$ 10.000,00 = R$ 6.000,00  
Alíquota: 27,5%  
Tributo: R$ 6.000,00 \* 27,5% - Deduções = R$ 780,64  
  
**2) Código retenção** 3208  
CPF 2: 704.371.144-49 - Nome Maria da Silva  
Rendimento: 40% de R$ 10.000,00 = R$ 4.000,00  
Alíquota: 22,5%  
Tributo: R$ 4.000,00 \* 22,5% - Deduções = R$ 263,87  
  
Neste exemplo acima, seria gerado um **TX** no valor de R$ 780,64 para o CPF 1 e outro **TX** no valor de R$ 263,87 para o CPF 2, totalizando R$ 1.044,51.  
Na geração dos dados para a **DIRF**, deverá ser enviado para o CPF 1, o rendimento de R$ 6.000,00 e retenção de R$ 780,64 e para o CPF 2, o rendimento de R$ 4.000,00 e retenção de 263,87.  
  
Caso somente possua o cadastro de CPF no **Fornecedor**, será considerado 100% para este, sendo enviada a informação de CPF do campo **A2\_CPFIRP** e o nome do **Fornecedor** (**A2\_NOME**) para a **DIRF**.  
  
**Saiba mais**  
[IRRF - Aluguel - Divisão de Rendimentos entre Beneficiários Pessoas Físicas](https://tdn.totvs.com/pages/releaseview.action?pageId=513418300)  
[IRRF - Pagamento de aluguel - incidência de juros e multa na base de cálculo do IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=187535634)
