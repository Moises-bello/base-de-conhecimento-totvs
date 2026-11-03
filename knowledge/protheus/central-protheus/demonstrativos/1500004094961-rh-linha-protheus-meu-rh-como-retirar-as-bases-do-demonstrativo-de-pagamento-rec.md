---
article_id: 1500004094961
category: DEMONSTRATIVOS
content_hash: 2120902395d1d6bbe41b8cee0ecbc3a11e1c623ec4a7a8d83b5f291a4f89956b
fetched_at: '2026-06-28T22:44:38.418804+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: RH - Linha Protheus - MEU RH -  Como retirar as bases do Demonstrativo de Pagamento
  (recibos/holerites)
type: support-article
updated_at: '2026-02-06T17:23:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004094961-RH-Linha-Protheus-MEU-RH-Como-retirar-as-bases-do-Demonstrativo-de-Pagamento-recibos-holerites
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17745351193879) Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
Como retirar as bases do Demonstrativo de Pagamento (recibos/holerites)  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Para ocultar as informações de base é necessário ajustar o parâmetro **MV\_IMPBASE com o conteúdo .F.**  
  
Para essa alteração, no programa inicial do Protheus, digite SIGACFG (acesso ao Configurador).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17745123111831)  
\*\* Será necessário solicitar um usuário e senha de administrador para essa alteração.  
  
Após acessar o Configurador, clicar em **Ambiente > Cadastros > Parâmetros**:  
  
Em seguida, clicar em Parâmetros e na lupa de busca.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17745186920983)  
  
Localizar **MV\_IMPBASE:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17745191973655)  
  
Por fim, editar o parâmetro e na tela a seguir, cadastrar o novo conteúdo .F. para não verificar as bases, ou .T. para verificar as bases.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17745249150231)  
  
Salve o novo conteúdo, feche o Configurador, reinicie o serviço do App Meu RH, e por fim, será possível a geração do Demonstrativo de Pagamento, conforme parâmetro escolhido.  
  
Caso não tenha o parâmetro ou para mais dúvidas acesse o Boletim Técnico:   
[**DT Imprimir eventos de base no relatório do recibo de pagamento**](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=554661859)  
  
Esse parâmetro só vai influenciar o Demonstrativos de Pagamento (recibos/holerites) impresso.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005037222)  
  
Na rotina do MEU RH continuará sendo exibido todas informações, conforme exemplo abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005149841)  
  
**Dúvidas Frequentes**  
[**O que é preciso para consultar o Demonstrativo de Pagamento no MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053872814)  
[**É possível limitar a quantidade de Demonstrativos de Pagamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059307574)  
[**O que fazer quando download de demonstrativo apresenta "Falha ao carregar documento PDF"?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042996014)  
[**Qual a regra para exibir os Demonstrativos de Pagamento (recibos/holerites)?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044237214)  
[**É possível visualizar o Demonstrativo de Pagamento somente do mês atual**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044764053)  
[**É possível utilizar o Rdmake RECIBO.PRW para geração do Demonstrativo no Meu RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055663753)  
  
**Importante**  
Caso você entenda que deve haver algum comportamento diferente ou outras opções de personalização, por gentileza, registre uma solicitação de melhoria através do da [**Central Colaborativa TOTVS**.](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics/360001644254-TOTVS-Meu-RH-Folha-de-pagamento-Envelope-de-Pagamento)  
  
É possível acompanhar as funcionalidades já disponíveis e o planejamento do que está por vir através do [**ROADMAP MEU RH - PROTHEUS**](https://tdn.totvs.com/display/public/NPR/Roadmap+-+Protheus).  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
