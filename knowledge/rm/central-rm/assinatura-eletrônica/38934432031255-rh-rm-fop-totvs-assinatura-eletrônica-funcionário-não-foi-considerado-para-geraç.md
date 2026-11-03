---
article_id: 38934432031255
category: Assinatura Eletrônica
content_hash: cb98c0d7d7504272dad12412a0ece7cf08250a457c191bbbdc50744603f91943
fetched_at: '2026-06-28T22:46:44.100109+00:00'
product: rm
section_id: 4403549405207
source: central-rm
title: RH - RM - FOP - TOTVS Assinatura Eletrônica -  Funcionário não foi considerado
  para geração do relatório, pois já possui este relatório pendente de assinatura.
type: support-article
updated_at: '2026-03-11T17:14:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38934432031255-RH-RM-FOP-TOTVS-Assinatura-Eletr%C3%B4nica-Funcion%C3%A1rio-n%C3%A3o-foi-considerado-para-gera%C3%A7%C3%A3o-do-relat%C3%B3rio-pois-j%C3%A1-possui-este-relat%C3%B3rio-pendente-de-assinatura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38934432020503) Tempo aproximado para leitura: **00:01:45 min**  
  
**Ocorrência**  
Ao realizar a integração de documentos para assinatura eletrônica do RM para o TAE, é apresentado a mensagem de erro: *"Funcionário 'xxxx' não foi considerado para geração do relatório, pois já possui este relatório pendente de assinatura."*  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38934432021399)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Este aviso é apresentado quando se utiliza o parâmetro "**Não integrar documento caso o mesmo já tenha sido integrado anteriormente (evita duplicidade)"**durante o processo de integração do relatório, essa opção permite que um mesmo documento não seja integrado mais de uma vez para o mesmo funcionário.   
  
**Solução**  
Para que seja possível integrar o relatório quando é apresentado este aviso, desmarque este parâmetro  "**Não integrar documento caso o mesmo já tenha sido integrado anteriormente (evita duplicidade),** desta forma será possível integrar novamente este documento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38934432022679)

**Saiba mais:**

[RH - RM - Meu RH - Integração do Meu RH com o Tae(Totvs Assinatura Eletrônica)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13740154028823-RH-RM-Meu-RH-Integra%C3%A7%C3%A3o-do-Meu-RH-com-o-Tae-Totvs-assinatura-eletr%C3%B4nica-)
