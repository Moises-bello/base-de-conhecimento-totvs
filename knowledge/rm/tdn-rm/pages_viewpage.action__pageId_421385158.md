---
content_hash: 6f64ff0901833955d91104a5a866b926624bf5a6dbdae2c1434e45e86de7d9cc
fetched_at: '2026-06-29T00:09:14.220547+00:00'
page_id: '421385158'
product: rm
source: tdn-rm
title: Liberar Período 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385158
version: 59
---

A liberação de período de um contrato é feita logo após os lançamentos da medição. Ao solicitar a liberação de uma medição aparecerá uma janela com os seguintes campos:

paiRM SolumMenuRMSolumMedição

Geração de Período

**Período**: É possível visualizar o período a ser liberado.

**Data Inicio e Data Fim** serão preenchidos de acordo com o período selecionado.

**Data da Liberação:** Informe a data da liberação da medição.

**% de Reajuste:** Este campo virá preenchido com o valor percentual do reajuste do período anterior. Um reajuste na medição não altera o valor do Contrato.

**Valor da Medição:****Sem Reajuste:**  valor da medição sem reajuste. **Com Reajuste:**  valor da medição com reajuste.

**Total Medição**: valor da medição adicionando o reajuste e subtraindo a retenção.

**Vlr. ret./ded./adt.****:** Este campo virá preenchido com o valor de retenção na liberação do período.

**Vr**. **Ret. item:** valor da retenção informada na medição do período.

**Vr**.**Ret. total:** valor da soma da retenção informada na medição do período e da retenção informada na liberação do período.

**Reajustes:**

Caso o período tenha algum reajuste aplicado é exibido moeda , coeficiente, cotação e a data da cotação.

**Ultima medição:**Um ponto importante do processo de liberação é a flag **Última Medição do Contrato**, localizada na parte inferior da tela de liberação.

* **Flag "Sim" (Em Vermelho):** Indica que, após a conclusão deste processo, o sistema entenderá que o objeto do contrato foi totalmente cumprido.
* **Impacto no Status do contrato:** Uma vez liberado um período marcado como "Última Medição", o contrato assume automaticamente o status de **Concluído**.

### Impedimentos para Liberação/Integração

O sistema impede a conclusão do processo se a flag de "Última Medição" estiver marcada, mas houver pendências financeiras, tais como:

* ❌ **Saldo de adiantamento pendente:** Existem adiantamentos que ainda não foram totalmente amortizados ou descontados.
* ❌ **Deduções pendentes:** Valores de faturamento direto que ainda não foram aplicados nas medições.

### Bloqueio de Movimentação em Contrato Concluído

Após a liberação da última medição, o contrato é concluído. Caso o usuário tente realizar uma nova liberação ou medição para um contrato com status **Concluído**, o sistema exibirá o seguinte erro:

## Ações Automáticas Pós-Encerramento

Se não houver restrições financeiras e a última medição for liberada, o sistema executa:

### Alteração de Status

O contrato passa para **Concluído**.

* **Configuração de Saldo:** Se configurado para utilizar saldo de contrato, o status deve permitir apenas a liberação de retenções remanescentes.

### Devolução de Saldo ao Planejamento

O sistema realiza o cálculo de sobra de orçamento:

$$Saldo = Valor Total do Contrato - Valor Total Medido$$

Este saldo é **devolvido automaticamente** para a tarefa correspondente no planejamento do projeto, permitindo que esse orçamento seja reaproveitado em outras frentes de serviço.

Detalhamento Dedução, Retenção e Adiantamento

**Deduções:** Utilizado para informar os tipos de deduções do período.

**Retenções:** Utilizado para informar os tipos de retenções do período.

**Retenções**: Utilizado para informar os tipos de adiantamento do período.

Campos Complementares

Nesta Aba, preenchemos os campos complementares cadastrados no Menu Cadastros/Campos Complementares/Detalhamento Medição.

Observações

Nesta Pasta, podemos digitar alguma observação sobre a liberação em questão.

Rateio de Estado e Municipio

Nesta aba é possível informar rateio de estado e município e seu valor.

Integração FinanceiroMenuIntegracaoFinanceiroIdentificação

**Cliente/Fornecedor:** permite informar o Cliente ou Fornecedor em questão.  
**Tipo Contábil:** permite informar qual o tipo contábil do Lançamento que será gerado no Financeiro.    
**Tipo Documento:** permite informar qual o tipo de documento do Lançamento que será gerado no Financeiro.  
**Conta Caixa:** permite informar qual a conta caixa do Lançamento que será gerado no Financeiro.  
**Tipo de Lançamento:** permite informar o tipo do Lançamento que será gerado no Financeiro.

Campos Opcionais de Valores

Sendo eles:

Bolsa, multa, perda, IRRF entre outros.

Datas Opcionais

Datas opcionais em relação ao período liberado.

Tabelas Opcionais

Tabelas opcionais , considerando seção , portador, centro de despesa, natureza do gasto e contratos.

Campos Adicionais Alfa

Campos adicionais considerando código da receita, RPA, DARF entre outros.

Informações sobre liberação de Período

Caso o projeto esteja com a parametrização [Integração ECM –WF](http://tdn.totvs.com/pages/viewpage.action?pageId=421385430) ativa, no momento da Liberação da Medição (Período) para Suprimentos/Faturamento, Financeiro ou TOP, o sistema dispara um Workflow para o ECM solicitando a criação de um atendimento.   
Para que o período seja liberado é preciso que o atendimento seja concluído como Aprovado. Caso o atendimento seja concluído como Reprovado, identifique quais mudanças devem ser efetuadas no projeto e acione novamente o processo  'Liberar Período' para que um novo atendimento seja aberto para aprovação.   
Não é possível alterar a medição do item até que o atendimento seja concluído.

Liberação de período ocorre de duas formas podendo ser para Totvs Obras e Projetos e Integração com o Financeiro (Gerando lançamentos Financeiros).  
   
**Movimentos gerados na liberação do período:**

* Quando o movimento é gerado a partir de uma liberação de período de um contrato com dedução e discriminação de valor de dedução e retenção o somatório das deduções é enviado para o campo "Desconto" do item de movimento no módulo Suprimentos/Faturamento.

* Quando o movimento é gerado e possui dedução no contrato discriminando o valor de dedução e retenção identificado no módulo Suprimentos/Faturamento, o campo "Desconto" do item de movimento terá sua edição bloqueada.  
     
     
  Para mais informações visualizar os parâmetros do contrato em: [Parâmetros do contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=421385359)

**Minhas Inspeções:**

* Se o parâmetro de projeto "Bloquear liberação de período se não existir Inspeção em conformidade" estiver marcado, um determinado período somente poderá ser liberado se existir alguma inspeção finalizada com o status de conformidade igual a "Conforme":
