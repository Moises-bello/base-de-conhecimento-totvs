---
content_hash: a12d98c5c3a20c9dfd9cd002a7bfee39b45ff2940c98f7f97fcd8238a22999b7
fetched_at: '2026-06-29T00:09:48.718593+00:00'
page_id: '435105222'
product: rm
source: tdn-rm
title: Minha Casa Minha Vida
type: documentation
url: https://tdn.totvs.com/display/LRM/Minha+Casa+Minha+Vida
version: 17
---

MCMVAtenção

**Valores de parcelas de  MCMV não são demonstrados no PDC, pois são valores pagos pela caixa.**

Parâmetros |

# Parâmetros e Cálculos

A funcionalidade Minha Casa Minha Vida foi desenvolvida no TOTVS Gestão Imobiliário a fim de facilitar o acompanhamento de uma obra, integrando-o ao TOTVS Obras e Projetos. Por ele é possível acompanhar o andamento do projeto, criação de contratos e gestão das baixas das parcelas, de acordo com os planos disponibilizados pela Caixa Econômica Federal.

**Procedimento para inserir o Cronograma no TOTVS Obras e Projetos**  
No TOTVS Obras e Projetos em Parâmetros do Projeto (F6) | Cronograma | Períodos é possível definir quantos períodos o cronograma será formado. Assim que definidos, os períodos do cronograma serão os mesmos tanto para a Planilha de Atividades quanto para a Planilha de Serviço.  
Depois de definir os períodos, é necessário informar o percentual previsto para cada um. Em Cadastros | Planilha | Atividades marque a obra e acesse o anexo Cronograma. Para cada período informe um percentual previsto, sendo que o total deve ser igual a 100%.

**Procedimentos no TOTVS Incorporação**  
Para o acompanhamento das medições da Obra, deverá ser realizado criado um Avanço de Obra, que se encontra em anexo ao Empreendimento. Através do Avanço da Obra, pode ser determinado qual o Tipo de Medição a ser utilizado, são eles:  
**Manual:** Nessa opção deverá ser inserido manualmente as datas e percentuais das medições.  
**TOTVS Obras e Projeto:** As medições serão buscadas do Cronograma do TOTVS Obras e Projetos informado no cadastro de Avanço de Obra.  
**Fórmula:** As medições serão inseridas conforme o resultado da execução da fórmula informada no cadastro de Avanço de Obra.  
Próximo passo antes de criarmos um Financiamento Minha Casa Minha Vida é cadastrar uma Modalidade de Venda com o modelo de Cálculo = Minha Casa Minha Vida. Temos que inserir nesta Modalidade os Componentes referentes a este processo. São eles:  
**Financiamento CEF** – Componente gerador de parcela. Este componente fica configurado o código de contrato do Cliente com a Caixa e o valor do financiamento.  
**Terreno CEF** – Receberá o valor do Terreno. Nem sempre deverá existir no plano, más quando existir, seu valor ficará todo na primeira parcela da serie de pagamento.  
**Subsídio CEF** – Nem sempre existirá no plano, só ocorre com o cliente consegue o subsídio do governo.  
**Recurso Mutuário CEF** – Ocorre quando o cliente utiliza recursos próprios para pagar parte da venda.  
**FGTS CEF** – Ocorre quando o Cliente possui FGTS e o utiliza para aquisição da casa própria.  
Após a realização da medição da Obra e do cadastrado da Modalidade de Venda, podemos criar os contratos de financiamentos Minha Casa Minha Vida. Devemos criar um novo contrato, utilizando o empreendimento com medições e Modalidade de Venda cadastrada. O sistema irá gerar o Plano de Financiamento de acordo com as medições da Obra, períodos e percentuais informados.  
Se houver alguma alteração no cronograma, por atraso ou antecipação, o mesmo deve ser atualizado assim como o Plano de Financiamento. Para isso devemos executar o processo "Atualização Plano de Financiamento", onde o sistema redistribuirá o valor do financiamento conforme as alterações realizadas no cronograma. Esta opção é realizada no processo "Atualização Plano de Financiamento" no menu Contratos.

Importante:

É possível incluir o componente **Financiamento CEF** com o valor R$ 0,00 para isso é necessário definir o **Efeito Contábil Financeiro** no **Tipo de Parcela** e nos parâmetros do Totvs Gestão financeira é preciso também **habilitar Permite Lançamentos Zerado**(Totvs Gestão Financeira>>Ambiente>>Parâmetros>>Totvs Gestão Financeira>>Contas a Receber>>Manutenção de Lançamentos>>Inclusão).

Para que esta combinação de parametrização seja efetiva os componentes **Recurso Mutuário CEF** ou **FGTS CEF** precisam possuir valor.

Medição Zerada

Somente na primeira Medição do Avanço de Obra é permitido medição com percentual zerado, caso deseje colocar outra medição zerada, então favor inserir a medição zerada na subunidade do contrato. Caso contrário dará erro na atualização do plano MCMV.

Web Service

Foi criado um novo parâmetro para permitir a alteração/inserção do componente 500. Para que o processo funcione é preciso habilitar o parâmetro '**Inserir o componente de terreno ao inserir o componente de financiamento MCVC quando o componente existir na modalidade e for via Web Service**'

**Parâmetros | Gestão de Imóveis | Contrato | Plano de Financiamento| MVC (Minha casa minha vida)**

**Contrato antes do Cronograma:**  
Se o contrato for criado antes de existir o cronograma de medição, será criada somente uma parcela com o valor total do financiamento e data de vencimento igual a data do componente. Após a criação do cronograma deste empreendimento, deve ser executado o processo "Atualizar Plano Financiamento" onde esta parcela será redistribuída conforme o cronograma inserido. Esta opção é realizada no processo "Atualizar Plano de Financiamento" no menu Contratos.  
Este processo pode ser executado de duas formas:  
1 - Quando o cliente consegue o Empréstimo de 100% do Financiamento. Neste caso, deve ser executado o processo de "Atualizar o Plano de Financiamento".  
2 - Quando o cliente NÃO consegue o Empréstimo de 100% do Financiamento. Neste caso, deve ser realizado um Aditivo de Renegociação do Contrato, adequando o plano de financiamento a condição que foi concedida.

**Observação:** Para realizar um **Aditivo de Renegociação** de modo a incluir uma nova regra Minha Casa Minha Vida em um contrato que já tenha uma regra destas, será necessário cancelar todas as parcelas relacionadas a esta regra existente, antes ou no mesmo aditivo que irá incluir as novas regras Minha Casa Minha Vida.

**Contrato no mesmo mês do Cronograma**  
Se o contrato for criado no mesmo mês do início do cronograma, será criado parcelas de acordo com a quantidade de períodos e percentuais de medições do cronograma.  
Exemplo: Se o cronograma tiver 5 períodos, o sistema criará 5 parcelas de acordo com os seus percentuais.

**Contrato após o Cronograma**  
Se o contrato for criado meses após o início do cronograma, será criado parcelas de acordo com a quantidade de períodos e percentuais de medições restantes do cronograma. A primeira parcela do financiamento terá o seu percentual acumulado em relação aos períodos anteriores a data do contrato.  
Exemplo: Se o cronograma tiver 5 períodos, iniciando em 01/2012 e efetuarmos um contrato em 03/2012 o sistema criará 3 parcelas de acordo com os seus percentuais, sendo que a primeira parcela terá o percentual acumulado do primeiro e segundo período.  
Após a Criação do contrato, medições da obra, podemos realizar o pagamento das parcelas do Plano de Financiamento. Esta etapa de baixa de parcelas será executado pelo processo "Baixas por Demonstrativo de Cronograma Desembolso", no menu Contratos. Neste processo iremos inserir o arquivo DCD - Demonstrativo de Cronograma Desembolso, que irá verificar em cada contrato as parcelas a serem baixadas pelo sistema, efetuando a baixa também no Financeiro. Este arquivo é gerado pela CEF.

**Observação:** O sistema irá impedir o usuário de criar mais de um grupo nas regras de financiamento do contrato com componentes MCMV, ainda que esteja efetuando um aditivo de renegociação cancelando todas as parcelas de um grupo e tentando gerar outro grupo. Pois no momento da atualização do plano de financiamento MCMV o sistema não tem como saber se um grupo está cancelado ou não. O sistema não cancela grupo e sim parcelas.

**Observação:** Para realizar um **Aditivo de Renegociação** de modo a incluir uma nova regra Minha Casa Minha Vida em um contrato que já tenha uma regra destas, será necessário cancelar todas as parcelas relacionadas a esta regra existente, antes ou no mesmo aditivo que irá incluir as novas regras Minha Casa Minha Vida

**Cálculo do Plano de Financiamento Minha Casa Minha Vida quando o Empreendimento está configurado para Deduzir FGTS com terreno permutado**

Uma vez que o sistema seja parametrizado para esta situação ele se comportará da seguinte forma ao gerar o Plano de Financiamento

* **Quando o valor do FGTS é maior ou igual ao valor do Terreno**

Para este caso a Caixa Econômica Federal deduz o valor do Terreno do valor do FGTS e realiza o repasse do saldo do valor do FGTS proporcional a cada medição, conforme exemplo abaixo:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **VR AP** | **170.000,00** | **VR MEDIÇÕES** | **152.884,62** |  | **30,61%** |
| Financiamento | 150.461,06 |  |  |  | 46.056,13 |
| Terreno | 17.115,38 |  |  |  | 17.115,38 |
| FGTS | 19.543,97 |  |  |  | 743,39 |
| Desconto | 5,03 |  |  |  | - 1,54 |
|  | **170.000,00** | 152.884,62 |  |  | **63.913,36** |

No exemplo acima, na primeira medição o sistema calcula o valor de FGTS para a parcela seguindo a fórmula:

FGTS Parcela = (Valor FGTS - Valor Terreno) \* Medição do Avanço de Obra

FGTS Parcela = (R$ 19.543,97 - R$ 17.115,38) \* 30,61%

**FGTS Parcela = R$ 743,39**

* **Quando o valor do FGTS é menor que o valor do Terreno**

Para este caso a Caixa Econômica Federal deduz o valor do FGTS e o saldo de Terreno é deduzido do valor do Financiamento para ser realizado cada medição como demonstrado abaixo:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **VR AP** | **170.000,00** | **VR MEDIÇÕES** | **152.884,62** |  | **30,61%** |
| Financiamento | 160.461,06 | 152.889,65 |  |  | 46.799,52 |
| Terreno | 17.115,38 | 7.571,41 |  |  | 17.115,38 |
| FGTS | 9.543,97 |  |  |  | - |
| Desconto | 5,03 |  |  |  | - 1,54 |
|  | **170.000,00** | 152.884,62 |  |  | **63.913,36** |

No exemplo acima, na primeira medição o sistema zera o valor de FGTS para a parcela e calcula o valor do Financiamento seguindo a fórmula:

Financiamento Parcela = (Valor Financiamento - (Valor Terreno - Valor FGTS)) \* Medição do Avanço de Obra

Financiamento Parcela = ((R$ 160.461,06 - (R$ 17.115,38- R$ 9.543,97)) \* 30,61%

**Financiamento Parcela = R$ 46.799,52**

**Cálculo do Plano de Financiamento Minha Casa Minha Vida quando o Empreendimento está configurado para Deduzir FGTS com terreno próprio**

Uma vez que o sistema seja parametrizado para esta situação ele se comportará da seguinte forma ao gerar o Plano de Financiamento

* **Quando o valor do FGTS é maior ou igual ao valor do Terreno**

O sistema irá utilizar a mesma forma de cálculo do exemplo anterior para terreno permutado:

FGTS Parcela = (Valor FGTS - Valor Terreno) \* Medição do Avanço de Obra

* **Quando o valor do FGTS é menor que o valor do Terreno**

Para este caso a Caixa Econômica Federal deduz o valor do FGTS e o saldo de Terreno não é deduzido do valor do Financiamento:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **VR AP** |  | **VR MEDIÇÕES** |  |  | **15%** |
| Financiamento | 70.000,00 | 78.000,00 |  |  | 11.700,00 |
| Terreno | 10.000,00 |  |  |  |  |
| FGTS | 8.000,00 |  |  |  | - |

No exemplo acima, na medição de 15% de avanço de obra, o sistema zera o valor de FGTS para a parcela e calcula o valor do Financiamento seguindo a fórmula:

Financiamento Parcela = (Valor Financiamento + Valor FGTS) \* Medição do Avanço de Obra

Financiamento Parcela = ((R$ 70.000,00 + R$ 8.000,00) \* 15%

**Financiamento Parcela = R$ 11.700,00**

**Entrando com contratos de Financiamento Minha Casa Minha Vida a partir do PVI incluindo Terreno**

Caso os contratos Minha Casa Minha Vida tenham valor de Terreno envolvido, há duas possibilidades de entrar com o valor do Terreno nas regras de financiamento. Para ambas é necessário que a Modalidade utilizada tenha em suas regras o componente de Terreno como percentual

**1 - Informando o valor do Terreno no PVI**

Esta situação implica na informação do valor de terreno na tela de proposta do PVI. Para que o valor informado para o Terreno se mantenha ao enviar o contrato para o RM, é necessário que o parâmetro "Calcular Valor do Terreno com Base no Valor do Terreno do Empreendimento" esteja desmarcado

**2 - Cálculo automático do valor do Terreno**

Esta situação depende da informação do campo Valor do Terreno no cadastro de Empreendimento, da informação da fração ideal no cadastro da sub-unidade e por fim, que o parâmetro "Calcular Valor do Terreno com Base no Valor do Terreno do Empreendimento" esteja marcado. Desta forma, ao enviar o contrato Minha Casa Minha Vida para o RM, o valor do Terreno será calculado multiplicando-se o valor do Terreno no Empreendimento pela fração ideal da sub-unidade

Processos:



* [Baixa por Demonstrativo Cronograma Desembolso](https://tdn.totvs.com/display/public/LRM/Baixa+por+Demonstrativo+Cronograma+Desembolso)

**Contratos de Venda** : Processo - Minha Casa Minha Vida

* **Atualizar Plano de Financiamento:**Esse processo permite atualizar o plano de financiamento de uma venda que possua componentes do Minha Casa Minha Vida, quando é realizado uma alteração no Avanço da Obra.
* **Atualizar Número do Contrato:**Esse processo permite atualizar o número de contrato de todas as vendas que possuam componente gerador Minha Casa Minha Vida.

Ao executar o processo é exibida uma tela com os seguintes campos:

* **Venda/Aluguel:** Exibe o numero da venda que possui componente gerador de parcela do Minha Casa Minha Vida;
* **Contrato CEF:** Esse campo permite editar o número do Contrato.
Exemplo MCMV

**Sobre o Minha Casa Minha Vida, cadastros principais.**

As parcelas são correpondes as mediçoes cadastradas no Avanço de Obra do Empreendimento do Minha Casa Minha Vida.

No Empreendimento é feito o cadastro do Avanço de Obra clicando em : Avanço de Obra (POC)

Neste exemplo, o Avanço de Obra em 4 Etapas.

* 1 Etapa : Novembro até Dezembro
* 2 Etapa : Janeiro até Fevereiro
* 3 Etapa : Fevereiro ate Março
* 4 Etapa : Março até Abril

Neste exemplo , a Construtora iria entregar o Empreendimento neste período acima.

* Todas as vendas que forem deste empreendimento irão assumir as parcelas do Plano MCMV cadastradas no avanço de obra.

Exemplo : Como iniciou em Novembro as parcelas , um contrato feito no Mês de Novembro, irá assumir 4 Parcelas.

Agora, se um contrato for feito no Mês de Fevereiro , o contrato irá assuimr apenas 2 Parcelas.

Primeira Parcela somando todas Porcentagens das 3 primeiras até Fevereiro e a parcela de Março , ainda continuando com sua Porcentagem.

Geraria uma Parcela com 80% e a outra com 20%.

Depois da entrega é gerada uma parcela única para recebar o valor da Caixa.

**Usuario vai fazendo baixa da parcelas com tempo, pode ser baixa DCD - arquivo que a Caixa envia ou Manual.**

Na tela de Contrato de Venda em Processos | Minha Casa Minha vida tem essas 2 opçoes:

Atualizar o Plano e Atualizar número do Contrato

* Atualizar Plano de Financiamento

Depois que é feito o Plano teve alguma alteração , inclusão de uma parcela nova , alteração de Porcentagem , neste processo é feito esse tipo de alteração.

* Atualizar Número do Contrato : Atualizar numero do contrato se a venda estiver efetivada , o numero é atualizado no componente dentro do contrato , esse número é enviado pela CAIXA no arquivo .. esse número é do contrato da CAIXA , não do Contrato do TCGI.

Para localizar as parcelas para efetuar a baixa do Arquivo é justamente por este Número de Contrato enviado pela CAIXA.

Sobre os Parâmetros do MCMV

### **Parâmetro: Limite de diferença importação DCD / MCMV (R$)**

**Localização:**  
Módulo: Construção e Gestão de Imóveis  
Menu: Parâmetros do Sistema → Aba *Minha Casa Minha Vida*

---

### **Descrição Geral**

Este parâmetro define o **limite de tolerância em valor (R$)** para diferenças entre o **valor da parcela contratual** e o **valor efetivamente baixado/importado** no processo de integração com o programa **Minha Casa Minha Vida (MCMV)**, durante a **importação do DCD (Demonstrativo de Crédito e Débito)**.

Seu objetivo é permitir **ajustes automáticos de pequenas diferenças** entre valores de parcelas e baixas, evitando a necessidade de tratamento manual no TOTVS Gestão Financeira, desde que as diferenças estejam **dentro do limite estabelecido**.

---

### **Funcionamento**

1. **Quando informado um valor-limite (ex: 5,00 R$):**  
   O sistema compara o **valor da parcela prevista** com o **valor baixado/importado**.

   * Se a diferença entre eles **estiver dentro do limite informado**, o sistema tratará automaticamente a diferença conforme a **parametrização de destino** definida pelo usuário (ver abaixo).
   * Se a diferença **exceder o limite definido**, o lançamento **será encaminhado ao TOTVS Gestão Financeira** para tratamento manual.

---

### **Tratamentos Possíveis Dentro do Limite**

#### ➤ **Caso 1: Valor da Parcela < Valor Baixado**

Se o valor baixado for **maior** que o valor da parcela, mas **dentro do limite**, o sistema lançará o excedente em uma das opções configuradas:

* **Baixar com diferença - Juros de Atraso**
* **Baixar com diferença - Multa**

A opção utilizada dependerá da parametrização escolhida pelo cliente.

**Exemplo:**  
Parcela: R$ 1.000,00  
Valor baixado: R$ 1.004,50  
Diferença: R$ 4,50 → Dentro do limite de R$ 5,00  
Resultado: Parcela baixada e diferença registrada como *Juros de Atraso* (ou *Multa*, conforme configuração).

---

#### ➤ **Caso 2: Valor da Parcela > Valor Baixado**

Se o valor baixado for **menor** que o valor da parcela, mas **dentro do limite**, o sistema lançará a diferença em:

* **Baixar com diferença**, ou
* **Desconto**,

conforme definido na parametrização do cliente.

**Exemplo:**  
Parcela: R$ 1.000,00  
Valor baixado: R$ 996,00  
Diferença: R$ 4,00 → Dentro do limite de R$ 5,00  
Resultado: Parcela baixada e diferença registrada como *Desconto* (ou *Baixar com diferença*).

---

### **Tratamento Fora do Limite**

Se a diferença entre o valor da parcela e o valor baixado **ultrapassar o valor do limite configurado**, a baixa **não será tratada automaticamente**.  
Neste caso, o sistema encaminhará a diferença para o **TOTVS Gestão Financeira**, onde o usuário deverá realizar o ajuste manual.

**Exemplo:**  
Parcela: R$ 1.000,00  
Valor baixado: R$ 1.007,50  
Diferença: R$ 7,50 → Fora do limite de R$ 5,00  
Resultado: Registro enviado ao Gestão Financeira para análise manual.

---

### **Boas Práticas e Recomendações**

* Recomenda-se utilizar **valores de limite baixos** (ex: até R$ 5,00) para evitar ajustes indevidos.
* Este parâmetro é especialmente útil para **tratamento de arredondamentos bancários ou pequenos desvios** em integrações do programa MCMV.
* A configuração do **destino da diferença (juros, multa ou desconto)** deve estar coerente com as **regras contábeis e fiscais da empresa**.

---

### **Resumo do Comportamento**

| Cenário | Diferença dentro do limite | Tratamento automático | Diferença acima do limite |
| --- | --- | --- | --- |
| Parcela < Valor Baixado | Sim | Juros ou Multa | Encaminha ao Gestão Financeira |
| Parcela > Valor Baixado | Sim | Desconto ou Baixar com diferença | Encaminha ao Gestão Financeira |

Aquivo DCD.

Se tiver uma uma diferença no Arquivo dentro do valor informado nos parâmetros , é feita a baixa normalmente.

Incluir automaticamente diferença de avanço 100% em avanço de obra do MCMV

Ao marcar esse parâmetro , incluindo uma única etapa por exemplo de 30% , o sistema inclui uma automaticamente de 70% para fechar os 100%.

Esse é um Acordo e calculo de terreno quando é integrado com Web Service.

Sem Avanço de ObraCaso cliente **não utilize Avanço de Obra** no Empreendimento, MCMV sem avanço, o Plano gera apenas uma parcela do Valor total financiado , com o usuário podendo fazer baixar parciais desta parcela.Avanço de medição com valor percentual zero

No programa MCMV, o primeiro avanço de medição pode ser registrada como zero por cento. Essa condição está vinculada ao pagamento inicial para o terreno, esse procedimento é adotado porque o valor do terreno já constitui um ativo tangível e uma parte integral do custo total do projeto imobiliário. Portanto, mesmo que a medição física de progresso da obra seja zero no início, financeiramente, a parcela não está zerada, pois incorpora o valor do terreno.  
Após o primeiro avanço, todas as medições subsequentes devem refletir progresso físico real e, consequentemente, um avanço percentual maior que zero. Isso garante que os lançamentos financeiros sejam significativos e sem valor zero.

Quando ocorre um evento que impede o avanço da obra em um determinado período, a prática recomendada é não registrar esse intervalo como um avanço de medição com valor percentual zero. Ao invés disso, o correto é ajustar o período de medição para refletir o próximo avanço efetivo. Isto significa que se, por algum motivo, não houve progresso na construção dentro desse intervalo, o período de medição deveria ser estendido até a data em que o avanço real ocorreu. Por exemplo, se não houve progresso entre 01/01/2024 e 15/01/2024, mas houve progresso a partir de 16/01/2024, o período de medição deve começar em 01/01/2024 e se estender até a próxima data em que houve avanço, digamos 01/02/2024. A porcentagem de avanço registrada deve refletir o progresso real ocorrido nesse período estendido, garantindo que seja maior que zero.
