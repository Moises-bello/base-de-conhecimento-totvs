---
article_id: 360047857193
category: SIGAEST - CUSTOS
content_hash: 79ea8eff3c4451f65231367b8b5a1a320b84e0ec5a48afcec0f2156f4d6dea13
fetched_at: '2026-06-28T22:39:00.890893+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Dicas de Performance
  custo medio e acompanha custos
type: support-article
updated_at: '2026-04-15T18:39:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047857193-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Dicas-de-Performance-custo-medio-e-acompanha-custos
---

O artigo detalha melhorias para otimizar o Recálculo do Custo Médio (MATA330) no TOTVS Protheus, destacando a importância da manutenção do banco de dados, uso de AppServer dedicado, baixa latência de rede e atualização do ambiente. Também orienta a coleta de logs e dados para análise de performance em casos de lentidão persistente.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28807804575511)** Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**  
Quais as possibilidades de melhoria na performance do custo médio de forma padrão e como isso impacta a rotina de Acompanha Custos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para otimizar o processamento do **Recálculo do Custo Médio (MATA330)** e, consequentemente, refletir em maior agilidade na rotina de **Acompanha Custos**, a TOTVS disponibiliza diversas configurações e parâmetros de performance. Abaixo, detalhamos as principais implementações:

De forma a ser obrigatorio, sempre sera sugerido a validação do ambiente, se o mesmo se encontra devidamente atualizado com as ultimas versões, avaliações de performance, requer o ambiente 100% atualizado, para necessidade de coleta de logs de performance, sob validação do time de produto, então o primeiro passo é, validar as atualizações mais recentes.

#### **Documentação central para questão de performance.**

##### [**PEST06008 - MATA330 - Como melhorar a performance da rotina de Recalculo do Custo Médio ?**](https://tdn.totvs.com/pages/viewpage.action?pageId=336404235)

### **Opções ideiais para a validação do seu time de T.I**

#### **Manutenção e Otimização do Banco de Dados (SGBD)**

A performance de qualquer rotina que use procedure, depende diretamente da saúde do banco de dados, pois a rotina realiza milhares de leituras e gravações.

* **Ação:** É mandatório que o DBA (Administrador de Banco de Dados) realize periodicamente a **Reconstrução de Índices (Rebuild)** e a **Atualização de Estatísticas** das principais tabelas envolvidas no processo, documentadas no link [**PEST06008 - MATA330 - Como melhorar a performance da rotina de Recalculo do Custo Médio ?**](https://tdn.totvs.com/pages/viewpage.action?pageId=336404235)
* **Impacto:** Tabelas fragmentadas ou com estatísticas desatualizadas fazem o banco de dados errar o plano de execução, gerando lentidão.
* É necessário verificar o arquivo **DBAPI.DLL** se estão com a mesma data de modificação nos diretórios **AppServer** e **DBAcess**.

#### **Isolamento de Ambiente (AppServer Dedicado)**

* **Recomendação:** Para bases de dados volumosas, crie um serviço (AppServer) dedicado e exclusivo no servidor (ou em um servidor de processamento separado) apenas para rodar o MATA330 em *Job* ou via *Smartclient* isolado.
* **Ganho:** Evita a concorrência de processamento de CPU e memória com os demais usuários conectados utilizando o ERP durante o fechamento, garantindo que os recursos sejam focados no processamento.

#### **Latência de Rede**

* **Latência:** Certifique-se de que a latência (ping) entre o servidor de Aplicação (AppServer), o DBAccess e o servidor de Banco de Dados seja a menor possível (idealmente no mesmo *datacenter* ou mesma máquina física/virtual).

### **Fez todos os procedimentos, mas entendo que a lentidão não é o ambiente**

* [Colete o Logprofiler e Dbtrace durante o processamento.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019902592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-habilitar-e-gerar-o-LogProfiler)
* [Colete o ID da central](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico) (Se ambiente desatualizado, atualize. Caso desatualizado, a analise não seguira).
* [Colete o TRACE e validacoes do seu DBA](https://tdn.totvs.com/pages/viewpage.action?pageId=336404235#:~:text=Caso%20mesmo%20utilizando%20todos%20os%20procedimentos%20descritos%20nesta%20FAQ%20n%C3%A3o%20tenha%20melhoras%20significativas%20no%20processamento%20na%20rotina%20de%20custo%20m%C3%A9dio%2C%20segue%20as%20a%C3%A7%C3%B5es%20para%20avalia%C3%A7%C3%A3o%3A)
* [Colete o resultado do MALLIOC do servidor de APLICAÇÃO](https://tdn.totvs.com/x/PRdXHw)
* Colete o arquivo **CV8** se esta usando a rotina MATA330 ou **D3X** se usando a rotina Acompanha Custos, após finalizar o processamento e salve em formato **SQLITE**
* **Colete junto com o seu DBA** o resultado da contagem da quantidade de registros que existem no processamento da filial, em relação ao periodo em aberto, das tabelas **SD1/SD2/SD3. (Sem deletados)**
* **Colete junto com o seu DBA** o resultado da contagem da quantidade de registros que existem na filial em processamento das tabelas **SB2/SB9. (Sem deletados)**

A validação de performance, é algo moroso e delicado, mas esses dados são necessarios para a averiguação pontual dos logs, sem esses dados, não há viabilidade de analise de performance.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
