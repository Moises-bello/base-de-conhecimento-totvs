---
article_id: 17891051466263
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 366f938b242f6f2b691a9c1ad74d97989b5cd7639daa3d8324dc1e4d41ecfb40
fetched_at: '2026-06-28T22:38:56.924043+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - Ao efetuar
  movimento de devolução não permite preencher o endereço. Por quê?
type: support-article
updated_at: '2024-10-10T18:03:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17891051466263-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Ao-efetuar-movimento-de-devolu%C3%A7%C3%A3o-n%C3%A3o-permite-preencher-o-endere%C3%A7o-Por-qu%C3%AA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17891022935703) Tempo aproximado para leitura: **00:03:20 min** **Dúvida**

Na rotina de ***Movimentos Internos (MATA241)*** ao efetuar Devolução de saldo no Estoque e tentar informar o Endereço (**D3\_LOCALIZ**) o campo não é populado e não permite a Devolução diretamente no Endereço, obrigando acessar a rotina Endereçamento de Produtos (**MATA265**) para destinar a Localização.

É possível no padrão de alguma forma, endereçar no momento da inclusão de saldo na rotina MATA241?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17891241907863)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Atualmente para Devoluções no Estoque pela rotina de Movimentos Internos (MATA241) ***não é possível e não tem parametrização que permita essa funcionalidade***. Realmente é necessário a utilização da rotina MATA265 para endereçamento dos produtos e destinar o saldo.  
  
***Observações:*** Somente na rotina **Documento de Entrada (MATA103)** e no **Apontamento de Ordem de Produção (MATA250)** utilizando o parâmetro ***MV\_DISTMOV***que quando ativo, abrirá a tela para distribuição da quantidade de entrada em endereços/números de série, logo após a confirmação da inclusão de entrada, faturas de entrada, remito de entrada ou apontamento de produção. Veja a FAQ abaixo.  
   
[***SIGAEST - Como endereçar Produto diretamente da rotina de Documento de Entrada "automaticamente"?***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021637231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-endere%C3%A7ar-Produto-diretamente-da-rotina-de-Documento-de-Entrada-automaticamente-?source=search)  
   
Outra opção também é para os casos de endereçamento automático no Controle de Qualidade com o parâmetro **MV\_DISTAUT**, veja na FAQ abaixo sobre esse cenário e como pode parametrizar caso desejar utilizar.  
   
[SIGAEST - Armazém CQ endereçar automaticamente - MV\_DISTAUT - Como configurar?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10668896901015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Armaz%C3%A9m-CQ-endere%C3%A7ar-automaticamente-MV-DISTAUT-Como-configurar-?source=search)

***Importante:*** Abaixo instruções sobre como entrar em contato com nossa Central Colaborativa sugerindo uma melhoria do processo padrão.

Como esse cenário trata-se de uma sugestão de melhoria no produto e deve ser incluída na [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics), localizada em nosso [**Portal do Cliente**](http://suporte.totvs.com/). É um espaço que você poderá sugerir melhorias, acompanhar a evolução das solicitações já realizadas, comentar, seguir, votar em sugestões feitas por outros clientes e muito mais!  
   
Para conhecer mais sobre as suas **funcionalidades**clique [AQUI](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13)e assista o nosso vídeo ou acesse nosso artigo [Central Colaborativa - Funcionalidades Disponíveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Funcionalidades-Dispon%C3%ADveis-na-Central-Colaborativa-TOTVS).  
Você pode acompanhar as suas **sugestões**e **comentários**clicando [AQUI](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**  
Acompanhe as **Novidades da Release** clicando [AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360009734433-Ciclo-de-Vida-Relat%C3%B3rio-de-Releases).  
   
![](https://atendimento.totvs.com/attachments/token/IacmZXL58Jxjazs9gUw3oEc5j/?name=image.png)  
   
Como alternativa, caso a melhoria seja validada, aceita pelo time de produto TOTVS e deseje a implementação da funcionalidade na versão atual ou em curto prazo, podemos direcionar essa solicitação para a nossa área de Central de Soluções que providenciará uma proposta de customização para sua empresa para atender a funcionalidade sugerida.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
