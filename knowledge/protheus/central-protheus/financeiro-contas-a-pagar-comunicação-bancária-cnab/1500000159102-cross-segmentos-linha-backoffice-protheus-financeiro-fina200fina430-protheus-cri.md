---
article_id: 1500000159102
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: a7f93f73399ed07ab69bd52c86153ffcbd0900692dcd5dd1d7e592211d9d083e
fetched_at: '2026-06-28T22:37:55.108809+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Linha BackOffice Protheus - Financeiro - FINA200/FINA430
  - Protheus criando bancos sozinho ao processar o retorno bancário
type: support-article
updated_at: '2025-08-01T18:07:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000159102-Cross-Segmentos-Linha-BackOffice-Protheus-Financeiro-FINA200-FINA430-Protheus-criando-bancos-sozinho-ao-processar-o-retorno-banc%C3%A1rio
---

**Dúvida**Em muitos casos, no Protheus, contas correntes estão sendo criadas sem a intervenção direta do usuário. Por qual motivo isso pode acontecer?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Causa**O Protheus realiza a criação dos bancos com base nas informações contidas no arquivo de retorno, uma vez que o Header desse arquivo possui campos específicos para agência e conta.**Exemplo:**  
**21H COD. AGENCIA 0530570**   
**21H DIG. VERIFIC 0580580**   
**21H NUM. C/CORR 0590700**   
**21H DIGITO VER.CONT0710710**   
**21H DIG. VERIF.AG/C0720720**

Ao processar o arquivo de retorno, essas posições são validadas e conferidas dentro do cadastro de bancos SA6   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33882826979991)

**Casos os valores não batam**, será automaticamente criado este banco baseado nas posições armazenadas pelo arquivo de configuração e irá gerar a movimentação no novo banco.

**Solução**

Para não gerar uma nova conta bancária, existem 03 opções;  
  
01 - Ajustar o **arquivo de configuração (retorno)** para que os dados da conta de retorno sejam corretamente extraídos do Header do arquivo (primeira linha), por meio do caminho: **Configurador >> Cadastros.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33882826988439)  
  
02 - Aplicar os dados bancários na **Sub-conta** utilizada no processamento do retorno, na **aba 'Outros', utilizando as informações do Banco Oficial.**Ao adicionar o **Banco Oficial,** as baixas sempre serão neste **banco / agencia / conta** independente do retorno do arquivo de configuração  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33882836748823)

03- Utilizando pontos de entrada para efetuar a baixa pelo **Portador** do título, seja **pagamento ou recebimento.**

* **Recebimento****: [F200PORT - Definição de banco na baixa](https://tdn.totvs.com/pages/releaseview.action?pageId=6070980)**
* **Pagamento:** **[F430PORT - Define se utiliza o Portador ou o banco](https://tdn.totvs.com/pages/releaseview.action?pageId=648838953)**

**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações para uso do CNAB - Modelos 1 e 2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407)
