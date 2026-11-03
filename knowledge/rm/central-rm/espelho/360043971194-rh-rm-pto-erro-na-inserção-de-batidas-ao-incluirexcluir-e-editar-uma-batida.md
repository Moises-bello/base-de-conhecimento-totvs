---
article_id: 360043971194
category: Espelho
content_hash: 3a71f976807a78740e0366b4b0999964d55a4758fdea1b25a7ff70e278d4001e
fetched_at: '2026-06-28T22:46:31.293409+00:00'
product: rm
section_id: 6045459696023
source: central-rm
title: RH - RM - PTO - "Erro na inserção de batidas" ao incluir/excluir e editar uma
  batida
type: support-article
updated_at: '2026-03-13T21:40:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043971194-RH-RM-PTO-Erro-na-inser%C3%A7%C3%A3o-de-batidas-ao-incluir-excluir-e-editar-uma-batida
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19409207345687) Tempo aproximado para leitura: 00:01:20 min**

**Dúvida**

Ao incluir uma batida no espelho do funcionário, o sistema emite uma mensagem de erro :"Erro na inserção de batidas:" (sem detalhes no texto da mensagem). O que fazer?  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**  
Este erro ocorre normalmente quando o ID da tabela **GAUTOINC** está dessincronizado com o ID da tabela **AAFDT**.

Para verificar se há esta dessincronização, com o apoio de um DBA, deverá executar a query abaixo para conferência:

SELECT AAFDT.CODCOLIGADA, MAX(ID) ID\_AAFDT, VALAUTOINC ID\_GAUTOINC FROM AAFDT, GAUTOINC  
WHERE AAFDT.CODCOLIGADA = GAUTOINC.CODCOLIGADA  
AND GAUTOINC.CODAUTOINC = 'IDBATIDAAAFDT'  
GROUP BY AAFDT.CODCOLIGADA, VALAUTOINC

* Se houver divergência entre os ID's retornados na consulta, no caso quando o **ID da AAFDT está maior** que o ID da GAUTOINC irá ocorrer o erro.
* Quando o ID da GAUTOINC estiver maior ou igual ao ID da AAFDT **não há problema**.

Abaixo uma imagem com os ID's sincronizados:  
![ID_IGUAL.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37890007087383)

Agora, uma imagem com os ID's dessincronizados, onde o ID da AAFDT é maior que o ID da GAUTOINC, que resulta no erro:  
![ID_ERRADO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37890010516119)

Para correção deste cenário, deverá seguir com os procedimentos abaixo:

* Acessar o menu Ambiente | Parâmetros | Parâmetros Globais | aba Configurações Públicas e desmarcar a opção "**Compartilhar a conexão dos Subscribers para acesso à tabela de controle de identificadores":**  
  **![subscriber.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37890007090839)**
* Após realizar as alterações acima e salvar, com apoio de um DBA, deverá executar a query abaixo para igualar os ID's:  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39026043620119)

No exemplo acima, o problema foi identificado na coligada 2 e 3. Portanto, deverá executar a query de UPDATE duas vezes. Uma para a coligada 2 e outra para a coligada 3. Desta forma, os ID's serão igualados posteriormente.  
Após os ajustes poderá acessar o espelho de ponto e incluir, editar ou excluir a batida normalmente.

**Saiba mais**  
Maiores detalhes sobre o parâmetro, acesse o link: [**Compartilhar a conexão dos Subscribers para acesso à tabela de controle de identificadores**](https://tdn.totvs.com/pages/viewpage.action?pageId=772040101)

**Importante**

Caso você seja cliente Cloud Totvs, deverá abrir um ticket com o time de Cloud para solicitar a execução do UPDATE.  
  
Se ao executar a consulta para avaliar se há a dessincronização dos ID's, os mesmos estiverem sincronizados, a causa raiz poderá ser outra. Nesta situação deverá acionar o time de suporte para análise.
