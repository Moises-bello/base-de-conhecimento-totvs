---
content_hash: 7fcc3984a07fb0afba2c4baaeaf351c146d6eb91985087cc4c66e81db8fe68b8
fetched_at: '2026-06-29T00:09:28.531383+00:00'
page_id: '423938699'
product: rm
source: tdn-rm
title: Relatório Balancete - Etapa Tipo de Balancete e Filtros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938699
version: 2
---

Nesta pasta serão informados os dados necessários à configuração do Balancete.

**Data inicial e Data Final**

Informe a faixa de datas desejada para a impressão do Balancete. Estas datas poderão estar dentro do Período Contábil vigente ou não, basta que para uma data anterior ao período, seja marcada a opção "Buscar do Histórico contábil".

O campo data será carregado automaticamente com a última data informada no Relatório, salvo nas preferências.

Ao lado do campo data, que pode ser utilizado a opção "filtro automático de datas" que possibilita retornar os períodos fixos (Semanal, Mensal, Bimestral, Trimestral, Semestral, Anual) e aplica-lo como período do Balancete.

**Buscar do Histórico Contábil**

Esta opção permite a impressão do Relatório Balancete baseando o resultado em datas anteriores ao período contábil. Desta forma deve ser informado uma data que seja anterior ao inicio do período contábil. ( Exemplo: Período Contábil = 01/01/2009 á 31/12/2013. A data a ser informada deve ser inferior a 31/12/2008.)

**Basear na Data de Cotação**

Esta opção permite a impressão dos valores baseando na data da cotação dos lançamentos. Marcando esta opção, o sistema buscará os lançamentos que possuírem a data da cotação dentro do período informado no intervalo de datas.

Observação: Esta opção somente será visualizada nesta janela, se nos "Parâmetros/Lançamentos" a opção "Usa segundo valor" estiver marcada e for informada uma moeda no parâmetro "Símbolo moeda 2º valor".

**Tipo Balancete**

Para emissão do balancete, deve ser escolhido um tipo para o mesmo dentre as opções a seguir:

* **Contábil:** Processamento do relatório por saldo da conta contábil.
* **Gerencial:** Processamento do relatório por saldo gerencial.
* **Contábil/Gerencial:** Processamento do relatório por saldo da conta contábil, quebrando por saldo gerencial.
* **Gerencial/Contábil:** Processamento do relatório por saldo gerencial, quebrando por saldo da conta contábil.
* **Contábil/Centro de Custo:** Processamento do relatório por saldo da conta contábil, quebrando por saldo de Centro de Custo.
* **Centro de Custo/Contábil:** Processamento do relatório por saldo de Centro de Custo, quebrando por saldo da conta contábil.

**Grau**

**Grau Contábil**

Selecione na caixa de seleção o grau de contas desejado para geração do balancete. Esta opção estará disponível para os balancetes Contábil, Contábil/Gerencial, Gerencial/Contábil, Centro de Custo/Contábil, Contábil/Centro de Custo   
   
Exemplo:

* **Grau TOTAL:** Todas as contas serão selecionadas (do primeiro nível sintético até a última conta analítica do plano de contas).
* **Grau 1**: Somente as contas sintéticas dos grupos serão selecionadas, neste caso (1 - Ativo, 2 - Passivo etc.) conforme o plano de contas.

**Grau Gerencial**

Selecione, na caixa de seleção, o grau de Contas Gerenciais desejado para geração do balancete. Esta opção estará disponível para os balancetes Gerencial, Contábil/Gerencial e Gerencial/Contábil.  
   
**Definir /Filtrar por:**

* **Conta Contábil:** Permite emitir o relatório filtrando por uma ou mais contas CONTÁBEIS especificas e por faixas de contas (Ex: Da conta Contábil 1.1.1.1.001 até a conta Contábil 1.1.1.1.008).
* **Conta Gerencial:** Permite emitir o relatório filtrando por uma ou mais contas GERENCIAS especificas e por faixas de contas (Ex: Da conta Gerencial 1.01 até a conta Gerencial 1.08).
* **Centro de Custo:** Permite emitir o relatório filtrando por um ou mais Centros de custos específicos e por faixas de centro de custos (Ex: Do Centro de Custo 01 até a Centro de custo 08).
* **Histórico Padrão:** Permite emitir o relatório filtrando por um ou mais Históricos Padrões

**Tipo de Valor / Moeda:** Permite escolher o valor e/ou moeda que será utilizado para a impressão de seu relatório.

* **Primeiro Valor:** Imprime o relatório utilizando o valor da moeda corrente.
* **Segundo Valor:** Imprime o relatório utilizando o segundo valor cadastrado nos lançamentos.
* **Cotação de Outra Moeda:** Marcando esta opção, você poderá imprimir os relatórios utilizando uma cotação específica de uma outra moeda, além da moeda principal e da segunda moeda. Desta forma você poderá escolher no ato da impressão em qual moeda seu relatório será impresso, e qual o valor da cotação.

**Observação:** Você deverá informar qual a moeda desejada e qual o valor da cotação, pois o sistema utilizará uma cotação única nesta opção e todos os valores apresentados no relatório serão convertidos com base no valor informado neste campo.

**Lote:**

Permite emitir o relatório Balancete filtrando por um lote diferente do Lote 0. Desta forma é possível preencher o campo com o código de um lote existente no cadastro de lotes. Para emitir para os lançamentos que já estão integrados basta informar o lote 0. Caso deseje emitir o relatório para um lote especifico basta inserir o código do mesmo.  
   
**Centro de Custo (Ativo/Inativo):**

Permite ao usuário definir como filtro para o relatório o status do centro de custo, podendo ser ATIVO, INATIVO ou TODOS. Sendo assim serão considerados os registros onde o status do centro de custo for compatível com o filtro definido pelo usuário.

**Observação:** Este campo não está visível quando o tipo do Relatório for Gerencial.

**Conta Contábil (Ativo/Inativo):**

Permite ao usuário definir como filtro para o relatório o status das contas contábeis, podendo ser ATIVO, INATIVO ou TODOS. Sendo assim serão considerados os registros onde o status da conta for compatível com o filtro definido pelo usuário.

**Observação:** Este campo não está visível quando o tipo do Relatório for Gerencial.
