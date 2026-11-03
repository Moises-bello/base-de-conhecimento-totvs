---
content_hash: 6d1aac42748c1b991e1d9d4c3cc8021d98ebab6177fbdae2bbb0fd40f388fc31
fetched_at: '2026-06-29T00:06:25.725347+00:00'
page_id: '224444417'
product: rm
source: tdn-rm
title: FOP_DT_eSocial_BR_Parte4
type: documentation
url: https://tdn.totvs.com/display/LRM/FOP_DT_eSocial_BR_Parte4
version: 3
---

# eSOCIAL PARTE 4

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *eSocial* |  | |
| **Versão/Release:** | Biblioteca RM 11.82.39 |

## Descrição

Este documento serve para que os usuários possam configurar dados que completam o eSocial.

## Procedimento para Utilização

## Tabelas e Cadastros da Carga Inicial do eSocial

### Cadastro - Informações do Empregador

No cadastro de Informações do Empregador, na aba identificação / informações do empregador foi adicionado os campos:   
• Indicativo de Desoneração da Folha;   
• Indicativo do optante pelo registro eletrônico;   
• Data de início das atividades (Empresa constante no CNPJ).

Caminho: RH / Folha de Pagamento / Guia eSocial (beta) / Informações do Empregador / Aba Informações do Empregador

Na aba identificação / Informações complementares, foi adicionado o campo “Situação da pessoa física”. Caminho: RH / Folha de Pagamento / Guia eSocial (beta) / Informações do Empregador / Aba Informações Complementares.

[

### Cadastro de Pessoas e Funcionários

Na aba de Documentação(Funcionários) e Doc. Básicos(Pessoas), foram implementado dois campos, sendo eles:

• Data da primeira CNH;   
• Estado Emissor da CNH.

Caminhos:   
• RH / Gestão de Pessoas / Guia Acompanhamento / Pessoas / Dados Pessoais / Doc. Básicos.  
 • RH / Folha de Pagamento / Guia Cadastros / Funcionários / Informações Pessoais / Documentação.

***Funcionários***

***Pessoas***

Na aba Documentos Estrangeiros(Funcionários) e Doc. Estrangeiros(Pessoas) foi implementado o campo Classificação da Condição no Brasil, com o objetivo de armazenar qual é a situação atual do estrangeiro.

Onde será possível escolher as seguintes opções:

Caminhos:   
• RH / Gestão de Pessoas / Guia Acompanhamento / Pessoas / Dados Pessoais / Doc. Estrangeiros.  
 • RH / Folha de Pagamento / Guia Cadastros / Funcionários / Informações Pessoais Documentos Estrangeiros;

### Cadastro de Funcionários

Foi adicionado na aba “Reintegração” a flag: Indicativo de Pagamento em juízo, possuindo o objetivo de indicar se as remunerações e correspondentes contribuições do período compreendido entre o desligamento e a reintegração foram pagas em juízo.   
• Caminho: RH / Folha de Pagamento / Guia Cadastros / Funcionários / Informações Contratuais / Registro / aba Reintegração.

Adicionamos também um novo tipo de reintegração, sendo ela “Reinclusão de Militar”. Já o código 1 do tipo de reintegração foi alterado para “Reintegração por decisão Judicial”.

Lembrando que a aba Reintegração só irá ficar disponível quando o campo Tipo de Admissão estiver preenchido com o tipo I - Reintegração.

### Processos Jurídicos

Foi adicionado no cadastro de processos, o Parâmetro “Processo da empresa contra órgão governamental envolvido no eSocial”.

Caminho: RH / Gestão de Pessoa / Guia Gestão Organizacional / Processos Jurídicos / Processos Jurídicos / aba Identificação.

Este parâmetro irá interferir na “Carga Inicial”de tabelas de processo jurídicos/administrativos, quando do envio deste evento para o governo, fazendo com que seja enviado somente os processos que estiverem com o parâmetro marcado.   
Caso o cliente utilize o Vitae, módulo Processos Jurídicos, deverá avaliar se na empresa existem processos administrativos ou judiciais em curso conforme tópicos abaixo e marcar o parâmetro citado acima.   
Não será necessário enviar para o governo (via carga inicial) todos os processos jurídicos cadastrados neste módulo, somente os abaixo.

Obs.: A Carga inicial de processos jurídicos será disponibilizada no produto em versão ainda a ser divulgada pela TOTVS.

1 – Processo Administrativo/Judicial Fap Registro que identifica, em caso de existência, o processo administrativo/judicial em que houve decisão ou sentença favorável ao contribuinte suspendendo ou alterando a alíquota FAP aplicável ao contribuinte

2 – Processo Administrativo/Judicial Rat Registro que identifica, em caso de existência, o processo administrativo ou judicial em que houve decisão/sentença favorável ao contribuinte modificando a alíquota RAT da empresa.

3 – Processo Contribuição Previdenciária – dados de Rubrica Caso a empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de contribuição previdenciária relativa a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.

4 – Processo IRRF – dados de Rubrica Caso a empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de imposto de renda relativo a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.

5 – Processo FGTS – dados de Rubrica Caso a empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de FGTS relativo a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.

6 – Processo Contribuição Sindical – dados de Rubrica Caso a empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de contribuição sindical relativa a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.

7 – informações de Processos Judiciais Terceiros/Outras Entidades e Fundos Informações sobre a existência de processos judiciais, com sentença/decisão favorável ao contribuinte, relativos às contribuições destinadas a outras Entidades e Fundos.

8 – Informações de Processos Judiciais do trabalhador Informações sobre a existência de processos judiciais do trabalhador com decisão favorável quanto à não incidência de contribuição previdenciária e/ou Imposto de Renda

9 - Informações de alvará Judicial Informações do alvará judicial, preenchimento obrigatório em caso de contratação de menores de 14 anos, em qualquer categoria, e de maiores de 14 e menores de 16, em categoria diferente de "Aprendiz".

10 – Processo Judicial reintegração Em caso de reintegração por determinação judicial, preencher com o número do processo. 11 – Processo Trabalhista quando desligamento decisão judicial Número que identifica o processo trabalhista, quando o desligamento se der por decisão judicial.

### Tabela “Natureza das Rubricas da folha de pagamento”

##### Tabela 3 do eSocial – Tabela de Natureza das rubricas da folha de Pagamento

A tabela de natureza de rubricas foi alterada no layout 2.0 do eSocial, algumas tiveram alterações de descrição, outras tiveram o código alterado, outras foram excluídas. Abaixo um quadro explicativo com todas as alterações.  
 Após a atualização do executor de script, as rubricas serão ajustadas conforme este quadro, inclusive no cadastro de “Eventos” o campo ‘natureza de rubrica’ será receberá alterações do tipo “depara” para que o cliente não tenha que preencher e configurar algumas naturezas de rubricas novamente. Porém será necessário uma avaliação/conferencia geral dos eventos (verbas) comparando com a tabela 3 do eSocial. Este vínculo de rubricas no cadastro de eventos (verbas) será importante para o envio correto do arquivo de folha mensal do funcionário para o eSocial.
