---
article_id: 26460431901719
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 9a5977096c7c6bf1cfd8e1f1fd22aebe79c62f4762444f90752c448404327dcf
fetched_at: '2026-06-28T22:37:55.072668+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - E-mail não
  está sendo enviado
type: support-article
updated_at: '2026-01-28T17:36:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26460431901719-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-E-mail-n%C3%A3o-est%C3%A1-sendo-enviado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26507119296663)** Tempo aproximado para leitura: **00:08:00 min**

**Dúvida**  
O que fazer quando não envia o e-mail com o boleto?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**

Validar os parâmetros a seguir:

| **Parâmetro** | | **Definição** |
| --- | --- | --- |
| **FINA811** **<= 23/08/2022** | **FINA811** **> 23/08/2022** |
| **MV\_RELSERV** | | Nome do servidor de envio de e-mail |
| **MV\_RELACNT** | **MV\_FINACNT** | Conta a ser utilizada no envio de e-mail |
| **MV\_RELPSW** | **MV\_FINPSW** | Senha da conta de e-mail |
| **MV\_RELFROM** | **MV\_FINFROM** | E-mail utilizado no campo FROM no envio do e-mail |
| **MV\_RELBODY** | | Determina o assunto padrão no envio do e-mail. Será usado quando o campo FWP\_TXTASS não for preenchido |
| **MV\_RELAUTH** | | Determina se o servidor exige autenticação |
| **MV\_RELAUSR** | **MV\_FINACNT** | Usuário para autenticação no servidor de e-mail (caso servidor assim exigir) |
| **MV\_RELAPSW** | **MV\_FINPSW** | Senha para autenticação no servidor de e-mail (caso servidor assim exigir) |

Após a configuração dos parâmetros, também no **Configurador**, menu **Ambiente, E-mail/proxy,** **configurar**, preencha o nome do **servidor de envio de e-mail**, o **endereço de e-mail de autenticação** e a respectiva **senha**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460431869975)  
   
   
Ajustar as configurações conforme a imagem a seguir:  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26460431876247)  
   
Dependendo do provedor, pode ser necessário realizar a verificação em duas etapas ou verificar com o provedor de e-mail se consta algum bloqueio.

[Envio de boleto - Visão geral](https://tdn.totvs.com/pages/releaseview.action?pageId=635983295)  
 

É necessário vincular a **carta de cobrança** referente ao **envio do boleto** ao parâmetro **MV\_NGFCART**.

No cadastro do **Cliente**, o e-mail deve ser cadastrado em complemento do cliente e habilitar o campo "**recebe Bol**" =sim

No cadastro do **Cliente**, o e-mail deve ser inserido em **Complemento do Cliente**, o campo "**recebe Bol**" deve ser habilitado como "**sim**".  
   
![](https://totvssuporte.zendesk.com/attachments/token/NHN2OnmTQvcLCyaRKfap4Ve44/?name=image.png)  
   
 

**Importante**

Atualmente, não existem parâmetros no sistema que realizem a limitação do envio de boletos. Nesses casos, eventuais restrições podem estar relacionadas ao próprio provedor de e-mail. Dessa forma, recomendamos a validação junto ao provedor para verificar a existência de bloqueios ou limitações quanto à quantidade de envios.

**Saiba mais**

[How To - Envio boleto via API](https://www.youtube.com/watch?v=7UxMVQ_O6A0)

[Carta de Cobrança - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=492706741)  
[Parâmetro MV\_NGFCART](https://tdn.totvs.com/pages/releaseview.action?pageId=620541089)

[Configurar o SMTP para envio de relatórios por e-mail](https://tdn.totvs.com/pages/releaseview.action?pageId=271166884)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN – FINA811 - Erro Falha de autenticação no envio de carta de cobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062679833-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA811-Erro-Falha-de-autentica%C3%A7%C3%A3o-no-envio-de-carta-de-cobran%C3%A7a?source=search)
