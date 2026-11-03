---
article_id: 6449793366039
category: Financeiro
content_hash: b0bf0ee84f559a4afefbd49c517808d83cf6cda3b56e3fcd65fb0867281887a1
fetched_at: '2026-06-28T22:38:00.942397+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como testar sem customizações
  do RpoCustom
type: support-article
updated_at: '2026-01-08T13:29:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6449793366039-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-testar-sem-customiza%C3%A7%C3%B5es-do-RpoCustom
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22854254642327) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como testar sem customizações do RpoCustom?  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - SIGAFIN - A partir da versão 12.1.33   
  
**Solução**  
A segregação de RPOs introduziu o **RPO Custom**, onde todas as funções de usuário e recursos customizados são armazenados separadamente do código padrão TOTVS.

Embora existam chaves como `IXBLOG=NORUN` ou o **Catálogo de Personalização (CFGA030)**, estas ferramentas controlam apenas a execução de Pontos de Entrada (Entry Points). Elas **não impedem** a execução de funções de usuário (`U_`) chamadas diretamente por gatilhos, validações de campo ou fórmulas configuradas no **Dicionário de Dados (SX3/SX7/SXB)**.

Para garantir que **nenhuma** customização seja executada durante um diagnóstico de erro no padrão, deve-se inviabilizar o acesso do Application Server ao arquivo de customizações.

**Passos**

1. Identifique o caminho do arquivo de customizações na chave `RPOCustom` dentro da seção de ambiente no arquivo `appserver.ini`.
2. Com os serviços do Protheus parados, acesse a pasta física do RPO.
3. **Renomeie o arquivo** do RPO Custom (exemplo: altere de `custom.rpo` para `custom.rpo.teste`).

   * **Nota:** O renomeio serve exclusivamente para fins de teste, garantindo que o sistema não encontre o repositório de customizações e execute apenas o código nativo contido no RPO Default.
4. Reinicie o Application Server.
5. Realize os testes necessários para validar se o sintoma persiste no ambiente padrão.
6. Após a validação, retorne o nome original do arquivo e reinicie o serviço para reativar as funções de usuário.

**Saiba mais**  
[RpoCustom](https://tdn.totvs.com/display/tec/RpoCustom)  
[RPOs Segregados](https://tdn.totvs.com/display/tec/Application+Server+-+RPOs+Segregados)  
[Catálogo de Personalização (CFGA030)](https://tdn.totvs.com/pages/releaseview.action?pageId=382541900)
