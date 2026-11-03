---
article_id: 17118508086679
category: eSocial - Middleware
content_hash: eb66ccedea6c02339f56f6f1097b5319bd25d5b2c8eb6ec2670b59e2feb3dd31
fetched_at: '2026-06-28T22:47:05.530465+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 402 na integração de eventos com Governo: The
  value ''XXXXX'' is invalid according to its datatype ''String'' - The Pattern constraint
  failed'
type: support-article
updated_at: '2024-10-23T11:01:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17118508086679-RH-RM-FOP-eSocial-Erro-402-na-integra%C3%A7%C3%A3o-de-eventos-com-Governo-The-value-XXXXX-is-invalid-according-to-its-datatype-String-The-Pattern-constraint-failed
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17118477780503) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Ao gerar XML de qualquer evento, é retornado a inconsistência: **O evento ID 'IDXXXXXXXXXXXXXXXXXXXXXXX' foi rejeitado pelo RET. Erro código 402:**  
**The 'http://www.esocial.gov.br/schema/lote/eventos/envio/v1\_1\_1:nrInsc' element is invalid - The value 'XXXXX' is invalid according to its datatype 'String' - The Pattern constraint failed..**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse erro ocorre após realizar a troca de um certificado digital vencido, por um novo dentro da validade. Sendo necessário atualizar no TSS o Número de Inscrição do Transmissor/Procurador (Outorga).

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Reiniciar os **Serviços do TSS**;  
2. Acessar **Configurações | Parametrizador | eSocial | Integração Middleware | Certificado Digital** e inserir um espaço em branco ou um ponto no campo Número de Inscrição do Transmissor/Procurador (Outorga);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17118256918039)

3. Clicar em **Atualizar Certificado TSS**, sendo exibido que todas as informações estão 'OK', avançar o Parametrizador para a última etapa e concluir para salvar o ajuste.

**Saiba mais:**  
Para maiores informações sobre, acesse:

* [RH - RM - FOP - eSocial - Middleware: Certificado Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009264782-RH-RM-FOP-eSocial-Middleware-Certificado-Digital?source=search)
* [RH - RM - FOP - eSocial - Modelos de Certificado Digital válidos para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007865172-RM-eSocial-Modelos-de-Certificado-Digital-v%C3%A1lidos-para-o-eSocial?source=search)
* [RH - RM - FOP - eSocial - Middleware - Como realizar exportação do Certificado Digital A1 no Internet Explorer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11335944332311-RH-RM-FOP-eSocial-Middleware-Como-realizar-exporta%C3%A7%C3%A3o-do-Certificado-Digital-A1-no-Internet-Explorer?source=search)
