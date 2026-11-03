---
article_id: 34725876989079
category: SIGAACD - Automação e Coleta de Dados
content_hash: 45af25f8947c1ea1e2cd89388e36bb10b9727f1171e09191bcc62267f7120e03
fetched_at: '2026-06-28T22:39:12.870252+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - O campo CBC_QUANT
  deixa informar somente um digito.
type: support-article
updated_at: '2025-09-05T17:17:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34725876989079-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-O-campo-CBC-QUANT-deixa-informar-somente-um-digito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34725846037015) Tempo aproximado para leitura: **01:00:00 min**  
  
**Dúvida**  
Ao fazer a inclusão dos Lançamentos de Inventários na rotina (ACDA035), ao informar o campo CBC\_QUANT com mais de dois dígitos, o sistema não permiti digitar como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Para correção adequada desse incidente relatado, é necessário realizar o seguinte procedimento:

1. Primero acessar o configurador, na tabela CBC localizando o campo CBC\_QUANT e verificar se a Picture do campo está com preenchimento.
2. Segundo caso não tiver com a Picture do campo com preenchimento igual ao imagem abaixo: ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34725846037783)
3. Terceiro é necessário informar essa Picture @E 9,999,999.9999 no campo Formato, salva as informações do configurador e acessa a rotina novamente ACDA035, dessa forma o sistema permitir informar mais de um digito no campo quantidade.

**Saiba Mais**:

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Guia Pratico Automação e Coleta de Dados SIGAACD](https://tdn.totvs.com/pages/releaseview.action?pageId=235596139)

[Inventário por Produto (ACDV035 -SIGAACD)](https://tdn.totvs.com/pages/releaseview.action?pageId=780791398)
