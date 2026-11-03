---
article_id: 38100469626007
category: Financeiro - Configurador
content_hash: 00b404aeaaa37dd0c5a9a5cbc78a15e826d12ba9a0cfd416190a0c6c38b00542
fetched_at: '2026-06-28T22:37:57.596405+00:00'
product: protheus
section_id: 1500001539601
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Não consigo atualizar
  a procedure 33, 39 ou 40
type: support-article
updated_at: '2026-06-17T20:46:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38100469626007-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-N%C3%A3o-consigo-atualizar-a-procedure-33-39-ou-40
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38100521174679) Tempo aproximado para leitura: **00:04 min**  
  
**Dúvida**  
Por que a procedure 33 permanece com status de desatualizada mesmo após a atualização completa de todas as procedures do sistema?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.33.  
  
**Solução:**

As **Procedures 33, 39, 40** possui uma particularidade técnica importante: trata-se de um recurso de uso exclusivo para clientes que utilizam a integração com o produto **Gesplan**.  
  
**33 - Integração Gesplan - Contas a Receber;**  
**39 - Integração Gesplan - Contas a Pagar;**  
**40 - Integração Gesplan - Movimento Bancário.**

O sistema não permite a atualização automática ou manual dessa procedure caso o ambiente não esteja previamente configurado para a integração com o Gesplan. Dessa forma, sua atualização somente é possível e necessária após a configuração completa do ambiente para esse produto.  
Documentação de apoio: [Integração Protheus x Gesplan (Gestão de Caixa e Tesouraria)](https://tdn.totvs.com/pages/releaseview.action?pageId=951327976)

É importante destacar que, para **clientes que não utilizam o Gesplan**, as **Procedures 33, 39, e 40 permanecer não instalada não gera qualquer impacto negativo**, erro de processamento ou interferência nas demais rotinas e processos do **módulo Financeiro**.

Para atualização da procedure:

Caso o cliente utilize ou deseje aderir ao Gesplan:

1. Realize a configuração completa do ambiente Protheus e parâmetros relativos ao **Gesplan (Wizards recomendados)**
2. Após a configuração, acessar o **Configurador** e executar a rotina de **atualização de procedures**;
3. Realize a atualização da **Procedure 33**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38100521175191)

Caso o cliente **não utilize** o Gesplan:

1. Nenhuma ação é necessária. O status da procedure pode ser ignorado, pois não há prejuízo às funcionalidades do Protheus.
