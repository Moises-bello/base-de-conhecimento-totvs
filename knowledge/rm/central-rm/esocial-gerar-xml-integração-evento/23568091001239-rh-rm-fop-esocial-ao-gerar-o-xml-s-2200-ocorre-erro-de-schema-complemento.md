---
article_id: 23568091001239
category: eSocial - Gerar XML/ Integração Evento
content_hash: 2f1b15ca6783b67dca953b67388504f994a4d479d21195895158c9ec927865fd
fetched_at: '2026-06-28T22:47:11.934364+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Ao gerar o XML S-2200 ocorre erro de Schema complemento
type: support-article
updated_at: '2026-06-01T17:31:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23568091001239-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-2200-ocorre-erro-de-Schema-complemento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23568090987159) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao transmitir o XML S-2200 para o governo ocorre erro de Schema Complemento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23568090988311)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**  
O erro ocorre quando é gerado no XML S-2200 uma informação que não condiz com o leiaute. De acordo com a informação no leiaute a tag tem que ser gerada com o tamanho de pelo menos 1 caractere e tamanho máximo 30.  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23614516914839)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **Administração de Pessoal | Funcionários:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23613717852823)

2. Identifique o cadastro do funcionário, acesse **Endereço Principal | Complemento** e verifique se há alguma informação cadastrada indevidamente ou algum espaçamento fazendo que a tag seja gerada incorretamente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23614291651863)

3. Salve as alterações e gere novamente o XML.   
  
**Saiba mais**  
[Mapeamento dos Eventos](https://tdn.totvs.com/display/public/LRM/Mapeamento+dos+Eventos)
