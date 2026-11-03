---
article_id: 360031814193
category: eSocial - Cadastros
content_hash: faeef0db7460905fa25484fe2da25bb92637d65921595f4e8ea13d388cfc99a5
fetched_at: '2026-06-28T22:47:14.385835+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial  - Cadastro do CAEPF
type: support-article
updated_at: '2026-01-26T15:59:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031814193-RH-RM-FOP-eSocial-Cadastro-do-CAEPF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24503293844119)**Tempo aproximado para leitura:**00:02:00 min**

**Dúvida**  
O que é CAEPF e como cadastrá-lo no RM?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial  - A partir da versão 12.1.22  
  
**Solução**  
Conforme **Instrução Normativa RFB Nº 1828**, de 10 de Setembro de 2018, o **CAEPF** é o cadastro da Secretaria da Receita Federal do Brasil (RFB) com informações das atividades econômicas exercidas pela pessoa física, quando dispensadas de inscrição no Cadastro Nacional da Pessoa Jurídica (CNPJ).

A estrutura do **CAEPF** comporta os primeiros 9 (nove) dígitos do CPF, seguido do número de ordem respeitada cada inscrição do **CAEPF** e complementado pelo número de controle do cadastro conforme imagem abaixo:

![image2019-2-21_11-19-48.png](http://tdn.totvs.com/download/attachments/458780869/image2019-2-21_11-19-48.png?version=1&modificationDate=1550758788293&api=v2)

O campo **CAEPF** está disponível no cadastro de seção quando a coligada é identificada por CPF ou CEI. Ao incluir ou alterar este campo, será disparado um gatilho (inclusão ou alteração) para o evento **S-1005**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043067933)

Ao gerar o evento **S-2200** ou **S-1200** para funcionário onde a seção centralizadora possua o campo **CAEPF** preenchido, os XMLs serão exibidos conforme abaixo:

• **S-1200**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042215314)

• **S-2200**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043063253)

**Saiba mais**  
Acesse [CAEPF](http://tdn.totvs.com/display/LRM/CAEPF) para mais informações.
