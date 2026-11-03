---
article_id: 37326340508055
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e0e8fe22b9c4e247d20b5f4c2cba8d5b531c2b87d8b44b009fd01c44bee7b336
fetched_at: '2026-06-28T22:38:29.742463+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como emitir uma nota de Multa
  e juros (tpNFDebito = 04)
type: support-article
updated_at: '2026-06-11T14:55:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37326340508055-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-emitir-uma-nota-de-Multa-e-juros-tpNFDebito-04
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37326347960215) Tempo aproximado para leitura:**00:03:00 min**  
  
**Dúvida**  
Como emitir uma nota de Multa e juros (**tpNFDebito = 04)**?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 12.1.2210  
  
**Solução**  
A Nota Fiscal de débito "**Multa e Juros**" é emitida pelo Fornecedor sempre que houver o recebimento de multas e juros por pagamentos atrasados, conforme o Art. 12, § 1º, II, da LC nº 214/2025. Este débito deve ser lançado no período de apuração do recebimento dos valores. Neste documento cada item da NF-e deve referenciar o item específico da nota fiscal original e aplicar a mesma classificação tributária <cClassTrib> e alíquota efetiva do fornecimento original. A quitação do débito gerado por esta nota produz o correspondente Crédito de IBS para o adquirente (se este for do regime regular).

Caso o Fornecedor não emita esta nota, o Adquirente tem permissão legal para regularizar a operação emitindo uma Nota Fiscal de Crédito.

**Processo**:

* Ao incluir o documento de débito deve ser informado no campo de tipo "Tipo Compl." como “4 - Multa e Juros”;

(A numeração e série não são editáveis, pois serão geradas na confirmação.)

* Informe o **Cliente**e **Loja**, este deve ser o Pagador da Multa e dos Juros, ou seja, o mesmo cliente do documento a ser referenciado;
* Informe uma **Condição de Pagamento**(meramente informativa, pois não haverá geração de financeiro);
* Informe na grid:
  + **Produto -** Devem ser informados todos os itens que geraram multa e/ou juros.
  + **Quantidade -** Para este tipo de documento não deve ser informada quantidade.
* Informe o **Valor**. Será sobre este valor que haverá incidência do calculo de tributos;

O valor de cada item deve seguir a proporcionalidade da nota original em relação ao valor total para o valor da multa e/ou juros.

Exemplo:

Nota Fiscal de Venda:

| Valor Total | 10000,00 |
| --- | --- |
| Valor Item 01 | 300,00 |
| Valor Item 02 | 700,00 |

O cliente desta nota não realizou o pagamento no prazo e foram gerados 10% de multa, portanto 100,00 em valor monetário e 2% pelo atraso, logo, 20,00 valor monetário. **Totalizando 120,00**, em multa e juros.

Ao serem detalhados os itens na Nota de Débito 04, deverão seguir a mesma razão:

| Valor Total | 120,00 |
| --- | --- |
| Valor Item 01 | 36,00 |
| Valor Item 02 | 84,00 |

* Informe uma **TES**que **não movimenta estoque** e **não gera financeiro**;
* Clique na opção **Vincular**;
  + Na parte superior, em **Filtros**, informe os dados para a busca do documento a ser referenciado nesta nota;
    - Como estamos tratando de saídas próprias anteriores, informe os dados contidos na nota referenciada que gerou a multa e/ou juros;
  + Na seção **Itens**, serão listados os produtos informados no documento. A busca será feita com base nos dados da seção **Filtros**e do produto posicionado nesta seção.
  + Clique em **Buscar**. Serão listados até 300 linhas de itens de entrada de acordo com os filtros na seção **Resultado do filtro**;
  + **Marque**o item que deu origem ao crédito. O registro marcado será listado na seção **Documentos Selecionados**;
  + Clique em **Confirmar**;
* Clique em **Confirmar**;
* Selecione a **Série**e **Numeração**para geração do documento.

**Importante**: O referenciamento da Nota de Débito (**Multas e Juros**) com o Documento de Saída é realizado por meio da tabela **DKN**.  
Nesse processo, o Documento de Origem (**DKN\_DOCREF**) é vinculado ao Documento gerado, pela Nota de Debito (**DKN\_DOC**) e, no campo **DKN\_CHVNFE**, é registrada a chave da NF-e.

No momento da transmissão da Nota de Débito, o sistema gera no XML a tag **DFeReferenciado**, contendo as tags **ChaveAcesso** (com o conteúdo da **F2\_CHVNFE**) e **nItem**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37805233636119)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37805233638423)

**Saiba mais:**

* [Notas de Débito (NF-e: finNFe = 6 - NT 2025.002)](https://tdn.totvs.com/pages/viewpage.action?pageId=1013620273)
* [Webinar TOTVS | SIGAFAT- Nota de Débito](https://www.youtube.com/watch?v=XbjR3mzXRp8)
