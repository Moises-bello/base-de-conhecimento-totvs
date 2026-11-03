---
article_id: 39715243396759
category: Avisos Automáticos
content_hash: e406bd4706be5fbe54bdddc78098b0e795c6943c03480a77d07834c6257add4b
fetched_at: '2026-06-28T22:46:40.473389+00:00'
product: rm
section_id: 31224122282519
source: central-rm
title: RH - RM - FOP - Como parametrizar avisos automáticos para exibir mensagem na
  tela?
type: support-article
updated_at: '2026-04-14T14:18:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39715243396759-RH-RM-FOP-Como-parametrizar-avisos-autom%C3%A1ticos-para-exibir-mensagem-na-tela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39715260108439) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
RH - RM - FOP - Como parametrizar avisos automáticos para exibir mensagem na tela?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**  
Para que o sistema envie avisos automáticos exibindo mensagens na tela do usuário, é necessário, primeiramente, realizar a configuração prévia dos avisos automáticos, conforme a documentação [**RH - RM - FOP - Parametrização de Avisos Automáticos**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024969912-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-de-Avisos-Autom%C3%A1ticos)

Após a configuração do ambiente, acesse o menu **Ambiente > Parâmetros > Parâmetros Globais** e, no item **17 - Sistema de Mensagens**, selecione a opção **Sistema de mensagens habilitado**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39715762927383)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39715243368983)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39715762928919)

Após habilitar essa opção, é necessário fechar o sistema RM, reiniciar o HOST e, em seguida, abrir o RM novamente. Com isso, o campo **Mensagem** passará a exibir a coluna **Mensagens de Usuários**, permitindo a visualização das mensagens diretamente na tela.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39715762929815)
