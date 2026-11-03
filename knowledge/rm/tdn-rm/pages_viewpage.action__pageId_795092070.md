---
content_hash: a694d55e95cbf9536587c64a5fa187bb51c9d632f2b48c010ca337479ade04ce
fetched_at: '2026-06-29T00:11:42.693898+00:00'
page_id: '795092070'
product: rm
source: tdn-rm
title: Contratação de Aprendiz - Leiaute S-1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795092070
version: 10
---

false

**A partir das Versões:**

* 12.1.2302.235
* 12.1.2306.182
* 12.1.2310.116 e superiores

# Objetivo:

---

O objetivo deste documento é apresentar como realizar a contratação de um Aprendiz seguindo as regras do Leiaute S-1.2

---

O aprendiz pode ter sua contratação efetivada de duas maneiras: contratação direta ou indireta, sendo elas:

**Contratação direta**

É aquela realizada entre o estabelecimento obrigado ao cumprimento da cota e o aprendiz, como típica relação de emprego com contrato especial de aprendizagem. Nessa modalidade de contratação, a entidade de formação profissional integra a relação jurídica apenas como parte responsável por proporcionar a formação teórica prevista no programa de aprendizagem, de forma que o estabelecimento cumpridor da cota é quem mantém a condição de empregador do aprendiz. Nesses casos, portanto, a própria empresa contratante é quem deverá enviar o evento de admissão do aprendiz (indicando, como local de trabalho, o CNPJ completo do estabelecimento da empresa onde exercer suas atividades), além das demais informações sobre a relação empregatícia, como alterações contratuais, afastamentos, remunerações, desligamento etc.

**Contratação indireta**

 A entidade de formação profissional assume a condição de empregador do aprendiz. São autorizadas a atuarem nesse tipo de contratação as **entidades sem fins lucrativos e as entidades de prática desportiva** que formalizarem contrato ou convênio nesse sentido com o estabelecimento que deve cumprir a cota. Nesses casos, a entidade que assume a condição de empregadora é quem deve enviar o evento de admissão do aprendiz (indicando, em campo próprio, o CNPJ do estabelecimento cumpridor da  
cota para o qual a contratação do aprendiz foi efetivada), além das demais informações sobre a relação empregatícia, como alterações contratuais, afastamentos, remunerações, desligamento etc. A única obrigação da empresa cumpridora da cota de aprendizagem com relação ao eSocial, nos casos de contratação indireta, será informar, no evento S-1005 (Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos), que a contratação de aprendizes daquele estabelecimento a ser cadastrado se dá por intermédio de entidade educativa sem fins lucrativos ou de prática desportiva, indicando o CNPJ da respectiva entidade.

Desta forma, abaixo serão apresentados em suas respectivas abas os eventos que devem ser enviados ao eSocial, juntamente com seus respectivos detalhamentos:

11Contração DiretaContração Direta

No caso de contratação direta, a empresa contratante **(responsável/cumpridora da cota)** deverá:

* Enviar o evento S-2200, indicando a categoria "103 - Empregado - Aprendiz" e preenchendo os campos "indAprend" (Indicativo da modalidade de contratação) e "cnpjEntQual" (CNPJ da entidade qualificadora).
* Todos os eventos relativos à relação de emprego do aprendiz devem ser fornecidos pela empresa (por exemplo, alterações contratuais, afastamentos, remunerações, desligamentos).

No cadastro do funcionário, no menu lateral "Registro", ao inserir o código de categoria eSocial como "103 - Empregador - Aprendiz", o sistema habilitará uma nova aba denominada "Dados do Aprendiz".

Nesta tela, em caso de contratação direta, você poderá informar:

* + - **Modalidade de Contratação** (<indAprend>) - Direta ou Indireta, sendo:

1 -**Contratação direta**: contratação do aprendiz efetivada pelo estabelecimento cumpridor da cota de aprendizagem

* + - CNPJ da **Entidade Qualificadora** (<cnpjEntQual> - no caso de contratação direta)

* + - O campo CNPJ do estabelecimento onde estão sendo realizadas as **atividades práticas**(<cnpjPrat>), deverá ser preenchido quando ocorrer uma das situações abaixo:

a) Modalidade alternativa de cumprimento de cota de aprendizagem (neste caso, informar o CNPJ da entidade concedente da parte prática);  
b) Realização das atividades práticas na empresa contratante do serviço terceirizado;  
c) Centralização das atividades práticas em estabelecimento da própria empresa, diverso do estabelecimento responsável pelo cumprimento da cota. 

Exemplo de geração do XML do evento S-2200 em caso de contratação direta:

Contratação IndiretaContratação Indireta

No caso de contratação indireta, a empresa contratante **(responsável/cumpridora da cota)** deverá:

* Enviar o evento S-1005 preenchendo o grupo "**infoEntEduc**" (Identificação da(s) entidade(s) educativa(s) ou de prática desportiva)

No cadastro da seção centralizadora, acessando o menu eSocial, o usuário deverá indicar se a contratação é obrigatória ou não. Em seguida, o usuário deve selecionar o parâmetro "Contrata aprendiz por intermédio de entidade educativa" localizado logo abaixo.

Em Anexos | CNPJs de Entidades Educativas, insira um novo registro e informe o número do CNPJ da entidade educativa sem fins lucrativos ou de prática desportiva.

Exemplo de geração do XML do evento S-1005 em caso de contratação indireta:

Já a **entidade educativa ou de prática desportiva** deverá:

* Enviar o evento S-2200, indicando a categoria "103 - Empregado - Aprendiz", preenchendo os campos "indAprend" (Indicativo da modalidade de contratação), "tpInsc" (Tipo de inscrição da entidade) e "nrInsc" (número de inscrição da entidade).
* Todos os eventos relativos à relação de emprego do aprendiz devem ser fornecidos pela empresa (por exemplo, alterações contratuais, afastamentos, remunerações, desligamentos).

No cadastro do funcionário, no menu lateral "Registro", ao inserir o código de categoria eSocial como "103 - Empregador - Aprendiz", o sistema habilitar uma nova aba chamada "Dados do Aprendiz".

Nesta tela, em caso de contratação indireta, você poderá informar:

* + - **Modalidade de Contratação** (<indAprend>) - Direta ou Indireta, sendo:

2 - **Contratação indireta**: contratação do aprendiz efetivada por entidades sem fins lucrativos ou por entidades de prática desportiva a serviço do estabelecimento cumpridor da cota 

* + - CPF/CNPJ do **empregador cotista** (<nrInsc> - no caso de contratação indireta)

* + - O campo CNPJ do estabelecimento onde estão sendo realizadas as **atividades práticas**(<cnpjPrat>), deverá ser preenchido quando ocorrer uma das situações abaixo:

a) Modalidade alternativa de cumprimento de cota de aprendizagem (neste caso, informar o CNPJ da entidade concedente da parte prática);  
b) Realização das atividades práticas na empresa contratante do serviço terceirizado;  
c) Centralização das atividades práticas em estabelecimento da própria empresa, diverso do estabelecimento responsável pelo cumprimento da cota. 

Exemplo de geração do XML do evento S-2200 em caso de contratação indireta:

Desobrigada de cumprimento da cota

Conforme Manual de Orientações do eSocial (MOS), caso o declarante estiver **desobrigado do cumprimento da cota, ainda que parcialmente, por força de decisão judicial**, deverá gerar no evento S-1005 o grupo "**infoApr**" (Informações da contratação do aprendiz) e seu respectivo campo "**nrProcJud**" (Nº do processo judicial). 

No cadastro da seção centralizadora, acessando o menu eSocial, o usuário deverá indicar se a contratação é obrigatória ou não. Em seguida, o usuário deve selecionar a opção "**Dispensado, mesmo que parcialmente, em virtude de processo judicial**"  para que seja habilitado o campo "**Processo da Dispensa**". Não há necessidade de envio do S-1070 com o processo, conforme MOS.
