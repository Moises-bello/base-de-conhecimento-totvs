---
article_id: 36090120212247
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 331b5792a94bad8782faa26285274202fca29bb6e7d1503370f3f8eed06507ca
fetched_at: '2026-06-28T22:37:22.879539+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help AJUDA:OBRIGAT
  Um ou mais campos obrigatórios não foram preenchidos no encerramento da medição
type: support-article
updated_at: '2025-11-18T11:44:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36090120212247-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-AJUDA-OBRIGAT-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-no-encerramento-da-medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36090120201623) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Help AJUDA:OBRIGAT  
Um ou mais campos obrigatórios não foram preenchidos. xxxxxxxxxxxxxxxxxx -> xxxxxxxxxx  
Nome do Campo

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Causa**  
Esse incidente normalmente ocorre quando é configurado como obrigatório um dos campos da tabela de Pedido de compra(SC7) ou Pedido de Venda(SC5/SC6), que são gerados no encerramento da medição. No entanto o campo referente não foi preenchido na medição, não sendo levada a informação para o pedido, impedindo a gravação do campo no pedido, e resultando na exibição do Help mencionado.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Caso no encerramento da Medição seja gerado um Pedido de Compra, localize no configurador do sistema o campo da rotina de Pedido de compras (**SC7)** indicado na mensagem do Help**.** Em seguida**,** retire a obrigatoriedade deste campo no configurador do sistema, salve as alterações e realize um novo teste.

Outra possibilidade é preencher, na medição, o campo correspondente ao indicado na mensagem de help (caso exista). Dessa forma, o valor será gravado corretamente no Pedido, evitando que o help seja exibido.

2. Caso no encerramento da Medição seja gerado um Pedido de Venda localize no configurador do sistema o campo indicado na mensagem do Help , na tabela (**SC5/SC6).** Em seguida**,** retire a obrigatoriedade deste campo no  configurador do sistema, salve as alterações e realize um novo teste.

Outra possibilidade é preencher, na medição, o campo correspondente ao indicado na mensagem de help (caso exista). Dessa forma, o valor será gravado corretamente no Pedido, evitando que o help seja exibido.

Por padrão, o sistema preenche apenas os campos do Pedido que são obrigatórios no padrão original do sistema.

Demais campos da tabela SC7 ou SC5/SC6 de Pedido que foram colocados como obrigatório além dos que já são poe padrão, para seus preenchimentos na geração do Pedido pelo Medição, podem ser preenchidos através de customização de Ponto de Entrada.

Abaixo segue artigo disponível com os pontos de entrada da Rotina de medição contendo o que pode ser utilizado para preenchimento de campos nos Pedidos gerados:

- [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o?source=search)

- CN121PED - [DT\_PE\_CN121PED\_Tratamento\_especifico\_antes\_da\_geração\_do\_pedido\_de\_compra](https://tdn.totvs.com/pages/viewpage.action?pageId=271385565)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o?source=search)

CN121PED - [DT\_PE\_CN121PED\_Tratamento\_especifico\_antes\_da\_geração\_do\_pedido\_de\_compra](https://tdn.totvs.com/pages/viewpage.action?pageId=271385565)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
