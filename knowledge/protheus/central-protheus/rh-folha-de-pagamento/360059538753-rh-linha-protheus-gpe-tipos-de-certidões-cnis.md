---
article_id: 360059538753
category: RH - Folha de Pagamento
content_hash: efc3a8f559074bc7c894025b0fd377e7f8358137b73e2b24f89af9b22319903c
fetched_at: '2026-06-28T22:44:17.182177+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Tipos de certidões CNIS
type: support-article
updated_at: '2025-08-12T12:35:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059538753-RH-Linha-Protheus-GPE-Tipos-de-certid%C3%B5es-CNIS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34120760704279)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Quais são os tipos de certidões conforme layout CNIS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução****CNIS** - Conforme Circular CAIXA 574 de 02/03/2012, publicada no DOU de 05/03/2012, a empresa poderá solicitar o cadastro do trabalhador em lote, mediante envio de arquivo, no formato leiaute padrão definido pela CAIXA, a partir da implantação do novo sistema de cadastramento de pessoas.

Conforme o leiaute do CNIS uma das informações necessárias para o correto envio do arquivo é a certidão civil, contendo 8 campos: (**Tipo de certidão, Data de emissão da certidão, Termo/Matrícula, Código IBGE do Município da Emissão da Certidão, UF de Emissão da Certidão, Nome do Cartório da Certidão, Livro da Certidão, Folha da Certidão**), campos que serão descritos e explicados abaixo:

**Tipo de certidão**:

**Será utilizado um código de campo para cada tipo de certidão no envio do arquivo do CNIS**

91 – Certidão de Nascimento, código de campo: **0374** – sequência 00.

92 – Certidão de Casamento, código de campo **0375** - sequência 00.

95 – Certidão Administrativa de Nascimento do Indígena, código de campo **0866** – sequência 00.

98 – Certidão de Óbito, código de campo **0376** – sequência 00.

**Preenchimento****no Protheus**: Funcionários (**GPEA010**) pasta **Documentos**, campo Data Emissão(**RA\_TIPCERT**).

**Data de Emissão da Certidão**

Data de emissão no formato **DDMMAAAA,**código de campo de acordo com o **tipo da certidão** (0374, 0375, 0866 ou 0376)  sequencia 01.

**Preenchimento no Protheus**: Funcionários (**GPEA010**) pasta **Documentos**, campo Tip.Certid.(**RA\_EMICERT**).

**Termo/Matrícula:**

Dependendo da data de emissão da certidão, este campo no CNIS poderá ter **8** ou **32** posições, para certidões emitidas até **31/12/2009** deverá ser utilizado o **termo com 8 posições**, já para as certidões emitidas a partir de **01/01/2010** será utilizada a **matrícula com 32 posições**.

Código de campo de acordo com o **tipo da certidão** (0374, 0375, 0866 ou 0376)  sequencia 02

**Preenchimento no Protheus**: Teremos 3 tipos de preenchimento possíveis:

– **Termo** (Certidões emitidas até 31/12/2009): Funcionários (**GPEA010**) pasta **Documentos**, campo Termo/Matric.(**RA\_MATCERT**) preenchido com as 8 posições referentes ao Termo.

– **Matrícula** (Certidões emitidas a partir de 01/01/2010):

a) Funcionários (**GPEA010**) pasta **Documentos**, campo Termo/Matric.(**RA\_MATCERT**) **com tamanho de 32** e  preenchido com as 32 posições referentes a Matrícula.

b) Funcionários (**GPEA010**) pasta **Documentos**, campo Termo/Matric.(**RA\_MATCERT**) que não tenha o tamanho de 32, a matrícula será formada pela junção dos seguintes campos:

6 primeiros dígitos do campo Cod. Servent (**RA\_SERVENT**) – 1º ao 6º dígitos da matrícula.

2 primeiros dígitos do campo Cod. Acervo (**RA\_CODACER**) – 7º ao 8º dígitos da matrícula.

2 primeiros dígitos do campo Reg. Civil (**RA\_REGCIVI**) – 9º ao 10º dígitos da matrícula.

4 digitos do campo (referentes ao ano AAAA) Data Emissão (**RA\_EMICERT**) – 11º ao 14º dígitos da matrícula.

1 digito do campo Tipo Livro (**RA\_TPLIVRO**) – 15º dígitos da matrícula.

5 dígitos do campo Livro (**RA\_LIVCERT**)  - 16º ao 20º dígitos da matrícula.

3 dígitos do campo Folha (**RA\_FOLCERT**) – 21º ao 23º dígitos da matrícula.

7 primeiros dígitos do campo Termo/Matric.(**RA\_MATCERT**) – 24º ao 30º dígitos da matrícula

Os 31º e 32º dígitos da matrícula serão calculados no critério de DV Módulo 11.

Ou seja, na geração do arquivo do CNIS, caso o campo Termo/Matric (**RA\_MATCERT**) esteja preenchido com a matrícula com os 32 caracteres, será utilizado este número para a matrícula, mas caso o conteúdo do campo Termo/Matric (**RA\_MATCERT**) não tenha os 32 caracteres a matrícula será formada pela junção de **8 campos** do cadastro de funcionários.

**Código IBGE do Município da Emissão da Certidão:**

Código do IBGE informado com 7 posições contém o código da UF**,**código de campo de acordo com o **tipo da certidão** (0374, 0375, 0866 ou 0376)  sequência 03.

**Preenchimento****no Protheus**: Funcionários (**GPEA010**) pasta **Documentos**, campo Cod.Mun.Cert (**RA\_CDMUCER**).

**UF de Emissão da Certidão:**

Sigla da UF com 2 posições**,**código de campo de acordo com o **tipo da certidão** (0374, 0375, 0866 ou 0376)  sequência 04.

**Preenchimento****no Protheus**: Funcionários (**GPEA010**) pasta **Documentos**, campo UF (**RA\_UFCERT**).

**Nome do Cartório da Certidão:**

Não poderá estar em branco, código de campo de acordo com o **tipo da certidão** (0374, 0375, 0866 ou 0376)  sequência 05.

**Preenchimento****no Protheus**: Funcionários (**GPEA010**) pasta **Documentos**, campo Cartório (**RA\_CARCERT**).

**Livro da Certidão:**

Obrigatório para o tipo 98 (**Certidão de Óbito**), não enviar ou enviar em branco caso a data de emissão da certidão for a partir de 01/01/2010, código de campo de acordo com o **tipo da certidão** (0374, 0375, 0866 ou 0376)  sequência 06.

**Preenchimento****no Protheus**: Funcionários (**GPEA010**) pasta **Documentos**, campo Livro (**RA\_LIVCERT**).

**Folha da Certidão:**

Obrigatório para o tipo 98 (**Certidão de Óbito**), não enviar ou enviar em branco caso a data de emissão da certidão for a partir de 01/01/2010, código de campo de acordo com o **tipo da certidão** (0374, 0375, 0866 ou 0376)  sequência 07.

**Preenchimento****no Protheus**: Funcionários (**GPEA010**) pasta **Documentos**, campo Folha (**RA\_LIVCERT**).

Importante:

Os campos Livro e Folha, só serão enviados no arquivo em caso de certidão de Óbito ou para certidões emitidas até 31/12/2009, mas em caso de certidão emitida a partir de 01/01/2010 e o campo RA\_MATCERT não esteja preenchido com os 32 dígitos da matrícula, estes 2 campos (Livro e Folha) deverão estar preenchidos, uma vez que não vão no arquivo mas serão utilizados para formar os 32 dígitos da matrícula.
