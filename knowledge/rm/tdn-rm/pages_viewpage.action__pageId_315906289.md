---
content_hash: 8df2673f96fcbfbf0226272a5638810310c3101eca7906b0816d89a8bc417ed9
fetched_at: '2026-06-29T00:08:46.230182+00:00'
page_id: '315906289'
product: rm
source: tdn-rm
title: 3. Validação Pré-Matrícula - EB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315906289
version: 38
---

**Menu disponível apenas para o contexto do Ensino Básico**

Aviso

As parametrizações sobre a matrícula já devem ter sido configuradas para que o curso esteja disponível

Estas validações são referentes a Habilitação/ Período Letivo em que o aluno está realizando a matrícula no Ensino Básico. Estas validações podem ser apenas informativas ou de bloqueio da matrícula.

* Verifica débitos financeiros no Educacional
* Verifica a Conta Corrente do aluno
* Verifica débitos financeiros na biblioteca
* Verifica Documentos Pendentes
* Verifica Ocorrências do aluno
* Verifica a existência de um Plano de Pagamento válido para geração do contrato financeiro

**Parametrização das Validações**

**Educacional | Configurações | Parâmetros | RM Portal | Matrícula | Geral 4/6**

Após parametrização acesse o Portal do Aluno e avance a tela de apresentação da matrícula, em seguida será exibido os cursos disponíveis do aluno onde é realizado as validações parametrizadas

**Portal | Matrícula | Período Letivo**

Para utilizar corretamente o bloqueio por débitos financeiros da Biblioteca ou do Portal, deverá ser marcado os parâmetros para bloquear débitos financeiros e/ou bloquear alunos com débitos na biblioteca, conforme prints abaixo:

Quando os parâmetros estiverem marcados e o aluno com a situação de matrícula correta, tentar realizar a matrícula, ele será barrado por inadimplência

**Educacional | Configurações | Parâmetros | RM Portal | Matrícula | Geral 4/6 e 6/6**

A partir da **versão 12.1.2402** é obrigatório parametrizar a Situação de Matrícula padrão para as Disciplinas da Matriz Curricular na P. Caso não seja parametrizado uma mensagem de validação será apresentada para o aluno conforme abaixo e não será possível avançar na matrícula.

O mesmo acontece se não parametrizar a Situação de Matrícula padrão para o Período Letivo também na

**Assinatura de contrato através da confirmação "Li e aceito"**

Estando a assinatura de contrato habilitada para a matrícula pelo portal, e o tipo de assinatura configurado sendo o "Li e Aceito", somente o usuário responsável financeiro do aluno e/ou o usuário responsável financeiro do contrato do aluno é que poderão realizar a matrícula para o respectivo aluno e/ou curso/série do aluno, independentemente de estarem parametrizados para acessar os dados acadêmicos ou não.

Caso o usuário logado no portal não seja nenhum desses tipos citados anteriormente, a seguinte mensagem será exibida ao selecionar o curso/série do aluno para matrícula, impedindo o usuário de prosseguir no processo de matrícula:

**OBS**: A partir da versão 12.1.2502.124,  caso o aluno seja seu próprio responsável financeiro (ou seja, aluno e responsável financeiro tenham o mesmo CPF e nome) e o registro do responsável financeiro do aluno não tenha um usuário gerado e o usuário logado no portal seja o do Aluno, o aluno conseguirá prosseguir com a matrícula.

Versões anteriores

Até as versões **12.1.2402.241, 12.1.2406.179, 12.1.2410.114,** o usuário logado com permissão à página de matrícula poderia realizar a matrícula.

Para que esse comportamento seja mantido, foi disponibilizado o seguinte parâmetro nas versões superiores às citadas anteriormente:

**ATENÇÃO: a partir da versão 12.1.2502 esta configuração não estará mais disponível e o comportamento atual do sistema é que estará em vigor. Ou seja, somente o responsável financeiro pode realizar a matrícula.**
