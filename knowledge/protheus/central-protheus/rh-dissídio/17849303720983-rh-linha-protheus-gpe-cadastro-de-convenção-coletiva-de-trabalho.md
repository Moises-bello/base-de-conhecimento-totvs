---
article_id: 17849303720983
category: RH - Dissídio
content_hash: 16d5a2b5b5a735eabe769f2c71f9e00b8cc8545c53b43a22f890e446a19e59cf
fetched_at: '2026-06-28T22:43:43.209324+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro de Convenção Coletiva de Trabalho
type: support-article
updated_at: '2025-08-07T15:08:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17849303720983-RH-Linha-Protheus-GPE-Cadastro-de-Conven%C3%A7%C3%A3o-Coletiva-de-Trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17849319258391) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Criação do cadastro de Convenção Coletiva de Trabalho para associação com sindicatos que possuam a mesma convenção.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Criação do cadastro de convenção coletiva de trabalho (GPEA943). Acesse **Atualizações -> Cadastros -> Convenção Coletiva de Trabalho .**

Neste cadastro será possível definir as principais regras de cálculo referentes a convenção coletiva. Todos os campos que existem na CCT existem no cadastro de sindicato, mas nem todos os campos do cadastro de sindicato, existem no cadastro de CCT por tratarem-se de informações específicas de cada sindicato.

O cadastro dos dados de cálculo são efetuados na parte superior do cadastro, enquanto na parte inferior é possível visualizar os sindicatos, funções e verbas associados a CCT.

![](https://tdn.totvs.com/download/attachments/676585489/image2022-4-7_9-46-19.png?version=1&modificationDate=1649335580617&api=v2)

Para associar um sindicato a uma convenção, basta executar a opção "Associar sindicato", em "Ações relacionadas", ou utilizar o atalho F6. Uma nova janela será exibida com todos os sindicatos existentes para seleção e associação. Ao confirmar a nova janela, os dados dos sindicatos selecionados são carregados na getdados da aba "Sindicatos". Ao confirmar o cadastro os dados definidos na convenção serão replicados para os sindicatos associados.

![](https://tdn.totvs.com/download/attachments/676585489/image2022-4-7_9-43-35.png?version=1&modificationDate=1649335415773&api=v2)

**Importante**Todos os dados do cadastro de sindicatos serão sobrepostos pelos dados da convenção, mesmo os que não possuírem conteúdo. Exemplo: Sindicato possui 30% de insalubridade e na CCT o campo de insalubridade não foi preenchido. Ao associar o sindicato e confirmar o cadastro os sindicatos associados ficarão com o percentual de insalubridade vazio, como na CCT.

Para desassociar um sindicato basta desmarcar o checkbox da getdados da aba "Sindicatos". Ao confirmar o cadastro, o sindicato será desassociado da CCT, mas nenhum outro campo será alterado ou retornado ao valor original antes da associação com a CCT.  
  
**Importante**

Um sindicato não pode estar associado a duas CCT's, caso um sindicato associado a CCT 00000001 seja associado a CCT 000000002, ele perde o relacionamento com a CCT antiga, e os dados são redefinidos conforme a nova CCT.

Não será possível a exclusão da CCT caso exista algum sindicato associado, neste caso primeiramente o sindicato deve ser desassociado para em seguida excluir a CCT.

Para associar funções a CCT basta selecionar a opção "Associar Funções" em "Ações Relacionadas" ou utilizar o atalho F7. Uma nova janela com as funções disponíveis será aberta para seleção das funções. Ao confirmar a nova janela, as funções associadas são carregadas para a GetDados presente na aba "Funções". Ao confirmar o cadastro as verbas são gravadas na tabela RI4 (Funções x CCT).

![](https://tdn.totvs.com/download/attachments/676585489/image2022-4-7_9-44-27.png?version=1&modificationDate=1649335468567&api=v2)

Funções podem ser associadas com mais de uma CCT, que por sua vez podem estar associadas com vários sindicatos. Ativando o parâmetro MV\_CCTFUNC, ao cadastrar um funcionário será validado se o sindicato e função definidos no cadastro estão relacionados com uma mesma CCT, caso não estejam, um alerta é enviado e o cadastro não é efetuado.

Para associar verbas a CCT basta selecionar a opção "Associar verbas" em "Ações Relacionadas" ou utilizar o atalho F8. Uma nova janela com as verbas será aberta no mesmo molde das anteriores onde poderão ser selecionadas as verbas para associação. Ao confirmar a tela as verbas marcadas serão carregadas na GetDados presente na aba "Verbas" e após confirmação do cadastro elas serão gravadas na tabela REB (Verbas x CCT).

**Importante:** A funcionalidade de verbas é utilizada pela rotina de [precificação](https://tdn.totvs.com/pages/viewpage.action?pageId=738244202) do Gestão de Serviços.

![](https://tdn.totvs.com/download/attachments/676585489/image2022-4-7_9-45-24.png?version=1&modificationDate=1649335524910&api=v2)

Inclusão da Aba "Bases Operacionais", para associação da [Base Operacional](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=656614381) do GS com a CCT.

![](https://tdn.totvs.com/download/attachments/676585489/image2022-4-29_14-29-12.png?version=1&modificationDate=1651253355317&api=v2)

**Importante**

Uma base operacional pode ser associada a várias CCT's.

**Dissídio Retroativo**

Nas rotinas de cálculo do dissídio retroativo, reajuste salarial e exclusão do dissídio retroativo foram criadas novas perguntas para possibilitar filtrar os funcionários, além do sindicato, também pela Convenção Coletiva de Trabalho.

![](https://tdn.totvs.com/download/attachments/676585489/image2022-5-13_10-51-20.png?version=1&modificationDate=1652449879627&api=v2)

**Saiba Mais:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=676585489>

[Artigos Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
