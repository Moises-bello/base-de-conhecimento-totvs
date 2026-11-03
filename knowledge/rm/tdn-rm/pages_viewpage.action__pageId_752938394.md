---
content_hash: dfa7c02942f6ee37e5a90500f796fc09bb1764beadac184c96763f4bdcd3214b
fetched_at: '2026-06-29T00:11:33.188837+00:00'
page_id: '752938394'
product: rm
source: tdn-rm
title: Relatórios - Posição de Estoque - Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=752938394
version: 10
---

Este relatório apresenta a **Posição de Estoque** das subunidades dos empreendimentos selecionados, com a situação e os valores destas subunidades.

Importante!

Para ter acesso a este relatório, é preciso que o Perfil do usuário tenha acesso à opção: *[01.02.01] - Empreendimento*, sem necessidade de dar permissões de acesso aos níveis abaixo deste.

Ao acessar este relatório no Smart View é possível de se aplicar os seguintes *Parâmetros de Visualização*:

* **Código da Coligada:** Neste parâmetro é possível de se filtrar as Coligadas, onde o valor padrão *-1*, processa todas as coligadas e caso o usuário queira filtrar uma ou mais coligadas específicas, pode-se realizar esta ação alterando este valor e/ou acrescentando as demais coligadas, através do botão "+" localizado em frente à descrição do mesmo;
* **Código do Empreendimento:** Neste parâmetro é possível de se filtrar o Código do Empreendimento, onde o valor padrão -1, processa todos os empreendimentos e como ocorre com o parâmetro da entidade acima, caso o usuário tenha necessidade, pode-se filtrar um ou mais empreendimentos específicos através dos botões destinados a este fim;

Importante!

Para a geração dos dados deste relatório, as subunidades devem estar associadas a uma [Tabela de Preço](https://tdn.totvs.com/pages/viewpage.action?pageId=435105236) do tipo Principal e em situação Efetivada.

Após definir estes parâmetros e gerar o relatório, o sistema apresentará as seguintes informações:

* Agrupador **Consolidado**: É um totalizador com um resumo das informações de todas as coligadas e empreendimentos selecionados, com as seguintes colunas:
  + **Empreendimento:** É apresentado o Código do [Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154) e o seu Nome de Fantasia.
  + **Número de Unidades:** É a quantidade total de unidades/blocos/quadras, da aba de Informações do empreendimento;
  + **Número de Subunidades:** É a quantidade total de subunidades/apartamentos/quadras, do empreendimento;
  + **Área Média:** É a soma da *área total(m²)*, dividido pela *quantidade de subunidades* dos empreendimentos;
  + **Preço Total:** É a soma dos valores das subunidades, de todos os empreendimentos filtrados no relatório, cadastrados na *tabela de preço*;
  + **Preço Médio:** É o *Preço Total*, citado acima, divido pelo *Número de Subunidades*, citado anteriormente;
  + Detalhe de **Situação das Subunidades**: É um resumo, de acordo com a situação das subunidades, com as informações abaixo:
    - **Situação:** É apresentada a situação das subunidades dos empreendimentos filtrados (reservada, disponível para venda, vendida, etc.);
    - **Quantidade:** É a quantidade de subunidades nesta situação;
    - **Valor Total:** É o preço total das subunidades nesta situação;

* Agrupador **Empreendimento**: São apresentadas os detalhes das informações das subunidades de cada um dos empreendimentos filtrados:

* + **Código e Nome:** São detalhados o código e o nome do empreendimento;
  + **Custo da Obra:** É o custo da obra que é cadastrado no campo de mesmo nome, na aba de [Informações](https://tdn.totvs.com/pages/viewpage.action?pageId=435105074) do empreendimento;
  + **Custo Total:** É o custo total cadastrado no campo de mesmo nome, na aba de Informações do empreendimento;
  + **Custo por M³:** É o custo por m² cadastrado no campo de mesmo nome, na aba de Informações do empreendimento

Além das informações acima, neste agrupador também são exibidas as informações sobre o **Número de Unidades**, **Número de Subunidades**, **Área Média**, todas detalhadas e sumarizadas por empreendimento.

* + Detalhe de **Subunidades**: Em relação às subunidades, são exibidas as informações abaixo:
    - **Unidade:** É o código identificador da [unidade](https://tdn.totvs.com/display/LRM/Empreendimento+-+Anexos+-+Unidade) do empreendimento detalhado no agrupador de Empreendimento;
    - **Subunidade:** É o código identificador da [subunidade](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade) do empreendimento;
    - **Situação da Subunidade:** É a *situação para venda*, da subunidade no momento de geração deste relatório;
    - **Área:** É a *área m²* cadastrada na aba [Dimensões/Áreas](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade), desta subunidade;
    - **Fração Ideal:** É a fração ideal cadastrada na aba de Identificação desta subunidade;
    - **Preço:** É o preço definido para esta subunidade na [Tabela de Preço](https://tdn.totvs.com/pages/viewpage.action?pageId=435105236);
    - **Valor da Venda:** É o valor da venda desta subunidade, caso ela esteja associada a um contrato de venda ativo. Caso ela não esteja associada a nenhum contrato de venda ativo, este valor será igual a zero;
