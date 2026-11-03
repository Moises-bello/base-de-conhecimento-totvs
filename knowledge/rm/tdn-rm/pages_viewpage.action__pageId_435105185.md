---
content_hash: 043d2586f45e8fe4ed3c435fb99cc22c6341447588b3ddc441df246a36006d9d
fetched_at: '2026-06-29T00:09:48.541846+00:00'
page_id: '435105185'
product: rm
source: tdn-rm
title: Parâmetros - Contrato - Reajuste Monetário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105185
version: 18
---

### **Etapa 1 - Reajuste monetário Pro-Rata Dia**

* **Modelo de Cálculo do Juros Pro-Rata dia:** Informe qual será o modelo de cálculo pró-rata dos juros de contrato. As opções de cálculo são:
  + **Pró-rata proporcional;**
  + **Pró-rata  temporis.**
* **Modelo de Cálculo da Correção Monetária Pro-Rata dia:** Informe qual será o modelo de cálculo pró-rata da Correção Monetária.
* As opções de cálculo são:
  + **Pró-rata proporcional;**
  + **Pró-rata  temporis.**

### **Etapa 2 - Reajuste Monetário**

* **Congela valor do resíduo da parcela após vencimento:** Se marcado, os valores de resíduo não serão corrigidos, ou seja, se a parcela de resíduo estiver vencida, ela não será reajustada. Será reajustado somente as parcelas vincendas.
* **Não permitir que a deflação altere o valor da Parcela para menos que o valor original:** 
  + **(Parâmetro descontinuado na 2410, mas continua funcionando para quem já marcou e não está utilizado o novo parâmetro);**
  + **Foi criando um novo parâmetro na Etapa 7 - Reajuste Revitalizado**
* **Reajusta parcelas "Em aberto" ou "Parcialmente Quitada" com vencimento anterior a data de reajuste:** Se marcado, o sistema irá reajustar todas as parcelas em aberto ou parcialmente quitada do plano de financiamento. Observação: Este parâmetro será descontinuado a partir da versão 12.1.21, pois, o sistema irá a partir desta versão reajustar as parcelas com vencimento anterior a data de reajuste independente das situações acima.

### **Etapa 3 - Reajuste monetário por coligada**

* **Precisão do Juros de Contrato:** Informe o número de casas decimais que será utilizado para o cálculo dos Juros de Contrato.
* **Arredondar a variação da moeda somente ao final do cálculo:** Se marcado, o sistema irá arredondar o resultado da correção somente no final de todo o processo do cálculo.
* **Ignorar a carência no Juros Price:** Se marcado, terá a finalidade de ignorar a carência ao calcular o Juros Price, ou seja, se a primeira parcela do grupo, que está parametrizado para o price, seja na venda ou no aditivo, for 2 ou mais meses superior a data da venda/aditivo, ou até inferior, o sistema irá ignorar essa carência no pagamento, e irá gerar o Juros Price como se a primeira parcela estivesse vencendo um mês após a venda/aditivo.
* **Modelo de cálculo PADRÃO: Arredondar variação da moeda apenas no início:** Se marcado, o sistema ira arredondar o resultado do cálculo do índice monetário no início, no modelo de Cálculo PADRÃO.

### Etapa 4 - Reajuste monetário por coligada

* **Permitir reajustar parcelas enviadas a banco no modelo PRICE:** Se marcado, o sistema irá permitir o reajuste de parcelas que já foram enviadas ao banco.
* **NÃO ALTERAR parcelas enviadas ao banco, no modelo de cálculo PADRÃO:** Se marcado, os lançamentos das parcelas que estiverem com status CNAB diferente de "Não Remetido" no TOTVS Gestão Financeira, o TOTVS Incorporação não irá reajustar estas parcelas. Se o usuário alterar o status CNAB para "Não Remetido", após efetuar um novo reajuste, estas parcelas serão corrigidas (atualizadas) normalmente.
* **Utiliza data vencimento para definir se a correção será com índice antes ou após:** Ao executar o processo de reajuste de uma parcela, o sistema utilizará a Data de Vencimento da parcela, ao invés da Data do Reajuste. Este parâmetro descontinuado na versão 12.1.23, pois o sistema sempre respeitará a referência de entrega do contrato para definir antes ou após.

### **Etapa 5 - Parâmetros do Reajuste**

Nesta etapa é possível parametrizar os itens básicos do reajuste, podendo escolher as opções Sim ou Não para as premissas abaixo:

* **Truncar Precisão Juros em vez de Arredondar.**
* **Desabilita Histórico de Reajuste Mensal.**
  + **Deixa de salvar dados na tabela "XPARCELAPAGAMENTOREAJUSTE" que server de base para a contabilização do reajuste**
* **Habilita fórmula por prioridade.**
* **Calcular Juros Após sobre Juros Antes da entrega (engine antiga).**
* **Habilita data base juros no modelo de cálculo "juros mensal".**
* **Habilita o reajuste paralelo.**

**Observação:** Os parâmetros "Calcula Correção Monetária sobre o Saldo Devedor Total Amortizado" e "Calcula Juros de Contrato sobre o Saldo Devedor Total Amortizado", foram descontinuados a partir da versão 12.1.23, onde o sistema sempre respeitará o cadastro de regra do contrato para reajustar os componentes.

A partir do Release 12.1.34, o *Parâmetro do Reajuste* ***Habilita Cálculo de Poupança da Real*** foi descontinuado.

### **Etapa 6 - Parâmetros do Reajuste**

* **Número de reajustes paralelos (por processador):** Indica quantas vendas serão reajustadas em paralelo para cada processador (núcleo) da máquina;
* **Valores calculados na correção serão arredondados mês a mês:** Se marcado, os valores calculados na correção serão arrendados mês a mês. **Observação:** Na versão 12.1.23 iremos descontinuar o parâmetro "Valores calculados na correção serão arredondados mês a mês", onde o sistema sempre irá arredondar ao final do reajuste para enviar os valores ao financeiro;
* **Data de Início de Reajuste não pode ser menor que a Data da Venda:** Se marcado, o sistema entenderá que se a Data Base dos componentes de reajuste for menor que a Data da Venda, então o início do Cálculo será a Data da Venda;
* **Considerar variação por periodicidade ao ignorar deflação no reajuste monetário:** Se marcado, quando o processo de reajuste estiver configurado para ignorar deflação ele irá considerar a variação na periodicidade;
* **Realizar a distribuição automática de Resíduo em todas as parcelas em aberto:** Se marcado, será realizada a distribuição automática de Resíduo em todas as parcelas em aberto com vencimento após o período de geração do resíduo;
* **Distribuir em componentes distintos os valores de resíduos de Juros de Contrato e Correção Monetária:** Se marcado, ao gerar a parcela de resíduo, o sistema deve separar juros de resíduo e CM de resíduo em 2 componentes separados.
* **Exibir a tela de aviso das vendas passando para o momento pós entrega no reajuste:** Se marcado esta opção, no momento do reajuste será exibido uma tela de aviso da venda se ela estiver passando de Antes da Entrega para Após a Entrega;
* **Habilita o Reajuste Automático no Cancelamento de Baixa de Parcela:** Se marcado, este parâmetro irá permitir que o sistema reajuste as parcela após o cancelamento de baixa para sincronizar com as outras parcelas da venda.

### **Etapa 7 - Reajuste Revitalizado [Clique](https://tdn.totvs.com/pages/viewpage.action?pageId=552575670) [A](https://tdn.totvs.com/pages/releaseview.action?pageId=546260610)[qui](https://tdn.totvs.com/pages/viewpage.action?pageId=552575670)**
