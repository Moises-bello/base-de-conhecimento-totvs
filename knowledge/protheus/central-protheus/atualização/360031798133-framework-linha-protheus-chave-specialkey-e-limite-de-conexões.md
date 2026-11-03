---
article_id: 360031798133
category: Atualização
content_hash: f744e03f9dc5d73c0682c597dfb7e8e36edd1f68cf1cff87a59c50897f18e0fe
fetched_at: '2026-06-28T22:42:21.206458+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Chave SpecialKey e limite de conexões
type: support-article
updated_at: '2024-03-26T12:38:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031798133-Framework-Linha-Protheus-Chave-SpecialKey-e-limite-de-conex%C3%B5es
---

**Dúvida**Qual a finalidade da chave SpecialKey no arquivo appserver.ini?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - AppServer - Todas as versões  
  
**Solução**A chave SpecialKey define uma string que é concatenada à string básica nas funções de controle para acesso simultâneo (semáforo). Essa chave **deve** ser definida em **ambientes com mais de um diretório de dicionário**(SX). No entanto, para cada um desses ambientes, um **SpecialKey** diferente deve ser definido. Para ambientes que utilizem a mesma pasta Protheus\_Data, deve ser utilizada a mesma SpecialKey.  
  
Se isso não for feito, o sistema pode gerar erros, por exemplo, de **Limite de conexões do usuário excedido**, mesmo que o número máximo de conexões do usuário não tenha sido excedido.  
  
**Exemplo**

|  |
| --- |
| `[AmbienteProd] SourcePath=C:\TOTVS 12\Microsiga\protheus\apo\ RootPath=C:\TOTVS 12\Microsiga\protheus_data StartPath=\system\ RpoDb=Top RpoLanguage=Portuguese RpoVersion=120 LocalFiles=CTREE Trace=0 Localdbextension=.dtc SpecialKey=AmbienteProd   [AmbienteTeste] SourcePath=C:\TOTVS 12\Microsiga\protheus\apo\ RootPath=C:\TOTVS 12\Microsiga\protheus_dataTeste StartPath=\systemTeste\ RpoDb=Top RpoLanguage=Portuguese RpoVersion=120 LocalFiles=CTREE Trace=0 Localdbextension=.dtc SpecialKey=AmbienteTeste   [AmbienteHomologa] SourcePath=C:\TOTVS 12\Microsiga\protheus\apoHomologa\ RootPath=C:\TOTVS 12\Microsiga\protheus_dataHomologa StartPath=\systemHomologa\ RpoDb=Top RpoLanguage=Portuguese RpoVersion=120 LocalFiles=CTREE Trace=0 Localdbextension=.dtc SpecialKey=AmbienteHomologa` |
