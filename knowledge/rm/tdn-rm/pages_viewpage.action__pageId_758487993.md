---
content_hash: 84ea36b3e6e458c159e7724b7b51db437ba4565ba890279f82fa318f03af2554
fetched_at: '2026-06-29T00:11:33.382471+00:00'
page_id: '758487993'
product: rm
source: tdn-rm
title: Relatório - Taxa de Ocupação dos Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=758487993
version: 7
---

## **Introdução**

---

O Relatório de **Taxa de Ocupação dos imóveis** tem como objetivo apresentar informações sobre a taxa de ocupação dos imóveis de uma ou mais coligadas, durante um período determinado.

Com os parâmetros de visualização, é possível filtrar e personalizar a exibição dos dados de acordo com a necessidade do usuário.

O relatório oferece informações consolidadas sobre o número total de imóveis, bem como a média de tempo em que eles estavam locados, vagos ou indisponíveis durante o período filtrado.

Além disso, é possível verificar informações detalhadas por coligada, incluindo códigos e descrições de imóveis e áreas, tempo locado, vago e indisponível para cada um deles.

Este relatório pode ser útil para gestores imobiliários ou proprietários que desejam acompanhar a ocupação de seus imóveis e identificar oportunidades para otimização da ocupação ou negociação de contratos de locação.

## **Procedimentos para utilização**

---

Este relatório pode ser acessado em Aluguel / Relatórios / SmartView. Este menu possui permissão, então o usuário deve ter a sua respectiva permissão habilitada para utilizá-lo.

Ao acessar este relatório é possível de se aplicar como filtro o *Parâmetro de Visualização* abaixo:

* **Código da Coligada:** Neste parâmetro é possível de se filtrar as Coligadas, onde o valor padrão -1, processa todas as coligadas e caso o usuário queira filtrar uma ou mais coligadas específicas, pode-se realizar esta ação alterando este valor e/ou acrescentando as demais coligadas, através do botão "+" localizado em frente à descrição do mesmo;
* **Início Ocupação:** Este parâmetro permite ao usuário especificar a data que será utilizada para o início do período da coleta dos dados; e
* **Fim Ocupação:** Este parâmetro permite ao usuário especificar a data que será utilizada para o fim do período da coleta dos dados.

Após definir estes parâmetros e gerar o relatório, o sistema apresentará as seguintes informações:

* **Consolidado** com as seguintes informações dos imóveis de todas coligadas selecionadas

* + **Número Total de Imóveis:** É a quantidade de Imóveis e Áreas existentes na base, no Período de Ocupação aplicado nos parâmetros acima;
  + **Média do Tempo Locado (Meses):** É a média de meses em que os imóveis filtrados no Período de Ocupação estavam associados a um [*Contrato de Locação*](https://tdn.totvs.com/pages/viewpage.action?pageId=520659123).

Esta informação é obtida pela soma do *Tempo Locado (Meses)*, dividido pela soma da quantidade de imóveis filtrados no período de ocupação;

* + **Média do Tempo Vago (Meses):** É a média de meses em que, os imóveis filtrados estavam vagos, ou seja, não estavam associados a nenhum Contrato de Locação e nem a um [*Período de Indisponibilidade do Imóvel*](https://tdn.totvs.com/pages/viewpage.action?pageId=435105363).

Esta informação é obtida pela soma do *Tempo Vago (Meses)*, dividido pela soma da quantidade de imóveis filtrados no período de ocupação;

* + **Média do Tempo Indisponível (Meses):** É a média de meses em que, os Imóveis ou Áreas filtrados estavam com um Período de Indisponibilidade cadastrado e não estavam associados a nenhum Contrato de Locação.

Esta informação é obtida pela soma do *Tempo Vago (Meses)*, dividido pela soma da quantidade de imóveis filtrados no período de ocupação.

* Detalhamento **Coligada**: Nesta seção são detalhadas as informações abaixo, dos Imóveis e suas Áreas, por Coligada:

* + **Código do Imóvel:** É a informação do campo **Imóvel**, da aba Identificação do cadastro de Imóvel;
  + **Descrição do imóvel:** É a informação do campo **Descrição Imóvel**, da aba Identificação do cadastro de Imóvel;
  + **Código da Área:** É a informação do campo **Código**, da aba Identificação do cadastro de [*Área do Imóvel*](https://tdn.totvs.com/pages/viewpage.action?pageId=435105057). Este anexo só é habilitado quando o Imóvel tem o *Tipo de Locação* por *Área Fracionada*;
  + **Descrição da Área:** É a informação do campo **Descrição**, da aba Identificação do cadastro de Área do Imóvel;
  + **Tempo Locado:** É o tempo em meses em que, o Imóvel ou Área filtrados no Período de Ocupação, estava associado a um Contrato de Locação; Veja mais detalhes sobre como essa informação é tratada no item *Importante*, ao final desta página;
  + **Tempo Vago:** É o tempo em meses em que, o Imóvel ou Área filtrados ficou vago, ou seja, não estava associado a nenhum Contrato de Locação e nem a um Período de Indisponibilidade;
  + **Tempo Indisponível:** É o tempo em meses em que, o Imóvel ou Área filtrado estava com um Período de Indisponibilidade cadastrado e não estava associado a nenhum Contrato de Locação.

Importante!

As informações acima são tratadas considerando as Regras abaixo:

* **Período de Ocupação** (*Início* e *Fim Ocupação*): Esta informação que é definida nos *Parâmetros de Visualização* deste relatório, será usada como data de início e data de corte para o cálculo dos meses de ocupação.

Portanto caso um Imóvel ou Área esteja em alguma das situações tratadas acima (Locado, Vago e Indisponível) em um período esteja fora ou que intercale com o Período de Ocupação filtrado, o sistema considerará somente o tempo que coincide com o deste filtro e não apresentará as informações fora do mesmo.

Exemplo: Se um Imóvel está associado a um Contrato de Locação com Data de Início de Vigência em 01/01/2020 e Data de Prorrogação até 01/01/2023 e o usuário aplicar um Período de Ocupação de 01/01/2022 até 01/01/2023, este relatório irá apresentar que este Imóvel está locado por apenas 12 meses e não por 36 meses.

* **Data de Cadastro** do Imóvel: Esta informação, que é definida no campo de mesmo nome, da aba Identificação, do Imóvel é utilizada como referência para indicar que um objeto de contrato está disponível para uso.

A *Data de Cadastro* do Imóvel será suprimida pela data de *Início Vigência* do Contrato de Locação, quando o Imóvel ou Área em análise, for associado a um Contrato de Locação, com uma data de Início de Vigência anterior à ela. Ou seja, em um cenário em que o Imóvel ou Área estiverem locados antes da data informada neste campo.

Exemplo: Caso um Imóvel que tenha uma *Data de Cadastro* em 01/01/2023 esteja associado a um Contrato de Locação com data de *Início Vigência* em 01/01/2020, o sistema irá considerar que este Imóvel existe e está disponível para uso desde *01/01/2020* e não somente a partir de 01/01/2023.

Este cenário pode ocorrer em contratos de sistemas legados.

* Data de **Início Vigência**: Esta informação, que é definida no campo de mesmo nome na aba Identificação do Contrato de Locação, é utilizada como base para se determinar o início do período de locação dos Imóveis e Áreas;

* **Data Início** do *Período de Indisponibilidade do Imóvel*: Esta informação, que é definida no campo de mesmo nome do anexo de *Período de Indisponibilidade do Imóvel*, é utilizada para determinar o tempo em que esta entidade ficou indisponível para locação.

Em cenários em que um Imóvel ou Área estão associados a um Contrato de Locação e há um *Período de Indisponibilidade* cadastrado intercalando com a Vigência de um Contrato de Locação, ou seja, o objeto deste contrato foi indisponibilizado durante a sua locação, o sistema irá considerar este imóvel como locado e não como indisponível para locação.

Um exemplo na prática: se um imóvel está associado a um Contrato de Locação com vigência entre 01/01/2020 e 01/01/2023, mas precisou passar por uma reforma e, por esse motivo, foi cadastrado um Período de Indisponibilidade que vai de 01/02/2020 até 01/04/2020, o sistema considerará que, apesar deste imóvel estar sendo reformado por 2 meses, ele continua locado por um período total de 36 meses e não apresentará nenhum tempo de indisponibilidade para o mesmo.
