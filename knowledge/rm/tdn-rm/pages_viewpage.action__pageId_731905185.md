---
content_hash: d4640573ee1e3c8d5bf429fd6b9d890b6bae8ceb771d741bd3a2eaa9c02e7a2c
fetched_at: '2026-06-29T00:11:28.577993+00:00'
page_id: '731905185'
product: rm
source: tdn-rm
title: 'Bloco 0: Abertura, Identificação e Referências'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=731905185
version: 83
---

Registro 0000: Abertura do Arquivo Digital e Identificação do Empresário ou da Sociedade Empresária.

O registro 0000 abre o arquivo da ECD, informa o período correspondente à escrituração e identifica a pessoa jurídica.

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | LECD |
| 03 | DT\_INI | Datas de Início e Término informadas no Cadastro da **Forma de Escrituração** existente na tela de geração da ECD. |
| 04 | DT\_FIN |
| 05 | NOME | Estes campos são gerados, respectivamente, com o **Nome**, **CNPJ**, **Estado**, **Inscrição Estadual**, **Município** e **Inscrição Municipal** existentes no Cadastro da Filial Matriz ou Filial Escriturada, informada na tela de geração da ECD. A filial utilizada irá depender do Tipo de Escrituração selecionada.   Dica! Para que o campo **Filial Escriturada** fique visível o **Tipo de Escrituração** selecionada deve ser Descentralizada e o campo **Descentralização** deve ser Filial. |
| 06 | CNPJ |
| 07 | UF |
| 08 | IE |
| 09 | COD\_MUN |
| 10 | IM |
| 11 | IND\_SIT\_ESP | Estes campos são gerados, respectivamente, com a **Situação Especial** e o **Indicador do Início do Período** informados no processo de geração da ECD. |
| 12 | IND\_SIT\_INI\_PER |
| 13 | IND\_NIRE | Este campo é gerado com o **Nro. Registro na Junta Comercial** existente no Cadastro da Filial Matriz ou Filial Escriturada, informada na tela de geração da ECD. A filial utilizada irá depender do Tipo de Escrituração selecionada. |
| 14 | IND\_FIN\_ESC | Estes campos são gerados, respectivamente, com o **Indicador de Finalidade da Escrituração**, **Hash da Escrituração Substituta**, **Indicador de Entidade Sujeita a Auditoria Independente** e **Indicador do Tipo de ECD** informados no processo de geração da ECD. |
| 15 | COD\_HASH\_SUB |
| 16 | IND\_GRANDE\_PORTE |
| 17 | TIP\_ECD |
| 18 | COD\_SCP | O CNPJ da SCP é gerado com o **CNPJ** existente no Cadastro da Filial SPC, informada na tela de geração da ECD. |
| 19 | IDENT\_MF | O Indicador de Moeda Funcional está presente dentro da Estrutura de Transferência de Grupos Contábeis informada na tela de geração da ECD.     Dica! Habilite o parâmetro "**Habilitar controle de Moeda Funcional no SPED Contábil**" para que o campo Moeda Funcional seja apresentado. |
| 20 | IND\_ESC\_CONS | Quando um **Plano Consolidado - Bloco K** for informado na geração da ECD, o RM irá imprimir esse campo com o caractere "S", caso contrário com "N". |
| 21 | IND\_CENTRALIZADA | Este campo é gerado com o **Tipo de Escrituração**informada no processo de geração da ECD. Ele irá receber "0" para Escrituração Centralizada e "1" para Escrituração Descentralizada. |
| 22 | IND\_MUDANC\_PC | Registro gerado automaticamente. Caso ocorra mudanças no Plano de Contas seu valor será "S", caso contrário será "N". |
| 23 | COD\_PLAN\_REF | Este campo é gerado com o **Plano Referencial**informado no processo de geração da ECD. |

Registro 0001: Abertura do Bloco 0

O registro 0001 abre o bloco 0 e indica se há ou não há dados informados no bloco.

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | IND\_DAD | Caso o Bloco 0 tenha dados informados seu valor será "1", caso contrário será "0". |

Registro 0007: Outras Inscrições Cadastrais da Pessoa Jurídica

Neste registro devem ser incluídas as inscrições cadastrais da pessoa jurídica que, legalmente, tenha direito de acesso ao livro contábil digital. O código da empresa no Banco Central corresponde ao “ID\_Bacen”, conforme registrado no Unicad (Informações sobre Entidades de Interesse do Banco Central), composto por 8 dígitos e iniciados com a letra "Z".

O registro 0007 irá listar todas as inscrições existentes no Cadastro de Outras Inscrições Cadastrais.

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | COD\_ENT\_REF | Estes campos estão presentes na tela de Outras Inscrições Cadastrais e são representados pela **Instituição** e pelo **Código Cadastral** respectivamente. |
| 03 | COD\_INSCR |

Registro 0020: Escrituração Contábil Descentralizada

Este registro deve ser preenchido somente quando a pessoa jurídica utilizar escrituração descentralizada (0000.IND\_CENTRALIZADA = “1”). Quando o arquivo se referir à escrituração da matriz (Campo 02 igual a “0”), os campos de 03 a 08 devem ser preenchidos com os dados da(s) filial(is). Por outro lado, quando o arquivo se referir à escrituração da filial (Campo 02 igual a “1”), os campos de 03 a 08 devem ser preenchidos com os dados da matriz. Para identificação de matriz ou filial, deve ser considerada a situação na data final a que se refere a escrituração. Quando a escrituração é da matriz (CNPJ da matriz no registro 0000), é possível apresentar um ou mais registros 0020, com o campo “Indicador de Descentralização” (Campo 02) preenchido com “0 – Escrituração da Matriz” e o CNPJ de cada uma das filiais informado no campo 03. Deve ser preenchido um registro 0020 para cada filial. Por outro lado, quando a escrituração é da filial (CNPJ da filial no registro 0000), só é possível que exista um registro 0020, com o campo “Indicador de Descentralização” (Campo 02) preenchido com “1 – Escrituração da Filial”, e o CNPJ da matriz informado no campo 02.

Para exibir o registro 0020 é necessário incluir previamente os participantes, através da tela de cadastro existente em Obrigações Acessórias → Cadastros → Participantes. Em seguida, na tela de geração da ECD, é imprescindível que o registro facultativo 0020 esteja marcado.

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | IND\_DEC | Gerado automaticamente pelo sistema. Caso a Escrituração seja da Matriz o valor impresso será "0", caso seja da Filial o valor impresso será "1". |
| 03 | CNPJ | Estes campos são gerados, respectivamente, com o **CNPJ**, **Estado**, **Inscrição Estadual**, **Município**, **Inscrição Municipal** e **Nro. Registro na Junta Comercial** informados no Cadastro de Filial.  Se o **Tipo de Escrituração** for Descentralizada e o campo **Descentralização** for Matriz estes dados serão recuperados das filiais existentes na coligada do contexto ou na coligada global, ou seja, haverá um registro 0020 para cada filial. Entretanto, se o **Tipo de Escrituração** for Descentralizada e o campo **Descentralização** for Filial, estes dados serão recuperados da **Filial Matriz,** informada na tela de geração da ECD. |
| 04 | UF |
| 05 | IE |
| 06 | COD\_MUN |
| 07 | IM |
| 08 | NIRE |

Registro 0035: Identificação das SCP

O registro só deve ser utilizado nas ECD das pessoas jurídicas sócias ostensivas que possuem SCP, para identificação das SCP da pessoa jurídica no período da escrituração.

Para gerar o registro 0035 é necessário que, no anexo Dados Fiscais do Cadastro de Filial, a opção **Filial SCP** esteja marcada e a **Filial Sócio Ostensivo** tenha sido informada.

Também é preciso que, na tela de parâmetros do processo de geração do SPED Contábil, o campo **Indicador do Tipo de ECD** seja "ECD de empresa participante de SCP como sócio ostensivo".

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | COD\_SCP | Estes campos são gerados, respectivamente, com o **CNPJ** e **Nome** existentes no Cadastro das Filiais associadas a **Filial Matriz** (Filial Sócio Ostensivo), informada na tela de geração da ECD.  Irá haver um registro 0035 para cada filial vinculada a **Filial Matriz** (Filial Sócio Ostensivo). |
| 03 | NOME\_SCP |

Registro 0150: Tabela de Cadastro do Participante

Representa um conjunto de informações para identificar as pessoas físicas e jurídicas com as quais a empresa tem algum tipo de relacionamento específico. Somente devem ser informados os participantes com os quais a empresa tenha um dos relacionamentos constantes em tabela específica do SPED. A grande maioria dos clientes e fornecedores das empresas não preenche os requisitos para ser incluída nos registros 0150.

Para exibir o registro 0150 é necessário incluir previamente os participantes, através da tela de cadastro existente em Obrigações Acessórias → Cadastros → Participantes. Em seguida, na tela de geração da ECD, é imprescindível que o registro facultativo 0150/0180 esteja marcado.

Haverá um registro 0150 para cada Participante cadastrado na coligada do contexto.

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | COD\_PART | Estes campos variam de acordo com o Tipo do Participante.  Para Participantes do tipo "Filial" eles são gerados, respectivamente, com o **Código**e **Filial** informados no Cadastro de Participantes.  Para Participantes do tipo "Cliente/Fornecedor" eles são gerados, respectivamente, com o **Código** e **Cliente/Fornecedor** informados no Cadastro de Participantes. |
| 03 | NOME |
| 04 | COD\_PAIS | Estes campos variam de acordo com o Tipo do Participante.  Para Participantes do tipo "Filial" eles são gerados, respectivamente, com **País** e **CNPJ** informados no Cadastro de Filial.  Para Participantes do tipo "Cliente/Fornecedor" eles são gerados, respectivamente, com o **País** e **CPF/CNPJ** informados no Cadastro de Cliente/Fornecedor. Vale ressaltar que o campo 05 só será preenchido se a **Classificação** do Cliente/Fornecedor for "Fornecedor". |
| 05 | CNPJ |
| 06 | CPF | Este campo é gerado com o **CPF/CNPJ** informadono Cadastro de Cliente/Fornecedor, cuja **Classificação** seja "Cliente" ou "Ambos". |
| 07 | NIT | Este campo é gerado com o **NIT** informado no Cadastro de Cliente/Fornecedor, pois só está presente em Participantes do tipo "Cliente/Fornecedor". |
| 08 | UF | Estes campos são gerados, respectivamente, com o **Estado**, **Inscrição Estadual**, **Inscrição Estadual S. T**, **Município**, **Inscrição Municipal** e **Inscrição no Suframa** informados.  Para Participantes do tipo "Filial" estes dados serão recuperados do Cadastro de Filial e para Participantes do tipo "Cliente/Fornecedor" serão recuperados do Cadastro de Cliente/Fornecedor. |
| 09 | IE |
| 10 | IE\_ST |
| 11 | COD\_MUN |
| 12 | IM |
| 13 | SUFRAMA |

Registro 0180: Identificação do Relacionamento com o Participante

Neste registro devem ser informados os códigos de relacionamento dos participantes, conforme tabela do SPED, a data início do relacionamento e a data de término do relacionamento, caso exista.

Os relacionamentos dos participantes devem ser incluídos em Obrigações Acessórias → Cadastros → Tipos de Relacionamentos de Participantes. Após a inclusão dos tipos de relacionamentos é necessário associá-los aos participantes, através do Cadastro de Participantes. Para cada registro 0150, que representa o participante, irão haver um ou mais registros 0180.

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | COD\_REL | Estes campos são gerados, respectivamente, com o **Relacionamento**, **Data Início do Relacionamento** e **Data Término do Relacionamento** informadas nos relacionamentos existentes no Cadastro de Participantes. |
| 03 | DT\_INI\_REL |
| 04 | DT\_FIN\_REL |
