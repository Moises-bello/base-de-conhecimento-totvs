---
article_id: 4406452757399
category: SIGAEST - SALDOS
content_hash: 9e20333ab726c193877e0cac010087840e7592ae0bcc46c9a9c713f0fb2a3848
fetched_at: '2026-06-28T22:39:14.931791+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual o objetivo do
  parâmetro MV_ESTNEG?
type: support-article
updated_at: '2025-12-08T12:52:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406452757399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-o-objetivo-do-par%C3%A2metro-MV-ESTNEG
---

O parâmetro MV\_ESTNEG no sistema TOTVS Protheus controla se os saldos em movimentações internas de estoque podem ficar negativos (S) ou não (N). Ele bloqueia movimentações internas como requisição, desmontagem e transferências quando o saldo é insuficiente, mas não afeta o faturamento, onde saldo negativo pode ocorrer em liberações manuais. Para evitar faturamento sem saldo, deve-se usar liberação automática.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25853153808663) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**  
Qual é o objetivo de configurar o parâmetro MV\_ESTNEG? Como ele funciona sistemicamente falando no estoque, e no faturamento para notas fiscais de saída?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O parâmetro MV\_ESTNEG, serve para indicar se o sistema permitirá que os saldos **em movimentações internas de estoque** dos produtos fiquem negativos ou não, onde:

* S = Sim (Permite que os saldos possam negativar)
* N = Não (Não permite que os saldos negativem)

**Quais são tipos de movimentações internas de estoque?**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os significados dos códigos dos tipos de Movimentos Internos RE/DE?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007057091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-significados-dos-c%C3%B3digos-dos-tipos-de-Movimentos-Internos-RE-DE)

**Como vou saber que o sistema barra negativar a movimentação interna?**

Por exemplo, seu saldo atual fisico do produto é 30 *(Saiba como consultar o saldo atual através do cadastro do mesmo, pressionando o botão F4 no produto* [*Aqui*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto)*)*, e o usuário tenta fazer qualquer **movimentação interna de estoque** como por exemplo: REQUISIÇÃO/DESMONTAGEM/TRANSFERENCIAS *(Demais tipos de requisições de estoque saiba mais* [*clicando aqui*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007057091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-significados-dos-c%C3%B3digos-dos-tipos-de-Movimentos-Internos-RE-DE#:~:text=Movimenta%C3%A7%C3%B5es%20de%20saida%20RE%3A)*)* O sistema vai acusar pra você a seguinte mensagem:

**MATA241 - Movimentação Múltipla**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25853153810583)

**MATA242 - Desmontagem**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25853217012119)

**MATA261 - Transferência Múltipla**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25853804899479)

**MATA310/MATA311 - Transferencia entre filial/Solicitação Tranferencia**

Caso o parametro **MV\_ESTNEG esta como N**, ou produtos controlem lote ou endereço, e também SALDO de terceiros, e não tiverem o saldo suficiente para efetivar a transferencia, a validação de saldo no processo de transferencia ou solicitação, sera para bloquear a movimentação pois não há saldo.

Caso desejar permitir a movimentação sem saldo útil na origem, a alteração do parametro **MV\_ESTNEG = S**, permite a movimentação.

Essa validação é devida nas rotinas MATA310/MATA311, pois se tratam de facilitadoras do Estoque, a validação de distribuição do saldo efetivo, sempre sera tratado na rotina de Pedido de venda, sobre analise de credito/estoque, a serem tratados com o seu Faturamento ou não para liberação.

**Segue validação na rotina MATA310**

![Screenshot_13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30834921460247)

**Segue validação na rotina MATA311**

![Screenshot_14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30834906939543)

**Mas eu fiz uma nota de FATURAMENTO e o meu SALDO ficou negativo, por quê?**

No **Ambiente de Faturamento** o MV\_ESTNEG **não tem efeito**, ao realizar uma Liberação Manual de Estoque, o sistema irá **negativar o saldo do produto**, independentemente da configuração deste parâmetro.

Para que **não seja faturado** produto que **não possui saldo** é necessário realizar a Liberação do Pedido somente de forma **Automática**.

Para saber mais sobre os Tipos de Liberação, consulte a documentação da area de Faturamento [**clicando aqui**](https://tdn.totvs.com/x/RjS4Ew)

Para retirar a permissão para Liberação Manual de Estoque, [**veja esta documentação.**](https://tdn.totvs.com/x/VUBtDQ)

### **Caso voce tenha um produto com saldo ATUAL negativo e tente efetuar uma nota de entrada desse item contra OP, sera apresentado o seguinte HELP com a validação do parametro como N.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34612723975063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34612723976343)

Dessa forma a classificação da NOTA não sera efetivada, pois voce tem a configuração do parametro MV\_ESTNEG como N, e se acaso queira descobrir o porque o saldo atual do produto esta negativo, sugerimos o seguinte:

* Processar o refaz saldos, para atualizar o saldo atual corretamente
* Gerar o relatorio MATR900 configurado exatamente conforme boletim, até a data ATUAL, assim voce vera as movimentações geradas e qual foi a que negativou os saldos. (MV\_ESTNEG não trata FATURAMENTO).
* [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)

**Boletim relevante ao controle de saldos que possa lhe interessar:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Utilização do parâmetro MV\_TPSALDO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013215531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-TPSALDO?source=search)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)
