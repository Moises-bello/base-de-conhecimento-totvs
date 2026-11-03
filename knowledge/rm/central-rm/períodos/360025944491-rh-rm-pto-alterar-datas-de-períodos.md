---
article_id: 360025944491
category: Períodos
content_hash: 6e85ff91a48476b69bda0b750b552598de219e3be46714e32dd5897966542dcd
fetched_at: '2026-06-28T22:46:37.275864+00:00'
product: rm
section_id: 6045149105687
source: central-rm
title: RH - RM - PTO - Alterar datas de períodos
type: support-article
updated_at: '2025-02-19T13:30:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025944491-RH-RM-PTO-Alterar-datas-de-per%C3%ADodos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503012817943) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**  
Como alterar as datas de períodos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto  – A partir da versão 11.80  
  
**Solução**Para alterar as datas de períodos do Automação de Ponto, existem duas opções:

* Alteração do fim do período atual para liberação de um novo período com as datas desejadas
* Criação de um período intermediário para que as próximas liberações sejam com as datas desejadas, sem a necessidade de realizar alterações no período atual e ativo.

Para alteração do período atual e ativo, algumas informações de movimentação são perdidas, portanto é necessário realizar um recálculo no período alterado antes de prosseguir. Segue abaixo as instruções a serem seguidas.

1. No exemplo abaixo, é desejado alterar a sequência de períodos, de forma que os próximos períodos sejam considerados no intervalo de datas de 16 a 15.  
   ![2019-03-28_09_43_09-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024906411)
2. Para isso, edite o período atual e ativo e altere a data fim para 15/MM.  
   ![2019-03-28_09_44_18-.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024906431)
3. Será apresentada a mensagem informando que com esta alteração, algumas informações dos funcionários serão perdidas, portanto é necessário efetuar o recálculo de todos os funcionários.  
   ![2019-03-28_09_44_07-RM.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024899852)
4. Após a alteração, realize o recálculo global para os funcionários. No exemplo abaixo o recálculo foi realizado considerando todos os parâmetros e funcionários.  
   ![2019-03-28_10_00_26-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024906531)
5. Após o recálculo, a liberação do período pode ser realizada, portanto é necessário acessar a tela de períodos e executar a rotina **Liberar Período** através do menu **Processos**.  
   ![2019-03-28_09_44_41-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024906451)
6. As datas então poderão ser alteradas para o desejado: 16/MM a 15/MM. Nas próximas liberações, o sistema já irá compreender a alteração e sugerir o período mensal de 16 a 15.  
   ![2019-03-28_09_45_10-Liberar_Per_odo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024906471)
7. Neste exemplo, os períodos serão considerados conforme abaixo. Nas próximas liberações, o sistema já irá sugerir a data mensal de 16 a 15.  
   ![2019-03-28_09_45_33-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024899892)

Para criação do período intermediário, a data fim da próxima liberação de períodos que deverá ser alterada, conforme instruções abaixo.

1. Neste exemplo, é desejado que os períodos sigam a sequência de 15 a 16. Portanto, é criado um período intermediário na liberação de períodos, alterando a data fim do período.  
   ![2019-03-28_09_47_28-Liberar_Per_odo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024899912)
2. Desta forma, o período será encerrado até o dia 14, e então uma nova liberação será realizada, de forma que a sequência considere as datas de 15 a 16.  
   ![2019-03-28_09_48_21-Liberar_Per_odo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024906491)
3. Neste exemplo, os períodos serão considerados conforme abaixo. Nas próximas liberações, o sistema já irá sugerir a data mensal de 15 a 16.  
   ![2019-03-28_09_48_38-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360024906511)

**Saiba mais**  
Para maiores informações sobre os períodos, acesse a documentação: [Períodos](https://tdn.totvs.com/pages/releaseview.action?pageId=452719539).
