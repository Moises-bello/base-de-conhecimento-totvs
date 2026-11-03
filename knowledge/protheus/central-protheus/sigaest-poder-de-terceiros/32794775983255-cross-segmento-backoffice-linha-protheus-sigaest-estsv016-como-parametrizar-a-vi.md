---
article_id: 32794775983255
category: SIGAEST - PODER DE TERCEIROS
content_hash: 101b7b52df89fcd14b870573a9c2c34dfdfaa77b6a6348e9aca0a43c5e0556f3
fetched_at: '2026-06-28T22:39:03.188581+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - ESTSV016 Como parametrizar
  a view de Materiais de/em Terceiros para analisar os saldos e movimentações
type: support-article
updated_at: '2025-06-16T15:58:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32794775983255-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-ESTSV016-Como-parametrizar-a-view-de-Materiais-de-em-Terceiros-para-analisar-os-saldos-e-movimenta%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32794803827223) Tempo aproximado para leitura: **00:07:00 min****Dúvida**Como configurar o Smarview de Materiais de/em Terceiros para analisar os saldos e movimentações?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.2310 ou Superior.  
  
 **Solução**Com a descontinuidade do relatório MATR480 conforme [documentação](https://tdn.totvs.com/pages/releaseview.action?pageId=823815318), pode ser necessário configurar a visualização ESTSV016 Materiais de/em Terceiros para analisar os saldos e movimentações, segue abaixo as configurações recomendadas junto a explicação de cada pergunte.  
  
  
1. Nesta tela é possível gerar a visualização em tela, ou em relatório, para o envio à análise do suporte e exemplo usaremos a geração de relatório em PDF;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794775941911)  
  
2. Para um maior entendimento e compreensão o recomendado é o arquivo PDF;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794803834263)

3. Clique no botão de "Parâmetros" para abrir a tela abaixo, é importante que o campo Filiais esteja em branco;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794775944727)

4. Nos perguntes de "Cliente" e "Fornecedor", se estiver avaliando o saldo e quantidade de um cliente/fornecedor em especifico é possível filtrar pelo o código dele, mas caso esteja avaliando o saldo em geral ou possui uma operação triangular, o mesmo deve estar de "(Branco)" á "zzz" em minúsculo para atender tanto letras maiúsculas quanto minúsculas;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32798846843287)  
  
  
5. Nos perguntes de Produtos, efetue um filtro do Produto que deseja avaliar;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794775948823)

6. Todos os parâmetros envolvendo Data, é ideal que estejam filtrados de "01/01/2000" a "data que está avaliando" no exemplo usaremos a data "30/04/2025", essa configuração inicial é para que possa pegar um período bem grande e não ocorre assim uma perda de dados durante a análise;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794803843479)

7. No pergunte de "Situação" temos duas opções possíveis onde "1" é igual a **"Todos "** e "2" é igual a **"Em aberto"** , caso esteja validando qual saldo está em aberto, selecione a opção "2".  Porém caso compreenda que esta com algum erro em um retorno e não identificou qual, selecione a opção "1".   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794775956631)

8. No pergunte de "Tipo" temos três opções possíveis onde "1" é igual a "De terceiros", ou seja produto de terceiros em sua posse, "2" é igual a "Em terceiro", ou seja produto seu em posse de terceiros e "3" é igual a "Ambos", ou seja o relatório irá informar tanto produto De terceiros como Em terceiros. Para avaliações de saldo o ideal é que esteja como "3" para não ocorre uma perca de dados durante a análise;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794803847063)

9. No pergunte de "Lista NF Devolução ?" temos duas opções possíveis onde "1" é igual a "Sim" e "2" é igual a "Não", o ideal é que o mesmo esteja como "1", para que seja possível visualizar todas as devoluções que ocorreram e se alguma foi feita de maneira incorreta

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32794775959191)

10. Após confirmar o dados, clique em Confirmar > Imprimir, e selecione qual local deseja salvar o arquivo.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32797845279639)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32798846845079)

**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar o Controle de Poder De/Em Terceiros?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005090232-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-Controle-de-Poder-De-Em-Terceiros)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como eliminar saldo em Poder de terceiro (retorno simbólico)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010519121-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-eliminar-saldo-em-Poder-de-terceiro-retorno-simb%C3%B3lico)

[Mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)
