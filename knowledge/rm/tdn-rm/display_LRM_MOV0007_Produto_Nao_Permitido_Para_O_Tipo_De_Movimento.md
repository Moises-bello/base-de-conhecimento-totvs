---
content_hash: 103295a5f2292d8dfe61177f191641f4614d54f3fd76ef82a885ff8b78bc490f
fetched_at: '2026-06-29T00:08:33.925540+00:00'
page_id: '274629572'
product: rm
source: tdn-rm
title: MOV0007_Produto_Nao_Permitido_Para_O_Tipo_De_Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/MOV0007_Produto_Nao_Permitido_Para_O_Tipo_De_Movimento
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.52 e SUPERIORES |
| **Ocorrência:** | Ao salvar um movimento, o erro de produto não permitido é apresentado. |
| **Ambiente:** | Movimento |
| **Passo a passo:** | Problema Ao salvar um movimento o erro abaixo é apresentado impedindo o processo de inclusão do movimento:   Causas  1. O tipo de movimento está parametrizado para um tipo de item (Produto ou Serviço), mas o item informado na movimentação é incompatível com o parâmetro; 2. O produto não é de último nível; 3. O produto está inativo; 4. É um produto base para grade numerada; 5. Em seu cadastro o produto está marcado como EPI - Equipamento de Proteção Individual; 6. No tipo de movimento o parâmetro "Visualizar apenas produtos relacionados com o cliente/fornecedor" está marcado, mas o produto informado no movimento não tem vínculo com o cliente/fornecedor.     Soluções  1. Deverá utilizar um item de movimento compatível com a parametrização, ou seja, se a parametrização permite apenas produto terá que selecionar um produto. Se a parametrização permite apenas Serviço, deverá incluir um serviço. Outra possível solução seria editar o cadastro do produto e alterar o tipo do produto, porém, esta alteração pode gerar impactos e deverá ser minuciosamente analisado antes de aplicar. 2. Dentro do cadastro do produto na aba Identificação deverá marcar a flag de "Último Nível" se realmente necessário a utilização deste no movimento. 3. Dentro do cadastro do produto na aba Identificação deverá desmarcar a flag de "Inativo" se realmente necessário. 4. Dentro do cadastro do produto na aba Identificação deverá verificar se a flag "Base para Grade Numerada" está marcada. Caso sim, este produto realmente não pode ser movimentado pois o que deverá ser utilizado na movimentação são os produtos de grade desta base. 5. Dentro do cadastro do produto na aba Integração, deverá verificar se a flag "Integrado a Equipamento de Proteção Individual (EPI)" está marcada. Está flag somente pode ser Marcada/Desmarcada pelo processo "Vincular/Desvincular Produto a EPI". 6. Se o parâmetro “Visualizar apenas produto relacionados com o cliente / fornecedor” estiver marcado na etapa Item - Identificação 2/2, deverá vincular o produto ao cliente/fornecedor utilizado na movimentação ou se for o caso desmarcar o parâmetro conforme necessidade. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
