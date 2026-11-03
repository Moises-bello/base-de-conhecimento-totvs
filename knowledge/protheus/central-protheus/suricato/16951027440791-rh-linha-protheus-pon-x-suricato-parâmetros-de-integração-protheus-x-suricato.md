---
article_id: 16951027440791
category: Suricato
content_hash: f05b552c5866c8a885a563a4200c05052fab49ae04f880815b931f82c0a0f79a
fetched_at: '2026-06-28T22:44:57.438456+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - PON x Suricato - Parâmetros de integração Protheus x
  Suricato
type: support-article
updated_at: '2023-12-20T16:44:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16951027440791-RH-Linha-Protheus-PON-x-Suricato-Par%C3%A2metros-de-integra%C3%A7%C3%A3o-Protheus-x-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16951064661655) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais são os **parâmetros para integração do Protheus com o Suricato?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.23  
  
**Solução**A integração do **Protheus x Suricato** acontece através de **parâmetros** e **Webservices,** que anteriormente eram utilizados pelo TSA. É importante que o **Suricato** já esteja **instalado e configurado** para seguir os passos citados nesta documentação.

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

Para envio dos ***logs*** por ***email*** utilizando o **parâmetro MV\_TSATLOG = 1**, é necessário se atentar aos **parâmetros** abaixo:  
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
  
**Saiba Mais:**[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[Integração Protheus x Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16779731236119)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
