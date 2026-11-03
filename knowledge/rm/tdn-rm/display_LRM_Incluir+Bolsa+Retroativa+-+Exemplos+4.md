---
content_hash: 12060ebd1c6e86ed515cbf902b8411ca5998998316a243c84e8ae7f6a9d66a87
fetched_at: '2026-06-29T00:09:33.127231+00:00'
page_id: '425458926'
product: rm
source: tdn-rm
title: Incluir Bolsa Retroativa - Exemplos 4
type: documentation
url: https://tdn.totvs.com/display/LRM/Incluir+Bolsa+Retroativa+-+Exemplos+4
version: 3
---

---

2- Utilizando a opção **'Utilizar a movimentação em conta corrente'**:

**Cenário:**− Saldo atual da Conta Corrente do aluno está vazio = 0,00  
− Aluno possui um contrato de 6 parcelas no valor de 1000,00 cada  
− Todos os lançamentos financeiros das 6 parcelas já foram gerados e estão 'Baixados'  
− Inclusão de Bolsa Retroativa de 10% para as 6 parcelas  
**Resultado**:  
− A bolsa será incluída no contrato do aluno e será marcada como Bolsa Retroativa.  
− Na Conta Corrente do aluno serão incluídos 6 registros com os valores dos créditos gerados pela inclusão da Bolsa Retroativa.  
− Informações da aba *'Valores créditos/débitos gerados'* no cadastro do contrato do aluno e também da bolsa no contrato serão atualizados.  
− Registros com a rastreabilidade serão incluídos em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

**Importante**: Optando por utilizar a opção '**Utilizar a movimentação em conta corrente**', a Conta Corrente do aluno será atualizada a cada Inclusão/Exclusão de Bolsa Retroativa com os registros de crédito e de débito respectivamente. Neste caso, os valores existentes na Conta Corrente do aluno serão aproveitados futuramente conforme parametrização prévia e específica para este fim. Ao realizar a baixa dos lançamentos das parcelas cujas bolsas foram concedidas retroativamente, não haverá nenhum abatimento, pois neste caso não há a inclusão de 'Vínculos'.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa Retroativa | Vínculo criado no Lcto da parcela | Valor líquido Lcto da parcela | Créditos incluídos na Conta Corrente do aluno ref. às Devoluções (C) |
| P1 = 1000,00 | Baixado | 10% = 100,00  (C1) | - | 1000,00 | C1 = 100,00 |
| P2 = 1000,00 | Em aberto | 10% = 100,00  (C2) | - | 1000,00 | C2 = 100,00 |
| P3 = 1000,00 | Em aberto | 10% = 100,00  (C3) | - | 1000,00 | C3 = 100,00 |
| P4 = 1000,00 | Em aberto | 10% = 100,00  (C4) | - | 1000,00 | C4 = 100,00 |
| P5 = 1000,00 | Em aberto | 10% = 100,00  (C5) | - | 1000,00 | C5 = 100,00 |
| P6 = 1000,00 | Em aberto | 10% = 100,00  (C6) | - | 1000,00 | C6 = 100,00 |
|  |  |  |  |  | Total de créditos na CC ref. às bolsas retroativas = 600,00 |
