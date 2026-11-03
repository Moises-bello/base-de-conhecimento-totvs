---
article_id: 360061914754
category: RH - Relatórios Cadastros/Funcionários
content_hash: 0b18ebab336008bf7dbbe5e8159a6fbed4e99acd2ba6185ff3488368db56b832
fetched_at: '2026-06-28T22:43:18.561634+00:00'
product: protheus
section_id: 360010843654
source: central-protheus
title: RH - Linha Protheus - GPE - Histórico de Médias (GPER080)
type: support-article
updated_at: '2025-10-02T17:41:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061914754-RH-Linha-Protheus-GPE-Hist%C3%B3rico-de-M%C3%A9dias-GPER080
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35362643387287)** Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Alteração do relatório de Demonstrativo de Médias, agora os cálculos de médias serão salvos em uma nova tabela, **mantendo assim um histórico**. Casos existam **cálculos já efetuados**, o sistema irá buscar as informações que estarão salvas na tabela **RJK**, caso contrário, terá que **efetuar os cálculos para salvar as médias e gravar** essas informações na nova tabela **RJK**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.27  
  
**Solução**Acesse o Relatório de Médias através do caminho Relatórios > Lançamentos > **Demonstrativo de Médias (GPER080)**

**1. Novas linhas totalizadoras**

\* BASE MEDIA ATS = Base ATS para 13 de Comissionado/professores  
\*\*\* TOT INSALUB = Total de insalubridade sobre médias  
\*\*\* TOT PERICUL = Total de periculosidade sobre médias  
\*\*\* TOT DSR = Total de DSR sobre media, soma-se ao valor \*\*MEDIA para poder realizar o pagamento  
\*\*\* TOT DSRHATIV = Total de DSR sobre horas atividade, soma-se ao valor \*\*MEDIA para poder realizar o pagamento  
  
![exemplo.png](https://tdn.totvs.com/download/attachments/519190688/exemplo.png?version=1&modificationDate=1571776021977&api=v2)

**2. Novo cabeçalho**

Agora no cabeçalho são demostrados além do salário mensal, salário dia e salário hora o salário incorporado e os adicionais Periculosidade, Insalubridade, Tempo de Serviço Confiança, Transferência.  
  
![](https://tdn.totvs.com/download/attachments/519190688/image2019-11-1_13-56-52.png?version=1&modificationDate=1572627413043&api=v2)

**3. Página de Parâmetros**

Ao emitir o relatório ser perguntado se deseja imprimir a página de parâmetros, nela são impressos os **mnemônicos** utilizados no cálculo e a data dos principais **fontes envolvidos.**  
  
![](https://tdn.totvs.com/download/attachments/519190688/image2019-11-1_13-58-42.png?version=1&modificationDate=1572627522097&api=v2)

**4. Histórico de relatório de médias**

Como agora os dados são gravados em diversas telas **será possível consultar o relatório de médias**, desde que ele tenha sido **gerado no novo modelo**, por exemplo ao ter uma rescisão normal e uma complementar, teremos 2 relatórios de médias e é possível consultar ambos pelo menu visualizar médias. Com os valores de parâmetros e verbas utilizados na época do cálculo.

Essa opção está disponível nas **rotinas** de Rescisão, Férias, Provisão, Recibo de pagamento e Consulta de cálculo.  
  
![](https://tdn.totvs.com/download/attachments/519190688/image2019-11-1_14-4-33.png?version=1&modificationDate=1572627873590&api=v2)  
  
**5.****Tabelas Utilizadas  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102373334)**

**6. Principais Campos e Parâmetros**

Tabela RJK (Histórico de Médias)

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Campo** | **Descrição** | **Nome** | **Tipo** | **Tamanho** | **Decimal** | **Picture** | **Contexto** | **Obrigatório** | **Usado** | **Módulos** |
| **RJK\_FILIAL** | Código da Filial | Filial | Caractere | 8 | 0 |  | Real | Não | Não |  |
| **RJK\_PROCES** | Código Processo | Processo | Caractere | 5 | 0 | @! | Real | Sim | Sim | Todos |
| **RJK\_MAT** | Número da Matrícula | Matricula | Caractere | 6 | 0 | 999999 | Real | Sim | Sim | Todos |
| **RJK\_PERIOD** | Período de Cálculo | Cod. Periodo | Caractere | 6 | 0 | @! | Real | Sim | Sim | Todos |
| **RJK\_SEMANA** | Semana | Semana | Caractere | 2 | 0 | 99 | Real | Sim | Sim | Todos |
| **RJK\_ROTEIR** | Roteiro Cálculo | Roteiro Calc | Caractere | 3 | 0 | @! | Real | Sim | Sim | Todos |
| **RJK\_DTREF** | Data Referência Cálculo | Data Ref. | Data | 8 | 0 |  | Real | Sim | Sim | Todos |
| **RJK\_DISSI** | Dissídio | Dissidio | Caractere | 1 | 0 | @! | Real | Sim | Sim | Todos |
| **RJK\_ID** | Id Cabeçalho Histórico Média | Id. Hist. Md | Caractere | 12 | 0 |  | Real | Não | Sim | Todos |
| **RJK\_CC** | Centro de Custo | C. Custo | Caractere | 9 | 0 | @! | Real | Não | Sim | Todos |
| **RJK\_ITEM** | Item Contábil | Item | Caractere | 9 | 0 | @! | Real | Não | Sim | Todos |
| **RJK\_CLVL** | Classe de Valor | Classe Valor | Caractere | 9 | 0 | @! | Real | Não | Sim | Todos |
| **RJK\_BASFER** | Base de Férias | Base Fer | Data | 8 | 0 |  | Real | Não | Sim | Todos |
| **RJK\_EMISSA** | Data Emissão | Data Emissao | Data | 8 | 0 |  | Real | Não | Sim | Todos |
| **RJK\_CODFUN** | Código da Função | Funcao | Caractere | 5 | 0 | @! | Real | Não | Sim | Todos |
| **RJK\_ADMISS** | Data de Admissão | Data Admis. | Data | 8 | 0 |  | Real | Não | Sim | Todos |
| **RJK\_SALBAS** | Salário do Funcionário | Salario | Numérico | 12 | 2 | @E 999,999,999.99 | Real | Não | Sim | Todos |
| **RJK\_SALINC** | Salário Incorporado | Sal. Incorp. | Numérico | 12 | 2 | @E 999,999,999.99 | Real | Não | Sim | Todos |
| **RJK\_SALMES** | Salário no mês | Salario Mes | Numérico | 12 | 2 | @E 999,999,999.99 | Real | Não | Sim | Todos |
| **RJK\_SALDIA** | Salário dia | Salario Dia | Numérico | 12 | 2 | @E 999,999,999.99 | Real | Não | Sim | Todos |
| **RJK\_SALHOR** | Valor salário hora | Salario Hora | Numérico | 12 | 2 | @E 999,999,999.99 | Real | Não | Sim | Todos |
| **RJK\_PERIC** | Adicional Periculosidade | Adc Pericul. | Numérico | 12 | 2 | @E 999,999,999.99 | Real | Não | Sim | Todos |
| **RJK\_INSAL** | Adicional Insalubridade | Adc. Insalub | Numérico | 12 | 2 | @E 999,999,999.99 | Real | Não | Sim | Todos |
| **RJK\_CONF** | Adicional Cargo de confiança | Adc. Confia. | Numérico | 12 | 2 | @E 999,999,999.99 | Real | Não | Sim | Todos |
| **RJK\_TRANSF** | Adicional de transferência | Adc. Transf. | Numérico | 12 | 2 | @E 999,999,999.99 | Real | Não | Sim | Todos |
| **RJK\_ATS** | Adicional Tempo de serviço | Adic. ATS | Numérico | 12 | 2 | @E 999,999,999.99 | Real | Não | Sim | Todos |
| **RJK\_MNEMO1** | Mnemonicos utilizados | Mnemonicos 1 | Mnemonico | 255 | 0 |  | Real | Não | Sim | Todos |
| **RJK\_MNEMO2** | Mnemonicos utilizados | Mnemonicos2 | Mnemonico | 255 | 0 |  | Real | Não | Sim | Todos |

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| 1 | RJK\_FILIAL+RJK\_PROCES+RJK\_MAT+RJK\_PERIOD+RJK\_SEMANA+RJK\_ROTEIR+DTOS(RJK\_DTREF)+RJK\_DISSI |

**Tabela SRP (Demonstrativo de Médias), inclusão do campo RP\_ID**

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Campo | Descrição | Nome | Tipo | Tamanho | Decimal | Picture | Contexto | Obrigatório | Usado | Módulos |
| RP\_ID | Id Cabeçalho Histórico Média | Id. Hist. Md | Caractere | 12 | 0 | @! | Real | Não | Sim |  |

**Saiba Mais**  
[Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=519190688)   
[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgKFbLUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ8aHR0cHM6Ly9jZW50cmFsZGVhdGVuZGltZW50by50b3R2cy5jb20vaGMvcHQtYnIvYXJ0aWNsZXMvMzYwMDUwNzI2MTU0LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZGUtbSVDMyVBOWRpYXMGOwhUOg5zZWFyY2hfaWRJIik1M2JjNDQ4Mi0xZTU0LTQ3MTYtYWJhNy01Y2QxYjg0ZDY1NjcGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhjw6FsY3VsbyBkZSBtw6lkaWFzBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--cbb28a0877b3f7ce647878c32dbd2838b92ccf23)  
[RH - Linha Protheus - GPE - Coluna Valor Original e Valor Atual Demonstrativo de Médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024606114-RH-Linha-Protheus-GPE-Coluna-Valor-Original-e-Valor-Atual-Demonstrativo-de-M%C3%A9dias)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de Médias para Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726351592855-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-M%C3%A9dias-para-F%C3%A9rias)
