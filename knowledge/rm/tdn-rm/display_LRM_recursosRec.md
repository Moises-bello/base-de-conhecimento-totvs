---
content_hash: 4f12070ec88f398f26199a0baf3a378648d122ff248cbafc9644e5b7e7fb5d6e
fetched_at: '2026-06-29T00:11:26.400358+00:00'
page_id: '716359106'
product: rm
source: tdn-rm
title: recursosRec
type: documentation
url: https://tdn.totvs.com/display/LRM/recursosRec
version: 3
---

## Recursos recebidos por associação desportiva que mantenha equipe de futebol profissional.

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| recursosRec | ideEstab | 1-N | - | Registro preenchido exclusivamente por associação desportiva que mantenha equipe de futebol profissional, quando receber repasse de outras empresas a título de patrocínio, publicidade, licenciamento, etc . Totalizador dos recursos recebidos por estabelecimento. | Informações do lançamento e do Cli/For associado. |
| cnpjOrigRecurso | recursosRec | 1-1 | 14 | Preencher com o CNPJ da empresa que repassou recursos  Validação: Deve ser um CNPJ válido, diferente do CNPJ do declarante | FCFO.CGCCFO |
| recEmprExt | recursosRec | 0-1 | 001 | Informar se a empresa é domiciliada no exterior e não sujeita à inscrição no  CNPJ. Valores válidos: S. | Gerado com S quando o cli\for é do exterior |
| nmEmprExt | recursosRec | 0-1 | 070 | Informar o nome da empresa que repassou os recursos e que não é sujeita à  inscrição no CNPJ por ser domiciliada no exterior. Validação: Informação obrigatória e exclusiva se {recEmprExt} for  informado. Regra de validação: REGRA\_NOME\_VALIDO\_EXT | Gerado com o nome do cli\for do Exterior |
| vlrTotalRec | recursosRec | 1-1 | 14 | Preencher com o valor bruto dos recursos recebidos.  Validação: Deve corresponder a soma do campo {vlrBruto} do grupo {infoRecurso} | Somatório dos registros filhos. |
| vlrTotalRet | recursosRec | 1-1 | 14 | Soma do valor da retenção dos recursos recebidos.  Validação: Deve corresponder a soma do campo {vlrRetApur} do grupo {infoRecurso}. | Somatório dos registros filhos. |
| vlrTotalNRet | recursosRec | 0-1 | 14 | Valor da retenção que deixou de ser feita pela entidade que efetuou o repasse ou que foi depositada em juízo em decorrência da decisão judicial/administrativa  Validação: Não pode ser maior que {vlrTotalRet} e deve corres-ponder a soma do campo {vlrNRet} dos registros vin-culados | Somatório dos registros filhos. |
