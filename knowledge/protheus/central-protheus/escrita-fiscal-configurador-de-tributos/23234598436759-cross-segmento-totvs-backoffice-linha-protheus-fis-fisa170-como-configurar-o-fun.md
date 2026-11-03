---
article_id: 23234598436759
category: Escrita Fiscal - Configurador de Tributos
content_hash: e62cf8185aa230fea9402839ab7bf6b3e4c3a2d4b47d7662f85c695439daad50
fetched_at: '2026-06-28T22:39:17.420343+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como configurar
  o Fundo Reforma do estado do RS?
type: support-article
updated_at: '2024-11-18T11:59:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23234598436759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-o-Fundo-Reforma-do-estado-do-RS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23234598415127) Tempo aproximado para leitura: **08:00min** **Dúvida**Como configurar o Fundo Reforma do estado do RS?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

MV\_ESTADO = RS

Todos os fundos estão sendo tratados no Configurador de Tributos

<https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10>

Calculo  
   
1.000,00 : 0,83 = 1.204,82 (Os 83% é a diferença entre 100% e 17% da alíquota do RS)  
1.204,82 x 0,17 = 204,82 (17% é a alíquota interna de ICMS do RS)  
204,82 x 0,10 = 20,48 (Esse é o valor do Fundo de Reforma do Estado)

FISA170

Inserir o ID \_ fundo de reforma

![](https://totvssuporte.zendesk.com/attachments/token/0jrloyDc4BNE4zSCdXSLAJ4EO/?name=image.png)

Perfil de Produtos

![](https://totvssuporte.zendesk.com/attachments/token/9o71RKO8m6ViTvsac7ps9OMUe/?name=image.png)

O produto precisa estar cadastrada no SB1 ( cadastro de produtos )

Perfil de operação = 000030

![](https://totvssuporte.zendesk.com/attachments/token/25dUeL7RBZmL8WpNlWPxEGO1z/?name=image.png)

Perfil de Participantes

![](https://totvssuporte.zendesk.com/attachments/token/7ZIbECri0uOlGUgst1nQQ0etx/?name=image.png)

Pode fazer a inclusão através do Facilitador siga a documentação

2.2.7[Facilitadores](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10#CFGTRIBConfiguradordeTributos12.1.22.10-Facilitadores)

Perfil origem destino

![](https://totvssuporte.zendesk.com/attachments/token/XQVguLE2evBJk9moan0xBPvEB/?name=image.png)

Para cadastrar a regra de base de calculo, primeiro precisa cadastrar a alíquota interna do estado RS = 17%

Cadastro regra de alíquota

![](https://totvssuporte.zendesk.com/attachments/token/MhnfcOnElYASqZGEJme6yPaje/?name=image.png)

Alíquota 10%

![](https://totvssuporte.zendesk.com/attachments/token/6LDjLGbJm7MxyV7OXyqYp6TcZ/?name=image.png)

Regra de Base de Calculo

![](https://totvssuporte.zendesk.com/attachments/token/IZ8puXt3iWvMfrIUhG86wWYEN/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/SKlrcTGUyv48hXi5tu3mQsvFX/?name=image.png)

Regra de escrituração de acordo com a sua necessidade

[Cadastro de Regra de Escrituração](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10#CFGTRIBConfiguradordeTributos12.1.22.10-CadastrodeRegradeEscritura%C3%A7%C3%A3o)

Regra de Calculo Documentos Fiscais

![](https://totvssuporte.zendesk.com/attachments/token/ubdqUtOyBkIKbTTLYua9t3I4P/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/Hj43ej8dNLCt1ZnkAhbmFgyBR/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/wbECao71vrip6LpJSecoYkRB0/?name=image.png)

O configurador usa o TES para fazer o lançamento da nota fiscal e precisa que o CFOP esteja no perfil de operação

![](https://totvssuporte.zendesk.com/attachments/token/n5bAgLdrJWLSTe3oDN1Q17N0R/?name=image.png)

Pedido de Vendas

![](https://totvssuporte.zendesk.com/attachments/token/OTD5RlzKlgk37H5HNwTh3hPOY/?name=image.png)
