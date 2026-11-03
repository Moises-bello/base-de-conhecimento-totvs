---
content_hash: 0acdbab659da6bc3a28e3905bcbcc8bf52dcc19a24812d5b4ec8f3de66607905
fetched_at: '2026-06-29T00:12:08.243446+00:00'
page_id: '929938867'
product: rm
source: tdn-rm
title: Apuração de Competência - Apurar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=929938867
version: 6
---

## ⚙️ **Processo de Apuração da Competência**

Nesta funcionalidade, você poderá **executar a apuração da competência para uma ou mais coligadas**, juntamente com seus respectivos empreendimentos.

### Regras gerais do processo:

* Para que uma **coligada possa ser fechada**, é necessário que **todos os empreendimentos vinculados a ela estejam apurados**.
* A apuração pode ser feita **em etapas**, e a **tela de Vendas Pendentes** auxiliará na visualização do que ainda falta ser processado antes do fechamento completo da competência.

---

### 📅 **Opções de Apuração por Data**

Você poderá escolher a competência inicial caso seja a primeira vez executada ao realizar o processamento

---

### 🔁 **Reprocessamento de Dados**

Sempre que a apuração for executada **para dados que já foram apurados anteriormente**, o processo irá:

1. **Excluir todos os registros anteriores** relacionados àquela coligada e competência
2. **Reprocessar integralmente os dados**

Esse comportamento pode impactar significativamente o **tempo de execução**, especialmente em coligadas com grande volume de dados já apurados.

Para mitigar esse impacto e tornar o processo mais eficiente, foram criadas **duas opções adicionais de execução**:

1. **Processar apenas vendas pendentes**:  
   Executa a apuração somente para as vendas que **ainda não foram apuradas**, evitando o reprocessamento completo da competência e **melhorando a performance**.
2. **Reprocessar uma venda específica**:  
   Permite recalcular **apenas uma venda pontual**, ideal para casos de ajustes manuais ou correções específicas, sem a necessidade de reexecutar toda a apuração da competência.

Essas opções oferecem **mais controle e flexibilidade** ao usuário, permitindo otimizar o tempo de processamento e reduzir impactos operacionais.

---

Excluir Apuração

 É permitido excluir apuração desde que ela esta em aberto, caso esteja fechada, favor reabrir a competência da coligada, ficando em aberto e exclua-a posteriormente.
