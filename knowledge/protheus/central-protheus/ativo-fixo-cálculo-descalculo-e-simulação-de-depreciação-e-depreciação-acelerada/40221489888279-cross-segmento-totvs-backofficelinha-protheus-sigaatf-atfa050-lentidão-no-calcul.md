---
article_id: 40221489888279
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 37382989e03bd102cbd55c14673e8e6c1bb1b4b9181da0cc027c6ac78ba9758a
fetched_at: '2026-06-28T22:41:43.339443+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - TOTVS Backoffice(Linha Protheus) - SIGAATF - ATFA050 - Lentidão
  no calculo de depreciação com contabilização
type: support-article
updated_at: '2026-05-04T19:56:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40221489888279-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Lentid%C3%A3o-no-calculo-de-deprecia%C3%A7%C3%A3o-com-contabiliza%C3%A7%C3%A3o
---

Durante a execução da rotina ATFA050 de cálculo mensal de depreciação no TOTVS Protheus, pode ocorrer lentidão devido à necessidade de atualização do ambiente, procedures, problemas no Cadastro de Relacionamentos (CTBA090) ou inconsistências no Controle de Numeração da tabela CTK. Recomenda-se atualizar o sistema, ajustar procedimentos e corrigir o cadastro para melhorar a performance.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40221489864855) Tempo aproximado para leitura: **10 min**  
  
**Dúvida**  
Durante a execução da rotina de Cálculo Mensal de depreciação (ATFA050), ocorre degradação significativa de performance. O sistema apresenta elevada lentidão e permanece travado na tela de processamento.  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo (SIGAATF) - a partir da versão 12  
  
  
**Solução**  
O cenário de travamento e lentidão na rotina ATFA050 com contabilização está geralmente associado à necessidade de atualização do ambiente e das procedures, a problemas no Cadastro de Relacionamentos (CTBA090) que impactam o tempo de processamento, ou a inconsistências no Controle de Numeração da tabela CTK.   
  
Quando a tabela CTK não é alimentada com a numeração correta de 10 caracteres, o sistema precisa percorrê-la inteira até encontrar a sequência adequada, causando a degradação de performance.  
  
  
**Passos**

1. **Atualização do Ambiente:**  
   Certifique-se de que o sistema está com a última atualização aplicada para garantir a execução correta das rotinas, como pacote backoffice, lib, DBAccess, AppServer e *SmartClient*  
   * [Link pacote Backoffice](https://tdn.totvs.com/pages/releaseview.action?pageId=382557083#issues-17)
   * [Link de downloads binários.](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads)
2. **Atualização das** ***Procedures*****:**   
   Verifique se o sistema está com as *procedures* atualizadas e devidamente instaladas no banco de dados. Especificamente, garanta a atualização das seguintes:

* Procedure 01 - REPROCESSAMENTO CONTÁBIL
* Procedure 06 - ATUALIZAÇÃO DE SALDOS ONLINE
* Procedure 07 - REPROCESSAMENTO POR CONTAS
* Procedure 11 - CÁLCULO DE DEPRECIAÇÃO DE ATIVOS
* Procedure 23 - Atualização de Saldo em Fila
* Procedure 31 - Lançamentos Contábeis  
    
  [SIGAATF - Utilização de procedure no cálculo de depreciação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021716291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Utiliza%C3%A7%C3%A3o-de-procedure-no-c%C3%A1lculo-de-deprecia%C3%A7%C3%A3o?source=search)

3. **Análise do Cadastro de Relacionamentos (CTBA090):**  
     
   Acesse o cadastro do Lançamento Padrão 820 (CTBA080) e verifique se ele está configurado utilizando a tabela SN3.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40221480572311)

   O cadastro de relacionamento (CTBA090) deste Lançamento Padrão é originalmente voltado para a tabela SN4.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40221489869591)

   Caso esteja configurado com a tabela SN3 e seja necessário manter o cadastro de relacionamento, ajuste o vínculo para a tabela SN4, utilizando a chave correspondente, para otimizar o desempenho.
4. **Ajuste do Controle de Numeração (Tabela CTK):**  
     
   Para este caso, é possível realizar um dos passos abaixos:

   1. Realize uma manutenção preventiva com a limpeza da tabela CTK, garantindo que o sistema volte a incluir os registros corretamente.  
        
      [CTBA105 Exclusão dos registros das tabelas CTK e CV3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018012532-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Exclus%C3%A3o-dos-registros-das-tabelas-CTK-e-CV3)
   2. Realizar o ajuste do controle de numeração:

      * Acesse o módulo Configurador (SIGACFG) no caminho: Ambientes -> Cadastros -> Controle de numeração.
      * Localize a rotina com o alias "\_CT" e verifique se o tamanho do registro está definido adequadamente com 10 caracteres.

        ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40221480576023)
      * Verifique se o campo que indica o próximo número a ser usado está coerente com o último registro preenchido no campo CTK\_SEQUEN no banco de dados.

        ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40221480579479)
      * No exemplo, o último registro na tabela CTK está com o CTK\_SEQUEN 0000000959, em que o próximo número disponível é o 0000000960, informado na rotina.

**Saiba mais:**  
[ATFA050 - Porque o sistema não calcularia a depreciação de um bem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018327952-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Porque-o-sistema-n%C3%A3o-calcularia-a-deprecia%C3%A7%C3%A3o-de-um-bem)  
[Erro na chamada de processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420151614743?source=search)
