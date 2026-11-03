---
content_hash: 973586c3440cdb10fd62674ead68318dac025219b0c2f77a289ccbe42d4a0815
fetched_at: '2026-06-29T00:12:02.457642+00:00'
page_id: '901953557'
product: rm
source: tdn-rm
title: Dados do Produto ou Serviço (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901953557
version: 12
---

# prod - Dados do Produto ou Serviço

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **prod** | **[det](https://tdn.totvs.com/pages/viewpage.action?pageId=901953457)** | **1-990** | **Grupo** | Dados do Produto ou Serviço |
| cProd | prod | 1-1 | Elemento | Cadastro do item | Código do produto/serviço.  TPRODUTO.CODIGOPRD |
| xProd | prod | 1-1 | Elemento | Em Ambiente | Parâmetros | Tabelas | Produtos | Definições Gerais:   Descrição do produto.   **Se** campo Descrição do produto =  Descrição  e a descrição do produto estiver preenchida.  **então** TPRODUTO.DESCRICAO **senão** campo Descrição do produto =  Descrição  Auxiliar e a descrição auxiliar do produto estiver preenchida.   **então**  TPRODUTO.DESCRICAOAUX  **senão**  TPRODUTO.NOMEFANTASIA   A tag é limitada a 120 caracteres, caso possua mais de 120 caracteres a informação será truncada. |
| cClass | prod | 1-1 | Elemento | Cadastro do serviço | Anexos | Dados Fiscais do Produto | Classificação item de Comunicação/Telecomunicação.  Somente serão apresentados registros cujo ao campo **Campo** seja = 6 (Classificação Item Serviços de Comunicação /Telec.)  Vide: <https://tdninterno.totvs.com/display/public/LRM/Valor+x+Campos+Rotinas> |
| CFOP | prod | 0-1 | Elemento | **Se** CFOP não Fiscal (Aba identificação, flag fiscal desmarcado)  **Então**CFOP do item do movimento. Integrações | aba Fiscal.  **Senão** O campo não será gerado |
| CNPJLD | prod | 0-1 | Elemento | Não será gerado |
| uMed | prod | 1-1 | Elemento | No item do movimento | pasta Identificação | aba Cabeçalho | unidade (TITMMOV.CODUND)  MIN = 1  MB = 2 GB = 3  UN = 4   Necessário cadastrar unidades de medida com os códigos acima. |
| qFaturada | prod | 1-1 | Elemento | No item do movimento | pasta Identificação | aba Cabeçalho | Quantidade.  TITMMOV.QUANTIDADE |
| vItem | prod | 1-1 | Elemento | Verifica parametrização do tipo de movimento na Etapa 28 - Item - Preços)  Calcular valor unitário = Edita preço total marcado  &&                    diferente de  Não calcular preço unitário &&          valor total do item no movimento maior que 0 &&  preço total editado no item de movimento marcado &&         quantidade no item de movimento maior que 0.  **Se** Calcular valor unitário   **então**  No item do movimento | pasta Identificação | aba Cabeçalho | valor total do item dividido pela quantidade.  (TITMMOV.VALORTOTALITEM /  TITMMOV.QUANTIDADE)  **senão**  No item do movimento | pasta Identificação | aba Cabeçalho | Preço unitário.  (TITMMOV.PRECOUNITARIO) |
| vDesc | prod | 0-1 | Elemento | Verifica parametrização do tipo de movimento na etapa 36 - Item - Valores Financeiros  **Se** Afeta desconto no movimento  **então**  No item do movimento | pasta Tributos e valores | aba valores | valor do desconto.  (TITMMOV.VALORDESC)  **senão**  No item do movimento | pasta Tributos e valores | aba valores | valor do desconto + valor do rateio do desconto + valor desconto incondicional.  (TITMMOV.RATEIODESC + TITMMOV.VALORDESC + TITMMOV.VALORDESCCONDICONALITM) |
| vOutro | prod | 0-1 | Elemento | Verifica parametrização do tipo de movimento na etapa 36 - Item - Valores Financeiros  **Se** Afeta despesa no movimento  **então**  No item do movimento | pasta Tributos e valores | aba valores | valor da despesa.  (TITMMOV.VALORDESP)  **senão**  No item do movimento | pasta Tributos e valores | aba valores | valor da despesa+ valor do rateio da despesa).  (TITMMOV.RATEIODESP+ TITMMOV.VALORDESP) |
|  |  |  |  |  |
| vProd | prod | 1-1 | Elemento | Verifica parametrização do tipo de movimento na Etapa 28 - Item - Preços)  Preço total  = Edita preço total marcado  &&           valor total do item no movimento maior que 0 &&  preço total editado no item de movimento marcado.  **Se** Preço total  **então**  No item do movimento | pasta Identificação | aba Cabeçalho | valor total do item (TITMMOV.VALORTOTALITEM)   **senão**  No item do movimento | pasta Identificação | aba Cabeçalho | Preço unitário  multiplicado pela quantidade.  (TITMMOV.PRECOUNITARIO \* TITMMOV.QUANTIDADE) |
| dExpiracao | prod | 0-1 | Elemento | Não será gerado |
| indDevolucao | prod | 0-1 | Elemento | Cadastro da natureza de operação Aba: Outros Dados | Tipo Devolução.  **Se** Tipo devolução (DCFOP.TIPODEVOLUCAO) = devolução  **Então** 1,  **senão** O campo não será gerado |

Exemploxml
  

01.01
Produto teste Um
0100101
6101
4
1.00
100.00000000
10.00
20.00
100.00000000


0,6500
3,0000
1,0000
600,0000
5,0000
  
]]>
