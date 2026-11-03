---
article_id: 30318556659095
category: Materiais - Compras (SIGACOM)
content_hash: 0ff40fc0c8779cf393fed04c56fb4743f9ab637c1857dea43dc03e6325078038
fetched_at: '2026-06-28T22:41:15.934802+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como incluir nota de
  complemento de valor em entradas do tipo Beneficiamento, utilizando clientes ?
type: support-article
updated_at: '2025-02-28T19:18:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30318556659095-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-incluir-nota-de-complemento-de-valor-em-entradas-do-tipo-Beneficiamento-utilizando-clientes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30318556647319) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Dei entrada em uma nota com o tipo Beneficiamento, é possível complementar esse valor ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões.  
  
**Solução**Recentemente efetuamos uma consulta à nossa equipe de produto, referente a esse processo. O retorno segue abaixo, com a sugestão do processo a ser efetuado na inclusão da nota de complemento de valor, como no momento de efetuar o retorno desse beneficiamento( nota de saída ).

A Nota Fiscal Complementar tem a função de corrigir informações da NF original.   
Com a Nota Fiscal Complementar de produto você pode acrescentar valor ou quantidade de produtos e complementar o ICMS, IPI, entre outros e tem, conforme as orientações fiscais legais, no corpo da nota um campo especifico com a identificação do numero da NF original o qual o complemento se refere.   
   
Sugestão:  
   
1 - O faturamento para realizar movimentação de poder de terceiros tem a obrigatoriedade que o TES atualize estoque e poder de terceiros = R ou D (dependendo do movimento que necessita realizar);  
   
2 - Conforme alinhamento com Squad de Entradas foi identificado que a entrada controlando poder de terceiros deve movimentar o saldo em estoque devido aos controles da tabela SB6;  
   
3 - Abaixo seguem orientações para o atendimento de eventual necessidade do cliente, como os passos necessários para entrada(s) e saída(s) das notas fiscais  
   
**1 Entradas**  
1A - Para a primeira entrada: Nota fiscal do tipo B (beneficiamento), TES com movimenta estoque = Sim, Poder de Terceiros = Remessa e Qtd. Zero = Não  
   
1B - Para a segunda  entrada: Nota fiscal do tipo B (beneficiamento), TES com movimenta estoque = Não, Poder de Terceiros = Não Controla e Qtd. Zero = Sim  
   
**2 Saídas**  
Pedido de venda Normal  
2A Primeiro item com TES com movimenta estoque = Sim, Poder de Terceiros = Devolução, Qtd. Zero = Não e vinculando o item de acordo com a nota fiscal/item de entrada  
   
2B Segundo item com TES com movimenta estoque = Não, Poder de Terceiros = Não Controla, Qtd. Zero = Sim e vinculando o item de acordo com a nota fiscal/item de entrada

***Saiba Mais :***

***[Página Centralizadora do Compras](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)***

*[**Artigos Materiais Sigacom**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)*
