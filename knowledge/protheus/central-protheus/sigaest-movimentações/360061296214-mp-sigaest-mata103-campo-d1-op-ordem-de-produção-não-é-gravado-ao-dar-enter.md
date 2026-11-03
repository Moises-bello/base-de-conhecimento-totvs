---
article_id: 360061296214
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 975d29ad4e95f369f7fb30dd076c25ee16b247267791537d748d844f21e82474
fetched_at: '2026-06-28T22:38:58.579875+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - MATA103 - Campo D1_OP (Ordem de Produção) não é gravado ao dar
  Enter
type: support-article
updated_at: '2021-04-28T15:45:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061296214-MP-SIGAEST-MATA103-Campo-D1-OP-Ordem-de-Produ%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-gravado-ao-dar-Enter
---

**Dúvida**No Documento de Entrada (MATA103), ao preencher o campo Ordem de Produção (OP - D1\_OP) e dar Enter, o campo é apagado mesmo selecionando a OP pelo botão [F4]. O que fazer para corrigir este problema?  
  
**Ambiente**Microsiga Protheus - Estoque/Custos - Ocorre apenas na versão 12.1.23

**Solução**Para corrigir este problema siga os passos a seguir:

1° - acesse o módulo Configurador (SIGACFG) em Base de Dados > Dicionário > Gatilhos;  
2° - Selecione o campo D1\_OP e clique para editar;  
3° - Altere o contradomínio (X7\_CDOMIN) do gatilho de D1\_OP para D1\_ORDEM conforme abaixo e salve a alteração.

![](https://tdn.totvs.com/download/attachments/471944887/image2019-4-8_10-50-12.png?version=1&modificationDate=1554731612133&api=v2)

Após isso basta efetuar novamente a entrada selecionando a OP para que o campo seja gravado corretamente.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
