---
content_hash: 01e2444ce4b1b01af76a00d947fa2b15da243225754098df410c3f300b0d9349
fetched_at: '2026-06-29T00:09:34.011427+00:00'
page_id: '425459112'
product: rm
source: tdn-rm
title: Excluir Bolsa Retroativa - Exemplos 4
type: documentation
url: https://tdn.totvs.com/display/LRM/Excluir+Bolsa+Retroativa+-+Exemplos+4
version: 2
---

---

**2.2 -** Exclusão de bolsas pelo processo de Bolsa Retroativa em parcelas que ***já possuem*** lançamentos financeiros gerados:

**Exemplos:**− Contrato possui 6 parcelas.  
− A Bolsa X de 10% está aplicada para as 6 parcelas do contrato (parcela inicial = 1 e parcela final = 6).  
− Os lançamentos financeiros das 6 parcelas *já* foram gerados.

**Cenário 1:**− Exclusão ***total*** da bolsa indicando-se parcela inicial = 1 e parcela final = 6  
**Resultado:**− A Bolsa X permanecerá no contrato mas ficará *inativada* (campo 'Bolsa ativa' será desmarcado) com todos os seus campos bloqueados para edição.  
− A Conta Corrente do aluno será atualizada com a inclusão de 6 registros de débitos no valor de 100,00 cada, correspondentes ao valor das bolsas removidas de cada parcela.  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
  (Contrato | Anexos | Rastreabilidade de bolsa retroativa)  
  (Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)  
  (Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)

**Cenário 2:**− Exclusão ***parcial*** da bolsa, somente da parcela 2, indicando-se parcela inicial = 2 e parcela final = 2  
**Resultado:**− A Bolsa X inicialmente aplicada para as 6 parcelas terá a sua validade alterada para a parcela 1 (parcela inicial = 1 e parcela final = 1) e será incluída a mesma Bolsa X de 10% para as parcelas de 3 a 6 (parcela inicial = 3 e parcela final = 6) sendo que essa última terá uma referência para o Id. da bolsa de origem.  
− A Conta Corrente do aluno será atualizada com a inclusão de um registro de débito no valor de 100,00 correspondente ao valor da bolsa removida da parcela 2.  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
  (Contrato | Anexos | Rastreabilidade de bolsa retroativa)  
  (Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)  
  (Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)
