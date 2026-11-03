---
article_id: 38958778694167
category: Ferramentas
content_hash: 491eb7ebe46092b52aec292dada792f3c5964098899d6beadc78beaad850854d
fetched_at: '2026-06-28T22:42:18.085919+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework – Wizard Smartlink – Configuração do Smartlink em ambiente de Homologação
  e Desenvolvimento
type: support-article
updated_at: '2026-04-10T14:01:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38958778694167-Framework-Wizard-Smartlink-Configura%C3%A7%C3%A3o-do-Smartlink-em-ambiente-de-Homologa%C3%A7%C3%A3o-e-Desenvolvimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38958778664983) Tempo aproximado para leitura: 00:02:10 min  
  
**Dúvida**  
O que é o SmartLink e como configurar quando apresenta o Wizard ao abrir o Protheus em ambientes não produtivos?  
  
**Ambiente**  
Cross Segmento - TOTVS Framework (Linha Protheus) - Wizard Smartlink  
  
**Solução**  
O Smartlink é uma ferramenta nativa, presente a partir da LIB de agosto/2025, que faz a comunicação do ambiente Protheus com a Totvs para coleta de métricas através do Credential Helper.

No ambiente de produção o Smartlink é configurado nativamente, sendo assim, quando é realizado o tombamento do ambiente de produção para um ambiente de homologação/teste, é identificado na comunicação do Smartlink com a Totvs que o ID cadastrado já está em uso, neste caso, pelo ambiente de produção, desta maneira, a tela do Wizard é apresentada no ambiente que recebeu o tombamento para que seja configurado um novo ID.

Para configurar o Wizard, realize os seguintes passos:

1. Na tela Configurador do SmartLink (Wizard), selecione a opção "Criar novo ambiente" e realize o cadastro do ambiente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38958778667031)

2. Após concluir, acesse o Configurador e acesse a rotina Configuração do Tipo de Ambiente.
3. Altere a configuração para Homologação. Caso já tenha um ambiente definido como Homologação, altere para Desenvolvimento.

**Obs.:** O Smartlink trabalha com 1 ambiente de Produção e 1 de Homologação, mas permite vários de Desenvolvimento, sendo assim, caso tenha 3 ou mais ambientes de testes, configure-os como Desenvolvimento.

4. Caso não encontre a rotina Configuração do Tipo de Ambiente no menu de seu Configurador, cadastre a função CFGA750.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38958803496087)

**Obs.:** Se o ambiente de Produção for tombado novamente para um ambiente de Homologação/Teste, os dados do Smartlink serão sobrepostos e o Wizard será apresentado. Será necessário reconfigurar e selecionar o ambiente previamente configurado.

 **Artigos relacionados**

[O que é o Smartlink?](https://tdn.totvs.com/pages/releaseview.action?pageId=1037967715)

[Protheus x Credential Helper](https://tdn.totvs.com/display/public/framework/Protheus+x+Credential+Helper)
