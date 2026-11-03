---
content_hash: 64d215293da8c80c056f5a4b35a21280771ed69cef95c2a818f644981e7b95eb
fetched_at: '2026-06-29T00:12:08.236382+00:00'
page_id: '929938795'
product: rm
source: tdn-rm
title: Apuração de Competência - Vendas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=929938795
version: 31
---

|  | ***Treinamento clique [Aqui](https://www.youtube.com/watch?v=z3eMhoRH1oU&feature=youtu.be)***  ***Webinar clique [Aqui](https://youtu.be/7gRh7NobS8M)*** |
| --- | --- |

---

## 🎯 **Objetivo do Módulo de Apuração de Competência**

O módulo de **Apuração de Competência** foi desenvolvido com o objetivo de consolidar, de forma estruturada e imutável, todas as informações financeiras de vendas, parcelas, baixas e distratos dentro de uma **competência contábil e por coligada**.

Esse processo cria uma **fotografia fiel do cenário financeiro em um determinado período**, garantindo que os dados reflitam a realidade operacional do fechamento daquele mês, sem o risco de alterações retroativas.

É similar a ficha financeira em questão de valores, mas os dados são salvos em tabelas para facilitar a criação de relatórios e cubos por parte do cliente.

---

### 🚀 **Principais benefícios e facilidades geradas:**

* **Base confiável para relatórios financeiros e contábeis**, eliminando inconsistências causadas por alterações posteriores;
* **Maior performance e organização** na extração de dados, com tabelas materializadas por ano e separação de histórico;
* **Controle total sobre o que está apurado e o que ainda está pendente**, com rastreabilidade por coligada e competência;
* **Facilidade na criação de cubos analíticos e dashboards**, com dados já tratados e estruturados, baixe o cubo ;
* **Padronização do processo de fechamento**, alinhando operações entre áreas como backoffice, financeiro e contabilidade;
* **Segurança nas auditorias**, com dados congelados após o fechamento da competência.

---

Esse módulo é um pilar importante para melhorar a **governança financeira**, dar suporte à **tomada de decisão baseada em dados consolidados** e atender às **exigências de compliance e controle interno**.

---

### **Apuração de Competência (Mensal)**

O objetivo deste processo é realizar **apuração mensal**, que será executada automaticamente na **virada de competência**, com base no **valor líquido das parcelas no último dia do mês**. Esse processo tem como finalidade consolidar os dados financeiros relativos à competência em questão, garantindo **integridade, rastreabilidade e consistência** das informações.

Os dados apurados serão armazenados em **tabelas do sistema RM**, seguindo o padrão da **ficha financeira**, contemplando os seguintes elementos:

* Dados da venda;
* Regra de negócio aplicada;
* Parcelas envolvidas;
* Lançamentos financeiros e suas respectivas baixas.

Com essas informações devidamente salvas na base, o cliente poderá utilizá-las para a criação de **cubos analíticos, dashboards, relatórios financeiros e contábeis**, promovendo **maior visibilidade, controle gerencial e apoio à tomada de decisão**.

---

### **Escopo e Regras de Fechamento**

A **apuração e o fechamento são realizados por coligada e competência**, possibilitando o controle individualizado por unidade empresarial e por período. Apenas as competências efetivamente encerradas por esse processo serão consideradas **fechadas**, passando a estar sujeitas às seguintes **restrições operacionais**:

* **Realização de baixa**;
* **Cancelamento de baixa**;
* **Geração de aditivos contratuais**;
* **Distrato de vendas**.

Essas restrições garantem a **imutabilidade dos dados consolidados**, evitando alterações retroativas que possam comprometer a integridade financeira e contábil.

Além disso, será implementado um **mecanismo de bloqueio no TCGI**, com base na competência apurada, impedindo qualquer movimentação indevida em períodos já encerrados.

---

### **Despesas de Reembolso**

Despesas de reembolso ocorrem quando a empresa paga por um custo de responsabilidade do cliente e depois o cobra em parcela de reembolso. Agora, é possível incluir essas parcelas no plano de financiamento da venda para que sejam exibidas no contrato, na ficha financeira, no Informe de Rendimentos, no módulo de cobrança e na apuração de competência.

**Configuração:**  
Acesse **Parâmetros Gerais > Integração Financeira > Financeiro** e selecione o componente principal que representa a despesa. A partir dessa configuração, qualquer nova geração incluirá ou excluirá automaticamente as despesas de reembolso.

**Para incluir dados legados nas vendas:**

1. Acesse **Visão de Venda > Processo > Atualizar Despesas**.
2. O sistema buscará todas as despesas de todas as coligadas e as associará ao contrato de venda.

Com isso, todos os módulos mencionados passarão a visualizar as parcelas de despesas. Caso não queira exibi-las nos relatórios, basta aplicar um filtro com os componentes desejados.

---

### **Operação Ideal**

Para garantir a eficiência e a confiabilidade do processo, recomenda-se a seguinte rotina operacional:

**1. Cronograma de Apuração e Fechamento:**  
A apuração deve ser iniciada no **último dia útil do mês**, após a conciliação bancária do mês. Uma vez finalizada a consolidação de todos os dados da competência, esta deve ser **fechada imediatamente** no sistema. Depois reabrir a **competência parcialmente**, sem informar a venda, para que no primeiro dia útil do mês subsequente, continue fazendo a importação do retorno bancário, sendo que o sistema abrirá e fechar a competência dessa venda importada de forma **automática.** Finalizado o fechamento, **fecha apuração da competência** por completo.

**2. Operação Contínua com Validação Paralela:**  
O fechamento da competência anterior libera automaticamente a operação do mês corrente. Enquanto isso, as áreas financeira e contábil realizam a validação final dos valores apurados, sem interromper as atividades operacionais do período atual.

**3. Gestão de Ajustes e Correções:**  
Caso seja identificado algum erro em uma venda específica após o fechamento, o sistema oferece flexibilidade para correção:

* **Ação Recomendada:** Reabertura individual da venda ou sem informá-la, mantendo o restante da competência protegido. Essa abordagem assegura que apenas o controlador, mediante permissão, possa realizar o ajuste necessário, preservando a integridade dos demais dados. Caso seja feito baixas dessa competência que fechou parcialmente, o sistema reabre a venda, permite a baixa e depois faz a apuração dessa venda automaticamente. Ao termino da validação, o usuário deverá fechar por completo a apuração.
* **Fluxo de Correção:**

  1. Caso existam operações vinculadas a essa venda na competência seguinte, estas devem ser **desfeitas temporariamente**.
  2. A venda é reaberta, o ajuste é realizado e sua apuração é refeita ("nova fotografia").
  3. A competência da venda é fechada novamente.
  4. As operações na competência subsequente podem então ser **reconstituídas** com base nos dados corrigidos.

Este fluxo garante a precisão das "fotografias" financeiras de cada mês, assegurando a rastreabilidade e a consistência das informações para relatórios e análises.

---

### **Materialização e Estrutura das Tabelas**

As tabelas de apuração são **materializadas por ano de execução**, ou seja, a cada exercício é criado um novo conjunto de tabelas, que armazena exclusivamente os dados apurados naquele ano. Serão consideradas:

* Vendas **efetivadas** no mês da apuração;
* Vendas **quitadas** no mês da apuração;
* Vendas **distratadas ou finalizadas** no mês da apuração.

### Tabelas de Apuração – Ano Corrente (ex.: 2026)

| Tabela | Descrição |
| --- | --- |
| `XCOMP` | Dados de coligada e competência. Status: 1 - Aberto / 2 - Fechado |
| `XCOMPVENDA2026` | Informações resumidas da venda |
| `XCOMPVENDAREGRA2026` | Regras comerciais aplicadas à venda |
| `XCOMPVENDAPARCELA2026` | Valores da parcela (líquido, presente, saldos, CM, juros, descontos, etc.) |
| `XCOMPFLAN2026` | Lançamentos financeiros apurados |
| `XCOMPFLANINTEGRACAO2026` | Valores de integração dos lançamentos financeiros |
| `XCOMPFLANBAIXA2026` | Dados de baixa dos lançamentos |
| `XCOMPFLANBAIXAINTEGRACAO2026` | Integrações relacionadas à baixa |

---

### **Tabelas de apuração histórica**

As vendas que foram **quitadas ou distratadas em períodos anteriores** serão apuradas uma única vez, na primeira execução do processo. Os dados históricos serão armazenados nas seguintes tabelas:

### Tabelas de Apuração – Histórico

| Tabela | Descrição |
| --- | --- |
| `XCOMP` | Dados de coligada e competência. Status: 1 - Aberto / 2 - Fechado |
| `XCOMPVENDAHST` | Informações resumidas da venda |
| `XCOMPVENDAREGRAHST` | Regras comerciais aplicadas à venda |
| `XCOMPVENDAPARCELAHST` | Valores da parcela (líquido, presente, saldos, CM, juros, descontos, etc.) |
| `XCOMPFLANHST` | Lançamentos financeiros apurados |
| `XCOMPFLANINTEGRACAOHST` | Valores de integração dos lançamentos financeiros |
| `XCOMPFLANBAIXAHST` | Dados de baixa dos lançamentos |
| `XCOMPFLANBAIXAINTEGRACAOHST` | Integrações relacionadas à baixa |

---

### **Benefícios do Modelo**

Esse modelo de apuração e fechamento por **ano, coligada e competência** proporciona:

* **Segurança e integridade** das informações apuradas;
* **Desempenho otimizado** para consultas e relatórios;
* **Maior controle sobre a gestão financeira e contábil**;
* **Rastreabilidade total** das operações, desde a origem até o status final.

O processo está alinhado com as melhores práticas de **controle financeiro**, **auditoria de dados** e **conformidade contábil**, e poderá futuramente ser integrado ao fluxo de **fechamento financeiro do time de backoffice**, promovendo uma gestão padronizada e confiável.

---

### **Apuração de Competência (Mês Caixa)**

Existe um parâmetro geral em Integração Financeira => Bloqueio de lançamento financeiro = > Realizar a apuração mês caixa

O objetivo deste parâmetro é realizar **apuração mensal**, que será executada automaticamente na **virada de competência**, com base no **valor líquido das parcelas do último dia do mês e o reajuste do mês subsequente, mês caixa**.

Ex.: Estou no mês de Maio/2026 e vou fechar a competência do mês Abril/2026, mas faço o reajuste de maio na competência de abril, então você marcar essa opção. pois os valores financeiros serão da competência de abril que está fechando e o valor do reajuste será de maio, mês caixa da competência.

Valores financeiros serão da data 30/04/2026 e o reajuste será da data de 31/05/2026

AtençãoExiste um outro parâmetro para salvar os detalhes das tabelas do financeiro que deve ser desmarcado caso você deseje ter valores quebrados na flanintegração e flanintegraçãobaixa na apuração, se não serão sumarizados na xcompvendaparcela2026

---
