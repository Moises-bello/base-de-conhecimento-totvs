---
content_hash: 0a7e147e0ffdd510adbcfb1206883b26728fdb8495920acec80564b72da0a854
fetched_at: '2026-06-29T00:09:48.362124+00:00'
page_id: '435105134'
product: rm
source: tdn-rm
title: Calcular Fechamento - Cálculos - Cálculo de Consumo (Medições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105134
version: 9
---

Ao executar o processo **"Calcular Fechamento"** para o item de **Consumo (Medições)**, serão processados e gerados os dados que servirão de insumo para a posterior geração dos lançamentos financeiros referentes ao condomínio, no **TOTVS Gestão Financeira**.

Para o fácil entendimento do Cálculo de Consumo (Medições), veremos abaixo os passos necessários para a utilização destes recursos:

**1º Passo -** O usuário deve cadastrar os medidores em **Condomínio / Medidor**;  
**2º Passo -** Realize o cadastro de Tarifas acessando **Medidor / Anexo Tarifa**.

Observação

Caso não seja associado uma Tarifa ao Medidor, o sistema pode buscar a Tarifa do Medidor Superior. Para que o sistema realize essa busca, o Medidor Superior deve estar associada ao mesmo Empreendimento, Unidade ou Subunidade do medidor a ser calculado.

**3º Passo -** Com isso, é preciso então associar os medidores necessários com os Empreendimentos desejados. Para isso, basta acessar **Condomínio / Empreendimento / Processos Associar Medidor**;   
**4º Passo -** É preciso que o usuário insira as medições em **Condomínio / Medidor / Anexo Medições**;  
**5º Passo -** Com as medições inseridas, ao utilizar o Processo de **Calcular Fechamento** localizado no cadastro de Fechamento, o sistema buscará as medições com a mesma competência do fechamento que está sendo apurado. Sendo que o medidor que possui as medições, precisa estar associado ao Empreendimento vinculado ao Fechamento.  
Ao final do processo, o status das medições apuradas será alterado para Calculado.

Observação

Caso um mesmo Medidor esteja associado a mais de um nível (Empreendimento, Unidade ou Subunidade), a apuração não poderá ser realizada, se os rateios forem:

* [Valor Fixo](http://tdn.totvs.com/pages/viewpage.action?pageId=435105104)
* [Rateio por CRD](http://tdn.totvs.com/pages/viewpage.action?pageId=435105196)
* [Rateio por M² Construído](http://tdn.totvs.com/pages/viewpage.action?pageId=435105299)
* [Rateio por M² Locado](http://tdn.totvs.com/pages/viewpage.action?pageId=435105202)
* [Rateio Linear por Total de Subunidades](http://tdn.totvs.com/pages/viewpage.action?pageId=435105093)

Como exemplo, podemos citar:

Medidor 1: Está associado aos seguintes níveis:

* Unidade A;
* SubUnidade 1 (Unidade B);
* SubUnidade 2 (Unidade B);

Ao executar o processo "Calcular Fechamento", será exibido uma mensagem alertando que não é possível realizar o cálculo para esse medidor.

Veja Também

**Considerar medições anteriores no fechamento**

O processo de Calcular Fechamento vai sempre considerar as medições de períodos anteriores que não tenham sido calculadas ou integradas no fechamento de sua competência. Todas as medições em aberto anteriores à competência do fechamento serão consideradas.

Exemplo:Caso o fechamento na competência de 01/2018 já esteja *Calculado* ou *Integrado*, quando o usuário cadastrar alguma medição para esta competência (01/2018), ao salvar esta medição, ele receberá a seguinte mensagem:  
*"Você está incluindo uma medição para uma competência que já possui o Fechamento calculado ou integrado. Se preferir continuar o cadastro, a medição somente será considerada para esse Fechamento se for realizado o Recalculo, caso contrário será calculada em um próximo Fechamento. Deseja continuar com a inclusão da medição?"*  
Desta forma, caso o usuário realize o recalculo no fechamento com competência em 01/2018, a medição inserida será vinculada ao fechamento. Porém caso o usuário realize o cálculo do fechamento de uma competência superior (Exemplo: 02/2018), então esta medição será vinculada à este fechamento.
