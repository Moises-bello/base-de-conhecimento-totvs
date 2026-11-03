---
article_id: 38191491592855
category: Materiais - Compras (SIGACOM)
content_hash: 46e3aa3fc717c1866d052b88c7708ef9dda344637ae11f7a086926e00338d2be
fetched_at: '2026-06-28T22:41:21.804554+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Filtros tela
  Necessidade de Compra
type: support-article
updated_at: '2026-02-05T16:42:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38191491592855-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Filtros-tela-Necessidade-de-Compra
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38191491579543) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Quais são os filtros disponíveis na tela da Necessidade de Compra no Novo Fluxo de Compras?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Release 12.1.2310  
  
**Solução**  
Na tela **Necessidade de Compra** do **Novo Fluxo de Compras**, estão disponíveis os seguintes filtros:

**Filtros da tela principal**

* Filtro por data
* Código do produto
* Valida grupo do produto (Sim ou Não)

**Filtros da Busca Avançada**

* Número da Solicitação de Compra
* Descrição do produto
* Código do Grupo de produto
* Descrição do Grupo de produto
* Solicitante
* Filial solicitante
* Filial entrega
* Centro de custo
* Conta contábil
* Item contábil
* Classe valor
* Registro por página

**Filtro do cadastro de Comprador**

**Filtro do Ponto de Entrada NFCFILTSC**

Os filtros acima podem ser utilizados pelo usuário de forma individual ou combinada. Esses filtros podem ser utilizados em todas as abas da tela de Necessidade de Compra (Em aberto, Parcialmente atendidas e Atendidas).

Seguem abaixo mais informações sobre os filtros existentes da tela Necessidade de Compra:

**O Filtro por Data** funciona com intervalo de duas datas (início e fim), após a seleção o filtro buscará solicitações de compras que possuem a **Data de necessidade** de acordo com o período selecionado. Essa **Data de necessidade**corresponde ao conteúdo do campo **C1\_DATPRF** da Solicitação de Compras. Não temos como filtrar as solicitações pela Data de Emissão da Solicitação de Compras (**C1\_EMISSAO)**.

O filtro **Registro por página** permite que permite ao usuário definir a quantidade de registros exibidos por página, podendo escolher entre 20 (padrão), 50, 100, 150 ou 200.

O filtro Registro por página é um Filtro Padrão, isso significa que, após configurada, essa preferência será salva em seu perfil, garantindo que esse filtro seja mantida nos próximos acessos. Ou seja, você poderá sair da rotina e, quando abri-la novamente, o filtro permanecerá aplicado.

A configuração e a gravação dos **Filtros Padrões** são definidas por **usuário** e pela**filial** em que ele está logado. Isso significa que cada filial pode possuir seus próprios filtros, permitindo que usuários de filiais diferentes utilizem configurações distintas.

A rotina realizava a listagem das solicitações apenas utilizando o conceito de **rolagem infinita**. Nesse modelo, os registros eram carregados de forma contínua à medida que o usuário descia a tela, sem uma divisão explícita dos registros.

Essa abordagem oferece maior flexibilidade e personalização, permitindo que cada usuário adapte a visualização dos dados de acordo com sua necessidade e contexto de trabalho em cada filial.

Referente o **Filtro do cadastro de Comprador,** o sistema permite a aplicação de filtros de usuário. Para isso, é necessário cadastrar o comprador na rotina Compradores (COMA087), no botão Botão Outras Ações > Filtro Necess. NFC, especificar o filtro desejado e ativar o parâmetro [MV\_FILTNFC](https://tdn.totvs.com/pages/viewpage.action?pageId=844976022). Para mais informações sobre como utilizar os filtros, consulte a documentação [PCOM09013 - Compradores (COMA087)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=274632269), na sessão **Filtro Necessidade de Compra para o Novo Fluxo de Compras (NFC).**

Sobre o Filtro do Ponto de Entrada **NFCFILTSC**, segue documentação abaixo.

**Nome do ponto de entrada**: NFCFILTSC

**Objetivo**: Este ponto de entrada é utilizado na necessidade de compra para filtrar SCs de acordo com os filtros estabelecidos.

**Documentação**: [Clique Aqui - Documentação NFCFILTSC](https://tdn.totvs.com.br/pages/viewpage.action?pageId=951342471)

Importante: O ponto de entrada NFCFILTSC não pode ser utilizado para adicionar novos campos de filtro na Busca Avançada nem na tela principal. Pode ser utilizada apenas para validações e filtros internos. Os pontos de entrada do Novo Fluxo de Compras não permitem apresentação de interface devido a tecnologia utilizada. As customizações possíveis serão acionadas em momentos de processamento, semelhante ao comportamento de execauto.

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
