---
content_hash: 7e1de1bf546d29506dceea268093e441b4781ca1dc36058e2f91736e35cf05de
fetched_at: '2026-06-29T00:09:31.892241+00:00'
page_id: '425458772'
product: rm
source: tdn-rm
title: Atualização do log das turmas/disciplinas sugeridas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458772
version: 5
---

---

O processo de importação das informações do Urânia para as tabelas temporárias do TOTVS Educacional executa várias validações e a partir dessas o sistema pode registrar logs com status "Pendente" ou "Aviso".

Os logs com status "Aviso" não interferem na atualização das turmas, mas dependem de permissões e parâmetros a serem definidos no processo de importação definitiva para permitir ou barrar uma determinada atualização.

Já os logs com status "Pendente" devem ser resolvidos para que a atualização possa acontecer e existem dois caminhos:

1. Ajuste do problema no Urânia, seguindo este caminho o usuário deverá realizar outra importação para as tabelas temporárias.
2. Ajuste do problema no TOTVS Educacional que não requer uma nova importação para as tabelas temporárias.

É justamente para o cenário de ajuste no TOTVS Educacional que é executado o processo para atualizar o status dos logs da importação do Urânia.

Ao selecionar as turmas/disciplinas e executar o processo todas as validações realizadas no processo de importação são refeitas podendo gerar os seguintes resultados:

* Itens que estavam pendentes no log podem passar a resolvidos;
* Itens de avisos podem passar a resolvidos caso não sejam mais encontrados;
* Novos itens podem ser incluídos no log.

**Exemplo**

Ao executar a importação para tabela temporária foi listado o log que "Professor '00400' inexistente no TOTVS Educacional" com status Pendente.  
 Cenário 1:

* Alterado do código do professor no Urânia
* Refazer a Importação

Cenário 2:

* Cadastrar um novo professor com código 00400
* Executa o processo de atualização do status dos logs da importação do Urânia
* O log "Professor '00400' inexistente no TOTVS Educacional" passa ao status para Solucionado
