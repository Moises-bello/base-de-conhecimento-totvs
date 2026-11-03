---
content_hash: c07321a31bfd6e69a32af568ab67bdac5f3fa7f0b4cb3301987b414d25574a66
fetched_at: '2026-06-29T00:05:54.063542+00:00'
page_id: '107380950'
product: rm
source: tdn-rm
title: Como_Fazer_Venda_SPED - RET 1800
type: documentation
url: https://tdn.totvs.com/display/LRM/Como_Fazer_Venda_SPED+-+RET+1800
version: 12
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Imobiliário                     **Versão:**Todas as versões |
| **Processo** | **:** | SPED - EFD PIS /COFINS Registro 1800 |
| **Subprocesso** | **:** | RET 1800 |
| **Data da publicação** | **:** | 03/12/2013 |

**Introdução:**

Parâmetros de Entrada:

* Coligada
* Filial;
* Intervalo de Data.

Parâmetros de Saída:

* Filial
* Valor Receitas Recebidas (somatório por filial)
* Valor Receitas Financeiras e Variações Monetárias (somatório por filial)

Considerações:

* Gerar **um** único registro por filial;

* Valor **Receitas Recebidas** e **Valor Receitas Financeiras e Variações Monetárias**:

Embasamento Legal:

**IN RFB 934 – Art. 4º**

§ 5 º Para fins do disposto no caput, considera-se receita mensal o total das **receitas recebidas** (1) pela incorporadora com a venda de unidades imobiliárias que compõem cada incorporação submetida ao RET, bem como, as receitas financeiras e "variações monetárias" decorrentes dessa operação.

§ 6 º Do total das receitas recebidas, de que trata o § 5 º , poderão ser deduzidas as vendas canceladas, as devoluções de vendas e os descontos incondicionais concedidos.

(1)Análise: Receitas Recebidas são reconhecidas quando efetivamente recebida ou paga.

**Guia Prático** **EFD-Contribuições – Versão Janeiro de 2013 -** **REGISTRO 1800: INCORPORAÇÃO IMOBILIÁRIA – RET**

Este registro deve ser preenchido pela pessoa jurídica que executa empreendimentos objeto de incorporação imobiliária e que apuram contribuição social com base em Regimes Especiais de Tributação – RET.

Devem ser escriturados registros específicos para cada incorporação imobiliária, bem para cada Regime Especial estabelecido na legislação tributária, sujeitos ao pagamento mensal unificado a alíquotas diversas.

A receita da incorporação sujeita a tributação pelo RET não deve ser computada nos demais registros da escrituração, relativos a suas outras atividades empresariais, inclusive incorporações não optantes pelo RET.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "1800" | C | 004\* | - | S |
| 02 | INC\_IMOB | Empreendimento objeto de Incorporação Imobiliária, optante pelo RET. | C | 090 | - | S |
| 03 | REC\_RECEB\_RET | Receitas recebidas pela incorporadora na venda das unidades imobiliárias que compõem a incorporação. | N | - | 02 | S |
| 04 | REC\_FIN\_RET | Receitas Financeiras e Variações Monetárias decorrentes das vendas submetidas ao RET. | N | - | 02 | N |
| 05 | BC\_RET | Base de Cálculo do Recolhimento Unificado | N | - | 02 | S |
| 06 | ALIQ\_RET | Alíquota do Recolhimento Unificado. | N | 006 | 02 | S |
| 07 | VL\_REC\_UNI | Valor do Recolhimento Unificado. | N | - | 02 | S |
| 08 | DT\_REC\_UNI | Data do recolhimento unificado | N | 008\* | - | N |
| 09 | COD\_REC | Código da Receita | C | 004 | - | N |

**Campo 03 - Preenchimento:** informe o valor das receitas recebidas pela incorporadora na venda das unidades imobiliárias que compõem a incorporação.

**Campo 04 - Preenchimento:** informe o valor das receitas financeiras (2) e variações monetárias decorrentes das vendas submetidas ao RET.

(2) Análise: Receitas Financeiras são classificadas no Plano de Contas Referencial da ECD como: Variações monetárias ativas decorrentes da atualização dos direitos de crédito e das obrigações, em função de índices ou coeficientes aplicáveis por disposição legal ou contratual.

**Tratamento no sistema**:

Para classificar os valores de Receitas referente a atividades de incorporação conforme solicitado no registro 1800 (Receitas Recebidas e Receitas Financeiras), iremos utilizar os valores baixados no financeiro, gerados de acordo com o Tipo de Componente e Valores de Juros e Multa por atraso no pagamento calculados pelo módulo financeiro. Veja abaixo a relação.

|  |  |
| --- | --- |
| TOTVS Incorporação: | |
| Campo / Descrição | Tipo Componente / Valor Financeiro |
| REC\_RECEB\_RET | 1 – Entrada |
| 2 – Principal |
| **500 – CEF** |
| REC\_FIN\_RET | 3 – Juros Fixo |
| 4 – Correção Monetária |
| 5 – Alíquota |
| 6 – Juros Variáveis |
| 10 – Resíduo |
| 12 – Juros de Mora |
| 13 – Multa de Atraso |
| 18 – Juros Contratuais Mod. Indexado |
| 20 – Juros de Aditivos |
| 21 – Juros de Cont. antes do Aditivo |
| 22 – Correção Mon. Antes do Aditivo |
| TOTVS Gestão Financeira: | |
| REC\_FIN\_RET | Valor de Juros por atraso no pagamento |
| Valor de Multa por atraso no pagamento |

Obs.: Os Tipos de Componentes não listados acima não entrarão na composição dos valores desse registro.

Para geração dos dados, vamos considerar informações dos lançamentos financeiros relacionados às parcelas geradas pelo TIN.

* Linha do registro 1800 no arquivo do EFD Contribuições:

* **REC\_RECEB\_RET**

Será a ***Diferença*** entre: ***Receitas Recebidas*** e ***Devoluções de Venda***

Obs.:

1. Para compor o valor desse campo, consideramos que os valores de ‘entrada’, ‘principal’ e ‘CEF’ da parcela são carregados para o Valor Original do lançamento financeiro.
2. A diferenciação entre Receita Recebida e Devolução de Venda, é o tipo de lançamento gerado (a receber – a pagar);
3. De acordo com a legislação, poderão ser deduzidas também as Vendas Canceladas e os Descontos Incondicionais. Consideramos que as Vendas Canceladas não terão lançamentos financeiros baixados no período, pois a devolução de valores será tratada como Devolução de Venda. E os descontos incondicionais, já estarão embutidos no valor da parcela.

**Para cálculo da *Receita Recebida*:**

Soma do *Valor Original Baixado* dos Lançamentos Financeiros quando:

Obs.:

Verificar o modelo de baixa utilizado: se modelo antigo (FLAN.VALORORIGINAL) ou novo modelo (FLANBAIXA.VALORORIGINAL), para definir de qual tabela o valor original baixado deve ser carregado. Verificar o campo FPARAM.ID = -22 se ID = 0 (modelo novo de baixa) se ID = 1 (modelo antigo de baixa)

* Origem do TIN - (FLAN.CODAPLICACAO = ‘X’)
* A Receber – (FLAN.PAGREC = 1)
* Baixado (FLAN.STATUSLAN = 1 ou flan.statuslan = 4) e flanbaixa.status = 0), cuja Data de Baixa (*FLANBAIXA.DATABAIXA ou FLAN.DATABAIXA*) esteja dentro do intervalo passado como parâmetro
* Da Filial (FLAN.CODFILIAL) passada como parâmetro (Lembrando que o empreendimento está vinculado obrigatoriamente a uma filial)

**Para cálculo das Devoluções de Venda:**

Soma do Valor Original Baixado dos Lançamentos Financeiros quando:

Obs.:

Verificar o modelo de baixa utilizado: se modelo antigo (FLAN.VALORORIGINAL) ou novo modelo (FLANBAIXA.VALORORIGINAL), para definir de qual tabela o valor original baixado deve ser carregado. Verificar o campo FPARAM.ID = -22 se ID = 0 (modelo novo de baixa) se ID = 1 (modelo antigo de baixa)

* Origem do TIN - (FLAN.CODAPLICACAO = ‘X’)
* A Pagar – (FLAN.PAGREC = **2**)
* Baixado (*FLANBAIXA.STATUS = 0*  *ou FLAN.STATUS = 1* ), cuja Data de Baixa (*FLANBAIXA.DATABAIXA* *ou* *FLAN.DATABAIXA*) esteja dentro do intervalo passado como parâmetro
* Da Filial (FLAN.CODFILIAL) passada como parâmetro

Obs.:

Se o valor REC\_RECEB\_RET calculado for negativo (quando o valor das devoluções de vendas for maior que o valor das receitas), passar ZERO, pois o validador da EFD não aceita valor negativo neste campo.

* **REC\_FIN\_RET**

Serão a Soma dos valores recebidos que compõem a parcela, com exceção do valor principal que será carregado como Receita Recebida. Esses valores serão carregados de acordo com os tipos de componentes citados acima, acrescidos dos valores de juros e multa por atraso, quando houver.

Dependendo da parametrização da base, os valores referentes aos tipos de componentes podem estar no lançamento financeiro como ‘*Valores Opcionais’* ou como ‘*Valores de Integração*’. Será necessário identificar como a base está parametrizada, para saber em quais campos buscar esses valores.

Os lançamentos financeiros pesquisados serão:

* Origem do TIN - (FLAN.CODAPLICACAO = ‘X’)
* A Receber – (FLAN.PAGREC = 1)
* Baixado (FLAN.STATUSLAN = 1 ou flan.statuslan = 4) e flanbaixa.status = 0), cuja Data de Baixa (*FLANBAIXA.DATABAIXA ou FLAN.DATABAIXA*) esteja dentro do intervalo passado como parâmetro
* Da Filial (FLAN.CODFILIAL) passada como parâmetro (Lembrando que o empreendimento está vinculado obrigatoriamente a uma filial).

##### API para RET1800:

A partir da versão **12.1.129** foi disponibilizado uma API para retornar os dados da RET1800. Para realizar o consumo da API é preciso utilizar o método POST informando a '<http://localhost:8052/api/imb/v1/realestates/registry1800>'. Para que a API retorne informações o corpo da mensagem precisa ter o seguinte JSON:

 {   
     "CodigoColigada" :"1", – Código do Empreendimento  
     "CodigosFiliais" :[1,2],  – Lista de Filiais  
     "DataInicial" :"2000-01-01",  – Data Inicial  
     "DataFinal" : "2020-12-31"  – Data Final  
 }

##### API para RET1800 sem uso de licença:

A partir da versão **12.1.2209** foi disponibilizado uma API para retornar os dados da RET1800 sem necessidade do uso de licença. Para realizar o consumo da API é preciso utilizar o método POST informando a '<http://localhost:8051/api/imb/v1/efd/registry1800>'. Para que a API retorne informações o corpo da mensagem precisa ter o seguinte JSON:

 {   
     "CodigoColigada" :"1", – Código do Empreendimento  
     "CodigosFiliais" :[1,2],  – Lista de Filiais  
     "DataInicial" :"2000-01-01",  – Data Inicial  
     "DataFinal" : "2020-12-31"  – Data Final  
 }

Importante:

Essa API irá ser utilizada para realizar o envio das informações da RET1800 para integração com o Protheus.

**Como fazer:**

Para geração do RET 1800, é necessário acessar  o menu Cadastro | Básicos | Filiais | Edita a filial desejada | Anexos | Dados Fiscais | Tributos | Deve-se marcar a *flag* "Apura pelo Regime Especial Tributação".

Ou se preferir por ser feito também acessando Cadastro | Empreendimento | Editar | Integração | Gestão Financeira | Filial | Edita a Filial | Anexos | Dados Fiscais | Tributos | Deve-se marcar a *flag* "Apura pelo Regime Especial Tributação".

Verifique se existe na tela tributos a tributação do tipo RET conforme a imagem abaixo, caso não tenha, favor registrar esse tributo.  
  
  
  
favor verificar e seguir os passos desses dois links abaixo caso queira mais detalhes sobre o cadastro e parametrização do tributo do tipo RET : 

Esse primeiro link ajuda a criar os períodos de cada tipo de tributação, caso não tenha.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024406792-Cross-Segmentos-Linha-RM-FIS-Inserir-M%C3%BAltiplos-Per%C3%ADodos>

Essa documentação ensina de forma detalhada toda a parametrização do tipo RET.  
<https://tdn.totvs.com/pages/releaseview.action?pageId=320378257>
