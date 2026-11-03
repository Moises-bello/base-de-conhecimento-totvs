---
article_id: 37527006602775
category: Financeiro - Baixas a Receber
content_hash: f30e8a354c9ca8ce5b6d8c394c27aacc744c0dd932aaef51bc1300ecd6cb6907
fetched_at: '2026-06-28T22:37:43.701933+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - E1_BAIXA e E2_BAIXA
  não atualizam com a última data
type: support-article
updated_at: '2026-01-08T12:36:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37527006602775-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-E1-BAIXA-e-E2-BAIXA-n%C3%A3o-atualizam-com-a-%C3%BAltima-data
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37527006593175) **Tempo aproximado para leitura: 00:08 min**  
  
**Dúvida**  
Campo E1\_BAIXA e E2\_BAIXA não atualizam a data quando antecedem a database do sistema.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Os campos responsáveis pelo controle da data de baixa nos módulos de Contas a Receber e Contas a Pagar (E1\_BAIXA e E2\_BAIXA) são atualizados sempre que uma baixa é efetivada, seja por meio de baixa manual, baixa automática, compensação, entre outros processos, registrando sempre a data da última operação realizada.

No caso de compensações parciais, o campo permanecerá preenchido com a data da última compensação efetuada, ainda que haja estorno de alguma das compensações. O campo somente será limpo quando todas as baixas e/ou compensações do título forem integralmente estornadas.

## Exemplo de Utilização

### Exemplo 1 – Múltiplas compensações realizadas em datas distintas

**Movimentos de compensação:**

* 1ª compensação realizada em **05/12/2024**
* 2ª compensação realizada em **16/12/2024**
* 3ª compensação realizada em **30/12/2024**

**Resultado:**  
O campo de data de baixa será gravado com o valor **30/12/2024**, correspondente à data da última compensação efetuada.

**Movimentos de estorno:**

* Estorno da 3ª compensação realizado em **30/12/2024**

**Resultado:**  
O campo de data de baixa permanecerá gravado com o valor **30/12/2024**, pois ainda existem compensações ativas associadas ao título.

* Estorno de todas as demais compensações.

**Resultado:**  
O campo de data de baixa será atualizado, permanecendo **sem conteúdo (em branco)**, uma vez que todas as baixas e compensações do título foram integralmente estornadas.

### Exemplo 2 – Compensação parcial com baixas em datas retroativas

**Movimento de compensação:**

* Compensação realizada em **30/12/2024**

**Movimento de baixa:**

* Baixa do título realizada posteriormente em **06/01/2025**

**Movimentos de estorno:**

* Estorno da baixa realizada em **06/01/2025**

**Resultado:**  
O campo de data de baixa permanecerá com o valor **06/01/2025**, pois esta corresponde à maior data registrada entre os movimentos de baixa existentes.

**Novo movimento de baixa:**

* Baixa realizada posteriormente com data retroativa em **28/12/2024**

**Resultado:**  
O campo de data de baixa continuará com o valor **06/01/2025**, uma vez que o sistema considera sempre a **maior data de baixa** entre todos os movimentos realizados.

**Importante**  
**Mesmo que um novo movimento de baixa seja registrado com data anterior à última já gravada, o campo de data de baixa não será atualizado retroativamente. A lógica aplicada mantém o registro da data mais recente (maior) dentre todas as baixas e compensações efetuadas.**
