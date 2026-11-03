---
article_id: 115013042127
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: cd2262120027837dbc6cb92e071628b66ea2a871f1122ba77cbd67da4c12703f
fetched_at: '2026-06-28T22:38:28.807639+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Comissões de Vendas no Faturamento
type: support-article
updated_at: '2026-03-10T11:55:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013042127-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Comiss%C3%B5es-de-Vendas-no-Faturamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38929488737943) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**

Como configurar comissões de vendas no Protheus e como funciona a sua geração?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

|  |
| --- |
| Assista ao vídeo explicativo para entender o fluxo de cadastro e comissão do processo abaixo:  [How To | MP - SIGAFAT - Configuração de vendedor para comissões](https://www.youtube.com/watch?v=hxKM-ESpAKI) |

**Solução**

Segue o processo de configuração e geração da Comissão de forma simplificada para que se possa avaliar o que melhor atende no processo e possibilite gerenciar de forma adequada a comissão do vendedor via módulo de Faturamento:  
  
1. **Cadastro de vendedor** - Defini o percentual de comissão,  se a comissão é gerada na emissão da nota ou na baixa do título, impostos que poderão ou não estar contidos nesta comissão, e o tipo de recebimento( contas a pagar, folha de pagamento ou sem interface);

2. **Faturamento de Pedido** - Gera-se um pedido de venda para o vendedor em questão, libera o pedido e o fatura. Dependendo da configuração de como a comissão será emitida, o sistema poderá já gerar os dados de comissão a partir da geração da nota.

3. **Baixa de titulo a Receber-** Caso a opção tenha sido configurado para gerar comissão na baixa do título, será necessário baixar o título a receber gerado através da nota de saída, para que o percentual de comissão seja gerado.

4. Conferência da comissão em '**Manutenção de Comissão**'(MATA490).

5. Execução da rotina **'Atualiza Pagto de Comissão'**. Neste passo, a comissão poderá ser gerada para o contas a pagar, poderá integrar com a folha de pagamento ou não tratar com a integração do Protheus, tudo dependerá da configuração efetuada no cadastro vendedor.

6. Relatório **Relação de Comissão (MATR540)**. - Este relatório tem como base os registros da manutenção de comissão (**SE3**), a partir do momento que os dados já constarem nesta rotina, já poderão ser visualizados no relatório.  
  
**Saiba mais:**

* [**Processo para configuração e geração da comissão dos vendedores**](https://tdn.totvs.com/x/efIKDg)

* [**Rotina de processamento dos Pagamentos de Comissões**](https://tdn.totvs.com/x/eisMEQ)
