---
article_id: 23120928825751
category: SIGAEST - INTEGRAÇÕES
content_hash: 24a6ffd32e3d7b2afae31aa40ee9b81300a1304815834620738234700bcd57eb
fetched_at: '2026-06-28T22:38:46.238583+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - INTEGRAÇÃO PIMS x
  Protheus invokeSOAPService: ERP Service Communication returned an error: INTERNAL
  SERVER ERROR'
type: support-article
updated_at: '2025-09-19T17:59:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23120928825751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-INTEGRA%C3%87%C3%83O-PIMS-x-Protheus-invokeSOAPService-ERP-Service-Communication-returned-an-error-INTERNAL-SERVER-ERROR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23120867811095) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao realizar algum tipo de movimentação no PIMS e salvar é apresentada a mensagem **"Internal Server Error".**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23120867811351)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O retorno **"Internal Server Error"** se trata de uma mensagem genérica, indicando apenas algum problema na conclusão do processo, segue abaixo algumas validações já mapeadas:

**1° - Quando não é gerado XML na XX3 do Protheus.**

Quando o registro enviado do PIMS para o Protheus, não chega e não é salvo na fila de recepção (Tabela XX3). Pode ser gerado o erro em questão no PIMS, para conferir basta verificar após a tentativa de integração se o sistema adicionou uma nova linha na Tabela XX3 referente ao adapter enviado, caso essa linha não tenha sido criada, segue abaixo validações e tratativas

**Procedimento:**

* Caso não tenha chegado, verifique se, no PIMS e no Protheus, a URL utilizada para a comunicação dos sistemas estão correta e liberada.  
    
  **Caminho no PIMS:** Administração > Propriedades > PIMSConector > Consultar > mensagemunica.protheus.ws.url no PIMS. (Caso necessite de auxílio nessa verificação, sugerimos que realize contato com o time de Suporte do PIMS Agrícola).  
    
  **Caminho no Protheus:** Parâmetro MV\_EAIURL2   
  (Se o ambiente estiver em Cloud, é necessário solicitar verificação dos links para equipe cloud).  
    
  **IMPORTANTE:** Para cenários onde um ambiente está em CLOUD e outro não é necessário se utilizar da configuração dos links Externos e Validar com a equipe Cloud a necessidade da criação de uma Regra de Security para os IP's internos/externos
* Se estiver fazendo um envio do Protheus para o PIMS verifique também:  
  [**SIGAEST - Ao realizar integração não ocorre erro, porém não gera mensagem na XX3**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26810171288215)

**2° - Quando é gerado XML na XX3 do Protheus.**

* Caso esteja enviando um registro do PIMS para o Protheus, acesse o SIGACFG na opção Schedule, clique em Schedule EAI e verifique que a mensagem enviada pelo PIMS chegou ao Protheus.
* Caso esteja enviando do Protheus para o PIMS, e verifique no monitor de integrações no PIMS que a mensagem foi recebida. (Caso necessite de auxilio nessa verificação, sugerimos que realize contato com o time de Suporte do PIMS Agrícola para auxílio).

**Procedimento:**

No sistema destino, validar a mensagem de erro apresentada no arquivo de recebimento, e tratar de acordo com a mensagem informada.

**3° - A falta ou configuração incorreta da CheckSpecialKey no ini do Serviço de WS**

A partir da release 12.1.2410 a chave CheckSpecialKey configurada com 1 passou a ser obrigatória para ambientes Protheus conforme documentação abaixo, em casos onde a mesma não está configurada incorretamente, pode ocorrer esse erro em integrações como por exemplo a STOCKTURNOVER.

**Tratativa:**

* Verifique se seu ambiente e serviço está devidamente configurado conforme documentação abaixo;  
  [**SIGAFAT - A chave CheckSpecialKey em seu ambiente está desligada, você deve liga-la para seu uso da seção [GENERAL]**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34672102058519-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-A-chave-CheckSpecialKey-em-seu-ambiente-est%C3%A1-desligada-voc%C3%AA-deve-liga-la-para-seu-uso-da-se%C3%A7%C3%A3o-GENERAL)

**4° - Usuário adminstrador do Protheus não cadastrado no PIMS**

A partir da release 12.1.2410 o Protheus passou a exigir chave **security**igual a 1, ou seja, é feita uma validação de autenticação de usuário da aplicação ao qual o Protheus está realizando integração, o que, se não ocorrer, pode gerar o erro em questão.

**Procedimento:**

* Verifique se seu ambiente PIMS está devidamente configurado conforme documentação abaixo;  
  [**Agro - PIMS MC - ADM - Falha na Finalização do Apontamento Agrícola**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33214556723863-Agro-PIMS-MC-ADM-Falha-na-Finaliza%C3%A7%C3%A3o-do-Apontamento-Agr%C3%ADcola)

**5º cenário: Quando é gerado XML, porém não é possível identificar a real mensagem de erro.**

Ao validar o arquivo de XML recebido pelo PIMS, ainda consta o erro genérico "Internal Server Error".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23717937158807)

**Pontos para a análise:**

* Se você efetuar um teste no Protheus com as informações que estão sendo enviada pelo o PIMS ocorre algum erro? Se sim, qual?
* Verifique se o serviço webservice está ativo e se está utilizando o Protocolo de segurança HTTPS na url
* Efetue um teste reiniciando o serviço Webservice
* Efetue a coleta do console.log do webservice para análise e validar se a mensagem com o erro real, é identificada para realizar a tratativa de acordo com o erro apresentado.
* Efetue também a coleta do inspetor de Objetos para análise dos fontes envolvidos.

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Integrações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
