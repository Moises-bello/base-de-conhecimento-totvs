---
content_hash: fff3d3a7d952acdbc8b2f388c3c5e09df4b08d22b5d51fb82bd409324302bf92
fetched_at: '2026-06-29T00:08:34.725843+00:00'
page_id: '274836436'
product: rm
source: tdn-rm
title: COT0003_Item_Nao_Exibido_Na_Cotacao
type: documentation
url: https://tdn.totvs.com/display/LRM/COT0003_Item_Nao_Exibido_Na_Cotacao
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e superiores |
| **Ocorrência:** | Item não exibido no Assistente de Cotação |
| **Ambiente:** | Cotação |
| **Passo a passo:** | Foi feita a movimentação de um ou mais produto(s) em um determinado tipo de movimento, porém estes não estão sendo exibidos na cotação. CAUSA 1- O movimento não está parametrizado como Solicitação de compras.  2- O movimento já está parametrizado como Solicitação de compras, porém seu status está como “Normal”.  3- O movimento trabalha com aprovação na solicitação de compras ou aprovação por Workflow e o mesmo não está aprovado.  4- O funcionário 1 informado no movimento de solicitação de compras é diferente do usuário responsável pela cotação.  5- O parâmetro “Carrega solicitações após filtro” está marcado. SOLUÇÃO 1- Acessar os parâmetros do movimento de solicitação de compras, etapa Compra/Venda – Outros dados -> Tipo de movimento de compra -> Selecionar “Solicitação de compra”.  2- Se o movimento já está parametrizado como solicitação de compra, porém seu status está como “Normal”, ele deve ser regravado para atualização de seu status.  3- Aprovar o movimento. Verificar se o mesmo possui registro na TMOVAPROVA e se o seu tipo de aprovação é “Aprovação na solicitação de compras” ou “Aprovação por Workflow”.  4- Informar dentro da cotação o mesmo funcionário que foi incluído na solicitação de compras ou então limpar o funcionário 1 da solicitação de compras.  5- Preencher um dos campos de filtros na tela “Adicionar filtro para produtos” que retorne o item desejado e clicar no botão “Atualizar Agora”   Importante Sempre que for alterar alguma parametrização da cotação (Gestão de compras -> Cotação), verificar a parametrização geral (em caso de não informar uma filial na cotação), e também a parametrização por filial dentro do parâmetro “Definição de Escopo – Filial” (no caso de informar uma filial na cotação). |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
