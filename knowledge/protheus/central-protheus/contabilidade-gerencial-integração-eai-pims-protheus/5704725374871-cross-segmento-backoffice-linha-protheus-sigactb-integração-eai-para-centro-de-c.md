---
article_id: 5704725374871
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: 7ab7109700c11bafe3f4852ab1b04dee5ee6ab3449cff8365d60389c989333e6
fetched_at: '2026-06-28T22:40:54.192637+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Integração EAI para
  centro de custo
type: support-article
updated_at: '2023-11-14T17:02:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5704725374871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Integra%C3%A7%C3%A3o-EAI-para-centro-de-custo
---

**Dúvida**Como configurar no protheus a integração de Centro de Custo via canal EAI  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Contabilidade Gerencial – Todas as versões  
  
**Solução**  
Realize os seguintes passos:  
1. Configure o **WebService** do Protheus conforme a documentação: [Cross Segmento - Backoffice Linha Protheus - SIGACTB/SIGAATF - Como Configurar o EAI no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410199853207-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAATF-Como-Configurar-o-EAI-no-Protheus?source=search)  
  
2. Cadastre o **adapter** do centro de custo, para acessar a rotina de adapter entre no configurador > Ambiente > Schedule > Adapter e.a.i. Segue exemplo de preenchimento:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5704089773463)

3. Após cadastrado o adapter em caso de envio para outros sistemas, basta criar o centro de custo via rotina **CTBA030** como é feito normalmente, que o sistema irá enviar o cadastro feito para o outro produto parceiro da TOTVS na rota informada no parâmetro **MV\_EAIURL2** (em dúvida do parâmetro consulte a documentação do passo 1).

4. Em caso de recebimento, o Protheus já lerá o arquivo enviado do outro produto e importará conforme o cadastro de **DePara** de Empresa/Filial, para acessar esse cadastro entre no configurador > Ambiente > Schedule > Emp. Filial Mensagem Única. Segue exemplo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19060888718999)

No exemplo da imagem acima, informo que a empresa 1 e filial 1 do RM se comunicará com o grupo de empresas 99 e filial 01 do Protheus.

5. Após a integração feita, sendo enviado ou recebido pelo Protheus o sistema criará um registro de **DEPARA** de informações, que demonstra o valor no outro produto e no Protheus, para verificar entre no configurador > Ambiente > Schedule > De/para de Mensagem Única:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5704398548247)

Acima podemos ver como exemplo, o valor externo que é o conteúdo usado pelo RM para se referir ao centro de custo e o valor interno que é a chave interna do Protheus para encontrar o centro de custo.

No Protheus o valor interno ficará sempre como XX|ZZZZ|COD, onde o XX é o grupo de empresa, o ZZZZ é como o campo filial está preenchido dentro do CTT\_FILIAL e o COD é o código do centro de custo.

**Dica:**Além de utilizar outras marcas é possível validar o recebimento das informações no Protheus a partir do SOAPUI, nesse caso poderá seguir a documentação [Como configurar o SOAP UI](https://tdn.totvs.com/pages/releaseview.action?pageId=224395491) para configurar e após isso basta utilizar o XML de envio(que pode ser o gerado através do próprio sistema, como RM, LOGIX e etc) no teste:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5704561740951)
