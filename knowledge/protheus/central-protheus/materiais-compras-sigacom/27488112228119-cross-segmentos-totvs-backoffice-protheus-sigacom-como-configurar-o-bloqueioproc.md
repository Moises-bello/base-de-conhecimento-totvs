---
article_id: 27488112228119
category: Materiais - Compras (SIGACOM)
content_hash: c083215d76d81fea958e44f1096eab2f6de997842534f89ec3f1cbdedb49a8f5
fetched_at: '2026-06-28T22:41:14.507059+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o Bloqueio/Processo
  do PCO em Rotinas MVC para posicionar corretamente os campos?
type: support-article
updated_at: '2024-11-01T14:10:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27488112228119-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-o-Bloqueio-Processo-do-PCO-em-Rotinas-MVC-para-posicionar-corretamente-os-campos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27488112188183) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**  
Como configurar o Bloqueio/Processo do PCO em Rotinas MVC para posicionar corretamente os campos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Será necessário utilizar a função **FWFLDGET** antes do campo para que possa posicionar corretamente.

Exemplo sem uso da Função (forma incorreta de uso para rotinas MVC, pois, da forma abaixo , o campo fica desposicionado).

Na tela de lançamento abaixo , trouxe um valor incorreto de 440,00, pois, para o campo utilizado no lançamento do PCO de exemplo foi utilizado a regra CNE->CNE\_VLTOT, e dessa forma não trouxe na tela, o valor correto na rotina que é de 15.900.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27488127410967)

Exemplo com uso da Função **FWFLDGET**

Utilizei no campo valor de lançamento do pco a regra utilizando a função **FWFLDGET**('CNE\_VLTOT'), dessa forma posicionou no campo da Rotina corretamente conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27488127412375)

Saiba Mais :

[FWFldGet](https://tdn.totvs.com/display/public/framework/FWFldGet)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível utilizar a contingencia de PCO via execução automática (Execauto)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6062858276375-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-utilizar-a-contingencia-de-PCO-via-execu%C3%A7%C3%A3o-autom%C3%A1tica-Execauto)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Configuração do Cubo Gerencial Simples - Utilização PCO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4584114767895-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Configura%C3%A7%C3%A3o-do-Cubo-Gerencial-Simples-Utiliza%C3%A7%C3%A3o-PCO)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de configuração do lançamento de Pedido de compras com rateio por centro de custo - 000052/08](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046017653-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-configura%C3%A7%C3%A3o-do-lan%C3%A7amento-de-Pedido-de-compras-com-rateio-por-centro-de-custo-000052-08)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM X PCO - Na tela de Manutenção de Lançamento utilizando processo:000052 - sequencial: 03 ,só é Demonstrado o Último item na Validação de Pedido de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18438415826711-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-X-PCO-Na-tela-de-Manuten%C3%A7%C3%A3o-de-Lan%C3%A7amento-utilizando-processo-000052-sequencial-03-s%C3%B3-%C3%A9-Demonstrado-o-%C3%9Altimo-item-na-Valida%C3%A7%C3%A3o-de-Pedido-de-Compras)
