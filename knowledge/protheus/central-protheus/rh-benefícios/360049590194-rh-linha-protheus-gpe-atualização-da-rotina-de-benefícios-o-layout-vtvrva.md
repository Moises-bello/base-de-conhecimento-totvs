---
article_id: 360049590194
category: RH - Benefícios
content_hash: effe3c192296a97568d472b938dc11dc3f4c17289674517a279676a7dfce3348
fetched_at: '2026-06-28T22:44:04.848482+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Atualização da rotina de Benefícios o layout -
  VT/VR/VA
type: support-article
updated_at: '2023-03-10T20:06:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049590194-RH-Linha-Protheus-GPE-Atualiza%C3%A7%C3%A3o-da-rotina-de-Benef%C3%ADcios-o-layout-VT-VR-VA
---

**Dúvida**Como atualizar o leiaute na rotina benefícios?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Para utilizar o novo layout, deve ser alterado o parâmetro **MV\_CALCBEN** para **.T.**e acessar a rotina de **Atualização de VA / VR / VT**. 

**Atenção:**O processo de conversão para a nova solução é irreversível. É muito importante realizar testes em customizações, caso existam, pois foi alterada a estrutura de dados e processamento dos benefícios. A partir da release **12.1.27**do Protheus, a versão anterior será descontinuada e o conteúdo do parâmetro MV\_CALCBEN será ignorado.

Após alterar o parâmetro **MV\_CALCBEN** para **.T.** e acessar a rotina de Atualização de Benefícios: **Atualizações > Benefícios > VT / VR / VA > Atualização,** pela primeira vez, será apresentada uma mensagem questionando se deseja realizar a conversão para a nova rotina de benefícios.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075806953/mceclip0.png)

Ao clicar em Sim, o sistema irá transferir as informações da tabela **SR0** para a nova tabela **SM7** e excluir os registros da SR0. Esse processo será executado apenas uma vez e é irreversível. 

***Alterar o parâmetro MV\_CALCBEN para .F. não irá retornar os registros para a tabela SR0**.*Assim que a conversão dos dados é concluída, a nova tela é apresentada.

*Veja mais detalhes sobre a tela:*

Na parte superior (1), contém as informações do funcionário, Matrícula, Nome e Data de Admissão. Agora os Benefícios são organizados em abas (2), possibilitando a navegação entre eles na mesma tela, facilitando a manutenção. Em cada aba, estão os vales vinculados ao funcionário (3) e os pedidos calculados no período atual (4), demonstrando a quantidade de dias e valores calculados, assim como dias de afastamento e quantidade de faltas consideradas para o cálculo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075807193/mceclip1.png)

O Histórico dos benefícios pode ser consultado acessando o menu **Outras Ações > Histórico*:***

***![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074593694/mceclip2.png)***

A tela de histórico também está organizada por abas e, para consultar os vales pagos, basta informar o período que deseja consultar na seção Pesquisa e o grid da parte inferior será atualizado com as informações daquele período;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075807493/mceclip3.png)
