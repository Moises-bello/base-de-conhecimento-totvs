---
content_hash: 28f25c71bec6ec23c9789c8ddeddd3583512b36642cf6cb8e8a021e817452b2f
fetched_at: '2026-06-29T00:10:30.360615+00:00'
page_id: '519726472'
product: rm
source: tdn-rm
title: Contabilização de Curto e Longo Prazo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519726472
version: 51
---

Será possível contabilizar os valores vincendos do contrato de venda considerado o curto prazo ou longo prazo.

ParametrizaçãoParametrização|Parametrização |

Será possível definir como o sistema irá consistir o período de corte para o processo de Contabilização de Curto e Longo prazo. É necessário acessar os parâmetros do Totvs Incorporação através da aba ‘Ambiente’>>Parâmetros>>Totvs Incorporação. Após selecione a opção ‘Integração Contábil’ e avance.

**Ação dos parâmetros:**

|  |  |
| --- | --- |
| **Utilizar Período Contábil para calcular os valores de curto e longo prazo** | Essa opção não pode ser marcada, sempre o sistema irá considerar como data inicial do curto prazo a data da Venda, Aditivo, Reajuste, Seguro Prestamista ou Distrato.  Habilitado, define que o sistema irá considerar o período contábil como base para a data inicial do curto prazo. A data se atualiza a cada adequação do período contábil (Período de Apuração). Desmarcado o sistema irá considerar como data inicial do curto prazo a data da Venda, Aditivo, Reajuste, Seguro Prestamista ou Distrato. |
| **Período limite curto prazo (Em meses)** | Define a quantidades de meses que o sistema considerar como curto prazo. |
| **Período de Apuração da Transferência (Em meses)** | A apuração sempre é mensal não tem a opção de alterar   Define o período (meses) que os valores serão transferidos das contas de longo prazo para o curto prazo. |
| **Inverter a Conta Contábil do Aditivo** | Inverter a conta contábil do aditivo caso o valor seja negativo |

**Por Default o sistema irá apresentar as opções da seguinte forma:**

* ‘Utilizar Período Contábil para calcular os valores de curto e longo prazo’ habilitado.
* Período limite curto prazo (Em meses) como 24 ou 12.
* Período de Apuração da Transferência (Em meses) como 12 ou 1.

Informações

É possível visualizar uma documentação especifica para a parametrização acessando o link a seguir: 

Utilizando Período Contábil|Utilizando Período Contábil |

**Parâmetro: Essa opção está desativado no sistema, tendo a opção somente desmarcado**

5
complete
**Utilizar Período Contábil para calcular os valores de curto e longo prazo**

Considerando 3 vendas distintas, com o período contábil de de 2 anos. As vendas foram criadas com datas diferentes para demonstrar a evolução dos períodos. conforme tabela a seguir:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Vendas** | **Data da Venda** | **Data Limite Curto** | **Período de curto** | **Período de Transferência Apuração** |
| **A** | 02/01/2019 | 31/12/2020 | 24 | 12 |
| **B** | 01/02/2019 | 31/12/2020 | 24 | 12 |
| **C** | 01/03/2020 | 31/12/2021 | 24 | 12 |

Utilizando Plano de Financiamento|Utilizando Plano de Financiamento |

**Parâmetro:**

6
incomplete
 **Utilizar Período Contábil para calcular os valores de curto e longo prazo**

Considerando 3 vendas distintas, com um plano de financiamento de 12 parcelas. As vendas foram criadas com datas diferentes para demonstrar a evolução dos períodos. conforme tabela a seguir:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Vendas** | **Data da Venda** | **Data Limite Curto** | **Período de Curto** | **Período de Transferência Apuração** | **Parcelas** |
| D | 10/01/2019 | 31/04/2019 | 3 | 1 | 12 |
| E | 15/02/2019 | 30/05/2019 | 3 | 1 | 12 |
| F | 09/03/2019 | 31/06/2019 | 3 | 1 | 12 |

Exemplo com Plano de Financiamento|Exemplo com Plano de Financiamento |

**Exemplo de período Trimestral com apuração mensal:**

**Exemplo dos Valores que serão Contabilizados:**

Exemplo com Período Contábil|Exemplo com Período Contábil |

### **Essa opção está desativado no sistema, tendo a opção somente desmarcado**

**Exemplos de Período Contábil anual:**

**Exemplo de atualização da Data Limite para curto prazo:**

**Exemplo dos Valores que serão contabilizados:**

Gerando a Contabilização RM|Gerando a Contabilização no RM|

No cadastro do contrato de Venda é necessário que seja informado na aba 'Contabilidade' os Eventos Contábeis que estão estruturados para a utilização da contabilização de Curto e Longo prazo. A contabilização será gerada seguindo o gatilho/processo de origem(Efetivação da Venda, Reajuste, Distrato e etc).

* **Venda**   
  A contabilização da venda será criada na efetivação do contrato.
* **Reajuste**  
  Durante a execução do processo de Reajuste o sistema irá criar a contabilização do Reajuste.
* **Distrato**  
  Ao efetivar o Distrato será criado a contabilização.

* **Seguro Por Empreendimento**  
  Ao concluir a geração do Seguro por Empreendimento, será realizado a contabilização.
* **Aditivo**  
  A contabilização será criada na efetivação do Aditivo. Caso o parâmetro **Inverter a conta contábil do aditivo caso o valor seja negativo**, esteja marcado o sistema realiza a inversão parcial das contas para gerar o estorno do curto para contabilizar no longo ou vice -versa.
* **Transferência**  
  Ao realizar o processo de Contabilizações de Transferências de Longo para Curto Prazo, a contabilização atualizada.

O cadastro do Evento Contábil é fundamental para o correto funcionamento da contabilização, na sua estruturação deve ser considerado todos o processos que serão contabilizados. 

Para visualizar a contabilização é necessário acessar o aba do sistema, 'Contabilidade' e apos acessar o menu Lotes, o sistema irá criar automaticamente um lote para cada operação utilizada que irá armazenar is dados referente a partida contábil.

Importante

Informações referente ao cadastro de Evento Contábil: 

Contabilização Curto e Longo 

Além de contabilizar os valores de juros de contrato, correção monetária, seguro prestamista, o cliente pode criar outros valores como taxas que precisam ser contabilizados. Para isso, será necessário criar o valor de incidência "Valores Agregado da Venda" a curto e a longo prazo para a contabilização da venda e da transferência. 

     Feita esta melhoria na contabilização para criar valores de incidência para "Valores Agregados" da venda como taxa administrativa, taxa Limpeza.  
Cálculo da incidência (Valor da Parcela - Original - Juros - CM - Seguro)                            

Configuração padrão de como gerar contabilização curto e longo prazo

Plano de Financiamento padrão com Juros, CM e Seguro por Empreendimento

Eventos que devem ser configurados, logo abaixo irei mostrar cada evento, não esquecer de fazer o mesmo para eventos deflacionário que inverte a conta.

Plano de Financiamento gerado

Na primeira parcela tem valor original de R$2500,00, seguro de R$ 1000,00 e R$20,00 de taxa de administração lançado via aditivo

Tipos de Eventos Contábeis

Agora como realizar a configuração dos eventos

Importante

Informações referente ao cadastro de Evento Contábil e variável:

Evento da Venda 

Evento da Venda

Siglas:

V - Venda

CP - Curto Prazo

LP - Longo Prazo

No débito foi configurado uma conta de CP utilizando a variável Valor Venda Curto Prazo e LP utilizando outra conta com a variável Valor Venda Longo Prazo.

No crédito pode configurar a mesma conta para CP e LP utilizando a variáveis acima ou usando apenas a variável Valor Venda que é a soma das duas.

Caso a venda fosse Juros Price, então configure evento com as variáveis de juros CP e LP

Evento do Reajuste

Evento do Reajuste

Siglas:

CM - Correção Monetária

CP - Curto Prazo

LP - Longo Prazo

No débito foi configurado uma conta de CP utilizando a variável Valor Juros Ambos Curto Prazo e Valor Monetária Ambos Curto Prazo, e para LP utilizando outra conta com a variável Valor Juros Ambos Longo Prazo e Valor Monetária Ambos Longo Prazo.

No crédito pode configurar a mesma conta para CP e LP utilizando a variáveis acima ou usando apenas a variável Valor Juros Ambos e valor Monetária Ambos que é a soma das duas.

Caso a venda fosse Juros Price a configuração deve ficar no evento da venda

Evento do Seguro por Empreendimento

Evento do Seguro por Empreendimento

No débito foi configurado uma conta de CP utilizando a variável Valor Seguro Prestamista Curto Prazo e LP utilizando outra conta com a variável Valor Seguro Prestamista Longo Prazo.

No crédito pode configurar a mesma conta para CP e LP utilizando a variáveis acima ou usando apenas a variável Valor Seguro Prestamista que é a soma das duas.

Evento do Aditivo

Evento do Aditivo - Alteração de Valor de Parcela

No débito foi configurado uma conta de CP utilizando a variável Valor Aditivo Venda Curto Prazo e LP utilizando outra conta com a variável Valor Aditivo Venda Longo Prazo.

No crédito pode configurar a mesma conta para CP e LP utilizando a variáveis acima ou usando apenas a variável Valor Aditivo Venda que é a soma das duas.

Evento do Distrato

Evento do Distrato

No débito foi configurado uma conta de CP utilizando a variável Valor Saldo Devedor Curto Prazo e LP utilizando outra conta com a variável Valor Saldo Devedor Longo Prazo.

No crédito pode configurar a mesma conta para CP e LP utilizando a variáveis acima ou usando apenas a variável Valor Saldo Devedor que é a soma das duas.

Não esqueça de configurar os eventos de pagamento para devolução de valores se for o caso.

Evento de Transferência

Evento de Transferência

Na transferência não iremos colocar os eventos de seguro e aditivo, pois no meu exemplo eles são sempre lançados na competência do vencimento da parcela que estão sendo gerados boletos, sendo assim sempre são lançados na conta de Curto Prazo. Desta forma, não precisa configurar, caso seja lançado no futuro deve-se configurar.

No débito vou configurar a conta de CP para receber do Crédito de Longo Prazo utilizando as variáveis já citadas acima.

Valor Venda Curto Prazo

Valor Venda Longo Prazo

Valor Monetária Ambos Curto Prazo

Valor Monetária Ambos Longo Prazo

Valor Juros Ambos Curto Prazo

Valor Juros Ambos Longo Prazo

Competência Contábil

**Dados da configuração do contrato**

**Data da Venda : 01/04/2021**

**Período de Curto Prazo : 12**

**Transferência: Mensal**

Competência 04/2021Competência 04/2021

Data da operação da competência: 04/2021

Contabilizando a Efetivação da Venda

Período considerado Curto Prazo: 01/04/2021 a 30/04/2022

R$2500,00 \* 12 meses = R$30.000,00

Período considerado Longo Prazo: 01/05/2022 até o fim do Plano de Financiamento

R$2500,00 \* 28 meses = R$70.000,00

Não existe outras operação nessa competência

A transferência de Longo para Curto foi executada no mês 04/2021 e não lançou valor por não ter nada a transferir, pois a única operação nesse mês é a efetivação da venda

aaaaCompetência 05/2021Competência 05/2021

Data da operação da competência 05/2021

Período considerado Curto Prazo: 01/05/2021 a 31/05/2022

Período considerado Longo Prazo: 01/06/2022 até o fim do Plano de Financiamento

Lançando o Seguro Por Empreendimento na parcela de vencimento 01/05/2021

Não tem longo prazo, porque sempre é lançando na competência do mês, desta forma não precisa colocar essa conta do seguro na transferência

Lançando a Taxa de Administração de 20 via aditivo de alteração de valor de parcela na parcela de vencimento 01/05/2021

Não tem longo prazo, porque sempre é lançando na competência do mês, desta forma não precisa colocar essa conta do seguro na transferência

Não tem reajuste para a competência 05/2021, pois o reajuste é anual.

Então vamos realizar Transferência das Contas de Longo para Curto Prazo

Somente do valor original da parcela 01/05/2022 que deixou de ser longo para ser curto prazo, sendo que o seguro e taxa não tem valor de transferência pois lança na parcela do mês e já coloca na conta certa de curto prazo.

Competência 04/2022Competência 04/2022

Vou fazer o processo de Seguro, taxa Administrativa e transferência até chegar o Primeiro Reajuste em 01/04/2022, até essa data tudo continua da mesma forma que foi explicado nos itens anteriores.

Data da operação da competência 04/2022

Período considerado Curto Prazo: 01/04/2022 a 30/04/2023

Período considerado Longo Prazo: 01/05/2022 até o fim do Plano de Financiamento

Nessa competência iremos fazer apenas para efeito didático o reajuste e a transferência para não ficar repetitivo

1º reajuste do contrato em 01/04/2022

Veja que no reajuste, o sistema já faz a contabilização correta das 13 próximas parcelas como curto e o resto como longo

No caso do reajuste, o sistema já faz o tratamento da parcela 01/04/2023 como sendo curto prazo e desta forma não será considerado na transferência.

Curto Prazo Juros: 13 parcelas \* R$300,00 =  R$3900,00

Curto Prazo CM: 13 parcelas \* R$88,50 =  R$1150,50

Longo Prazo Juros: 16 parcelas \* R$300,00 =  R$4800,00

Longo Prazo CM: 16 parcelas \* R$88,50 =  R$1416,00

CM

Juros

Não haverá transferência de valor para reajuste nesse mês, pois foi o primeiro mês de reajuste e no reajuste do mês o sistema já lançou parte do valor no curto e parte no longo. Somente haverá transferência de valor original da parcela com vencimento de 01/04/2023 que vira curto prazo

Competência 05/2022Competência 05/2022

Data da operação da competência 05/2022

Período considerado Curto Prazo: 01/05/2022 a 31/05/2023

Período considerado Longo Prazo: 01/06/2023 até o fim do Plano de Financiamento

No mês 05/2022 não haverá reajuste, mas haverá normalmente o lançamento de seguro e taxa como processo do mês e já lançado no evento de curto prazo, já que estamos lançando na parcela do mês

Agora ao realizar a transferência de longo para curto o reajuste que aconteceu no mês passado passa a entrar na transferência desse mês, pois a parcela com o valor de cm e juros de 05/2023 deixa de ser longo prazo e vira curto prazo

Competência 06 a 07/2022Competência 06 a 07/2022

Data da operação da competência 06/2021

Período considerado Curto Prazo: 01/06/2022 a 30/06/2023

Período considerado Longo Prazo: 01/07/2023 até o fim do Plano de Financiamento

Data da operação da competência 07/2021

Período considerado Curto Prazo: 01/07/2022 a 31/07/2023

Período considerado Longo Prazo: 01/08/2023 até o fim do Plano de Financiamento

E segue essa lógica daqui para a frente da transferência

Ao realizar o distrato devemos zerar o saldo das contas de Curto e Longo prazo e conta padrão

Transferência do Longo para o Curto Prazo|Transferência do Longo para o Curto Prazo

Os valores de Curto e Longo prazo são alterados com de acordo com o avanço do período, o sistema atualiza o período considerando o processo que foi executado no contrato de venda. Com isso é necessário atualizar  os valores contábeis movendo um montante das contas de Longo Prazo para o Curto prazo.

Importante

É necessário acessar o perfil vinculado ao usuário e conceder permissão para execução do processo. Acesse o cadastro de Perfil do sistema 'Incorporação' edite o cadastro do perfil que está sendo utilizado vá aba 'Acesso a Menus', de permissão as TAGS:

**[04.02.03]Contabilizações de Transferência de Longo Para Curto Prazo**  
**[04.02.03.01]Contabilizar Transferência: Estornar**

Para execução do processo é necessário acessar aba do sistema 'Contabilidade' em seguida o menu '**Contabilizações de Transferência de Longo Para Curto Prazo**' , após acessar a visão deve-se ir ao menu Processos>>**Contabilizar/Estornar Transferência**. Na visão do processo deve ser selecionado o **Contrato** que deseja realizar a transferência, informado o **Tipo de Processo** e o **Período da Competência de Transferência,** caso seja exercício contábil sempre transferirá no último dia do mês do ano.

Tipo de Processo

* Contabilizar: Realiza a Transferência do contrato selecionado.
* Estornar: Realiza o estorno contábil do contrato selecionado.
* Recontabilizar(Estornar e Contabilizar): Permite que que seja feito o reprocessamento da operação.

Sempre que for executado o processo de Contabilizar o contato o sistema irá criar um registro na visão de '**Contabilizações de Transferência de Longo Para Curto Prazo**' que será contabilizada no última dia da competência do período selecionado.

Transferência do Longo para o Curto Prazo|| Fórmulas 

| PARMQRY | Retorna o valor de um campo com passagem em parâmetros |
| --- | --- |
| **CONTEXTO** | Usa como contexto os dados do processo |
| **SINTAXE** | CONVERTDATE( PARMQRY('DATAREFERENCIA')) |

| PARMQRY | Retorna o valor de um campo com passagem em parâmetros |
| --- | --- |
| **CONTEXTO** | Usa como contexto os dados do processo |
| **SINTAXE** | PARMQRY('NUM\_VENDA') |

| PARMQRY | Retorna o valor de um campo com passagem em parâmetros |
| --- | --- |
| **CONTEXTO** | Usa como contexto os dados do processo |
| **SINTAXE** | PARMQRY('NUMVENDA') |
