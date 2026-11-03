---
content_hash: e227c02121d227d3409b0d2ca4151dd9f27133087caa192c3b254db48e1494c6
fetched_at: '2026-06-29T00:06:13.901927+00:00'
page_id: '208347682'
product: rm
source: tdn-rm
title: FOP_0002_Emissão DIRF/Informe de Rendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208347682
version: 244
---

# Parametrização do menu de emissão da rotina DIRF / Informe de Rendimentos

|  |  |
| --- | --- |
| **Produto:** | TOTVS Folha de Pagamento |
| **Versões:** | * 12.1.2502.267 * 12.1.2506.228 * 12.1.2510.157 ou superior |
| **Ocorrência:** | Parametrização do menu de geração do arquivo DIRF e emissão do Informe de Rendimentos |
| **Ambiente:** | Rotinas Anuais - DIRF / Informe de Rendimentos |
| **Observações:** | DIRF 2026 - Ano Base 2025 |
| **Passo-a-Passo** | Prazo de Entrega da DIRF A entrega da DIRF deve ser realizada até o último dia útil do mês de fevereiro do ano subsequente àquele em que os rendimentos tenham sido pagos ou creditados.  Dessa forma, a DIRF 2026 (ano-calendário 2025) deverá ser transmitidaaté as **23h59min59s do dia 27 de fevereiro de 2026**, salvo alteração por ato oficial da Receita Federal.   ---  Disponibilização das Versões As versões para geração da DIRF estarão disponíveis na área pública da **Central de Download**, no Portal do Cliente TOTVS.   ---  Como realizar o download Para baixar a versão correspondente, siga os passos abaixo:   1. Acesse: **[www.totvs.com/suporte](http://www.totvs.com/suporte)** 2. Faça login com seu **e-mail e senha**; 3. No menu superior, clique em **Downloads e Atualizações**; 4. Na lista de produtos, selecione **Produto RM**; 5. Escolha a sua **versão**; 6. Selecione **CorporeRM**; 7. Na grade de downloads, serão exibidos todos os arquivos disponíveis para a série selecionada.  💡 Dica Para facilitar a busca, utilize o campo de pesquisa da grade de downloads e digite o nome completo ou parte do nome do arquivo desejado, como por exemplo: **“Patch”**. |

1true1Parâmetros para GeraçãoParâmetros para GeraçãoMapeamentotrue2-1Parâmetros de SeleçãoParâmetros de Seleção

## Informe de Rendimentos | DIRF em Arquivo | DIRF para Confência

Para emissão dos relatórios, acesse: Anuais | DIRF/Informe de Rendimentos | DIRF/Informe de Rendimentos

Ao acessar o menu, será apresentada a tela de parametrização para geração dos relatórios.

Por meio deste módulo, é possível emitir:

* **Informe de Rendimentos** (padrão, detalhado ou em arquivo .TXT);
* **DIRF em Arquivo** (para importação no programa da Receita);
* **DIRF para Conferência** (relatório para validação visual dos dados).

---

## Quebra de Seção

É extremamente importante que a DIRF seja gerada com apenas uma seção (uma coligada por vez).

O arquivo deve estar totalmente centralizado em uma única seção.  
Não pode haver quebra de seção no arquivo da DIRF, pois isso poderá ocasionar diversos erros durante a validação ou importação no programa da Receita Federal.

---

## Código do Relatório – DIRF para Conferência

Informe o código do relatório que será utilizado quando, ao final do processo, for selecionada a opção: **“**DIRF para Conferência”

Esse relatório será utilizado exclusivamente para validação visual das informações e não poderá ser importado no programa da DIRF.

---

## Código do Relatório – Informe de Rendimentos

Informe o código do relatório que será utilizado quando for selecionada a opção:

**“Informe de Rendimentos”**

O sistema disponibiliza três modelos padrão:

* **FOPREL0008** – Informe de Rendimentos (modelo padrão)
* **FOPREL0011** – Informe de Rendimentos Detalhado
* **FOPREL0012** – Informe de Rendimentos em Arquivo TXT

Caso deseje gerar o Informe de Rendimentos em formato **.TXT**, será necessário:

1. Informar o relatório **FOPREL0012**;
2. Marcar o parâmetro **“Gerar Informe de Rendimentos em TXT”**.

---

## Observação

Caso nenhum relatório seja apresentado na tela de seleção, será necessário realizar previamente a importação dos relatórios pelo caminho: Gestão | RM Reports | Processos

As estruturas dos relatórios estão disponíveis no diretório: totvs\CorporeRM\ObjetosGerenciais\Relatórios

---

## Localização do(s) Arquivo(s)

Informe o caminho (diretório) onde o(s) arquivo(s) da DIRF será(ão) gravado(s).

Certifique-se de que o usuário responsável pela geração possua permissão de gravação na pasta informada.

2-2Aba GeralAba Geral

**Aba Geral | Após Avançar e clicar em "Adicionar Parâmetros a coligada"**

Para emissão dos relatórios verifique a *seleção de funcionários*, o *código de quebra* e *período referência*.

**1.1 Parâmetros para a geração da DIRF/Informe de Rendimentos**

* **Eventos:**

* **Evento de Restituição de IRRF**

Informe o evento de restituição de IRRF que o sistema deverá considerar no campo "Imposto de Renda Retido" do Informe de Rendimentos e da DIRF. Este evento não deve ter o código de cálculo 122-Restituição IRRF, pois, o evento de CC122 vai reduzido automaticamente o valor do IR Retido para a DIRF, não sendo necessário informa-lo neste campo e caso seja informado o valor do abatimento será duplicado. Neste campo deve ser informado apenas quando utiliza-se outro evento para restituição de IRRF que não tenha o código de cálculo 122.

* **13º Pago pela Previdência sobre Lic. Maternidade**

Preencher com o evento de **13º Salário Pago pela Previdência sobre Licença Maternidade**, lançado na ficha financeira durante o período informado no campo ‘Período Referência’para a empregada gestante com afastamento iniciado entre 12/1999 a 31/08/2003, ou para segurada empregada doméstica, contribuinte individual, trabalhadora avulsa e segurada especial. Nos demais casos este campo deverá ficar em branco.

* **Considera movimentação de períodos anteriores para transferidos**

Ao marcar este parâmetro, o sistema apresentará a mensagem abaixo:

* **Opções de seleção**

Através dessa opção é possível fazer considerações específicas para emissão dos relatórios.

 

 Os Rendimentos Recebidos Acumuladamente, podem der oriundos das decisões da Justiças do Trabalho, Federal, Estaduais e do Distrito Federal, sendo neste caso informados através do Histórico de RRA localizado no anexo do cadastro do funcionário. Quando provenientes do trabalho, devem ser informados através dos eventos com códigos de cálculo de 204 à 218. Desta forma, para os campos abaixo serão considerados Históricos de RRA + Eventos da Ficha Financeira. Para mais informações acesse o documento:

<http://tdn.totvs.com/pages/viewpage.action?pageId=208347807> 

**Selecionar funcionários e autônomos:**

***Apenas com IRRF:***Imprime apenas funcionários que sofreram desconto de IRRF;

***Com IRRF, não assalariado com rendimentos acima de R$ 6.000,00 ou assalariado com rendimentos igual ou acima de R$28.559,70:*** essa opção irá relacionar os funcionários autônomos e assalariados que, no ano calendário, entraram em alguma das condições descritas acima - (conforme IN RFB 1.216 de 15/12/2011).

***Todos:***imprime todos os funcionários com exceção daqueles que não tiveram pelo menos um dos seguintes rendimentos abaixo:

* Qualquer valor de rendimento incidente em IRRF
* Qualquer valor de desconto de IRRF
* Bolsa de Estudo Recebida por Médico-Residente
* Indenizações rescisão, PDV, acidente de trabalho
* Descontos de assistência saúde (médico - odonto - hospitalares)
* Valor de pensão ou aposentadoria por Moléstia grave ou acidente em serviço

Quando esta opção **"Todos"** é marcada, o sistema habilita o campo “**Usa filtro de seleção ao gerar DIRF em arquivo”.** Com isso, o usuário poderá gerar a DIRF em arquivo utilizando o filtro de seleção, ou seja, poderá determinar quais funcionários serão ou não enviados para o arquivo.

**Opções:**

***Usa filtro de seleção ao gerar DIRF em arquivo***

Marque este parâmetro, para que o filtro de seleção criado seja utilizado durante a geração da DIRF em arquivo.

***Selecionar apenas funcionários com CPF preenchido***

Ao marcar este parâmetro, o sistema selecionará apenas os funcionários que tenham CPF preenchidos em seus cadastros.

***Agrupar funcionários sem CPF como um único funcionário***

O sistema emitirá o relatório do Informe de rendimentos com o somatório dos valores dos funcionários que não tem CPF cadastrado.

***Desconsidera número de dependentes no mês da rescisão por transferência***

Ao marcar esta opção, os funcionários com dependentes de IRRF transferidos no mês não terão o número de dependentes deduzido em duplicidade no mês da transferência. Caso contrário, a dedução ocorrerá duas vezes.

**Associações de eventos aos “Campos” da DIRF/Informe de Rendimentos**

Na parte superior da tela de emissão dos relatórios da DIRF, existem as abas onde devem ser informados eventos correspondentes aos “Campos” da DIRF/Informe de Rendimentos.

2-3Previdência ComplementarPrevidência Complementar

## Previdência Complementar (Previdência Privada)

A partir da **DIRF 2018 (ano-base 2017)**, houve alteração na forma de tratamento das informações de **Previdência Complementar (Previdência Privada)**.

## Alteração Implementada

O registro do beneficiário passou a contemplar o novo campo:

**Indicador de Identificação da Previdência**

* Quando houver detalhamento da Previdência Complementar por operadora, o sistema assumirá **“S” (Sim)**.
* Quando não houver detalhamento, assumirá **“N” (Não)**.
* Caso a empresa não discrimine a Previdência Privada, nenhuma informação será levada para a DIRF e o indicador será gerado como **“N”**.

---

## Como Discriminar a Previdência Privada por Operadora

Caso a empresa não tenha realizado a discriminação por operadora e deseje passar a realizar, deverá seguir os passos abaixo:

### 1º Cadastrar as Operadoras

Cadastrar todas as operadoras de previdência complementar para as quais houve desconto em folha durante o ano-base.

### 2º Informar os Eventos por Operadora

Para cada operadora cadastrada:

* + Informar o(s) evento(s) utilizado(s) para desconto em folha.
  + Devem ser informados apenas eventos referentes à contribuição de Previdência Privada.
  + Não devem ser informados eventos de INSS (Previdência Social), como por exemplo o Código de Cálculo 3.

### 3º Empresas que Utilizaram Eventos Diferentes por Operadora

Caso a empresa tenha utilizado eventos distintos para cada operadora:

* + Informar, nos parâmetros da DIRF, os eventos correspondentes a cada operadora.
  + O sistema realizará automaticamente o cálculo mês a mês e levará os valores corretamente para a DIRF.

### 4º Empresas que Utilizaram o Mesmo Evento para Mais de uma Operadora

Se o mesmo evento foi utilizado para desconto de mais de uma operadora:

* + Será necessário informar na ficha financeira dos funcionários os valores rateados por operadora.

---

## Alteração Estrutural nos Parâmetros da DIRF

Até o ano-base 2016, os eventos de Previdência Complementar eram informados nos seguintes campos dos parâmetros da DIRF:

* Campo 3 – Rendimentos Tributáveis – Deduções e IRRF
* Campo 5 – Rendimentos Sujeitos à Tributação Exclusiva

A partir do ano-base 2017, esses campos foram descontinuados para essa finalidade.

Foi criado o novo campo: **“Informações de Previdência Complementar (Previdência Privada)”**

---

## Como Parametrizar a Nova Pasta

Acesse: Informações de Previdência Complementar (Previdência Privada) , clique em Novo e informe:

* CNPJ da Operadora
* Nome Empresarial

---

## Observação Importante

O sistema agrupa os eventos de:

* Folha Mensal
* 13º Salário

em um único cadastro, utilizando um **flag específico** para diferenciar os eventos de 13º salário.

---

## Flag “Subtrair Valor”

Ao inserir o evento na operadora, estará disponível o parâmetro:

**Subtrair Valor**

* Se **marcado**, o sistema irá deduzir o valor do evento no mês em que ele constar na ficha financeira.
* Se **não marcado**, o sistema somará o valor ao total do mês, mesmo que o evento seja de estorno.

---

## RTFA – Rendimentos Tributáveis – Dedução – FAPI

**FAPI (Fundo de Aposentadoria Programada Individual)**

Os eventos classificados como FAPI terão o mesmo tratamento aplicado à Previdência Privada, sendo considerados como: Rendimentos Tributáveis – Dedução – Previdência Privada.

Devem ser informados os eventos utilizados para desconto de FAPI durante o ano-base correspondente.

---

## RTPS – Rendimentos Tributáveis – Dedução – Fundo de Previdência do Servidor (Estatutário)

Nesta opção devem ser informados os eventos referentes ao Fundo de Previdência do Servidor (Estatutário) utilizados durante o ano-base.

O sistema considerará esses eventos como dedução de rendimentos tributáveis na geração da DIRF e do Informe de Rendimentos.

---

## RTEP – Rendimentos Tributáveis – Dedução – Contribuição do Ente Público

Devem ser informados os eventos utilizados para Contribuição do Ente Público, classificados como: Rendimentos Tributáveis – Dedução – Contribuição do Ente Público.

Esses eventos serão considerados como dedução na composição dos rendimentos tributáveis na DIRF, conforme a parametrização adotada pela empresa no respectivo ano-base.

2-4Campo 4Campo 4

## Aba **Campo 4 – Rendimentos Isentos e Não Tributáveis**

As Sub-Abas abaixo possuem descrição definida internamente no sistema e não podem ser modificadas pelos usuários.

Essas descrições estão parametrizadas na **Tabela Dinâmica INT41**.

* + ***Sub-Aba - Prov.Aposentadoria/Reserva/Reforma/Pensão (+ 65 anos):***

Informe os eventos que foram utilizados durante o ano a título de proventos inatividade - benefícios aos funcionários com mais de 65 (sessenta e cinco anos).

* + ***Sub-Aba - 13 Prov.Aposentadoria/Reserva/Reforma/Pensão (+ 65 anos):***

Informe os eventos que foram utilizados durante o ano a título de proventos inatividade - benefícios aos funcionários com mais de 65 (sessenta e cinco anos) de décimo terceiro salário.

* + ***Sub-Aba - Diárias/Ajuda de Custo:***

Informe os eventos de "Diárias" e "Ajuda de Custo", que tenham CC15, e foram utilizados durante o ano e não são tributáveis.

* + ***Sub-Aba - Prov.Aposentadoria p/Moléstia/Acidente emServiço:***

Informe o código dos eventos que foram utilizados durante o ano a título de proventos de pensão, aposentadoria ou reforma por moléstia grave ou por invalidez permanente (não são tributáveis).

Leia mais sobre essas verbas acessando o link:

* + ***Sub-Aba - Prov.Aposentadoria p/Moléstia/Acidente em Serviço Sobre o 13º salário:***

Informe o código dos eventos que foram utilizados durante o ano a título de proventos de pensão, aposentadoria ou reforma por moléstia grave ou por invalidez permanente (não são tributáveis), sobre 13º salario.

Leia mais sobre essas verbas acessando o link:

* + ***Sub-Aba -* Lucro/Dividendos pagos por PJ a partir de 1996:**

Informe os eventos que foram utilizados durante o ano a título de proventos correspondentes a lucros e dividendos apurados a partir de 1º de janeiro de 1996, distribuídos a sócio, acionista ou titular de pessoa jurídica submetida ao regime de tributação com base no lucro real, presumido ou arbitrado, apurados com base em balanço.

* + ***Sub-Aba - Valores pagos ao Titular ou Sócio Microempresa:***

Informar o(s) evento(s) relativo(s) aos valores pagos ao titular ou sócio de microempresa ou de empresa de pequeno porte, exceto pró-labore e aluguéis.

* + ***Sub-Aba - Indenização Rescisão Contrato Trabalho / PDV / Ac. Trab.***

Informe os eventos utilizados no pagamento de indenizações, programa de demissão voluntária ou por acidente de trabalho. Nesta pasta devem ser informados os eventos de CC 62 e 99 caso não tenham incidido em IRRF.

Existem ainda mais 3 Sub-Abas que, quando liberadas no produto, em sua versão inicial, apresentavam as seguintes descrições padrão (default):

* **Outros (especificar): Campo 5 / Linha 8**
* **Outros (especificar): Campo 5 / Linha 9**
* **Outros (especificar): Campo 5 / Linha 10**

Correspondência com a Tabela Dinâmica **INT41**:

* **1ª aba – Campo 5 / Linha 8 / Outros (especificar):** refere-se ao item **8** da Tabela Dinâmica INT41;
* **2ª aba – Campo 5 / Linha 9 / Outros (especificar):** refere-se ao código **9** da Tabela Dinâmica INT41;
* **3ª aba – Campo 5 / Linha 10 / Outros (especificar):** refere-se ao código **10** da Tabela Dinâmica INT41.

Essas descrições devem ser ajustadas conforme a necessidade de cada cliente.

Para realizar a alteração, acesse o menu Administração de Pessoal | Tabelas Dinâmicas, e em seguida, localize a tabela de código **INT41** e ajuste a descrição conforme deseja que a informação seja apresentada no Informe de Rendimentos.

**ATENÇÃO:** Na **1ª aba**, cuja descrição interna está vinculada ao item 8 correspondente da Tabela Dinâmica INT41, o sistema sempre irá gerar, na primeira linha, o evento com **código de cálculo “39 – Abono Pecuniário”,** desde que o funcionário possua esse evento na Ficha Financeira do respectivo ano-base do Informe de Rendimentos. E a partir da da 2a. linha o sistema irá imprimir a descrição do item 8 da Tabela Dinâmica e os eventos relacionados na aba.

* + ***Sub-Aba - Bolsa Estudo Médico-Residente***

*Informe o código do evento referente bolsa pago durante o ano 2017 para Medico-Residente.*

* + ***Sub-Aba - J****uros de mora recebidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função***

Informe o código do evento referente o juros de mora durante o ano base gerado.

**OBSERVAÇÃO:** A exibição correta dos eventos nesta aba está condicionada ao cumprimento dos seguintes critérios, devidamente parametrizados nos eventos/verbas, no menu Administração de Pessoal | Eventos | Eventos:

* **`FORCARINCIRRF`** = **FALSO**
* **`ISENTOIRRF`** = **VERDADEIRO**
* **`INCIRRFISENCAO`** = **704**

Ao realizar a consulta para listar os eventos, somente foi listado o evento que atende a regra citada.

2-5Campo 7Campo 7

## Aba “Campo 7 – Informações Complementares”

### Sub-aba – Informações Complementares

Neste campo devem ser informados os códigos dos eventos utilizados durante o ano-base que precisam ser demonstrados como Informações Complementares no Informe de Rendimentos.

Os eventos cadastrados nesta aba não compõem os valores principais dos quadros de rendimentos, mas terão seus valores detalhados no campo destinado às informações complementares, conforme exigência legal.

2-6Reembolso MédicoReembolso Médico

## Aba “Operadora de Assistência à Saúde”

A partir da DIRF 2018 (ano-base 2017), houve alterações no processo de Operadora de Assistência à Saúde, mantendo-se o mesmo procedimento nas versões posteriores.

### Conversão de Operadoras já cadastradas

Caso já existam operadoras cadastradas na aba antiga, será necessário realizar a conversão acessando: Anuais | DIRF/Informe de Rendimentos | Conversão de Operadora Perfil x Cadastro

A conversão pode ser realizada:

* Por coligada específica; ou
* Para todas as coligadas.

Ao processar a conversão, o sistema copiará todas as operadoras cadastradas para o novo caminho: Anuais | DIRF/Informe de Rendimentos | Operadora de Saúde

Durante esse processo, o sistema criará automaticamente umcódigo sequencial para cada operadora convertida.

---

### Novo módulo de cadastro

Também foi disponibilizado o módulo: eSocial | Operadora Saúde | Cadastro Operadora de Saúde

⚠️ **Importante:**  
O sistema somente levará as operadoras para a DIRF se elas estiverem cadastradas neste novo módulo.

---

### Regras importantes de parametrização

* Não é permitido informar o mesmo evento para mais de uma operadora de saúde.  
  Caso isso ocorra, os valores serão duplicados na geração da DIRF.
* Empresas que trabalham com mais de uma operadora devem possuir pelo menos um evento exclusivo para cada operadora.
* Para que as informações de despesas médico-odonto-hospitalares sejam demonstradas corretamente no Informe de Rendimentos e na DIRF, recomenda-se revisar a parametrização conforme o roteiro:[Histórico de Assistência a Saúde](https://tdn.totvs.com/pages/viewpage.action?pageId=210052115)

---

### Dependentes com 8 anos ou mais sem CPF

Nos casos em que houver dependentes com idade igual ou superior a 8 anos e sem CPF informado no cadastro, o sistema:

* Não gerará o valor de assistência à saúde para o dependente na DIRF;
* Somará o valor correspondente ao dependente ao valor do titular;
* Ignorará informações de reembolso referentes ao dependente.

Nessa situação, será exibido aviso na aba Logs ao gerar o arquivo da DIRF, informando que o registro do dependente não foi gerado por ausência de CPF.

2Opções para GeraçãoOpções para Geração

## Opções para Geração

Ao acessar o menu Anuais | DIRF/Informe de Rendimentos | DIRF/Informe de Rendimentos e avançar a primeira tela (Perfil de Parâmetros), será possível selecionar, na parte superior da tela, o tipo de emissão desejado.

As opções disponíveis são:

* **DIRF em Arquivo**;
* **DIRF para Conferência**;
* **Informe de Rendimentos**.

Cada opção atende a uma finalidade específica, permitindo a geração do arquivo oficial para entrega, a conferência prévia das informações ou a emissão do informe individual para os beneficiários.

Opções para Geraçãotrue2-1Informe de RendimentosInforme de Rendimentos

## Informe de Rendimentos

O Informe de Rendimentos (Comprovante de Rendimentos) é um relatório que contempla as mesmas informações prestadas na DIRF, acrescido de dados complementares quando aplicável.

Esse comprovante deve ser entregue ao funcionário ou prestador de serviço que tenha recebido pagamentos durante o ano-calendário. O documento é utilizado pela pessoa física para a elaboração da sua Declaração de Ajuste Anual do Imposto de Renda, no prazo estabelecido pela Receita Federal.

**Observação Importante**

Existem duas possibilidades para geração do Informe de Rendimentos:

1. 1. Pelo programa da DIRF (contemplado pelo RM Labore);
   2. Pelo próprio sistema **TOTVS Folha de Pagamento (RM Labore)**, que disponibiliza um leiaute similar ao programa da DIRF e plenamente aderente à legislação vigente.

Conforme a **Instrução Normativa RFB nº 1.215**, Art. 2º, § 3º, o modelo de leiaute do Informe de Rendimentos disponibilizado por sistema informatizado pode ser diferente do modelo estabelecido no § 1º, desde que contenha todas as informações nele previstas, ficando dispensada assinatura ou chancela mecânica.

### Opções para Emissão do Informe de Rendimentos

Para a emissão do relatório, estão disponíveis as seguintes opções:

**Lançar valores para o Gerador de Relatórios**

Permite que os dados sejam gravados na tabela PDIRF, para utilização no Gerador de Relatórios. Este parâmetro deve ser marcado caso deseje disponibilizar os dados do Informe de Rendimentos através do TOTVS Portal. Consulte o documento no TDN: [Disponibilizar Informe de Rendimento no RM PORTAL](https://tdn.totvs.com/display/public/LRM/FOP_0008_Informe+de+Rendimentos+-+Portal+e+Via+E-mail)[.](https://tdn.totvs.com/display/public/LRM/FOP_0008_Informe+de+Rendimentos+-+Portal+e+Via+E-mail)

**Deletar Ano de Referência**

Ao marcar este parâmetro, antes de gravar os dados na tabela PDIRF, o sistema irá excluir os registros já existentes referentes ao ano-base selecionado. Essa opção é recomendada quando for necessário regerar as informações, evitando duplicidades.

**Enviar por e-mail**

Permite o envio do Informe de Rendimentos diretamente para o e-mail do funcionário (desde que o endereço esteja corretamente informado em seu cadastro). O envio poderá ser realizado com o documento em anexo no formato PDF.

**Comprovante de Rendimentos**

Marque esta opção para que o comprovante seja enviado em formato PDF.

**E-mail do remetente**

Informe o endereço de e-mail do remetente que será utilizado no envio.

> ⚠️ Este campo é obrigatório e deve ser preenchido com um e-mail válido.

**Dica:** Para mais informações sobre o envio do informe por e-mail, consulte o roteiro: [Enviar Informe de Rendimentos Por E-mail](https://tdn.totvs.com/display/public/LRM/FOP_0008_Informe+de+Rendimentos+-+Portal+e+Via+E-mail), no qual são detalhados o processo e as parametrizações necessárias.

**Natureza do rendimento**

Informe o texto que será impresso nos relatórios de funcionários e autônomos, logo após o nome do beneficiário.

**Imprimir mensagens de fórmulas**

O sistema permite a impressão de mensagens oriundas de fórmulas no Campo 7 do Informe de Rendimentos. É possível utilizar até 5 fórmulas simultaneamente.

# Modelo de Informe de Rendimentos para conferência de valores

A seguir, apresentamos um modelo detalhado de **Informe de Rendimentos**, com orientações sobre a composição de cada campo do relatório, a fim de auxiliar na conferência dos valores gerados pelo sistema.

**Ano-calendário**

Será impresso o ano-calendário informado no menu de geração do relatório.

---

**1 – Fonte Pagadora**

Serão apresentadas as informações cadastradas na **coligada**.

---

**2 – Pessoa Física Beneficiária dos Rendimentos**

Será exibida a natureza conforme o tipo e a parametrização do funcionário. Mais informações:

## Campo 03 – Rendimentos Tributáveis

### 01 – Total dos Rendimentos (inclusive férias)

Considera todos os eventos com incidência de IRRF e que compõem o Informe de Rendimentos. São deduzidos os valores que estornam IRRF, **exceto**:

* Códigos de cálculo 13, 113, 57
* Eventos informados em campos específicos no menu de geração da DIRF

---

### 02 – Contribuição Previdenciária Oficial

Serão considerados os seguintes códigos de cálculo:

**Prioridade 1:**  
(89 + 90 + 137 + 132 + 85 + 179) – 92

**Na ausência destes:**  
(3 + 82 + 130 + 132 + 85) – 92

---

### 03 – Contribuição à Previdência Privada e ao FAPI

Serão considerados os eventos informados na pasta:  
**“Contribuição à Previdência Privada”** – Aba Campo 2 (RTFA – Rendimentos Tributáveis – Dedução FAPI).

---

### 04 – Pensão Alimentícia (beneficiário informado no campo 7)

Considera os códigos de cálculo:

(13 + 113 + 53 + 195 + 197 + 319 + 326 + 320 + 386) – (199 + 201 + 327)

---

### 05 – Imposto de Renda Retido

Considera os códigos de cálculo:

(4 + 84 + 61 + 30) – 122

## Campo 04 – Rendimentos Isentos e Não Tributáveis

### Linha 01 – Parcela Isenta dos Proventos de Aposentadoria, Reforma e Pensão (65 anos ou mais)

Será apresentado o total da parcela isenta recebida durante o ano pelos funcionários aposentados, somado aos eventos informados na pasta:

**“Prov. Aposentadoria/Reserva/Reforma/Pensão + 65 anos”**

O sistema valida:

* Código de receita 3533
* Indicativo de aposentadoria
* Parâmetro “Deduz IRRF > 65 anos”
* Idade do funcionário
* Valor fixo cadastrado para maiores de 65 anos

Verifique maiores detalhes em: [Código de Receita: 3533 (Proventos de Aposentadoria)](http://tdn.totvs.com/pages/viewpage.action?pageId=209453637)

---

### Linha 02 – Diárias e Ajuda de Custo

Eventos informados na pasta: **“Diárias / Ajuda de Custo”** – Aba Campo 4.

---

### Linha 03 – Pensão ou Aposentadoria por Moléstia Grave ou Acidente em Serviço

Eventos informados na pasta: **“Prov. Aposentadoria p/ Moléstia/Acidente em Serviço”** – Aba Campo 4. Veja maiores detalhes em: [Código de Receita: 3533 (Proventos de Aposentadoria)](https://tdn.totvs.com/veja maiores detalhes em: http:/tdn.totvs.com/pages/viewpage.action?pageId=209453637)

---

### Linha 04 – Lucros e Dividendos (a partir de 1996)

Eventos informados na pasta: **“Lucros / Dividendos pagos por PJ a partir de 1996”** – Aba Campo 4.

---

### Linha 05 – Valores pagos a Titular ou Sócio de ME/EPP

Eventos informados na pasta: **“Valores pagos ao Titular ou Sócio de Microempresa”** – Aba Campo 4.

---

### Linha 06 – Indenizações (Rescisão / PDV / Acidente de Trabalho)

Eventos informados na pasta: **“Indeniz. Rescisão Contrato Trabalho / PDV / Ac. Trab.”**

⚠️ Aviso prévio indenizado:

* + Sem incidência de IRRF → permanece nesta linha
  + Com incidência de IRRF → deve compor o campo 3 (Rendimentos Tributáveis)

---

### Linha 07 – Abono Pecuniário

Considera eventos com os seguintes códigos:

* [39 - Abono de Férias](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719764)
* [47 - Média de abono de férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452718717)
* [59 - Dif. Abono de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452718362)
* [311 - Abono de Férias em Dobro](https://tdn.totvs.com/pages/viewpage.action?pageId=452719762)
* [339 - Abono  Férias Transferida Para Outra Filial](https://tdn.totvs.com/pages/viewpage.action?pageId=452719760)

⚠️ Eventos com código de cálculo de **1/3 de abono pecuniário** não são considerados aqui, pois devem compor o campo **01 – Total dos Rendimentos**, para fins de incidência de IR. Veja mais detalhes em: [DIRF - 1/3 Abono Pecuniário - Incidência IR](https://tdn.totvs.com/pages/viewpage.action?pageId=663845768)

---

### Linha 08 – Bolsas de Estudo – Médico Residente

Eventos informados na pasta: **“Bolsas Estudo Médico-Residente”** – Aba Campo 4.

---

### Linha 09 – Outros (Especificar)

Reservado para eventos que não se enquadram nas linhas anteriores. Eventos informados na pasta: **“Outros (especificar) – Campo 5 / Linha 9”**

A descrição pode ser alterada na tabela dinâmica **INT41** (Menu Administração Pessoal | Cadastros Globais | Tabelas Dinâmicas).

A linha somente será exibida se houver eventos informados.

## Campo 05 – 13º Salário

### 01 – 13º Salário (Líquido)

Entende-se como líquido: Base IRRF 13º – INSS 13º– Previdência Privada – Pensão Alimentícia – Dedução por dependente

Cálculo (códigos): (48 + 71 + 97 + 102 + 66 + 52 + 139 + 180) – (11 + 103 + 49 + 85 + 108 – 120) – valor por dependente – eventos de previdência privada 13º

---

### 02 – IRRF sobre 13º

Neste campo será descriminado o valor do Imposto de renda que foi retido nos pagamentos do 13° Salário. Serão considerados os eventos de código de cálculo: 49 e 106.

---

### 03 – Outros (Linha 3 – Campo 5)

Neste campo será informado o valor líquido recebido de participação nos lucros (PLR) . Para o líquido da PLR o sistema executa seguinte cálculo: CC 126 – (CC 127 – CC 121 – CC 321)

## Rendimentos Recebidos Acumuladamente

(Art. 12-A da Lei nº 7.713)

### 1 – Número do Processo

Informação do campo “Nro Processo” (apenas para decisões judiciais).

### 2 – Quantidade de Meses

Valor do campo “Qtdade Meses” e/ou quantidade dos códigos: 216 + 217 + 218.

---

### Linha 01 – Total dos Rendimentos Tributáveis

Campo “Valor Total Rend. Tributáveis” e/ou códigos: 204 + 208 + 212.

---

### Linha 02 – Despesas com Ação Judicial

Campo “Valor despesas Ação Judicial”. Não possui código de cálculo específico.

---

### Linha 03 – Contribuição Previdenciária Oficial

Campo “Valor Contribuição Prev. Oficial” e/ou: 205 + 209 + 213.

---

### Linha 04 – Pensão Alimentícia

Campo “Valor da pensão alimentícia” e/ou: 206 + 210 + 214.

---

### Linha 05 – IRRF

Campo “Valor do IRRF” e/ou: 207 + 211 + 215.

---

## Informações Complementares

Serão discriminados na Linha 07 do campo 04 - Outros:

* Assistência médica (titular e dependentes), com nome e CNPJ da operadora
* Previdência privada (por operadora)
* Pensão alimentícia detalhada por dependente (Folha, Férias e 13º)

---

## Dependentes com Movimentação de Pensão

Serão demonstrados:

* Nome do dependente
* CPF
* Valores descontados de pensão

Para os campos “Folha” e “PLR”, o sistema utiliza as informações da tela **Movimentação da Pensão** (anexo do cadastro do dependente).

⚠️ Diferente da linha 04 do campo 3, que busca informações na ficha financeira.

No campo “Folha” serão somados:

* Pensão Férias
* Pensão Folha
* Retificação Folha

---

## Mensagens Complementares

Serão exibidas:

* Mensagens inseridas no menu de geração
* Mensagens padrão (quando houver PLR – CC 126)

Incluem:

* Rendimentos do trabalho assalariado (repete linha 01 do Campo 03)
* Participação nos Lucros ou Resultados (PLR – valor líquido)

---

## Despesas Médico-Odonto-Hospitalares

As informações são extraídas do cadastro no módulo **Relatório/DIRF – Aba Operadora de Assistência à Saúde**.

Serão exibidos:

* Nome da operadora
* CNPJ
* Valores detalhados por dependente

Mais detalhes acesse o documento: [Histórico de Assistencia a Saúde](https://tdn.totvs.com/pages/viewpage.action?pageId=210052115)

---

## Responsável pelas Informações

O campo **Data** considerará a data informada em: “Data de Entrega” - Aba central **DIRF em Arquivo** Parâmetros Específicos da Coligada

O campo somente será exibido quando a opção **DIRF em Arquivo** estiver selecionada.

Empresa e CNPJ seguirão as informações cadastradas na coligada.

2-2DIRF Para Conferencia:DIRF Para Conferencia:

## DIRF para Conferência

Este relatório é destinado à **conferência visual** dos dados que serão enviados para o programa da DIRF, quando a geração for realizada pela opção **“DIRF em Arquivo”**.

⚠️ Importante:  
O relatório gerado neste módulo, mesmo quando salvo em arquivo, **não pode ser importado no programa da DIRF**. Ele possui finalidade exclusivamente conferencial.

Após a exibição dos valores individuais de cada funcionário, o sistema apresentará os **Totais Gerais**, que correspondem às mesmas informações demonstradas individualmente, porém consolidadas com o somatório de todos os funcionários listados no relatório.

---

## Geração do Arquivo de Log da DIRF

Esta opção será exibida quando, na tela de seleção do tipo de arquivo a ser gerado, for escolhida uma das opções:

* **DIRF em Arquivo**
* **DIRF para Conferência**

### Regras importantes:

* Não é possível gerar o log para mais de um funcionário simultaneamente.
* É necessário:

  + Marcar a opção **“Gerar arquivo de Log da DIRF”**
  + Informar a **chapa** do funcionário para a geração

### Finalidade do Log

O relatório de log apresenta:

* Todas as informações consideradas na geração da DIRF
* Detalhamento das verbas processadas
* Valores de deduções
* Totais mensais apurados

Esse recurso é essencial para análises técnicas, validações e identificação de possíveis divergências antes da transmissão oficial.

2-3DIRF em arquivoDIRF em arquivo

## DIRF em Arquivo

Ao marcar a opção **“DIRF em Arquivo”**, o sistema gerará o arquivo que deverá ser importado no Programa Gerador da DIRF da Receita Federal.

Ao selecionar essa opção, na tela de **Parâmetros da Coligada**, será apresentada a aba **“DIRF em Arquivo”**, contendo os campos obrigatórios para a geração do arquivo.

---

## Data de Entrega

Informe a **Data de Entrega** da declaração.  
Essa informação será utilizada na composição do arquivo e também poderá ser apresentada no relatório do Informe de Rendimentos.

---

## Responsável

Preencha os dados do responsável pela entrega da declaração.

---

## Declarante

Informe os dados do declarante da DIRF.

A partir da DIRF 2008, tornou-se obrigatório informar se o declarante é **Sócio Ostensivo**.

Caso a declaração seja **retificadora**, é obrigatório informar o número do recibo da declaração anterior no campo: **“Nº Recibo da Última Declaração Entregue”**

---

## Indicador – Assistência à Saúde Coletivo Empresarial

Deve ser informado se a empresa possui **Plano de Saúde Coletivo Empresarial**, para que o sistema gere no arquivo da DIRF:

* Informações das operadoras cadastradas
* Valores de deduções de titulares
* Valores de deduções de dependentes (quando houver)

### Atenção

Se for selecionada a opção:

**“1 - Não existe pagamento de valor titular/dependente”**

O sistema **não enviará para o arquivo da DIRF**:

* Informações das prestadoras de saúde
* Valores de deduções de titulares e dependentes

---

## Indicador – Rendimentos Pagos a Residentes ou Domiciliados no Exterior

Deve ser informado se a empresa realizou pagamento de rendimentos a residentes ou domiciliados no exterior, para que sejam gerados no arquivo da DIRF:

* Os valores das verbas
* Seus respectivos códigos de receita

### Atenção – Pessoa Jurídica

A partir da versão 12.1.3, o campo passou a permitir a opção:

**“1 - Pagou Rendimentos a Residentes ou Domiciliados no Exterior”**

Em versões anteriores, essa opção permanecia fixa como:

**“0 - Não pagou”**

---

## Aba Pessoa Jurídica

Essa aba será apresentada quando, no campo **Tipo de Declarante**, for selecionado **Pessoa Jurídica**.

Nela deverão ser preenchidas as informações do responsável pela empresa.

⚠️ Atenção especial ao campo:

**“CPF do Responsável pelo CNPJ”**

Este campo é obrigatório e não pode permanecer em branco.

---

## Indicador de Fundação Pública de Direito Privado

Foi criado o campo: **“Indicador de Fundação pública de direito privado instituída pela União, Estados, Municípios ou Distrito Federal”**

Esse campo será habilitado somente quando o campo **“Natureza do Declarante”** estiver com uma das seguintes opções:

1 - Órgãos, autarquias e fundações da administração pública federal  
2 - Órgãos, autarquias e fundações da administração pública estadual, municipal ou do Distrito Federal  
8 - Entidade com alteração de natureza jurídica (uso restrito)

---

## Aba Pessoa Física

Quando o tipo de declarante for **Pessoa Física**, estarão disponíveis os seguintes campos no registro DECPF:

* Indicador de Declarante Falecido
* Data do Óbito
* Situação do Espólio
* CPF do Inventariante
* Nome do Inventariante

---

## Regras Importantes

### Evento/Situação Especial

O campo **“Evento/Situação Especial”** depende do campo **“Situação da Declaração”**.

A opção:

**“1 - Encerramento de Espólio”**

Somente será aceita quando a **Situação da Declaração** for:

**“2 - Declaração de extinção/espólio/saída definitiva do país”**

---

### Indicador de Declarante Falecido

* É obrigatório.
* Se preenchido com:  
  **“1 - Declarante Falecido”**  
  então o campo **“Data do Óbito”** torna-se obrigatório.

---

### Campos de Inventariante

Os campos:

* Nome do Inventariante
* CPF do Inventariante

Não são obrigatórios, mas devem ser preenchidos quando houver inventariante responsável pelo espólio.

---

## Campos Complementares

Nesta aba deve ser vinculado o **campo complementar do cadastro do funcionário**, do tipo **DATA**, que deverá conter a data do laudo médico, nos casos de funcionário com **Moléstia Grave**.

### Observação Importante

Quando o funcionário receber proventos relacionados à Moléstia Grave (Código de Receita 3533), é obrigatório que a **data do laudo médico** esteja devidamente informada em seu cadastro.

---

## Log de Erros e Avisos na Geração da DIRF em Arquivo

Durante a geração da DIRF em Arquivo, o sistema poderá apresentar:

* Mensagens de erro (impedem a geração)
* Mensagens de aviso (não impedem a geração, mas exigem conferência)

Ao final da execução, será gerado o arquivo da DIRF conforme layout vigente.
