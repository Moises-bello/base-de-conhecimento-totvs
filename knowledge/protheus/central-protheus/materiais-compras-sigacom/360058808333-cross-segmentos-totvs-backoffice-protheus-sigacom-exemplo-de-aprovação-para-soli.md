---
article_id: 360058808333
category: Materiais - Compras (SIGACOM)
content_hash: 84ab2948b881e3c3d333396c0df825563465853fafa0122c4d30d256135e6406
fetched_at: '2026-06-28T22:41:17.702215+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de Aprovação
  para Solicitação de Compras Com Produto de Importação
type: support-article
updated_at: '2025-11-12T17:49:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058808333-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-Aprova%C3%A7%C3%A3o-para-Solicita%C3%A7%C3%A3o-de-Compras-Com-Produto-de-Importa%C3%A7%C3%A3o
---

**Dúvida**

Exemplo de Aprovação para Solicitação de Compras Com Produto de Importação

**Ambiente**  
Protheus – Gestão de Compras  – A partir da versão 11.80  
  
**Solução**

É possível bloquear Solicitação de Compras de produto de Importação ?

Sim, é possível com base no exemplo a seguir com a utilização do bloqueio por alçada da Solicitação de Compras:

SIGACOM > Atualizações > Solicitações > Solicitação de Compras:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25501753922839)

E para ser realizado o Bloqueio da SC com Produto importado, deve-se possuir configurado a alçada de SC, cujas informações estão no artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alçada de Solicitação de Compras por Entidade Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Al%C3%A7ada-de-Solicita%C3%A7%C3%A3o-de-Compras-por-Entidade-Cont%C3%A1bil?source=search)

Ao confirmar a inclusão da SC com o controle de alçada configurado ela ficará bloqueada por alçada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25501788118295)

Após liberar a alçada da SC, ela estará apta pra geração da SI (Solicitação de Importação para o SIGAEIC) na rotina de Itens pra Importação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25501788121495)

***Obs:***

NO processo de geração de Solicitação de Importação (SI) na rotina Itens para Importação (MATA112) há disponível o parâmetro ***MV\_APROVSI,*** que caso esteja com o conteúdo **.T.**, não é possível gerar a SI a partir de uma SC em processo de aprovação, conforme informação do artigo abaixo:

[MV\_APROVSI - Ativa o bloqueio das solicitações de importação.](https://tdn.totvs.com/x/kb3wMQ)

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alçada de Solicitação de Compras por Entidade Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Al%C3%A7ada-de-Solicita%C3%A7%C3%A3o-de-Compras-por-Entidade-Cont%C3%A1bil?source=search)

[PCOM09002 - Configuração para Controle de Alçadas por Entidade Contábil - Solicitação de Compras e Armazém](https://tdn.totvs.com/pages/viewpage.action?pageId=284348332)

[MV\_APROVSI - Ativa o bloqueio das solicitações de importação.](https://tdn.totvs.com/x/kb3wMQ)

[Parâmetro MV\_APROVSI](https://tdn.totvs.com/x/N4rDOQ)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
