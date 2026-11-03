---
article_id: 12828153511959
category: eSocial - Gerar XML/ Integração Evento
content_hash: 4a452b3eeecd423379a94db05cf1d7cf19d29c8f6cd3a272872ac562c339897c
fetched_at: '2026-06-28T22:47:13.083871+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware - Erro na integração com governo: Certificado
  vencido, validade: XX/XX/XXXX'
type: support-article
updated_at: '2025-04-10T12:59:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12828153511959-RH-RM-FOP-eSocial-Middleware-Erro-na-integra%C3%A7%C3%A3o-com-governo-Certificado-vencido-validade-XX-XX-XXXX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21632417294871) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao transmitir eventos para o governo é retornado a inconsistência **Certificado vencido, validade: XX/XX/XXXX.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12828160634903)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse incidente ocorre quando o certificado encontra-se vencido, precisando realizar a importação de um novo com prazo válido, ou quando o TSS ainda não reconheceu a nova validade do certificado.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Caso o certificado seja A1, é necessário que o mesmo possua tamanho **maior que 7KB**. Caso seja menor que 7KB será necessário, primeiramente, realizar a exportação do mesmo via **Internet Explorer.** Abaixo as orientações de como realizar a exportação:  
       - [RH - RM - FOP - eSocial - Middleware - Como realizar exportação do Certificado Digital A1 no Internet Explorer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11335944332311-RH-RM-FOP-eSocial-Middleware-Como-realizar-exporta%C3%A7%C3%A3o-do-Certificado-Digital-A1-no-Internet-Explorer?source=search)  
2. Realize a importação do certificado no RM, conforme demonstrado no artigo abaixo:  
   - [RH - RM - FOP - eSocial - Middleware: Certificado Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009264782-RH-RM-FOP-eSocial-Middleware-Certificado-Digital?source=search)  
3. Caso o erro persista, após realizar todos os passos acima, será necessário reiniciar os serviços do TSS;  
4. Em seguida, acesse **Configurações | Parametrizador | Esocial | Integração com Middleware | Certificado Digital** e clique no botão **Atualizar Certificado TSS** e avance até concluir.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12887047110295)

5. Após, envie ao eSocial novamente.  
  
**Saiba mais:**Para mais informações acesse: - [RH - RM - FOP - eSocial - Modelos de Certificado Digital válidos para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007865172-RM-eSocial-Modelos-de-Certificado-Digital-v%C3%A1lidos-para-o-eSocial?source=search)  
- [RH - RM - FOP - eSocial - Middleware - Certificado Digital A3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11333824146327-RH-RM-FOP-eSocial-Middleware-Certificado-Digital-A3)  
- [RH - RM - FOP - eSocial - Certificado Digital Middleware: Erro ao consultar/cadastrar entidade no TSS. IE inválida](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409144283927-RH-RM-FOP-eSocial-Certificado-Digital-Middleware-Erro-ao-consultar-cadastrar-entidade-no-TSS-IE-inv%C3%A1lida?source=search)  
- [RH - RM - FOP - eSocial - Erro 607 na integração com governo: O número de inscrição do transmissor deverá ser igual ao CNPJ/CPF do certificado utilizado para o envio do lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11628969703831-RH-RM-FOP-eSocial-Erro-607-na-integra%C3%A7%C3%A3o-com-governo-O-n%C3%BAmero-de-inscri%C3%A7%C3%A3o-do-transmissor-dever%C3%A1-ser-igual-ao-CNPJ-CPF-do-certificado-utilizado-para-o-envio-do-lote?source=search)
