---
article_id: 11334901781655
category: esocial - Periódicos
content_hash: 536c7bedfd94c10bbaec93a69c2ee891eea722353484461feaf9c9bd2ecc6c82
fetched_at: '2026-06-28T22:47:09.324405+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: Necessário preencher o parâmetro
  "Evento Abono Férias envelope" nos Parâmetros Gerais do eSocial!'
type: support-article
updated_at: '2024-06-13T17:02:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11334901781655-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-Necess%C3%A1rio-preencher-o-par%C3%A2metro-Evento-Abono-F%C3%A9rias-envelope-nos-Par%C3%A2metros-Gerais-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**  
Ao gerar evento S-1200 ou S-2299 para funcionários que tiveram férias, é exibido o erro **Necessário preencher o parâmetro "Evento Abono Férias envelope" nos Parâmetros Gerais do eSocial!**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11334936313623)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre quando o campo **Evento Abono Férias envelope** localizado no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 6/7** não está preenchido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11334688337303)

**Solução**Para correção dessa ocorrência, siga os passos abaixo:

1. Acesse o menu **Administração de Pessoal | Eventos** e crie uma verba do tipo **Provento**, sem código de cálculo e sem incidência;
2. Transmita o evento S-1010 da nova verba criada;
3. Após o S-1010 ser aceito pelo RET, acesse o menu **Configurações | Parametrizador | eSocial | Configurações Gerais 6/7** e informe a verba criada no campo **Evento Abono Férias envelope**;
4. Gere novamente o evento S-1200/S-2299 e envie ao eSocial.

**Saiba mais**  
Para maiores informações, acesse:  
      • [Configurações Gerais 6/7](https://tdn.totvs.com/pages/releaseview.action?pageId=540899121)
