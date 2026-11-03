---
content_hash: fcc2e61ca704edee36208624d01c22663488a0c0fdc1d572c53423644d4f2de5
fetched_at: '2026-06-29T00:10:44.395565+00:00'
page_id: '552575670'
product: rm
source: tdn-rm
title: Reajuste Revitalizado / Parâmetros Gerais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552575670
version: 24
---

Foi criado uma nova tela de parâmetros para o reajuste revitalizado onde no mesmo poderá ser definido os parâmetros que virão marcados/desmarcados no processo de reajuste.  
**Acesse Ambiente>> Parâmetros>> Gestão de Imóveis>> Contrato>> Reajuste Monetário>>** **Reajuste Revitalizado**.

Parâmetros disponíveis:

* **Reajustar no último dia do mês (tela reajuste - Pro-Rata)**

Utilizo o último dia do mês na data do reajuste selecionada, senão será utilizada a data informada na tela.

* **Reajustar até dia do Vencimento (tela reajuste - Pro-Rata)**

Utilizo o dia do vencimento da parcela na data do reajuste selecionada, senão será utilizada a data informada na tela.

* **Enviar o Reajuste Mês a Mês para o Financeiro / Contábil**

Serão enviados os valores dos reajustes, em todos os meses do intervalo do último reajuste, até a data selecionada,  senão será enviado apenas os valores do último mês do Reajuste.

* **Gerar Histórico das Tabelas de Reajuste do Legado**

Gerar as tabelas de histórico de reajuste XREAJUSTE, XREAJUSTEVENDA, XREAJUSTEPARCELA, XREAJUSTECOMPONENTEPARCELA e XREAJUSTECOMPONENTEREGRA. 

Para melhor performance, manter o parâmetro desmarcado

* **Contabilizar o reajuste sempre no mês atual**

Desmarcado, contabilizará na competência do reajuste.

* **Contabilizar o reajuste no último dia do mês.**

Desmarcado, contabilizará no primeiro dia do mês.

* **Validar se o evento contábil foi preenchido no reajuste.**

Se o evento de reajuste não estiver preenchido no contrato o sistema emitirá um erro de obrigatoriedade.

* **Reajustar utilizando data base.**

Marcado, utiliza o reajuste anterior para reajustar o próximo mês. 

Desmarcado , reajusta da forma antiga, sempre reajusta as parcelas em aberto desde o início do contrato.

Para melhor performance, manter o parâmetro marcado e se houver alteração de parâmetro que impacta o reajuste, o usuário deverá reajustar toda a base e marcar a opção *"Apagar o Log do Reajuste Anterior Antes de Iniciar o Novo Reajuste".*

*Quando marcar esse parâmetro o sistema deixará de voltar o reajuste para o início do contrato e passa usar a data base do último reajuste aplicado na base.  Caso haja mudança de parâmetros ou índices que impactam o reajustes já executados, o mesmo deve ser executado novamente e marcado a opção de apagar o data base para o sistema utilizar a nova parametrização*

* **Limitar o tamanho do log do Reajuste por data base.**

Limita o tamanho do log do reajuste, por data base, por no mínimo 12 meses, desmarcado mantem todo o log por data base.

Para melhor performance, manter o parâmetro marcado com 12 meses

* **Salvar a memória de cálculo no log de database.**

Esta opção salva o log da *memória de cálculo* dos reajustes de cada parcela da venda, período a período, no Histórico de Reajuste das Parcelas, que fica acessível no menu de *Anexos*, do *Log de reajuste das Parcelas.*

Por questões de performance, este parâmetro vem desmarcado, devido às informações deste campo gerarem um volume de dados considerável, fazendo com que a tabela deste campo ocupe muito espaço em disco.

Importa ressaltar que as informações deste campo não afetam nenhum processo do TCGI. 

* **Calcular o valor proporcional de Juros (Padrão) e CM (Todos) para antecipação de parcela com periodicidade > 1.**

Se o reajuste on-line  e deságio de juros price estiver marcado, então o sistema irá aplicar a taxa/índice proporcional do período de antecipação até o último aniversário da periodicidade. Somente aplica a proporcionalidade na antecipação de parcelas, ou seja, parcela com vencimento superior a data da geração do boleto. (Competências diferentes).

Ex.: Data do Contrato: 01/01/2020, Periodicidade 12 meses, Data para antecipação 01/09/2020 e data de vencimento 25/12/2030.

Se o parâmetro marcado, então irei aplicar o taxa/índice do dia 01/02/2020 a 01/09/2020, se desmarcado, não irei aplicar nada, pois seu próximo aniversário é somente no dia 01/01/2021. 

* **Aplicar no período atual do aniversário**

         Aplicar no período atual do aniversário, desde que o parâmetro anterior esteja marcado

* **Calcular o primeiro aniversário do resíduo com 12 meses**

         Calcular o primeiro aniversário do resíduo com 12 meses, desmarcado considera 13 meses

* **Calcular Pro Rata Utilizando Mês Comercial (30 dias). (Opção desmarcada utiliza mês Cheio )**

Utilizar a proporção de mês comercial no pro-rata utilizando a divisão por 30, desmarcado a opção utiliza mês cheio, ou seja, podendo a divisão ser por 31, 30, 29 ou 28 dias.

* **Aplicar Coeficiente Composto no CM. (Multiplica o coeficiente ao CM ao invés de somar)**

No cadastro de regra do componente de CM, existe a opção de aplicar coeficiente, ao utilizar essa opção o reajuste soma esse valor ao valor da moeda, com esse parâmetro marcado, o sistema irá multiplicar esses valores, fazendo o cálculo como COMPOSTO. 

Ex.:  INCC 01/2026 => 0,8% e Coeficiente 1,01:

* + - Parâmetro desmarcado = 0,008 + 0,01 = 0,018 ou 1,8%
    - Parâmetro marcado = 0,008 \* 0,01 =  1,008 \* 1,01  =  1,01808 = 0,01808 ou 1,808%

* **Não permitir que o Valor do CM acumulado fique negativo e reduza os valores de outros componentes (Original, Juros, Seguro e Outros)**
  1. Nenhum
  2. Zerar CM negativa no mês (sem compensação futura)
  3. Zerar CM negativa no mês (com compensação futura)

1. Nenhuma ação configurada
2. Zerar CM negativa no mês (sem compensação futura)
   1. Quando o índice de correção for negativo, o valor da correção do mês será zerado. O valor negativo **não** será acumulado e **não** reduzirá o saldo devedor ou as próximas parcelas.
   2. Não será permitido que o CM, independente do tipo de índice, fique negativo no acumulado. Esse parâmetro permite deflação até o limite do próprio valor do componente, por exemplo: 

      1. 1. 1. Valor Original: R$100.000,00;
            2. Juros Price: R$10.000,00
            3. Seguro: R$10.000,00
            4. CM: R$0,00
            5. Total Parcela: R$120.000,00
         2. 1. Reajuste INCC 01/2025 => 1%:  = Valor Base: R$120.000,00 \* 1% =  R$1.200,00 de CM => CM Acumulado: R$1.200,00
               1. Com o parâmetro **Nenhum** o  CM Acumulado ficaria em: **R$1.200,00**
               2. Com o parâmetro **marcado** o CM Acumulado ficaria em: **R$1.200,00**
            2. Reajuste INCC 02/2025 => -0,1%: = Valor Base: R$120.000,00 \* 1% =  - R$120,00 de CM => CM Acumulado: R$1.080,00
               1. Com o parâmetro **Nenhum** o  CM Acumulado ficaria em: **R$1.080,00**
               2. Com o parâmetro **marcado** o CM Acumulado ficaria em: **R$1.080,00**
            3. Reajuste INCC 03/2025 => -1%: = Valor Base: R$120.000,00 \* 1% =  -R$1.200,00 de CM => CM Acumulado: -R$120,00
               1. Com o parâmetro **Nenhum** o CM Acumulado ficaria em: **-R$120,00**
               2. Com o parâmetro **marcado** o CM Acumulado ficaria em : **R$0,00**
            4. Reajuste INCC 04/2025 => 1%: = Valor Base: R$120.000,00 \* 1% =  R$1.200,00 de CM => CM Acumulado: R$1.200,00
               1. Com o parâmetro **Nenhum** o  CM Acumulado ficaria em: **R$1.080,00**
               2. Com o parâmetro **marcado** o CM Acumulado ficaria em: **R$1.200,00**
3. Zerar CM negativa no mês (com compensação futura)
   1. Quando o índice de correção for negativo, o valor da correção da parcela do mês será zerado. Contudo, esse valor negativo será guardado como um **crédito/resíduo** para ser compensado e abater os próximos reajustes positivos.
   2. Não será permitido que o CM, independente do tipo de índice, fique negativo no acumulado. Mas o Valor Negativo será compensado quando houver índice negativo. O Valor está no log do reajuste para ver o quão negativo está.  Esse parâmetro permite deflação até o limite do próprio valor do componente, por exemplo: 

      1. 1. 1. Valor Original: R$100.000,00;
            2. Juros Price: R$10.000,00
            3. Seguro: R$10.000,00
            4. CM: R$0,00
            5. Total Parcela: R$120.000,00
         2. 1. Reajuste INCC 01/2025 => 1%:  = Valor Base: R$120.000,00 \* 1% =  R$1.200,00 de CM => CM Acumulado: R$1.200,00
               1. Com o parâmetro **Nenhum** o  CM Acumulado ficaria em: **R$1.200,00**
               2. Com o parâmetro **marcado** o CM Acumulado ficaria em: **R$1.200,00**
            2. Reajuste INCC 02/2025 => -0,1%: = Valor Base: R$120.000,00 \* 1% =  - R$120,00 de CM => CM Acumulado: R$1.080,00
               1. Com o parâmetro **Nenhum** o  CM Acumulado ficaria em: **R$1.080,00**
               2. Com o parâmetro **marcado** o CM Acumulado ficaria em: **R$1.080,00**
            3. Reajuste INCC 03/2025 => -1%: = Valor Base: R$120.000,00 \* 1% =  -R$1.200,00 de CM => CM Acumulado: -R$120,00
               1. Com o parâmetro **Nenhum** o CM Acumulado ficaria em: **-R$120,00**
               2. Com o parâmetro **marcado** o CM Acumulado ficaria em : **R$0,00 (crédito em:  -R$120,00)**
            4. Reajuste INCC 04/2025 => 1%: = Valor Base: R$120.000,00 \* 1% =  R$1.200,00 de CM => CM Acumulado: R$1.200,00
               1. Com o parâmetro **Nenhum** o  CM Acumulado ficaria em: **R$1.080,00**
               2. Com o parâmetro **marcado** o CM Acumulado ficaria em: **R$1.080,00**
            5. **Ou seja, fica o mesmo valor se não tivesse marcado o parâmetro, mas nunca deixa valor ficar negativo**
