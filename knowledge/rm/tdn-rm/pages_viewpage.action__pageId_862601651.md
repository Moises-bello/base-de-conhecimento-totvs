---
content_hash: f9356eb11a75112478e601b06142aceecd7420d8a4da5b5e4f5c4847dda541ea
fetched_at: '2026-06-29T00:11:55.621177+00:00'
page_id: '862601651'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Cálculos - Cálculo de Subsídio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862601651
version: 17
---

### Introdução

---

O cálculo do subsídio é um processo que é realizado durante o fechamento de um condomínio e consiste no repasse aos sócios do empreendimento do valor da diferença entre o CTO mínimo do contrato e o valor total do condomínio. Para que esse repasse ocorra são necessárias algumas parametrizações e veremos abaixo como gerar o subsídio no fechamento individual.

### Procedimentos para utilização

---

Para utilização do subsídio na apuração individual do condomínio, devemos [parametrizar a utilização do mesmo;](https://tdn.totvs.com/pages/viewpage.action?pageId=856434519)

Além deste parâmetro, [os itens de cobrança que serão participantes do cálculo do subsídio devem ser marcados como "Utiliza subsídio"](https://tdn.totvs.com/pages/viewpage.action?pageId=435105029);

O Empreendimento deve ter sua [gestão condominial integrada com o aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105264);

E os contratos de locação devem possuir [CTO mínimo em suas faixas de faturamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105013), além de estarem marcados com o campo "Considera Condomínio" 

Estando os pré-requisitos acima satisfeitos, podemos realizar o cálculo de subsídio como veremos abaixo.

Lembrando que, o subsidio somente é cobrado no fechamento individual, sendo sempre **desconsiderado** quando o fechamento é integral.

### **Calculando o subsídio**

---

O cálculo do subsídio ocorre quando, em determinada competência, temos um valor do CTO de determinado contrato inferior ao total do meu condomínio. Toda essa diferença de valores será gerada através do subsídio e repassado integralmente aos sócios do empreendimento.

Para entender como cadastrar faixas com CTO mensal, [veja a documentação aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105013)

Para entender como cadastrar um sócio ao empreendimento, [verifique a documentação aqui.](https://tdn.totvs.com/display/LRM/Empreendimento+-+Anexo+-+Dados+de+Repasse+Empreendimento)

#### Exemplo de incidência de subsidio:

Aluguel

* Contrato de Locação 01: CTO Mensal R$ 5000,00
* Contrato de Locação 02: CTO Mensal R$ 8000,00

Condomínio

Contrato de Locação 01:

* Orçamento: R$ 1200,00
* Cobranças diretas: R$ 4890,00
* Medição (Energia, Luz, Etc): R$ 800,00
* Total das cobranças: **R$ 6890,00**

Contrato de Locação 02:

* Orçamento: R$ 500,00
* Cobranças diretas: R$ 2200,00
* Medição: (Energia, Luz, Etc.): R$ 1800,00
* Total das cobranças: **R$ 4500,00**

Subsídio Contrato de Locação 01: Com subsídio de R$ 1890,00 Valor Condomínio - CTO Mensal (6890,00 - 5000,00 - 1890,00)

Subsídio Contrato de Locação 02: Sem subsidio, valor do condomínio total é inferior ao CTO mensal.

Este cálculo então, será gerado sempre no processo de [Apurar Condomínio](https://tdn.totvs.com/pages/viewpage.action?pageId=852299397) (Consulte a documentação clicando no link ao lado)

É importante notar que o subsídio sempre será calculado junto aos processos do fechamento, não sendo um cálculo exclusivo no sistema. Visto que o mesmo depende sempre dos valores calculados dos processos na competência em questão. Não há como calcular um subsídio sem que um processo (Cobrança direta, orçamento, medições, etc) tenha sido apurado. Entretanto é possível realizar os cálculos dos processos de forma assíncrona. E na medida que os processos forem compondo a apuração, os valores de subsídio serão sempre atualizados, caso existam.

#### Exemplo de cobrança assíncrona:

Aluguel

* Contrato de Locação 01: CTO Mensal R$ 5000,00

Condomínio

Contrato de Locação 01:

* Orçamento: R$ 1200,00
* Cobranças diretas: R$ 4890,00
* Medição (Energia, Luz, Etc.): R$ 800,00
* Total das cobranças: **R$ 6890,00**

Se realizo o processo de apurar o meu orçamento na competência, para essa subunidade terei apenas um valor de condomínio de R$ 1200,00, **inferior ao valor do CTO.** Dessa forma, ainda não foi gerado o cálculo de subsídio no sistema.

Se após isso, realizo a apuração da cobrança direta (R$ 4890,00) o sistema irá gerar o valor do subsídio após a conclusão deste cálculo, visto que a cobrança total, agora é **maior que o meu CTO** (4890+1200 = 6090)

Neste caso, posso gerar o lançamento financeiro do subsídio (Como demonstrado abaixo) entretanto, após essa geração, nenhuma outra apuração poderá ser feita, visto que o subsídio nesta competência já foi gerado. Para apurar os cálculos restantes, deve ser cancelado o lançamento financeiro do subsídio, através do processo de Cancelar Lançamentos Financeiros.

#### Visualizando o subsidio calculado

Para visualizar o subsídio basta clicar na linha do processo definido como subsídio. Caso o mesmo esteja calculado e com registros, basta dar dois cliques em sua linha para exibir todo o valor subsidiado.

Os valores subsidiados são abatidos das cobranças comuns e depois das específicas, na ordem abaixo:

* Orçamento
* Cobrança Direta
* Despesa Financeira
* Reserva
* Consumo

**Exemplo de incidência de subsidio (utilizando o Parâmetro de priorização da cobrança no cálculo do subsídio)**

Veja este exemplo na prática:  
Um condomínio possui contratos com os seguintes dados:

Contrato de locação :

1. * CTO Fixo: R$ 4.000,00
   * Descontos no CTO: R$ 700,00
   * Fundo Promocional na Competência: R$ 300,00
   * Locação na Competência: R$ 0,00
   * Valor Total de Cobrança do Condomínio: **R$ 5.000,00**  
     O parâmetro **"Priorização da Cobrança no Cálculo do Subsídio"**: Está marcado.
2. #### O sistema realizará o seguinte cálculo:

   1. **Serão utilizados os valores:**

      * CTO Inicial: R$ 4.000,00
      * Descontos Aplicados:
        + Fundo Promocional: - R$ 300,00
        + Locação: - R$ 0,00
      * **CTO Final (após priorizações será calculado assim)**:  
        R$ 4.000,00 - R$ 700,00 (desconto inicial) - R$ 300,00 (fundo) - R$ 0,00 (locação) = **R$ 3.0****00,00**.
   2. **A diferença Entre a Cobrança do Condomínio e o CTO Ajustado:**

      * Valor do Condomínio: R$ 5.000,00
      * CTO Ajustado: R$ 3.000,00
      * **Diferença (subsídio)**:  
        R$ 5.000,00 - R$ 3.000,00 = **R$ 2.000,00**.
   3. **Resultado Final:**

      * O valor de **R$ 2.000,00** será subsidiado diretamente ao sócio.

Com o parâmetro **"priorização da cobrança no cálculo do subsídio"** ativado, os valores de **fundo promocional** e **locação** foram incluídos no cálculo do desconto do CTO. Isso resultou em uma redução maior no CTO final (de R$ 4.000,00 para R$ 3.000,00), aumentando o subsídio que será imputado ao sócio.

### Subsídio para Contratos de Locação com múltiplos imóveis

---

Quando o valor do CTO de um contrato é inferior a minha cobrança de condomínio em determinada competência e ocorrer o subsídio, o sistema irá realizar o cálculo de forma automática para todas as subunidades / imóveis que fazem parte deste contrato, independente do momento em que são apuradas. Isto quer dizer que o cálculo do subsídio irá respeitar sempre o valor apurado no tempo.

Quando um contrato possui vários imóveis, o valor do CTO continua sendo único por contrato. Entretanto, o sistema no momento da apuração, irá identificar essas subunidades que fazem parte de um mesmo contrato e irá atualizar o valor de subsídio de acordo com as apurações realizadas. Isto quer dizer que o cálculo do subsídio irá sempre acompanhar a apuração de uma determinada subunidade e **será sempre atualizado** quando as apurações para as subunidades que fazem parte de um mesmo contrato acontecerem. Veja o exemplo abaixo:

Contrato A - CTO 2.000.

* Subunidade 00001
* Subunidade 00002
* Subunidade 00003

Apuração na competência 03/04 Totaliza **R$ 5000**. Logo, 5000 - 2000, teremos um valor de **R$ 3000,00** para ser subsidiado e distribuído entre as três subunidades.

Entretanto, foi apurado num momento apenas a subunidade 00001, cujo total de cobranças equivale a R$ 2200.

* Neste caso, temos um subsídio de **R$ 200** (2200 - 2000)

Após isso, faço a apuração da subunidade 00002, onde o total das minhas cobranças é de R$ 500.

* Agora, eu tenho um subsidio de (2200 + 500 - 2000) = **R$ 700**

Finalizando, faço a apuração da subunidade 00003, onde o total das minhas cobranças agora é de R$ 2300.

* O subsídio total para esse contrato irá ser: subsidio de (2200 + 500 + 2300 - 2000) = **R$ 3000,00**

É importante frisar que, nestes três momentos distintos onde realizamos a apuração do condomínio o sistema irá atualizar o valor subsidiado, bem como o valor descontado resultante do cálculo do subsídio nas devidas cobranças apuradas.

A partir da versão 12.1.2410, o valor subsidiado será abatido já no momento do cálculo e exibido diretamente na tela de apuração, permitindo ao usuário visualizar o subsídio antes de gerar o lançamento financeiro.  
**Comportamento antes da atualização:**  
O sistema realizava o abatimento do valor subsidiado apenas no momento da geração do lançamento financeiro, o que dificultava a visualização antecipada do valor exato do subsídio.

É importante ressaltar que, quando contratos de locação possuírem mais de um imóvel associado, o cálculo de subsídio continua sendo calculado através da diferença do CTO na competência.  
O valor do subsídio calculado então será sempre o mesmo para as subunidades deste contrato.

Neste cenário, mesmo que apenas uma subunidade seja selecionada para a apuração, caso ela esteja vinculada a um contrato que envolva múltiplas subunidades, todas essas subunidades serão incluídas no processo de apuração.

### Geração de lançamentos financeiros

---

O processo de Geração de lançamentos financeiros de subsídio consiste em gerar para os sócios do empreendimento os valores subsidiados durante a apuração dos cálculos.

Para executar o processo, basta Ir em *Processos / Gerar Lançamento Financeiro de Subsídio*

Ao executar o processo, serão exibidos os cálculos de subsídio de todas as unidades, caso existam. Estes lançamentos que serão gerados por este processo não possuem agrupamento, sendo sempre gerados de forma única para o sócio do empreendimento, para cada subunidade cujo cálculo resultou em subsídio.

Há a possibilidade de definir uma data de vencimento para estes lançamentos durante a execução do processo.

#### Cancelar lançamentos de subsídio

O processo de cancelamento utiliza o mesmo menu existente de cancelamento de lançamentos financeiros, bastando selecionar na visão os lançamentos de subsidio gerados para cancelamento.

### Restrições para Exclusão de Cálculos com Subsídio Integrado

---

Caso o lançamento de subsídio já esteja integrado ao sistema, **não será possível excluir os cálculos que fizeram parte desse subsídio**.  
Somente será permitida a exclusão de cálculos cujos itens de cobrança **não consideram subsídio** nesse cenário.

#### Resumo das Regras

* **Cálculos vinculados a subsídio integrado:**  
  Não podem ser excluídos.
* **Cálculos com itens de cobrança que não consideram subsídio:**  
  Podem ser cancelados normalmente, mesmo após a integração de subsídio.

### Veja mais

---
