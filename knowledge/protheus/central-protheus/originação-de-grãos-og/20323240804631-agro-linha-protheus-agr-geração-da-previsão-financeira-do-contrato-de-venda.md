---
article_id: 20323240804631
category: Originação de Grãos (OG)
content_hash: 56ea2f3ca2a2bc5817bed8423b272a0f4fe727753175a9876930ca0531cbe077
fetched_at: '2026-06-28T22:45:39.518268+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Geração da Previsão Financeira do contrato de
  venda
type: support-article
updated_at: '2025-06-18T20:27:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20323240804631-Agro-Linha-Protheus-AGR-Gera%C3%A7%C3%A3o-da-Previs%C3%A3o-Financeira-do-contrato-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20323240770711) Tempo aproximado para leitura: **00:02:45 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para  gerar a previsão financeira é apresentada a ocorrência **Geração da Previsão Financeira do contrato de venda**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Esse incidente ocorre, pois é preciso realizar o processo para gerar a previsão financeira no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, ao editar o contrato de venda e ser acionado o botão **confirmar** serão geradas as previsões financeiras somente no módulo de **Comercialização** - **SIGAAGR**  
Esta informação pode ser verificada ao visualizar o registro e ir na pasta **Dados das Previsão Financeira**.  
Ao selecionar a ação relacionada e **Confirmar do Contrato de venda** será gerada a previsão financeira no módulo **Financeiro - SIGAFIN**.  
  
Serão considerados para a geração da previsão financeira no **financeiro** os dados do contrato de venda, tais como:

* Cadastro de **Condições de pagamento**
* Cada **Previsão de entrega** pode ter 1 ou mais **Regras fiscais**;
* Para o algodão, cada regra fiscal poderá ter *take-up*vinculado;
* Para gerar as previsões financeiras, podemos ter a relação de:**(n)Previsão de entregas X (n)Regra Fiscal X (n)Condição de Pagamento**

Para nova comercialização na ação relacionada **Gerar Previsão Financeira**, existente no contrato de venda, terá a funcionalidade de gerar ou atualizar as provisões financeiras no módulo de **Comercialização - SIGAAGR** e **Financeiro - SIGAFIN**.  
A finalidade de ter está opção é para caso tenha alguma alteração dos índices ou cotações de moeda, e o contrato fizer uso deles, **realizar a atualização da previsão financeira**.  
  
Por exemplo ao gerar uma previsão financeira para um contrato com moeda estrangeira, eu considero uma cotação prevista, pois, geralmente é uma **previsão para o futuro**, porém, ao ter a cotação firme, é necessário que esse valor seja recalculado para evitar divergências com o pagamento efetuado pelo cliente e também evitar erros em fluxo de caixa.  
  
Esta mesma funcionalidade de atualizar as previsões financeiras dos contratos, pode ser executada em batch periodicamente utilizando a tarefa **OGX065 - Atualizar o valor da previsão financeira**.  
  
Para isto é necessário:

1. Configurar o *schedule* do **Protheus** [Schedule Protheus](http://tdn.totvs.com/display/framework/Schedule+Protheus)
2. Cadastrar a tarefa do **OGX065** para execução via *schedule*.
3. Definir uma quantidade de dias que será considerada antes do vencimento.

Processos que atualizam as previsões financeiras do contrato:

* **Contrato venda > Ação relacionada > Gerar Previsão Financeira**
* **Atualização Batch** **OGX065**
* **Fixação de preços**.
* **Alteração de fixação**.
* **Alteração de Contrato: adição ou supressão**
* **Geração de NF de complemento**.
* **Confirmação do Romaneio**.
* **Exclusão Nota Fiscal e reabertura do romaneio**.
* **Take-up**

![log111.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20323240774679)
