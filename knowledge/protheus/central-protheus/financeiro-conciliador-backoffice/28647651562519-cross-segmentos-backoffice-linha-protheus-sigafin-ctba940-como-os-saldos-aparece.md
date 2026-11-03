---
article_id: 28647651562519
category: Financeiro - Conciliador Backoffice
content_hash: 24f74c115d1d34dcb9d217160516de9548608e0838829b5979da7923b616e97c
fetched_at: '2026-06-28T22:37:47.179087+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Como os saldos
  aparecem no novo conciliador financeiro
type: support-article
updated_at: '2025-10-24T12:36:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28647651562519-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Como-os-saldos-aparecem-no-novo-conciliador-financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28647627915287) Tempo aproximado para leitura: **00:15:00 min****Dúvida**  
Como os saldos são apresentados no novo conciliador financeiro?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - 12.1.2310

**Solução:**

O conciliador não realiza nenhum tipo de processamento, atuando apenas como **uma ferramenta de consulta,** ou seja, ele monta a exibição com base nas informações já registradas na tabela SE8.   
  
Nesse contexto, os saldos são apurados na SE8, e refletidos para o conciliador, considerando:

* **Saldo anterior**: obtido por meio da somatória dos saldos dos dias anteriores;
* **Saldo atual**: baseado na somatória das movimentações do dia corrente + saldo acumulado

Por esse motivo, sempre que houver dúvidas sobre os valores exibidos, recomendamos validar diretamente os dados registrados na **FINA030**, observando se os saldos estão sendo alimentados corretamente conforme o esperado.  
  
**Exemplo prático:**  
Foram gerados dois títulos no financeiro:

* R$ 1.000,00 a pagar (CP)
* R$ 1.000,00 a receber (CR)

#### 

Ambos **ainda não conciliados,** logo, permanecem com o campo **Saldo Reconc (SE8\_RECONC)** em branco.

Resultado na rotina FINA030 - Atualizações de saldos bancários

#### 

* **Saldo Atual = Saldo bancário:** R$ 0,00
* **Saldo Reconc = Saldo conciliado:** R$ 0,00

Ao consultar o dia 26/07 (posterior a data do lançamento, por exemplo), o sistema buscará o saldo mais recente disponível nos dias anteriores. Caso não encontre saldo do dia 25, buscará do dia 24, e assim por diante. Essa é a lógica padrão de exibição adotada pelo conciliador.

Os saldos no conciliador devem ser exibidos através do botão **"saldos bancários"** alocado na parte superior do browser:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723363745559)

Considerando o exemplo acima, os saldos do conciliador devem ser R$0,00 quando não há nenhuma conciliação efetivada, conforme print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723336591511)

Podemos ver que temos:

* Saldo Atual (Bancário)  = R$ 0,00
* Saldo Atual (Conciliado)  = R$ 0,00

Ao conciliar um título dos lançamentos acima, teremos uma atualização no saldo conciliado, conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723336593431)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723363750807)

Os saldos serão refletidos no conciliador:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723363751447)

**Na data do dia 26/07/2025**

**FINA050 (contas a pagar)** - Inclui um título de número A001 a pagar no valor R$ 50,00 com status baixado (movimentando banco)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723336602903)

Podemos observar que temos no dia **26/07/2025**  
Uma movimentação a pagar no valor de R$ 50,00 que foi o único título do dia **26/07/2025**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723363754519)**

E um total no dia **26/07/2025** de **R$ -50,00** na rotina **FINA030**

Vamos conciliar para o registro ir para a aba **"Dados de Conciliação"**, conforme processo abaixo:

![Design sem nome.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33723336608791)

#### Para consultamos os saldos é necessário clicar no botão **"Saldos Bancários"**. É possível visualizar o extrato, que inclui o saldo anterior (bancário e conciliado), as entradas e saídas, além do saldo atual (bancário e conciliado).

Segue exemplo de saldos, logado na data do dia **26/07/2025:**

* Saldo anterior (Bancário) = **R$ 0,00**
* Saldo anterior (Conciliado) = **R$ -1.000,00**
* Saldo atual (Bancário) = **R$ - 50,00**
* Saldo atual (Conciliado) = **R$ -1050,00**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33723363759767)

**Importante 🚩️**

Os registros feitos na rotina "**FINA380 - Conciliação Bancária Manual**" ficarão na aba "**Dados não encontrados**", não sendo necessário conciliá-los novamente, pois já foram conciliados na rotina antiga, pois deve haver uma data de corte entre uso da rotina antiga com a rotina nova.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/28647627931799)](https://tdn.totvs.com/pages/releaseview.action?pageId=754946735)

**Saiba mais**

[Conciliadores Bancários Manual e Automático (FINA380 e FINA473)](https://tdn.totvs.com/pages/releaseview.action?pageId=754946735)
