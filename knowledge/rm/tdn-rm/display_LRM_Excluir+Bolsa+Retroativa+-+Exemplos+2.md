---
content_hash: b25bb166b2fe7e82cefd22c920ada18eb2ae2cf2656cd3cea9ae7d555967d478
fetched_at: '2026-06-29T00:09:36.364159+00:00'
page_id: '425459503'
product: rm
source: tdn-rm
title: Excluir Bolsa Retroativa - Exemplos 2
type: documentation
url: https://tdn.totvs.com/display/LRM/Excluir+Bolsa+Retroativa+-+Exemplos+2
version: 3
---

---

**2 – Dividir pela quantidade de parcelas restantes**:

**Exemplos:**− Contrato possui 6 parcelas de 1000,00 cada.  
− A Bolsa X de 10% está aplicada para as 6 parcelas do contrato (parcela inicial = 1 e parcela final = 6).

**Cenário 1:**− Os lançamentos financeiros das parcelas 1 e 2 *já* foram gerados.  
− Parcelas 3, 4, 5 e 6 *não* possuem lançamentos financeiros gerados.  
− Exclusão ***parcial*** da bolsa, somente da parcela 2, indicando-se parcela inicial = 2 e parcela final = 2  
**Resultado:**− A Bolsa X inicialmente aplicada para as 6 parcelas terá a sua validade alterada para a parcela 1 (parcela inicial = 1 e parcela final = 1) e será incluída a mesma Bolsa X de 10% para as parcelas de 3 a 6 (parcela inicial = 3 e parcela final = 6) sendo que essa última terá uma referência para o Id. da bolsa de origem.  
− Serão incluídos no contrato do aluno 4 parcelas (parcela 3 - cota 2, parcela 4 - cota 2, parcela 5 - cota 2 e parcela 6 - cota 2,) no valor de 25,00 cada.  
Cálculo do valor:  
• Valor total referente à bolsa excluída = 100,00 (parcela inicial = 2 e parcela final = 2).  
• Quantidade de parcelas que ainda não possuem lançamentos financeiros gerados = 4 (P3, P4, P5 e P6). Rateio do valor a ser cobrado = 25,00 (100,00 / 4 parcelas não geradas)  
− Se a opção '*Gerar lançamentos de cobrança automaticamente'* definida previamente nos parâmetros do sistema estiver marcada, os lançamentos financeiros destas parcelas serão gerados automaticamente, caso contrário, a parcela será incluída sem o respectivo lançamento financeiro gerado.  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa | Bolsa excluída retroativamente  (P2 à P2) | Status da Bolsa após exclusão | Parcela criada no contrato do aluno para registrar a cobrança do valor total das bolsas excluídas |
| P1 = 1000,00 | Baixado | 10% = 100,00 (Status=Ativa) |  | Ativa |  |
| P2 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | - |  |
| P3 = 1000,00 | - | 10% = 100,00 (Status=Ativa) |  | Ativa | P3\_cota2 = 25,00 (100,00 / 4 parcelas sem lançamento) |
| P4 = 1000,00 | - | 10% = 100,00 (Status=Ativa) |  | Ativa | P4\_cota2 = 25,00 (100,00 / 4 parcelas sem lançamento) |
| P5 = 1000,00 | - | 10% = 100,00 (Status=Ativa) |  | Ativa | P5\_cota2 = 25,00 (100,00 / 4 parcelas sem lançamento) |
| P6 = 1000,00 | - | 10% = 100,00 (Status=Ativa) |  | Ativa | P6\_cota2 = 25,00 (100,00 / 4 parcelas sem lançamento) |
|  |  |  | Total = 100,00 |  |  |

**Importante**:   
Como as novas parcelas incluídas para cobrança da bolsa removida possuem a mesma data de vencimento e mesmo responsável financeiro, elas podem ser geradas agrupadas em um único boleto com o lançamento da parcela correspondente desde que o Tipo destas parcelas seja diferente de 'Parcela extra'. A configuração do Tipo de parcela a ser adotado é definida em *Ambiente | Configuração | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Bolsa Retroativa 3/3*.

**Cenário 2:**− Os lançamentos financeiros das 6 parcelas *já* foram gerados.  
− Exclusão ***total*** da bolsa indicando-se parcela inicial = 1 e parcela final = 6  
**Resultado:**− A Bolsa X permanecerá no contrato mas ficará *inativada* (campo 'Bolsa ativa' será desmarcado) com todos os seus campos bloqueados para edição.  
− Mesmo sendo selecionada a opção *'Dividir pela quantidade de parcelas restantes'* será incluída no contrato do aluno a parcela **7** no valor de 600,00 (6 x 100,00 = 600,00) para a cobrança do valor total das bolsas excluídas, pois todas as parcelas possuem lançamentos financeiros gerados, não sendo possível assim, ratear o valor da cobrança entre as parcelas. O Tipo de parcela, Serviço e Data de vencimento utilizados para esta parcela obedecerão às informações que foram previamente parametrizadas.  
− Se a opção '*Gerar lançamentos de cobrança automaticamente'* definida previamente nos parâmetros do sistema estiver marcada, o lançamento financeiro desta parcela será gerado automaticamente, caso contrário, a parcela será incluída sem o respectivo lançamento financeiro gerado.  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa | Bolsa excluída retroativamente  (P1 à P6) | Status da Bolsa após exclusão | Parcela criada no contrato do aluno para registrar a cobrança do valor total das bolsas excluídas |
| P1 = 1000,00 | Baixado | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa | \* P7 = 600,00 (6 x 100,00 de cada bolsa excluída) |
| P2 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa |  |
| P3 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa |  |
| P4 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa |  |
| P5 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa |  |
| P6 = 1000,00 | Em aberto | 10% = 100,00 (Status=Ativa) | 100,00 | Inativa |  |
|  | | | Total = 600,00 | \* Criou a **P7**, pois todas as parcelas do contato estão geradas | |
