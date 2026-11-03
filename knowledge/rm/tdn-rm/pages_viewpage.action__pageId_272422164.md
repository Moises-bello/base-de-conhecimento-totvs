---
content_hash: 5b748066b2238b14fbbf0c0a181c07ec76d87b1bf2682f73e76a8a04c49d81f0
fetched_at: '2026-06-29T00:08:30.328761+00:00'
page_id: '272422164'
product: rm
source: tdn-rm
title: DT Saneamento de dados/Carga Inicial - eSocial Layout 2.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272422164
version: 146
---

Layout 2.2 eSocial]]>

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | Recursos Humanos | | |
| **Módulo:** | TOTVS Folha de Pagamento, TOTVS Gestão de Pessoas | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Informações do Empregador | Informações do Empregador | | Seções | Seções | | Tomador de Serviço (CLI/FOR) | Tomador de Serviço (CLI/FOR) | | Eventos | Eventos | | Funções | Funções | | Horários | Horários | | Funcionários | Funcionários | | Processos Jurídicos | Processos Jurídicos | | | |
| **Requisito (ISSUE):** |  | | |
| **País:** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

---

Índice]]>

.\*ndice:

---

Objetivo]]>

Este documento visa demonstrar, de acordo com a liberação do layout 2.2 do eSocial, quais foram as evoluções que ocorreram nos dados cadastrais e na geração da Carga Inicial de Dados XML.

As evoluções foram realizadas nos eventos:

* **S-1000**–******Informações do Empregador/Contribuinte**
* **S-1005**–******Tabela de Estabelecimentos e Obras de Construção Civil (Cadastro de Seção e Tomador de Serviço)**
* **S-1010**–******Tabela de Rubricas (Cadastro de Eventos)**
* **S-1020**–**Tabela de Lotações Tributárias (Cadastro de Seção)**
* **S-1030**–**Tabela de Cargos (Cadastro de Função)**
* **S-1050**–**Tabela de Horários/Turnos de Trabalho**
* **S-1070**–**Tabela de Processos Administrativos/Judiciais**
* **S-2100**–**Cadastramento Inicial do Vínculo (Cadastro de Funcionário)**

---

Evoluções]]>

# S-1000 - Informações do Empregador/Contribuinte

Para um melhor entendimento, as alterações exercidas em cima do cadastro de "Informações do Empregador", se encontram dividas em grupos, sendo eles Exclusão, Inclusão e Alteração.

O cadastro de Informações do Empregador pode ser localizado pelo caminho Folha de Pagamento | eSocial | Informações do Empregador.

## **1. Exclusões**

De acordo com o novo layout do eSocial (2.2), o agrupador "Processo alteração alíquota FAP", contendo os campos tipo e número do processo,  foi removido do cadastro de "Informações do Empregador".

## **2. Edições**

* + - Valores da tabela “Natureza Jurídica”.

Nos itens que são apresentados no campo "Natureza Jurídica", foram adicionadas os seguintes códigos:

* + 232-1 - Sociedade Unipessoal de Advogados
  + 233-0 - Cooperativas de Consumo
  + 331-0 - Demais Condomínios

* + - O campo "Ministério" que se encontra na aba "Informações Complementares" teve sua descrição alterada para "Sigla e nome do Ministério ou Lei que concedeu o Certificado" e deixou de ser um lookup, passando a permitir um texto com no máximo 30 caracteres.   
      Obs.: O campo será habilitado apenas se a Classificação Tributária for 80 - Entidades Beneficentes/Isentas.  
        
      Antes  
        
        
      Depois

* + - Campo "Indicativo acordo de multa" se tornou obrigatório quando a Classificação Tributária for 60 - Missão Diplomática ou Repartição Consular de Carreira Estrangeira.

## **3. Inclusões**

* + - Foi adicionado o campo "Entidade educativa sem fins lucrativos", ou seja, entidades que visam  a assistência ao adolescente e à educação profissional (art. 430, inciso II, CLT). (Campo eSocial: indEntEd)

 

* + - Empresa de Trabalho Temporário e Registro no Ministério do Trabalho (Campo eSocial: indEtt  e nrRegEtt  respectivamente)

---

# S-1005 - Tabela de Estabelecimento

As modificações realizadas para o evento S-1005, podem ser encontradas dentro do cadastro de Seção, pelo caminho Folha de Pagamento | Administração de Pessoal | Seções.

## **1. Edições**

A validação em torno do valor "FAP" (Fator Acidentário Previdenciário) que ocorre ao gerar o XML, foi alterado de acordo com o novo layout e irá se comportar da seguinte maneira:

* + - Se o valor "FAP" estiver fora da faixa 0,5 a 2,0 será gerada mensagem de erro.

Observações:

1. Independentemente se existir ou não alerta relacionado ao "FAP" o XML será gerado normalmente.
2. Será considerado o valor (FAP) informado para o estabelecimento (anexo cadastro seção). Se não existir valor definido para "FAP" no estabelecimento, será considerado o valor fixo.  
     
   Anexo Seção  
     
     
     
   Valor Fixo   
     
    Caminho: Folha de Pagamento | Administração de Pessoal | Cálculos | Valores Fixos.

* + - O processo jurídico deverá ser informado dentro do cadastro da seção, aba eSocial.

Caminho: Folha de Pagamento | Administração de Pessoal | Seções | aba eSocial | campo Processo alteração alíquota FAP

## **2. Inclusões**

* + - O campo "Código de Suspensão" foi acrescentado aos cadastros que envolvem o processo judicial ("Processo alteração alíquota RAT" e "Processo alteração alíquota FAP") no cadastro de Seção.

Observações:

a) Será permitido digitar um valor (máximo 14 caracteres alfanuméricos) diferente dos contidos na lista, caso não exista nenhum processo selecionado no Vitae.

b) Ao selecionar um processo no "Vitae", a lista do campo "Código de Suspensão", irá apresentar como opção apenas os códigos de suspensão associados ao processo.

c) O campo referente ao código de suspensão no cadastro de Seções, quando preenchido da lista do cadastro de Processos Jurídicos do Vitae, poderá ser limpo ou editado com outro código que não existe do cadastro de processos jurídicos.

* + - O agrupador **"Informações relacionados à contratação de aprendiz"**será adicionado à aba eSocial do cadastro de Seção contendo os seguintes campos:

1. **Contratação de aprendiz****-** O campo foi adicionado junto a uma lista de valores pre-definidos, podendo optar por:   

   0 - Dispensado de acordo com a lei;  
   1 - Dispensado, mesmo que parcialmente, em virtude de processo judicial;  
   2 - Obrigatório.  
     
   Obs.: Caso seja optado pela opção "Dispensado, mesmo que parcialmente, em virtude de processo judicial", o número do processo será de preenchimento obrigatório.
2. ****Contratação por intermédio de entidade educativa******-** Também será possível informar se o estabelecimento realiza contratações de aprendizes por intermédio de entidade educativa sem fins lucrativos, para isso, basta assinalar a flag em questão.
3. **CNPJ de entidades educativas** **-** Foi criado o anexo em questão dentro do cadastro de Seções, permitindo que seja incluso CNPJ's das entidades educativas.

* + - O Agrupador **"****Informações sobre a contratação de pessoa com deficiência (PCD)****"** foi adicionado à aba eSocial no cadastro de Seção, onde:

**Indicativo de contratação de PCD****-** O campo foi adicionado junto a uma lista de valores pre-definidos, podendo optar por:   
0 - Dispensado de acordo com a lei;  
1 - Dispensado, mesmo que parcialmente, em virtude de processo judicial;  
2 - Com exigibilidade suspensa, mesmo que parcialmente em virtude de Termo de Compromisso firmado com o Ministério do Trabalho;  
3 - Obrigatório.

Obs.: Caso seja optado pela opção "Dispensado, mesmo que parcialmente, em virtude de processo judicial", o número do processo será de preenchimento obrigatório.

 

---

# S-1010 - Tabela de Rubricas

Para o evento S-1010, as modificações se encontram dentro do Cadastro de Eventos - Administração de Pessoal.

## **1. Edições**

* + - Os campos Tipo Processo, Número Processo e Extensão da decisão/sentença que se encontravam dentro da aba "Inc. Proventos" no cadastro de Eventos, foram movidos para o novo Anexo "Processo de Suspensão de Incidência".

Obs.: Para maiores informações sobre o novo anexo, favor fazer a leitura do tópico**"S-1010, Inclusões"****.**

**Antes**  
  
  
**Depois**

## **2. Inclusões**

* + - Foi feita a criação do anexo "**Processo de Suspensão de Incidência**".

Para que o mesmo fique disponível para acesso, deverá ser dado permissão no item [01.01.32.01.15] Processo de Incidência de Suspensão no perfil vinculado ao usuário  
Obs.: A permissão é dada através do caminho Serviço Globais | Segurança | Perfis.  
  
  
Conforme já dito no tópico **S-1010 Edições**, o anexo em questão foi criado com o intuito de agrupar os campos Tipo Processo, Número Processo e Extensão da decisão/sentença.

Informações relevantes sobre os campos:  
**- Tributo:** Deverá optar por INSS, IRRF, FGTS, Contribuição Sindical.  
**- Número do Processo:**A Lupa irá busca o processo cadastrado no vitae, caso utilizado, o campo "Tipo do processo" e "Código do indicativo da suspensão" serão preenchidos automaticamente.

* + A lupa de busca de processos só estará disponível caso exista integração com o VITAE.
  + Somente retornará processos que serão enviados para o e-social (Campo "Processo da empresa contra órgão governamental envolvido no eSocial").
  + Se o tributo não for informado ou seja do tipo INSS, o sistema retornará os processos do tipo "Administrativo e Judicial".
  + Caso o tributo seja diferente do tipo "INSS", o sistema retornará os processos do tipo "Judicial".

**- Extensão da Decisão/Sentença:** Será de preenchimento obrigatório quando tributo for do tipo INSS.  
**- Tipo do Processo:** Deverá ser Judicial ou Administrativo quando o tributo for INSS, para os demais tributos, será como default Judicial.  
Obs.:Os campos Extensão da Decisão/Sentença e Tipo do Processo só serão habilitados quando o tributo for igual a "INSS".

---

# S-1020 - Tabela de Lotações

As modificações realizadas no evento S-1020 (Cadastro de Seções e Cliente/Fornecedor), de acordo com o layout 2.2, são:

Obs.: Os cadastros de seção e cliente/fornecedor, podem ser encontrados na guia Administração de Pessoal.

## **1. Inclusões**

* No cadastro de tomador de serviço (CLI/FOR) e Seções, foi adicionado o "Código de recolhimento suspenso para terceiros (Campo eSocial: codTercsSusp)  
  O campo tem como objetivo informar o código combinado dos Terceiros para os quais o recolhimento está suspenso em virtude de processos Judiciais.   
  Exemplo: Se o contribuinte possui decisões de processos para suspensão de recolhimentos ao Sesi (0008) e ao Sebrae (0064), deve informar o código combinado das duas entidades, ou seja, 0072.  
    
  + Seção
  + Tomador de serviço (Cliente/Fornecedor)

* + - Código de suspensão (codSusp)

O campo foi adicionado dentro dos cadastro de Seções, onde deverá ser informado o código do indicativo de suspensão.

---

# S-1030 - Tabela de Cargos

Nenhuma alteração realizado no evento S-1030 de acordo com o layout 2.2.

---

# S-1050 - Horários e Turnos

Nenhuma alteração realizado no evento S-1030 de acordo com o layout 2.2.

---

# S-1070 - Processos Jurídicos

As modificações realizadas no evento S-1070 (Processos Jurídicos - RM Vitae), de acordo com o layout 2.2, são:

Obs.: O menu de processos jurídicos se encontra dentro de Gestão de Pessoas | Gestão Organizacional | Processos Jurídicos.

## **1. Exclusões**

Na aba "Identificação", presente no cadastro de Processos Jurídicos, os campos "Indicativo de Suspensão da Exigibilidade", "Data da Decisão" e "Depósito do Montante Integral" foram removidos.

Antes

Depois

## **2. Inclusões**

* + - Criação do campo "**Indicativo da matéria do processo ou alvará judicial**".

* + - Criação do anexo "**Suspensão de exigibilidade de tributos e FGTS devido processo judicial**", onde armazenará informações de suspensão de exigibilidade de tributos e FGTS em virtude de processo judicial.   
      Obs: Só deve ser preenchido este grupo se o processo se refere a contestações relacionadas a contribuição previdenciária, IRRF e FGTS.

* + - Para que o anexo fique disponível para acesso, deverá ser dado permissão no item [05.03.01.01.18] Suspensão de exigibilidade de tributos e FGTS devido processo judicial no perfil vinculado ao usuário  
      Obs.: A permissão é dada através do caminho Serviço Globais | Segurança | Perfis.

---

# S- 2100 - Cadastramento Inicial do Vínculo

As modificações especificadas no layout 2.2 do eSocial em relação ao cadastro de Funcionários (Folha de Pagamento | Administração de Pessoal | Funcionários), são:

## **1. Edições**

* + - No cadastro de Trabalhador Temporário, a descrição do campo “Motivo da contratação de trabalhador temporário (mtvContrat)” foi alterado para “Hipótese legal para contratação de trabalhador temporário (hipLeg)”.

**Antes**

**Depois**

* + - A validação do campo CPF no cadastro de dependentes foi alterado, passando a ser necessário o preenchimento do mesmo caso o dependente tenha mais que 14 anos.  
      Observações:

1. 1. 1. 1. Não poderá existir CPF repetido nos dependentes.
         2. O CPF do dependente não pode ser igual ao CPF do empregador quando o empregador for pessoa Física.

* + - Na aba "Situação" dentro do cadastro de funcionário, o campo "Tipo de Regime Previdenciário" teve a descrição do item 3 alterada.

**Antes**  
  
  
**Depois**

* + - Para os funcionários que possuir mais de uma sucessão de vínculo, o campo "Data Início Vínculo (Campo eSocial: dtIniVinculo)" deverá retornar a data inicial do vínculo (data da primeira admissão).  
      Obs.: Apenas será apresentada a aba em questão, se o tipo de admissão do funcionário for "T - Ent Transf sem ônus p/ Cedente".

* + - Na aba "Registro", o campo "Data Final do Contrato (Campo eSocial: dtTerm)" teve sua validação alterada, permitindo que seja preenchido a data de admissão como data final do contrato.  
      Obs.: O campo **deverá** ser preenchido caso a flag "Contrato com Prazo" seja marcado.

## **2. Inclusões**

* + - Na aba de "Trabalhador Temporário", que se localiza dentro do menu "Registro", foi implementado o campo "Justificativa para a Contratação (Campo eSocial: justContr)".  
      O campo tem como objetivo armazenar a descrição do fato determinado que, no caso concreto, justifica a hipótese legal para a contratação de trabalho temporário.   
      Obs.: O prazo de contratação do trabalho temporário deve ser compatível com o motivo justificador alegado.

* + - Ainda na aba de Trabalhador Temporário, foi implementado também o campo "Tipo de Inclusão do Contrato (Campo eSocial: tpInclContr), podendo optar por:

1. 1. 1. 1. Locais sem filiais;
         2. Estudo de mercado;
         3. Contratação superior a 3 meses.

* + - No menu Salário / Jornada foi feita a implementação da opção "**Contrato de trabalho em regime de tempo parcial**", onde representará que a jornada semanal não irá exceder 25 horas semanais. (Campo eSocial: tmpParc)".
    - Foi implementado a validação para verificar se o dependente possui plano de saúde em cima do campo " Assistência Médica (Campo eSocial: depPlan)".
    - No cadastro de Dependentes, o campo "Grau de parentesco", passará a validar se o dependente possui incapacidade física ou mental para o trabalho.   
      A validação irá ocorrer em cima das opções 3 e N, retornando ao XML como "SIM" (Possui incapacidade) caso optado por elas
    - O campo "Preenche cota de PCD (Campo eSocial: infoCota)" foi criado para informar se o trabalhador irá preencher ou não, cota de pessoas com deficiência

---

divs
