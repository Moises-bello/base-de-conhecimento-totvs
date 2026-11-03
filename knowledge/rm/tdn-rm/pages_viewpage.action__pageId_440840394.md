---
content_hash: 83c68b82d580b910fa0048b345608da4d25a7bcf815d8522acc57ecbe67b2be5
fetched_at: '2026-06-29T00:09:53.525204+00:00'
page_id: '440840394'
product: rm
source: tdn-rm
title: Orçamento (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440840394
version: 15
---

O processo de Controle Orçamentário implica na utilização de técnicas e procedimentos financeiros aplicados antecipadamente aos fatos decorrentes de planos, políticas e metas para a consecução de um resultado desejado. Portanto, ao final do processo, são obtidos os demonstrativos financeiros preparados sob condições de premissas que se espera que aconteçam durante um determinado período.  
O Orçamento funciona como uma ferramenta que os gerentes podem usar para monitorar a evolução da empresa, comparando seus resultados reais com os esperados (ou planejados), permitindo que ações corretivas possam ser tomadas, caso sejam necessárias.   
Com isto, as decisões estratégicas para a correção dos rumos empresariais torna-se uma finalidade para a utilização do Controle Orçamentário.  
A utilização de um Controle Orçamentário pode ser analisada como um plano que contém as operações anuais da empresa, formalizando o desempenho das ações e funções administrativas, medindo quantitativamente estas operações e seus efeitos.   
Para tanto, é necessário o exame prévio, sistemático e cuidadoso de todos os fatores antes da tomada de decisões importantes, além de forçar a alta administração empresarial a dedicar atenção adequada e oportuna aos efeitos causados pelo surgimento de novas condições externas.  
Como benefícios do Controle Orçamentário, podemos citar:

1. Obriga os administradores a pensar à frente dos negócios;
2. Estabelece expectativas definidas, facilitando a análise posterior do desempenho;
3. Auxilia na coordenação dos esforços dos administradores, aumentando a eficiência do cumprimento dos objetivos.

Além disso, esta rotina no sistema TOTVS Gestão de Estoques, Compras e Faturamento possui a funcionalidade de realocação de valores orçamentários entre Centros de Custos.   
Isto significa que, caso o Orçamento de um Centro de Custos exceda seu valor total, o sistema permite que os valores de outros orçamentos possam ser 'transferidos' para este orçamento 'estourado', permitindo demais movimentações para este Orçamento.   
Neste cenário, o sistema bloqueia os movimentos que excedem o valor total do Orçamento até que este processo de [Realocação Orçamentária](http://tdn.totvs.com/pages/viewpage.action?pageId=423938874) seja realizado, desbloqueando este movimento para continuar seus processos.  
Existe também uma [Consulta aos Valores do Orçamento](http://tdn.totvs.com/pages/viewpage.action?pageId=423938207), modelada para permitir a busca por Centro de Custos, Períodos do Orçamento e Natureza Orçamentária/Financeira, agilizando completamente o processo de pesquisa das movimentações orçamentárias.  
Lembrando que alguns Cadastros específicos para o correto funcionamento do Controle Orçamentário, o sistema ainda possui um recurso de Importar o Orçamento, utilizando planilhas ou arquivos-texto. Isto facilita a integração com outras fontes de dados e com outros métodos de controle atualmente utilizados nas empresas.

**Parametrização**

**Editar Natureza Orçamentária/Financeira do item**

* Não Edita: Fica indisponível.
* Edita: se esta natureza deverá ser utilizada e informada no momento da inclusão do movimento.
* Edita Obrigatoriamente: a natureza deverá ser informada.
* Mostra: se esta deverá ser utilizada, mas não poderá ser editada.

***Observações**:*

1. 1. O movimento que será configurado para efetuar o Orçamento terá as seguintes consistências:
   2. Para Utilizar o Controle orçamentário por item, o campo "Não agrupar quantidades de itens iguais" deve ser marcado. Pasta integração Compras /Outras opções dos parâmetros do tipo de movimento.
   3. Para utilizar o controle orçamentário o centro de custo do item deve ser editado.
   4. Pasta Tabelas/Itens dos parâmetros do tipo de movimento.
   5. Quando o tipo de movimento estiver parametrizado para controlar orçamento, todos os parâmetros do Orçamento devem ser preenchidos.

**Controla orçamento**

Se o campo estiver marcado, os campos abaixo ficarão disponíveis.

**Efeito no Orçamento**

* Nenhum Efeito: Os movimentos deste tipo não terão nenhum efeito sobre o valor orçado.
* Aumenta Orçado: Os movimentos deste tipo aumentarão o valor do orçamento. É este que terá o seu valor controlado. Portanto, a opção "aumenta o orçado" geralmente é utilizada nos movimentos do tipo 4, pois, é através deste que serão informados os valores orçados e a partir dele é que o sistema faz o controle.
* Diminui o Orçado: Os valores de tipos de movimentos com esta opção, irão diminuir o valor orçado.
* Aumenta Realizado: O valor realizado é aquele que será comparado ao orçado para o controle do orçamento. Movimentos com este efeito sobre o orçamento aumentará o valor real e se este ultrapassar ao valor orçado, o sistema poderá avisar ou barrar a inclusão do movimento dependendo do que foi informado no campo "Efeito no Orçamento", exemplo:*:*

Vamos supor que o valor orçado de um movimento é 4.000,00, ao incluir um movimento de compra cujo efeito no orçamento é "Aumenta Realizado" no valor de 1.000,00 o sistema guardará

Valor Orçado     Valor Realizado 4.000,00           1.000,00

Se incluir outra compra no valor de 3.500,00 o sistema guardará:

Valor Orçado    Valor Realizado 4.000,00          4.500,00  
Caso esteja informado no campo "Ação ao exceder Orçamento" para avisar quando ultrapassar o valor orçado, o sistema emitirá uma mensagem que o valor está ultrapassado. Se parametrizou para barrar quando ultrapassar, o sistema irá barrar a inclusão do movimento e emitirá uma mensagem que o valor orçado foi ultrapassado.

**Ação ao Exceder Orçamento**

Quando um movimento for afetar o orçamento e não possuir verba suficiente para o valor solicitado, podem ser configuradas três ações sobre esse movimento:

* Avisa: Uma mensagem é emitida sobre o valor excedente do orçamento, e o movimento é criado com status "Pendente".
* Barra: Uma mensagem é emitida sobre o valor excedente do orçamento, e não permite salvar o movimento.
* Bloqueia: Uma mensagem é emitida sobre o valor excedente do orçamento, e o movimento criado com o status "Bloqueado". Com esse status o movimento fica aguardando que seja liberado pelo assistente de realocação orçamentário, e não pode ser recebido para outro tipo de movimento enquanto estiver bloqueado.

***Observação**:*: O controle orçamentário por tipo de movimento (controle financeiro) considera como valor orçado o "valor líquido" do movimento. No caso de controle orçamentário físico (por produto ou alguma tabela opcional) o valor orçado é definido pela "a quantidade x preço".

**Data Default do Orçamento**

* Data de Emissão: o campo será preenchido com a data de emissão do movimento.
* Data de Entrada/Saída: deverá ser igual a data de entrada/saída.
* Data Extra 1/2: Se desejar utilizar outras datas para algum outro controle, pode-se utilizar estas duas, os campos a preencher são os mesmos descritos acima em "Data de Entrada".

Exemplo*:*No movimento do tipo de "Ordem de Fornecimento", podemos criar uma data com o nome de "data orçamento", e parametriza para buscar esta data na data de emissão do movimento.

**Utiliza Rateio no Orçamento**

• Informe como será o rateio no orçamento. As opções são: Não utiliza, Utiliza no Movimento e Utiliza no Item.  
***Observações**:*

* + O sistema não permite a alteração do parâmetro que utiliza rateio se já tiver incluído algum movimento.
  + Se o usuário escolher que vai utilizar o rateio no orçamento, ele irá consistir se o parâmetro de rateio esta marcado.
  + O rateio do movimento pode ser por valor ou quantidade, o sistema irá fazer uma proporção da Quantidade X Valor Unitário do Orçamento (Fórmula) e irá aplicar no rateio selecionado.
  + Quando parametrizado para Utiliza no Movimento, o orçamento será afetado por uma combinação entre os centros de custo de movimento com as naturezas orçamentárias   
    de cada um dos itens.

**Fórmula do valor unitário do orçamento**

Informe a fórmula que irá calcular o valor unitário do orçamento.

---

Informações Adicionais

[Como Fazer - Controle Orçamentário](http://tdn.totvs.com/pages/viewpage.action?pageId=4813126)

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
