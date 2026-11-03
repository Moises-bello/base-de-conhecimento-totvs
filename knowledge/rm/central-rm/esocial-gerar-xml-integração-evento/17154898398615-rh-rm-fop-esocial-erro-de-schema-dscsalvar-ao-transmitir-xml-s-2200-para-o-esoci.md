---
article_id: 17154898398615
category: eSocial - Gerar XML/ Integração Evento
content_hash: 9bf14f31a59d892193ca87778b9c0fffc83f889512d3c8ac8c32cce61e382d46
fetched_at: '2026-06-28T22:47:12.281489+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erro de schema dscSalVar ao transmitir XML S-2200
  para o eSocial
type: support-article
updated_at: '2024-09-23T12:13:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17154898398615-RH-RM-FOP-eSocial-Erro-de-schema-dscSalVar-ao-transmitir-XML-S-2200-para-o-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17177292621463) Tempo aproximado para leitura: **00:03:00 min**  
**Ocorrência**  
Ao transmitir o XML S-2200 para o governo ocorre erro de Schema dscSalVar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17150106295831)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**   
O erro ocorre quando é gerado no XML S-2200 uma informação que não condiz com o leiaute. De acordo com a informação do leiaute a *tag* tem que ser gerada com o tamanho de pelo menos 1 caractere e tamanho máximo 999.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17174905179287)**

**Solução**Para solucionar o erro, recomendamos seguir os passos a passos abaixo:   
1. Identifique no XML a *tag* **dscSalVar**;

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17153386857495)**

2. Identifique o cadastro do funcionário, acesse **Salário/Jornada |** **Descrição do Salário Variável** e verifique se há alguma informação cadastrada indevidamente, como por exemplo, algum espaçamento dentro do campo que está fazendo com que a *tag* seja gerada incorretamente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17153299455383)

3. Salve as alterações e gere novamente o XML.

**Saiba mais**Para mais informações acesse:[Mapeamento](https://tdn.totvs.com/display/public/LRM/Mapeamento+dos+Eventos) [dos Eventos](https://tdn.totvs.com/display/public/LRM/Mapeamento+dos+Eventos)
