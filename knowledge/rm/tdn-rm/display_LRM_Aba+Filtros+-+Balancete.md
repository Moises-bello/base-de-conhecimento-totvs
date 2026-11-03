---
content_hash: 4a3ed44153d3ed73df02233cadf8741fc5fd271b2e4752009112c626afd60409
fetched_at: '2026-06-29T00:09:27.534055+00:00'
page_id: '423938536'
product: rm
source: tdn-rm
title: Aba Filtros - Balancete
type: documentation
url: https://tdn.totvs.com/display/LRM/Aba+Filtros+-+Balancete
version: 9
---

**Conta Contábil:** Permite emitir o relatório filtrando por uma ou mais contas CONTÁBEIS especificas e por faixas de contas (Ex: Da conta Contábil 1.1.1.1.001 até a conta Contábil 1.1.1.1.008).

**Conta Gerencial:** Permite emitir o relatório filtrando por uma ou mais contas GERENCIAS especificas e por faixas de contas (Ex: Da conta Gerencial 1.01 até a conta Gerencial 1.08).

**Centro de Custo:** Permite emitir o relatório filtrando por um ou mais Centros de custos específicos e por faixas de centro de custos (Ex: Do Centro de Custo 01 até a Centro de custo 08).

**Histórico:** Permite emitir o relatório filtrando por um ou mais Históricos Padrões. Os históricos selecionados podem ser considerados ou desconsiderados para a emissão do relatório, há uma opção disponibilizando tal flexibilidade.

**Grau Contábil:** Selecione na caixa de seleção o grau de contas desejado para geração do balancete. Esta opção estará disponível para os balancetes Contábil, Contábil/Gerencial, Gerencial/Contábil, Centro de Custo/Contábil, Contábil/Centro de Custo.

Exemplo:

* Grau TOTAL: Todas as contas serão selecionadas (do primeiro nível sintético até a última conta analítica do plano de contas).
* Grau 1: Somente as contas sintéticas dos grupos serão selecionadas, neste caso (1 - Ativo, 2 - Passivo etc.) conforme o plano de contas.

**Grau Gerencial:** Selecione, na caixa de seleção, o grau de Contas Gerenciais desejado para geração do balancete. Esta opção estará disponível para os balancetes Gerencial, Contábil/Gerencial e Gerencial/Contábil.   
   
**Tipo de Valor / Moeda:** Permite escolher o valor e/ou moeda que será utilizado para a impressão de seu relatório.

**Formatação:** Permite definir qual será o formato impresso no relatório. Padrão de data Americano ou Brasileiro e separador de milhar com vírgula ou ponto.

**Primeiro Valor:** Imprime o relatório utilizando o valor da moeda corrente.

**Segundo Valor:** Imprime o relatório utilizando o segundo valor cadastrado nos lançamentos.

**Cotação de Outra Moeda:** Marcando esta opção você poderá imprimir os relatórios utilizando a cotação de outra moeda, além da moeda principal e da segunda moeda. Desta forma você poderá escolher no ato da impressão em qual moeda seu relatório será impresso. Observação: Será possível selecionar apenas uma das moedas utilizadas nos processos contábeis multimoeda. Elas estão disponíveis na etapa Moedas dos parâmetros de sistema.

**Centro de Custo (Ativo/Inativo):** Permite ao usuário definir como filtro para o relatório o status do centro de custo, podendo ser ATIVO, INATIVO ou TODOS. Sendo assim serão considerados os registros onde o status do centro de custo for compatível com o filtro definido pelo usuário. Observação: Este campo não está visível quando o tipo do Relatório for Gerencial.

**Conta Contábil (Ativa/Inativa):** Permite ao usuário definir como filtro para o relatório o status das contas contábeis, podendo ser ATIVO, INATIVO ou TODOS. Sendo assim serão considerados os registros onde o status da conta for compatível com o filtro definido pelo usuário. Observação: Este campo não está visível quando o tipo do Relatório for Gerencial.
