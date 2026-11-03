---
article_id: 360050367993
category: NFe - Nota Fiscal Eletrônica
content_hash: 1d502495aeca35f3aee92c9172af5332e448faaa7ef3ff72445b99d90e871836
fetched_at: '2026-06-28T22:40:06.642760+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a TAG
  (e-mail) <email>
type: support-article
updated_at: '2025-08-12T00:09:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050367993-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-e-mail-email
---

**Dúvida**

Como gerar a TAG (e-mail) <email> ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Se a nota utilizar o cadastro de  Cliente preencher o campo  **A1\_EMAIL  "E-mail"**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074582334)

2- Se a nota utilizar o cadastro de  fornecedor preencher o campo  **A2\_EMAIL  "E-mail"**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074583674)**

3- Se for o e-mail da transportadora preencher o campo  **A4\_EMAIL  "E-mail"**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075797893)**

* **Saiba mais:**

Se houver mais de um ***e-mail*** o mesmo deve ser separado ***por ponto e vírgula ; sem espaço.***

***No XML***será levado até 60 caracteres, conforme o ***Manual do Contribuinte abaixo página 181:***

[Manual de Orientação do Contribuinte - versão 6.00](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=nebWFce4X9o=)

Porém ***na tabela do TSS será gravados até 250 caracteres,*** para a transmissão dos e-mails.

Para configurar o ***Danfe e o XML por e-mail verificar*** o link abaixo:

[MP - TSS - Como enviar DANFE por e-mail via TSS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043007793)

Para cadastrar quem pode consultar a ***Nota no Portal da Sefaz Nacional temos o link abaixo:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a Tag AUTXML (Ajuste Sinief 16/2018)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020670492)

* **Importante:**

Em **homologação,** será enviado **automaticamente o e-mail para a empresa o emitente e não para o destinatário.**

Para gerar o e-mail do cadastro do **Redespacho** temos**três opções de processos** a ser seguido:  
  
1- Esses casos devem ser customizados o **NFESEFAZ .**  
  
 [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)   
  
**Rdmake disponível no link acima.**  
  
2- Segunda opção pode ser aberto melhoria na Central Colaborativa:  
  
[***Central Colaborativa TOTVS.***](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
**Para saber como criar uma sugestão de melhoria clique [*AQUI.*](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)**  
  
  
3- Para que seja atendido no padrão é necessário que a empresa tenha alguma legislação na qual informe a obrigatoriedade de gerar conforme deseja.  
  
Havendo a legislação abra um ticket no suporte e nos encaminhe que será compartilhado **junto a consultoria tributária da TOTVS e posteriormente ao produto.**
