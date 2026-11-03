---
article_id: 37896695032215
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 76eca0a40cd1c73acf8e4bd6b34ab392cab6e16ce9961330829f7dcfef054acf
fetched_at: '2026-06-28T22:38:55.481469+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível utilizar
  campo endereço na pré-requisição ao estoque?
type: support-article
updated_at: '2026-01-26T12:03:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37896695032215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-utilizar-campo-endere%C3%A7o-na-pr%C3%A9-requisi%C3%A7%C3%A3o-ao-estoque
---

O campo "Numero Lote" (CP\_LOTE) não pode ser criado na pré-requisição na tabela SCP, pois está ligado ao módulo SIGAMNT, não à rastreabilidade do estoque. O lote só é definido no momento da baixa pelo usuário responsável. Para adaptações, sugere-se desenvolvimento personalizado ou sugestão via Central Colaborativa TOTVS.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37896664190359) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
O campo de lote pode ser criado na pre requisicao, dentro da tabela SCP?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**  
Não há mecanismo padrão para se definir o endereço na criação da Solicitação ao Armazém.

Sobre o campo "Numero Lote" (CP\_LOTE), ele diz respeito a um conceito atrelado ao modulo SIGAMNT (algo relacionado a gestão de pneus), não sendo o lote da Rastreabilidade do Estoque.  
   
Isso pois, somente no ato da baixa, quando o MATA185 exibe a tela do MATA241, é onde dá a oportunidade ao usuario definir de qual lote/endereço o material vai sair para o usuario requisitante. Por ser algo mais "de controle do responsavel do estoque", os campos não são exibidos no MATA105.  
   
Alternativas propostas:

* Via Processo de Desenvolvimento Participativo, cotar com o time de Desenvolvimento para que criem um ponto de entrada exclusivo para a sua empresa de acordo com suas necessidades (detalhes neste link: <https://tdn.totvs.com/pages/releaseview.action?pageId=589518919> na opção " **Criação de novo Ponto de Entrada**")
* Via Central Colaborativa, onde você pode documentar sua sugestão de melhoria e o time de Produto avaliará e lhe dará um retorno sobre a viabilidade de inclusão desta funcionalidade no padrão.

A [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics), localizada em nosso [**Portal do Cliente**](http://suporte.totvs.com/), é um espaço que você poderá sugerir melhorias, acompanhar a evolução das solicitações já realizadas, comentar, seguir, votar em sugestões feitas por outros clientes e muito mais!  
   
Para conhecer mais sobre as suas **funcionalidades**clique [**AQUI**](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13)e assista o nosso vídeo ou acesse nosso artigo [**Central Colaborativa - Funcionalidades Disponíveis**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Funcionalidades-Dispon%C3%ADveis-na-Central-Colaborativa-TOTVS).  
   
Você pode acompanhar as suas **sugestões**e **comentários**clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**  
   
Acompanhe as **Novidades da Release** clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360009734433-Ciclo-de-Vida-Relat%C3%B3rio-de-Releases).

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
