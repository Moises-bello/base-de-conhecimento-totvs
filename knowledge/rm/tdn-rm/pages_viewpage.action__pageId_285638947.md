---
content_hash: 4799da5123863efee187b091b9ab47f60a4fd165654e242f34824f351def7d45
fetched_at: '2026-06-29T00:08:38.180582+00:00'
page_id: '285638947'
product: rm
source: tdn-rm
title: Geral 3/3
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285638947
version: 9
---

Foram criados funcionalidades nos parâmetros do sistema para que seja possível o portal receber cadastros de candidatos e responsáveis estrangeiros:

**Obrigar o preenchimento de um dos campos (CPF, Passaporte ou Registro geral), caso estejam visíveis:** Caso essa opção seja marcada e os campos "CPF", "Passaporte" ou "Registro geral" estejam marcados como visíveis na aba "Visibilidade/Obrigatoriedade de campos" e se na inscrição o candidato escolher um País diferente do cadastrado na nacionalidade do processo seletivo, esses três campos ficaram obrigatórios, mas a partir do momento em que preencher um dos três campos, os outros ficaram como opcionais.

**Utilizar parametrização dos campos do grupo "Documentos" sem exigir obrigatoriedade:** neste campo será definido se o sistema irá exibir os campos de documentos que foram definidos para serem visualizados nos cadastros de responsáveis e de candidatos, porém, se algum destes campos forem obrigatórios, exclusivamente para estrangeiros não serão obrigatórios.  Se desabilitado, os campos continuam obrigatórios mesmo para candidatos estrangeiros.

**Nacionalidade do processo seletivo:** localizado na aba Gerais - será informado o país de nacionalidade do sistema.

**Exemplo:**

Se o sistema estiver parametrizado com nacionalidade do processo seletivo igual a "Brasil", ao informar no portal de inscrições o país natal do candidato, como "Nova Zelândia", por exemplo, o sistema irá entender que este candidato é estrangeiro e consultará a parametrização definida nos campos de passaporte para candidatos e responsáveis. Para mais informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=284883738#Formul%C3%A1riodeInscri%C3%A7%C3%A3o-Inscri%C3%A7%C3%A3ocomestrangeiros).

**Serviços disponibilizados na inscrição do portal:** Links úteis para o candidato que já está inscrito no processo seletivo. Quando o candidato clicar nesses links, se o candidato ainda não esteja logado no browser será redirecionado para a tela de login, assim que feito o login será aberto o serviço solicitado senão já será aberto o serviço automaticamente.

Importante

A "**Opção que será apresentada como primeiro da lista da seleção no portal"**estará disponível a partir da versão **12.1.2205** **Previsto(Maior/2022)**

**Opção que será apresentada como primeiro da lista da seleção no portal:**

Esses campos definem qual informação referente a "País", "Estado" e "Cidade" aparecerão como os primeiros itens da lista de seleção no portal nas seguintes localidades:

* Preenchimento das informações de naturalidade na inscrição do candidato.

* Preenchimento das informações do endereço na inscrição do candidato, nos responsáveis (pai, mãe, resp. fin, resp. acadêmico).

* Preenchimento das informações de naturalidade na matricula do candidato.

* Preenchimento das informações do endereço na matricula do candidato, nos responsáveis (pai, mãe, resp. fin, resp. acadêmico).
