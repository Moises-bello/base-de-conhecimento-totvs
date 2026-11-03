---
article_id: 360049690673
category: TAF - eSocial - Configuração
content_hash: a4d60a387a7eda879e61e1a22d06a4ca58925da81329e6b1d06cafec7a2b24af
fetched_at: '2026-06-28T22:45:14.394671+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Num de inscrição diferente
  do certificado digital
type: support-article
updated_at: '2026-06-23T20:58:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049690673-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Num-de-inscri%C3%A7%C3%A3o-diferente-do-certificado-digital
---

**Ocorrência**Essa mensagem de erro significa que o numero de inscrição cadastrado no TAF é diferente do utilizado no certificado digital.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração - Todas as versões

**Solução**1 - Caso o certificado tenha o mesmo número de inscrição da empresa que está configurando, verifique no cadastro dessa empresa se o numero de inscrição esta correto;

2 - Para isso acesse o configurador digitando SIGACFG no campo programa inicial do SmartClient:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727790155799)

3 - No configurador acesse o cadastro de filiais através do menu: Ambiente | Empresas | Filial:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727818089111)

4 - Selecione a filial ou matriz em questão e click em alterar, a próxima tela é o cadastro dessa filial, verifique se os campos da abá "Dado Gerais" e "Endereço Fiscal/Entrega" estão preenchidos, os campos chave são "Tipo de Inscrição" e "CNPJ ou CPF" na aba "Dado Gerais" e o campo "Estado Fiscal/Entrega" na aba "Endereço Fiscal/Entrega" onde deve ser informado a UF. Caso faça alguma alteração nesses dados click em Confirmar para salva-los:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074359093)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073166714)

5 - Acesse o SIGATAF e vá na opção Complemento cadastral através do menu:

Atualizaçoes | Configs. Taf | Complemento Cadastral:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727818096023)

6 - Selecione a empresa responsável pelas transmissões ao e-Social e informe o CNPJ do certificado digital no campo "CNPJ Transm" na aba "Outras informações":

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073167294)

7 - Verifique o Certificado Digital se caso o mesmo seja por outorga é necessário informar o CNPJ ou CPF do certificado no completo cadastral do TAF e na Wizard de configuração do TSS;

8 - Reveja a documentação da Configuração do Certificado Digital e verifique no artigo a informação da Outorga caso seu certificado possua procuração:

[RH - Linha Protheus - TAF - eSocial - Configuração - Como configurar o Certificado Digital no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001814402-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-configurar-o-Certificado-Digital-no-TAF)
