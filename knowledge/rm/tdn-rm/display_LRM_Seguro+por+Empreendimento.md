---
content_hash: 3508d7168eed225a18a9e9ec91c0641ae9ab075c938fe648994bde55e58ab4be
fetched_at: '2026-06-29T00:09:47.842318+00:00'
page_id: '435105084'
product: rm
source: tdn-rm
title: Seguro por Empreendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Seguro+por+Empreendimento
version: 11
---

**Seguro por Empreendimento**

Neste Wizard, será gerado o Seguro por Empreendimento do Empreendimento e Vendas que foram selecionadas.  
 O sistema irá calcular mensalmente, o seguro dos contratos do TIN, por empreendimento, e gerar o valor do seguro calculado como componente da próxima parcela mensal em aberto, em forma de componente, dos contratos do RMSGI.   
 O processo irá efetuar o cálculo, multiplicando o saldo devedor do grupo (somatório das parcelas a vencer em aberto + o somatório das parcelas vencidas em aberto com multa e juros de mora) pelo percentual de seguro do grupo.  
  
 Se marcarmos o parâmetro "Calcular sem Multa e Juros de Atraso das Parcelas Vencidas", o sistema irá calcular o Seguro sem o valor da Multa e Juros de Atraso.  
  
 Se estiver informado um evento contábil na aba Seguro por Empreendimento na venda será realizado a contabilização da Inclusão do Seguro por Empreendimento ao executar o processo.

AtençãoO cálculo só ocorre para vendas efetivadas, com parcelas já geradas para o Financeiro e que tenha parcelas **VINCENDAS** em aberto. Observe também o período de vigência do componente de seguro.

---

Como Fazer
