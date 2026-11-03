---
article_id: 4405084582423
category: RH - Cadastros
content_hash: 7b47fe4035dddbe5ab5809e8f32aa42b522196086237e2f24d09e6c7b22358a6
fetched_at: '2026-06-28T22:44:52.924518+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como trocar um Evento calculado por um informado
  manualmente nas rotinas de Integrados ou Apontamentos
type: support-article
updated_at: '2025-12-10T12:42:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405084582423-RH-Linha-Protheus-PON-Como-trocar-um-Evento-calculado-por-um-informado-manualmente-nas-rotinas-de-Integrados-ou-Apontamentos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34191241302167) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como trocar um **evento calculado** por um **informado manualmente** nas rotinas de Integrados ou Apontamentos?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Existem situações onde é necessário para o cliente, que o Ponto considere um **código de evento diferente** do que foi **apontado**, para que a **apuração** de **BH** ou **desconto/pagamento em Folha** ocorra de maneira correta, ou seja: um **evento apontado** seria **descontado em Folha**, mas por particularidades do cliente, é necessário que seja feita uma **troca** para que ocorra um **desconto no BH** do funcionário, por exemplo.  
  
O SIGAPON **permite** que o usuário **troque** um **evento** que foi **apontado** por um outro **informado manualmente** através das rotinas de **Integrados** ou **Apontamentos**, para isso, basta seguir os passos abaixo (**lembrando que o campo existe em ambas rotinas**):  
  
1 - Acessar em**Integrados**, veja que no dia 16.07 foi apontado o evento de código 009 - Falta Folha, porém, eu preciso que neste dia a falta seja descontada no BH do funcionário, portanto, vou utilizar o campo **Código Inf**.:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405076635799)  
  
2 - No campo **Código Inf.**, foi lançado o evento 010, que é Falta para desconto em BH:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405076651671)  
  
3 - Após o **Cálculo Mensal**, a falta foi lançada no BH do funcionário:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405071770519)  
  
**Importante** ressaltar que: uma vez que o campo **Código Inf.** é utilizado, **o sistema despreza o evento que foi gerado anteriormente** no apontamento, portanto, é **importante** que o campo seja utilizado apenas em **trocas TOTAIS**, caso seja informado um **valor proporcional**, o sistema **não vai considerar nenhum dos dois eventos** (nem o apontado, nem o informado manualmente).  
  
Segue um exemplo abaixo de como o campo NÃO deve ser utilizado:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405071834391)  
  
**Importante** também ressaltar que **uma vez que um código é informado**, o dado é **gravado** na tabela **SPC** (Apontamentos do Período em aberto), portanto, mesmo que ocorra algum ajuste nas marcações de Ponto, fazendo com que os **Apontamentos** daquele dia sejam alterados, o **Apontamento** **continuará aparecendo**, bem como o **código informado**.   
  
Para **desprezar o dado**, o **usuário deve manualmente excluir o conteúdo do campo de código informado** e fazer um **novo reapontamento** das marcações.  
No exemplo abaixo, veja que o funcionário tinha marcações ímpares, onde gerou um **Apontamento** de Falta 1/2 Período e foi lançado um **código informado**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8207899053591)  
  
Depois, o usuário lançou uma marcação e fez um **reapontamento**, veja que neste caso o funcionário teve uma Hora Extra, porém, como **não foi deletado manualmente o código informado**, o sistema **mantém o registro**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8207935074839)  
  
É necessário **deletar manualmente o conteúdo do campo de código informado** e fazer um **novo reapontamento**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8207937726231)

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
