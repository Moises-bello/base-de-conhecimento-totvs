---
article_id: 13607521563159
category: RH - Cadastros
content_hash: b8aec119f70d304c72d97428e55883bff2809a353aa26fdefd63d6118cfb6d29
fetched_at: '2026-06-28T22:44:53.027307+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Funcionários isentos de Marcação de Ponto - Art.
  62 da CLT
type: support-article
updated_at: '2026-01-15T13:42:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13607521563159-RH-Linha-Protheus-PON-Funcion%C3%A1rios-isentos-de-Marca%C3%A7%C3%A3o-de-Ponto-Art-62-da-CLT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19462216668823) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como fazer o controle no módulo de Ponto Eletrônico para funcionários isentos de marcação de ponto, conforme o Art. 62 da CLT?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Na **Regra de Apontamento** é possível configurar como isento de ponto para associar a regra aos funcionários que são isentos de marcação de ponto. Para isto, basta criar uma regra de apontamento ou utilizar uma regra especifica para funcionários isentos de ponto.

Para cadastro da Regra de Apontamento acessar **Atualizações> Cadastro do Ponto> Regra de Apontamento**. Em caso de novo cadastro clique no botão incluir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23296736760215)  
  
Se for alterar uma regra existente, selecione a regra já criada clique em alterar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23296736789911)  
  
Com isso, terá um campo na rotina de **Regra de Apontamento** na aba **Outros campo Isentos Marc.**  
Ao incluir ou alterar uma regra, acesse a aba Outros e configurar o campo com conteúdo **2-Sim**, conforme tela abaixo:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19462216690455)**  
  
Após isto, acesse em Atualizações> Cadastros de Funcionários> Troca de Turno, filtre a matricula e faça a troca de turno com data inicial que o funcionário passou a ser isento de ponto. Faça a troca somente da regra, já o turno e sequência poderá permanecer os mesmos da linha anterior. Veja aqui [Como funciona a Troca de Turno dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671?source=search).  
  
Cabe ressaltar que uma vez que o funcionário é vinculado à uma Regra de Apontamento que o campo Isentos Marc. esteja como Sim, nenhum apontamento será gerado pra ele, mesmo que existam marcações em algum dia do período.  
  
Nas rotinas de Integrados e Marcações, será possível ver na legenda do calendário que o funcionário é isento de marcação:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19462156196375)**  
  
  
**Saiba Mais:**  
[Funcionários Isentos de Marcação](https://tdn.totvs.com/pages/releaseview.action?pageId=780013433)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
