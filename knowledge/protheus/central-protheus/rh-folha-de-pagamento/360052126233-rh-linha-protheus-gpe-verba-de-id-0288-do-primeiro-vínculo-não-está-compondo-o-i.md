---
article_id: 360052126233
category: RH - Folha de Pagamento
content_hash: 364c35198d6ea73d9297f1f2261a402c76008a08c01dac5b9c9f1ba496934411
fetched_at: '2026-06-28T22:44:16.417147+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Verba de ID 0288 do primeiro vínculo, não está
  compondo o IR do pagamento 02 do semanalista do segundo vínculo
type: support-article
updated_at: '2024-09-12T21:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052126233-RH-Linha-Protheus-GPE-Verba-de-ID-0288-do-primeiro-v%C3%ADnculo-n%C3%A3o-est%C3%A1-compondo-o-IR-do-pagamento-02-do-semanalista-do-segundo-v%C3%ADnculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337541699351) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Por que verba de ID 0288 do primeiro vínculo mensalista, não está compondo o IR do pagamento 02 do semanalista do segundo vínculo, com isso, a composição do IR está incorreta, calculando valor de IR a maior para o funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Hoje temos uma nova rotina de múltiplos vínculos. Utilizando a nova rotina e efetuando os cadastros abaixo o cálculo fica correto.

No **Configurador (SIGACFG),**acesse **Ambientes/Cadastro/Menu (CFGX013)**. Informe a nova opção de menu **SIGAGPE**, conforme instruções a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081815513)  
  
Realizado a liberação de nova rotina (GPEM930) onde será possível consultar todos os funcionários que possuam mais de um vínculo e efetuar o cálculo deles isoladamente do restante dos funcionários. O cálculo através das demais rotinas continua funcionando normalmente, o diferencial desta tela é que será possível calcular todos os vínculos de uma só vez.   
 **Principais Campos e Parâmetros**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080752434)****Identificadores de Cálculo necessários:**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080752494)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080752534)**

É necessário estar com o ambiente atualizado (pacote da expedição contínua e dicionários) incluisive executar o upddistr para a criação dos novos campos para a nova rotina.

<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO>

**Existe o mnemônico abaixo que deve estar habilitado**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080753074)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081816313)

Cadastro das verbas de desconto do INSS, identificador 0064:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081816493)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081816553)  
  
Cadastro da verba INSS Outras Empresas - identificador 0289:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081816593)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081816633)  
  
Cadastro da tabela de INSS:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081816793)

Cadastro da tabela de IR:

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081816953)

Cadastro de período para o Pro-Labore mensalista

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081817073)

Cadastro de período para o Autônomo semanalista

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081817133)![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080753814)  
  
Cadastro da primeira matrícula:

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080753934)  
  
![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080753974)  
  
![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080754014)  
  
![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080754074)  
  
Cadastro da segunda matrícula:

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080754114)  
  
![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080754154)  
  
![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080754194)  
  
![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080754234)

Cálculo realizado pela rotina GPEM930, poderá ser realizado também pelas rotinas GPEM020 ou GPEM020A.

![mceclip25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080754294)

Primeiro recibo do nº de pagamento 01, funcionário semanalista:

![mceclip26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081817613)

**Análise:**Houve desconto do teto do INSS neste recibo.  
Conferência Base IRRF: Verba 191 (15.186,89) - INSS (671,11) = 14.515,78  
Conferência Desc IRRF: Base IRRF (14.515,78) \* Alíquota (27,5%) - Dedução (869,36) = 3.122,47  
  
Segundo recibo do nº de pagamento 01, funcionário mensalista:

![mceclip27.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081817653)  
  
**Análise:**Não houve desconto de INSS, pois no outro recibo já atingiu o teto.  
Conferência Base IRRF: Verba 190 e 849 (15.236,38 + 14.515,78(já tem a dedução do INSS)) = 29.752,16  
Conferência Desc IRRF: Base IRRF (29.752,16) \* Alíquota (27,5%) - Dedução (869,36) - IRRF do outro recibo (3.122,47) = 4.190,01  
  
Único recibo do nº de pagamento 02, funcionário semanalista:

![mceclip29.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081817773)

**Análise:**Não houve desconto de INSS, pois no outro recibo já atingiu o teto.  
Conferência Base IRRF: Verba 705 e 849 (29.702,67 + 15.236,38) = 44.939,05  
Conferência Desc IRRF: Base IRRF (44.939,05) \* Alíquota (27,5%) - Dedução (869,36) - IR pago no 1º vínculo (4.190,01) - IR pago no 2º vínculo do Pagamento 01 (3.122,47)  = 4.176,39

***Verifique que para a composição dos encargos de INSS e IR, foram considerados todos os vínculos.***

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
