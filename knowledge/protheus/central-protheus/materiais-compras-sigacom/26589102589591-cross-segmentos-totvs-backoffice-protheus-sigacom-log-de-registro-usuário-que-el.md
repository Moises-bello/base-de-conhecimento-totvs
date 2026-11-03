---
article_id: 26589102589591
category: Materiais - Compras (SIGACOM)
content_hash: f2ced52e6b501f8fb52aa64376fd351db739455235f0d07b472e5d4e89d18463
fetched_at: '2026-06-28T22:41:20.046262+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Log de Registro - Usuário
  que eliminou resíduo
type: support-article
updated_at: '2024-09-24T14:58:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26589102589591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Log-de-Registro-Usu%C3%A1rio-que-eliminou-res%C3%ADduo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26589102568087) Tempo aproximado para leitura: **00:02:SS min** **Dúvida**

Como consultar logs de registro de suário que eliminou resíduo ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

Dentro da Solicitação de Compras (SC1) e Pedido de Comras (SC7), temos os campos de RESÍDUO,  C1\_RESÍDUO e C7\_RESÍDUO. Quando preenchidos com "S", indicam que o item teve eliminação de resíduo.

Para identificar o usuário,acessando o  Configurador do sistema , estão disponíveis os campos USERLGA e USERLGI, que podem ser habilitados na tabela SC7. Dessa forma, se ocorrer a eliminação, o nome do usuário que executou a rotina ficará registrado como a última alteração no Pedido de Compras.

Saiba mais em :

[Rotinas de Log e Auditoria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024872752-Framework-Linha-Protheus-Rotinas-de-Log-e-Auditoria?source=search)

[Qual a Funcionalidade da rotina Eliminar de Resíduo (MATA235)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024673534-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-Funcionalidade-da-rotina-Eliminar-de-Res%C3%ADduo-MATA235)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
