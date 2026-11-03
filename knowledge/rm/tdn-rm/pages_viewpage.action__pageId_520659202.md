---
content_hash: d6ab88d737769610e18b5f7abac95b2c88b3c7fd25ac3ad2f6cb9d741279ae22
fetched_at: '2026-06-29T00:10:30.992051+00:00'
page_id: '520659202'
product: rm
source: tdn-rm
title: Contrato de Locação - Gestão - Escalonamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520659202
version: 15
---

Para acessar a funcionalidade seguir o seguinte menu: Aluguel > Contratos de Locação > Contrato de Locação > Anexos > Escalonamento.

Inicialmente, para que um Escalonamento seja cadastrado corretamente no sistema, devemos cadastrar primeiro um tipo de escalonamento e então, associá-lo ao registro.  
Este cadastro está disponível no próprio formulário de Escalonamento e irá definir se o mesmo será do tipo "Desconto" ou "Acréscimo". O campo tipo de escalonamento não é obrigatório, e ao cadastrar um escalonamento sem o tipo definido, teremos o comportamento antigo do sistema, cujo valor de integração para desconto será considerado dos parâmetros do TIN.

Os campos do cadastro de tipo de escalonamento são:

* **Desconto ou acréscimo**: Define se o escalonamento possuirá um desconto ou acréscimo que irá compor o lançamento escalonado através de um valor de integração;

Importante: 

Quando a opção for "Desconto" ou "Acréscimo", apenas valores de integração com a ação "Nada" poderão ser utilizados no tipo de escalonamento. A opção "Nada" preserva o valor original do contrato, mesmo que um desconto seja aplicado.

Sobre o Parâmetro: Gestão de Imóveis > Aluguel > Contrato de locação:**Valor de integração para descontos**Ele possui duas opções principais que definem como o desconto impacta o valor final do contrato:

1. **Ação "Desconto"**: O valor do desconto é **subtraído** diretamente do valor total do contrato. Isso reduz o valor final do contrato, refletindo o desconto aplicado.
2. **Ação "Nada"**: O valor do desconto **não é subtraído** do contrato, ou seja, o valor original do contrato é **preservado**. Esse comportamento é útil em cenários de escalonamento de desconto, onde se deseja aplicar um desconto sem alterar o valor final do contrato.

* **Descrição**: Descrição do tipo de escalonamento;
* **Valor de integração**: Valor de integração que será utilizado para compor o lançamento escalonado, caso possua um desconto, acréscimo.

*Cadastrando um tipo de escalonamento*

Após a criação de um tipo de escalonamento, podemos prosseguir com a criação de um escalonamento. Os campos disponíveis são:

* **Situação**: Campo de controle interno e não editável pelo usuário. As situações disponíveis são:
  + **Em Preparação**: Esta situação será aplicado ao incluir um novo escalonamento;
  + **Efetivado**: Esta situação será aplicado após a execução do processo "Efetivar Escalonamento";
  + **Cancelado**: Esta situação será aplicado após a execução do processo "Cancelar Escalonamento".
  + **Em Aprovação:** Esta situação será utilizada em Workflows do Fluig (A partir da versão 12.1.27). Não serão permitidas edições, bem como execuções de processos no escalonamento que se encontra "Em Aprovação".
* **Data Inicial**, **Data Final** e **Valor** são de preenchimento obrigatório;
* **Data Inicial** deve ser sempre maior ou igual à data de Início da vigência do Contrato de Locação;
* **Data Final**, não pode ser maior que a data de prorrogação da vigência;
* **Prioridade** deve ser utilizado pelo usuário para informar a prioridade de um determinado escalonamento quando ocorre conflito de períodos entre escalonamentos. Este campo é numérico e o maior valor tem a maior prioridade. Quando não estiver definida a prioridade, ou seja, quando existirem escalonamentos num mesmo período com um mesmo valor para esse campo, o sistema irá sempre usar o primeiro escalonamento cadastrado para realizar os cálculos.
  + **Exemplo 1 de Prioridade (Escalonamento pro rata dia):**

Escalonamento 1: (01/03/2018 a 25/03/2018) - Prioridade 0;  
Escalonamento 2: (20/03/2018 a 31/03/2018) - Prioridade 1;  
Conflito entre as datas 20/03 a 25/03;  
Neste exemplo, para calcular o valor da parcela utilizando pro rata dia no escalonamento, o sistema irá utilizar o escalonamento 1 para o período 01/03 a 19/03 e o escalonamento 2 para o período 20/03 a 31/03. Nos dias em que houve conflito de datas entre os escalonamentos, o sistema utilizou o escalonamento de maior prioridade.

* + **Exemplo 2 de Prioridade:**

Escalonamento 1: (01/03/2018 a 31/03/2018) - Prioridade 0;  
Escalonamento 2: (01/03/2018 a 31/05/2018) - Prioridade 1;  
Neste exemplo, para calcular o valor da parcela, o sistema irá utilizar o escalonamento 2 para o mês 03 porque este escalonamento tem a maior prioridade.

* **Escalonamento por m²** define se o escalonamento será por m². Quando marcado, o valor do Escalonamento será em relação ao m², não mais pelo valor total. Dessa forma a aplicação do Escalonamento será de acordo com o cálculo do Valor Final m² (informado no escalonamento) \* Área locada do contrato em cada período.

Só poderá ser aplicado Escalonamento por m² em Contrato de Locação que possua Imóvel do tipo Áreas Fracionadas ou Unificadas;  
O aditivo de Alteração dos Imóveis do Contrato não poderá incluir Imóveis do Tipo "Imóvel" no Contrato de Locação com data do aditivo anterior a data final de Escalonamento por M² nas situações "Em preparação" ou "Efetivado".

* **Valor** aceitará qualquer valor positivo, com até duas casas decimais, não validando se é maior ou menor que o valor do contrato de aluguel. Valores iguais ou menores que 0 (zero) não serão aceitos;
* **Tipo** definirá se o desconto / acréscimo será por "percentual" ou por "valor fixo". 
  + **Percentual**: O campo de Valor poderá receber um valor decimal igual ou maior que 0 (zero) ou igual ou menor que 100. O Valor padrão será 0. Se o campo "Valor Escalonado" for alterado manualmente o campo de Valor deverá ser atualizado novamente com a reaplicação do percentual sobre o novo "Valor Escalonado". Caso o tipo de desconto / acréscimo seja por "valor fixo", o campo Valor irá conter o "valor fixo de desconto / acréscimo" a ser considerado para o escalonamento;
  + **Valor Fixo** Se o campo "Valor Escalonado" for alterado manualmente o campo de Percentual deverá ser atualizado proporcionalizando o percentual com o novo valor escalonado. E o cálculo do valor final será feito da seguinte forma: Valor Final = Valor Corrigido – ValorDesconto. ou Valor Final = Valor Corrigido + ValorAcrescimo.
* **Aplicar Reajuste:** é obrigatório e deverá ser marcado para os casos em que o valor do escalonamento precise ser reajustado juntamente com o contrato de locação. Por padrão, o escalonamento nascerá com a opção "Sem Reajuste" marcada. As opções de reajuste são:
  + **Sem reajuste**: Define que o escalonamento não será impactado pelo processo de reajuste;
  + **Reajusta valor principal**: Define que os reajustes serão aplicados apenas no valor principal, ou seja somente no valor do escalonamento. Exemplo: Um escalonamento de R$ 1000,00 com um acréscimo de R$100. Após o processo de reajuste, na opção "Reajusta valor principal" somente o valor de escalonamento será alterado pelo reajuste.
  + **Reajusta valor principal e a diferença**: Define que tanto o valor principal e a diferença (Desconto / Acréscimo) serão reajustados. Exemplo: Um escalonamento de R$ 1000,00 com um desconto de R$100. Após o processo de reajuste, na opção "Reajusta valor principal e a diferença:" tanto o valor definido para desconto quanto o valor de escalonamento serão alterados pelo reajuste.

Importante!

* As opções de reajuste "Valor principal e a diferença" somente poderão ser aplicadas caso a opção de tipo de escalonamento esteja definida para "Valor".
* O processo de reajuste não realiza o cálculo pró-rata quando um período escalonado se estende até a data do reajuste, uma vez que o escalonamento possui prioridade sobre o reajuste.

* **Observação:** tem como objetivo inserir detalhes e observações sobre o escalonamento que está sendo cadastrado.

*Tela do escalonamento com os campos preenchidos*

**Rateio (Pró Rata Dia) do Escalonamento**

Para utilizar o Rateio (Pro Rata Dia) no Escalonamento acesse o contrato de locação e no campo **Modelo de Cálculo** marque a opção **Utiliza Cálculo Pro Rata.**  
Para os períodos de parcelas **Inicial** e **Final** o sistema utilizará **Mês Civil** e para os períodos das outras parcelas será usado o **Mês Comercial**.

**Qual a diferença entre Mês Civil e Mês Comercial?**

* **Mês Civil:** Expressão existente no mercado financeiro e administrativo que considera todos os dias do mês, da forma real mesmo. Por exemplo, em fevereiro teremos 28 ou 29 dias. Sendo assim, o **Ano Civil** é considerado com 365 dias.
* **Mês Comercial:** Considera que todos os meses tenham 30 dias, com isso, o **Ano Comercial** é considerado com 360 dias.

**Exemplo de Escalonamento:**

Pra facilitar a conta vamos considerar um aluguel de R$30.000,00 ( do dia 1 a 31) (30.000,00/30 = 1.000,00 por dia);

Se tiver um escalonamento do dia 16 a 31/12 no valor de 35.000,00 (35.000,00/30 = 1.166,66 por dia);

De 01 a 15/12 (sem escalonamento) = 15.000,00 De 16 a 31/12 (com escalonamento) = (15 \* 1.166,66) = R$17.499,90;

Aluguel total no período de 01 a 31/12/2017 = R$15.000,00 + R$17.499,90 = R$ 32.499,90.

* Quando o valor cobrado no mês é dividido por 30 dias significa que está sendo considerado Mês Comercial ("Chama-se ano comercial o período de tempo em que se considera que o ano tem 360 dias e cada um dos meses 30 dias, indistintamente. É utilizado na contabilidade e também na matemática financeira com o objetivo de simplificar os cálculos com datas.");
* Quando o cálculo é feito usando exatamente a quantidade de dias do mês chamado Mês Civil ("Mês civil é uma expressão usada no mercado financeiro e administrativo. Considera todos os dias existentes no mês em questão (por exemplo: se estamos em fevereiro, teremos 28 ou 29 dias, etc.).

Para ver o log do escalonamento realizado, basta acessar o **Contrato de Locação / Parcelas do Contrato de Locação** e abrir a parcela com um clique duplo. Na Memória de cálculo serão mostrados todos os detalhes do cálculo realizado.

**Impactos do Aluguel Complementar no Escalonamento**

No Contrato de Locação, caso exista algum Faturamento (Aluguel Complementar) e no mesmo período exista algum Escalonamento em Preparação, ao efetivar este Escalonamento, o sistema deve então regerar o aluguel complementar com base nesse novo valor de Escalonamento.

**Para entender melhor, veja o exemplo abaixo:**

Contrato 001 (01/2018 a 12/2018) – Valor de locação: 1000,00;

Escalonamento Valor: 1500, 00 03/2018 a 06/2018 Em Preparação;

Aluguel Complementar 10% do faturamento para a competência 05/2018 Valor do faturamento: 20.000,00 Valor do aluguel complementar = 1000,00   (0,1 \* 20.000 = 2000,00 | 2000,00 – 1000,00 = 1000,00);

Neste caso, ao efetivar o escalonamento, para que o valor de aluguel complementar não fique desatualizado, o aluguel complementar será excluído e gerado novamente, ficando da seguinte forma:

Valor do aluguel complementar = 500,00   (0,1 \* 20.000 = 2000,00 | 2000,00 – 1500,00 = 500,00).

Ao recalcular, se o valor do escalonamento for maior que o valor do percentual de faturamento, pode não ser gerado aluguel complementar.

Informações Complementares

---

 

Recursos Adicionais

---
