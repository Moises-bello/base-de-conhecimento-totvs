---
article_id: 4404245148823
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b169a302d35a105e25f8bb59ce55ba24d5764741bfc8daf9a6f302924190186d
fetched_at: '2026-06-28T22:38:39.898041+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Nota sobre numeração única
  para pedido de vendas
type: support-article
updated_at: '2025-12-23T21:57:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404245148823-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Nota-sobre-numera%C3%A7%C3%A3o-%C3%BAnica-para-pedido-de-vendas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19647030455063) Tempo aproximado para leitura: 00:07:00 min**

**Dúvida**  
É possível trabalhar com numeração única de pedidos de vendas (**MATA410**) quando se trabalha com filiais, não permitindo que cada uma tenha sua numeração própria?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**  
Hoje, a numeração do pedido de vendas  é gerida pelo *License Server*, caso tenha a configuração do [SpecialKey](https://tdn.totvs.com/display/public/framework/SpecialKey) se houver filiais, o sistema irá informar a filial e o número do pedido relacionado aquela filial no momento, não há um tratamento específico para numeração única como no caso da geração da nota (**MATA461**), e sim ajuste na tabela de de controle de numeração (**APCFG110**).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19647030474135)

[Ajuste do Controle de Numeração automática](https://tdn.totvs.com/pages/releaseview.action?pageId=235570751#Valida%C3%A7%C3%B5es-Ajuste%20da%20numera%C3%A7%C3%A3o%20autom%C3%A1tica)

Exemplo:

Uma empresa com duas Filiais:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404244568983)

Veja que a numeração da filial 01,tabela inferior, a próxima numeração do pedido será 001141 e o próximo número mais um , será 001142, indicado na tabela superior, já na filial 02, a próxima numeração do pedido será 000018 e o próximo mais um é 000019.

Seguindo pela tabela de controle de numeração, conforme o exemplo acima, é possível ajustar a numeração da filial 02 para seguir com a mesma numeração da filial 01, se assim for desejado.

Caso após o ajuste da chave do **SpecialKey** e do Controle de Numeração da "SC5", ainda ocorrer o incidente, verifique o **"Passo 1 - License Server"** da documentação [Ajuste do Controle de Numeração automática](https://tdn.totvs.com/pages/releaseview.action?pageId=235570751#Valida%C3%A7%C3%B5es-Ajuste%20da%20numera%C3%A7%C3%A3o%20autom%C3%A1tica), realize o ajuste novamente da numeração da **"SC5"**, efetue o backup do arquivo **"LSNumber.val"** pare o serviço do license server e delete o arquivo **"LSNumber.val".**

E para que não haja a perda dessa numeração, pode-se implementar o ponto de entrada [**CRIASXE**](https://tdn.totvs.com/x/y-1n)

Para tratar o ajuste de numeração, basta seguir as informações da documentação:  [**MP-FAT-Numeração-automática-incorreta-nas-Tabelas-do-Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000582027-MP-FAT-Numera%C3%A7%C3%A3o-autom%C3%A1tica-incorreta-nas-Tabelas-do-Protheus)

**Obs:** Não é indicado o ajuste o inicializador padrão do campo **C5\_NUM** (**GETSXENUM("SC5","C5\_NUM")** ) para travar a busca da numeração para ambas as filiais , pois esta validação faz a busca diretamente na tabela de controle de numeração, qualquer interferência na validação, poderá não efetuar a busca corretamente, podendo ocasionar perda da numeração.

**Saiba mais:**   
[**MP-FAT-TAMANHO-DO-CAMPO-C5-NUM**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046826433-MP-FAT-TAMANHO-DO-CAMPO-C5-NUM)

[**MP - ADVPL - Rotina automática mata410 com getsxenum**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021116031-MP-ADVPL-Rotina-autom%C3%A1tica-mata410-com-getsxenum)
