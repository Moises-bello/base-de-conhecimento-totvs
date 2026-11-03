---
article_id: 38581784659095
category: Customizações (ADVPL)
content_hash: 719c314c602004a43edb1ad596ab8e2a5c52812f1fd84bf3c25d4f9efb7dbea6
fetched_at: '2026-06-28T22:36:31.598245+00:00'
product: protheus
section_id: 1500001533641
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Aumentar tamanho
  de Query para uso no Protheus
type: support-article
updated_at: '2026-02-24T18:02:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38581784659095-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Aumentar-tamanho-de-Query-para-uso-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38581778566551) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como alterar a validação do limite de tamanho de query (em bytes) executada por meio de uma aplicação AdvPL no TOTVS AppServer?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões

**Solução**  
A chave `MaxQuerySize` permite configurar o limite de tamanho de query, em bytes, que pode ser executada pelas aplicações. Essa configuração deve ser inserida no arquivo `appserver.ini` do TOTVS AppServer.

A parametrização pode ser especificada na seção `[General]` (para afetar globalmente todos os ambientes) ou diretamente na seção específica do ambiente (Environment) em uso, atuando unicamente sobre ele.

**Passos**  
Pare o serviço do TOTVS AppServer do ambiente que será configurado.

1. Acesse o diretório de instalação do AppServer.
2. Edite o arquivo `appserver.ini` com um editor de texto de sua preferência.
3. Localize a seção `[General]` ou a seção específica do seu ambiente (exemplo: `[P12]`).
4. Adicione ou altere a chave `MaxQuerySize`, informando o limite desejado em bytes.

   * *Exemplo de uso:* `MaxQuerySize=31960`
5. Salve as alterações realizadas no arquivo `appserver.ini`.
6. Reinicie o serviço do TOTVS AppServer para que a nova configuração seja validada.

**Saiba mais**  
[TDN - Chave MaxQuerySize](https://tdn.totvs.com/display/tec/MaxQuerySize)
