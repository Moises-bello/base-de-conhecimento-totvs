---
article_id: 16779731236119
category: Suricato
content_hash: e5259fc65684cc3a4beaf44d30a6c1891fca949a674fa32aff5dbe9efc8ae1fc
fetched_at: '2026-06-28T22:44:57.290162+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - PON x Suricato - Integração Protheus x Suricato
type: support-article
updated_at: '2026-06-15T14:07:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16779731236119-RH-Linha-Protheus-PON-x-Suricato-Integra%C3%A7%C3%A3o-Protheus-x-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16779723961751) Tempo aproximado para leitura: **00:20:00 min**  
  
**Dúvida**  
Como funciona a integração do **Protheus** com o **Suricato?**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A integração do **Protheus x Suricato** acontece através de **parâmetros** e **Webservices,** que anteriormente eram utilizados pelo TSA.  
É importante que o **Suricato** já esteja **instalado e configurado** para seguir os passos citados nesta documentação.  
  
**PARÂMETROS**

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Descrição** | **Exemplo de utilização** |
| **MV\_TSREP** | Define se haverá integração entre o modulo SIGAPON e o aplicativo Suricato. | .T. |
| **MV\_TSASERV** | Endereço IP ou nome do servidor da instalação do aplicativo Suricato. | 10.0.0.90:8080/tsa-ejb |
| **MV\_TSANDIA** | Define o Número de dias anteriores a data do sistema para que seja feito o sincronismo dos funcionários demitidos. | 30 |
| **MV\_TSATLOG** | Define qual será o tipo de envio do Log de erros da integração do módulo Ponto Eletronico X Aplic. Suricato (0=Não Gera, 1=E-mail, 2=Arquivo, 3=Ambos, 5=SaveXML). | 3 |
| **MV\_TSADARQ** | Define o nome do diretório onde serão gravados os arquivos de Log de erros gerados da integração do módulo Ponto Eletrônico X Aplicativo TSA. | \logwsrhtsa\ |
| **MV\_TSAIURB** | Habilita a integração do crachá do funcionário com o Suricato. | .T. |
| **MV\_TSAMAIL** | Endereço de E-mail para recebimento de mensagens do Log de integração. Caso esteja em branco o e-mail não é enviado. | [equipesuricato@servidor.com.br](mailto:equipetsa@servidor.com.br) |
| **MV\_TSAINT** | Identifica se a integração será realizada com o TSA ou Suricato. .T. = TSA, .F. = Suricato | .F. |
| **MV\_APISUR** | Define se a integração do Suricato com o Protheus ocorre por API (.T.) ou direto no banco (.F.) | .F. |
| **MV\_TSADTAD** | Define se na transferência o sistema utilizara a data de admissão ou a data da transferência para a tag HiringDate. .T.=Dt Adm,.F.=Dt Transf | .F. |

Para envio dos ***logs***por ***email*** utilizando o **parâmetro MV\_TSATLOG = 1**, é necessário se atentar aos **parâmetros** abaixo:  
**MV\_RELACNT** - Conta utilizada para envio do e-mail  
**MV\_RELSERV** - Endereço do servidor de e-mail  
**MV\_RELPSW** - Senha da conta utilizada para envio do e-mail  
**MV\_RELAUSR** - Usuário de autenticação de e-mail  
**MV\_RELAPSW** - Senha do usuário de autenticação de e-mail  
**MV\_RELFROM** - Endereço de e-mail que ira disparar o e-mail  
**MV\_RELAUTH** - Faz autenticação no servidor de e-mail  
  
Caso o conteúdo do **parâmetro MV\_TSATLOG** esteja como **5**, os **XMLs** de **envio** e **retorno** serão gerados na pasta ***System***, essa opção é útil para **analisar erros**, porém, existe uma queda de **performance**. Neste caso orientamos que o cliente gere os arquivos desta forma apenas para análises pontuais.  
Entende-se por **XML** de **envio**:  
**Numero Sequencial\_SND.XML** → XML enviado ao Suricato. Exemplo: 12345678\_SND  
Entende-se por **XML** de **retorno**:  
**Numero Sequencial\_RCV.XML** → XML recebido do suricato como retorno do XML SND. Exemplo: 12345678\_RCV.  
  
  
**INTEGRAÇÕES REALIZADAS ENTRE OS PRODUTOS**  
Para verificar as integrações feitas entre o Ponto Eletrônico e Suricato, você pode clicar [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16980211725335-RH-Linha-Protheus-PON-x-Suricato-Quais-dados-s%C3%A3o-integrados-do-Ponto-Eletr%C3%B4nico-para-o-Suricato)  
Para verificar as integrações feitas entre a Folha de Pagamento e Suricato, você pode clicar [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16981120406551-RH-Linha-Protheus-GPE-x-Suricato-Quais-dados-s%C3%A3o-integrados-da-Folha-de-Pagamento-para-o-Suricato)  
  
**TABELAS, ROTINAS E WEBSERVICES ENVOLVIDOS NA INTEGRAÇÃO**  
Para verificar as tabelas, rotinas e webservices envolvidos na integração entre o Ponto Eletrônico e Suricato, você pode clicar [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16981752786455-RH-Linha-Protheus-PON-x-Suricato-Rotinas-Webservices-e-Tabelas-envolvidas-na-integra%C3%A7%C3%A3o-do-Ponto-Eletr%C3%B4nico-x-Suricato)  
Para verificar as tabelas, rotinas e webservices envolvidos na integração entre o Ponto Eletrônico e Suricato, você pode clicar [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16982531856535-RH-Linha-Protheus-GPE-x-Suricato-Rotinas-Webservices-e-Tabelas-envolvidas-na-integra%C3%A7%C3%A3o-da-Folha-de-Pagamento-x-Suricato)

**MONTAGEM DO CONTEÚDO DO XML E PRINCIPAIS OCORRÊNCIAS NA INTEGRAÇÃO**  
Para verificar em detalhes exemplos da montagem do arquivo XML de integração do Protheus para o Suricato, você pode clicar [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16983749875351-RH-Linha-Protheus-PON-x-Suricato-XML-da-Integra%C3%A7%C3%A3o-com-o-Suricato)

**LEITURA DE MARCAÇÕES VINDA DO SURICATO ATRAVÉS DE INTERFACE OU SCHEDULE E PORTARIA 671**  
Para consultar em detalhes as tabelas que recebem as marcações de Ponto vindas do Suricato, configuração de relógio ou Schedule, você pode clicar [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16984496753175-RH-Linha-Protheus-PON-x-Suricato-Leitura-de-Marca%C3%A7%C3%B5es-vindas-do-Suricato)  
  
**Saiba Mais:**  
[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[Integração Protheus x Suricato](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546695095)  
[Schedule - Leitura/Apontamento das Marcações](https://tdn.totvs.com/pages/releaseview.action?pageId=631321258)  
[Pacote de Expedição Contínua - Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
