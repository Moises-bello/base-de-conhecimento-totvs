---
content_hash: 97e229153e7180b318b6734c1db9c30d0008e054d1bc15ed30980f186b4c1f48
fetched_at: '2026-06-29T00:11:15.693668+00:00'
page_id: '661867357'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Fundo Promocional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=661867357
version: 49
---

**ÍNDICE**

---

### **Introdução**

---

O cadastro de fundo promocional visa agregar as cobranças do fundo promocional para os contratos de aluguel, possibilitando um controle maior sobre este tipo de cobrança e sua posterior geração, aplicando valores ou percentuais, reajustes ou cobranças em dobro.

### **Procedimentos para utilização**

---

Para cadastrarmos um fundo promocional, precisaremos dar a permissão ao cadastros de fundo promocional que se encontra em *Segurança / Perfil.*

Habilitando esta permissão, basta ir no menu *Shopping / Fundo Promocional* e realizar um cadastro.

Segue uma breve descrição dos campos:

* **Coligada**: A coligada onde serão gerados os lançamentos do fundo promocional. Pode ser diferente da coligada dos contratos associados.
* **Descrição**: Descrição do cadastro.
* **Aplicar reajuste do contrato:** A opção aplicar reajuste, define se o fundo deverá ser reajustado. O reajuste ocorrerá quando o tipo de cobrança é definido como "Valor" e o processo de reajuste é executado para o contrato associado ao fundo de cobrança.
  + Processo do reajuste de fundo promocional
    - Serão utilizados os mesmos índices cadastrados no contrato para reajustar o fundo associado.
    - O valor do fundo promocional será reajustado independente da data de inicio de cobrança.
    - A data do reajuste do fundo é a mesma data do reajuste do contrato de locação. Esta data e valor reajustado serão preenchidos na aba histórico de valores.
    - Quando houver a geração do lançamento financeiro, ele irá utilizar o início do período da parcela e gerar um lançamento de fundo com esta mesma data,  O valor então será definido através da data inicial e final do histórico. Se existe reajuste neste período ou não.
* **Tipo de evento financeiro:** O evento financeiro que será utilizado para geração do fundo promocional. Somente eventos do tipo "Fundo Promocional" podem ser associados.
* **Parâmetros de integração financeira:** Os parâmetros que serão utilizados para geração do fundo promocional.
* **Tipo de cobrança:** Valor ou percentual.
* **Fórmula de cálculo do Fundo Promocional**: Permite associar uma fórmula que irá realizar o cálculo do fundo através das variáveis disponíveis. Para saber mais sobre estas variáveis, [consulte a documentação aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=823802112)

Importante

A fórmula de cálculo do fundo promocional, somente poderá ser utilizada quando o tipo de cobrança for por **valor**. É importante notar que, visto que este cálculo está sendo realizado através da fórmula, **não será possível** utilizar o processo de alteração de valor de fundo, nem mesmo o reajuste. Todo e qualquer cálculo para este contrato deverá ser realizado através da fórmula.

Além disto, os fundos promocionais para contratos que estão definidos como pro-rata **não poderão ser calculados** via fórmula.

Quando a cobrança do fundo é do tipo Percentual, teremos uma opção nova que é a cobrança incidindo no cálculo do aluguel complementar (faturamento). Para que isso aconteça, ao cadastrar o contrato no template do fundo, basta marcar a opção "Considerar somente no faturamento".

Para entender mais sobre essa cobrança, acesse a página a seguir [(clique aqui).](https://tdn.totvs.com/pages/viewpage.action?pageId=799265691)

Quando o contrato de locação associado ao template possui cálculo pró-rata, o sistema irá realizar o cálculo pró-rata do fundo promocional quando necessário. Ressaltamos que apenas cobranças de valor fixo, terão influência de um cálculo pró-rata. Para FPP's calculados por percentual o sistema irá considerar sempre o valor total do período.

Quando um aditivo de alteração de locatário ser executado numa data que incide num período de fundo promocional gerado, será gerado um cálculo pró-rata entre o locatário antigo e o novo, com a correta proporção de valores, na mesma forma que ocorre nos lançamentos de locação. Neste período, então, existirão dois lançamentos de FPP.

### **Geração e exclusão de lançamentos para fundo promocional**

---

Toda a geração de lançamentos para fundo promocional é realizada através da [geração de lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=435105008) do contrato de aluguel, com exceção da opção "Considerar somente no faturamento". Quando essa opção está marcada, toda a geração e exclusão de lançamentos de fundo promocional serão geradas através dos processos de geração de aluguel complementar.

Para a geração de lançamentos do fundo promocional, o contrato de locação deverá estar associado a um template de fundo promocional, com todos os parâmetros preenchidos como exemplificado na imagem acima.

Para entender como anexar um contrato de aluguel a um template de fundo promocional, [veja o procedimento seguindo este link (clique aqui).](https://tdn.totvs.com/display/LRM/Fundo+Promocional+-+Anexos+-+Contratos+do+Fundo+Promocional)

Estando o cadastro associado e o fundo preenchido, Ao gerar os lançamentos do contrato de locação o sistema irá verificar se para este contrato existe fundo promocional cadastrado.

Os lançamentos, serão incluídos num evento financeiro do tipo "**Fundo Promocional**", e obedecerão o parâmetro de dia de vencimento cadastrado [no anexo de contrato do fundo promocional.](https://tdn.totvs.com/display/LRM/Fundo+Promocional+-+Anexos+-+Contratos+do+Fundo+Promocional)

O mês e o ano do vencimento da parcela do fundo será calculado a partir da mesma competência da parcela de locação.

Para excluirmos os lançamentos de um fundo promocional, o processo também é realizado através do contrato de locação, utilizando o [processo de exclusão de lançamentos financeiros.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105003)

A partir da versão 12.1.2502 ao gerar os lançamentos financeiros de fundo promocional, o sistema irá sempre preencher o campo *Mês/Ano da Competência*, com a data da competência da parcela de fundo promocional gerada. Este campo pode ser encontrado no próprio lançamento financeiro na aba *"Dados Adicionais".*

---

### **Particularidades na Geração de Lançamentos de Fundo Promocional**

Algumas configurações podem ser feitas na geração dos lançamentos de Fundo Promocional:

**Data de Emissão**  
O sistema permite que definir datas específicas para os campos de Emissão das parcelas geradas utilizando: **Primeiro dia da competência ou Último dia da competência**.  
Para configurar, acesse os Parâmetros > *Assistente de Implantação de Processos > Imobiliária > Aluguel,* na opção Data de Emissão do Fundo Promocional: poderá ser definida uma destas opções;

1. **Primeiro dia da competência**: Ao selecionar esta opção, o sistema irá registrar na Data de Emissão do lançamento do Fundo Promocional o primeiro dia da competência referente à data informada no contrato.
2. **Último dia da competência**: Quando selecionada, o sistema registrará na Data de Emissão do lançamento do Fundo Promocional a data correspondente ao último dia da competência referente à data informada no contrato.

**Variáveis pré definidas (Histórico do lançamento)**

Foram criadas duas variáveis pré-definidas: **[ICOMP] e [FCOMP] .**   
Ao serem inseridas no Histórico do Lançamento (no cadastro de Evento Financeiro), e se esse tipo de evento estiver especificado no contrato de aluguel, os lançamentos gerados do Fundo Promocional incluirão no campo Histórico do Lançamento as datas de Início e Fim da competência, referentes à data configurada no contrato de locação.

### **Cobrança em dobro**

---

Através do anexo de cobrança em dobro, poderemos parametrizar competências onde existirão cobranças em dobro, de acordo com os parâmetros definidos neste cadastro.

Para saber como cadastrar a cobrança em dobro, [veja o procedimento seguindo este link (clique aqui).](https://tdn.totvs.com/pages/viewpage.action?pageId=676048646)

#### **Geração não agregada (Disponível a partir da versão 12.1.2502)**

---

Com a opção de geração não agregada, o sistema gerará lançamentos separados de fundo em dobro, durante o processo de geração de lançamentos.

Esta separação além de permitir um controle mais detalhado de cada parcela gerada em dobro, permite que sejam utilizados parâmetros financeiros distintos, possibilitando então realizar rateios de centro de custo / naturezas orçamentárias financeiras diferentes do lançamento original.

Todos os lançamentos em dobro gerados dessa forma, passam a compor um novo evento financeiro que abriga todos os registros gerados pelo processo.

* É importante notar que apesar do cadastro ser flexível, não deve ser utilizado gerações hibridas, ou seja, em determinada competência não agregada e em outra competência, agregada. Recomendamos que siga o mesmo padrão para todas as competências onde deve incidir cobrança em dobro.
* No processo de cancelamento de lançamento financeiros, além da exclusão das parcelas do fundo promocional, o sistema irá automaticamente também excluir as parcelas do evento financeiro gerado para o processo de fundo em dobro, desde que estejam dentro do período escolhido para cancelamento.
* Não será possível cancelar através do processo quando um dos lançamentos (Origem ou Em Dobro) esteja com o status igual a "Baixado" ou "Baixado Parcialmente". O cancelamento é sempre feito para as duas parcelas. Caso uma destas esteja, por algum motivo, bloqueada o sistema não prosseguirá com o cancelamento.

### Rateio de Centro de Custo

---

O rateio de centro de custo para lançamentos de fundo promocional, irá respeitar, primeiramente os Centros de Custos cadastrados no(s) imóvel(is) associado(s) ao contrato.

Caso o imóvel não possua centro de custo associado, será sempre utilizado o centro de custo do parâmetro de integração financeira do Fundo Promocional.

A natureza orçamentária financeira a ser utilizada no rateio será sempre a natureza cadastrada no parâmetro de integração financeira.

É importante ressaltar que, caso o centro de custo e natureza orçamentária financeira sejam parametrizados como obrigatórios no rateio, os lançamentos **não poderão** ser gerados caso os mesmos **não** estejam parametrizados no imóvel ou no parâmetro de integração.

### Cálculos do fundo promocional com pro-rata e carência

---

É importante notar que, quando existem períodos de carência que percorrem parte de competência do fundo promocional, o sistema irá proporcionalizar esses valores de acordo com os exemplos abaixo.

Temos o pro-rata do fundo promocional em diversas situações, como por exemplo:

* Contrato de locação com período de carência para fundo promocional;
* Alteração de valores do fundo promocional na mesma competência;
* Reajuste do contrato de locação.

Exemplos de cálculos

#### Exemplo 1 - Calculo de fundo promocional (Valor) pro-rata, com proporcionalização de valores na mesma competência devido a carência de contrato

**Período fundo inicial..........................: 01/02/2024 período fundo final: 14/02/2024**  
Nº Dias Mês.....................................................: [30] (Considera o mês comercial)  
Fator diário.......................................................: (Valor / Nº Dias Mês) => (1200/30)=40  
Quant. dias.......................................................: [14]  
Período carência............................................: Inicial [01/02/2024]   Final [14/02/2024]  
Quant. dias carência.....................................: [14]  
Quant. dias deduzindo a carência: [00] **(O período inteiro encontra-se em carência, então não há cobrança)**  
Cálculo pró-rata.............................................: (Dias \* Proporção diária)  
Valor pró-rata..................................................: ( 00 \* 40   ) = 0  
**Período fundo inicial.........................: 15/02/2024 período fundo final: 29/02/2024**  
Nº dias mês....................................................: [30] (Considera o mês comercial)   
Fator diário.....................................................: (Valor / Nº Dias Mês) => (1193,79/30)=39,793  
Quant. dias.....................................................: [15]  
Período carência..........................................: Inicial [15/02/2024]   Final [15/02/2024]  
Quant. dias carência...................................: [01]  
Período carência..........................................: Inicial [25/02/2024]   Final [29/02/2024]  
Quant. dias carência...................................: [05]  
Quant. dias deduzindo a carência: [09] (**Os dias que irão incidir cobrança para este fundo promocional**)  
Cálculo pró-rata...........................................: (Dias \* Proporção diária)  
Valor pró-rata................................................: ( 09 \* 39,79   ) = 358,14

**O valor da parcela é neste caso, R$ 358,14 nesta competência.**

**No exemplo acima o sistema proporcionalizou os valores de acordo com o período de carência e o período do fundo promocional**

#### Exemplo 2 - Calculo de fundo promocional (Percentual) pro-rata, com proporcionalização de valores na mesma competência devido a carência de contrato e alteração de valor devido a reajuste de contrato

Como o valor é percentual, o sistema determina o fator diário, levando em conta o valor percentual do fundo promocional, o valor do contrato no período e os possíveis períodos de carência, que podem ou não existir durante a competência.

Período de aplicação dos valores no contrato:

[01/02/2024] a [14/02/2024] Valor contrato: [R$ 5.000,00]  
[15/02/2024] a [29/02/2024] Valor contrato: [R$ 4.974,14]

Período de carência:

[15/01/2024] a [15/02/2024]  
[25/02/2024] a [10/03/2024]

[01/02/2024] [Sim]        [5,00%]         [Período em carência]  
[02/02/2024] [Sim]        [5,00%]         [Período em carência]  
[03/02/2024] [Sim]        [5,00%]         [Período em carência]  
[04/02/2024] [Sim]        [5,00%]         [Período em carência]  
[05/02/2024] [Sim]        [5,00%]         [Período em carência]  
[06/02/2024] [Sim]        [5,00%]         [Período em carência]  
[07/02/2024] [Sim]        [5,00%]         [Período em carência]  
[08/02/2024] [Sim]        [5,00%]         [Período em carência]  
[09/02/2024] [Sim]        [5,00%]         [Período em carência]  
[10/02/2024] [Sim]        [5,00%]         [Período em carência]  
[11/02/2024] [Sim]        [5,00%]         [Período em carência]  
[12/02/2024] [Sim]        [5,00%]         [Período em carência]  
[13/02/2024] [Sim]        [5,00%]         [Período em carência]  
[14/02/2024] [Sim]        [5,00%]         [Período em carência]  
[15/02/2024] [Sim]        [5,00%]         [Período em carência]  
[16/02/2024] [Não]       [5,00%]         [R$ 8,29]  
[17/02/2024] [Não]       [5,00%]         [R$ 8,29]  
[18/02/2024] [Não]       [5,00%]         [R$ 8,29]  
[19/02/2024] [Não]       [5,00%]         [R$ 8,29]  
[20/02/2024] [Não]       [5,00%]         [R$ 8,29]  
[21/02/2024] [Não]       [5,00%]         [R$ 8,29]  
[22/02/2024] [Não]       [5,00%]         [R$ 8,29]  
[23/02/2024] [Não]       [5,00%]         [R$ 8,29]  
[24/02/2024] [Não]       [5,00%]         [R$ 8,29]  
[25/02/2024] [Sim]        [5,00%]         [Período em carência]  
[26/02/2024] [Sim]        [5,00%]         [Período em carência]  
[27/02/2024] [Sim]        [5,00%]         [Período em carência]  
[28/02/2024] [Sim]        [5,00%]         [Período em carência]  
[29/02/2024] [Sim]        [5,00%]         [Período em carência]

**Neste exemplo o sistema considerou apenas os dias onde não houve carência e proporcionalizou o percentual baseado no fator de dias utilizado.**

Valor do contrato: R$ 4.974,14  
Percentual do fundo promocional:  5,00%  
**Valor da parcela do Fundo Promocional = R$ 74,61**

#### Exemplo 3 - Calculo de fundo promocional (Percentual) pro-rata, com proporcionalização de valores na mesma competência devido a carência de contrato e alteração de valor devido a escalonamento e aditivo.

Como o valor é percentual, o sistema determina o fator diário, levando em conta o valor percentual do fundo promocional, o valor do contrato no período e os possíveis períodos de carência, que podem ou não existir durante a competência.

Período de aplicação dos valores no contrato:

[01/09/2024] a [26/09/2024] Valor contrato: [R$ 4.974,14]  
[27/09/2024] a [30/09/2024] Valor contrato: [R$ 5.600,00] **(Alteração de valor via Aditivo)**

Período de escalonamento:

[12/09/2024] a [14/09/2024] Valor escalonado: [R$ 7.200,00]

Período de carência:

[05/09/2024] a [12/09/2024]

[01/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[02/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[03/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[04/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[05/09/2024] [Sim]         [7,00%]         [Período em carência]  
[06/09/2024] [Sim]         [7,00%]         [Período em carência]  
[07/09/2024] [Sim]         [7,00%]         [Período em carência]  
[08/09/2024] [Sim]         [7,00%]         [Período em carência]  
[09/09/2024] [Sim]         [7,00%]         [Período em carência]  
[10/09/2024] [Sim]         [7,00%]         [Período em carência]  
[11/09/2024] [Sim]         [7,00%]         [Período em carência]  
[12/09/2024] [Sim]         [7,00%]         [Período em carência]  
[13/09/2024] [Não]        [7,00%]         [R$ 16,80]  
[14/09/2024] [Não]        [7,00%]         [R$ 16,80]  
[15/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[16/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[17/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[18/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[19/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[20/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[21/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[22/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[23/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[24/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[25/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[26/09/2024] [Não]        [7,00%]         [R$ 11,61]  
[27/09/2024] [Não]        [7,00%]         [R$ 13,07]  
[28/09/2024] [Não]        [7,00%]         [R$ 13,07]  
[29/09/2024] [Não]        [7,00%]         [R$ 13,07]  
[30/09/2024] [Não]        [7,00%]         [R$ 13,07]

**Neste exemplo o sistema considerou apenas os dias onde não houve carência e proporcionalizou o percentual baseado no fator de dias utilizado, considerando o período escalonado, bem como o aditivo de alteração de valor no final do contrato.**

O valor da parcela do fundo promocional é de **R$ 271,57**

**Gerar lançamentos de fundo promocional juntamente com lançamentos de locação** *(a partir da Versão 12.1.2502)*  
Quando este parâmetro encontra-se  marcado e o fundo promocional for gerado junto com os lançamentos de locação, a carência (informada no contrato de locação) continuará sendo aplicada conforme as regras do contrato.

O sistema irá *desconsiderar a carência do contrato* ao gerar lançamentos de fundo promocional, somente quando este for gerado separadamente dos lançamentos de locação.  
Exemplo Simples para Entendimento:

* Contrato com carência de 2 meses.
* **Cenário 1**: Fundo promocional gerado junto com o lançamento de locação → **Carência aplicada**.

  + Exemplo:
    - Fundo promocional gerado em janeiro junto com locação → Será aplicado após a carência, em março.
* **Cenário 2**: Fundo promocional gerado separadamente → **Carência não aplicada**.

  + Exemplo:
    - Fundo promocional gerado emjaneiro, separadamente → Será aplicado imediatamente, em janeiro mesmo.

### **Veja mais**

---

* **[Contratos do Fundo Promocional](https://tdn.totvs.com/display/LRM/Fundo+Promocional+-+Anexos+-+Contratos+do+Fundo+Promocional)**

* **[Aplicar Reajuste](https://tdn.totvs.com/pages/viewpage.action?pageId=435104980)**
* **[Desfazer Reajuste](https://tdn.totvs.com/pages/viewpage.action?pageId=435105398)**
