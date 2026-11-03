---
content_hash: 6373e749121116bffaf20137dbaa1cb9881413c3589f9e99e536280d64902a4a
fetched_at: '2026-06-29T00:08:37.209410+00:00'
page_id: '284879209'
product: rm
source: tdn-rm
title: Dados Pessoais
type: documentation
url: https://tdn.totvs.com/display/LRM/Dados+Pessoais
version: 11
---

Nessa página irá conter todas as informações do aluno como contato, endereço, curso, registro acadêmico, turno e toda sua identificação.

Para que possa ser visualizado no portal os dados pessoais do aluno, deve ser dado a permissão em seu perfil.

  **Acessar MDI I Menu | Serviços Globais| Perfil | Educacional (portal) | Acadêmico | Dados pessoais.** 

Após dar permissão, para o acesso no portal ir no canto superior direito onde encontra-se a foto do aluno e clicar nela, onde irá aparecer **‘Cadastro acadêmico’**. Segue:

Para que o aluno possa fazer alterações em seu cadastro vai depender da parametrização na MDI.

 **Acessar configurações|Parametros|RMPortal |Geral 1/18**

* Com a Opção ‘**Apenas consulta’** marcada, o aluno não poderá fazer nenhuma alteração em seus dados.
* Com a opção ‘**Solicitar alteração para a Filial do aluno**’ marcada, o aluno e o responsável acadêmico poderão fazer alterações, porém quando ele salva ainda fica as informações antigas e ele é informado que foi enviado para sua filial. É enviado as alterações para o e-mail cadastrado na filial do aluno e o responsável por receber estes e-mails na instituição deverá alterar no cadastro do aluno. Só assim ficará disponível para o aluno.  
  **Para cadastrar o e-mail na Filial do aluno basta acessar MDI/Fiscal/Filial/Anexos/Dados Educacionais.**
* Com a opção ‘**Solicitar alteração para o Nível de ensino do aluno**’ marcada, o aluno e o responsável acadêmico poderão fazer alterações, porém quando ele salva ainda fica as informações antigas e ele é informado que foi enviado para seu nível de ensino. É enviado as alterações para o e-mail cadastrado no nível de ensino do aluno e o responsável por receber estes e-mails na instituição deverá alterar no cadastro do aluno. Só assim ficará disponível para o aluno.  
  **Para cadastrar o e-mail do Nível de ensino do aluno basta acessar MDI/ Configurações/ Nível de Ensino.**
* Com a opção **‘Permitir Alteração’** marcada o aluno e o responsável acadêmico poderão fazer qualquer alteração em seus dados e salvar.

Foto do Aluno - Versões inferiores à 12.1.2502

A foto do aluno somente é possível incluir pela MDI no cadastro do aluno. No portal para sua visualização ela tem o tamanho máximo de 190x190px e dependendo do seu tamanho e formato (quadrada ou retangular) ela é ajustada para melhor visualização.

Para que o aluno possa fazer alteração da foto no portal vai depender da parametrização, bem como as permissões dadas no menu Dados pessoais [14.01.02].

Veja :

 **Acessar configurações|Parametros|RMPortal |Geral 1/18**

**Atenção!!!**

A fim de adequar ao eSocial (Legislação do Governo Federal), os dados relativos aos funcionários devem ser gerenciados pelo RH.  Portando não é permitido realizar alteração dos dados cadastrais do Aluno pelo portal do aluno, quando o mesmo for funcionário da instituição. Este tipo de alteração deve ser realizada pelo departamento da instituição de ensino responsável pela gestão dessas informações.

Neste caso, a seguinte mensagem será apresentada no Portal do Aluno: 

e os campos da área de Contato e Endereço do Aluno ficarão bloqueados para edição:

Essa atualização está disponível a partir das versões: **12.1.2205.171,1****2.1.2209.112 e 12.1.2302**.

Para garantir maior integridade cadastral, evitar inconsistências nos dados e reduzir erros em integrações fiscais e regulatórias, foi criada na parametrização da Secretaria a aba **"Endereço do Aluno"**, contendo os seguintes parâmetros:

* Cidade deve ser obrigatoriamente cadastrada no cadastro de municípios
* Aplicar regra apenas para endereços nacionais

Por padrão, os parâmetros não vêm selecionados. Ao marcar o primeiro parâmetro, o segundo é automaticamente marcado, permanecendo disponível para desmarcação, caso necessário.

Com o parâmetro ativado, o sistema não permite salvar a **descrição da cidade** caso ela não esteja previamente cadastrada no cadastro de municípios.

Quando o parâmetro **"Aplicar regra apenas para endereço nacional"** estivermarcado, a validação será aplicada somente aos endereços nacionais**.**

Para endereços estrangeiros, o sistema continuará seguindo o comportamento atual, permitindo informar a cidade livremente, sem a necessidade de que ela esteja cadastrada na lista oficial de municípios.

Ao desmarcar o parâmetro **"Aplicar regra apenas para endereço nacional"**, a regra também passa a ser aplicada aos endereços estrangeiros, exigindo que a cidade seja selecionada a partir do cadastro oficial de municípios.

Foram adicionados os seguintes campos ao formulário:

* Tipo de Rua
* Tipo de Bairro

### Regras de preenchimento

* Ao informar o **Logradouro**, o sistema passa a exigir o preenchimento do campo **Tipo de Rua**.
* Ao informar o **Bairro**, o sistema passa a exigir o preenchimento do campo **Tipo de Bairro**.

Disponível a partir das versões: 12.1.2506.313; 12.1.2602.152;12.1.2510.238
