---
content_hash: db3d90bee8c161577690a6b5c6db1e368f4ae70f25372ff41e05a98387e6e34e
fetched_at: '2026-06-29T00:09:36.321853+00:00'
page_id: '425459500'
product: rm
source: tdn-rm
title: Excluir Bolsa Retroativa - Exemplos 1
type: documentation
url: https://tdn.totvs.com/display/LRM/Excluir+Bolsa+Retroativa+-+Exemplos+1
version: 2
---

---

**1 –****Gerar uma única parcela para o pagamento**:

**Exemplos:**− Contrato possui 6 parcelas de 1000,00 cada.  
− A Bolsa X de 10% está aplicada para as 6 parcelas do contrato (parcela inicial = 1 e parcela final = 6).  
− Os lançamentos financeiros das 6 parcelas *já* foram gerados.

**Cenário 1:**− Exclusão ***total*** da bolsa indicando-se parcela inicial = 1 e parcela final = 6  
**Resultado:**− A Bolsa X permanecerá no contrato mas ficará *inativada* (campo 'Bolsa ativa' será desmarcado) com todos os seus campos bloqueados para edição.  
− Será incluída no contrato do aluno a parcela **7** no valor de 600,00 (6 x 100,00 = 600,00) para a cobrança do valor total das bolsas excluídas. O Tipo de parcela, Serviço e Data de vencimento utilizados para esta parcela obedecerão às informações que foram previamente parametrizadas.  
− Se a opção '*Gerar lançamentos de cobrança automaticamente'* definida previamente nos parâmetros do sistema estiver marcada, o lançamento financeiro desta parcela será gerado automaticamente, caso contrário, a parcela será incluída sem o respectivo lançamento financeiro gerado.  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa | Bolsa excluída retroativamente (P1 à P6) | Status da Bolsa após exclusão | Parcela criada no contrato do aluno para registrar a cobrança do valor total das bolsas excluídas |
| P1 = 1000,00 | Baixado | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa | P7 = 600,00 (6 x 100,00 de cada bolsa excluída) |
| P2 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa |  |
| P3 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa |  |
| P4 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa |  |
| P5 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa |  |
| P6 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa |  |
|  | | | Total = 600,00 |  | |

**Cenário 2:**− Exclusão ***parcial*** da bolsa, somente da parcela 2, indicando-se parcela inicial = 2 e parcela final = 2  
**Resultado:**− A Bolsa X inicialmente aplicada para as 6 parcelas terá a sua validade alterada para a parcela 1 (parcela inicial = 1 e parcela final = 1) e será incluída a mesma Bolsa X de 10% para as parcelas de 3 a 6 (parcela inicial = 3 e parcela final = 6) sendo que essa última terá uma referência para o Id. da bolsa de origem.  
− Será incluída no contrato do aluno a parcela **7** no valor de 100,00 para a cobrança do valor da bolsa excluída (parcela 2 à parcela 2). O Tipo de parcela, Serviço e Data de vencimento utilizados para esta parcela obedecerão às informações que foram previamente parametrizadas.  
− Se a opção '*Gerar lançamentos de cobrança automaticamente'* definida previamente nos parâmetros do sistema estiver marcada, o lançamento financeiro desta parcela será gerado automaticamente, caso contrário, a parcela será incluída sem o respectivo lançamento financeiro gerado.  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa | Bolsa excluída retroativamente (P2 à P2) | Status da Bolsa após exclusão | Parcela criada no contrato do aluno para registrar a cobrança do valor total das bolsas excluídas |
| P1 = 1000,00 | Baixado | 10% = 100,00 (Status=Ativa) |  | Ativa | P7 = 100,00 (valor da bolsa excluída da P2) |
| P2 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | - |  |
| P3 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) |  | Ativa |  |
| P4 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) |  | Ativa |  |
| P5 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) |  | Ativa |  |
| P6 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) |  | Ativa |  |
|  | | | Total = 100,00 |  | |
