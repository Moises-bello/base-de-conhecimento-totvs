---
article_id: 360056020454
category: Ferramentas
content_hash: 422e6959c09b0d6866e4185c2cbbf6111f61efe0449c029e03ae99fdbd7a454d
fetched_at: '2026-06-28T22:42:18.040975+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: 'Framework - Linha Protheus - Log de Registros, campos _USERLGI e _USERLGA
  Gravando com ano de 1996  '
type: support-article
updated_at: '2024-05-09T11:07:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056020454-Framework-Linha-Protheus-Log-de-Registros-campos-USERLGI-e-USERLGA-Gravando-com-ano-de-1996
---

**Dúvida**  
Como evitar que os campos \_USERLGI e \_USERLGA gravem com o ano de 1996?  
  
**Ambiente**Framework - Linha Protheus - FRAME - DBAccess - Todas as versões  
  
**Solução**O problema está relacionado ao **Collation** que foi configurado na criação do database.  
  
Segue abaixo link do TDN:  
<https://tdn.totvs.com/display/tec/DBAccess+-+Collation%2C+Character+Type+e+Encoding>  
  
Para efetuar essas alterações, o banco atual deve ser **exportado**, removido e recriado na configuração correta e então os dados **importados** novamente.  
  
É recomendado que o profissional a realizar o trabalho seja um DBA, que poderá caso o cliente deseje ser alocado através da TOTVS.
