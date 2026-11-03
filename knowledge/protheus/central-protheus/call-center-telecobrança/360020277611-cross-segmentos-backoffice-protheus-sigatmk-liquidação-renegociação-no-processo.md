---
article_id: 360020277611
category: Call Center - Telecobrança
content_hash: 82dab8f1e20aa5a94f5eeca77c0016fad6bd8129b16bb620a678ee092180648c
fetched_at: '2026-06-28T22:41:28.598693+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Liquidação / Renegociação
  no processo de Telecobrança
type: support-article
updated_at: '2026-03-20T13:41:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020277611-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Liquida%C3%A7%C3%A3o-Renegocia%C3%A7%C3%A3o-no-processo-de-Telecobran%C3%A7a
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35496304134935)** **Tempo aproximado para leitura:****00:03:00 min**

**Dúvida**  
Como efetuar a Liquidação / Renegociação no Processo de Tele cobranças do Call Center - SIGATMK?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGATMK - Todas as versões

**Solução**  
Configuração necessária para a liquidação / renegociação ocorrer:

* Definir a natureza que será utilizada na liquidação do título através do parâmetro **MV\_TMKNTCB;**
* Definir o prefixo utilizado nos títulos gerados pela liquidação através do parâmetro **MV\_TMKPRTR**. Caso não seja definido, o padrão será REN de renegociação;
* Definir o tipo utilizado nos títulos gerados pela liquidação através do parâmetro **MV\_TMKTPTR**. Caso não seja definido, o padrão será BOL;

Para efetuar a cobrança dos títulos em atraso:

1. Realizar o Processamento da Seleção de Título (TMKA180);
2. Em Call Center inclua um novo atendimento;
3. Selecione o cliente para efetuar a cobrança;
4. Selecione o contato relacionado ao cliente;
5. Informe a condição de pagamento para a liquidação no campo Condição (ACF\_CONDPG). Esta condição deve estar cadastrada na Regra de negociação do operador.
6. Altere o status do título para negociado. O título pode ser alterado com relação a decréscimo e desconto de juros, que refletirá nos valores dos títulos gerados na liquidação.
7. Confirme a cobrança.
8. Visualize a cobrança para verificar se o status dos títulos negociados mudou para Pago. Em caso de alteração da cobrança, o operador não poderá mudar o status para refazer a negociação, ou seja, deve ser realizado o Cancelamento da Liquidação.
9. Para verificar se a liquidação foi realizada com sucesso e visualizar o relatório, acesse o módulo Financeiro, clique em Relatórios/Contas Receber/ Liquidação.
10. Verifique se o título negociado foi baixado e se os títulos foram gerados de acordo com a condição de pagamento informada no telecobrança.

**Saiba mais**:

* [Liquidação/Renegociação no Telecobranças (SIGATMK)](https://tdn.totvs.com/x/cfQJE)
* [Cross Segmentos - Backoffice Protheus - SIGATMK - Data de Vencimento x Data de Vencimento Real para o Cálculo de Juros do Telecobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018760431-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Data-de-Vencimento-x-Data-de-Vencimento-Real-para-o-C%C3%A1lculo-de-Juros-do-Telecobran%C3%A7a)
* [Cross Segmentos - Backoffice Protheus - SIGATMK - Processamento da Seleção de Título (TMKA180)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404768843031-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Processamento-da-Sele%C3%A7%C3%A3o-de-T%C3%ADtulo-TMKA180)
