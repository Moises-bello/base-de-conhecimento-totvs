---
article_id: 16983749875351
category: Suricato
content_hash: 3d5532d5ffe816ff9dfe5d6cad85a02560c596b97d6db208dbdf1876342227fb
fetched_at: '2026-06-28T22:44:57.349332+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - PON x Suricato - XML da Integração com o Suricato
type: support-article
updated_at: '2025-06-17T18:27:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16983749875351-RH-Linha-Protheus-PON-x-Suricato-XML-da-Integra%C3%A7%C3%A3o-com-o-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16983786745879) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como funciona a montagem do arquivo XML para integração do Protheus com o Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - A partir da versão 12.1.23  
  
**Solução**Nesta documentação, iremos abordar sobre como é feita a **montagem do conteúdo do XML**, no qual será enviado para o ***Web Service***. Lembrando que caso haja a necessidade de pegar o **XML** completo, com as informações do cabeçalho e etc, será necessário ativar o **parâmetro MV\_TSATLOG** com o valor **5** e verificar o arquivo gerado na pasta ***System***, conforme descrito anteriormente no tópico de Parâmetros. Neste exemplo, iremos realizar a integração da partir da rotina de **Carga Inicial** (Integração TSA - PONM430), integrando o **Centro de Custo.**  
Ao acessar a rotina de A rotina de Carga Inicial (POMM430 - Miscelânea → S.r.e.p. → Integração Tsa), quando selecionamos apenas o Centro de Custo, podemos observar que o valor da opção é 06:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877670530583)  
  
Sabendo disso, podemos localizar qual **função** irá realizar essa integração, no caso, é função **ProcP08** no fonte da **Carga Inicial** (PONM430):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877670535063)

Verificando a f**unção ProcP08**, ela está chamando **outra função**, que neste caso é a **WSRHCostCenter:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877700619031)

Procurando onde a **função WSRHCostCenter** está, descobrimos que ela está localizada no fonte **PONXFUN1**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877700619415)  
  
Aqui podemos verificar que ela faz a busca das informações dos **Centro de Custos** diretamente na **tabela:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877670542999)  
  
Após realizar a consulta na **tabela CTT**, o sistema irá enviar essas informações para o método **WSCostCenter:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877670543511)

O método **WSCostCenter**, está localizado no fonte **PTSREPOBJ:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877700621591)  
  
Antes de enviar as informações para o ***Web Service***, podemos verificar que o sistema está montando as informações do **Centro de Custo**, como a **Descrição e a Chave Externa:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877700624407)  
**Observação:**O método do ***Web Service*** chamado, foi o **insertOrUpdate.**O método **insertOrUpdate** localizado no ***Web Service*** **WebWSClient\_WSRHTSACostCenter**, está realizando a integração com o **Suricato:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877670552599)

Antes de enviar as informações da integração, conseguiremos verificar o conteúdo do **XML**, no caso as informações do **Centro de Custo,** verificando o conteúdo do objeto **oWSarg0:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877670554519)

Após todo esse processo, conseguimos verificar de fato quais informações estão sendo integradas com o **Suricato.** Este mesmo processo pode ser realizado com as demais integrações, como por exemplo as integrações de **Funcionários, Funções, Turnos e etc.** Para isso, só será necessário identificar qual é a opção selecionada e posteriormente a função desta opção. Em outros casos, como por exemplo, a integração de funcionário realizadas após a inclusão ou alteração do mesmo, precisaremos localizar no fonte de Cadastro de Funcionário, qual função ou método está sendo chamado para a integração. Por exemplo, no cadastro de funcionário, os métodos WSNatural e WSUser estão sendo chamados:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877670556311)  
  
  
**OCORRÊNCIAS NA INTEGRAÇÃO**Com a utilização do parâmetro **MV\_TSATLOG**, na qual o parâmetro permite que todas as rotinas de integração gerem um *log* de retorno com as críticas realizadas pelas regras do aplicativo, é possível saber exatamente qual foi o **erro** gerado durante o processo de integração. No exemplo que iremos mostrar, utilizamos o parâmetro com o valor igual a 5, desta maneira iremos ter o **XML** enviado e o **XML** de retorno com o código do erro ou sucesso.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877670557079)  
  
Após a inclusão do funcionário no **Protheus**, iremos visualizar o código de retorno informado no *log* gerado. Para isso, basta acessar a pasta ***System*** do **Protheus** e procurar pelo arquivo. O nome do arquivo é composto por um número sequencial, seguido de \_RCV.xml para o XML de retorno e \_SND.xml para o XML enviado. Em nosso exemplo, o nome do arquivo de retorno gerado é 55847972\_rcv.xml. Ao abrir o arquivo de retorno devemos procurar pela **Tag statusCode**, ela que conterá o código do retorno, que poderá ser de sucesso ou erro na integração. No nosso teste, o código gerado foi o 00100, isso significa que a integração funcionou corretamente.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32877670557463)  
  
  
Cada ***Web Service*** possui códigos e descrições diferentes, por isso para facilitar no entendimento dos códigos de retorno, segue abaixo a tabela de códigos de cada ***Web Service:***  
  
**Empresa**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 101 | Inclusão/Alteração da Empresa Jurídica realizada com sucesso. |
| 102 | Chave externa da Empresa Jurídica é obrigatória. |
| 103 | Deve ser informado pelo menos o CNPJ ou CEI. |
| 104 | Exclusão da unidade realizada com sucesso. |
| 105 | Deve ser informado apenas um dos campos: CNPJ ou CEI. |
| 106 | Nome da pessoa jurídica é obrigatória. |
| 107 | Pessoa jurídica está sendo usada, não é possível realizar a exclusão. |
| 100 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Unidade**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 201 | Inclusão/Alteração da unidade realizada com sucesso. |
| 202 | Chave externa da Unidade é obrigatória. |
| 203 | Chave externa de Pessoa Jurídica é obrigatória. |
| 204 | Código da unidade é obrigatório. |
| 205 | Tipo da unidade é obrigatório. |
| 206 | Exclusão da unidade realizada com sucesso. |
| 207 | Inclusão de relacionamento realizada com sucesso. |
| 208 | Exclusão de relacionamento realizada com sucesso. |
| 209 | Inclusão de relacionamento realizada parcialmente. |
| 210 | Unidade está sendo usada, não é possível realizar a exclusão. |
| 211 | Inclusão de relacionamento não realizada, nenhuma chave externa é existente. |
| 212 | Exclusão de relacionamento não realizada, nenhuma chave externa é existente. |
| 213 | Usuário ou senha são inválidos. |
| 214 | Unidade está sendo usada, não é possível realizar a exclusão. |
| 215 | Descrição da Unidade é Obrigatória. |
| 216 | Nenhum registro encontrado com a chave externa. |
| 200 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Centro de Custo**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 301 | Inclusão/Alteração do Centro de Custo realizada com sucesso. |
| 302 | Chave externa do Centro de Custo é obrigatória. |
| 303 | Exclusão da unidade realizada com sucesso. |
| 304 | Usuário ou senha são inválidos. |
| 305 | Descrição do Centro de Custo é obrigatória. |
| 306 | Centro de Custo está sendo usado, não é possível realizar a exclusão. |
| 300 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Unidade de Lotação**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 401 | Inclusão/Alteração da Unidade de Lotação realizada com sucesso. |
| 402 | Chave externa da Unidade de Lotação é obrigatória. |
| 403 | Exclusão da Unidade de Lotação realizada com sucesso. |
| 404 | Usuário ou senha são inválidos. |
| 405 | Descrição da Unidade de Lotação é obrigatória. |
| 406 | Unidade de Lotação está sendo usada, não é possível realizar a exclusão. |
| 400 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Turno**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 501 | Inclusão/Alteração do Turno realizada com sucesso. |
| 502 | Chave externa do Turno é obrigatória. |
| 503 | Data de início é obrigatória. |
| 504 | Data de início deve ser uma data válida. |
| 505 | Exclusão do Turno realizada com sucesso. |
| 506 | Pelo menos uma escala deve estar informada e deve conter pelo menos um intervalo de horário do tipo Jornada. |
| 507 | Descrição é obrigatória. |
| 509 | Turno está sendo usado, não é possível realizar a exclusão. |
| 500 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Tabela de Horário Padrão**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 601 | Inclusão/Alteração da Grade de Trabalho realizada com sucesso. |
| 602 | Chave externa da Grade de trabalho é obrigatória. |
| 603 | A chave externa do turno é obrigatória. |
| 604 | A escala deve conter pelo menos um par de horários do tipo Jornada. |
| 605 | Os pares de horários informados estão incorretos. |
| 606 | A sequência de inicio é obrigatória. |
| 607 | A sequência de término é obrigatória. |
| 608 | O tipo é obrigatório. |
| 609 | A entrada de jornada é obrigatória. |
| 610 | A saída de jornada é obrigatória. |
| 611 | A sequência de início não pode ser superior à sequência de término. |
| 612 | Exclusão do Turno realizada com sucesso. |
| 613 | Usuário ou senha são inválidos. |
| 614 | Escala está sendo usada, não é possível realizar a exclusão. |
| 600 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Funcionários**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 701 | Inclusão/Alteração da Pessoa física realizada com sucesso. |
| 702 | Chave externa da Pessoa Física é obrigatória. |
| 703 | Pelo menos o CPF ou RG deve ser informado. |
| 704 | Exclusão da pessoa física realizada com sucesso. |
| 705 | Usuário ou senha são inválidos. |
| 706 | Pessoa física está sendo usada, não é possível realizar a exclusão. |
| 700 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Localidade**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 801 | Inclusão/Alteração da Localidade realizada com sucesso. |
| 802 | Chave externa da Localidade é obrigatória. |
| 803 | Exclusão da localidade realizada com sucesso. |
| 804 | Usuário ou senha são inválidos. |
| 805 | Pelo menos País, Estado ou Cidade deve ser informada. |
| 806 | Descrição de País deve ser informada. |
| 807 | Descrição de Estado deve ser informada. |
| 808 | Descrição de Cidade deve ser informada. |
| 809 | Localidade está sendo usada, não é possível realizar a exclusão. |
| 800 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Funções**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 901 | Inclusão/Alteração do cargoNivel realizada com sucesso. |
| 902 | Chave externa do cargoNivel é obrigatória. |
| 903 | Descrição é obrigatória. |
| 904 | Exclusão do cargoNivel realizada com sucesso. |
| 905 | Usuário ou senha são inválidos. |
| 906 | CargoNivel está sendo usado, não é possível realizar a exclusão. |
| 900 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Afastamento**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 1001 | Inclusão/Alteração da situação de afastamento realizada com sucesso. |
| 1002 | Chave externa da situação de afastamento é obrigatória. |
| 1003 | Tipo da situação de afastamento é obrigatório. |
| 1004 | Exclusão da situação de afastamento realizada com sucesso. |
| 1005 | Data início e Data término são obrigatórias. |
| 1006 | Exclusão do relacionamento realizado com sucesso. |
| 1007 | Usuário ou senha estão inválidos. |
| 1008 | Descrição da situação de afastamento é obrigatória. |
| 1009 | Situação de Afastamento está sendo usada, não é possível realizar a exclusão. |
| 1010 | Inclusão do relacionamento realizado com sucesso. |
| 1000 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Exceção**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 1101 | Inclusão/Alteração da exceção realizada com sucesso. |
| 1102 | Chave externa da exceção é obrigatória. |
| 1103 | Tipo da exceção é obrigatório. |
| 1104 | Origem é obrigatório. |
| 1105 | Data início é obrigatória. |
| 1106 | Data Término é obrigatória. |
| 1112 | Exclusão da exceção realizada com sucesso. |
| 1113 | Pelo menos um período deve ser informado. |
| 1114 | Usuário ou senha inválidos. |
| 1115 | Os pares de horários informados estão incorretos. |
| 1106 | Direção é obrigatória. |
| 1100 | Erro Técnico (retornar erros ocorridos durante a execução). |

**Feriados**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 1201 | Inclusão/Alteração do dia não trabalhado realizado com sucesso. |
| 1202 | Chave externa do dia não trabalhado é obrigatória. |
| 1203 | Recorrente é obrigatório. |
| 1204 | Data é obrigatória. |
| 1205 | Exclusão do dia não trabalhado realizada com sucesso. |
| 1206 | O turno deve ser informado. |
| 1207 | A localidade deve ser informada. |
| 1208 | Usuário ou senha Inválidos. |
| 1209 | Dia não Trabalhado está sendo usado, não é possível realizar a exclusão. |
| 1200 | Erro Técnico (retornar erros ocorridos durante a execução). |
| 1210 | Inclusão do relacionamento Dia Não Trabalhado/Localidade/Turno realizado com sucesso. |
| 1211 | Exclusão do relacionamento Dia Não Trabalhado/Localidade/Turno realizado com sucesso. |

**Usuários**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 1301 | Inclusão/Alteração do usuário realizado com sucesso. |
| 1302 | Chave externa do usuário não foi informada. |
| 1303 | Chave externa de pessoa física não foi informada. |
| 1304 | O tipo papel não foi informado. |
| 1305 | Data início de validade do turno deve ser informada. |
| 1306 | Data término de validade do turno deve ser informada. |
| 1307 | Data início de validade do Centro de custo deve ser informada. |
| 1308 | Data término de validade do Centro de Custo deve ser informada. |
| 1309 | Data início de validade do CargoNivel deve ser informada. |
| 1310 | Data término de validade do CargoNivel deve ser informada. |
| 1311 | Data início de validade da Unidade de Lotação deve ser informada. |
| 1312 | Data término de validade da Unidade de Lotação deve ser informada. |
| 1313 | Data início de validade da Localidade deve ser informada. |
| 1314 | Data término de validade da Localidade deve ser informada. |
| 1315 | Chave externa de pessoa Física não existe. |
| 1316 | Chave externa de turno não existe. |
| 1317 | Chave externa de centro de custo não existe. |
| 1318 | Chave externa de CargoNivel não existe. |
| 1319 | Chave externa de unidade de lotação não existe. |
| 1320 | Chave externa de localidade não existe. |
| 1321 | Chave externa de usuário não existe. |
| 1322 | Relacionamento incluído/alterado com sucesso. |
| 1323 | Usuário ou senha Inválidos. |
| 1324 | Usuário está sendo usado, não é possível realizar a exclusão. |
| 1325 | Exclusão do usuário realizada com sucesso. |
| 1326 | Exclusão do relacionamento de usuário com nome do relacionamento, realizada com sucesso. |
| 1327 | Exclusão do relacionamento de usuário com nome do relacionamento, não realizada. |
| 1301 | Inclusão/Alteração do usuário realizado com sucesso. |
| 1302 | Chave externa do usuário não foi informada. |
| 1303 | Chave externa de pessoa física não foi informada. |
| 1300 | Erro Técnico (retornar erros ocorridos durante a execução) |

**Marcações**

|  |  |
| --- | --- |
| **Código do Retorno** | **Descrição do código de retorno** |
| 1401 | Importação da batida realizada no REP: número do rep e NSR: número do nsr foi importada com sucesso. |
| 1402 | Importação da batida realizada no REP: número do rep e NSR: número do nsr não foi importada. |
| 1400 | Erro Técnico (retornar erros ocorridos durante a execução) |

**CAMPOS DA TABELA UTILIZADA - SRA**  
Ao incluir ou alterar qualquer um dos dados utilizados para a montagem do **XML** de funcionários, será realizada uma nova integração, utilizando os **campos/*Web Services*** abaixo:

**WSRHTSANaturalPerson**<?xml version="1.0" encoding="UTF-8"?>  
-<soap:Envelope xmlns:soap="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:xsd="<http://www.w3.org/2001/XMLSchema>" xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>">  
    -<soap:Body>  
        -<insertOrUpdate xmlns="[http://naturalperson.tsa.totvs.com/](https://naturalperson.tsa.totvs.com/)">  
            -<arg0 xmlns="">  
                <address>AV. BRAZ LEME </address> Endereço + Num.Endereço + Compl.Ender. (RA\_ENDEREC + RA\_NUMENDE + RA\_COMPLEM)  
                <city>SAO PAULO </city> Municipio (RA\_MUNICIP)  
                <country>BRASILEIRO</country> Nacionalid. (RA\_NACIONA)  
                <email>totvs@[totvs.com.br](http://totvs.com.br/)</email> End. E-Mail (RA\_EMAIL)  
                <externalKey>T1D MG 01 00079820211011164347</externalKey> Código Unico RA\_CODUNIC (Empresa + RA\_FILIAL + RA\_MAT + Data e hora da Integração)  
                <federalId>03024407049</federalId> CPF (RA\_CIC)  
                <idCard>2020-01-01</idCard> R.G. (RA\_RG)  
                <idCardDate>1900-01-01</idCardDate> D t.Emis.RG (RA\_DTRGEXP) Se não for preenchido será enviado 1900-01-01  
                <idCardEmitter>SSP </idCardEmitter> Orgao expedR (RA\_RGEXP)  
                <idCardState>SP </idCardState> UF do RG (RA\_RGUF)  
                <name>Funcionário Totvs </name> Nome do Funcionário (RA\_NOME)  
                <neighborhood>CASA VERDE </neighborhood> Bairro (RA\_BAIRRO)  
                <phone1>11111111 </phone1> Telefone (RA\_TELEFON)  
                <phone2>911111111 </phone2> Num. Celular (RA\_NUMCELU)  
                <phoneCode1>11</phoneCode1> DDD Telefone (RA\_DDDFONE)  
                <phoneCode2>11</phoneCode2> DDD Celular (RA\_DDDCELU)  
                <state>SP</state> Estado (RA\_ESTADO)  
                <zipCode>02511000</zipCode> CEP (RA\_CEP)  
                <sex>M</sex> Sexo (RA\_SEXO)  
                <birthDate>1985-11-19</birthDate> Data Nasc. (RA\_NASC)  
           </arg0>  
       </insertOrUpdate>  
    </soap:Body>  
</soap:Envelope>

**WSRHTSAUserIntegration**<?xml version="1.0" encoding="UTF-8"?>  
-<soap:Envelope xmlns:soap="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:xsd="<http://www.w3.org/2001/XMLSchema>" xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>">  
    -<soap:Body>  
        -<insertUserShiftWork xmlns="[http://user.tsa.totvs.com/](https://user.tsa.totvs.com/)">  
            -<arg0 xmlns="">  
                <endDate>2049-12-31T00:00:00</endDate> Data Demissão (RA\_DEMISSA se RA\_DEMISSA estiver vazia será enviado 2049-12-31)  
                <initialDate>2021-01-01T00:00:00</initialDate> Data Admissão (RA\_ADMISSA)  
                <shiftWorkExternalKey>T1D MG 00101</shiftWorkExternalKey> Chave de identificação do turno (Empresa + Turno + Sequencia (Empresa + PF\_FILIAL + PF\_TURNOPA + PF\_SEQUEPA))  
                <userExternalKey>T1D MG 01 000798</userExternalKey> Chave de identificação do funcionário (Empresa + RA\_FILIAL + RA\_MAT)  
                <InitialScaleBaseDate>2020-12-28T00:00:00</InitialScaleBaseDate> Primeiro dia da sequência e turno informado. Por exemplo a data de admissão do funcionário foi no dia 01/01/2021, esse dia é uma sexta-feria e a sequência 01 começa na segunda, então será enviada o dia 28/12/2020.  
            </arg0>  
        </insertUserShiftWork>  
    </soap:Body>  
</soap:Envelope>

**Saiba Mais:**[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)[Integração Protheus x Suricato](https://tdn.totvs.com/pages/viewpage.action?pageId=546695095)  
[Pacote de Expedição Contínua - Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
