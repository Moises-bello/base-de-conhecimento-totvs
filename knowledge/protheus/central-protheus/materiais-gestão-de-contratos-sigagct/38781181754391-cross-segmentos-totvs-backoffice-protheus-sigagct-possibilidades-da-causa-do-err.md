---
article_id: 38781181754391
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: b33f6b2afb9942ae0f4279742ea28bff6379c588e248f42273cfebcbe90d89df
fetched_at: '2026-06-28T22:37:24.039664+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Possibilidades da causa
  do erro  Cannot insert duplicate key row in object 'dbo.CNAXXX na Inclusão do Contrato
type: support-article
updated_at: '2026-03-04T11:01:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38781181754391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Possibilidades-da-causa-do-erro-Cannot-insert-duplicate-key-row-in-object-dbo-CNAXXX-na-Inclus%C3%A3o-do-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38781157064599) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**

Error log Cannot insert duplicate key row in object 'dbo.CNAXXX na Inclusão do Contrato

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Gestão de contratos - A partir da release 12.1.2410.

**Solução**

Segue abaixo algumas  possibilidades da causa para esse erro.

**1.** Normalmente, esse erro ocorre devido a uma inconsistência na base de dados. Ele indica que, ao executar essa ação no sistema, está sendo feita uma tentativa de inserir um registro na tabela **CNA** com chave duplicada.

Ou seja, o conteúdo que está sendo incluído possui uma chave primária (chave única) que já existe gravada na tabela.

Com isso, ocorre a quebra de integridade, pois os índices configurados não permitem a inserção de registros duplicados.  
   
   
Por gentileza abrir um ticket para equipe de suporte solicitando as tabelas apenas afim de visualização e comparação SIX, SX2 e SX3 padrão da tabela CNA para pra que possa ser analisado no ambiente em questão (Importante ressaltar que é apenas para análise e comparação em teu ambiente.

A recomendação do suporte é que não manipule sua base, para que seu dicionário esteja de acordo com o Portal do cliente, pois existem particularidades de cada ambiente.   
   
Recomenda-se verificar no error.log o conteúdo que o sistema está tentando gravar, se possui registro um idêntico na Tabela CNA.

Segue exemplo abaixo:  
   
INSERT INTO CNA010(CNA\_FILIAL,CNA\_CONTRA,CNA\_NUMERO,CNA\_FORNEC,CNA\_LJFORN,CNA\_DTINI,CNA\_VLTOT,CNA\_SALDO,CNA\_DTFIM,CNA\_TIPPLA,CNA\_PRORAT,CNA\_CRONOG,CNA\_FLREAJ,CNA\_RPGANT,CNA\_RATEIO,R\_E\_C\_N\_O\_) VALUES ( :1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16)  
-- Binded Parameters List --  
[#1](https://totvssuporte.zendesk.com/agent/tickets/1) [C] [010101]  
[#2](https://totvssuporte.zendesk.com/agent/tickets/2) [C] [000000000000003]  
[#3](https://totvssuporte.zendesk.com/agent/tickets/3) [C] [000001]  
[#4](https://totvssuporte.zendesk.com/agent/tickets/4) [C] [XXXXXX]  
[#5](https://totvssuporte.zendesk.com/agent/tickets/5) [C] [0001]  
[#6](https://totvssuporte.zendesk.com/agent/tickets/6) [D] [20221201]  
[#7](https://totvssuporte.zendesk.com/agent/tickets/7) [N] [3300.000000]  
[#8](https://totvssuporte.zendesk.com/agent/tickets/8) [N] [3300.000000]  
[#9](https://totvssuporte.zendesk.com/agent/tickets/9) [D] [20491231]  
[#10](https://totvssuporte.zendesk.com/agent/tickets/10) [C] [001]  
[#11](https://totvssuporte.zendesk.com/agent/tickets/11) [C] [2]  
[#12](https://totvssuporte.zendesk.com/agent/tickets/12) [C] [000001]  
[#13](https://totvssuporte.zendesk.com/agent/tickets/13) [C] [2]  
[#14](https://totvssuporte.zendesk.com/agent/tickets/14) [C] [2]  
[#15](https://totvssuporte.zendesk.com/agent/tickets/15) [C] [2]  
[#16](https://totvssuporte.zendesk.com/agent/tickets/16) [R] [71]  
   
   
Há de fato na tabela do ambiente um registro com esses dados (Verificar o trecho acima de exemplo no erro ocorrido)?  
   
Segue procedimento para realizar essa verificação devidamente:  
-> [Verifica a integridade de registros duplicados](http://tdn.totvs.com/pages/releaseview.action;jsessionid=4EE73EDA4E24C4BA7AAF4FF0FA95743A?pageId=242386686)  
-> [Configuração da verificação da integridade de Registros Duplicados](http://tdn.totvs.com/pages/releaseview.action?pageId=275454634)  
   
Se de fato há o registro, precisamos primeiramente identificar o porque de já haver esse registro idêntico no banco., com mesmos números.  
   
O dado que já possui gravado na base com mesmo índice é antigo ou recente?  
Caso seja antigo, sabe informar se foi appendado na base em algum momento de implantação, desconsiderando assim o incremento de numeração automático?  
   
OBS: Caso identifique que a gravação duplicada é, na verdade, por falha em seu controle automático de numeração, consulte aqui as instruções para [ajuste do controle automático de numeração](https://tdn.totvs.com/pages/releaseview.action?pageId=235570751).  
   
**2.** Pesquise no arquivo de erro se possui algum ponto de entrada sendo executado.Para localizar pesquise por XX7 ou CFUNCTION no arquivo do erro.![](https://centraldeatendimento.totvs.com/hc/article_attachments/38781157065495)  
Caso possua customização sendo chamada no erro.

Peço por gentileza, que realize os testes desativando as customizações do ambiente através dos [3 métodos indicados nesta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292), impreterivelmente.

1 - Através da chave IXBLOG no arquivo APPSERVER.ini

2 - Através do Configurador CFG - Catálogo de Personalizações

3 - Desabilitar customizações chamadas no dicionário de dados

**3.** Teste com as últimas atualizações do portal

Caso o problema persista após as verificações acima, solicitamos, por gentileza, a abertura de um ticket em um de nossos canais de atendimento para a equipe de suporte.

É importante encaminhar o arquivo de erro completo e com ambiente atualizado, sem customizações, juntamente com o vídeo demonstrando o processo realizado até o momento da ocorrência.

***Saiba Mais:***

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
