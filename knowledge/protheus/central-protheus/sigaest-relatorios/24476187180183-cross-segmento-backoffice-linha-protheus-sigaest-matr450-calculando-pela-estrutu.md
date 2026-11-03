---
article_id: 24476187180183
category: SIGAEST - RELATORIOS
content_hash: ff34282b78c315b02043d53ba2bea501c77d0c044fe2248790c9810134c1fe6e
fetched_at: '2026-06-28T22:39:06.159064+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR450 calculando
  pela Estrutura apresenta componente que não foi consumido na OP
type: support-article
updated_at: '2025-03-12T12:26:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24476187180183-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR450-calculando-pela-Estrutura-apresenta-componente-que-n%C3%A3o-foi-consumido-na-OP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24476232281111) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**

No relatório **"Consumo Real X Standard" (MATR450)** calculando pela Estrutura, apresenta componente que não foi consumido na Ordem de Produção. Identificamos isso, após efetuarmos Revisão da Estrutura e retirar o componente. É possível ajustar esse comportamento na emissão do Relatório para não exibir o componente que não faz mais parte da Estrutura?

![image01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24476670012311)

![image02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24476670023191)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Esse **cenário ocorre devido** não ter definido as Revisões da Estrutura nos componentes do Produto Acabado e o parâmetro **MV\_REVAUT estar configurado igual F (Desligado)**.  
  
**Para correção do cenário:** Efetuando os mesmos passos, porém, com o parametro **MV\_REVAUT igual a T (Ligado)**, o sistema cria automaticamente as revisões nos Componentes e o Relatorio vai isolar as revisões da OP corretamente mesmo usando a opção dos parametros **"Calcular pela ?" = Estrutura**.  
  
Revisar a definição da Revisão da Estrutura , **definindo manualmente no componente** a revisão inicial e revisão final, ou mesmo ativar o **parâmetro MV\_REVAUT** para gerar estas revisões.  
  
***Observações importantes:*** Segundo a equipe de MANUFATURA (PCP), o parâmetro deve ser ativado ***antes da criação*** das Estruturas, e **não deve** ser ativado para alterar uma Estrutura existente.

![mv_revaut.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/24477082220695)

Saiba Mais:

[Clique aqui e veja mais artigos sobre RELATÓRIOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
