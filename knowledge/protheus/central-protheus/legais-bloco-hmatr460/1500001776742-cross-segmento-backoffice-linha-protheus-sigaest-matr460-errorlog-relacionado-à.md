---
article_id: 1500001776742
category: LEGAIS - BLOCO H/MATR460
content_hash: 641c9e675d87338a57df6f5ed4d676a68a57fd604d14251638cc9912aab9c37b
fetched_at: '2026-06-28T22:42:15.125446+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Error.log
  relacionado à tabela H ao imprimir o relatório P7
type: support-article
updated_at: '2021-06-14T14:31:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001776742-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Error-log-relacionado-%C3%A0-tabela-H-ao-imprimir-o-relat%C3%B3rio-P7
---

**Dúvida**Ao gerar o MATR460 com a pergunta Gerar Arquivo Exp?" = Sim e "Nome do Arquivo de Exp" com preenchimento, ocorre o error.log:

*Alias does not exist: TRB\_R460 on RECLOCK(APLIB060.PRW)"* **ou** *"THREAD ERROR -*  
*H\_NOMEDATABELA: Error :  (S0001) (RC=-1) - [Microsoft][SQL Server Native Client 10.0][SQL Server]There is already an object named 'H\_NOMEDATABELA' in the database."*

Como corrigir estes erros quando apresentam?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17  
  
**Solução**

Para solucionar este erro, basta checar na APSU (ferramenta de visualização de dados) a tabela H\_ que está aberta. Quando ela está aberta e ocorre uma tentativa de geração do MATR460 com a pergunta "Gerar Arquivo Exp?" habilitada ocorre este erro. Então, basta fechá-la para gerar o MATR460 com sucesso.

**Fechando a tabela H\_ via APSDU:**

**![Fechando_tabela_H.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360103287034/Fechando_tabela_H.gif)**

**Observação:** A tabela H\_ tem um padrão de nomenclatura, para o correto funcionando, a mesma deve estar conforme a [documentação da geração do Bloco H.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059965954)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
