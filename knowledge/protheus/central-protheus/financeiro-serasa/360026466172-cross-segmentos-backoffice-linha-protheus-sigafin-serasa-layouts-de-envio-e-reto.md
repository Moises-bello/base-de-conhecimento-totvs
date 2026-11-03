---
article_id: 360026466172
category: Financeiro - Serasa
content_hash: 44e825de6012c11309a5b738f44f0e830cd7ad58a7e190a39045258f0f2a1919
fetched_at: '2026-06-28T22:37:28.275144+00:00'
product: protheus
section_id: 35058289522071
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  SERASA - Layouts de
  envio e retorno utilizando MILE
type: support-article
updated_at: '2026-01-30T12:35:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026466172-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-SERASA-Layouts-de-envio-e-retorno-utilizando-MILE
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38043912413463)***Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como configurar o Layout de envio e retorno utilizando o Mile para SERASA?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução:**  
Para utilização do envio e recebimento de arquivos SERASA, deve-se importar os *layouts* MILE **serasa\_layout\_envio.xml**e **serasa\_layout\_retorno.xml**, disponibilizados junto com o release 12.1.6.

A importação dos *layouts* no MILE, podem ser modificados, de forma a atender alguma customização ou particularidade do ambiente. Para importa-los é necessário realizar os procedimentos abaixo:

* No **Configurador (SIGACFG)** acesse **Ambiente** > **Aceleradores** > **Mile** >***Layouts***
* Selecione a opção **Importar**.

**Observação:** A nomenclatura dos *layouts*, **SERA\_ENV**(envio) e **SERA\_RET**(retorno) são padrão para uso no protheus e não podem ser alterados.

**Estrutura do layout SERASA**

O *layout* de envio SERASA possui a seguinte estrutura:

***Header*****:**

**![SERASA_-_Layouts_de_envio_e_retorno_utilizando_MILE_-_Linha_Microsiga_Protheus_-_TDN_-_Google_Chrome_7.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360027198351)**

***Detail*****:**

**![SERASA_-_Layouts_de_envio_e_retorno_utilizando_MILE_-_Linha_Microsiga_Protheus_-_TDN_-_Google_Chrome_8.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360027198651)**  
**![SERASA_-_Layouts_de_envio_e_retorno_utilizando_MILE_-_Linha_Microsiga_Protheus_-_TDN_-_Google_Chrome_9.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360027192252)**

***Trailer*****:**

**![SERASA_-_Layouts_de_envio_e_retorno_utilizando_MILE_-_Linha_Microsiga_Protheus_-_TDN_-_Google_Chrome_10.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360027192352)**

**O** ***layout*** **de retorno SERASA possui a seguinte estrutura:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027198771)**

**Importante:**  
Cada variável corresponde ao campo definido no *layout* de retorno. Caso o *layout* de retorno seja customizado, esses campos devem ser mantidos, apenas novos campos podem ser inseridos no *layout*.  
As variáveis são alimentadas a cada linha lida do arquivo. Para identificar se a linha corresponde ao *Header*, *Detail* ou *Trailer* do arquivo, valide o conteúdo da variável **TP\_REG**, sendo: "0" = *Header*; "1" = *Detail*; "9" = *Trailer*.

**Saiba mais:**  
[**SERASA - Layouts de envio e retorno utilizando MILE**](http://tdn.totvs.com.br/display/public/PROT/SERASA+-+Layouts+de+envio+e+retorno+utilizando+MILE)
