---
content_hash: 741ed38d4cf46579f047537a779d5fae316cf996acb883ae39da09b0f80278f4
fetched_at: '2026-06-29T00:10:36.152609+00:00'
page_id: '531029608'
product: rm
source: tdn-rm
title: Produtos Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531029608
version: 19
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Itens padronizados**
3. **Item especial**
4. **Baixa estoque**
5. **Baixa estoque KIT**
6. **Atenção**
7. **Tabela de preços**
8. **Tabela de preços por Fabricante**
9. **Atenção**
10. **Produtos associados**
11. **Classificação terapêutica**
12. **Classificação de medicamentos controlados**
13. ****Laboratórios Brasíndice****
14. ****Apresentações Brasíndice****
15. ****Quantidades de gotas em ML X Volume (ML)****
16. ****Parâmetro de Arredondamento****
17. ****Classificação Hierárquica do Produto****
18. ****Processo Atualização de múltiplas informações****

ProdutosSaudevisaoGeralVisão Geral

## **01. VISÃO GERAL**

Pasta Identificação  
Nesta tela são definidos os tipos de item para o produto, se o mesmo é controlado ou não, e qual opção será usada para saída do produto no estoque.  
Nesta tela são definidos ainda se os tipos de item para o produto são Padronizados ou não, e se são Itens Especiais ou não.  
Cód. TIPI: Os produtos que possuem código TIPI definido serão considerados produtos tipo "Alíquota Zero", conforme Lei 10.147/00 (Medicamentos Tributados). O RM Saúde possui um relatório específico para listagem destes itens (Estoques | Consultas e relatórios | Consumo de Medicamentos Alíquota Zero). Listará todos os medicamentos de "alíquota zero" que foram lançados na conta do paciente dentro do período informado. As colunas Vr. Unit., Quantidade e Vr. Total são os valores deste item na conta do paciente. As colunas COFINS, PIS e Total Impostos existem apenas no relatório e são calculados a partir do valor do item na conta e o percentual definido em parâmetros gerais | Estoques 2 | Medicamentos Tributados (Lei 10.147/00).

AbasProdutoSaudeIdentificação IIdentificação II

As configurações do medicamento que indicam se ele é classificado como **Vesicante**, **Irritante** ou de **Alta Vigilância** são utilizadas diretamente nos parâmetros da rotina de **Análise Farmacêutica**.

Essas classificações permitem aplicar regras específicas de validação, priorização ou tratamento diferenciado durante a análise, garantindo maior segurança e controle nos processos clínico-farmacêuticos.

itensPadronizadosItens Padronizados

## **02. ITENS PADRONIZADOS**

Usados para identificar qual o produto deve ser prescrito "preferencialmente". Na tela Pesquisa de Medicamentos o item padronizado é apresentado na cor verde. Isto ajuda o médico a identificar este medicamento dentre as demais opções. Ao clicar no botão OK da tela de "Pesquisa de Atendimentos ",se o item não for Padronizado o sistema exibirá a mensagem:"O item não é padronizado na instituição. Confirma o seu lançamento?".Na tela Pesquisa de Itens do Estoque este tipo de item também é destacado (existe uma coluna Padronizado = Sim/Não).

itemEspecialItem Especial

## **03. ITEM ESPECIAL**

 A princípio é um campo apenas informativo. Pode ser usado para identificar itens que possuem alto valor na tabela de preço do Convênio e que normalmente não são indexados no Brasindice e nem no SIMPRO. Para facilitar a inclusão de itens no cadastro das Condições Contratuais com Convênios, aba Coberturas, sub-pasta Restrições, existe um botão "Importa MATMED" esta tela permitirá selecionar apenas os itens especiais.

Se o produto for utlilizado no Prontuário Eletrônico, o parâmetro "Considerar no Sumário PEP" deverá ser marcado. A mesma regra vale para o parâmetro "Kit pré – montado", que deverá ser marcado se o item fizer parte de kits pré-montados.

baixaEstoqueBaixa Estoque

## **04. BAIXA ESTOQUE**

Define o comportamento padrão da movimentação de estoque quando este produto é incluído diretamente.

baixaEstoqueKitBaixa Estoque Kit

## **05. BAIXA ESTOQUE KIT**

Fez-se necessário a criação deste parâmetro para identificar o comportamento do (s) produto (s) quando este faz parte de um kit

Arredonda quantidade fracionada na movimentação de estoque: Ao marcar este parâmetro quando for criada uma Prescrição Médica e a quantidade total da mesma seja uma fração, será lançado na movimentação de estoque o proximo valor inteiro.  
Exemplo:  
Quantidade informada = 1,5 ou 1,2  
Lançado na Movimentação de Estoque quantidade = 2

atencaoFaturamentoAtenção

## **06. ATENÇÃO**

Na tela de Produto, quando for órtese ou prótese e na tabela de preço do produto um campo para informar o código do procedimento SUS referente a OPM. Esse campo somente aparece para tabelas de preço que estejam vinculadas a convênios que sejam SUS

* Na tela de Mov. Estoque, ao incluir um item OPM será realizado a pergunta se deve ser lançado na AIH. Para lançar escolher SIM.
* Na tela de Mov. Estoque, quando estiver selecionado no Grid um item OPM que tenha sido lançado automaticamente na AIH será  
  Apresentado um botão "AIH" onde será possível editar campos do procedimento sem ter que entrar na AIH.
* Na tela de Mov. Estoque, ao excluir um OPM que foi lançado diretamente na AIH ele também será excluido na AIH.  
  **Atenção**  
  Para que se possa alimentar o Livro de Medicamentos Controlados, para o cadastro do produto,na aba Classificação será necessario informar um item de Classificação previamente cadastrado.O cadastro é feito no RM Nucleus, em Cadastros / Tabelas de Classificação / Tipos.
tabelaDePrecosTabela de Preços

## **07. TABELA DE PREÇOS**

Para esse tópico, as informações estão disponíveis na página **Tabelas de Preços**.  Vá até **Informações TOTVS Saúde > Tabela de Preços > Incluir.**  
Inclua ou selecione uma tabela de preços já existentes e dê um duplo click para abrir a tela abaixo:

tabelaDePrecosTabela de Preços por Fabricante

## **08. TABELA DE PREÇOS POR FABRICANTE**

Possibilita cadastrar preços diferentes para a mesma tabela de preço de um produto especifico para fabricantes diferentes.

Com esse recurso o gestor de estoque não precisará realizar diversos cadastros de novos produtos por fabricantes, apenas cadastra preços e fatores diferentes.

Conforme imagem abaixo, é possível verificar que o produto possui vários preços cadastrados para a mesma tabela de preço, variando o fabricante.

O conceito e configuração é exatamente a mesma da tabela de preço já existente.

produtosAssociadosProdutos Associados

## **09. PRODUTOS ASSOCIADOS**

No anexo Produtos Associados é permitido fazer o cadastramento de outros Itens do Estoque que deverão ser cobrados automaticamente na Conta do Paciente, no momento em que for confirmada a requisição do Item no Estoque.

É possível configurar o produto associado para multiplicar a quantidade ou não com as opções:

* **Multiplica:** Neste cenário a quantidade do produto associado acompanhará a quantidade necessária para o item principal em cada aplicação.   
  Caso Prático: Cada ampola de dipirona possui como produtos associados uma agulha e uma seringa. Foram prescritas duas ampolas de dipirona, duas vezes ao dia.   
  Neste caso, deverão ser dispensadas 4 ampolas de dipirona + 4 agulhas + 4 seringas.
* **Consiste quant. por aplicação:** Neste cenário a quantidade do produto associado acompanhará a frequência de administração, não influenciando a dose do medicamento principal.   
  Caso Prático: Cada ampola de dipirona possui como produtos associados uma agulha e uma seringa. Foram prescritas duas ampolas de dipirona, duas vezes ao dia.   
  Neste caso, deverão ser dispensadas 4 ampolas de dipirona + 2 agulhas + 2 seringas.
* **Nenhuma das opções marcadas:** Neste cenário a quantidade do produto associado se relacionará apenas com o que foi cadastrado, não importando a dose do medicamento principal nem a frequência de administração.   
  Caso Prático: Cada ampola de dipirona possui como produtos associados uma agulha e uma seringa. Foram prescritas duas ampolas de dipirona, duas vezes ao dia.   
  Neste caso, deverão ser dispensadas 4 ampolas de dipirona + 1 agulha + 1 seringa.   
    
  **09.1 EXEMPLOS DE UTILIZAÇÃO**

Ao prescrever: MEDICAMENTO - 3 COMPRIMIDOS - 6 VEZES AO DIA e utilizar as opções no ASSOCIADO com QUANTIDADE 1 temos:

* **Multiplica**: VERDADEIRO, **Consiste quant. por aplicação:** VERDADEIRO- **Resultado:** 6 \* 1 = 6
* **Multiplica**: VERDADEIRO, **Consiste quant. por aplicação:** FALSO- **Resultado:** 3 \* 6 \* 1 = 18
* **Multiplica**: FALSO, **Consiste quant. por aplicação**: FALSO- **Resultado:** 1
classificacaoTerapeuticaClassificação Terapêutica

## **10. CLASSIFICAÇÃO TERAPÊUTICA**

**Informações TOTVS Saúde > Anexos > Classificação Terapêutica.**

A Classificação Terapêutica define e considera a composição química e as propriedades terapêuticas dos medicamentos, mas não incorporam variáveis relativas ao mecanismo de ação dos mesmos, seus efeitos colaterais, interações medicamentosas e contra-indicações.  
Classificação DCB  
A Classificação de Denominações Comuns Brasileiras (DCB) é uma nomenclatura de fármacos utilizada na comunicação entre os profissionais de saúde, tratamentos medicamentosos ou no registro de novos fármacos.  
As Denominações Comuns Brasileiras são utilizadas em registros de medicamentos, rastreamento de insumos e prescrição médica, entre outros.  
No Brasil a Lista de Denominações Comuns Brasileiras foi publicada na Portaria nº 1179/MS, de 17 de junho de 1996 (DCB 96).  
O endereço permanente da lista pode ser encontrado no site da Anvisa em "Áreas de Atuação">"Medicamentos">"Listas de  Medicamentos">"Denominações Comuns Brasileiras (DCB)  
Através desta funcionalidade você poderá cadastrar os nomes de fármacos utilizados pelo Hospital.  
Dose máxima e mínima da medicação  
Neste anexo do Produto onde serão definidos os valores máximo e mínimo por medicamento e unidade de faturamento. A unidade será filtrada pelas unidades que estão cadastradas nas tabelas de preço.  
Este cadastro será utilizado no PEP, quando o usuário gravar um item do tipo medicamento e que estejam definidos os valores máximo e mínimo de dose.

clasificassaoMedicamentosControladosClassificação de Medicamentos Controlados

## **11****. CLASSIFICAÇÃO DE MEDICAMENTOS CONTROLADOS**

Tela de cadastro das Listas de Classificação de Medicamentos Controlados. Através desta lista de Classificação os Medicamentos poderão ser agrupados conforme a necessidade de cada Hospital e das Exigências Legais aplicadas sobre substâncias e medicamentos sujeitos a controle especial (Portaria n.º 344, de 12 de maio de 1998). Os medicamentos tidos como controlados, devem ser classificados conforme o grau de perigo que o mesmo pode oferecer à saúde do paciente, caso seja usado indevidamente e sem um controle adequado.

laboratorioBrasindiceLaboratório Brasíndice

## **12. LABORATÓRIO BRASÍNDICE**

Nesta função cadastramos os laboratórios do BRASÍNDICE.  
Estes laboratórios também poderão ser importados para o sistema, através da rotina Importação / Atualização BRASÍNDICE (em Utilitários | Rotinas).

apresentacaoBrasindiceApresentação Brasíndice

## **13. APRESENTAÇÃO BRASÍNDICE**

Nesta função são exibidos os tipos de apresentações utilizados pelo padrão BRASÍNDICE.  
Os dados desta função são importados para o sistema, através da rotina Importação / Atualização BRASÍNDICE (em Utilitários | Rotinas).

quantidadeGotasQuantidade de Gotas em ML X VOLUMES (ML)

## **14.****QUANTIDADE DE GOTAS EM ML X VOLUMES (ML)**

Foram incluídos 3 grupos de unidade: um é para o médico definir a dosagem do medicamento de acordo com a concentração do mesmo, o outro é a dose calculada para a enfermagem e por fim a dose calculada para se fazer a requisição. Para se fazer o cálculo é necessário que o médico informe a dosagem e a unidade e utilizar um padrão de prescrição. Para esta funcionalidade foram criados novos campos no cadastro do item de estoque: "Volume (ml)" e "Qtd. de gotas em 1 ml". O volume é utilizado para saber quantos ml existem nos frascos/ampolas.

parametrosArredondamentoParâmetros de Arredondamento

## **15. PARÂMETROS DE ARREDONDAMENTO**

Quando marcados os parâmetros de arredondamento (indicados na imagem acima) após a conversão de unidades, as frações prescritas serão arredondadas para o próximo número inteiro.

classificacaoHierarquicaProdutoClassificação Hierárquica do Produto

## **16. CLASSIFICAÇÃO HIERÁRQUICA DO PRODUTO**

Classifica o produto em Tipo, Categoria, Classe e Família.

Utilizado para valorização do produto de forma personalizada de acordo com a classificação hierárquica.

Atualização de Múltiplas Informações

Este processo tem a funcionalidade de replicar as informações fornecidas na tela para todos os registros selecionados.  
Caso o vínculo com o Brasíndice ou Simpro seja alterado, a atualização de valores será executada para pegar o preço correto.  
Ao final do processo, todas as tabelas selecionadas ficarão com as mesma configurações e o preço poderá ficar com o valor de acordo com a importação da Revista de cada tabela.
