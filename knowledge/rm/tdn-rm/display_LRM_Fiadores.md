---
content_hash: f8ee900d9ecec07e519b9f1eff9c37538e42951ea48e2b94746abb251f186482
fetched_at: '2026-06-29T00:11:05.435474+00:00'
page_id: '631010125'
product: rm
source: tdn-rm
title: Fiadores
type: documentation
url: https://tdn.totvs.com/display/LRM/Fiadores
version: 55
---

Índice

## **01. Visão Geral**

Disponível apenas para o nível de ensino **superior,** a partir do patch ****12.1.33.****

Com intuito de tornar os processos de matrícula e rematrícula mais digitais, o TOTVS Educacional passa a ter, também, o controle de fiador do aluno para os cursos que possuírem essa exigência. 

O modelo de assinatura eletrônica de contratos, integrado com o , vem, de forma digital, facilitar a assinatura do contrato de seus alunos e seus assinantes.

## **02. Documentos exigidos do Fiador**

**Acesse:** Currículo e Oferta | Oferta | Parametrização por curso | Anexo - Documentos exigidos do fiador

Documentos que serão solicitados ao fiador do aluno, podendo ser obrigatórios ou não, caso a  esteja configurada para que seja exigido um fiador, através do parâmetro **"exige fiador"**.

Para saber mais sobre o cadastro .

## **03. Parametrização por curso**

**Acesse:** Currículo e Oferta | Oferta | Parametrização por curso

Para cada curso ofertado, no período letivo, será possível indicar se o mesmo irá exigir um fiador para o aluno. Essa exigência é possível através do campo **"exige fiador"**, no cadastro da .

Ao se definir a exigência de um fiador, a matrícula irá exigir a informação de um fiador para o aluno/responsável e que o mesmo faça o upload dos .

A partir do patch **12.1.33,**o processo que efetua a , também, irá realizar a cópia dos  de uma parametrização para outra.

A partir do patch **12.1.33,**o processo que efetua a criação da , também, permitirá adicionar os  e definir a sua exigência.

 

## **04. Cadastro de fiador**

**Acesse:** Financeiro / Contábil | Contratos | Fiadores ou Currículo e Oferta | Aluno e Professor | Alunos | Anexo - Fiador

É possível cadastrar o fiador pelo TOTVS Educacional ou pelo .

Para mais detalhes sobre este cadastro no TOTVS Educacional () e para o Novo Portal do Aluno ().

Vale lembrar que, somente, será possível informar um fiador no  se a  **exigir fiador**.

A partir da versão ****12.1.33,**** será possível limitar a quantidade máxima de fiadores por contexto, em ***Configurações | Parâmetros | Tesouraria | Passo 3***.

O parâmetro **"Quantidade máxima de fiador(es) permitida"** deverá ter ter no mínimo um fiador e no máximo quatro fiadores configurados.

Tanto o Novo Portal do Aluno quanto o TOTVS Educacional irão obedecer este parâmetro, ele é válido tanto para fiadores globais como para fiadores com matriz aplicada preenchido.

Exemplo:

Dado uma quantidade máxima de 2 fiadores, um aluno com dois cursos Sistema de Informação e Ciência da Computação poderá ter 4 fiadores aprovados, sendo 2 para o curso de Sistemas e 2 para o curso de Ciência da Computação.

Fiadores reprovados e inativos não entram na quantidade máxima.

Exemplo: Dado uma quantidade máxima de 3 fiadores, poderá ter 2 fiadores aprovados ou em analise e 1 reprovado.

## **05. Documentos do fiador**

**Acesse:** Financeiro / Contábil | Contratos | Fiadores | Anexo - Documentos ou Currículo e Oferta | Aluno e Professor | Alunos | Anexo - Fiador | Anexo - Documentos

Neste anexo é possível inserir os documentos que foram solicitados para o fiador. Para mais detalhes sobre este cadastro .

## **06. Controle do Fiador na Matrícula**

A partir da versão **12.1.33** será possível solicitar o fiador para o aluno durante a realização da matrícula para o período letivo. Para isso é necessário que o campo **Exige Fiador** no cadastro da   do aluno esteja marcado.

A  no período letivo poderá bloquear a matrícula ou alteração da mesma caso o parâmetro **bloqueia alteração para este status por falta de fiador aprovado** presente na aba **período letivo** esteja marcado.

Vale ressaltar que todos os processos presentes no sistema TOTVS Educacional que realizam alteração da situação de matrícula irão considerar a configuração do parâmetro **bloqueia alteração para este status por falta de fiador aprovado.**

Entretanto, foi criado o parâmetro **matricular alunos sem fiadores aprovados**para desconsiderar as configurações relacionadas à exigência do fiador e o bloqueio de alteração para status por falta de fiador aprovado. Este parâmetro está presente na aba **matrícula/rematrícula/transferência** no anexo  **parâmetros educacionais**no cadastro do perfil do usuário. Com esse parâmetro marcado será possível matricular o aluno mesmo que o fiador não esteja aprovado., entretanto será exibida uma mensagem de alerta para o usuário. Vale ressaltar que este parâmetro especial vale apenas para o RM.exe, não é válido para o portal do aluno.

Os alunos que tenham 100% de bolsa incondicional e/ou desconto incondicional a exigência do fiador poderá ser facultativa, caso o novo parâmetro **não exigir fiador em caso de alunos com 100% de bolsa / desconto** esteja marcado. Esse novo parâmetro se encontra no menu Configurações → Parâmetros → RM Portal → RM Portal  → Matrícula → Portal - Matrícula / Geral 1/6.

ATENÇÃO

O novo parâmetro **não exigir fiador em caso de alunos com 100% de bolsa / desconto** está disponível a partir do patch **12.1.33.207** da versão 12.1.33

É importante frisar que a regra de bloqueio ocorrerá se o aluno:

* Não tiver nenhum fiador cadastrado.
* O parâmetro **não exigir fiador em caso de alunos com 100% de bolsa / desconto**marcado, porém não ter 100% de bolsa incondicional e/ou desconto incondicional.
* O parâmetro **não exigir fiador em caso de alunos com 100% de bolsa / desconto** desmarcado

## **07. Controle de Validade do Fiador**

A partir da versão **12.1.33** será possível definir se o aluno precisará renovar a validade do fiador e o momento que isso deve acontecer. Essas regras irão ter impacto na visibilidade da etapa de fiadores que fica presente na .

Esse controle da validade dos fiadores é feito em ***Configurações | Parâmetros | Tesouraria | Passo 3***.

Por padrão, o sistema trabalha com o controle de fiadores feito por período letivo, que é o funcionamento dos fiadores antes da aplicação dessa mudança, contudo, é possível configurar o sistema para fazer o controle através de 3 modos:

* **Válido para todo o curso**: o passo do fiador na rematrícula será exibido somente quando o aluno não tiver fiador ativo previamente cadastrado;
* **Válido por período letivo**: o passo do fiador sempre será exibido na rematrícula online. Nesse caso, o sistema traz os fiadores já cadastrados para o período letivo anterior para este aluno, permitindo que o aluno confirme ou troque os fiadores;
* **Verificar inadimplência do aluno**: se o aluno tiver alguma inadimplência ou não tiver nenhum fiador ativo previamente cadastrado, o sistema traz os fiadores já cadastrados anteriormente, permitindo que o aluno confirme ou troque, senão, o passo do fiador na rematrícula não é exibido.

## **Informações Complementares**
