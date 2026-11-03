---
article_id: 4409142410263
category: RH - MANAD
content_hash: e7dade59779c9f179163dbf2b83349f7764c18ffe4912c5fad567af9b4bbae85
fetched_at: '2026-06-28T22:43:33.760337+00:00'
product: protheus
section_id: 360008157193
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar o arquivo MANAD
type: support-article
updated_at: '2025-09-19T22:01:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409142410263-RH-Linha-Protheus-GPE-Como-gerar-o-arquivo-MANAD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17375187831063) Tempo aproximado para leitura: **00:07:00 min****Dúvida**Como gerar o arquivo MANAD?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**1) Para geração do arquivo MANAD, execute a **Contabilização Manad** toda vez que for gerar um período para o Manad que ainda não foi gerado. É imprescindível que o cadastro de verbas esteja com Lançamento padrão cadastrado para geração do arquivo MANAD.  
  
Acesse: **Miscelânea > Fechamentos > Contabilização MANAD;**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11440075710231)

2) No ambiente **Livros Fiscais**, em **Miscelânea > Arq. Magnéticos > Instruções Normativas (MATA950),** configure os parâmetros da rotina, conforme instruções a seguir:  
  
![](https://tdn.totvs.com/download/attachments/283389390/image2017-6-29%2015%3A5%3A3.png?version=1&modificationDate=1498760940000&api=v2)

![](https://tdn.totvs.com/download/attachments/283389390/image2017-6-29%2015%3A5%3A49.png?version=1&modificationDate=1498760940000&api=v2)  
  
3) Para a correta geração, é necessário utilizar os parâmetros da seguinte forma;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13117998799767)  
  
**Data Inicial ?**Informe a data inicial para processamento da Instrução Normativa.

**Data Final ?**  
Informe a data final para processamento da Instrução Normativa.

**Instr. Normativa ?**  
Informe o nome do arquivo de configuração, sem extensão “.INI”. Informe, neste caso, MANAD. Na validação do campo Instrução Normativa, é necessário buscar o arquivo MANAD.INI atualizado na pasta System e confirmar.   
  
**OBS: Para que consiga selecionar o arquivo MANAD no campo Instr. Normativa, deve existir o arquivo de configuração - MANAD.INI na pasta system do Protheus.**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409153469463)

**Arq. Destino ?**  
Informe o nome do arquivo em que serão geradas as informações.

**Diretório ?**  
Informe o nome do diretório em que será gravado o arquivo texto gerado.

4. Após a confirmação dos parâmetros genéricos da Instrução Normativa, serão apresentados os parâmetros específicos do Manad;

![](https://tdn.totvs.com/download/attachments/283389390/image2017-6-29%2015%3A8%3A47.png?version=1&modificationDate=1498760940000&api=v2)

 

Passo 1/7 – Identificação do Estabelecimento do Contribuinte  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409142164759)

Observação para as filiais:  
As perguntas “Filiais de/até” devem ser informadas respeitando a pergunta “Centralização de Escrituração”, ou seja:

* Para o estabelecimento centralizador, devem ser preenchidas, no Assistente da Rotina, as perguntas de “filiais de/até” abrangendo as filiais que estão sendo centralizadas, e, para este caso, as perguntas de CEI, NIT e IM contidas no assistente só servirão como padrão se não possuírem os parâmetros MV\_CEI, MV\_NIT e MV\_INSCRIM, descritos anteriormente.
* Para estabelecimentos centralizados, devem ser preenchidas, no Assistente da Rotina, as perguntas “filiais de/até” com a mesma filial indicando qual o estabelecimento que centraliza suas informações.

**Inscrição Cadastro Específico INSS**  
Informe o número da inscrição do contribuinte no INSS.

**Inscrição PIS/Pasep/CI/SUS**Informe o número da inscrição do contribuinte no PIS, Pasep, CI ou SUS, de acordo com o enquadramento da empresa.

**Inscrição Municipal**  
Informe o número da Inscrição Municipal do contribuinte.

**Inscrição na Suframa**  
Informe o número da inscrição no Suframa do contribuinte, se houver.

**Versão do Layout**  
Informe qual o layout gerado, sendo:  
01-Portaria n.63/2004  
02-Portaria n.58/2005  
03-IN MPS/SRP n.12/2006

**Centralização de Escrituração**  
Informe se o estabelecimento centraliza a entrega de informações, sendo:  
0-Sem Centralização (estabelecimento sem centralização de escrituração)  
1-Centralizador (estabelecimento centralizador de escrituração)  
2-Centralizado (estabelecimento com escrituração centralizada)

**Finalidade do Arquivo**  
Informe a finalidade do arquivo a ser apresentado, sendo:  
61-Solicitação do Auditor-Fiscal através de MPF  
62-Movimento anual de Órgão Público, conf. intimação  
90-Dados Internos UF

Passo 2/7 – Dados do Contabilista

![](https://tdn.totvs.com/download/attachments/283389390/image2017-6-29%2015%3A17%3A19.png?version=1&modificationDate=1498760940000&api=v2)

**Indicador de Movimento**  
Informe se estas informações deverão ser apresentadas, sendo:  
0-Com movimento  
1-Sem movimento

**Nome do contabilista/escritório**  
Informe o nome do contabilista ou escritório responsável pelo estabelecimento.

**CNPJ do escritório**  
Informe o número da inscrição no CNPJ do escritório de contabilidade responsável pelo estabelecimento.

**CPF do contabilista**  
Informe o número do CPF do contabilista responsável pelo estabelecimento.

**CRC do contabilista**  
Informe o número do CRC (Conselho Regional de Contabilidade) do contabilista responsável pelo estabelecimento.

**Data início prestação serviço**  
Informe a data de início da prestação do serviço de contabilidade.

**Data final prestação serviço**  
Informe a data de término da prestação do serviço de contabilidade.

**Informações sobre o endereço:**

**CEP**  
Informe o CEP do endereço do contabilista ou escritório de contabilidade responsável pelo  
estabelecimento.  
**Endereço**  
Informe o endereço do contabilista ou escritório de contabilidade responsável pelo  
estabelecimento.  
**Número**  
Informe o número do endereço do contabilista ou escritório de contabilidade responsável pelo  
estabelecimento.  
**Complemento**  
Informe o complemento do endereço do contabilista ou escritório de contabilidade responsável  
pelo estabelecimento.  
**Bairro**  
Informe o bairro do endereço do contabilista ou escritório de contabilidade responsável pelo  
estabelecimento.  
**Cep caixa postal**  
Informe o CEP da caixa postal do contabilista ou escritório de contabilidade responsável pelo  
estabelecimento.  
**Caixa postal**  
Informe a caixa postal do contabilista ou escritório de contabilidade responsável pelo  
estabelecimento.

**Telefone**  
Informe o telefone do contabilista ou escritório de contabilidade responsável pelo  
estabelecimento.  
**FAX**  
Informe o FAX do contabilista ou escritório de contabilidade responsável pelo estabelecimento.  
**E-mail**  
Informe o e-mail do contabilista ou escritório de contabilidade responsável pelo  
estabelecimento. 

Passo 3/7 – Dados do técnico/empresa responsável pela geração do arquivo digital

![](https://tdn.totvs.com/download/attachments/283389390/image2017-6-29%2015%3A20%3A41.png?version=1&modificationDate=1498760940000&api=v2)

**Data início prestação serviço**  
Informe a data de início do fornecimento do sistema de geração dos arquivos digitais (início do contrato com a Protheus).

**Data final prestação serviço**  
Informe a data de término do fornecimento do sistema de geração dos arquivos digitais. 

Passo 4/7 – Identificação da escritura contábil

![](https://tdn.totvs.com/download/attachments/283389390/image2017-6-29%2015%3A21%3A50.png?version=1&modificationDate=1498760940000&api=v2)

**Indicador de Movimento**  
Informe se essas informações deverão ser apresentadas, sendo:  
0-Com movimento  
1-Sem movimento

**Indicador de tipo de escrituração**  
Informe o tipo de escrituração contábil do estabelecimento, sendo:  
G-Diário geral  
A-Diário/Razão auxiliar

**Nº Cta. Analítica diário do geral**  
Informe o código da conta analítica do Diário Geral que recebe os lançamentos globais.

**Data da apuração de resultado**  
Informe a data em que é efetuada a apuração dos resultados do estabelecimento.  
Ex. 31/12/2017 se a geração do arquivo se referir ao ano calendário de 2017.

**Conta(s) analítica(s) de resultado**  
Informe o(s) código(s) da(s) conta(s) analítica(s) de resultado. Podem ser digitadas varias contas (separadas por ponto e vírgula) e/ou intervalos (separados por dois pontos sucessivos).  
Exemplo:  
Para as contas “11010101;13080202;11050101..11050199”, as contas de resultado serão a 11010101, a 13080202 e todas as contas entre 11050101 e 11050199.

Passo: 5/7 - Informação da Previdência Social

![](https://tdn.totvs.com/download/attachments/283389390/image2017-6-29%2015%3A23%3A34.png?version=1&modificationDate=1498760940000&api=v2)

**Indicador de Movimento**  
Informe se essas informações deverão ser apresentadas, sendo:  
0-Com movimento  
1-Sem movimento

Passo: 6/7 - Sistema Financeiro e orçamentário dos Órgãos Públicos

![](https://tdn.totvs.com/download/attachments/283389390/image2017-6-29%2015%3A24%3A18.png?version=1&modificationDate=1498760940000&api=v2)

**Indicador de Movimento**  
Informe se essas informações deverão ser apresentadas, sendo:  
0-Com movimento  
1-Sem movimento

**Tipo de Empresa**  
Informe o tipo da empresa, que pode ser:  
0-Geral  
1-Órgãos Públicos  
  
Observação:  
Quando a opção do tipo de empresa escolhida for “0-Geral”, não serão gerados os arquivos de Registro tipo L00X – (Registros de natureza financeira e orçamentária) e quando a opção escolhida for: “1-Órgãos Públicos”, não serão gerados os arquivos de Registro tipo I00X – (Lançamentos Contábeis), conforme definido no manual disponível no site da Previdência Social.

Passo: 7/7 - Dados do técnico/empresa responsável pela geração do arquivo digital

![](https://tdn.totvs.com/download/attachments/283389390/image2017-6-29%2015%3A25%3A36.png?version=1&modificationDate=1498760940000&api=v2)

 

**Técnico/Responsável**  
Informe o nome do técnico/responsável pelas informações prestadas.

**Cargo**  
Informa o cargo do técnico/responsável pelas informações prestadas.

**CNPJ**  
Informe o CNPJ do técnico/responsável pelas informações prestadas.

**CPF**  
Informe o CPF do técnico/responsável pelas informações prestadas.

**Fone**  
Informe o telefone do técnico/responsável pelas informações prestadas.

**FAX**  
Informe o número do FAX do técnico/responsável pelas informações prestadas.

**E-Mail**  
Informe o e-mail do técnico/responsável pelas informações prestadas.

9. Confira os dados e clique no botão “Finalizar”.

O sistema vai popular a tabela RCZ e gerar o arquivo magnético na pasta especifica no item 3.

**IMPORTANTE:**

Anexo arquivo MANAD.INI (27/02/2024). Sempre validar com nosso time de suporte se há arquivo MANAD.INI mais atualizado no momento da geração. 

Saiba Mais:  
[Página Centralizadora do MANAD](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360008157193-RH-MANAD)
