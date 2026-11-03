---
article_id: 4402660750487
category: esocial - Periódicos
content_hash: 37192ae5b3ed648205d599a6a3e7aa446a83b7bd9b4d893e37ea59da05806624
fetched_at: '2026-06-28T22:47:09.311225+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar o S-1200: Necessário preencher o parâmetro
  Evento IRRF Férias envelope nos Parâmetros Gerais do eSocial'
type: support-article
updated_at: '2024-06-26T11:48:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402660750487-RH-RM-FOP-eSocial-Erro-ao-gerar-o-S-1200-Necess%C3%A1rio-preencher-o-par%C3%A2metro-Evento-IRRF-F%C3%A9rias-envelope-nos-Par%C3%A2metros-Gerais-do-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24441958687895) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Ao gerar evento S-1200 para funcionários que tiveram férias, é exibido o erro **Necessário preencher o parâmetro Evento IRRF Férias envelope nos Parâmetros Gerais do eSocial**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre quando o campo **Evento IRRF Férias envelope** localizados no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 6/7** não está preenchido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6806182633239)

**Solução**Para correção dessa ocorrência, siga os passos abaixo:

1. Acesse o menu **Administração de Pessoal | Eventos** e crie uma verba do tipo **desconto**, sem código de cálculo, sem incidência e com natureza da rubrica **9299 - Outros descontos**;
2. Transmita o evento S-1010 da nova verba criada;
3. Após o S-1010 ser aceito pelo RET, acesse o menu **Configurações | Parametrizador | eSocial | Configurações Gerais 6/7** e informe a verba criada no campo **Evento IRRF Férias envelope**;
4. Gere novamente o evento S-1200.

**Saiba mais**  
Para maiores informações, acesse:  
      • [Configurações Gerais 6/7](https://tdn.totvs.com/pages/releaseview.action?pageId=540899121)
