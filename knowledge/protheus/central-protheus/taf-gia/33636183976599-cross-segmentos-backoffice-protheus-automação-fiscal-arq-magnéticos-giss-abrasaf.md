---
article_id: 33636183976599
category: TAF - GIA
content_hash: a5800f30c1932ae1f86b4d73b08644a39f3a3dd172e14a9a643fb61a4053bacd
fetched_at: '2026-06-28T22:41:32.332848+00:00'
product: protheus
section_id: 1500001547982
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Automação Fiscal - Arq. Magnéticos
  - GISS ABRASAF - Erro de estrutura ao importa arquivo XML.
type: support-article
updated_at: '2025-07-22T17:20:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33636183976599-Cross-Segmentos-Backoffice-Protheus-Automa%C3%A7%C3%A3o-Fiscal-Arq-Magn%C3%A9ticos-GISS-ABRASAF-Erro-de-estrutura-ao-importa-arquivo-XML
---

**Ocorrência**  
 Ao importar o arquivo XML no site do município é apresentada mensagem " ERRO DE ESTRUTURA"   
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - A partir da versão **12.1.2310**  
  
**Causa**  
Esse incidente ocorre, pois na escrituração do documento há campos obrigatórios para correta geração do arquivo em branco.

**Solução**  
Para solucionar essa ocorrência, confirme se todas TAG do XML foram geradas corretamente com todos os conteúdo valido.

### **Preenchimento das Principais Tags**

Para geração das Tags, é importante que o documento seja criado seguindo a estrutura abaixo:

Documentos Fiscais

* Capa do documento
  + Dt Emissão (**C20\_DTDOC**): O mês/ano selecionado deve corresponder ao mês/ano da data de emissão do Documento Fiscal;
  + Oper. (**C20\_INDOPE**): Para que o Documento Fiscal seja considerado, seu Tipo de Operação deverá corresponder a uma Emissão (Entrada);
  + Id.Tp DOcto (**C20\_TPDOC**): Deve representar o tipo de documento de Serviços (Nota Fiscal de Serviço);
* Produtos/Serviços
  + Cod. Serviço (**C30\_CODSER**): Código do Serviço;
* Tributo do Item
  + C. Tributo (**C35\_CODTRI**): Tributo 000016 ou 000001
  + Base Trib (**C35\_BASE**): Valor Consolidado
  + Aliq Tributo (**C35\_ALIQ**): Alíquota do Tributo
  + Vlr Tributo (**C35\_VALOR**): Valor do Tributo para o item do documento Fiscal

**Grupos importantes**

IdentificacaoDeclaracao

|  |  |
| --- | --- |
| <tipos:Numero>000000009</tipos:Numero> | C20\_NUMDOC |
| <tipos:NumeroDeclarado>000000009</tipos:NumeroDeclarado> | C20\_NUMDOC |
| <tipos:Serie>TAF</tipos:Serie> | C20\_SERIE |
| <tipos:SerieDeclarada>TAF</tipos:SerieDeclarada> | C20\_SERIE |
| <tipos:Tipo>1</tipos:Tipo> | Fixo = 1 |
| <tipos:Competencia>2022-06-30</tipos:Competencia> | C20\_DTCPIS |

**DadosPrestador**

|  |  |
| --- | --- |
| <tipos:Cnpj>62598779000146</tipos:Cnpj> | C1H\_CNPJ / C1H\_CPF |
| <tipos:NomeFantasia>TAFG04 - SAO PAULO SERVICOS - N RECOLHE</tipos:NomeFantasia> | C1H\_NOME |
| <tipos:RazaoSocial>TAFG04 - SAO PAULO SERVICOS - N RECOLHE</tipos:RazaoSocial> | C1H\_NOME |
| <tipos:Endereco>AV PAULISTA</tipos:Endereco> | C1H\_TPLOGR |
| <tipos:Numero>901</tipos:Numero> | C1H\_NUM |
| <tipos:Bairro>CENTRO</tipos:Bairro> | C1H\_BAIRRO |
| <tipos:CodigoMunicipio>SP50308</tipos:CodigoMunicipio> | C1H\_CODMUN |
| <tipos:Uf>SP</tipos:Uf> | C1H\_UF |
| <tipos:Cep/> | C1H\_CEP |
| <tipos:Telefone/> | C1H\_FONE |
| <tipos:Email/> | C1H\_EMAIL |
| <tipos:OptanteSimplesNacional>2</tipos:OptanteSimplesNacional>  <tipos:CodigoMunicipio>3550308</tipos:CodigoMunicipio> | C1H\_SIMPLS    C20\_CODLOC |

**DadosServicoComprado**

|  |  |
| --- | --- |
| <tipos:ValorServicos>1922.21</tipos:ValorServicos> | C20\_VLSERV |
| <tipos:ValorDeducoes>0</tipos:ValorDeducoes> | C20\_VLABMT+C20\_VLABSU |
| <tipos:ValorPis>0</tipos:ValorPis> | C35\_VALOR |
| <tipos:ValorCofins>0</tipos:ValorCofins> | C35\_VALOR |
| <tipos:ValorInss>0</tipos:ValorInss> | C35\_VALOR |
| <tipos:ValorIr>0</tipos:ValorIr> | C35\_VALOR |
| <tipos:ValorCsll>0</tipos:ValorCsll> | C35\_VALOR |
| <tipos:ValTotTributos>0</tipos:ValTotTributos> | Soma todos os tributos diferentes de 000001 e 000016 |
| <tipos:ValorIss>96.11</tipos:ValorIss> | C35\_VALOR |
| <tipos:Aliquota>5.00</tipos:Aliquota> | C35\_VALOR |
| <tipos:DescontoIncondicionado>0</tipos:DescontoIncondicionado> | C30\_VLDESC |
| <tipos:ItemListaServico>20.01</tipos:ItemListaServico> | C30\_CODSER |
| <tipos:CodigoTributacaoMunicipio>00.01.01</tipos:CodigoTributacaoMunicipio> | C30\_SRVMUN |
| <tipos:Discriminacao>Declaracao de servicos comprados</tipos:Discriminacao> | C30\_DESCRI |
| <tipos:ExigibilidadeISS>1</tipos:ExigibilidadeISS> | C30\_CODNAT - (Necessário que o campo C1N\_IDEXIG esteja preenchido) |

DadosConstrucaoCivil

|  |  |
| --- | --- |
| <tipos:CodigoObra>XXXXXX</tipos:CodigoObra> | C20\_IDOBR |
| <tipos:Art>XXXXXX</tipos:Art> | T9C\_CODART |

Documentação completa de geração da obrigação no TAF:   
<https://tdn.totvs.com/pages/releaseview.action?pageId=878920036>
