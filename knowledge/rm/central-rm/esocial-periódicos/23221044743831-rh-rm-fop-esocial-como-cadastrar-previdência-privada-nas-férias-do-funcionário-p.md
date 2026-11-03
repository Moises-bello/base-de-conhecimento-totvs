---
article_id: 23221044743831
category: esocial - Periódicos
content_hash: cce6f7e2967dacdabdec1dfbc185713bb70deb208dd1be360056913c3b93b5ad
fetched_at: '2026-06-28T22:47:09.182930+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Como cadastrar previdência privada nas férias do
  funcionário, para correta geração da incidência no XML S-1210
type: support-article
updated_at: '2026-01-22T14:06:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23221044743831-RH-RM-FOP-eSocial-Como-cadastrar-previd%C3%AAncia-privada-nas-f%C3%A9rias-do-funcion%C3%A1rio-para-correta-gera%C3%A7%C3%A3o-da-incid%C3%AAncia-no-XML-S-1210
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23221044722071)Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
Como cadastrar previdência privada nas férias do funcionário, para correta geração da incidência no XML S-1210?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**  
Ao gerar o XML S-1210 a partir do leiaute S-1.2 é gerada a informação da Previdência Privada. Para a correta geração do evento S-1210, quando o funcionário possuir férias, realize os seguintes passos:

1. Acesse **Configurações - Parametrizador - Férias- Eventos Adicionais** e inclua o evento da previdência com código de cálculo 420 em Cód. Evento Recibo. No campo Cód. Evento Folha, será necessário a criação de um novo evento, sem incidência e sem código de cálculo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37642208395031)

2. Acesse o **Recibo de Férias - Anexos - Adicionais de Férias** e inclua a mesma informação acima;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37642200462743)

3. No Recibo de férias constará lançado o evento de código de cálculo 420;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37642208405271)

4. Na Folha de pagamento constará lançado o evento sem código de cálculo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37642200464791)

5. XML S-1210 gerado sem a informação em duplicidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37642200468119)
