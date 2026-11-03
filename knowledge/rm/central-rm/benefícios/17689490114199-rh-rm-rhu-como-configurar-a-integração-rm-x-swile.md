---
article_id: 17689490114199
category: Benefícios
content_hash: c02c6ab714da75b042c0fb42ba16047ad4477f89ea28f525b1490fe4cfa86822
fetched_at: '2026-06-28T22:47:17.051461+00:00'
product: rm
section_id: 1500000861362
source: central-rm
title: RH - RM - RHU - Como configurar a integração RM x Swile
type: support-article
updated_at: '2024-10-01T13:56:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17689490114199-RH-RM-RHU-Como-configurar-a-integra%C3%A7%C3%A3o-RM-x-Swile
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17689518442519) Tempo aproximado para leitura: **00:02:00 min****Dúvida**RH - RM - RHU - Como configurar a integração RM x Swile?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas  - **12.1.2302.141** e **superiores.**  
  
**Solução**Para configurar a integração RM x Swile e realizar o envio de dados de funcionários e pedidos para a Swile é necessário marcar o parâmetro '**Ativar Integração com Swile**', em **Totvs Gestão de Pessoas | Configurações | Parâmetros | Configurações | Integração com Terceiros e APIs | APIs | Integração API Swile**. Após marcar o parâmetro, serão habilitados os campos para preenchimento, conforme a imagem abaixo:

![](https://tdn.totvs.com/download/attachments/737546308/image2023-4-5_17-21-4.png?version=1&modificationDate=1680726065063&api=v2)

- Após tal configuração, será necessário acessar **Totvs Gestão de Pessoas | Valorização | Controle de Benefícios | Benefícios e Remuneração Variável** e cadastrar os benefícios abaixo que serão fornecidos para os funcionários, conforme exemplo da imagem abaixo:

![](https://tdn.totvs.com/download/attachments/737546308/image2023-4-5_17-23-58.png?version=1&modificationDate=1680726238667&api=v2)

- Além deste cadastro, também é necessário acessar **Totvs Gestão de Pessoas | Valorização | Controle de Benefícios | Tabelas Auxiliares | De/Para Benefícios Terceiro**, e vincular os Benefício RM x Benefício Swile conforme exemplo da imagem abaixo:

![](https://tdn.totvs.com/download/attachments/737546308/image2023-4-5_16-59-11.png?version=1&modificationDate=1680724752197&api=v2)

![](https://tdn.totvs.com/download/attachments/737546308/image2023-4-5_17-0-22.png?version=1&modificationDate=1680724822743&api=v2)  
  
Obs: Caso a opção **De/Para Benefícios Terceiro** não esteja disponível, será necessário validar se o menu está liberado em ***Serviços Globais > Segurança > Perfis > Sistema: Gestão de Pessoas > Edite o perfil > Acesso a Menus > Verifique se os menus referente ao campo [04.01.05.10.01] estão com acessos liberados:***  
  
![De Para Beneficio Terceiro.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/21704865512087)

**Saiba Mais**  
Para maiores informações sobre a integração RM x Swile, acesse:

- [Integração TOTVS RM X Benefício Flexíveis Swile](https://tdn.totvs.com/pages/releaseview.action?pageId=737546308)
