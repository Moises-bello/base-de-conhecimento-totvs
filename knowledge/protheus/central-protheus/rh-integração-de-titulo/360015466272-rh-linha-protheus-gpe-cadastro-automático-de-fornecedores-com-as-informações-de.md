---
article_id: 360015466272
category: RH - Integração de Titulo
content_hash: 4e915db5045feec359b475e5228d217766d8bcb2a87a9a25a9849629fc15aabf
fetched_at: '2026-06-28T22:43:36.164075+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro Automático de Fornecedores com as informações
  de Funcionários
type: support-article
updated_at: '2025-07-17T14:27:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015466272-RH-Linha-Protheus-GPE-Cadastro-Autom%C3%A1tico-de-Fornecedores-com-as-informa%C3%A7%C3%B5es-de-Funcion%C3%A1rios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33531179272087)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como realizar um cadastro automático de fornecedores com as informações de Funcionários (SRA)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Primeiramente no **Configurador (SIGACFG)**, acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Configure o parâmetro MV\_CADFORA:  
  
![figura2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360010642751)  
![figura3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360010642771)

**Obs: Se o parâmetro MV\_CADFORA estiver configurado como ".T.", uma vez que o fornecedor não puder ser cadastrado devido a alguma inconsistência, o título também não será gerado.**

**Atenção:**

* Para essa implementação é necessária a configuração em **Definição de Títulos** (GPEM640), no qual o campo **Agrupamento (RC0\_AGRUPA)** deve estar configurado por Funcionário e no campo  **Cod. Fornec. (RC0\_FORNEC)** deve constar o campo **RA\_MAT** ou **RA\_CIC**(caso o tamanho do campo A2\_COD esteja maior que 15) da tabela de **Cadastro de Funcionários (SRA)**;
* Caso já exista um registro com o código que foi definido no campo **Cod. Fornec. (RC0\_FORNEC)**, a rotina consultará o último código utilizado e somará mais um, garantindo assim que o código ainda não tenha sido utilizado;
* A amarração entre o funcionário e o fornecedor sempre será feita pela tabela de **Participantes (RD0)**, pelos campos **RD0\_FORNEC** e **RD0\_LOJA**, independentemente do código do fornecedor estar igual à matrícula do funcionário ou não;
* Caso já exista algum funcionário cadastrado como fornecedor deve ser feita a amarração manual na tabela RD0, nos campos RD0\_FORNEC e RD0\_LOJA, pois caso esses campos estejam em branco, será cadastrado um novo fornecedor para este participante;
* O cadastro de fornecedores possui **integração** com alguns produtos e **estando ativa** (configurada no EAI), o fornecedor será integrado automaticamente com as informações geradas pela rotina de geração de títulos (GPEM650);
* Os campos referentes ao endereço do funcionário (que foram informados no detalhamento dos campos acima) **devem estar sempre preenchidos**, mesmo não sendo obrigatórios na tabela de **Cadastro de Funcionários (SRA)** do Protheus, pois esses campos são **obrigatórios** no cadastro de fornecedores;
* A rotina apenas incluirá os fornecedores caso ainda não existam, portanto se houver alguma atualização no cadastro do funcionário na SRA e este funcionário já existir na tabela de fornecedores (SA2), deve-se atualizar também, manualmente, a tabela SA2.

Em seguida siga o procedimento abaixo: **1.**No **Gestão de Pessoal**acesse **Miscelânea / Títulos / Definição**;  
**2.**Defina os títulos conforme orientações do **Help**e do item **Descrição;  
3. Acesse Miscelânea / Títulos / Geração;  
4.**Preencha os parâmetros e clique em **OK;  
5.**A rotina de cadastro de fornecedores é chamada **de forma automática, caso o parâmetro MV\_CADFORA estiver configurado como ".T.";  
6.**Caso os funcionários **já existam na tabela de fornecedores, o cadastro não é realizado;  
7.**Caso ainda não exista o cadastro, os funcionários são cadastrados como fornecedores; **8.**Havendo integração do cadastro de fornecedores com alguma outra marca, a mensagem única é disparada e o cadastro de fornecedores é sincronizado.

As informações do cadastro de fornecedor serão preenchidas **de acordo com os campos** preenchidos na **tabela de cadastro do funcionário** (tabela SRA), conforme descrição abaixo:

- Código (A2\_COD): será preenchido com o código que for definido no campo **Cod. Fornec. (RC0\_FORNEC)** da rotina de **Definição de Títulos** (GPEM640);  
- **Loja (A2\_LOJA)**: será preenchido com o conteúdo do campo **Loja (RC0\_LOJA)** da tabela de Definição de Títulos;  
- Razão Social **(A2\_NOME)**: será preenchido com o nome do funcionário **(RA\_NOME)**;  
- Nome Fantasia **(A2\_NREDUZ)**: será preenchido com o nome do funcionário **(RA\_NOME)**;  
- Endereço **(A2\_END)**: será preenchido com o endereço do funcionário **(RA\_ENDEREC)**;  
- Estado **(A2\_EST)**: será preenchido com o Estado de residência do funcionário **(RA\_ESTADO)**;  
- Município **(A2\_MUN)**: será preenchido com o município de residência do funcionário **(RA\_MUNICIP)**;  
- Tipo de fornecedor **(A2\_TIPO)**: será preenchido com o conteúdo "F", representando "Pessoa Física";  
- CPF do funcionário **(A2\_CGC)**: será preenchido com o CPF do funcionário **(RA\_CIC)**;  
- Bairro do funcionário **(A2\_BAIRRO)**: será preenchido com o bairro do funcionário **(RA\_BAIRRO).**

**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
