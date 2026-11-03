---
article_id: 360052864793
category: MDT - EPI
content_hash: 97c78497f6c55fa2db6c28e46b2a9ea35de1525a1010510c8a597c96324fed0f
fetched_at: '2026-06-28T22:44:25.382700+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Como realizar uma entrega de EPI com solicitação
  ao armazém
type: support-article
updated_at: '2024-11-05T11:22:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052864793-RH-Linha-Protheus-MDT-Como-realizar-uma-entrega-de-EPI-com-solicita%C3%A7%C3%A3o-ao-armaz%C3%A9m
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20197428987287)**  Tempo aproximado para leitura: **00:02:00min  
  
Dúvida**Como realizar uma entrega de EPI com solicitação ao armazém?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Temos disponíveis um vídeo demonstrando o passo a passo. Além do vídeo existe a documentação de apoio que pode ser acessada através do link: [MDT EPI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945554-MDT-EPI)  
  
How To | MP - SIGAMDT - Como Entregar EPI Com Solicitação ao Armazém   
  
  
  
É possível realizar uma entrega de EPI com solicitação ao armazém. Para isto é necessário ativar alguns parâmetros de integração. Acesse o Configurador ( SIGACFG), no seguinte caminho: Atualizações > Cadastro > Parâmetros, localize e edite os parâmetros abaixo.  
  
O parâmetro **MV\_NG2SA** em conjunto com o parâmetro de integração com o módulo de Estoque **MV\_NGMDTES** devem estar habilitados para que a solicitação no estoque seja gerada.  
  
MV\_NGMDTES - Integração do Medicina e Segurança do Trabalho com o Estoque. Conteúdo deve ser S=Sim ou N=Não.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084895053)  
  
MV\_NG2SA - Indica se gera solicitação ao armazém ao invés de baixar do estoque. Conteúdo deve ser S=Sim ou N=Não.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084895193)  
  
Importante ter definidos os cadastros de produtos  
Se tiver dúvidas em como cadastrar Produtos do TIPO EPI consulte  
[MP - MDT - Como cadastrar um produto com o tipo EPI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048704353/)Para realizar uma solicitação de um EPI acesse o Módulo 35 (SIGAMDT), no seguinte caminho: Atualizações > EPI > Funcionário x EPI. Selecione a matricula e clique em EPI.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083752914)  
  
Na parte inferior selecione o EPI  e a quantidade que posteriormente serão entregues. Clique em confirmar.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084900333)

Após confirmar e retornar na visualização da entrega de EPI é possível ver o número da S.A criada.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083728914)  
  
Para atender esta solicitação deverá acessar o Módulo 04 (SIGAEST), no seguinte caminho: 

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083729674)  
  
Certifique-se que sua solicitação foi criada.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084900913)

Deverá gerar a pre requisição, para isto acesse:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083729894)

 Selecione o item desejado e clique em **GERAR**.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084901873)  
  
Clique em gerar e preencha corretamente os parâmetros para geração, Se tiver alguma dúvida neste processo deverá ser verificado com o suporte do ESTOQUE.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084928453)  
  
  
Por Fim executar a rotina de baixa pre requisição **(MATA185),** para isto acesse:  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083730514)

Importante ressaltar que esses dados de cadastros são apenas exemplos de teste, caso tenha alguma dúvida conceitual em seu cadastro acione o suporte do Estoque para esclarecimentos.  
  
Selecione a opção desejada e clique em baixar.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083730534)

Será apresentado esta tela para preenchimento deverá informar o  Código da TM e salvar o registro.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084928053)  
   
Após preenchimento basta salvar o registro.]

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084902193)

Veja que a legenda é alterada.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083751554)

Dica: caso você não tenha um Tipo de MOVIMENTAÇÃO em sua base acesse a rotina **(MATA230)**  crie um TM do tipo Requisição. No seguinte caminho: Acesse o Módulo (04) de Estoque\Custos.  
Vá em > Atualizações > Cadastros > Movimentações > Internas > Incluir  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083880914)

FAQ Sobre o Tipo de movimentação, caso mesmo assim tenha dúvidas entre em contato  com o Suporte ESTOQUE e CUSTO .  
<https://tdn.totvs.com/pages/releaseview.action?pageId=344472467>Ao conferir a rotina Funcionário x EPI no Módulo **(SIGAMDT)**Note que o Status do EPI foi alterado de Solicitação ao Armazém para Entregue.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084926093)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
