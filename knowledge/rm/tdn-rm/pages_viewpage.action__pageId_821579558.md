---
content_hash: 0695919e8144f5be6bf09c6183b04e4500b7c83d497e71218dfadb51f64e6be0
fetched_at: '2026-06-29T00:11:45.794507+00:00'
page_id: '821579558'
product: rm
source: tdn-rm
title: Fatos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821579558
version: 4
---

Fatos Contábeis são as linhas horizontais que serão apresentadas no relatório.

DMPL / DLPA

O sistema identifica a conta correspondente na coluna da DMPL ou DLPA através do Fato Contábil, com a parametrização da Origem do valor igual a "Saldo Anterior", ou seja, tanto na DMPL ou DLPA devemos ter um fato contábil que vai representar o saldo inicial e as devidas parametrizações nas respectivas colunas. Confira os .

**Cadastro de Fatos Contábeis:**

**Campo Código:**O campo de código do fato contábil, é o número que irá aparecer ao gerar a demonstração. Caso haja máscara, esse campo deverá preenchido de acordo com ela.

**Campo Grau:** Existem três tipos de Graus, sendo eles: 

**Sintético:** Quando um fato é sintético, ele funciona apenas com o tipo "Totalizador", ou seja, somará valores.

Quando adicionado no topo de uma hierarquia, irá somar todos seus filhos, por exemplo:

Nesse caso, o fato de código "01", totalizará todos valores de 01.01 até 01.05.

Quando adicionado ao final de uma hierarquia, irá somar todos os valores acima, por exemplo: 

Nesse caso, o fato de código "02.05", totalizará todos valores de "01" até "02.05".

**Analítico:**Quando um fato é Analítico ele pode possuir todos os tipos, sendo eles:

**Rótulo:** Quando um fato é Rótulo ele funciona como um texto livre, que será exibido na Demonstração Contábil.

**Campo Descrição:** Descrição será exibida ao executar a Demonstração Contábil.

**Campo Tipo:** tipo da linha a ser apresentada no relatório e de acordo com o campo **Grau**, sendo ele: 

**Fato Contábil:** parametrizável.

**Totalizador**: Funcionará como o sintético.

**SubTotal**: Que irá apresentar o mesmo comportamento do totalizador de topo de hierarquia, somando apenas valores de um mesmo grupo.

**Campo Número de Ordem no J150:**Este campo será utilizado para geração do campo 02 (NU\_ORDEM) do Registro J150 do SPED Contábil.   
Ele não interfere na ordenação dos Fatos Contábeis, nem na geração da Demonstração Contábil.

**Campo Imprimir em negrito:** Indicativo se tal linha no relatório será impressa/gerada em negrito, caso marcado, ou normal (sem negrito), caso desmarcado.

Atenção

Por padrão, apenas ao incluir um novo registro, ainda na tela de edição, o campo **Imprimir em negrito** virá marcado e será desmarcado apenas caso o usuário selecione para o campo **Tipo** o valor **Fato contábil**.

Isto é somente um facilitador, o usuário poderá alterar essa marcação conforme desejar.

**Notas Explicativas:** O layout 6.0 do SPED teve como principal novidade a inclusão do  campo NOTA\_EXP\_REF (Notas explicativas relativas às demonstrações contábeis.), o novo campo vai afetar três registros já existentes, sendo eles: J100 – Balanço Patrimonial, J150 – Demonstração dos Resultados e J210 - DLPA – Demonstração de Lucros ou Prejuízos Acumulados/DMPL – Demonstração de Mutações do Patrimônio Líquido. Para mais informações sobre notas explicativas, clique aqui.

**Observação:**

Na emissão do SPED Contábil, o usuário tem três opções para buscar informações para compor o registro J100 (Balanço Patrimonial):   
-Estrutura do Relatório DRE  
-A partir do Plano de Contas  
-Ferramenta das Demonstrações Contábeis: Caso o usuário opte por buscar as informações da Ferramenta de Demonstrações Contábeis é necessário que no cadastro da demonstração que será utilizada, o usuário cadastre o código do fato contábil iniciando com 1 caso represente o Ativo e com 2 caso represente o Passivo e Patrimônio Líquido. Isso é necessário para identificação do grupo para geração do arquivo da ECD e se informado de forma incorreta pode vir a dar alguma inconsistência quando validado no PVA do SPED.
