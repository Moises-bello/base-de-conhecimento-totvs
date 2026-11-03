---
article_id: 4409144283927
category: eSocial - Middleware
content_hash: 06f15fe9103891490b594601b9e093e4e61679cb8246051dce2a9a7e1b3dc0fb
fetched_at: '2026-06-28T22:47:05.596667+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Certificado Digital Middleware: Erro ao consultar/cadastrar
  entidade no TSS. IE inválida'
type: support-article
updated_at: '2024-06-07T20:40:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409144283927-RH-RM-FOP-eSocial-Certificado-Digital-Middleware-Erro-ao-consultar-cadastrar-entidade-no-TSS-IE-inv%C3%A1lida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao realizar a ativação do Middleware ou a atualização do certificado digital é apresentada mensagem de erro:  **Erro ao consultar/cadastrar entidade no TSS. TOTVS Service SOA TSS : TOTVS Service SOA TSS CNPJ:XXXXXXX CPF: IE:XXXXXXX UF:XX Empresas: XXX - IE invalida**.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409191327895/mceclip0.png)**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**O erro geralmente ocorre quando o número de **Inscrição Estadual**, presente no cadastro da **Coligada**, está incorreto.

![](https://totvssuporte.zendesk.com/attachments/token/FNpOzYEsPjzSIoh2vRlXh2Fh2/?name=inline-1949847963.png)

**Solução**Para ajuste da ocorrência, siga os passos abaixo:

1. Acesse o site do **Sintegra** ([Sefaz](http://www.sintegra.gov.br/)) e selecione o estado correspondente;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409143266711/mceclip1.png)

2. Na janela que será aberta, informe a identificação da empresa (CNPJ, CPF, etc.);  
3. Após concluir a consulta e verificar as devidas informações, acesse novamente no RM o menu **Administração de Pessoal | Cadastros Globais | Coligadas** e edite a coligada utilizada;  
4. No campo **Inscrição Estadual**, informe o valor correto não deixando espaços ao final do número. Salve o cadastro;  
5. Faça novamente o processo de ativação ou atualização de certificado.  
  
**Observação:**  
A Inscrição Estadual, na maioria das vezes, possui 9 números a até 14 dígitos, a depender do estado\*. Caso necessário, favor incluir o zeros a esquerda.

\* De acordo com o Manual de Orientação do Contribuinte (MOC).
