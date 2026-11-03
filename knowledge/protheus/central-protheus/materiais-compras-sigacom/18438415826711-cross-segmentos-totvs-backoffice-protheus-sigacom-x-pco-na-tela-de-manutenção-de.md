---
article_id: 18438415826711
category: Materiais - Compras (SIGACOM)
content_hash: 44fd96970cf8a8e78bb798d6f97a0cfc44062efe45170398002b3f79b87704b5
fetched_at: '2026-06-28T22:41:25.441167+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM X PCO - Na tela de Manutenção
  de Lançamento utilizando processo:000052 - sequencial: 03 ,só é Demonstrado o Último
  item na Validação de Pedido de Compras '
type: support-article
updated_at: '2023-10-20T17:06:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18438415826711-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-X-PCO-Na-tela-de-Manuten%C3%A7%C3%A3o-de-Lan%C3%A7amento-utilizando-processo-000052-sequencial-03-s%C3%B3-%C3%A9-Demonstrado-o-%C3%9Altimo-item-na-Valida%C3%A7%C3%A3o-de-Pedido-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18438415803159) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Na tela de Manutenção de Lançamento utilizando processo:000052 - sequencial: 03 ,só é Demonstrado o Último item na Validação de Pedido de Compras.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
 **Exemplo de Cenário**

Pedido com 3 Itens e com Centro de Custo e Conta Contábil Aglutinados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18438447542551)

-Tela de Manutenção de Lançamento apresenta somente o último item.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18438422859927)

**Solução:**

Para que o sistema exiba uma linha do lançamento para cada item do pedido de compras, é necessário configurar o {*}processo (000052) no sequencial 01{*}, que é por itens, desta forma será exibido 1 lançamento para cada item.

Segue documentação dos processos e lançamentos: <https://tdn.totvs.com/pages/viewpage.action?pageId=630567761>.

Obs:Hoje não é possível realizar aglutinação (Conta+C.Custo) , pois o modulo de Planejamento e Controle Orçamentário não disponibiliza essa opção para este processo.  
Para que seja avaliado a melhoria é necessário abrir uma sugestão na central colaborativa.  
Mas para que o valor do lançamento (AKC\_VALOR) reflita a somatória de todos os itens do pedido, poderá ser utilizado a variável: m->Avalores[6].

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
