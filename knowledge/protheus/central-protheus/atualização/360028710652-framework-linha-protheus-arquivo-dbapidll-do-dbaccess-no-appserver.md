---
article_id: 360028710652
category: Atualização
content_hash: 0f10fc3716a08fe23908107a05e64fbe0e1f62a8bc0c8b7f983e1b62b6a0d70d
fetched_at: '2026-06-28T22:42:21.193061+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Arquivo dbapi.dll do DBAccess no AppServer
type: support-article
updated_at: '2024-03-26T13:13:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028710652-Framework-Linha-Protheus-Arquivo-dbapi-dll-do-DBAccess-no-AppServer
---

**Dúvida**  
Como devo atualizar o arquivo dbapi.dll do DBAccess no meu AppServer?  
  
**Ambiente**  
Protheus - AppServer - A partir da versão 12  
  
**Solução**O arquivo dbapi.dll é uma biblioteca de integração do AppServer com o DBAccess. Para atualizá-lo, siga o procedimento abaixo:  
  
1. **Pare** os serviços do **Protheus**  
2. Na pasta do executável do Application Server, faça um **backup** do arquivo **dbapi.dll** atual e remova-o desta pasta  
3. **Baixe** o pacote mais recente do **DBAccess** no Portal do Cliente (conforme a arquitetura que você utiliza, 32 bits ou 64 bits)  
4. Do DBAccess baixado e descompactado, **copie** o arquivo **dbapi.dll** para a pasta do Application Server, respeitando a arquitetura do Application Server e renomeando o arquivo se necessário  
  
- Em versões anteriores a 19.2.1.0, a DBAPI 64 Bits tem sua nomenclatura definida como "dbapi64.dll"  
- A partir da versão 19.2.1.0 do TOTVS | DBAccess, a DBAPI 64 Bits passa a ser disponibilizada na pasta client e sua nomenclatura muda de "dbapi64.dll" para apenas "dbapi.dll".  
  
5. **Reinicie** os serviços do **Protheus**  
  
Observação: Para requisitos, procedimentos em outros sistemas operacionais e demais informações, favor consultar o link da documentação completa:  
<https://tdn.totvs.com/display/tec/DBAccess+-+Como+atualizar+a+biblioteca+DBAPI>
