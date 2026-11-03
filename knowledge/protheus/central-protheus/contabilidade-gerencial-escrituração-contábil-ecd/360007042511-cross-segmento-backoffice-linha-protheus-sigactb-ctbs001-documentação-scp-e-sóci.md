---
article_id: 360007042511
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 2df98a5edf905652dd5be44f625d272f37766b3216a6376a2db4749712f51f60
fetched_at: '2026-06-28T22:40:44.544459+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - Documentação
  SCP e Sócio Ostensivo
type: support-article
updated_at: '2023-06-01T17:47:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007042511-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Documenta%C3%A7%C3%A3o-SCP-e-S%C3%B3cio-Ostensivo
---

**Dúvida**Como gerar/cadastrar SCP e Sócio Ostensivo na ECD e ECF?

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.8

**Solução**

Para entrega da ECD e ECF pela SCP é necessário:

* Que a SCP esteja cadastrada como uma filial da empresa principal (Sócio Ostensivo) e possua um CNPJ próprio.

[Apresentação por CNPJ da SCP - Sociedade em Conta de Participação e Obrigações Acessórias](http://tdn.totvs.com/pages/releaseview.action?pageId=185747221)

* A SCP deve possuir movimentações exclusivas (separadas) do Sócio Ostensivo. Por exemplo: os lançamentos contábeis da SCP não podem refletir nos lançamentos do Sócio Ostensivo, sendo assim, a tabela CT2 e demais tabelas de movimento, devem ter seu compartilhamento exclusivo por filial.

[http://tdn.totvs.com/display/PROT/CTB0012\_Compartilhamento\_de\_tabelas\_SIGACTB](http://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)

* Para gerar a ECF necessário ter os cadastros abaixo no TAF

[Documentação para a geração da ECF com SCP](https://tdn.totvs.com/pages/releaseview.action?pageId=521665262)

[TAF001\_Geração da ECF com SCP](https://tdn.totvs.com/pages/releaseview.action?pageId=521996655)

**Cadastros:**

Na wizard, teremos duas escriturações separadas, somente a da SCP e somente do Sócio Ostensivo.

**Para escrituração da SCP:**

* Rotina CTBS001- Central de escrituração + ECD

Na escrituração da SCP,  informar "Tipo da ECD (SCP)"= 2- ECD SCP

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008123781/mceclip1.png)

* Na próxima tela informe que é a SCP

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007936162/mceclip2.png)

* E selecionar, através do SIGAMAT, qual filial representa o Sócio Ostensivo

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007936322/mceclip3.png)

* Ao finalizar a exportação do arquivo e gerar o arquivo TXT, no campo 18 do Registro 0000 teremos o CNPJ da SCP

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008127701/mceclip5.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008127581/mceclip4.png)

**Para escrituração do Sócio Ostensivo:**

* Através da rotina CTBA017 necessário cadastrar a SCP para gerar a ECD e a ECF

Campo Ident. SCP (CVS\_IDTSCP) informar o CNPJ da SCP.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008123241/mceclip0.png)

* Na escrituração do Sócio Ostensivo,  informar **"Tipo da ECD (SCP)"** = 1- ECD da empresa participante da SCP como sócio ostensivo.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008132981/mceclip6.png)

* Ao finalizar a exportação do arquivo e gerar o arquivo TXT, será gerado o Registro 0035 com a informação da SCP.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008134301/mceclip7.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008134441/mceclip8.png)

Saiba mais :

[DSERTAF2-11021 DT ECF - Geração Bloco Zero campo 15 - CNPJ da SCP](https://tdn.totvs.com/pages/releaseview.action?pageId=561845981)

<https://tdn.totvs.com/pages/releaseview.action?pageId=185747221>
