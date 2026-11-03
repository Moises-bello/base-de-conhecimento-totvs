---
content_hash: 004e51abc01f114961ba5aaa42d3d5d3b5af9a9b59f00b69e49f3c5ec1e2c6be
fetched_at: '2026-06-29T00:09:21.399423+00:00'
page_id: '422545880'
product: rm
source: tdn-rm
title: Conversão de Natureza de Operação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545880
version: 7
---

Através desta opção é possível associar aos Lançamentos Fiscais, às novas naturezas definidas no cadastro após a mudança do parâmetro "Natureza Global". Com este recurso, todos os lançamentos anteriormente incluídos, poderão ser alterados automaticamente, após a correta inclusão e manutenção dos novos códigos no Cadastro Naturezas Fiscais. É de extrema importância portanto, que as naturezas da nova tabela definida, após a mudança do parâmetro, contenha a mesma estrutura, configurações e dependências dos antigos códigos associados aos lançamentos.

*****Observações*:****Após a alteração do parâmetro "Natureza Global", o sistema irá considerar que será utilizada uma outra tabela de naturezas, que poderá ser por cada Filial/Exercício cadastrada ou a Filial Global(um cadastro utilizado para todas as Filiais/Exercício da coligada). Deste modo as naturezas utilizadas no antigo cadastro deverão ser incluídas, alteradas e/ou redefinidas na nova tabela.false***Atenção*:**O sistema consistirá somente as Regras de ICMS , Regras de IPI e o Tipo (entrada/saída). É importante observar que se a conversão for feita para naturezas que possuem características diferentes, os lançamentos criados e inicialmente relacionados com a Natureza Global terão inconsistências fiscais e isso poderá provocar diversos problemas no momento de apuração dos tributos ou na geração de alguma rotina, seja ela municipal, estadual ou federal.false

**Regras de Conversão de Natureza**

Ao se iniciar o processo de conversão de natureza, os seguintes dados serão requisitados:

**Exercício Fiscal:**Este campo é responsável pelo filtro das Naturezas de Operação Globais existente para a Coligada corrente.

**Filial:**Este campo é responsável pelo filtro das Naturezas de Operação não Globais.

**Natureza Global :**Tem como objetivo mostrar o atual estado do parâmetro referente à Natureza Global.  
Se o parâmetro de Natureza Global estiver habilitado no sistema para a coligada corrente este campo será apresentado marcado, caso contrário o elemento aparecerá sem marcação.

**Naturezas de Operação a Serem Convertidas:**este campo serão apresentadas todas as Naturezas de Operações a serem convertidas

**Naturezas para Converter:**Neste campo serão apresentadas as Naturezas que serão utilizadas para converter as naturezas apresentadas na tela Naturezas de Operação a serem convertidas.

**Relacionamento entre Naturezas Globais e Não Globais:**Neste campo serão apresentadas quais naturezas serão convertidas, e quais serão seus novos valores (nova natureza).   
Serão apresentadas quais naturezas foram relacionadas para realizar a conversão. Quando o botão "Associar Naturezas" for clicado o sistema identificará quais naturezas do campo Natureza de Operação a serem Convertidas foram selecionados e quais naturezas do campo Naturezas para Converter estão marcadas, de forma a relacionar cada natureza do primeiro campo com a natureza marcada no segundo campo.  
No momento em que uma natureza é associada a outra para a conversão a mesma é removida do campo Naturezas de Operação a Converter.  
Caso necessite alterar o relacionamento feito, será necessário que o mesmo remova a linha do relacionamento do Grid que a natureza voltará a ser apresentada no campo Naturezas de Operação a serem convertidas.

---
