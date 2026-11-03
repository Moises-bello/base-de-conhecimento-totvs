---
article_id: 37567714181271
category: Financeiro - Cadastros
content_hash: 7109c30264ae4a88b66275b427b90d05515bcf18b36eb6bd11c7e1e38e6c4f5c
fetched_at: '2026-06-28T22:37:53.110976+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA490 - Como criar motivo de
  baixa
type: support-article
updated_at: '2026-01-09T19:13:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37567714181271-Cross-Segmentos-Backoffice-Linha-Protheus-FINA490-Como-criar-motivo-de-baixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37567714157975) Tempo aproximado para leitura: **00:15min**  
  
**Dúvida**  
Como criar um novo motivo de baixa?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Para realizar o cadastro dos Motivos de Baixa, acesse o módulo 06 – SIGAFIN e execute o procedimento descrito a seguir:

1. No menu principal, selecione Miscelânea > Arquivos > Tabela de Motivos de Baixa ou pesquisar por FINA490.

2. Clique na opção Incluir para iniciar um novo cadastro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37567714160663)

3. Preencha as informações do Motivo de Baixa de acordo com a necessidade do processo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37567714162071)

* **Sequência:**identificador sequencial do motivo de baixa.
* **Sigla:** código abreviado utilizado para identificar o motivo de baixa no sistema.
* **Descrição**  
  Descrição detalhada do motivo de baixa, facilitando sua identificação e entendimento.
* **Carteira: d**efine o tipo de carteira ao qual o motivo de baixa se aplica:

  + **P** – Pagar
  + **R** – Receber
  + **A** – Ambas (Pagar e Receber)
* **Movimentação Bancária:** Indica se o motivo de baixa deverá gerar movimentação bancária:

  + **S** – Sim
  + **N** – Não
* **Comissão:** define se o motivo de baixa deverá gerar comissão:

  + **S** – Sim
  + **N** – Não
* **Cheque:** Indica se o motivo de baixa deverá gerar emissão ou controle de cheque:

  + **S** – Sim
  + **N** – Não
* **Espécie:** define-se se o motivo de baixa estará relacionado a pagamento ou recebimento em espécie:

  + **S** – Sim
  + **N** – Não

4. Após a conferência dos dados, confirme a operação para concluir o cadastro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37567714163095)

Se a rotina estiver aberta no momento do cadastro, será necessário **fechá-la e reabri-la**, para que o novo **Motivo de Baixa** seja corretamente carregado e disponibilizado para uso.

**Importante**

As alterações realizadas nos **Motivos de Baixa padrão do sistema** devem ser efetuadas com **extrema cautela**, uma vez que esses registros são utilizados em diversas **operações internas** do sistema. Alterações indevidas podem comprometer a **rastreabilidade das transações**, além de gerar impactos negativos em processos de **conciliação**, **contabilização**, **cancelamento** e **reprocessamento de dados históricos**.

Considere, por exemplo, uma movimentação associada ao motivo **DEB – Débito em Conta Corrente**, que em determinado momento está configurado para a carteira **Contas a Pagar**. Caso seja realizada uma alteração da carteira de **Pagar** para **Receber**, as operações já registradas poderão deixar de ser reconhecidas pelo sistema.

Um cenário comum ocorre quando uma **baixa** é realizada utilizando um determinado motivo e, posteriormente, esse motivo sofre alterações em sua **carteira** ou **sigla**. Caso seja necessário efetuar o **cancelamento dessa baixa**, o sistema poderá não localizar o movimento original, uma vez que o **motivo de baixa** faz parte dos critérios utilizados para a identificação da transação.

Diante disso, os riscos de irregularidades decorrentes de alterações nos Motivos de Baixa podem ser classificados da seguinte forma:

* **Alto risco**:  
  Alterações de **Carteira**, **Sigla** e **exclusão** de motivos de baixa.
* **Risco médio**:  
  Alterações nas propriedades **Movimentação Bancária**, **Comissão**, **Cheque** e **Espécie**.
* **Baixo ou muito baixo risco**:  
  Alterações na **Descrição** do motivo de baixa.

Recomenda-se **sempre criar novos registros** para atender a novas necessidades operacionais, mantendo **inalterados os motivos de baixa padrão do sistema**.

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Motivo de baixa corrompido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018384491-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Motivo-de-baixa-corrompido?source=search)
