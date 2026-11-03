---
article_id: 11464498386455
category: Quírons
content_hash: 53cd079274dc63fef5108f7db32b7ac479d9b9307f2c2a8ae0d2bd23b17c74e2
fetched_at: '2026-06-28T22:42:52.172535+00:00'
product: protheus
section_id: 9033517492119
source: central-protheus
title: RH - Linha Protheus - GPE - Quírons - Como consultar o Status das integrações
  no Monitor dentro do Protheus
type: support-article
updated_at: '2025-04-15T20:28:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11464498386455-RH-Linha-Protheus-GPE-Qu%C3%ADrons-Como-consultar-o-Status-das-integra%C3%A7%C3%B5es-no-Monitor-dentro-do-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18704370546455) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como consultar o ***status*** das **integrações para o Quírons** na rotina de **Monitor de Integração** (GPEM924) dentro do Protheus?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para verificar se os dados foram ou não **integrados para o Quírons**, deve ser acessada a rotina de **Monitor de Integração (GPEM924).**  
  
Ao acessar a rotina, serão exibidos em tela os registros gerados na tabela **RJP**, que são criados quando a **Carga Inicial é processada** **ou quando são feitas movimentações relacionadas aos Funcionários**, como transferências, demissões, etc.  
  
Os registros podem ser classificados por:  
**>** Falha na Integração (legenda vermelha)  
**>** Pendente de Integração (legenda azul)  
**>** Processado e Integrado (legenda verde)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31439234499735)  
  
  
Para registros com *status* de **Falha**, é possível fazer o **Reenvio**, ou seja, **disponibilizar novamente este registro na tabela RJP**, de modo que o Protheus tente integrá-lo mais uma vez ao Quírons:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31439238735767)  
  
  
É possível também visualizar **detalhes dos registros**, como a data em que ele foi gerado/integrado, qual foi o retorno da integração, o usuário responsável por gerar este dado, etc:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31439238737815)  
  
  
Dentro do botão **Outras Ações**, é possível fazer uma **limpeza nos registros** exibidos em tela, podendo ser escolhido se essa limpeza será uma exclusão permanente ou não:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31439238739223)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31439238741527)  
  
  
  
Além dos dados da rotina de **Monitor de Integração**, é possível fazer com que o Protheus armazene um **histórico de envio** contendo inclusive o arquivo *json* da integração. Para isso, é necessário configurar o parâmetro [**MV\_HISTQUI**](https://tdn.totvs.com/pages/viewpage.action?pageId=809135189) como 1 (grava apenas histórico de erros) ou 2 (sempre grava o histórico).  
Estes dados serão armazenados na tabela **RU7** **após o processamento do *job* da rotina de integração GPEM923**, e ficarão disponíveis para consulta na rotina de **Monitor de Integração** dentro da opção **Outras Ações - Histórico de Envio:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31439234504599)  
  
  
Para visualizar os **dados gerados no arquivo *json*** para integração, clique em **MEMO** no campo **Mensagem:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31439234505751)  
  
  
  
Para visualizar qual foi o **retorno da integração**, clique em **Memo** no campo **Ret. Integ:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31439238745367)  
  
**OBS:** cabe ressaltar que **não é obrigatório habilitar o parâmetro MV\_HISTQUI**, porém, o time de Suporte pode solicitar esta ação ao cliente para uma análise mais aprofundada em cenários de erro na integração.

**Saiba Mais:**  
[Integração | Protheus SIGAGPE x Quírons](https://tdn.totvs.com/pages/releaseview.action?pageId=793200883#Integra%C3%A7%C3%A3o|ProtheusSIGAGPExQu%C3%ADrons|-05.CARGAINICIAL)  
[Artigos sobre Quírons](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9033517492119-Qu%C3%ADrons)
