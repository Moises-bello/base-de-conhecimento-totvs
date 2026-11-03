---
article_id: 4403079861655
category: RH - Contabilização
content_hash: a3221bbd4e2f977e3ae7549dd6dcdc99cd025887301b84c30addcfdff2031963
fetched_at: '2026-06-28T22:43:46.099250+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema valida a data base na geração da
  Contabilização
type: support-article
updated_at: '2025-07-30T02:24:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403079861655-RH-Linha-Protheus-GPE-Como-o-sistema-valida-a-data-base-na-gera%C3%A7%C3%A3o-da-Contabiliza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33811014688279) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como o sistema valida a data base na geração da Contabilização?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Para a **Contabilização da Folha de Pagamento** a data base da contabilização é definida de acordo com a data cadastrada no cadastro de períodos. Essa data será considerada como a data fim do período de cadastro da competência selecionada.   
  
Existe uma variável **dDataBase** que recebe o conteúdo de data, de acordo com as informações do campo **Fim Tarefa - RCH\_DTFIM** do cadastro de **Períodos**, este deve estar com a mesma informação do campo **Data Final - RFQ\_DTFIM**  
  
 No Gestão de Pessoa - SIGAGPE acesse **Atualizações** -> **Definições de Cálculo** -> **Períodos**  
![](https://totvssuporte.zendesk.com/attachments/token/ghtAMdQjutzgpOYUaqjJpByvH/?name=inline314196279.png)  
  
Consulta Genérica da Tabela **RCH - Período de Cálculo** com gravação do campo Fim Tarefa - RCH\_DTFIM  
Acesse **Consultas** -> **Cadastros** -> **Genéricos** -> RCH  
![](https://totvssuporte.zendesk.com/attachments/token/yvSefDgA6IqUYrWADzvp5JGvy/?name=inline-2146532370.png)  
  
Na geração da Contabilização a data assumida será o conteúdo assumido pela variável dDatabase o último dia do mês.  
![](https://totvssuporte.zendesk.com/attachments/token/1eXE6MBCFw16lILSfvSRGGs2Z/?name=inline903217921.png)

A **Contabilização da Provisão** não segue os mesmos moldes da contabilização da Folha de Pagamento, pois na Folha segue-se como base o último dia do Período informado, devido já serem períodos fechados da Folha.  
Já para as Provisões, a sugestão é que o usuário altere a **Data Base** do sistema para o **último dia** do período desejado, porém a critério do usuário, o sistema permite que informe qualquer outra data que o sistema irá respeitar. Isso porque o usuário pode realizar a Provisão de um período de forma fracionada.  
  
O usuário pode realizar a contabilização da provisão mais de uma vez no mês, informando datas diferente (Data Base), embora seja aconselhável informar o ultimo dia do período(mês).  
  
Para que a contabilização da Provisão seja mais próxima do real, altere sempre a Data Base do sistema para o último dia do período a ser contabilizado, além disso o sistema irá gravar e utilizar a data informada no momento do cálculo.  
  
**Saiba Mais**  
Para adquiri mais conhecimento acesso o(s) link(s) abaixo:  
[9285674 DRHGCH-20130 DT Contabilização de Provisão validando Data Base](https://tdn.totvs.com/pages/viewpage.action?pageId=556877927)
