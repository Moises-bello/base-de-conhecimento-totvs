---
content_hash: c03ec9da8e5f264433d2330b2ae5493e892fa2906d69fe1c5cb17f05fe9bafb6
fetched_at: '2026-06-29T00:11:11.613418+00:00'
page_id: '648045494'
product: rm
source: tdn-rm
title: Layout de importação - CIH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=648045494
version: 5
---

O sistema TOTVS CIH funciona a partir de informações alimentadas do ERP do Cliente, estas devem ser importadas. Este documento possibilita a construção de Integração do programa TOTVS CIH com ERP do cliente através de views.

Painel Internação e Alta

**Internação e Alta**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV**\_**InterAlta | | | | | | |
| **Campo na View** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | I | Linha com dados do paciente, internação e alta |
| **COLIGADA** | Código da coligada | Número inteiro |  |  | Sim |  |  |
| **PRONTUARIO** | Prontuário | Texto | 9 |  | Sim |  |  |
| **NOMEPACIENTE** | Nome do paciente | Texto | 50 |  | Sim |  |  |
| **DATANASCIMENTO** | Data de nascimento | Data | 10 | dd/mm/aaaa | Não |  |  |
| **DATAADMISSAO** | Data de internação | Data | 10 | dd/mm/aaaa | Sim |  |  |
| **HORAADMISSAO** | Hora da internação | Texto | 4 | hhmm | Não |  |  |
| **SEXO** | Sexo | Texto | 1 |  | Não | M (Masculino) F (Feminino) |  |
| **PESO** | Peso | Número inteiro |  |  | Não |  | Apenas para recém-nascidos (peso do nascimento) |
| **ENDERECO** | Endereço | Texto | 40 |  | Não |  | Rua, número e complemento |
| **BAIRRO** | Bairro | Texto | 20 |  | Não |  |  |
| **CIDADE** | Cidade | Texto | 25 |  | Não |  |  |
| **TELEFONE** | Telefone | Texto | 14 |  | Não |  |  |
| **CEP** | CEP | Texto | 10 |  | Não |  |  |
| **CODCONVENIO** | Código do convênio | Texto | 50 |  | Não |  |  |
| **CODCLINICA** | Código da unidade clínica | Texto | 50 |  | Sim |  | Área física da internação |
| **CODLEITO** | Código do leito | Texto | 50 |  | Não |  |  |
| **CODESPECIALIDADE** | Código da especialidade | Texto | 50 |  | Sim |  | Especialidade para qual o paciente internou |
| **EMAIL** | E-mail do paciente | Texto | 40 |  | Não |  |  |
| **DATAALTA** | Data da alta | Data | 10 | dd/mm/aaaa | Não |  |  |
| **HORAALTA** | Hora da alta | Texto | 4 | hhmm | Não |  |  |
| **TIPOALTA** | Tipo de alta | Texto | 1 |  | Não | A (Domicílio) O (Óbito) T (Transferência) |  |
| **NOMEMAE** | Nome da mãe | Texto | 100 |  | Não |  |  |
| **OBSERVACOES** | Campo de Observações | Texto grande | ≈ 2 GB |  | Não |  | Campo observação na internação do paciente |
| **ATENDIMENTO** | Identificador / Código do Atendimento | Texto | 50 |  | Não |  | A partir da release 12.1.2302 |

 Movimentação

**Movimentação**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV\_Movimentacao | | | | | | |
| **Campo na view** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | M | Linha com dados do paciente, internação e alta |
| **COLIGADA** | Código da coligada | Número inteiro |  |  | Sim |  |  |
| **PRONTUARIO** | Prontuário | Texto | 9 |  | Sim |  |  |
| **NOMEPACIENTE** | Nome do paciente | Texto | 50 |  | Sim |  |  |
| **DTENTRINTERNACAO** | Data de Entrada da Internação | Data | 10 | dd/mm/aaaa | Sim |  |  |
| **HRENTRINTERNACAO** | Hora de Entrada da Internação | Texto | 4 | hhmm | Sim |  |  |
| **DATAENTRADA** | Data de Entrada | Data | 10 | dd/mm/aaaa | Sim |  |  |
| **HORAENTRADA** | Hora de Entrada | Texto | 4 | hhmm | Sim |  |  |
| **DATASAIDA** | Data de Saída | Data | 10 | dd/mm/aaaa | Não |  |  |
| **HORASAIDA** | Hora de Saída | Texto | 4 | hhmm | Não |  |  |
| **CODCLINICA** | Código da unidade clínica | Texto | 50 |  | Sim |  |  |
| **CODLEITO** | Código do Leito | Texto | 50 |  | Não |  |  |

Cirurgia 

**Cirurgia**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV\_Cirurgia | | | | | | |
| **Campo na view** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | C | Linha com dados do cabeçalho da cirurgia |
| **CODCOLIGADA** | Código da coligada | Número inteiro |  |  | Sim |  |  |
| **PRONTUARIO** | Prontuário | Texto | 9 |  | Sim |  |  |
| **PACIENTE** | Nome do paciente | Texo | 50 |  | Sim |  |  |
| **CODESPECIALIDADE** | Código da especialidade | Texto | 50 |  | Não |  |  |
| **TIPOCIRURGIA** | Tipo de cirurgia | Texto | 1 |  | Não | E (Eletiva) T (Trauma) U (Urgência) |  |
| **TIPOFERIDA** | Tipo de ferida | Texto | 1 |  | Não | P (Potencialmente Contaminada) C (Contaminada) I (Infectada) L (Limpa) |  |
| **DATAHORAINICIO** | Data e hora do início | Data / Hora | 17 | dd/mm/aaaa hh:mm | Sim |  |  |
| **DATAHORATERMINO** | Data e hora do término | Data / Hora | 16 | dd/mm/aaaa hh:mm | Não |  |  |
| **ASA** | Risco cirúrgico | Número inteiro |  |  | Não | 1 à 6 |  |
| **CRMANESTESISTA** | CRM do anestesista | Texto | 50 |  | Não |  | É o CRM ou o cód. cliente do médico |
| **TIPOANESTESIA** | Tipo da anestesia | Texto | 1 |  | Não | L (Local) G (Geral) B (Bloqueio) |  |
| **CODCIRURGIA** | Código identificador da cirurgia | Texto | 50 |  | Sim |  | Deve ser único por cirurgia |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV\_Procedimentos | | | | | | |
| **Campo na view** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | P | Linha com dados dos procedimentos da cirurgia |
| **CODTABELAORIGEM** | Código da tabela da qual provém o procedimento cirúrgico | Texto | 6 |  | Sim |  | Ex.: SUS, UNIMED, CBHPM, etc. |
| **CODPROCORIGEM** | Código do procedimento dentro da tabela de origem | Texto | 10 |  | Sim |  |  |
| **DESCORIGEM** | Descrição do procedimento dentro da tabela de origem | Texto | 100 |  | Sim |  |  |
| **VIDEO** | Procedimento por vídeo | Lógico | 1 |  | Não | 0 (Não) 1 (Sim) |  |
| **CODCIRURGIA** | Código identificador da cirurgia | Texto | 50 |  | Sim |  |  |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV\_Cirurgioes |  |  |  |  |  |  |
| **Campo na view** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | M | Linha com dados dos cirurgiões atuantes na cirurgia |
| **CRM** | CRM do cirurgião | Texto | 50 |  | Sim |  | É o CRM ou o cód. cliente do médico |
| **FUNCAO** | Função do cirurgião na cirurgia | Texto | 1 |  | Sim | P (Principal) A (Auxiliar) |  |
| **CODCIRURGIA** | Código identificador da cirurgia | Texto | 50 |  | Sim |  |  |

**Observações:**A data / hora de início e término são usadas para fazer o cálculo de tempo de ferida aberta e devem ser referentes à data / hora de início e término efetivos da cirurgia em detrimento da data / hora de início e término de ocupação da sala cirúrgica

Cultura 

**Cultura**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV\_Cultura | | | | | | |
| **Campo na view** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | C | Linha com dados do cabeçalho da cultura |
| **CODCOLIGADA** | Código da coligada | Número inteiro |  |  | Sim |  |  |
| **PRONTUARIO** | Prontuário | Texto | 9 |  | Sim |  |  |
| **PACIENTE** | Nome do paciente | Texto | 50 |  | Sim |  |  |
| **DATACULTURA** | Data da cultura | Data | 10 | dd/mm/aaaa | Sim |  | É a data da coleta |
| **HORACULTURA** | Hora da cultura | Texto | 4 | hhmm | Não | [0-2][0-9]:[0-5][0-9] | Hora da coleta |
| **DATARESULTADO** | Data do resultado da cultura | Data | 10 | dd/mm/aaaa | Sim |  | Data do Resultado Final do exame |
| **HORARESULTADO** | Hora do resultado da cultura | Texto | 4 | hhmm | Não | [0-2][0-9]:[0-5][0-9] | Hora do Resultado Final do exame |
| **GRUPOMATERIAL** | Grupo do material | Texto | 50 |  | Não |  |  |
| **CODMATERIAL** | Código do material coletado | Texto | 50 |  | Não |  | É o material detalhado |
| **CODCLINICA** | Código da unidade clínica | Texto | 50 |  | Não |  | É a unidade em que o paciente estava internado no momento da coleta |
| **CODESPECIALIDADE** | Código da especialidade | Texto | 50 |  | Não |  | É a especialidade do médico que solicitou a coleta do exame |
| **GRAM** | Gram efetuado na cultura | Texto | ≈ 2 GB |  | Não |  |  |
| **OBSERVACOES** | Observações adicionais | Texto grande | ≈ 2 GB |  | Não |  |  |
| **NUMPEDIDOCULTURA** | Código identificador do resultado de cultura | Texto | 50 |  | Sim |  | Deve ser único por resultado de cultura |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV\_Germes | | | | | | |
| **Campo na view** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | G | Linha com dados dos germes da cultura |
| **CODGERME** | Código do germe | Texto | 50 |  | Sim |  |  |
| **NUMCOLONIAS** | Número de colônias | Texto | 150 |  | Não |  | Ex.: > 300 ufc/m |
| **NUMPEDIDOCULTURA** | Código identificador do resultado de cultura | Texto | 50 |  | Sim |  |  |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV\_Antibiograma |  |  |  |  |  |  |
| **Campo na view** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | A | Linha com dados dos antibiogramas dos germes da cultura |
| **CODANTIBIOTICO** | Código do antibiótico | Texto | 50 |  | Sim |  | Deve ser trazido o código contido no campo cód. cliente do cadastro de antibiótico, não um dos nomes comerciais |
| **CODGERME** | Código do germe | Texto | 50 |  | Sim |  |  |
| **SENSIBILIDADE** | Sensibilidade do germe ao antibiótico | Texto | 1 |  | Não | R (Resistente) S (Sensível) I (Intermediário) P (Positivo / Presente) N (Negativo / Ausente) |  |
| **NUMPEDIDOCULTURA** | Código identificador do resultado de cultura | Texto | 50 |  | Sim |  |  |
| **OPERADORMIC** | Operador de comparação do valor do MIC | Texto | 2 |  | Não | <, <=, >, >=, = |  |
| **VALORMIC** | Valor do MIC | Número com uma casa decimal com vírgula |  |  | Não |  |  |

Antibiótico

**Antibiótico**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV\_Antibiotico | | | | | | |
| **Campo na view** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | A | Linha com dados do paciente, internação e alta |
| **CODCOLIGADA** | Código da coligada | Número inteiro |  |  | Sim |  |  |
| **PRONTUARIO** | Prontuário | Texto | 9 |  | Sim |  |  |
| **PACIENTE** | Nome do paciente | Texto | 50 |  | Sim |  |  |
| **CODCLINICA** | Código da unidade clínica | Texto | 50 |  | Sim |  | É a unidade clínica que o paciente estava no momento do consumo do antibiótico |
| **CODESPECIALIDADE** | Código da especialidade | Texto | 50 |  | Não |  | É a especialidade do médico que prescreveu o antibiótico |
| **CRM** | CRM do médico que receitou o antibiótico | Texto | 50 |  | Não |  |  |
| **DATADISPENSACAO** | Data da dispensação do antibiótico pela farmácia | Data | 10 | dd/mm/aaaa | Sim |  |  |
| **HORADISPENSACAO** | Hora da dispensação | Texto | 4 | hhmm | Não |  |  |
| **NOMEANTIBIOTICO** | Nome comercial ou princípio ativo do antibiótico | Texto | 250 |  | Sim |  |  |
| **VIA** | Via de administração do antibiótico | Texto | 1 |  | Não | O (Oral) T (Tópica) P (Parenteral) |  |
| **CONCENTRACAO** | Concentração do antibiótico | Número com uma casa decimal com vírgula |  |  | Não |  | Expressa em mg |
| **QUANTIDADE** | Quantidade dispensada | Número inteiro |  |  | Não |  |  |
| **DOSETOTAL** | Dose total | Número inteiro |  |  | Não |  | Expressa em mg |
| **INDICACAO** | Tipo de indicação | Texto | 1 |  | Sim | T (Terapêutico) P (Profilático) S (Sem indicação) |  |
| **PROFILAXIA** | Tipo de profilaxia | Texto | 1 |  | Não | L (Limpa) P (Pot. Contaminada) C (Contaminada) I (Infectada) D (Indicação clínica) |  |
| **INFECCAO** | Tipo de infecção | Texto | 1 |  | Não | H (Hospitalar) C (Comunitária) O (Hospitalar de outra instituição) |  |
| **SITIO1** | Sitio Secundário | Texto | 4 |  | Não |  | Sitio secundário do pedido de anbiótico, ao enviar o sítio, automaticamente a 'Indicação' do pedido será 'terapêutico'. |
| **SITIO2** | Sitio Secundário | Texto | 4 |  | Não |  | Sitio secundário do pedido de anbiótico, ao enviar o sítio, automaticamente a 'Indicação' do pedido será 'terapêutico'. |
| **SITIO3** | Sitio Secundário | Texto | 4 |  | Não |  | Sitio secundário do pedido de anbiótico, ao enviar o sítio, automaticamente a 'Indicação' do pedido será 'terapêutico'. |
| **OUTRASINFORMACOES** | Informações adicionais | Texto grande | ≈ 2 GB |  | Não |  | Deve trazer informações que sejam importantes para completar a prescrição no Janus |
| **CODCLINICADISPENSACAO** | Código da unidade clínica da dispensação | Texto | 50 |  | Não |  | Unidade Clínica onde ocorreu a dispensção do antibiótico |
| **NUMITEMPEDIDOANTIBIOTICO** | Número da dispensação do antibiótico | Texto | 50 |  | Sim |  | Deve ser único por item (antibiótico) de dispensação |

**Observações:**

Deverá ser feito um de-para do tipo de apresentação da base de origem para a via de administração.  
  
Por exemplo:

* se apresentação = comprimido ou cápsula, então a via é **oral** (O);
* se apresentação = ampola ou frasco, então a via é **parenteral** (P);
* se apresentação = creme ou pomada, então a via é **tópico** (T).

O campo **OUTRASINFORMACOES** é destinado para informações não estruturadas do sistema origem, que não podem ser obtidas para preenchimento de um dos outros campos.  
Este campo será utilizado para que, no momento da validação da importação, o profissional possa utilizá-lo para conferências e posterior cálculo e preenchimento de valores, isto ocorre pois nem sempre o sistema de origem pode fornecer dados como quantidade, data/hora, concentração, etc.

 Cada antibiótico deverá ter todos os nomes comerciais que são dispensados pela farmácia. Estes nomes comerciais devem ser cadastrados até o primeiro número da descrição do antibiótico no sistema de estoque.

Por exemplo:

* Nome do antibiótico trazido via importação: "Amoxicilina Generis 500 mg Cápsulas".
* Deve ser cadastrado para o princípio ativo "AMOXICILINA" o nome comercial "Amoxicilina Generis".
* O restante do nome, "500 mg Cápsulas", será gravado no campo OUTRASINFORMACOES na importação.
Cultura Parcial

**Cultura Parcial**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV\_Cultura\_Parcial | | | | | | |
| **Campo na view** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | C | Linha com dados do cabeçalho da cultura |
| **CODCOLIGADA** | Código da coligada | Número inteiro |  |  | Sim |  |  |
| **PRONTUARIO** | Prontuário | Texto | 9 |  | Sim |  |  |
| **PACIENTE** | Nome do paciente | Texto | 50 |  | Sim |  |  |
| **DATACOLHETA** | Data da coleta da cultura | Data | 10 | dd/mm/aaaa | Sim |  | É a data da coleta |
| **COLETA** | Hora da coleta da cultura | Texto | 4 | hhmm | Não | [0-2][0-9]:[0-5][0-9] | Hora da coleta |
| **GRUPOMATERIAL** | Grupo do material | Texto | 50 |  | Não |  |  |
| **CODMATERIAL** | Código do material coletado | Texto | 50 |  | Não |  | É o material detalhado |
| **CODCLINICA** | Código da unidade clínica | Texto | 50 |  | Não |  | É a unidade em que o paciente estava internado no momento da coleta |
| **NUMPEDIDOCULTURA** | Código identificador do resultado de cultura | Texto | 50 |  | Sim |  | Deve ser único por resultado de cultura |

Procedimento Invasivo

**Procedimento Invasivo**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome da view:** | RMV\_PROCINVASIVO | | | | | | |
| **Campo na view** | **Descrição** | **Tipo** | **Tamanho Máximo** | **Formato** | **Obrigatório** | **Valores Válidos** | **Observações** |
| **<Não usado>** | Tipo da linha | Texto | 1 |  | Sim | P | Linha com dados do paciente, internação e alta |
| **CODCOLIGADA** | Código da coligada | Número inteiro |  |  | Sim |  |  |
| **PRONTUARIO** | Prontuário | Texto | 9 |  | Sim |  |  |
| **NOMEPACIENTE** | Nome do paciente | Texto | 50 |  | Sim |  |  |
| **DATAINTERNACAO** | Data de Entrada da Internação | Data | 10 | dd/mm/aaaa | Não |  |  |
| **HORAINTERNACAO** | Hora de Entrada da Internação | Texto | 4 | hhmm | Não |  |  |
| **DATAINICIO** | Data de Início | Data | 10 | dd/mm/aaaa | Sim |  |  |
| **HORAINICIO** | Hora de Início | Texto | 4 | hhmm | Não |  |  |
| **DATAFIM** | Data de Saída | Data | 10 | dd/mm/aaaa | Não |  |  |
| **HORAFIM** | Hora de Saída | Texto | 4 | hhmm | Não |  |  |
| **TIPOPROCEDIMENTO** | Tipo de procedimento | Texto | 8 |  | Não |  |  |

**Observações:**

* Estes layouts servem tanto para importação via view como para importação via txt.
* Na importação via view, as colunas referentes ao tipo da linha devem ser desconsideradas.
* Na importação via txt, as colunas referentes ao tipo da linha devem trazer o valor especificado como valor válido.
* Na importação via txt, os campos devem ser separados por ; (ponto e vírgula).
* Não é necessário completar os campos com espaços ou zeros à esquerda.
* Na importação via view, o nome da view e o nome de seus campos devem ser respeitados.

Para que a importação ocorra com sucesso, os cadastros do Janus devem estar alinhados com os cadastros do sistema o qual estão vindo os dados.

O campo 'Cód. Cliente' deve estar preenchido de acordo com o valor trazido via importação nos seguintes cadastros:

* Unidade Clínica.
* Especialidade.
* Médico.
* Convênio.
* Germe.
* Antibiótico.
* Material.

Os antibióticos devem ter nomes comerciais cadastrados.

Todos os campos deverão respeitar o tamanho máximo definido neste layout, seja na importação via view ou via txt.

Caso haja a possibilidade do dado trazido para importação exceder o tamanho máximo de seu campo definido neste layout (quando o tamanho máximo do campo na base de origem excede o tamanho máximo definido neste layout), a view ou txt deverá trazer o campo truncado ou deverá ser feito um de-para para que o dado trazido caiba no tamanho máximo de seu campo definido neste layout.

O formato de data deve ser usado apenas para importação via txt.  
Nas importações via view, os campos do tipo data devem ser do tipo "data" do SGBD.
