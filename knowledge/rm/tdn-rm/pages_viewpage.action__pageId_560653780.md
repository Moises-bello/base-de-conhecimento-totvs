---
content_hash: bf9507303ef2e1845b90d8000d9bde91f9f270c1d434a424f7b62fa85840f448
fetched_at: '2026-06-29T00:10:47.713849+00:00'
page_id: '560653780'
product: rm
source: tdn-rm
title: Dados do intermediário do serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653780
version: 4
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **intermediario** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **G** | **0-1** | **Tag raíz para as informações sobre o intermediador.** |  | **Não será Gerado** |
| razao | intermediario | E | 0-1 | Razão social do intermediador. |  | Não será Gerado |
| cpfcnpj | intermediario | E | 1-1 | CPF/CNPJ do intermediador. |  | Não será Gerado |
| NIF | intermediario | E | 0-1 | NIF. |  | Não será Gerado |
| cNaoNIF | intermediario | E | 0-1 | Motivo sem NIF. |  | Não será Gerado |
| CAEPF | intermediario | E | 0-1 | CAEPF. |  | Não será Gerado |
| inscmun | intermediario | E | 0-1 | Inscrição municipal do intermediador. |  | Não será Gerado |
| issretido | intermediario | Alfanumérico | 0-1 | ISS Retido. |  | Não será Gerado |
| codmunint | intermediario | Numérico | 0-1 | Código Município do Intermediário. |  | Não será Gerado |
| identificador | intermediario | Alfanumérico | 0-1 | Identificador. |  | Não será Gerado |
| tipologr | intermediario | Alfanumérico | 0-1 | Tipo logradouro. |  | Não será Gerado |
| logradouro | intermediario | Alfanumérico | 0-1 | Logradouro. |  | Não será Gerado |
| numend | intermediario | Alfanumérico | 0-1 | Número. |  | Não será Gerado |
| complend | intermediario | Alfanumérico | 0-1 | Complemento. |  | Não será Gerado |
| tipobairro | intermediario | Alfanumérico | 0-1 | Tipo bairro. |  | Não será Gerado |
| bairro | intermediario | Alfanumérico | 1-1 | Bairro. |  | Não será Gerado |
| codmunibge | intermediario | Numérico | 0-1 | Código IBGE. |  | Não será Gerado |
| codmunsiafi | intermediario | Numérico | 0-1 | Código SIAFI. |  | Não será Gerado |
| cidade | intermediario | Alfanumérico | 1-1 | Cidade. |  | Não será Gerado |
| estado | intermediario | Alfanumérico | 0-1 | Estado. |  | Não será Gerado |
| uf | intermediario | Alfanumérico | 1-1 | UF. |  | Não será Gerado |
| cep | intermediario | Alfanumérico | 0-1 | CEP. |  | Não será Gerado |
| email | intermediario | Alfanumérico | 0-1 | E-mail. | 120 | Não será Gerado |
| ddd | intermediario | Numérico | 0-1 | DDD. | 2 | Não será Gerado |
| telefone | intermediario | Numérico | 0-1 | Telefone. | 10 | Não será Gerado |
| codpais | intermediario | Alfanumérico | 0-1 | Código País. | 5 | Não será Gerado |
| nomepais | intermediario | Alfanumérico | 0-1 | Nome País. | 50 | Não será Gerado |
| estrangeiro | intermediario | Alfanumérico | 1-1 | Estrangeiro (1-Sim, 2-Não). | 1 | Não será Gerado |
| inscest | intermediario | Alfanumérico | 0-1 | Inscrição Estadual. | 20 | Não será Gerado |
| situacaoespecial | intermediario | Alfanumérico | 0-1 | Situação Especial. | 1 | Não será Gerado |
| tipopessoa | intermediario | Alfanumérico | 0-1 | Tipo Pessoa. | 2 | Não será Gerado |
