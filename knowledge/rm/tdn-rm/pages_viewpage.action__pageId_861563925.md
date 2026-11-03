---
content_hash: 16da3ab845ee3cbe87634f50567f769b27b706605a04eee791de5a2593c3ca36
fetched_at: '2026-06-29T00:11:55.471940+00:00'
page_id: '861563925'
product: rm
source: tdn-rm
title: TOTVS Aprovações e Atendimento - Manutenção de Equipamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=861563925
version: 3
---

Para gerar uma Ordem de Serviço de Manutenção a partir de um atendimento criado no TOTVS Aprovações e Atendimento, são necessárias algumas parametrizações:

1) Acesse o TOTVS Aprovações e Atendimento e cadastre o Tipo de Atendimento que será usado na integração com o Manutenção de Equipamentos: através do menu Workflow\Tipos de Atendimentos, informe um   
Nome e o Serviço associado ao Tipo de Atendimento, que deve ser o serviço para Geração de OS:

2) Ainda na tela do Tipo de Atendimento, após salvar as informações inseridas, acesse o Anexos de Etapas, e crie pelo menos duas etapas para o tipo de atendimento:

3) Ainda no cadastro de Etapas, acesse aquela que deverá originar a OS, na aba Ações Visíveis e marque a opção:

4) Defina os Fluxos de Etapas do Tipo de Atendimento no Anexos Fluxo de Etapas, conforme exemplo na figura abaixo:

5) Após salvar as informações, acesse a aba Ações Visíveis e selecione a Ação Gerar O.S. (Gerar OS) no avanço para a etapa que deverá gerar a OS:

6) Crie um Grupo de Atendimento no menu Workflow>Grupos:

7) Em seguida, associe o Tipo de Atendimento no Anexo Tipos de Atendimentos do Grupo de Atendimento:

8) Acesse os parâmetros no menu de Manutenção de Equipamentos no TCOP>Integrações>TOTVS Aprovações e Atendimento, e informe o Tipo de Atendimento, e a Etapa Final desse mesmo tipo de atendimento, para habilitar a integração com o TAA:

9) Crie um atendimento no TOTVS Aprovações e Atendimento, do mesmo tipo referenciado logo acima:

10) Ainda na tela do atendimento, o usuário de umas das etapas que precede a geração da OS, deverá acessar o anexos Ações de Serviços:

11) Preencher o tipo de movimento e os dados do respectivo objeto de manutenção que dará origem à OS, e salvar:

12) Ao avançar o atendimento para a etapa parametrizada para gerar OS, a ação estará visível conforme imagem a seguir:

E ao concluir o avanço da etapa com sucesso, a OS será criada automaticamente pelo TOTVS Aprovações e Atendimento:
