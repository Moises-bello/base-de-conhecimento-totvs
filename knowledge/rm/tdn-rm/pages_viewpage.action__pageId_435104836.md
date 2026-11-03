---
content_hash: dec2d3beed737564db3de6e7f721eb1a1849873df534f6fdab6284af4cc69844
fetched_at: '2026-06-29T00:09:46.559997+00:00'
page_id: '435104836'
product: rm
source: tdn-rm
title: Calcular Fechamento - Cálculos - Cálculo de Cobrança Direta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104836
version: 9
---

Ao executar o processo de **Calcular Fechamento** para o item de **Cobrança Direta**, serão gerados registros que irão compor o valor total dos lançamentos referentes ao condomínio. Desta forma, todas as cobranças feitas no mesmo período de vigência do Fechamento calculado serão apuradas para a geração dos respectivos lançamentos.   
São exemplos de cobrança direta: taxa de condomínio fixa, fundo de reserva e multas por infrações no empreendimento.

Na execução do fechamento integral, o sistema utilizará todas as cobranças diretas em que a competência do fechamento esteja entre a data inicial e a data final da cobrança.   
Para realizar o rateio da cobrança é utilizado o modelo definido no cadastro de cobrança direta. São as opções disponíveis:



Particularidades:

* No cadastro de Cobrança Direta, temos o campo de Item de Cobrança, no qual será utilizado para compor o valor do lançamento a ser gerado. Esse item de cobrança pode ou não estar associado à um **Valor de Integração**. Lembrando que os registros de Valores de Integração tem origem no **TOTVS Gestão Financeira.**
* Após realizar o processo de **Calcular Fechamento**, no fechamento integral, serão gerados os registros para cada apartamento do Empreendimento selecionado, calculados de acordo com os parâmetros de modelo de cálculo exemplificados acima.
* No fechamento integral, cada subunidade terá um registro no histórico do Fechamento, podendo ser visualizadas em **Condomínio / Fechamento do Condomínio / Histórico de Cálculos**.
* No fechamento integral, depois do processo concluído, o sistema lista todas as cobranças diretas que foram utilizadas no fechamento em **Condomínio / Fechamento do Condomínio / Cobrança Direta.** Para mais informações sobre essa tela .

Importante: No fechamento integral, não será possível realizar o cálculo da cobrança direta caso exista um [adiantamento de cobrança](https://tdn.totvs.com/pages/viewpage.action?pageId=553898548) associado ao fechamento. Para que os cálculos das cobranças diretas sejam realizados, deve-se primeiro, realizar a integração financeira do adiantamento, gerando seus respectivos lançamentos.

Esta regra não se aplica ao fechamento individual, visto que as cobranças são calculadas por subunidade, não sendo possível incluir adiantamentos ou cobranças complementares.
