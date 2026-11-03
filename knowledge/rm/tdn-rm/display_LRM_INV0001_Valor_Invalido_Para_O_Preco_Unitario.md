---
content_hash: a70eab25813b19819c85b3d0df93db2baed6b9d1902209009b9eb84cb4616531
fetched_at: '2026-06-29T00:08:14.719082+00:00'
page_id: '244714243'
product: rm
source: tdn-rm
title: INV0001_Valor_Invalido_Para_O_Preco_Unitario
type: documentation
url: https://tdn.totvs.com/display/LRM/INV0001_Valor_Invalido_Para_O_Preco_Unitario
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e superiores |
| **Ocorrência:** | Erro ao gerar acerto |
| **Ambiente:** | Manutenção de Inventário |
| **Passo a passo:** | Ao tentar gerar o(s) acerto(s) e encerrar o inventário é apresentado o erro abaixo impedindo a geração do movimento:   ErroMensagem     Ocorreram erros durante o processo de inventário. Maiores detalhes verifique o log do processo.   Logs   Inicio do Processo: Geração de Acertos e Encerramento do Inventário  Erro ao tentar gerar acertos e encerrar o Inventário 000003:  Item 0 - Produto 01.03 - PRODUTO 3 do Movimento ?741?! - Série INV: Valor inválido para o Preço Unitário.  Fim do Processo: Geração de Acertos e Encerramento do Inventário   CAUSA Este erro ocorre pois o preço unitário do produto que o movimento de acerto está tentando salvar é igual a 0. E neste caso o tipo de movimento está parametrizado para não permitir preço unitário igual a 0.  Ex.:   * No tipo de movimento está parametrizado para buscar preço em **Custo Médio,** porém ao visualizar o custo médio do produto é notado que o mesmo é 0. * No tipo de movimento está parametrizado para buscar preço em **Ultima Compra,** porém este produto ainda não foi movimentado. Sendo assim, o sistema não tem de onde buscar o preço. * No tipo de movimento está parametrizado para buscar preço em um dos 5 preços disponíveis do cadastro de produto, porém, no(s) escolhido(s) para buscar o preço o mesmo não está informado.  SOLUÇÃO Existem 2 soluções possíveis, e são elas:  1 - Alterar o campo de onde o sistema está buscando o preço a ser levado ao item.    Na imagem acima, o sistema está buscando o preço do Custo Médio, porém, este é 0. Neste caso, terá que escolher uma outra opção onde o valor a ser gerado seja maior que 0.    2 - Na etapa Item - Preços, marcar a opção para **"Aceitar Preço Zero" .**  Marcando essa opção o erro não será apresentado, porém, o movimento poderá ser salvo com o preço unitário como R$0,00. A edição do mesmo após a geração será liberada, desde que o parâmetro de Edição do Preço esteja como Edita. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
