---
article_id: 360052077593
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 03d4a5af5d7ca4644047b74b8d8a0fab8ec9f7f575d752ed7280a15e74640aaf
fetched_at: '2026-06-28T22:45:21.183628+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - TSS - Erro 607: O número de inscrição
  do transmissor deverá ser igual ao CNPJ/CPF do certificado utilizado para o envio
  do lote'
type: support-article
updated_at: '2026-06-26T12:03:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052077593-RH-Linha-Protheus-TAF-eSocial-TSS-Erro-607-O-n%C3%BAmero-de-inscri%C3%A7%C3%A3o-do-transmissor-dever%C3%A1-ser-igual-ao-CNPJ-CPF-do-certificado-utilizado-para-o-envio-do-lote
---

**Dúvida**

Ao transmitir os eventos para o e-Social, ocorre o erro conforme mensagem:

**Erro 607: O número de inscrição do transmissor deverá ser igual ao CNPJ/CPF do certificado utilizado para o envio do lote**

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões

**Solução**

1 - Pare o serviço do TSS;

2 - Limpe o console.log do TSS;

3 - Faça a atualização do TSS conforme link abaixo:

[Automação Fiscal - ATUALIZAÇÃO - Links para atualizar o TSS - Transmissão de Documentos Eletrônicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7658806742679-Automa%C3%A7%C3%A3o-Fiscal-ATUALIZA%C3%87%C3%83O-Links-para-atualizar-o-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos?source=search)

4- Inicie o serviço do TSS;

5 - Acesse o SIGATAF e vá no Complemento Cadastral da empresa. Atualizações -> Config's TAF -> Complemento Cadastral:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080637414)

6 - Na rotina de complemento cadastral da empresa, selecione a empresa em questão e clique em **Alterar:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080637674)**

7 - Na aba Complemento do Estabelecimento e Outras Informações, informe o CNPJ do Certificado Digital do seu procurador:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080639314)

8 - Inicie o serviço do TSS, e refaça a configuração do Certificação Digital conforme ***links*** abaixo:  
  
**Obs.:** Na opção de configuração do certificado digital em "Atualizações -> Configs. TAF -> Wizard Config. TSS" certifique-se no termino da configuração se os dados que serão apresentados do certificado digital são da própria empresa configurada no TAF. Os passos 5, 6 e 7 são para clientes que possuem Certificado Digital por outorga/procuração!

A- Certificado Tipo A1:

**Realizando a preparação do Certificado Digital:**

[TAF - CERTIFICADO DIGITAL A1 - Como realizar a preparação do Certificado Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034159554-TAF-CERTIFICADO-DIGITAL-A1-Como-realizar-a-prepara%C3%A7%C3%A3o-do-Certificado-Digital?source=search)

B -Como atualizar o Certificado Digital:

[TAF - CONFIGURAÇÃO - Inserindo o Certificado Digital no TAF e Smart eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527832-TAF-CONFIGURA%C3%87%C3%83O-Inserindo-o-Certificado-Digital-no-TAF-e-Smart-eSocial?source=search)

C - Certificado Tipo A3:

**Realizando a preparação do Certificado Digital:**

[TAF - CERTIFICADO DIGITAL A3 - Como realizar a preparação do Certificado Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034171074)

D - Como atualizar o Certificado Digital:

[TAF - CONFIGURAÇÃO - Inserindo o Certificado Digital no TAF A3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034238914)

9 - Acesse o monitoramento dos eventos de transmissão e reenvie os registros para o governo.
