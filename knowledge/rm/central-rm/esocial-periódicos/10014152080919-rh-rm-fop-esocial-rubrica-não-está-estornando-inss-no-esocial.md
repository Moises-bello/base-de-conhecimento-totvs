---
article_id: 10014152080919
category: esocial - Periódicos
content_hash: 26740bc23e6cb846b73be82ca225c0d399e01de73464c6291a903c13a6255ed4
fetched_at: '2026-06-28T22:47:09.478157+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Rubrica não está estornando INSS no eSocial
type: support-article
updated_at: '2024-06-14T17:14:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10014152080919-RH-RM-FOP-eSocial-Rubrica-n%C3%A3o-est%C3%A1-estornando-INSS-no-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Determinada rubrica está estornando INSS no RM porém não estona o INSS no eSocial Web.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Esse incidente pode ocorrer por motivos diversos como, por exemplo, falta de distribuição do SEFIP para este evento e tipo de rubrica incorreta no eSocial Web.   
  
**Solução**  
Para correção da ocorrência favor realizar as validações abaixo:

• Falta de **distribuição do SEFIP**

Para empresas que utilizam tomadores de serviço, o sistema irá buscar as verbas para montagem do XML na distribuição do SEFIP realizada. Caso exista eventos faltantes na distribuição, poderá impactar no valor final, apresentando divergências. Importante também que a distribuição esteja conforme o histórico de rateio de tomadores do funcionário.  Desta forma, acesse o menu **Encargos | SEFIP | Distribuir SEFIP** e verifique a distribuição realizada para o mês/ano correspondente ao período de apuração. Verifique a necessidade de [retificação do evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028334171-RM-eSocial-Retifica%C3%A7%C3%A3o-do-evento-S-1200?source=search) para atualizar os valores no eSocial Web. 

• Tipo de **rubrica e vigência divergentes** no eSocial Web

Verifique se as incidências estão corretas no eSocial, pois o Governo utiliza a parametrização dos eventos S-1010 para identificar a forma de cálculo. Veja os passo abaixo:  
1. Para corrigir o tipo de rubrica e incidências divergentes, no módulo **Folha de Pagamento** acesse o menu **Administração de Pessoal | Eventos** e altere a parametrização do evento conforme a sua necessidade.   
2. Em seguida, acesse **eSocial | Fila de Eventos** e localize o evento S-1010 criado;

**![mceclip0.png](https://totvssuporte.zendesk.com/hc/article_attachments/9811431909911)**

3. Verifique se há necessidade de alterar a **competência** correspondente ao início da vigência da rubrica no eSocial;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10015841124759)

4. Após ajustes, gere o XML e envie ao eSocial;  
5. Realizando o reenvio do S-1010, é necessário também realizar a [retificação do evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028334171-RM-eSocial-Retifica%C3%A7%C3%A3o-do-evento-S-1200?source=search) para atualizar os valores no eSocial Web.

**Importante**  
Para facilitar a validação do XML, execute o processo **Validar S-1200 com Envelope** presente em **eSocial | Eventos Periódicos**.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043018974/mceclip4.png)
