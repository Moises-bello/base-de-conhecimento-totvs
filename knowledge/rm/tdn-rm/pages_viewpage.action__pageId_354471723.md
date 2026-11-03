---
content_hash: 992e3746b5dd1e4ff8616c0c7f4724f5519187bc0a18d4887b9255c8436623bc
fetched_at: '2026-06-29T00:08:57.736761+00:00'
page_id: '354471723'
product: rm
source: tdn-rm
title: 02 - Validações Pré-Matrícula - ES
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354471723
version: 30
---

**Este Menu está disponível apenas para o contexto ENSINO SUPERIOR.**

Este step tem como objetivo realizar as validações pré-matrícula do cadastro do aluno, parametrizadas previamente no sistema.

Aviso

As parametrizações sobre a matrícula já devem ter sido configuradas para que o curso apareça, assim o aluno deverá selecionar o mesmo e o portal realizará as validações parametrizadas.

Estas validações são referentes à Habilitação/Período Letivo em que o aluno está realizando a matrícula no ensino superior. Estas validações podem ser apenas informativas ou de bloqueio da matrícula.

As validações realizadas são:

* Verifica débitos financeiros no Educacional;
* Verifica a Conta Corrente do aluno;
* Verifica débitos financeiros na biblioteca;
* Verifica Documentos Pendentes;
* Verifica Ocorrências do aluno;
* Verifica a existência de um Plano de Pagamento válido para geração do contrato financeiro.

**Realizando a parametrização das validações**

 **Educacional| Configurações| Parâmetros| RM Portal| Matrícula| Geral 4/5 e Geral 5/5**

Após parametrização, acessar o Novo Portal do Aluno, e após avançar a tela de Apresentação da matrícula será exibido os cursos disponíveis do aluno, onde será realizado as validações parametrizadas.

 **Portal | Matrícula| Período Letivo**

Para utilizar corretamente o bloqueio por débitos financeiros, da biblioteca ou do portal, deve seguir o seguinte passo:

Ao marcar nos parâmetros para bloquear débitos financeiros e/ou bloquear alunos com débitos na biblioteca, conforme prints abaixo:

**Educacional| Configurações| Parâmetros| RM Portal| Matrícula| Geral 4/5 e Geral 5/5**

Será habilitado no cadastro de situação de matrícula, a opção "Validar inadimplência de aluno na matrícula pelo portal", para que a instituição parametrize quais situação de matrícula iram validar a inadimplência.

 **Educacional| Currículo e Oferta| Situação de matrícula| Aba Status no período letivo**

Quando os dois parâmetros estiverem marcados e o aluno com a situação de matrícula correta, tentar realizar a matrícula, ele será barrado por inadimplência.

**Assinatura de contrato através da confirmação "Li e aceito"**

Estando a assinatura de contrato habilitada para a matrícula pelo portal, e o tipo de assinatura configurado sendo o "Li e Aceito", somente o usuário responsável financeiro do aluno e/ou o usuário responsável financeiro do contrato do aluno é que poderão realizar a matrícula para o respectivo aluno e/ou curso/habilitação do aluno, independentemente de estarem parametrizados para acessar os dados acadêmicos ou não.

Caso o usuário logado no portal não seja nenhum desses tipos citados anteriormente, a seguinte mensagem será exibida ao selecionar o curso/habilitação do aluno para a matrícula, impedindo o usuário de prosseguir no processo de matrícula:

**OBS**: A partir da versão 12.1.2502.124,  caso o aluno seja seu próprio responsável financeiro (ou seja, aluno e responsável financeiro tenham o mesmo CPF e nome) e o registro do responsável financeiro do aluno não tenha um usuário gerado e o usuário logado no portal seja o do Aluno, o aluno conseguirá prosseguir com a matrícula.

Versões anteriores

Até as versões **12.1.2402.241, 12.1.2406.179, 12.1.2410.114****,** o usuário logado com permissão à página de matrícula poderia realizar a matrícula.

Para que esse comportamento seja mantido, foi disponibilizado o seguinte parâmetro nas versões superiores às citadas anteriormente:

**A partir da versão 12.1.2502 esta configuração não estará mais disponível e o comportamento atual do sistema é que estará em vigor.****Ou seja, somente o responsável financeiro pode realizar a matrícula.**
