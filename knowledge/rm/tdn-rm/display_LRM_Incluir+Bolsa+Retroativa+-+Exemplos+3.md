---
content_hash: bebde3c0a433f08409fe3e4e41072ded9eebc047860e14375baeea7d58b35cdf
fetched_at: '2026-06-29T00:09:32.777015+00:00'
page_id: '425458917'
product: rm
source: tdn-rm
title: Incluir Bolsa Retroativa - Exemplos 3
type: documentation
url: https://tdn.totvs.com/display/LRM/Incluir+Bolsa+Retroativa+-+Exemplos+3
version: 3
---

---

1.3 – **Devolver em espécie**:

**Cenário:**Contrato do aluno possui 6 parcelas no valor de 1000,00 cada.  
− Todos os lançamentos financeiros das 6 parcelas já foram gerados.  
− Somente o lançamento financeiro da parcela 1 já foi 'Baixado' e os outros ainda permanecem 'Em aberto'.  
− Foi incluída uma bolsa retroativa de 10% para as 6 parcelas deste contrato.  
**Resultado:**− Serão incluídos 6 lançamentos de devolução no valor de 100,00 cada referente às bolsas incluídas retroativamente.  
− Informações da aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato serão atualizadas.  
− Registros com a rastreabilidade serão incluídos, registrando somente a inclusão da bolsa, em:  
*(Contrato | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)**(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Parcelas | Status do Lcto da parcela | Bolsa Retroativa | Vínculo criado no Lcto da parcela | Valor líquido Lcto da parcela | Lcto de Devolução (L) |
| P1 = 1000,00 | Baixado | 10% = 100,00 (L1) | - | 1000,00 | L1 = 100,00 |
| P2 = 1000,00 | Em aberto | 10% = 100,00 (L2) | - | 1000,00 | L2 = 100,00 |
| P3 = 1000,00 | Em aberto | 10% = 100,00 (L3) | - | 1000,00 | L3 = 100,00 |
| P4 = 1000,00 | Em aberto | 10% = 100,00 (L4) | - | 1000,00 | L4 = 100,00 |
| P5 = 1000,00 | Em aberto | 10% = 100,00 (L5) | - | 1000,00 | L5 = 100,00 |
| P6 = 1000,00 | Em aberto | 10% = 100,00 (L6) | - | 1000,00 | L6 = 100,00 |
|  | | | | | A baixa destes lançamentos deverá ser feita manualmente, pois não há Vínculo. |
