---
content_hash: 39a0c618b9cabaa92d26dec0263d40c24b4c3417d90c6344b4235a0a95079980
fetched_at: '2026-06-29T00:10:33.335530+00:00'
page_id: '528472830'
product: rm
source: tdn-rm
title: Designer
type: documentation
url: https://tdn.totvs.com/display/LRM/Designer
version: 67
---

# Páginas Filhas:

---

# Índice:

---

[^Páginas Filhas://Índice:].\*

# Objetivo:

---

       O objetivo desta página tem por finalidade demonstrar as ferramentas e funcionalidades da etapa Design do TReports.

# Introdução:

---

       Os relatórios criados no TReports, permitem apresentar informações em suas bandas de detalhe sem complexidade, permitirá exportar seus dados para os formatos mais populares, além de personalizar a aparência dos elementos do seu relatório.

       Na etapa Designer, utilizamos estes elementos e suas propriedades para criar os mais variados tipos de relatórios e forma prática e ágil.

# Designer:

---

       Para acessar a visão do designer de um determinado relatório, no menu “Relatórios”, clique na opção de reticencias de um dos registros na tela listados. Escolha dentre as opções “Estrutura”. O sistema irá carregar novas opções de menu e a de Designer ficará disponível na última opção.

       Ao acessar esse menu o sistema irá carregar a visão do Designer. Para melhor explicarmos suas funcionalidades vamos dividir essa visão em três partes: Barra de Controles, Layout e Barra de Propriedades.

Membro de Dados

Para que todas as informações sejam trazidas ao gerar um relatório, é necessário informar o Membro de Dados nas Propriedades do Relatório.

falseDesigner1Barra de Controlesslide

       Localizado na lateral esquerda da tela a barra de controles predispõe de vários controles que serão abordados em outras páginas. Para uso destes controles basta selecionar o controle desejado e arrastar para área do layout.

2Layoutslide

       Na área de layout utilizamos os controles e suas propriedades para construir os relatórios. Um relatório em branco contém as seguintes bandas:

* A banda **detalhes** (**Detail 1**) será impressa para cada registro de uma fonte de dados, a menos que se tenha filtrado os dados.

 *Todo relatório contém a banda detalhes e essa não poderá ser excluída.*

* As bandas **Margem Superior** (**TopMargin 1**) e **Margem Inferior** (**BottomMargin 1**) serão repetidas em todas as páginas do relatório.

       Também podem ser adicionadas as seguintes bandas:

* **Cabeçalho** (**ReportHeader**) e **Rodapé do Relatório** (**Report Footer** )

       O cabeçalho do relatório é a primeira banda do relatório. Use-a para exibir o nome do relatório, logotipo da empresa, data de criação, nome de usuário etc.

       O rodapé do relatório é colocado antes do rodapé da página e da margem inferior na última página do relatório. Utilize a banda Rodapé do relatório para resumos ou conclusões de relatórios.

* **Cabeçalho da página** (**Page Header**) e **rodapé da página** (**Page Footer**)

       Essas bandas estão na parte superior e inferior de todas as páginas de um relatório. Elas exibem informações que devem ser impressas em todas as páginas.

* **Cabeçalho** (**Group Header**) e **rodapé do grupo** (**Group Footer**)

       Essas bandas estão acima e abaixo de cada grupo. O grupo e o painel de classificação criam essas bandas automaticamente.

*Somente as faixas de detalhes e grupos podem ser usadas para exibir o conteúdo dinâmico da fonte de dados. Outras bandas exibem títulos, resumos e informações extras .*

*As imagens a seguir ilustram exemplos de layout de relatório e o que reflete a estrutura do relatório:*

Gerenciar bandas do relatório1Ocultar bandas no layout

       Para ocultar uma banda no seu relatório basta selecionar a banda que deseja ocultar e clicar novamente após a banda selecionada, note que a banda receberá uma coloração cinza. Para habilitar novamente basta novamente sobre a banda.

 *Lembrando que essa opção apenas oculta a banda na área do layout. Os dados manipulados pela banda continuam valendo e continuaram sendo impressos.*

*As bandas que são sub-bandas do grupo que foi oculto, também serão ocultados automaticamente.*

2Ocultar bandas no relatório

       Para ocultar uma banda no relatório selecione primeiramente a banda que deseja ocultar. Em seguida selecione as propriedades dessa banda e expanda a opção “Comportamento”, desmarque a opção “Visível”.

 *Lembrando que essa opção não ocultará a banda na área do layout e seus dados continuaram valendo, , porém não serão impressos.*

3Remover bandas

       Selecione uma banda na superfície de layout do relatório e pressione DELETE. Isso removerá a banda e todo o seu conteúdo.

       Ou

       Selecione uma banda na superfície do layout do relatório e clique no ícone de exclusão localizado na parte superior da área do layout.

Adicionar bandas

       Para adicionar novas bandas ao relatório selecione a banda que fara associação a nova banda. No exemplo associamos a banda detalhe um cabeçalho do detalho e um rodapé do detalhe.

3Barra de Propriedadesslide

       Localizada na lateral direta da tela a barra de propriedades predispõe de várias propriedades conforme o controle ou parte do layout do relatório selecionado. Costa na barra, também, os dados das [entidades](https://tdn.totvs.com/x/viGTEg) cadastradas para esse relatório entre outras opções.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.23 ou superiores

false

**Processo:** Designer

falsefalse

**Status:** Em Construção

false

**Data:**

false

**Autores:**
