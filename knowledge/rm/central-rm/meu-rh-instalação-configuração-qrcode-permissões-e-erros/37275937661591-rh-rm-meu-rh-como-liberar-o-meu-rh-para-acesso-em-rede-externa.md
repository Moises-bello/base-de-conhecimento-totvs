---
article_id: 37275937661591
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: d99a9f9d54883d84434ffbbcce4f09536ab320a5bb75ca5e72a00777391f8b80
fetched_at: '2026-06-28T22:47:29.449561+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Como liberar o Meu RH para acesso em rede externa
type: support-article
updated_at: '2025-12-26T18:47:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37275937661591-RH-RM-Meu-RH-Como-liberar-o-Meu-RH-para-acesso-em-rede-externa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37275937652887) Tempo aproximado para leitura: **00:03:03 min**  
  
**Dúvida**  
O **Meu RH** está funcionando apenas internamente, em **localhost**. Como liberar o acesso ao **Meu RH** para a rede externa, utilizando **HTTPS**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**  
Caso seja identificado que o **Meu RH** já esteja funcionando corretamente em **localhost** ou via **rede interna**, para disponibilizá-lo para acesso externo utilizando **HTTPS**, é necessário, inicialmente, providenciar um **Certificado Digital SSL válido**.

Para isso, siga as instruções disponíveis na documentação abaixo:  
[RH - RM - Meu RH -  Escolhendo e testando um certificado HTTPS/SSL válido para o Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035159453-RH-RM-Meu-RH-Escolhendo-e-testando-um-certificado-HTTPS-SSL-v%C3%A1lido-para-o-Meu-RH)

Após a escolha do certificado, é necessário vinculá-lo ao **Meu RH**, conforme orientações da documentação:  
[RH - RM - Meu RH - Como configurar certificado SSL no portal Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20672026455319-RH-RM-Meu-RH-Como-configurar-certificado-SSL-no-portal-Meu-RH)  
  
Após a configuração e vinculação do certificado, a **publicação do site para acesso externo**, bem como as configurações de **DNS, Firewall, liberação de portas, escolha do certificado e demais recursos de infraestrutura**, são de responsabilidade da **equipe interna de TI/Infraestrutura da própria empresa**.  
Por este motivo, essas atividades estão fora do escopo do **suporte padrão TOTVS**.

Caso o cliente necessite de apoio nas etapas relacionadas à **Infraestrutura** (DNS, Firewall, publicação da URL, entre outras), esse serviço pode ser contratado junto à **Consultoria RM**. Para mais informações e orçamento, basta entrar em contato com a equipe de **Consultoria TOTVS**.
