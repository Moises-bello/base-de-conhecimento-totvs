---
article_id: 28600743613847
category: Originação de Grãos (OG)
content_hash: 3053490b3a11bcb66b92b3d267103b8c129c7b05538e6e4b70462fdd8fd24766
fetched_at: '2026-06-28T22:45:37.772599+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Configuração/Parâmetros da Rotina na Geração
  da Previsão Financeira do contrato de venda
type: support-article
updated_at: '2025-06-24T20:23:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28600743613847-Agro-Linha-Protheus-AGR-Configura%C3%A7%C3%A3o-Par%C3%A2metros-da-Rotina-na-Gera%C3%A7%C3%A3o-da-Previs%C3%A3o-Financeira-do-contrato-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28600723547287) Tempo aproximado para leitura: **00:02:00 min****Dúvida**  
Como é realizador uma Configuração/Parâmetros da Rotina na Geração da Previsão Financeira do contrato de venda?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**Principais parâmetros:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo padrão** | **Conteúdo exigido para esta rotina** |
| [MV\_AGRA001](https://tdn.totvs.com/pages/viewpage.action?pageId=497914828) | Utiliza novo conceito de comercialização do UBA. | .F. | .T. |
| [MV\_AGRO002](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326) | Utiliza novo modelo de comercialização. | .F. | .T. |
| [MV\_AGRO040](https://tdn.totvs.com/pages/viewpage.action?pageId=519202897) | Retira a obrigatoriedade do Registro de Negócio | .F. | (opcional) |
| [MV\_AGRPREV](https://tdn.totvs.com/pages/viewpage.action?pageId=353275942) | Permitir incluir contratos de compra e venda sem informar previsão financeira. | .F. | .T. |

Aplicação:  
Ao editar o **contrato de venda**  e ser acionado o **botão confirmar**serão geradas as previsões financeiras somente no modulo de **Comercialização - SIGAAGR**.

Este informação pode ser verificada ao visualizar o registro e ir na pasta **Dados das Previsão Financeira.**  
Ao selecionar a **ação relacionada** e **Confirmar**  do Contrato de venda será gerada a previsão financeira no módulo **Financeiro - SIGAFIN**.  
Serão considerados para a geração da previsão financeira no financeiro os dados do contrato de venda, tais como:

**1.** Cadastro de condições de pagamento

**2.** Cada Previsão de entrega pode ter 1 ou mais Regras fiscais.

**3.** Para o algodão, cada regra fiscal poderá ter *take-up* vinculado.

**4.** Para gerar as previsões financeiras, podemos ter a relação de : **(n)Previsão de entregas X (n)Regra Fiscal X (n)Condição de Pagamento**.

Para nova comercialização na ação relacionada **Gerar Previsão Financeira**, existente no contrato de venda, terá a funcionalidade de **gerar  ou atualizar** as provisões financeiras no módulo de **Comercialização** **- SIGAAGR** e **Financeiro** **- SIGAFIN**.  
A finalidade de ter está opção é para caso tenha alguma alteração dos **índices** ou **cotações** de moeda, e o contrato fizer uso deles, realizar a atualização da previsão financeira.  
Por exemplo ao gerar uma previsão financeira para um contrato com moeda estrangeira, eu considero uma cotação prevista, pois, geralmente é uma previsão para o futuro, porém,  
ao ter a cotação firme, é necessário que esse valor seja recalculado para evitar divergências com o pagamento efetuado pelo cliente e também evitar erros em fluxo de caixa.

Esta mesma funcionalidade de atualizar as previsões financeiras dos contratos, pode ser executada em **batch**periodicamente utilizando a tarefa**OGX065**.  
Para isto é necessário:

* Configurar o schedule do Protheus **http://tdn.totvs.com/display/framework/Schedule+Protheus**.
* Cadastrar a tarefa do **OGX065**para execução via schedule.
* Definir uma quantidade de dias que será considerada antes do vencimento.

Processos que atualizam as previsões financeiras do contrato:

* **Contrato venda > Ação relacionada > Gerar Previsão Financeira**
* **Atualização Batch (OGX065)**
* **Fixação de preços.**
* **Alteração de fixação.**
* **Alteração de Contrato: adição ou supressão**
* **Geração de NF de complemento.**
* **Confirmação do Romaneio.**
* **Exclusão Nota Fiscal e reabertura do romaneio.**
* **Take-up**
