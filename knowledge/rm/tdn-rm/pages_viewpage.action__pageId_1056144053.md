---
content_hash: e335fabafa1cd6e7878a6b7c734cb9e3196aec805c4d672b770c3e96c0b0146f
fetched_at: '2026-06-29T00:05:51.981927+00:00'
page_id: '1056144053'
product: rm
source: tdn-rm
title: Dados específicos do local da prestação do serviço (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056144053
version: 3
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **prestacao** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | **G** | **0-1** | **Tag raíz para as informações sobre a prestação dos serviços do documento.** |  | **O grupo será gerado conforme parâmetro "Não preencher grupo de prestação".**  **Para mais detalhes acesse:** |
| logradouro | prestacao | E | 1-1 | Logradouro onde foi realizada a prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| numend | prestacao | E | 1-1 | Número do endereço da prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| complend | prestacao | E | 1-1 | Complemento do endereço da prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| codmunibge | prestacao | E | 1-1 | Código do município da prestação padrão IBGE |  | Código de Classificação definido para o  município da Prestação conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI)  Obs: Esta tag será gerada com base na seguinte regra:  **Origem**: Município do Cadastro do Filial (Movimento de Venda\Lançamento de Saída)  ou município do cadastro Cliente\Fornecedor (Movimento de Compra\Lançamento de Entrada)  **Destino**:  Município do cadastro Cliente\Fornecedor(Movimento de Venda\Lançamento de Saída) e  Município do Cadastro do Filial (Movimento de Compra\Lançamento de Entrada)  **Local** **Incidência:** Município informado no movimento (Integrações | Fiscal | Município). Imagem  **Importante**: quando o movimento possuir mais de um item e os itens possuírem locais de prestação diferentes, a tag será gerada como **Local de Incidência.** |
| codmunincidenciaibge | prestacao | E | 0-1 | Código do município da prestação padrão IBGE |  | Código de Classificação definido para o  município da Prestação conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI)  **Obs**.: Esta tag será gerada quando estiver parametrizado para integração via TPF Imagem |
| municipio | prestacao | E | 1-1 | Município da prestação dos serviços do documento. | GMUNICIPIO.NOMEMUNICIPIO |  |
| bairro | prestacao | E | 1-1 | Bairro da prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| uf | prestacao | E | 1-1 | Unidade federativa da prestação dos serviços do documento. | GMUNICIPIO.CODETDMUNICIPIO |  |
| cep | prestacao | E | 0-1 | CEP da prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| pais | prestacao | E | 0-1 | Código de classificação do país de prestação. |  | Não será gerado |
| cep | prestacao | E | 1-1 | CEP da prestação dos serviços do documento. |  | Campo complementar conforme documento .  Caso esteja vazia, esta tag não será exibida no XML da nota |
| tipoLogradouro | prestacao | E | 0-1 | Tipo de Logradouro |  | Não será gerado |

Caso esteja vazio, este grupo "prestacao" não será exibido no XML da nota
