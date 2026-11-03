---
article_id: 22967620309399
category: Materiais - Compras (SIGACOM)
content_hash: 2337a60e66ffc5676a626239209c137d6cead0c586cc6353fbe11601b1209c07
fetched_at: '2026-06-28T22:41:21.989143+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O que fazer quando
  o documento está com o CKO_FLAG = "0"?
type: support-article
updated_at: '2024-05-09T14:57:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22967620309399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-fazer-quando-o-documento-est%C3%A1-com-o-CKO-FLAG-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22967620300823) Tempo aproximado para leitura: **00h05min****Dúvida**O que fazer quando o documento está com o CKO\_FLAG = "0"?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Solução**

**Passo 1:** Se estiver utilizando o Importador Xml padrão ou integrado com o Totvs Transmite, valide se o parâmetro **MV\_IMPXML** se encontra como .T.. Caso estiver como .F. , será gravado o código EDI(**CKO\_CODEDI**) incorreto e o documento não será processado.

**Passo 2:** Colocar a rotina SCHEDCOMCOL no menu para execução manualmente conforme demonstra na documentação:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - (Importador XML ou Totvs Colaboração) | Como executar as funções de carga SEM utilizar o Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-Schedule)

**Passo 3:** Validação dos campos CKO\_EMPPRO e CKO\_FILPRO na tabela CKOCOL

* Acesse a tabela CKOCOL no banco de dados e valide os valores dos campos CKO\_EMPPRO e CKO\_FILPRO para cada registro.

**Passo 4:** Execução da rotina SCHEDCOMCOL em cada empresa/filial listada.

* Para cada combinação de valores únicos de CKO\_EMPPRO e CKO\_FILPRO encontrados na tabela CKOCOL, execute a rotina SCHEDCOMCOL na respectiva empresa/filial.
* Garanta que a rotina seja executada na empresa/filial correta para que as notas sejam lidas corretamente.

**Passo 5:** Verificação do campo CKO\_FLAG após a execução da rotina.

* Após a execução da rotina **SCHEDCOMCOL**em cada empresa/filial, verifique o valor do campo **CKO\_FLAG**para cada registro na tabela **CKOCOL**.
* Se o valor for igual a 1, significa que as notas estão prontas para serem geradas no monitor.
* Se o valor for igual a 2, significa que as notas devem ser processadas novamente na rotina de reprocessamento.

**Passo 6:** Validação das documentações relacionadas.

* Caso as notas não sejam encontradas tanto no monitor quanto no reprocessamento, vamos validar as documentações abaixo relevantes para identificar possíveis problemas ou inconsistências.

Após realizar a importação os documentos não estão aparecendo na rotina do monitor.

[**Os documentos não estão aparecendo na rotina do monitor (COMXCOL).**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20435145226135)  
 

Os documentos não estão aparecendo na rotina do REPROCESSAR.

[**Os documentos não estão aparecendo na rotina do REPROCESSAR dentro monitor.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20435997213591)

**IMPORTANTE: Pedimos que caso seja gerado algum error.log no momento da execução da rotina que seja aberto um ticket para o suporte e encaminhe o inspetor de objetos junto o error.log que foi gerado.**

***Saiba Mais:***

* [Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-MP-SIGACOM-Importador-XML#:~:text=No%20Importador%20de%20XML%20%C3%A9%20necess%C3%A1rio%20criar%20agendamentos,op%C3%A7%C3%B5es%20do%20menu%20Ambiente%20-%3E%20Schedule%20-%3E%20Schedule%3A)
* [Agendamento (Schedule) - Importador XML](https://tdn.totvs.com/display/public/PROT/Agendamento+%28Schedule%29+-+Importador+XML)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a configuração do agendamento da rotina SCHEDCOMCOL dentro do novo SCHEDULE POUI?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22062559984791-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-configura%C3%A7%C3%A3o-do-agendamento-da-rotina-SCHEDCOMCOL-dentro-do-novo-SCHEDULE-POUI)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Códigos de preenchimento do campo CKO\_FLAG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011715772-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-C%C3%B3digos-de-preenchimento-do-campo-CKO-FLAG)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
