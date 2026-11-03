---
article_id: 115001426067
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 1d1f1307c74f8d79134d210c37e4657115501828048cae1afaf0f1838331e576
fetched_at: '2026-06-28T22:38:30.040094+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Tentativa de
  reservar registro no Alias em EOF Stack de chamadas em MSRLOCK.eof
type: support-article
updated_at: '2023-06-01T20:03:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001426067-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Tentativa-de-reservar-registro-no-Alias-em-EOF-Stack-de-chamadas-em-MSRLOCK-eof
---

**Ocorrência:**

O que fazer quando aparece a mensagem de MSRLOCK.eof em um processo?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.

**Solução:**

O controle de transação é uma ferramenta importante que garante a integridade de dados quando uma determinada operação é realizada no Banco de Dados.

![](http://tdn.totvs.com.br/download/attachments/235575485/image2017-9-27_10-28-34.png?version=1&modificationDate=1506518915000&api=v2)  
O Protheus possui o parâmetro **MV\_TTS** que quando ativado garante que este processo exista nos processos críticos de transação de arquivos. Detalhes: Controle de Transação - MV\_TTS

As alternativas existentes quando da atualização de tabelas são :

* Efetivar a transação - quando realizada com sucesso.
* Voltar a status anterior (rollback) - desfaz toda a transação iniciada quando o final da transação não foi concluído com sucesso. Isto garante a total integridade dos dados.

A mensagem "**EOF Stack em MSRLOCK**" indica que a rotina tentou reservar um registro para ser manipulado no processamento; mas o ponteiro da tabela estava em FIM DE ARQUIVO (MODO EOF) pois não localizou o dado procurado na Tabela.

Para maiores informações sobre a ocorrência "Tentativa de reservar registro no Alias x em EOF Stack" consulte nossa documentação através do Link:

[FAT0240 EOF Stack de chamadas em MSRLOCK.eof Controle de transaçoes Habilitado](https://tdn.totvs.com/x/vZgKDg)
