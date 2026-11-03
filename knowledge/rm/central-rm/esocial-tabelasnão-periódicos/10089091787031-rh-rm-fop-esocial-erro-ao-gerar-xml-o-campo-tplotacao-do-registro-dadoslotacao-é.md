---
article_id: 10089091787031
category: eSocial - Tabelas/Não Periódicos
content_hash: 1344661878c229d213f4360959fb35e935ff94d13d3d5d5b413ce2c54e4c4f74
fetched_at: '2026-06-28T22:47:10.405818+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: O campo ''tpLotacao'' do registro
  ''dadosLotacao'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-12-18T15:44:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10089091787031-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-campo-tpLotacao-do-registro-dadosLotacao-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24180618337303) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar XML do evento S-1020 apresenta a mensagem **O campo 'tpLotacao' do registro 'dadosLotacao' é obrigatório e não está preenchido.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse erro geralmente ocorre quando o **Tipo de Lotação** não está preenchida no cadastro da **Lotação Tributária** ou da **Seção**.  
  
**Solução**  
Para correção da ocorrência favor realizar as validações abaixo:  
  
• Se o parâmetro **Utiliza tomadores de serviço** estiver **marcado**

1. No módulo **Folha de Pagamento**, acesse o menu **eSocial | Lotação Tributária**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10089618854935)

2. Localize o cadastro da lotação tributária em questão e preencha o campo **Tipo da Lotação** conforme desejado e salve;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10089825963287)

3. Em seguida, gere o XML novamente e envie ao eSocial.

• Se o parâmetro **Utiliza tomadores de serviço** estiver **Desmarcado**

1. Quando não utiliza tomadores de serviço, o sistema irá considerar o tipo de lotação do **cadastro da seção**. Para isso, acesse o menu **Administração de Pessoal | Seções;**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10091631010327)

2. No cadastro da seção em questão, preencha o campo **Tipo da Lotação (eSocial);**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10091730814743)**

3. Em seguida, gere o XML novamente e envie ao eSocial.

**Importante**  
O parâmetro **Utiliza Tomadores de Serviço** fica localizado no menu **Configurações | Parametrizador | Folha Normal | Tomadores de Serviço**. Não é aconselhável marcar ou desmarcar o parâmetro, quando já ocorreram movimentações de Folha e eSocial na coligada, sem consultar um especialista do produto.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Identificação da origem da Lotação Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015506452)
