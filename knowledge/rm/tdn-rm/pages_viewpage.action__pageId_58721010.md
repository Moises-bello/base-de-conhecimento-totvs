---
content_hash: 901307094721d7427aea7cf4c60f9632769ea8246aced0bac5e25ab50dbb5df5
fetched_at: '2026-06-29T00:10:53.824860+00:00'
page_id: '58721010'
product: rm
source: tdn-rm
title: 'Dica: Não é possível incluir itens no movimento gerado por faturamento'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=58721010
version: 3
---

**Produto**: Totvs Gestão de Estoque, Compras e Faturamento

**Processo do Sistema**: Faturamento

**SubProcesso**: Movimento

**Sintoma**

Ao  faturar um movimento sistema não permite incluir novos itens no movimento que esta sendo gerado.

**Causas**

A  flag “Marcar itens que farão parte do movimento gerado” se encontra marcada no  Tipo de Movimento de origem.

**Solução**

1.  Acessar  | Opções | Parâmetros | RMNucleus |  e selecionar o processo onde o tipo de

movimento utilizado está configurado.

 √  Avançar a etapa  |Compra/Vendas  –  Outros Dados  |  e  desmarcar a flag “Marcar itens que farão parte do movimento gerado”.

2.  Após alterar a parametrização realize um teste verificando se agora é possível incluir o

novo item durante o faturamento. Caso não o seja, execute o próximo passo.

3.  Feche todos os aplicativos RM  e acesse a pasta “C:\totvs\CorporeRM\RM.Net”.

Localize o arquivo RM.Host.Service.Manager.exe e execute-o.

Na tela exibida clique sobre o botão Desistalar e aguarde até que o botão instalar seja habilitado e feche a tela.

Ainda na tela exibida clique sobre o botão Instalar e aguarde até que o botão desinstalar seja habilitado e feche a tela.

Feito isso realize um novo teste.

**Informações adicionais**

A flag “Marcar itens que farão parte do movimento gerado”  tem como função não permitir a

inclusão de novos itens durante o faturamento de um movimento, além de proporcionar a

possibilidade de marcar os itens que serão faturados, realizando assim um faturamento parcial

sem a necessidade da exclusão de itens do movimento a ser gerado, para tanto ao marcar esta

Flag o sistema passa a disponibilizar uma nova coluna na tela dos itens de movimento

denominada  “Faturar”, esta coluna deverá ser configurada para que seja exibida (configuração

de colunas).

Para maiores informações:

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
