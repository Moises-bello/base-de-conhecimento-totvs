---
content_hash: 4d2fc319596010dfee45e0b4c39a9d9fe72b9ccc1fdc70565054b12613104dd1
fetched_at: '2026-06-29T00:09:28.698936+00:00'
page_id: '423938759'
product: rm
source: tdn-rm
title: Registro Bloco K280 (Estoque)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938759
version: 3
---

A geração do Bloco K280 é realizada no TOTVS Gestão de Estoque, Compras e Faturamento através de movimentações de correções de apontamento do estoque escriturado.   
Essa correção de apontamento é necessária pois dependendo da natureza física dos produtos pode ocorrer diferenças no estoque, pois as vezes a quantidade não pode ser medidas com precisão.   
Então essas correções poderão ser efetuadas no registro K280 – Correção de Apontamento – Estoque Escriturado que visa escriturar a correção de apontamento de estoque escriturado, de período de apuração anterior escriturado no registro K200 – Estoque Escriturado e esses ajustes podem ser realizados para produtos estocados, sejam eles produtos acabados, insumos ou material de embalagem.  
No TOTVS Gestão de Estoque, Compras e Faturamento o registro K280 será gerado a partir de movimentos de ajuste positivo ou negativo do saldo atual, saldo do estoque com terceiros ou saldo de terceiros em poder da empresa.   
Para que o tipo de movimento possa gerar o registro do bloco K280, na etapa 61 - Fis Dados foi criado o parâmetro SPED Fiscal onde no campo Data para Registro K280 o usuário possa escoher as seguintes opções:

* Não usa;
* Data Emissão;
* Data Extra 1;
* Data Extra 2.

***Observação***: Se a opção for Não usa, os movimentos gerados não irão gerar registro para o bloco K280 no SPED. Caso a opção seja preenchida com alguma das outras opções, a mesma deve está habilitada no movimento para seu preenchimento na inclusão do mesmo e assim possibilitar a geração de registro para o bloco K280 no SPED.  
Algumas consistência serão feitas pelo sistema ao parametrizar e incluir movimentos para geração do bloco k280. São elas:

* Por default o campo não virá preenchido
* Como o movimento que gera o Registro K280 pode afetar não só o saldo atual, como também o saldo de estoque de terceiros ou o saldo de estoque com terceiros, foi criado o Tipo de Controle de Estoque de Terceiros Ajuste Ref. Correção Apontamento - Estoque Escriturado na etapa 41 - Estoque - Estoque.
* A data selecionada para ser a data do Registro K280 não pode estar parametrizada como "Data do Movimento Default" na Etapa 4 - Mov - Datas 1/2, já que a data do movimento é a data em que o estoque será realmente afetado;
* O tipo de movimento deverá obrigatoriamente afetar, aumentando ou diminuindo, pelo menos um dos seguintes saldos: Saldo Atual, Saldo de Terceiros e Saldo com Terceiros (TITMTMV.EFEITOCOMTERCEIROS);
* O Tipo de Controle de Estoque de Terceiros somente poderá ser de "Ajuste ref. Correção Apontamento - Estoque Escriturado" caso a "Data para Registro K280" esteja preenchida com uma das datas disponíveis, caso contrário esse tipo de controle não poderá ser utilizado.
* Movimentação: - A data configurada como "Data para Registro K280" não poderá estar em branco;
* A data configurada como "Data para Registro K280" tem que ser de meses anteriores à "Data do Movimento" - Caso o movimento esteja afetando o Saldo de Terceiros ou o Saldo com Terceiros, o preenchimento do cli/for ou do cli/for origem/destino deve ser obrigatório devido à informação do código do participante (consistência já efetuada pela rotina que controla o estoque de terceiros);
* Campo Situação da Mercadoria (TPRDFISCAL.SITUACAOMERCADORIA) de todos os itens constantes do movimento tem que estar preenchido com um dos conteúdos: Mercadoria para Revenda, Matéria-Prima, Produto em Processo, Produto Acabado, Embalagem, Subproduto, Produto Intermediário e Outros insumos.
* Podem existir tipos de movimento que estejam parametrizados para afetar ao mesmo tempo o Saldo Atual e o Saldo com Terceiros

Informações Adicionais

[Bloco K - Registro K280](http://tdn.totvs.com/display/LRM/270950+MCP-1360+ER+Bloco+K+-+Registro+K280)
