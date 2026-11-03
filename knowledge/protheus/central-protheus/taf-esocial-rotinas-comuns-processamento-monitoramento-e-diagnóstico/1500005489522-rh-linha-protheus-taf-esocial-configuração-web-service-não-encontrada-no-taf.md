---
article_id: 1500005489522
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 6793353760e99970951e5dee2470d4c9ba84e8a8885c021765fbe783d0e14472
fetched_at: '2026-06-28T22:45:20.951164+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - WEB Service não encontrada
  no TAF
type: support-article
updated_at: '2026-06-16T20:01:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005489522-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-WEB-Service-n%C3%A3o-encontrada-no-TAF
---

**Dúvida**  
Ao acessar a tela de diagnósticos, não é apresentada o status de conexão com a Web Service do TAF mesmo estando ativo.  
WEB service não encontrada no TAF.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões  
  
**Solução**  
1. Acesse o configurador do TAF e procure pelo parâmetro MV\_TAFREST:  
[TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233-TAF-CONFIGURADOR-Como-acessar-os-par%C3%A2metros-do-sistema-)  
  
2. Insira o IP do servidor onde está instalado o TAF, e para descobrir qual a porta de comunicação, basta acessar o arquivo *appserver.ini* da *web service* localizado na pasta *bin/app* e procurar pela seção [HTTPREST] e verifique qual a porta utilizada. Exemplo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007449361)  
  
(\*Se seu ambiente for CLOUD verificar com a equipe qual a URL e porta disponível)

3. Segue exemplo como deverá ficar preenchido o parâmetro MV\_TAFREST:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007300222)
