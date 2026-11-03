---
content_hash: fbf7ba82958d5a4a873df956c7515ad98c3d3e69102cc284854879d53da3ae92
fetched_at: '2026-06-29T00:09:32.623712+00:00'
page_id: '425458887'
product: rm
source: tdn-rm
title: Parametrização por Curso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458887
version: 58
---

O cadastro de parametrização por curso é onde se define as configurações de oferta da matriz aplicada para um período letivo específico. Esse cadastro é dividido nas seguintes abas:

## **Identificação**

Nessa aba deve ser feito o relacionamento entre a matriz aplicada e o período letivo.

Observações

Ao configurar uma conta caixa no campo de mesmo nome existente dentro de Dados financeiros, se quiser utiliza-la como default, deve-se configurar o sistema em **Parâmetros | Educacional | Integração | Financeiro | Educacional | Geral 2/4 | Utilizar Conta Caixa → Default parametrizações por curso**.

## **Configuração de matrícula**

Nessa aba é feito toda configuração da matrícula na matriz aplicada e período letivo configurados na aba de identificação.

Observações

No ensino básico é o usuário poderá informar nessa aba um **Plano Modelo para Personalização**. No contrato do aluno deixe de informar o plano de pagamento, e habilitará um campo de personalização, neste o usuário poderá personalizar o plano de acordo com o pedido do responsável financeiro (Ex: O aluno quer pagar seu plano em apenas 2 pagamentos).

Matrícula via Central do Candidato

Os campos referente a data de matrícula via central do candidato serão utilizados somente quando a matrícula de um candidato aprovado pelo TOTVS Processo Seletivo e a matrícula for feita através do portal do processo seletivo.

Para mais informações acesse: 

Mudança de regra - Relatório RM Reports do contrato financeiro

A partir da versão **12.1.2209** será possível definir, para cada parametrização por curso, o relatório do RM Reports utilizado no contrato financeiro. Essa configuração terá precedência sobre a já existente no parametrizador [15.04 - RM Portal | 15.04.02 - RM Portal - Matrícula | Portal - contrato financeiro 1/4 | "Relatório RM Reports do contrato"], ou seja, se estiver preenchido na parametrização por curso, essa será utilizada. Caso o sistema não encontre o relatório configurado na parametrização por curso, será feita a leitura do parâmetro acima descrito.

Para as duas situações, o parâmetro "Utilizar Relatório do RM Reports" deverá estar marcado. Esse parâmetro está também disponível no caminho do parametrizador citado anteriormente.

Os processos "Copiar matriz aplicada para outro período letivo", do cadastro de parametrização por curso, e "Parametrização por curso em lote" do cadastro de período letivo, também foram adaptados para permitir informar o relatório do RM Reports a ser utilizado no contrato financeiro.

Assinatura Eletrônica - Parametrização do Documento do Diário de Classe

Essa funcionalidade estará disponível a partir da versão 12.1.2310

A Instituição de ensino, poderá definir o documento de diário de classe que será utilizado nas turmas/disciplinas e estará disponível no portal para os professores assinarem.

Ao informar o relatório no cadastro da Parametrização por curso, o mesmo documento estará disponível para a(s) Turma(s)/Disciplina(s) associada(s) a ela.

Copiar dados do contrato anterior na rematrícula 

À partir das versões 12.1.2410.296, 12.1.2502.202, 12.1.2506.146 e 12.1.2510, o parâmetro "Copiar dados do contrato anterior na rematrícula" foi incluído para que as informações referente ao tipo de bolsa e ao desconto por antecipação sejam copiados do contrato do período letivo anterior, na realização de uma rematrícula.

Informações que serão copiadas do contrato anterior:

Importante

Caso exista mais de um contrato com o tipo de contrato igual a **"Plano"**, no período letivo anterior, o processo de rematrícula irá criar o contrato, mas não irá realizar a cópia das informações do contrato anterior.

Assinatura do contrato obrigatória com TOTVS Assinatura Eletrônica na rematrícula

À partir das versões 12.1.2510.223, 12.1.2602.141 e 12.1.2606 o parâmetro "Assinatura do contrato obrigatória com TOTVS Assinatura Eletrônica na rematrícula" foi incluído para que, na realização da rematrícula no Portal do Aluno, seja obrigatória a assinatura eletrônica do contrato financeiro quando a habilitação da matrícula tenha essa configuração na parametrização por curso.  
É importante ressaltar que, esse parâmetro só ficará disponível, quando em Ambiente > Parâmetros > Educacional > RM Portal > Matrícula > Portal - Assinatura contrato, estiver marcado o parâmetro "Restringir obrigatoriedade apenas conforme configurado na 'Parametrização por curso'", conforme documentação .  
Seguindo a mesma regra, esse parâmetro está disponível também nos processos ,  e .

### Itinerário formativo

O campo **Utiliza agrupamento de itinerários formativos** (a partir da versão **12.1.2306**) define se na hora da matrícula será disponibilizado um grupo de itinerário para o aluno. Quando o agrupamento não é utilizado, ao efetuar matrícula em itinerários formativos será verificada a obrigatoriedade de mínimo e máximo de itinerários na própria tela de parametrização por curso. Quando o agrupamento é utilizado, a verificação de mínimo e máximo será feita no anexo de [agrupamento de itinerários formativos](https://tdn.totvs.com/x/5vAWLQ).

O campo **Min. itinerários** e **Max. itinerários** definem as quantidades mínima e máxima de itinerários formativos que o aluno pode se matricular dentro da matriz aplicada no período letivo. Esses campos ficarão habilitados apenas quando a matriz curricular parametrizada tiver pelo menos um itinerário formativo associado e não for utilizado agrupamento de itinerários.

O parâmetro **Exibir o itinerário formativo durante a matrícula no portal do aluno** tem por objetivo mostrar ou não a etapa de itinerário formativo na matrícula do portal do aluno.

À partir da versões 12.1.2306.174,12.1.2310.108 e 12.12402 foi incluído o parâmetro "Ocultar Quadro de Horários na matrícula através do Portal".

Ao marcar este parâmetro durante a realização da matrícula o quadro de horários permanece oculto.

Este parâmetro está disponível somente para o nível de ensino superior.

Ao marcar o parâmetro "Ocultar Quadro de Horários na matrícula através do Portal",  as informações dos horários da turma/disciplina também serão ocultadas na área de detalhes da turma/disciplina. Implementação disponível a partir da versões: 12.1.2306.245,12.1.2310.187,12.1.2402.123.

À partir da versões 12.1.2306 e 12.1.2310, a aba Itinerário formativo foi incluída para facilitar a configuração de informações referente ao Itinerário Formativo.

Ao marcar o parâmetro o "Utiliza escolha de turma/disciplinas ", durante a confirmação de matricula no portal o sistema permite realizar a escolha de turma/disciplinas no momento de escolher as disciplinas de itinerários.

Com ele habilitado no anexo da disponibilidade de Itinerário, o parâmetro "exibir disciplinas do itinerário formativo durante a matrícula no portal do aluno" e a "turma do itinerário formativo" ficam ocultos. desta forma a enturmação não ocorrerá em uma turma default e sim na turma/disciplina escolhida.

## **Movimento**

Nessa aba deve ser cadastrado as datas de competência do movimento contábil.

## **Disciplina**

Nessa aba é feito a configuração de datas relacionadas ao complemente de disciplina via Portal

**Configuração para sugestão de turma/disciplina (Ensino Superior)**

Ao marcar o parâmetro **Utilizar a sugestão de disciplina da parametrização do curso**, serão listadas todas as possíveis sugestões para visualização de disciplinas durante o processo de matricula. Fazendo as configurações nessa aba, durante o processo de matrícula, o usuário conseguirá visualizar no campo sugestões de disciplina as disciplinas de outro curso, de outro turno, outros níveis de ensino ou outra filial, etc.

Importante

Se nenhum parâmetro em configuração de sugestão de disciplinas for marcado, o sistema irá respeitar a marcação dos parâmetros de sugestão de disciplinas presente nos parâmetros do sistema.

## **Associar documentos exigidos do aluno á matriz aplicada**

A partir da versão 12.1.2510, foi incluído no processo a flag 'Validar documento pela inteligência artificial' .

Informações Complementares

---

[Documentos Exigidos](http://tdn.totvs.com/x/Mv1bGQ)

[Modelos de Etapa da matriz aplicada](http://tdn.totvs.com/x/1vtbGQ)

[Disponibilidade do Itinerário Formativo](https://tdn.totvs.com/x/VQx9IQ)

[Agrupamento de itinerários formativos](https://tdn.totvs.com/x/5vAWLQ)

Como Fazer

---

[Atualizar Etapas de Turma Disciplina](http://tdn.totvs.com/x/zfxbGQ)

[Atualizar campos da Parametrização por curso](https://tdn.totvs.com/x/i6QrLg)

[Copiar Modelo de Etapas para outro Período Letivo](http://tdn.totvs.com/x/NfxbGQ)

[Copiar Matriz Aplicada para Outro Período Letivo](http://tdn.totvs.com/x/NPxbGQ)

Veja Também

---

[HOW TO - Configuração da Sugestão de Disciplinas na Parametrização por Curso](https://youtu.be/72D66Ze63NI)
