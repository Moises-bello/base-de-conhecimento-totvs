---
article_id: 360059450793
category: RH - Ponto Eletrônico
content_hash: 7cef5dfc984438f507b0c6af1d68d3c85cdde623174ae5f451ba660ce8e8f1aa
fetched_at: '2026-06-28T22:44:58.266331+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Alteração ou Exclusão de Pré Abonos já utilizados
type: support-article
updated_at: '2024-03-27T14:45:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059450793-RH-Linha-Protheus-PON-Altera%C3%A7%C3%A3o-ou-Exclus%C3%A3o-de-Pr%C3%A9-Abonos-j%C3%A1-utilizados
---

**Ocorrência**No módulo de Ponto Eletrônico, ao tentar realizar uma alteração ou exclusão em um registro já utilizado na rotina de Pré-Abono, o sistema emite o *log* abaixo e não permite nenhuma manutenção:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099956473)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**Quando temos este *log*, é porque o abono já foi utilizado, ou seja, já foi feito o processo de Apontamento e o abono foi lançado para o evento.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099956913)​

Veja que o campo **Utilizado** está como **SIM**.  
  
**Solução**Para **alterar ou excluir** o Pré Abono, será necessário primeiramente excluir o lançamento do Abono, portanto, siga os passos abaixo:  
**>** para a rotina de **Apontamentos** (Atualizações - Lançamentos - Apontamentos): clique em Atualizar - posicione no dia do abono e acesse Outras Ações -> Abonar/Justificar ou clique com F4 no teclado, com isso, delete o abono utilizado.  
**>** para a rotina de **Integrados** (Atualizações - Lançamentos - Integrados): clique em Outras Ações - Alterar - posicione no dia do abono e clique na opção Abonar/Justificar ou clique com F7 no teclado, com isso, delete o abono utilizado.  
  
Retornando na rotina de Pré-Abono, o campo terá mudado para **Não** e com isso, será possível a alteração ou exclusão do registro.  
  
Para os casos de Abonos vindos do App MEU RH ou Portal GCH, que já passou por todos os níveis de aprovação, também será possível fazer a exclusão do Pré Abono seguindo os passos citados acima, fazendo com que toda a solicitação seja excluída também.  
  
Cabe ressaltar que em casos de exclusão, a rotina **não pedirá confirmação do usuário**, portanto, é importante ter atenção no acesso à rotina.  
  
  
**Saiba Mais:**  
[RH - Linha Protheus - PON - Como fazer o lançamento de Pré Abono no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052082954-RH-Linha-Protheus-PON-Como-fazer-o-lan%C3%A7amento-de-Pr%C3%A9-Abono-no-Ponto-Eletr%C3%B4nico)  
[Exclusão de Pré Abono das tabelas do MEU RH](https://tdn.totvs.com/pages/viewpage.action?pageId=790646210)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
