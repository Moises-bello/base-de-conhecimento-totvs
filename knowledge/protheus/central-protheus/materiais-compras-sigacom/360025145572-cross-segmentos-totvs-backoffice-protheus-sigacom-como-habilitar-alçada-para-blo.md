---
article_id: 360025145572
category: Materiais - Compras (SIGACOM)
content_hash: 68dc09f5f41ca8af4fbbf402a74bb20493ccf8fb9e217031858ca6d74f131b08
fetched_at: '2026-06-28T22:41:07.659139+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como habilitar alçada
  para bloqueio de Autorização de Entrega ?
type: support-article
updated_at: '2026-06-09T17:17:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025145572-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-habilitar-al%C3%A7ada-para-bloqueio-de-Autoriza%C3%A7%C3%A3o-de-Entrega
---

O artigo explica como habilitar a alçada para bloqueio de Autorização de Entrega no Protheus. Deve-se ativar o parâmetro MV\_AEAPROV=.T. e configurar aprovadores (MATA095), perfil de aprovação (COMA210) e grupo de aprovação (MATA114). O sistema valida o grupo vinculado ao comprador ou ao parâmetro MV\_PCAPROV para definir o fluxo de aprovação. Para a AE, não há controle de alçada por entidade contábil nem flexibilidade relacionada para contratos de parceria.

**Dúvida**

Como habilitar alçada para bloqueio de Autorização de Entrega ? MV\_AEAPROV

**Ambiente**

Protheus – Compras – A partir da versão 11.80

**Solução**

***Assistam nosso Vídeo com a Configuração.***

How To| MP-SIGACOM Alçada Autorização de Entregas #TOTVS Backoffice (linha Protheus) <https://www.youtube.com/watch?v=3td9B0FngEg>

Segue abaixo o passo a passo da configuração.

Ativar o parâmetro MV\_ALTPDOC= .T., e validar se no grupo de aprovação está marcado a opção de Autorização de entrega:  
  
**![](https://totvssuporte.zendesk.com/attachments/token/mYcUNVt5tdWjVYoUz4fSMKfqw/?name=inline-1713960337.png)**

Segue abaixo as configurações para que a autorização de entrega seja gerada bloqueada.

Ativar o parâmetro ***MV\_AEAPROV = .T***.  
.T. Indica se tem controle de alçada,    
.F. Não tem controle de alçada.

Cadastro de aprovadores rotina ***MATA095*** informação do valor disponível para aprovação e se diário, semanal ou mensal e moeda.

Cadastro do perfil de aprovação rotina ***COMA210*** informar range de aprovação para o bloqueio do pedido, valor mínimo e máximo e a moeda.

Cadastro do Grupo de aprovação  rotina ***MATA114***na pasta cadastrais informar o(s) aprovador(es) que participarão do grupo, nível, tipo de aprovador se é apenas um vistador ou aprovador, limite automático se sim ira validar o range informado no perfil de aprovação para o bloqueio como não bloqueara qualquer valor, Tipo de liberação Usuário, Nível ou Documento e o perfil de aprovação.

Cadastro do Comprador preencha o campo ***Y1\_GRAPROV*** para informar o Grupo de aprovação da Autorização de Entrega

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413920040599)

Caso o sistema não tenha a informação no cadastro do comprador será verificado o parâmetro ***MV\_PCAPROV*** para escolha do grupo de aprovação que irá cair a AE.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413928159639)

**Fluxo do processo:**

1) Ao incluir uma AE > O Sistema valida se o fluxo de alçada está ativo (Através do parâmetro MV\_AEAPROV);  
2) Caso o parâmetro acima seja (.T.), a rotina irá buscar o grupo de aprovação para encaminhar a AE nos locais:  
2.1) Primeiro, a consulta será feita no cadastro do comprador que está incluindo o AE, caso encontre algum grupo neste cadastro, essa AE será encaminhada a ele.  
2.2) Segundo, caso não encontre nenhum grupo vinculado ao comprador, a rotina irá buscar o grupo de aprovação definido no parâmetro MV\_PCAPROV, encontrando, essa AE será encaminhada a ele.  
2.3) Caso não encontre nenhum grupo de aprovação nos cadastros acima, a AE nascerá Liberada (Sem passar por fluxo de alçada).

**Importante:**

Existe a possibilidade de configuração de alçadas de aprovação por entidade contábil da Autorização de Entrega ?

***R.:*** Por padrão o sistema apenas efetua o bloqueio se for por alçada padrão conforme orinetações acima, caso contrário (por Entidade Contábil) não será bloqueada a AE, **não gerando** dessa forma registros na ***tabela DBM*** de Alçada por Item

***Obs1:***

***Pergunta:*** Existe a possibilidade da Autorização de Entrega não Entrar na Alçada caso o Contrato de Parceria que ela for vinculada já tiver passaso pela aprovação de alçada ?

***Resposta:*** No padrão do sistema/rotina ele não possui uma funcionalidade ou parametrização para realização deste processo de a alçada de aprovação da Autorização de Entrega ser flexivel de forma a entrar ou não na alçada a depender de caracteristicas do Contrato de Parceria para o qual ela é vinculada.

Caso deseje pode-se avaliar a possibilidade através de uma customização no processo de alçada conforme a necessidade.

Abaixo artigo com os pontos de entrada disponíveis do processo para que possa avaliar algum que melhor possa atender conforme a necessidade.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de Entrada no Controle de Alçadas - MATXALC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053600534-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-no-Controle-de-Al%C3%A7adas-MATXALC)

***Saiba Mais:***

[MP - SIGACOM - Qual a utilidade do cadastro de Aprovadores?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025179531-MP-SIGACOM-Qual-a-ultilidade-do-cadastro-de-Aprovadores-?source=search)

[MP - SIGACOM - Qual a utilidade do cadastro do Perfil de Aprovação ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024881732-MP-SIGACOM-Qual-a-utilidade-do-cadastro-do-Perfil-de-Aprova%C3%A7%C3%A3o-?source=search)

[PCOM09010 - Grupo de Aprovação (MATA114)](https://tdn.totvs.com/pages/releaseview.action?pageId=274637723)

[MP - SIGACOM - Conceito do Tipo de Liberação no Grupo de Aprovação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018595131-MP-SIGACOM-Conceito-do-Tipo-de-Libera%C3%A7%C3%A3o-no-Grupo-de-Aprova%C3%A7%C3%A3o?source=search)

[MP - SIGACOM - Em quais processos o Grupo de Aprovação (MATA114) é validado ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024652012-MP-SIGACOM-Em-quais-processos-o-Grupo-de-Aprova%C3%A7%C3%A3o-MATA114-%C3%A9-validado-?source=search)

[MP - SIGACOM - Grupo de Aprovação irá considerar ou não os valores do Perfil de Aprovação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058057973-MP-SIGACOM-Grupo-de-Aprova%C3%A7%C3%A3o-ir%C3%A1-considerar-ou-n%C3%A3o-os-valores-do-Perfil-de-Aprova%C3%A7%C3%A3o-?source=search)

[MV\_AEAPROV - Controle de alçada para Autorização de Entrega](http://tdn.totvs.com/pages/releaseview.action?pageId=6085241)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001545042)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
