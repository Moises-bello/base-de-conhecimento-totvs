---
content_hash: 024b67bf3b837f4870ce5b263eb26da60e79346210e716dcf563fd0776d60a67
fetched_at: '2026-06-29T00:09:22.761860+00:00'
page_id: '422546026'
product: rm
source: tdn-rm
title: NF-em (Joinville)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546026
version: 19
---

A geração da NF-em deverá ser executada a partir do TOTVS Gestão de Estoque, Compras e Faturamento, no menu \*Utilitários / NF-e Municipal / NF-em Joinville{\*}. Deverão ser informados, na tela da rotina, a Filial, a Data Inicial e Final, Numeração Inicial e Final o Local aonde os arquivos deverão ser salvos e o Tipo de Movimento de Entrada e de Saída (os dois Tipos de Movimento são necessários para que sejam gerados os dois arquivos).

Além destas informações, também deverá ser informado se deverão ser exportadas todas as notas que atendam os critérios informados anteriormente ou somente notas que ainda não foram exportadas.  
Poderão ser gerados dois arquivos, um arquivo referente aos RPS, contendo as Notas Fiscais emitidas e outro arquivo referente aos DIR, contendo as Notas Fiscais \*recebidas\* cujo ISS deverá ser retido pela Filial, dependendo do Tipo de Movimento informado na tela de geração.  
Os arquivos serão gerados em formato XML para depois serem importados no site da Prefeitura.  
***Observação***: Não é necessária nenhuma parametrização específica nos Tipos de Movimento. As parametrizações existentes, referentes à NF-e Municipal, dizem respeito à NF-e padrão São Paulo e não à de Joinville.

**Seleção de Nota Fiscal**

Para a geração do arquivo referente às Notas Fiscais Emitidas (NF-em), serão selecionados todos os Movimentos de Saída que atendam aos critérios informados anteriormente e que possuam pelo menos um item cuja Natureza de Operação associada seja NÃO FISCAL.  
Para a geração do arquivo referente às Notas Fiscais Recebidas (DIR), serão selecionadas todas as Notas Fiscais de Entrada, que atendam aos critérios informados anteriormente e que tenham o Tributo do Tipo ISS com Tipo de Recolhimento "Retido na Fonte" ou "Retido na Fonte Deduzido".

**Preenchimento dos Campos - RPS**

Seguem as descrições de preenchimento de alguns campos que podem causar dúvidas:

* Campos relativos ao **Lote**:

**<numero>**: Será gerado um código seqüencial para cada lote de RPS gerado. Este código será armazenado em um campo interno do Movimento, chamado "RECIBONFENUMERO", de modo que possam ser montados relatórios de rastreabilidade para se identificar quais Movimentos compuseram determinado lote.

* Campos relativos ao **RPS**

**<operacao>**: Receberá o valor "C - Cancelamento" caso o Status do Movimento seja cancelado. Caso contrário receberá o valor "I - Inserção";  
**<tipo>**: Receberá o valor "2 - NF Conjugada" caso o Movimento possua algum CFOP Fiscal;  
**<descrição\_servicos>**: Receberá, de forma concatenada, as seguintes informações do movimento : o conteúdo do seu histórico mais o conteúdo das descrições dos produtos / itens mais o conteúdo dos históricos dos produtos / itens;  
**<destino\_servico>**: Será preenchido de acordo com o "Ramo de Atividade" do Cliente/Fornecedor do Movimento. Se o mesmo for "Comércio" ou "Indústria" este campo será preenchido com o valor "1 - Comércio/Indústria". Caso contrário será preenchido com o valor "0 - Outros";  
**<valor\_total>**: Será preenchido com o somatório de ((Quantidade X Preço) - Descontos + Despesas) dos itens que estejam vinculados a Naturezas de Operação NÃO FISCAL. Para os Descontos e Despesas serão considerados os valores informados no Item mais o Rateio dos valores informados no Movimento;\[2\]  
**<valor\_deducao>**: Será preenchido com o somatório dos campos "Valor do Material" e "Valor da Sub Empreitada";  
**<local\_servico>**: Será preenchido com o nome do Município aonde o serviço foi prestado (TMOV. CODMUNSERVICO), caso este seja diferente de Joinville;  
**<aliquota\_iss>**: Será preenchido de acordo com a Alíquota do Tributo ISS do Item de Movimento;  
**<valor\_iss>**: Será preenchido com o somatório do Valor do Tributo ISS do Item de Movimento;  
**<iss\_retido>**: Será preenchido com "1" caso o Tipo de Recolhimento do Tributo ISS seja "Retido na Fonte" ou "Retido na fonte Deduzido". Caso contrário será preenchido com "0";  
**<valor\_irrf>**: Será preenchido de acordo com o Valor do Tributo IRRF, caso exista. Caso seja informado no Item de Movimento, ser preenchido com o somatório de todos os Itens;  
**<valor\_inss>**: Será preenchido de acordo com o Valor do Tributo INSS, caso exista. Caso seja informado no Item de Movimento, ser preenchido com o somatório de todos os Itens;  
**<valor\_pis>**: Será preenchido de acordo com o Valor do Tributo PIS-RF, caso exista. Caso seja informado no Item de Movimento, ser preenchido com o somatório de todos os Itens;  
**<valor\_cofins>**: Será preenchido de acordo com o Valor do Tributo COFINS-RF, caso exista. Caso seja informado no Item de Movimento, ser preenchido com o somatório de todos os Itens;  
**<valor\_csll>**: Será preenchido de acordo com o Valor do Tributo CSLL-RF, caso exista. Caso seja informado no Item de Movimento, ser preenchido com o somatório de todos os Itens.

* Campos relativos ao **Tomador**:

**<situação\_especial>**: Será preenchido de acordo com o "Ramo de Atividade" do Cliente/Fornecedor do Movimento. Se o mesmo for "Comércio" ou "Indústria" este campo será preenchido com o valor "4 – Comércio/Indústria". Caso contrário será preenchido com o valor "0 – Outro".

**Preenchimento de Campos - DIR**

Seguem as descrições de preenchimento de alguns campos que podem causar dúvidas:

* Campos relativos ao **Lote**:

**<numero>**: Será gerado um código sequencial para cada lote de DIR gerado. Este código será armazenado em um campo interno do Movimento, chamado "RECIBONFENUMERO", de modo que possam ser montados relatórios de rastreabilidade para se identificar quais Movimentos compuseram determinado lote.

* Campos relativos ao **DIR**:

**<valor\_total>**: Será preenchido com o somatório de ((Quantidade X Preço) - Descontos + Despesas) dos itens que estejam vinculados a Naturezas de Operação NÃO FISCAL. Para os Descontos e Despesas serão considerados os valores informados no Item mais o Rateio dos valores informados no Movimento;\[3\]  
**<valor\_base\_calculo>**: Será preenchido com o somatório da Base de Cálculo do Tributo ISS dos Itens do Movimento cujo tipo de Recolhimento seja "Retido na Fonte" ou "Retido na Fonte Deduzido";  
**<valor\_iss>**: Será preenchido com o somatório do Valor do Tributo ISS do Item de Movimento cujo tipo de Recolhimento seja "Retido na Fonte" ou "Retido na Fonte Deduzido";  
**<aliquota\_iss>**: Será preenchido de acordo com a Alíquota do Tributo ISS do Item de Movimento.
