---
content_hash: af84ebafb34f116bb8105a39bbcc33b6f43a4ba6c9ac56525e076e83d38e7c50
fetched_at: '2026-06-29T00:11:26.424035+00:00'
page_id: '716367248'
product: rm
source: tdn-rm
title: recursosRep
type: documentation
url: https://tdn.totvs.com/display/LRM/recursosRep
version: 2
---

## Recursos repassados para associação desportiva

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| recursosRep | ideEstab | 1-1 |  | Recursos repassados para associação desportiva. | Informações do lançamento e do cli/for associado |
| cnpjAssocDesp | recursosRep | 1-1 | 14 | Preencher com o CNPJ da associação desportiva que mantém clube de futebol para a qual foi efetuado o repasse  Validação: Deve ser um CNPJ válido, diferente do CNPJ do declarante | FCFO.CGCCFO |
| vlrTotalRep | recursosRep | 1-1 | 14 | Preencher com o valor bruto dos recursos repassados  Validação: Deve corresponder a soma do campo {vlrBruto} do grupo {infoRecurso} | Somatório dos registros filhos. |
| vlrTotalRet | recursosRep | 1-1 | 14 | Soma do valor da retenção dos recursos recebidos  Validação: Deve corresponder a soma do campo {vlrRetApur} do grupo {infoRecurso}. | Somatório dos registros filhos. |
| vlrTotalNRet | recursosRep | 0-1 | 14 | Valor da retenção que deixou de ser feita pela entidade que efetuou o repasse ou que foi depositada em juízo em decorrência da decisão judicial/administrativa  Validação: Não pode ser maior que {vlrTotalRet} e deve corresponder a soma do campo {vlrNRet} dos registros vinculados | Somatório dos registros filhos. |
