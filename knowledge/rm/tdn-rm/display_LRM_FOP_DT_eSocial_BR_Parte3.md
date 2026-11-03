---
content_hash: 95508ccbe2db8797d4b2cc1e0010b6e11dca8e086a6fa115832acdaa97c7ffe8
fetched_at: '2026-06-29T00:06:25.592201+00:00'
page_id: '224442152'
product: rm
source: tdn-rm
title: FOP_DT_eSocial_BR_Parte3
type: documentation
url: https://tdn.totvs.com/display/LRM/FOP_DT_eSocial_BR_Parte3
version: 3
---

# eSOCIAL PARTE 3

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *eSocial* |  | |
| **Versão/Release:** | Bibliotecas RM 11.52.63 **|** 11.53.75 **|** 11.82.35 **|** 11.83.55. |

## Descrição

Este documento serve para que os usuários possam configurar dados que completam o eSocial.

## Procedimento para Utilização

### Cadastro de Pessoas - Campos ''Reabilitado'' e ''Deficiente intelectual''

TOTVS Gestão de Pessoas

No Cadastro de Pessoas, na aba Informações Adicionais foram adicionados os campos para informação de deficiência: Intelectual e Reabilitado

### Alteração Global Campos Cadastro Funcionário – Inclusão campo Tipo de Rua

No processo Alteração Global do Cadastro de Funcionários temos a opção para alterar a informação do campo Tipo de Rua do Endereço de Funcionários.

Esta funcionalidade visa facilitar a alteração do campo, com o recurso de alteração para vários funcionários, de acordo com a seleção definida. Para executar a alteração, o usuário deverá selecionar no campo Dados a serem alterados, a nova opção Dados Pessoais. Serão listados os campos possíveis de serem alterados: Bairro, Rua, Tipo de Bairro além da opção Tipo de Rua.

### SEFIP – Concatenação do campo Tipo de Rua

A geração do arquivo SEFIP.RE foi ajustada para concatenar o campo Tipo de Rua do cadastro Endereço dos funcionários. Desta forma, o registro 14 do arquivo, será gerado com a informação do campo Tipo Rua.

***Registro 14 do arquivo SEFIP.RE***

***Endereço do funcionário no TOTVS Folha de Pagamento***

### 

### Cadastro de Funcionários

***Campo Calcula/Não Calcula IRRF***

Foi incluído no cadastro de Funcionários na aba Parâmetros, os campos relacionados a IRRF (Calcula / Não calcula). Marcando a opção Não calcula, o usuário deverá cadastrar o processo judicial que concedeu a isenção do imposto para o funcionário. O cadastro do processo jurídico deverá ser realizado vide item 4.3 - deste documento.

Observação: Os campos IRRF – Não Calcula e Calcula, ainda não influenciam no cálculo da folha de pagamento

### *Anexo Processos Judiciais do Funcionário*

Para atender o arquivo S-1200 da folha de pagamento foi criado no cadastro de Funcionários o anexo Processos Judiciais do Funcionário. Os processos jurídicos deverão ser cadastrados quando o funcionário tiver isenção de INSS ou IRRF (campos Não calcula INSS / IRRF marcados).

***Anexo – Cadastro de Atestado***

No anexo Atestados, do cadastro de Funcionários, o campo Código do Médico foi ajustado e agora é um lookup que lista os médicos cadastrados como Profissional de Saúde.

O campo Número do CRM receberá o número cadastrado para o médico “Profissional de Saúde”.

***Anexo Vínculos Empregatícios com outras Empresas***

No anexo Vínculos Empregatícios com outras Empresas do cadastro de Funcionários, foram incluídos os campos Competência Final e Sempre Válido. Com estes novos campos, o usuário da folha de pagamento poderá limitar por Competência Inicial e Competência Final a validade dos dados de Remuneração e Valor Desconto de INSS de outra empresa, ou ainda definir que os dados são Sempre Válidos. Os usuários poderão utilizar este recurso quando os valores do outro emprego do funcionário não alterar mês a mês.

***Anexo Histórico de Endereço***

No Histórico de Endereços do Cadastro de Funcionário, foi incluído o campo Tipo de Rua:

### 

### 

### Parametrização De-Para do Estado Civil eSocial

No eSocial está definido que o campo estadoCivil deverá ser preenchido com uma das informações:

1 - Solteiro   
2 - Casado   
3 - Separado   
4 - Divorciado   
5 - Viúvo   
6 - União Estável

Devido ao TOTVS Folha de Pagamento permitir os usuários definirem os estados civis, foi necessário disponibilizar no Parametrizador o recurso de De – Para, onde os usuários deverão definir a correspondência dos itens de estado civil existentes na Folha de Pagamento, em relação aos itens definidos pelo eSocial:

Observação: no campo “Estado Civil Labore” serão listados apenas os tipos de estado civil diferentes de C, D, I, S, V pois estes valores são internos do labore (não permitem alteração) e o de-para será feito internamente.

### 

### Condições Diferenciadas de Trabalho

O eSocial lista os seguintes tipos de condições diferenciadas de trabalho conforme layout do evento S-2360.

• 01 – Insalubridade   
• 02 – Periculosidade   
• 03 – Fator de Risco  04 – Membro Sesmt   
• 05 – Designado CIPA  06 – Trabalhador treinado para utilização de material de primeiros socorros   
• 07 – Autorizado a trabalhar em instalações elétricas   
• 08 – Autorizado a operar e intervir em máquinas   
• 09 – Responsável Técnico pela Segurança em Espaço Confinado Foi implementado no Cadastro de Funcionários o anexo Condições Diferenciadas de Trabalho.

### 

Através deste anexo os usuários visualizarão as condições diferenciadas geradas automaticamente pelo sistema e especificamente poderão incluir manualmente as condições diferenciadas abaixo:

• 06 – Trabalhador treinado para utilização de material de primeiros socorros   
• 07 – Autorizado a trabalhar em instalações elétricas   
• 08 – Autorizado a operar e intervir em máquinas   
• 09 – Responsável Técnico pela Segurança em Espaço Confinado

Os demais itens da lista de Condições Diferenciadas de Trabalho serão gerados automaticamente pelo sistema, no anexo Condições Diferenciadas de Trabalho:   
• 01 – Insalubridade   
• 02 – Periculosidade

As condições diferenciadas relativas a Insalubridade e Periculosidade, são definidas através do TOTVS Segurança e Medicina do Trabalho, pelo menu Reconhecimento e Avaliação de Risco.

No Cadastro de Reconhecimento e Avaliação de Riscos foi inserido uma nova aba denominada “Insalubridade/Periculosidade”, onde o usuário deverá informar se um determinado Reconhecimento de Risco irá oferecer aos funcionários uma condição de trabalho de Periculosidade e/ou Insalubridade

Os campos Exposição a Periculosidade e Exposição a Insalubridade deverão ser marcados para indicar as situações que houverem e deverá descrever os respectivos campos de Laudo. Quando o campo Exposição a Insalubridade for marcado, será habilitado o campo Fator de Insalubridade onde o usuário deverá informar o grau insalubre Máximo, Médio ou Mínimo que o funcionário está exposto. Observação: A geração automática das Condições diferenciadas de trabalho, que serão visualizadas no anexo do cadastro de funcionários, depende da geração da Avaliação do Risco.

• 03 – Fator de Risco

Quando uma Avaliação de Risco é realizada, é gerado no anexo do cadastro de Funcionário automaticamente a Condição diferenciada de trabalhado por Fator de Risco. E será incluída também Periculosidade e/ou Insalubridade caso a Avaliação tenha estas situações marcadas no cadastro.

• 04 – Membro Sesmt

Serão membros Sesmt, os funcionários que tiverem cadastrados como: Responsáveis pelos Registros Ambientais Sesmt, que é realizado no TOTVS Segurança e Medicina do Trabalho em PPRA / Resp. Reg. Ambientais, e ou;

Responsáveis pelas Monitorações Biológicas Sesmet, que é realizado no TOTVS Segurança e Medicina do Trabalho em PCMSO / Resp. Monitoração Biológica.

• 05 – Designado CIPA

Será identificado com condição diferenciada de trabalho Designado da CIPA, os funcionários que forem Representantes ou Suplentes da CIPA, eleitos pelos empregados ou indicados pelo empregador.

Observação: Condições diferenciadas de trabalho geradas automaticamente pelo sistema não poderão ser editadas ou excluídas pelo Anexo do Cadastro de Funcionários.

### Cadastro de Estabilidades – Carga Inicial Estabilidade

No cadastro de Funcionários, em Processos foi disponibilizada a funcionalidade Carga Inicial Estabilidade para gerar as estabilidades provenientes dos registros de afastamentos antigos.

Quando não for marcado nenhum funcionário no Grid de Visão de Funcionários, será aberto a tela Wizard abaixo, que permitirá utilizar a grade de seleção de funcionários.

Caso seja selecionado no Grid de Visão um ou vários Funcionários, o processo será imediatamente executado sem abrir a tela de Wizard.

 

### Portal – Campo de Registro Profissional

No RM Portal o campo Registro Profissional localizado em Meus Dados / Documentos / Documentos 2, exibirá o número do registro que estiver parametrizado como Registro Profissional no TOTVS Folha de Pagamento, anexo Registro Profissional, conforme print abaixo.

Veja o Registro profissional associado ao funcionário como Principal, no TOTVS Folha de Pagamento:

 

### Parâmetros de EPI – Cadastro Reconhecimento/Avaliação de Riscos

Na Tela de Reconhecimento/Avaliação de Riscos, ao inserir um novo registro, os campos da aba Parâmetros de EPI estarão marcados por padrão. Havendo necessidade, o usuário poderá desmarcar os parâmetros que forem necessários.

### Cadastro de Processos Jurídicos - Campo Indicativo de Decisão

No cadastro de Processos Jurídicos, localizado no TOTVS Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos, a descrição dos itens do campo Indicativo de Decisão foram adequados conforme manual do eSocial:

Cadastro de Seções – Anexo Processo Judicial de Terceiros/Outras Entidades

No Cadastro de Seções do TOTVS Folha de Pagamento, foi incluído o anexo Processo Judicial de Terceiros/Outras Entidades. Neste anexo deverão ser cadastrados os processos judiciais com sentença/decisão favorável ao contribuinte, relativos às contribuições destinadas a outras Entidades e Fundos (terceiros).

Neste cadastro o usuário deverá informar no campo código, o código da entidade Terceiros constante no anexo II da IN 971/2009, e no campo Número do Processo Judicial, o processo com sentença favorável a empresa. Neste campo poderá associar através do ícone Lupa o processo cadastrado no TOTVS Gestão de Pessoas em Processos Jurídicos.
