---
article_id: 360045221353
category: MDT - PPP
content_hash: 76877a125125cf258260ca101c984614641e34b91f8c9030070f2422250eb817
fetched_at: '2026-06-28T22:44:22.287566+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus - MDT - Qual é a origem das informações da seção I dados
  administrativo (campos cadastrais 01 ao 11) do relatório PPP
type: support-article
updated_at: '2025-03-03T12:30:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045221353-RH-Linha-Protheus-MDT-Qual-%C3%A9-a-origem-das-informa%C3%A7%C3%B5es-da-se%C3%A7%C3%A3o-I-dados-administrativo-campos-cadastrais-01-ao-11-do-relat%C3%B3rio-PPP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20008701679895)** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Qual é a origem das informações da seção I dados administrativo (campos **cadastrais** 01 ao 11) do relatório PPP?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte: **[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)**Veja abaixo a tabela com origem das informação dos campos 01 a 11 do relatório PPP.O relatório de Perfil Profissiográfico Previdenciário (rotina mdtr700) é gerado através Caminho sigamdt: atualizações > relatórios > PPP > perfil profissiogr.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Origem** | **Conteúdo** | **Parâmetros (caso exista)** |
|  | **DADOS ADMINISTRATIVOS** | | | |
| 1 | CNPJ | Dados da empresa | Configurações da filial (módulo sigacfg) |  |
| 2 | Nome Empresarial | Dados da empresa | Configurações da filial (módulo sigacfg) |  |
| 3 | CNAE | Dados da empresa | Configurações da filial (módulo sigacfg) |  |
| 4 | Nome do Trabalhador | Dados do Funcionário | Cadastro do funcionario |  |
| 5 | BR/PDH | Dados do Funcionário | Campo novo criado pelo programa RHPPP |  |
| 6 | NIT | Dados do Funcionário | Cadastro do funcionário (SRA) campo PIS |  |
| 7 | Data de Nascimento | Dados do Funcionário | Cadastro do funcionário (SRA) |  |
| 8 | Sexo | Dados do Funcionário | Cadastro do funcionário (SRA) |  |
| 9 | CTPS | Dados do Funcionário | Cadastro do funcionário (SRA) |  |
| 10 | Data de Admissão | Dados do Funcionário | Cadastro do funcionário (SRA) |  |
| 11 | Regime Revezamento | Dados do Turno | Cadastro de turno (SR6) Campo novo criado pelo programa RHPPP |  |
| **12** | **CAT REGISTRADA** | | | |
| 12.1 | Data do Registro | Dados do Acidente de Trabalhado | Acidentes (TNC) só serão considerados aqueles acidentes cujo os campos “Num CAT INSS” e “Data Emissão” estiverem preenchidos. |  |
| 12.2 | Número da CAT | Dados do Acidente de Trabalhado | Acidentes (TNC) só serão considerados aqueles acidentes cujo os campos “Num CAT INSS” e “Data Emissão” estiverem preenchidos. |  |
| **13** | **LOTAÇÃO E ATRIBUIÇÃO** | | | |
| 13.1 | Período | Dados do Funcionário | Este campo é definido pelo menor período que o funcionário trabalhou em um determinado ambiente (Setor e Função). Qualquer mudança de setor ou função causará a impressão de uma nova linha. As informações são obtidas das tabelas de Cadastro de Funcionário (SRA) Transferências (SRE) e Históricos de Função (SR7). |  |
| 13.2 | CNPJ / CEI | Dados da empresa | Obtida do módulo sigacfg com base na filial que o funcionário trabalhou na época. O programa só considera as filiais de uma mesma empresa, caso o funcionário seja transferido para outra empresa (conjunto de dicionário diferente “SX”), o usuário deverá imprimir um PPP referente a saída do funcionário da Empresa, como se este fosse demitido da empresa. |  |
| 13.3 | Setor |  | Dados do setor por onde o funcionário já trabalhou, obtido da tabela CTT, com base no código do setor da tabela de Históricos de Transferências (SRE). |  |
| 13.4 | Cargo | Dados do Cargo | O nome do cargo é obtido da tabela de cargos (SQ3). Esta informação tem origem na tabela de histórico de funções (SR7), para cada função o programa busca o cargo correspondente, conforme relacionamento feito na tabela de funções (SRJ). Pode ocorrer repetição do nome se o funcionário mudar o setor e não mudar de função. Ou mudar de função e não mudar de Cargo. | MV\_NG2INVE - Indica se deve ser trocado na impressão do PPP o conteúdo da coluna do Cargo com a coluna da Função |
| 13.5 | Função | Dados da Função | O nome da Função é obtido da tabela de Funções (SRJ). Esta informação tem origem na tabela de histórico de funções (SR7). Pode ocorrer repetição do nome se o funcionário mudar o setor e não mudar de função. | MV\_NG2INVE - Indica se deve ser trocado na impressão do PPP o conteúdo da coluna do Cargo com a coluna da Função |
| 13.6 | CBO | Dados da Função | Código do CBO, obtido da tabela de funções (SRJ). Esta informação tem origem na tabela de histórico de funções (SR7). |  |
| 13.7 | Cód. GFIP | Dados do Funcionário | Código de ocorrência da GFIP, o programa verifica por período se existe alguma informação na tabela de histórico de alterações (SR9), se não encontrar nada na tabela de histórico, lista o valor que esta no campo Ocorrência (RA\_OCORREN) no cadastro do trabalhador (SRA). |  |

**Saiba Mais**[Artigos PPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050700933)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
