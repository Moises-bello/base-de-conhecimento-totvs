---
article_id: 38156901664535
category: Financeiro - Movimentos Bancários
content_hash: d552576c7f5496ee8498044afd35faab0c5faed68fe9534f7f5198a049a00a8f
fetched_at: '2026-06-28T22:37:31.835541+00:00'
product: protheus
section_id: 35057601824535
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA100 - HELP:MF100GRVFK
type: support-article
updated_at: '2026-02-04T12:52:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38156901664535-Cross-Segmentos-Backoffice-Linha-Protheus-FINA100-HELP-MF100GRVFK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38156901658903) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Ao realizar a movimentação bancária, é apresentado o HELP:MF100GRVFK  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
O help MF100GRVFK é acionado quando ocorre falha na gravação das tabelas de FKs.

Para esse cenário, é necessário realizar as seguintes validações:

1. Avaliar o compartilhamento das tabelas, conforme a documentação disponível no link abaixo:  
   [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Reestruturação da tabela SE5 na família de tabelas FKx.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020874791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Reestrutura%C3%A7%C3%A3o-da-tabela-SE5-na-fam%C3%ADlia-de-tabelas-FKx)
2. Verificar se houve alteração no tamanho de algum campo que pertença a um grupo de campos. Nesses casos, o ajuste deve ser realizado no grupo de campos como um todo, e não apenas na tabela específica. Conforme a documentação disponível no link abaixo:

   [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Help: TITNAOXADO ao cancelar a baixa do título](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053001473-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Help-TITNAOXADO-ao-cancelar-a-baixa-do-t%C3%ADtulo)
3. Validar se houve criação de campos customizados ou a aplicação de alguma customização específica para o processo. Recomenda-se a realização de testes em ambiente sem customizações, a fim de confirmar se o comportamento persiste.

   [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como desativar customizações via Rpo Custom](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6449793366039-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-desativar-customiza%C3%A7%C3%B5es-via-Rpo-Custom?source=search)

**Importante**

O help sempre indica o campo relacionado à inconsistência. No exemplo apresentado, o erro está associado ao campo **FK8\_DEBITO**. Nesse caso, a análise deve ser direcionada, inicialmente, ao campo mencionado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38156963789079)

No escopo de atendimento padrão, atuamos na resolução de problemas pontuais relacionados às rotinas do sistema. Dessa forma, a análise de base não está contemplada em nosso escopo de suporte, sendo necessária a avaliação pelo departamento de TI da empresa ou por um analista in loco.
