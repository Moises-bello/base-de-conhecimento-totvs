---
article_id: 10208790706071
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 263e34130b2751d101e0948ae3903a7ef43df33a17718515668c0c2c9521a2e7
fetched_at: '2026-06-28T22:38:48.096733+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - ERR_UNSAFE_PORT rotina
  Acompanha Custos
type: support-article
updated_at: '2025-03-12T12:17:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10208790706071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-ERR-UNSAFE-PORT-rotina-Acompanha-Custos
---

**Dúvida**Ao tentar efetuar o acesso a rotina MATA038 - Acompanha Custos, é apresentado a mensagem de "não é possível acessar esse site", destinando o caminho e o erro ERR\_UNSAFE\_PORT, como resolver?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33.

**Solução**  
A [nova interface PO UI](https://tdn.totvs.com/display/framework/Nova+interface+do+Protheus+com+PO+UI) utiliza a classe [TWebEngine](https://tdn.totvs.com/display/tec/TWebEngine) que cria um objeto para manipular uma página HTML, trocando informações em tempo real entre o SmartClient e o Navegador através do **protocolo*****WebSocket***.

O erro ***ERR\_UNSAFE\_PORT***é causado porque o navegador (chrome, Firefox, IExplorer, e outros) possa estar **impedindo** utilizar a porta **6000**, que entende que são portas reservadas para protocolos específicos e não seguras.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10208716814615)

O suporte ESTOQUE/CUSTOS, recomenda que utilize outra porta ou faça liberação da mesma nos navegadores do servidor e estação cliente.  
  
Para mais informações:  
<https://superuser.com/questions/188058/which-ports-are-considered-unsafe-by-chrome>  
<https://dev.to/myogeshchavan97/comment/14p38>

Dúvidas posteriores, contatar o time "Tecnologia Atendimento".

**Saiba mais:**

[*Tudo sobre a rotina Acompanha Custos MATA038*](https://tdn.totvs.com/display/public/PROT/Acompanha+Custos)
