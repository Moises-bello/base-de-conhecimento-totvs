---
content_hash: b3a06a69550da314639178a891446870001299b08f9cafd049b6a324e083a5aa
fetched_at: '2026-06-29T00:09:29.837701+00:00'
page_id: '425458305'
product: rm
source: tdn-rm
title: Criptografia de Senha dos Candidatos
type: documentation
url: https://tdn.totvs.com/display/LRM/Criptografia+de+Senha+dos+Candidatos
version: 4
---

Este Processo localizado nos "Parâmetros", foi criado para adaptar todo o sistema para trabalhar com senhas de candidatos criptografadas na base de dados. Em linha gerais funcioná da seguinte forma: Se o processo for rodado e o status atual do sistema for de senhas "não criptografadas", o processo criptografará todas as senhas de candidatos já existentes no banco e alterará o status do sistema para "criptografado". Assim, todos os novos cadastros de candidatos terão suas senhas criptografadas no momento da inscrição. Se o processo for aberto e o status for de senhas criptografadas, o processo não poderá ser executado novamente. Por default, quando nunca executado o processo, o sistema iniciará com o status "não criptografado". O sistema definirá o status de criptografia das senhas do candidato através da tabela "SPSPARAMETROGERAL na coluna IDPARAMETRO ='SENHACRIPTOGRAFADA'.  Este registro será global, ou seja, será aplicado para todas as coligadas do Processo Seletivo.

Este processo será **irreversível:** após as senhas serem criptografadas elas não poderão ser descriptografadas.

**Impactos:**

Os seguintes serviços do sistema foram adaptados, pois através do status de criptografia deverão decidir internamente se há a necessidade de validar a criptografia ou não na senha do candidato:

* Esqueci minha senha
* Alteração de senha
* Login
* Inscrição pela secretaria
* Envio de login

Quando a criptografia for ativa no sistema os serviços "Esqueci minha senha" e "Envio de login" criarão uma nova senha de usuário e esta será enviada por e-mail. Senão, caso não esteja com criptografia ativa no sistema, serão enviados aos usuários suas senhas originais.
