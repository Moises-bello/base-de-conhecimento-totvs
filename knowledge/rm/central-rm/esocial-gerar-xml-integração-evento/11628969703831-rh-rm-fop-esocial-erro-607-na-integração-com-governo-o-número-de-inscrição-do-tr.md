---
article_id: 11628969703831
category: eSocial - Gerar XML/ Integração Evento
content_hash: c79915d3ce5da2830fdc692ec131ed6e03e9d0ac21c2264b99604ea8a1d5e3b4
fetched_at: '2026-06-28T22:47:12.154871+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 607 na integração com governo: O número de
  inscrição do transmissor deverá ser igual ao CNPJ/CPF do certificado utilizado para
  o envio do lote'
type: support-article
updated_at: '2024-12-30T15:43:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11628969703831-RH-RM-FOP-eSocial-Erro-607-na-integra%C3%A7%C3%A3o-com-governo-O-n%C3%BAmero-de-inscri%C3%A7%C3%A3o-do-transmissor-dever%C3%A1-ser-igual-ao-CNPJ-CPF-do-certificado-utilizado-para-o-envio-do-lote
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21787463430039) Tempo aproximado para leitura: **03:00:00 min** **Ocorrência**Ao transmitir os eventos para o eSocial, apresenta a mensagem **Erro 607: O número de inscrição do transmissor deverá ser igual ao CNPJ/CPF do certificado utilizado para o envio do lote.****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial- Todas as Versões.  
  
**Causa**Esse erro ocorre quando os dados do Transmissor não foi informada de acordo com o Certificado Digital (Contador ou Empresa) utilizado pela empresa.  
  
**Solução**Primeiramente, avalie se a empresa cadastrou corretamente o **Certificado Digital**. Após, realize um dos ajustes a seguir conforme o certificado digital e forma de envio utilizado:

****•  Envio pelo Middleware****

Para **importar** o certificado, realize os seguintes passos:

1. Acesse o menu **RH | Folha de Pagamento | eSocial | Certificado Digital**;
2. Clique em **Processos | Importar certificado digital**;
3. Selecione o certificado que deseja realizar a importação, digite a senha e cadastre uma descrição;
4. Clique no botão **Executar** para concluir o processo.

Já para **atualizar** o certificado, siga os passos abaixo:

1. Acesse o menu **RH | Folha de Pagamento | Configurações| Parametrizador | eSocial**;
2. Avance até a etapa **Integração com *Middleware***;
3. Clique na aba **Certificado Digital**;
4. Ao lado do campo **Certificado**, clique nos três pontinhos conforme imagem abaixo;  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21787431798935)
5. Será apresentada a lista de certificados importados/cadastrados. Selecione o certificado desejado;
6. Reinicie os serviços TSS;
7. Clique no botão **Atualizar Certificado TSS**. Será exibida mensagem conforme abaixo;  
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21787463447575)
8. Avance o *Wizard* até sua conclusão;
9. Em seguida, tente uma nova transmissão.

**• Envio pelo TAF**  
Para solucionar o incidente, deverá realizar a parametrização conforme artigo a seguir:

* [TAF - TSS - Erro 607: O número de inscrição do transmissor deverá ser igual ao CNPJ/CPF do certificado utilizado para o envio do lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052077593-TAF-TSS-Erro-607-O-n%C3%BAmero-de-inscri%C3%A7%C3%A3o-do-transmissor-dever%C3%A1-ser-igual-ao-CNPJ-CPF-do-certificado-utilizado-para-o-envio-do-lote)

**Saiba Mais**  
Para mais informações acesse: 

* [Como realizar exportação do Certificado Digital A1 no Internet Explorer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11335944332311-RH-RM-FOP-eSocial-Middleware-Como-realizar-exporta%C3%A7%C3%A3o-do-Certificado-Digital-A1-no-Internet-Explorer?source=search)
* [Middleware - Certificado Digital A3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11333824146327-RH-RM-FOP-eSocial-Middleware-Certificado-Digital-A3-?source=search)
