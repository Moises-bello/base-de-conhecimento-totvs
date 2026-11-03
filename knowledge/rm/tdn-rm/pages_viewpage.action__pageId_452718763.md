---
content_hash: e7fb4da653aeb418e72203ad10a4f8b5792ef28f3006b3d95e550a69e626e4e0
fetched_at: '2026-06-29T00:10:01.527104+00:00'
page_id: '452718763'
product: rm
source: tdn-rm
title: Restrições Cadastrais da Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718763
version: 5
---

**Ativar controle de bloqueio de dados cadastrais da rescisão**

Ao preencher uma rescisão na competência atual ou futura estará automaticamente desbloqueada. O sistema irá incluir o funcionário automaticamente na tabela PFRESCDESBLOQUEADA.   
   
Ao liberar competência todos os Demitidos na competência atual terão os dados cadastrais da rescisão bloqueados para edição, além dos Demitidos em competências anteriores que tenham sido desbloqueados.  
   
No cadastro da rescisão ao tentar alterar qualquer dado de uma rescisão que esteja com seu cadastro bloqueado o sistema irá emitir a mensagem: "Os dados cadastrais para esta rescisão estão bloqueados."   
   
No Cancelamento da Rescisão será apresentado o aviso: "Funcionário 00004 está com os dados cadastrais da rescisão bloqueado." para cada funcionário que tenha sido bloqueado os dados cadastrais da rescisão.   
   
Na Rescisão Coletiva será apresentado o aviso: "Funcionário 00004 está com os dados cadastrais da rescisão bloqueado." para cada funcionário que tenha sido bloqueado os dados cadastrais da rescisão.   
   
No cadastro de funcionário mudando da situação "D" para "A" o sistema zera automaticamente os dados da rescisão não observando o controle de bloqueio de dados cadastrais da rescisão.  
   
Rescisão complementar continua com o mesmo comportamento alterando a data do último movimento.

**Estabilidade**

**Considerar o cadastro de estabilidade do funcionário**

Verifica se o funcionário possui alguma estabilidade cadastrada e retorna mensagem de informação quando for realizar demissão do funcionário. 

Desta forma, com o parâmetro marcado, não é mais verificado o cadastro CIPA e Representantes de funcionários no módulo TOTVS Segurança e Saúde Ocupacional. 

Parâmetro marcado, Parâmetro desmarcado, Passo 03, Passo 04passo1,passo2yespasso1

Parâmetro ' Considerar o cadastro de estabilidade do funcionário' marcado:

Funcionário com estabilidade Eleito Titular CIPA até 07/08/2027. A estabilidade não estar vinculada a um comissão de CIPA do módulo Segurança e Saúde Ocupacional:

Na aba Pendências demissionais a mesma é exibida:

nopasso2

Parâmetro 'Considerar o cadastro de estabilidade do funcionário' desmarcado:

Funcionário possui a estabilidade até dia 07/08/2024. A estabilidade não estar vinculada a um comissão de CIPA do módulo Segurança e Saúde Ocupacional:

A mesma não aparece em pendências demissionais:

Cadastrou a rescisão no período de estabilidade sem retornar a mensagem:

IMPORTANTE

* A adequação foi realizada nos cadastros de Rescisão Individual, Rescisão Coletiva e Cadastro Global
* Em nenhum dos processos/cadastro acima a rescisão será bloqueada quando existir estabilidade, retornando somente mensagem de aviso
* Caso o funcionário esteja afastado no período de estabilidade, continua não permitindo o cadastro da rescisão
* Para as estabilidades de CIPA ou representantes dos empregados abaixo, somente irá retornar mensagem se a rescisão for do tipo 2 e M.
  + 7 - Candidato CIPA
  + 8 - Eleito Titular CIPA
  + 9 - Eleito Suplente CIPA
  + 14 - Candidato Representante dos Funcionários
  + 15 - Eleito Titular Representante dos Funcionários
  + 16 - Eleito Suplente Representante dos Funcionários
* As demais estabilidades será retornada a mensagem de aviso para qualquer tipo de demissão

---
