---
content_hash: a0e17a389e791a4dfecf241b1c2631dea28e5c4650ef60a1d475f5c90815531d
fetched_at: '2026-06-29T00:12:03.582169+00:00'
page_id: '911862386'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Cálculos - Cálculo de Cobrança Direta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911862386
version: 2
---

**Procedimentos para Utilização**

---

Ao executar o processo de **Apurar Condomínio** para o item de **Cobrança Direta**, serão gerados registros que irão compor o valor total dos lançamentos referentes ao condomínio, de acordo com as subunidades escolhidas. Desta forma, todas as cobranças feitas no mesmo período de vigência do Fechamento calculado serão apuradas para a geração dos respectivos lançamentos para estas subunidades.   
São exemplos de cobrança direta: taxa de condomínio fixa, fundo de reserva e multas por infrações no empreendimento.

Na apuração do fechamento individualizado, o sistema utilizará todas as cobranças diretas em que a competência do fechamento esteja entre a data inicial e a data final da cobrança.   
Para realizar o rateio da cobrança é utilizado o modelo definido no cadastro de cobrança direta. São as opções disponíveis:



**Particularidades do Processo**

---

* No cadastro de Cobrança Direta, temos o campo de Item de Cobrança, no qual será utilizado para compor o valor do lançamento a ser gerado. Esse item de cobrança pode ou não estar associado à um **Valor de Integração**. Lembrando que os registros de Valores de Integração tem origem no **TOTVS Gestão Financeira.**
* Após realizar o processo de **Apurar Condomínio,** no fechamento individualizado, serão gerados os registros para cada subunidade selecionada no processo, calculados de acordo com os parâmetros de modelo de cálculo exemplificados acima.
* No Fechamento individualizado o histórico de cálculo é observado na própria aba anexa de Apuração do Condomínio, podendo o log ser verificado ao dar dois cliques na subunidade que fez parte do processo.
* No fechamento individualizado, basta consultar as apurações de cobrança direta indo direto na subunidade que fez parte do processo, na aba Apuração do Condomínio.

Importante: No fechamento integral, não será possível realizar o cálculo da cobrança direta caso exista um [adiantamento de cobrança](https://tdn.totvs.com/pages/viewpage.action?pageId=553898548) associado ao fechamento. Para que os cálculos das cobranças diretas sejam realizados, deve-se primeiro, realizar a integração financeira do adiantamento, gerando seus respectivos lançamentos.

Esta regra não se aplica ao fechamento individual, visto que as cobranças são calculadas por subunidade, **não sendo possível incluir adiantamentos ou cobranças complementares.**
