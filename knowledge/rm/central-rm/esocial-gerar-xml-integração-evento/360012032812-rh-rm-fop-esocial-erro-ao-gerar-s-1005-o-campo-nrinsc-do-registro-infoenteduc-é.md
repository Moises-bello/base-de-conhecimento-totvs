---
article_id: 360012032812
category: eSocial - Gerar XML/ Integração Evento
content_hash: b7607a16491159dc2d8638644b6731a9b88c13319803eddf122f14bde9b7450f
fetched_at: '2026-06-28T22:47:12.198088+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar S-1005: O campo ''nrInsc'' do registro
  ''infoEntEduc'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-12-27T18:12:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012032812-RH-RM-FOP-eSocial-Erro-ao-gerar-S-1005-O-campo-nrInsc-do-registro-infoEntEduc-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:43 min  
  
Ocorrência**Ao gerar o XML do evento S-1005 é apresentada seguinte mensagem de erro: **O campo 'nrInsc' do registro 'infoEntEduc' é obrigatório e não está preenchido**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044171554/mceclip2.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Essa mensagem de erro geralmente é apresentada quando no cadastro da seção, o parâmetro **Contrata aprendiz por intermédio de entidade educativa** está marcado e o campo de **CNPJ de entidades educativas** não está preenchido.  
  
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
1. No cadastro da seção centralizadora acesse a aba **eSocial** e verifique a marcação do parâmetro **Contrata aprendiz por intermédio de entidade educativa**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045032873/mceclip0.png)

2. Caso o parâmetro esteja marcado, acesse **Anexos | CNPJ´s de Entidades Educativas** e realize a inclusão do CNPJ.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044171094/mceclip1.png)

**Saiba mais**  
Para mais informações acesse:  
      • [Mapeamento do evento S-1005](http://tdn.totvs.com/display/LRM/Evento+S-1005)
