---
content_hash: 2514bbcb58ddae9a789e0e5119f0a82e1bb5bf5e3d3672bcc11681f80218d8fa
fetched_at: '2026-06-29T00:10:47.702093+00:00'
page_id: '560653725'
product: rm
source: tdn-rm
title: Dados específicos do local da prestação do serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653725
version: 36
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **prestacao** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **G** | **0-1** | **Tag raíz para as informações sobre a prestação dos serviços do documento.** |  | **O grupo será gerado conforme parâmetro "Não preencher grupo de prestação".**  **Para mais detalhes acesse:** |
| serieprest | prestacao | E | 1-1 | Série da prestação dos serviços do documento. |  | Fixo 99 |
| logradouro | prestacao | E | 1-1 | Logradouro onde foi realizada a prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| numend | prestacao | E | 1-1 | Número do endereço da prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| complend | prestacao | E | 1-1 | Complemento do endereço da prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| codmunibge | prestacao | E | 1-1 | Código do município da prestação padrão IBGE |  | Código de Classificação definido para o  município da Prestação conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI)  Obs: Esta tag será gerada com base na seguinte regra:  **Origem**: Município do Cadastro do Filial (Movimento de Venda\Lançamento de Saída)  ou município do cadastro Cliente\Fornecedor (Movimento de Compra\Lançamento de Entrada)  **Destino**:  Município do cadastro Cliente\Fornecedor(Movimento de Venda\Lançamento de Saída) e  Município do Cadastro do Filial (Movimento de Compra\Lançamento de Entrada)  **Local** **Incidência:** Município informado no movimento (Integrações | Fiscal | Município). Imagem  **Importante**: quando o movimento possuir mais de um item e os itens possuírem locais de prestação diferentes, a tag será gerada como **Local de Incidência.** |
| codmunibgeinc | prestacao | E | 0-1 | Código do município da prestação padrão IBGE |  | Código de Classificação definido para o  município da Prestação conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI)  **Obs**.: Esta tag será gerada quando estiver parametrizado para integração via TSS |
| codmunsiafi | prestacao | E | 1-1 | Código do município do prestador padrão SIAFI |  | Código de Classificação definido para o município conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI) |
| municipio | prestacao | E | 1-1 | Município da prestação dos serviços do documento. | GMUNICIPIO.NOMEMUNICIPIO |  |
| bairro | prestacao | E | 1-1 | Bairro da prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| uf | prestacao | E | 1-1 | Unidade federativa da prestação dos serviços do documento. | GMUNICIPIO.CODETDMUNICIPIO |  |
| codpais | prestacao | E | 0-1 | Código de classificação do país de prestação. | DPAIS.CODPAIS |  |
| cep | prestacao | E | 1-1 | CEP da prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| tipologr | prestacao | E | 0-1 | Tipo logradouro. |  | Não será gerado |

Caso esteja vazio, este grupo "prestacao" não será exibido no XML da nota
