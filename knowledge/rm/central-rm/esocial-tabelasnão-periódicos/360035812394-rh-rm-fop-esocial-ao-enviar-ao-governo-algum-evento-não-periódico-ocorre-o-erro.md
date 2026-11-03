---
article_id: 360035812394
category: eSocial - Tabelas/Não Periódicos
content_hash: 45c5053b58e93cbcf6a0e7975f621be7a48ca0f7f88f7186e9fd6808498aede9
fetched_at: '2026-06-28T22:47:10.251015+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao enviar ao governo algum evento não periódico
  ocorre o erro 130: É necessário existir informação cadastral do Empregador para
  o período'
type: support-article
updated_at: '2024-12-30T12:28:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035812394-RH-RM-FOP-eSocial-Ao-enviar-ao-governo-algum-evento-n%C3%A3o-peri%C3%B3dico-ocorre-o-erro-130-%C3%89-necess%C3%A1rio-existir-informa%C3%A7%C3%A3o-cadastral-do-Empregador-para-o-per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484970023575)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao enviar ao governo algum evento não periódico ocorre o erro 130: É necessário existir informação cadastral do Empregador para o período. Verificar se já foi enviado um evento de cadastramento do empregador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24501510472471)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
 **Causa**Esta mensagem de erro pode ser apresentada em certas ocasiões, as mais comuns são:  
   • O não envio do evento **S-1000** para o governo;  
   • **S-1000** foi enviado em um ambiente e o evento a ser enviado em outro ambiente;  
   • Início da validade do evento, **iniValid**, é anterior ao início de validade do evento **S-1000**.  
  
**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
• **Não envio do S-1000**:Caso o evento S-1000 ainda não tenha sido enviado, faça a [geração dos gatilhos iniciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009056971-RM-eSocial-Como-gerar-os-Gatilhos-Iniciais-por-Evento?source=search) e transmita para o governo;

• **Ambiente diferente do S-1000**:Verificar se no XML com erro e no XML S-1000 constam o mesmo tipo de ambiente, 1- Produção e 2- Homologação. Caso o ambiente seja diferente será necessário o envio do S-1000 para o ambiente desejado, ou corrigir o ambiente que está gerando no XML a ser enviado (Configurações - Parametrizador \_ eSocial - Configurações Gerais 1/7);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24501510478103)

• **Validade do anterior ao do S-1000**: O envio de eventos deve seguir uma ordem de predecessão. Assim, no exemplo, o S-1005 precisa ter o início da validade igual ou posterior ao do evento S-1000. O início da validade dos eventos podem ser validado no XML como mostra abaixo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047852413)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046979774)

**Importante**  
Caso o erro ocorra na integração com o TAF, confira se o S-1000 já foi integrado com o TAF e se o **S-1000 consta sem recibo**: Se o evento S-1000 já estiver no TAF mas não possuir número de recibo, será necessário executar o processo de [ajuste de recibo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-TAF-Ajuste-de-Recibo-Como-inserir-um-n%C3%BAmero-de-recibo-no-TAF-?source=search).
