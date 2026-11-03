---
article_id: 360041781134
category: Materiais - Compras (SIGACOM)
content_hash: 204080e6440a0ab62c665cf0808cfa65a7432320ba9ce1dda2110c7e39d727c1
fetched_at: '2026-06-28T22:41:19.970798+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Impressão do Pedido
  de Compras - Relatório MATR110
type: support-article
updated_at: '2024-08-23T14:21:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041781134-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Impress%C3%A3o-do-Pedido-de-Compras-Relat%C3%B3rio-MATR110
---

**Dúvida**

MATR110 - Fluxo de impressão do relatório de Pedido de Compras  
  
**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Solução**

A impressão do Pedido de Compras no Protheus pode ser realizada através do relatório MATR110 que pode ser executado de duas formas:  
  
**1. Via browser do Pedido de Compras/Autorização de Entrega:**  
Somente o pedido posicionado é que será impresso.  
Os parâmetros (perguntes) do relatório ficam desativados e o sistema imprimirá todos os registros compreendidos pela chave C7\_FILIAL+C7\_NUM do registro posicionado.

* **Exemplo de utilização:**  
  Usuário acabou de inserir um pedido de compra e deseja rapidamente imprimi-lo/enviá-lo via e-mail para o setor responsável pelo andamento do pedido.  
  Assim como o sistema fica posicionado no registro que acabara de ser inserido, isso facilita seu fluxo de trabalho.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055826294)

***Obs:***

Esta impressão através da opção "Outras Ações -> Imprimir" do Browse da rotina, tem a funcionalidade de imprimir/executar o programa que consta no parâmetro ***MV\_PCOMPRA***, que no padrão do sistema tem o conteúdo "MATR110" no qual é chamado o relatório padrão.

**2. Via menu de Relatórios (Rotina MATR110);**  
Nesta rotina, pode-se imprimir diversos pedidos.  
Os parâmetros (perguntes) do relatório ficam ativados e o sistema imprimirá todos os registros compreendidos pelos filtros aplicados via pergunte.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056693173)

* **Exemplo de utilização:**  
  Extração de pedidos emitidos numa determinada competência (mensal/anual), para fins de auditoria e/ou atividades gerenciais.  
  Desta forma com os perguntes ativados a extração fica completa.

Para ajustar esses perguntes (filtro), basta ir em **Outras** **ações**, **Parâmetros**:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055826994)

**Perguntes**:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055827194)

**Parâmetro MV\_PCHABPG:**  
Existe uma exceção para o cenário 1), onde o parâmetro MV\_PCHABPG = .T., o sistema considerará os seguintes perguntes na impressão do relatório via browse:

* Somente os novos ? (mv\_par05)
* Imprime ? (mv\_par08)
* Numero de Vias ? (mv\_par09)
* Imprime Pedidos ? (mv\_par10)
* Considera SCs ? (mv\_par11)
* Lista quais ? (mv\_par14)     
    
  Por default o parâmetro MV\_PCHABPG é desabilitado, ficando o cliente responsável pela configuração conforme desejar ajustar seu fluxo de trabalho.

Para utilização deste parâmetro, a rotina MATR110 deverá ser atualizada, para isso [clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041778474)

***Saiba Mais :***

[MP - SIGACOM - Alerta: Verifique os parâmetros definidos para este relatório - Impressão PC/AE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041778474)

[M110MAIL - Fornece pedidos AE para manipulação](https://tdn.totvs.com/pages/releaseview.action?pageId=6085311)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
