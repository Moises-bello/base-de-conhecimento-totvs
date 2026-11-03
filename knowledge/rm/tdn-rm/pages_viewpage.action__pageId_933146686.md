---
content_hash: 75087f71dc985d6dcb68c8133acd9450b48481f94cade676d21155f0aacdf22d
fetched_at: '2026-06-29T00:12:08.390437+00:00'
page_id: '933146686'
product: rm
source: tdn-rm
title: Histórico Salarial - Smart UI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=933146686
version: 8
---

**A partir das Versões:**

* [DT - Smart UI - Histórico Salarial](https://tdn.totvs.com.br/pages/viewpage.action?pageId=933147350)

## **CONTEÚ****DO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A informação de salário de um funcionário é primordial no ato de admissão. Este salário poderá ser alterado ao longo do contrato de trabalho, seja por convenção coletiva ou por concessão da empresa. As alterações salariais devem ser guardadas em um histórico salarial. Este histórico poderá ser utilizado para anotações na carteira profissional, para cálculos retroativos de possíveis diferenças, para relatórios e gráficos gerenciais, dentre outros.

## **02. EXEMPLO DE UTILIZAÇÃO**

Disponibilizamos a tela do **Histórico Salarial**utilizando a tecnologia **Smart UI** para as versões **12.1.2516** e superiores. Essa implementação trouxe uma atualização visual para a página, aprimorando não apenas sua aparência, mas também a forma como ela é utilizada, proporcionando uma experiência mais moderna e eficiente.

Veja a nova tela:

 O histórico salarial é acrescido de informações sempre que houver alteração diretamente no salário base do funcionário, tanto por alteração global de salário como por reprogramação salarial ou ainda individualmente, e também pode ser acrescentado diretamente linhas no histórico salarial, por motivo de migração ou outro motivo que seja necessário inclusão/alteração/exclusão diretamente no histórico.

Para a inclusão de um novo registro basta clicar em .

Para a Edição de um registro basta clicar no registro desejado e clicar em .

Após alterar os dados necessários clique em .

Caso queira **Excluir**o registro, é necessário selecionar a linha desejada e clicar em , após a confirmação o registro será excluído:

O sistema gravará a data de alteração salarial com dez minutos de acréscimo nos campos **Data Processamento** e **Data da Mudança**, caso seja alterado o salário do funcionário no mesmo dia que já ocorreu outra alteração.

A informação do campo **Data de Processamento** deve ser editada sempre que for inserido manualmente um novo registro, havendo valores posteriores já existentes.

Esse campo somente estará habilitado caso o parâmetro **Edita data de processamento**, localizado no menu Parametrizador | Folha de Pagamento | Funcionário | Restrições Cadastrais, esteja marcado, conforme demonstrado abaixo:

A alteração do histórico salarial de funcionários com salário composto permite modificar informações como **Tabela Salarial**, **Faixa** e **Nível Salarial**, desde que estejam habilitados os seguintes parâmetros no menu:  
Parametrizador | Folha de Pagamento | Funcionário | Restrições Cadastrais:

* **Utiliza Tabelas Salariais para evento de Salário Composto**
* **Edita Tabelas Salariais nos Eventos de Salário Composto**

**ATENÇÃO:** Estas informações são ocultas para aqueles funcionários que não recebem salário composto.

**📌 Exemplo de Simulação:**

No histórico salarial, o último registro existente é:

* + **Data de Processamento:** 01/11/2000
  + **Data da Mudança:** 02/11/2000
  + **Valor do Salário:** R$291,50

Ao incluir um registro retroativo que estava faltando antes desse já existente, a inclusão deve ser feita da seguinte forma:

* + **Data de Processamento:** 28/02/1996
  + **Data da Mudança:** 28/02/1996
  + **Valor do Salário:** R$ 270,00

**Atenção:**

* + A alteração da **Data de Processamento** influencia diretamente nos **cálculos de diferença salarial**.
  + Para que o sistema calcule corretamente as diferenças salariais, é fundamental que os registros do histórico salarial estejam consistentes e ordenados corretamente.
  + A ordenação utilizada para comparação entre o salário atual e o anterior é feita com base na **Data de Processamento**.

**EXEMPLOS DATA DE PROCESSAMENTO**

**Exemplo A**

|  |  |  |  |
| --- | --- | --- | --- |
| **Data de processamento** | **Data de mudança** | **Salário** | **Percentual** |
| 01/10/2008 | 01/10/2008 | R$1.000,00 | 0% |
| 01/12/2008 | 01/12/2008 | R$1.200,00 | 20% |

Neste caso o ultimo salário é R$1.200,00. O seu salário em 10/2008 é R$1.000,00  
   
   
**Exemplo B:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Data de processamento** | **Data de mudança** | **Salário** | **Percentual** |
| 01/09/2008 | 01/09/2008 | R$800,00 | 0 |
| 01/11/2008 | 01/11/2008 | R$1.000,00 | 25% |
| 01/12/2008 | 01/10/2008 | R$1.200,00 | 20% |

Neste caso o ultimo salário é R$1.200,00. O seu salário em 01/10/2008 é R$1.200,00, isso porque a data de processamento atual é última linha, mas a data de mudança se refere a 10/2008.   
Se for efetuado um cálculo de diferença iniciando em 10/2008 o sistema considerará que o funcionário tem uma diferença de R$400,00, visto que o cálculo será a diferença entre R$800,00 e R$1.200,00. Em relação ao salário de 01/10/2008 o funcionário teve um aumento de 50%.

No cálculo de diferença salarial retroativa o histórico salarial será preenchido da seguinte forma:

* **Data da Mudança:** Data oficial em que ocorreu a alteração salarial.
* **Data do Processamento:** Data em que foi processada a alteração salarial.

**Exemplo:**

* + **Data Atual:** 15/12/2008
  + **Data Alteração Salarial:** 01/10/2008
  + **Data de Processamento:** 15/12/2008
  + **Data da Mudança:** 01/10/2008

O campo **Nro. Salário** serve para funcionários que possuem salários compostos, será enumerado os salários de acordo com o número do salário registrado na pasta Salário Composto. Para os demais funcionários será colocado como default o número "1".

   
**Atenção:**  
Não será permitido incluir o "Nro. Salário" com o número de salário diferente de 1 quando não se utiliza salário composto para o funcionário.  
   
**Exemplo:**  
Funcionário com salário composto:  
Número do salário = 1 para o salário composto 1 registrado na pasta Salário Composto.  
Número do salário = 2 para o salário composto 2 registrado na pasta Salário Composto.  
Número do salário = 3 para o salário composto 3 registrado na pasta Salário Composto.  
   
Será informada a alteração de jornada automaticamente quando a alteração salarial for referente apenas ao campo "Jornada" e for processada através do módulo de alteração global salarial.

Outra funcionalidade que passou por alterações visuais e funcionais foi o gerenciamento e a aplicação de **Filtros**. Anteriormente, ao clicar em **Filtro**, era aberta uma janela pop-up para criar ou utilizar filtros existentes. Agora, ao clicar em **Filtro**, uma janela lateral será exibida, permitindo o gerenciamento de filtros de forma mais prática.

Nessa nova interface, estão disponíveis filtros padrão, como **"Motivo da Mudança"**, além da possibilidade de criar filtros personalizados. Para isso, basta clicar eme, em seguida, clicar em 

Para concluir a criação do Filtro, basta clicar então em **Salvar e Filtrar.**

Na tela inicial do **Histórico Salarial**, é possível ajustar as colunas do grid, permitindo fixá-las, alterar sua posição de exibição ou optar por não exibi-las. Além disso, também é possível definir a quantidade de registros a serem exibidos. Todas essas configurações podem ser realizadas através da função**Configurar Grid**.

## **03. TABELAS UTILIZADAS**

* PFHSTSAL
