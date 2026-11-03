---
content_hash: b93613a4f2cfcc2ffeaa3cfd1a05e3e76230d72ff893d9149c9c4a2beaec311f
fetched_at: '2026-06-29T00:11:59.653303+00:00'
page_id: '874598653'
product: rm
source: tdn-rm
title: Negociação inteligente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=874598653
version: 35
---

Relatório do termo de aceite

A parametrização para o relatório do termo de aceite será configurada no campo "Relatório dos Termos do acordo", dentro da tela de "Template de Acordo".

Possibilidade de negociação de um ou mais títulos **vencidos** podendo gerar um ou mais títulos de acordo com a regra da negociação selecionada (template de acordo).

Para saber mais sobre negociação online consulte o link: [Negociação online](https://tdn.totvs.com.br/pages/releaseview.action?pageId=494962674)

Para saber mais sobre formas de negociação, consulte o link [Template de Acordo](https://tdn.totvs.com/display/LRM/Template+de+Acordo).

Permissão de acesso

Marcar a opção de negociação (botão "Negociar") na tela de extrato financeiro que só estará visível se o perfil do usuário permitir negociação online:

Importante

A exibição do **Menu de Pagamento** deve seguir algumas parametrizações, acesse as regras [clicando aqui](https://tdn.totvs.com/).

Seleção do títulos para negociação

Neste passo o usuário deverá selecionar os lançamentos/boletos que deseja negociar

ATENÇÃO

A seleção dos lançamentos/boletos para a negociação **deve ser sempre do mesmo aluno**. Assim a opção de "Negociar" ficará habilitada, caso seja **selecionado títulos de alunos diferentes** a opção "Negociar" não ficará habilitada.

### 

Simulação e Conferência da Negociação

Após o usuário selecionar os títulos vencidos para negociação, serão exibidos todos os títulos selecionados com o valor líquido de cada título bem como as formas de negociação disponíveis (templates de acordo) e seus respectivos valores.

Termo de Aceite

Caso a opção "Obter aceite dos Termos do Acordo" esteja marcada no cadastro do template será apresentado a etapa "Termo de Aceite" 

Confirmar Negociação

Na etapa seguinte, "Confirmação", caso esteja parametrizado, será apresentado o termo de aceite na tela para que o usuário leia e aceite. 

Nesta etapa será apresentado o relatório parametrizado conforme destacado na imagem.

Caso a opção "Obter aceite dos Termos do Acordo" **não esteja marcada**no cadastro da template, no app exibirá apenas a etapa de "Confirmação", sendo assim não irá solicitar o usuário o aceite do termo de negociação.

Seguir para Pagamento

Após ser feita a negociação, o usuário terá a opção de voltar para a página inicial ou realizar o pagamento da primeira parcela resultante do processo não sendo possível retornar para as etapas anteriores do processo já concluído.

**TABELAS UTILIZADAS**

* FTEMPLATEACORDO - Tabela principal de registros de templates de acordo
* FACORDO - Tabela com as negociações feitas (acordos)
* FACORDOREL - Tabela com os lançamentos participantes da negociação

]]>
