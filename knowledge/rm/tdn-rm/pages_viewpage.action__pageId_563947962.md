---
content_hash: b7a6d51f79e547215c4026c5326f30ab221a605e44df6e02356f7c3b36ad1011
fetched_at: '2026-06-29T00:10:51.237067+00:00'
page_id: '563947962'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Empreendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563947962
version: 38
---

#FF9000Comissão

A partir da **versão 12.1.33** foi criada a visão de comissão que agrega todos os campos pertinentes ao cadastro de comissão.

Campos da visão de comissão

---

**Diretor:**O campo diretor do empreendimento permite associar um usuário como um diretor, facilitando a distribuição dos percentuais de comissão para estes agentes.

**Percentual de comissão do diretor:**Este campo definirá o percentual de comissão do gerente para o empreendimento em questão.

Importante: A comissão do diretor será sempre calculada à parte do rateio da comissão entre corretor e gerente e não influenciará este cálculo.

**Gerente:** O campo gerente do empreendimento permite associar um usuário do Portal de Imóveis ao empreendimento, facilitando fluxos de aprovação nas propostas.

**Percentual de comissão do gerente:** Este campo definirá o percentual de comissão do gerente para o empreendimento em questão.

Importante: Quando existe percentual de comissão do gerente cadastrado para um empreendimento o Portal de Imóveis irá sempre considerar este percentual de comissão para o gerente, independente se a comissão estipulada ao corretor foi zerada.

Não serão possível associar gerentes e diretores quando os mesmos são de grupos marcados como correspondentes bancários.

#FF9000Correspondentes Bancários

A partir da **versão 12.1.33**, foi criada a visão de correspondentes bancários do Empreendimento.

Esta visão permite selecionar os correspondentes bancários que pertencem ao empreendimento, bem como definir qual correspondente será o correspondente padrão deste empreendimento.

O correspondente padrão, quando definido nesta visão, será sempre selecionado automaticamente quando o corretor fizer uma proposta.

Importante: Somente os correspondentes do empreendimento serão apresentados para seleção na opção de correspondente bancário quando não houver correspondente padrão definido.#FF9000Documentos da Proposta

##### Envio de e-mails

---

Na aba de **Documentos Proposta**, foi adicionado um novo parâmetro onde selecionamos quais grupos daquele empreendimento receberão os e-mails quando novos documentos forem incluídos na proposta. Conforme a imagem abaixo, nesse exemplo o grupo Corretor está marcado para receber, então todos os usuários deste grupo, irão receber o e-mail de avaliação de documentos.

Os grupos que aparecem para a seleção, serão sempre os que estiverem com o parâmetro **Avaliar documentos da proposta**  marcado. 

Esse parâmetro é encontrado em **Backend → Usuários → Grupos → Editar**

* Os e-mails sempre serão enviados para os usuários dos grupos selecionados e seus superiores, desde que estejam ativos.
* Caso nenhum grupo seja selecionado o Portal de Imóveis por padrão irá enviar o e-mail somente ao seu corretor e seu superior.
* O envio de anexo do e-mail foi retirado, sendo assim não é mais enviado os documentos como anexo, no e-mail terá um link te direcionando para o Portal de Imóveis, onde será possível visualizar os documentos.
Unidades - Documentos da Unidade

**Documentos**

---

Foi adicionada a possibilidade de gerenciar documentos específicos para cada unidade do empreendimento. Essa funcionalidade permite que documentos pertinentes a uma determinada unidade sejam vinculados previamente, garantindo que eles sejam incluídos de forma automática no envelope do TOTVS Assinatura Eletrônica (TAE) durante a jornada do corretor.

Para gerenciar os anexos, acesse a tela de **Editar Empreendimento** e navegue até a aba **Unidades**.

Na listagem de blocos e unidades, foi incluída a nova coluna **Documentos**. Ao clicar no botão **Gerenciar**, o sistema abrirá a janela de **Documentos da Unidade**, informando a quantidade de arquivos já anexados (ex: "Gerenciar (2)").

Dentro da visão de Documentos da Unidade, é possível:

* **Adicionar:** Clicar no botão **+ Adicionar** para realizar o upload de novos arquivos vinculados estritamente à unidade selecionada.
* **Excluir:** Clicar no ícone de lixeira (vermelho) para remover um documento previamente inserido.

**Importante:** Os documentos anexados nesta tela do Backend aparecerão listados para envio na tela de "Proposta e Contrato" ao solicitar a assinatura eletrônica. Caso a unidade não possua documentos geridos nesta aba, a respectiva seção não exibirá arquivos de documentos da Unidade no momento da solicitação de assinatura.
