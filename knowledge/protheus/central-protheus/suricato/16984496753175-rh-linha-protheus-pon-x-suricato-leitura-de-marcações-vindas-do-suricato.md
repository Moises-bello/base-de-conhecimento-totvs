---
article_id: 16984496753175
category: Suricato
content_hash: a2d8ac86140a70f9dc2055904e59431805d1761c2c2099513a4e6471c8ac715a
fetched_at: '2026-06-28T22:44:57.429295+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - PON x Suricato - Leitura de Marcações vindas do Suricato
type: support-article
updated_at: '2024-11-12T19:15:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16984496753175-RH-Linha-Protheus-PON-x-Suricato-Leitura-de-Marca%C3%A7%C3%B5es-vindas-do-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16984485600407) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como funciona a leitura de marcações vindas do Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - A partir da versão 12.1.23  
  
**Solução**Para efetuar a **leitura de marcações** a partir do **Suricato**, deve-se incluir um cadastro do relógio e informar o conteúdo “R” no campo Tipo Arquivo (P0\_TIPOARQ). Ao iniciar o processo de leitura de marcações, a rotina irá buscar os registros da tabela MSA\_CONTROL\_MARCAC ou RR1 de determinada data de/até, que contém o campo LOG\_IMPORT\_PRODUT = 0.

Para que as marcações salvas na MSA/RR1 sejam processadas corretamente, o código do REP, no cadastro do Protheus, deverá ser o mesmo código salvo no campo COD\_REP na tabela MSA/RR1. Por exemplo, se o Suricato salvar o código 5001030033938 no campo COD\_REP da MSA, o campo REP do cadastro de relógio do Protheus deverá ser salvo com o conteúdo 5001030033938.  
  
Com a portaria 671 é necessário informar o tipo do REP (1510, REP-A, REP-C e REP-P). Para um relógio do Suricato teremos apenas duas opções: 1510 ou REP-C. É necessário verificar qual o tipo do REP do Suricato e preencher corretamente o cadastro do relógio, para que a leitura seja feita através do PIS ou CPF do funcionário.  
  
Exemplo de configuração dos campos no **Cadastro de Relógio** para integração de marcações do **Suricato**:  
Para leitura por PIS:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27745685071767)  
Para leitura por CPF:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27745685079191)  
  
**PORTARIA 671**Com a **portaria 671/2021**, surgiu a necessidade de realizar duas alterações no **Protheus** para que o sistema consiga realizar corretamente a integração de **marcações** vindas do **Suricato.**  
A primeira alteração foi a estrutura das tabelas **MSA\_CONTROL\_MARCAC/RR1**, que armazenam as marcações.  
A segunda alteração foi a **API*****recordClockMarkings**,*ela foi atualizada para receber os novos campos da Portaria 671/2021. A utilização da **API *recordClockMarkings***é apenas para as marcações serem integradas na **RR1**. Caso a integração das marcações seja feita via **banco de dados** utilizando a **MSA\_CONTROL\_MARCAC**, o processo **continuará o mesmo**, porém, será necessária  a criação dos novos campos.

**CAMPOS DA TABELA RR1/MSA\_CONTROL\_MARCAC**Se a tabela utilizada for a **MSA\_CONTROL\_MARCAC**, será necessária a atualização do ambiente com o pacote de **expedição contínua Acumulado de RH** e a execução do **UPPDISTR**. Após a execução do pacote de dicionários, será criada a pergunta **Atualiza Tabela MSA?** na rotina de **Carga Inicial** (PONM430). Esta pergunta será responsável para dizer se o sistema deve ou não atualizar a **MSA\_CONTROL\_MARCAC** com os novos campos. A pergunta terá apenas **duas respostas**, sendo: **1 - Sim** e **2 - Não**, caso seja preenchida com **1 - Sim**, o sistema irá criar o novos campos da MSA\_CONTROL\_MARCAC, caso ela esteja preenchida com não, o sistema não irá atualizar a tabela.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **X1\_GRUPO** | **X1\_ORDEM** | **X1\_PERGUNT** | **X1\_TIPO** | **X1\_TAMANHO** | **X1\_VAR01** | **X1\_DEF01** | **X1\_DEF02** | **X1\_HELP** |
| PONM430 | 4 | "Atualiza Tabela MSA"? | N | 1 | MV\_PAR04 | 1 - Sim | 2 - Nao | .PONM43004. |

Com a pergunta preenchida com **Sim**, as demais perguntas podem ficar em branco e o sistema irá desconsiderar as demais perguntas, fazendo assim com que a execução da rotina seja **exclusivamente**para a **criação** dos **novos campos** na **MSA\_CONTROL\_MARCAC.**  
Caso a tabela **MSA\_CONTROL\_MARCAC** **já**exista no banco de dados, ao executar a rotina de **Carga Inicial** (PONM430) preenchendo apenas a pergunta **Atualiza Tabela MSA?** com **Sim**, será realizada a criação dos novos campos.  
  
Caso a tabela **MSA\_CONTROL\_MARCAC** **não**exista no banco de dados, ao executar a rotina de **Carga Inicial** (PONM430), preenchendo apenas a pergunta **Atualiza Tabela MSA?** com **Sim**, será realizada a criação da tabela com os novos campos.

Após a execução da rotina, os novos campos serão criados:

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Tipo** | **Tamanho** |
| COD\_FUSO | varchar | 5 |
| COD\_CPF\_FUNC | varchar | 11 |
| NUM\_VERS\_LAYOUT\_AFD | int | 3 |
| COD\_INSCR\_EMP | varchar | 14 |

As **marcações** são gravadas na tabela **MSA\_CONTROL\_MARCAC** conforme exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16985799230231)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16985791232791)  
  
  
Caso a tabela responsável por armazenar as marcações seja a **RR1**, será necessária a atualização do ambiente com o pacote **de expedição contínua Acumulado de RH** e a execução do **UPPDISTR.**  
Após a execução do **UPPDISTR,** os seguintes campos serão criados na tabela **RR1**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **X3\_CAMPO** | **X3\_TIPO** | **X3\_TAMANHO** | **X3\_TITULO** | **X3\_DESCRIC** |
| RR1\_FUSO | C | 5 | Fuso Horário | Fuso horário da marcação |
| RR1\_CODCPF | C | 11 | CPF | CPF do funcionário |
| RR1\_VRSLAY | N | 3 | Vers. Layout | Versão do Layout |
| RR1\_INSCR | C | 14 | Inscr. Emp | CNPJ ou CPF do empregador |

 

**Observação:** O **Suricato não grava o horário da marcação em horas e minutos** no campo **NUM\_HORAR\_MARCAC\_ACES** das tabelas MSA\_CONTROL\_MARCAC/RR1. É necessário **converter** o conteúdo para horas e minutos efetuando a seguinte conta:  
**- NUM\_HORAR\_MARCAC\_ACES / 3600** para encontrar as **horas**;  
- **Resto da divisão X 60** para encontrar os **minutos**;  
- **Resto da divisão X 60** para encontrar os **segundos**.  
Exemplo: NUM\_HORAR\_MARCAC\_ACES = 59730:  
59730 / 3600 = 16,59166666666667;  
0,59166666666667 X 60 = 35,5;  
0,5 X 60 = 30.  
Resultado: 16:35:30.  
  
As **marcações** são gravadas na tabela RR1 desta forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16985486871959)  
  
Cabe ressaltar que as **marcações** são gravadas nas tabelas **após envio por parte do Suricato.**

**ALTERAÇÃO DA API RECORDCLOCKMARKINGS**A **API*****recordClockMarkings**,* foi alterada para receber, validar e salvar os dados nos novos campos da **RR1**. Se as marcações a serem integradas forem referentes a **Portaria 671**, antes de consumir a **API** será necessário validar se os novos campos, mencionados anteriormente, já foram criados no **Protheus**. Para isso foi criada uma nova **API** que irá dizer para o **Suricato** se o **Protheus** já possui os novos campos e se poderá ser utilizado os mesmo na **API *RecordclockMarkings*.**

**RECORDVALIDATEDVERSION**A **API *RecordValidatedVersion***irá verificar no sistema se os novos campos foram criados, respeitando o conteúdo do parâmetro **MV\_APISUR.** Se o parâmetro **MV\_APISUR** estiver configurado com **.T.** (integração via API) o sistema irá verificar a tabela **RR1**, nos casos onde o parâmetro estiver com **.F.** será verificada a tabela **MSA\_CONTROL\_MARCAC.**Para mais informações sobre a **API**, acesse o link abaixo:  
[DT API recordValidatedVersion](https://tdn.totvs.com/display/PROT/DT+API+recordValidatedVersion).

Após validar se o sistema possui os novos campos, bastar utilizar a **API *RecordclockMarkings*,** informando os novos campos como o exemplo abaixo:

```
{
    "items": [
                {
                    "codRelogioExtChave": "",
                    "codFuncMsa": "003651",
                    "codNsr": 1,
                    "codPisMsa": "022036983234",
                    "datMarcacAces": "2022-11-01 09:00:00.000",
                    "numHorarMarcacAces": 32400,
                    "codRep": "00000000000000123",
                    "codUnidExtChave": "T1D MG 01",
                    "codUsuarExtChave": "T1D MG 01 003651",
                    "codFuso": "-0300",
                    "codCPF": "16046091098",
                    "numVersLayout": 3,
                    "inscrEmp": "11456156000111"
                }
        ]
}
```

**CONFIGURAÇÃO DO SCHEDULE**Após o **cadastro do relógio**, é possível realizar a configuração do ***Schedule*** para que a rotina de **Leitura e Apontamento** seja executada de tempos em tempos, desta maneira, todas as marcações que foram integradas serão processadas pelo **Protheus.** O processo também pode ser realizado de forma **manual,** para isso acesse a rotina de Leitura Apontamento em **SIGAPON → Miscelanea → Cálculos → Leitura/Apontamento Marcações**, preencha os parâmetros informando o código do relógio cadastrado anteriormente e execute a rotina.  
  
Para a configuração do ***Schedule*** siga a documentação:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052033373-RH-Linha-Protheus-PON-Como-configurar-o-Schedule-de-Leitura-Apontamento>

**Saiba Mais:**[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[https://tdn.totvs.com/pages/releaseview.action?pageId=546695095Integração Protheus x Suricato](https://tdn.totvs.com/pages/releaseview.action?pageId=546695095)  
[Schedule - Leitura/Apontamento das Marcações](https://tdn.totvs.com/pages/releaseview.action?pageId=631321258)  
[Pacote de Expedição Contínua - Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
