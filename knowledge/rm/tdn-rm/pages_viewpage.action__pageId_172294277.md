---
content_hash: e4921f3d9b0f6bf151af5ce465c1e3cea4b1f124981bb8f9e5c70e812573d8aa
fetched_at: '2026-06-29T00:05:57.265150+00:00'
page_id: '172294277'
product: rm
source: tdn-rm
title: Como Fazer - Log contábil no TOTVS Gestão de estoque, compras e faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=172294277
version: 3
---

|  |  |
| --- | --- |
| Linha | RM |
| Produto | TOTVS Gestão de Estoque, Compra e Faturamento |
| Versões | A partir da 11.40 |
| Processo | Integração Contábil |
| Subprocesso | Log de Contabilização aplicado em movimento |
| Data da publicação | 15/10/2014 |

Avaliação

* ***Como Fazer***

Como realizar a configuração do log contábil no movimento

* ***Definição do Processo***

Habilitar o log de evento contábil para auxiliar na identificação da(s) causa(s) da diferença entre débito e crédito das partidas geradas.

Solução

* ***Parametrizações Necessárias***

- Clique no ícone “Ativar/Desativar Log do evento contábil” ( localizado no canto superior esquerdo)

    - o menu “Operação a ser executada” marque a opção “Ativar LOG” e execute.

Após ativar o Log do evento será preciso refazer a contabilização, clicando no ícone “Refaz Contabilização” (exempo imagem) o evento será executado novamente e será então gerado o Log.

Ao refazer a contabilidade será mostrado um novo ícone ao lado do “Ativar/Desativar Log do evento contábil” chamado “Visualização do Log da contabilização gerada a partir do Evento contábil” e após clicar neste ícone será aberta uma aba (Log Evento Contábil) conforme imagem abaixo:

A partir desta tela será possível identificar onde está ocorrendo o erro na execução do evento contábil. Ao estender a opção “Contabilização” serão apresentado todos os itens do evento contábil em questão divididos entre itens de débito e itens de crédito. Ao clicar no Item será apresentado o evento executado ou então a log que mostra a trajetória do item, possibilitando achar a diferença.

Ex.:

Na imagem abaixo o item de débito não foi executado pois apesar de sua formula retornar um valor maior que zero (quadro verde) , o local onde se buscou a conta contábil não existia a conta de débito, mas sim uma conta de crédito (quadro Azul). Neste caso a falha esta na origem da conta.

Sendo assim, após descobrir o motivo da má execução, basta consertar o evento e logo após contabilizar novamente o movimento com o evento contábil corrigido.

***Observação**: Clicando no ícone  poderá salvar o log em formado XML, caso seja necessário armazená-lo ou se o mesmo for solicitado pelo suporte.*

*Link de documento explicando **[Como avaliar seu Evento Contábil](http://tdn.totvs.com/x/aJrYCg).***
