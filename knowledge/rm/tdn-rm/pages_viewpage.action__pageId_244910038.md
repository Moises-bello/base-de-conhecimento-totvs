---
content_hash: 17cbc7a457a81826447871e5a7d834243b7d8247a48628788421a4c197840d82
fetched_at: '2026-06-29T00:08:15.553068+00:00'
page_id: '244910038'
product: rm
source: tdn-rm
title: TVBQEU ER Memorando de Exportação - Convênio ICMS / 20
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244910038
version: 126
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Totvs Gestão de Estoque, Compras e Faturamento | **Módulo** | Faturamento |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado** | TVBQEU | | |
| **País** | (X) Brasil | | |

   

## Objetivo

Essa melhoria tem como objetivo a adequação do movimento de Exportação às exigências do Convênio ICMS nº 20 de 08 de abril de 2016, além de proporcionar a melhoria da usabilidade na geração destes movimentos.

## Definição da Regra de Negócio

O Convênio ICMS nº 20 de 08 de abril de 2016 altera o Convênio ICMS 84/09, que dispõe sobre as operações de saída de mercadoria realizada com o fim específico de exportação. 

Neste convênio o Conselho Nacional de Política Fazendária - CONFAZ, estabelece em sua Cláusula Primeira que vários dispositivos do Convênio ICMS 84/09 passam a vigorar com nova redação.

Destacamos abaixo a Cláusula Quarta (IV) que originou a melhoria aqui especificada:

*“Cláusula quarta Relativamente às operações de que trata este convênio, o estabelecimento destinatário, além dos procedimentos a que estiver sujeito conforme a legislação de sua unidade federada, deverá emitir “Memorando-Exportação”, conforme modelo constante do Anexo Único, contendo, no mínimo, as seguintes indicações:*

*I - denominação: “Memorando-Exportação”;*

*II - número de ordem;*

*III - data da emissão;*

*IV - nome, endereço e números de inscrição, estadual e no CNPJ, do estabelecimento emitente;*

*V - nome, endereço e números de inscrição, estadual e no CNPJ ou CPF, do estabelecimento remetente da mercadoria;*

*VI - chave de acesso, número e data da(s) nota(s) fiscal(is) de remessa com fim específico de exportação;*

*VII - chave de acesso, número e data da(s) nota(s) fiscal(is) de exportação;*

*VIII - número da Declaração de Exportação;*

*IX - número do Registro de Exportação;*

*X - número do Conhecimento de Embarque e a data do respectivo embarque;*

*XI - a classificação tarifária NCM/SH e a quantidade da mercadoria exportada;*

*XII - data e assinatura do emitente ou seu representante legal."*

Veja mais sobre o Convênio ICMS nº 20 de 08 de abril de 2016 no link <https://www.confaz.fazenda.gov.br/legislacao/convenios/2016/cv020_16>

Conforme podemos verificar acima, a Cláusula Quarta determina os dados que devem constar do Memorando de Exportação, sendo que deverá ser gerado um memorando para cada fornecedor que remeteu ao exportador os itens a serem exportados.

Além disso, na EFD ICMS/IPI no Registro 1110 - Operações de Exportação Indireta - Mercadorias de Terceiros, existe o vínculo entre o fornecedor da mercadoria destinada à exportação, o documento emitido pelo mesmo com fins específicos de exportação, o Memorando de Exportação e as quantidades efetivamente exportadas. 

Assim, para atendimento às legislações acima o 'Número do Memorando de Exportação' que até então era vinculado a cada item que estava sendo exportado, passará a ser vinculado aos movimentos em que os mesmos foram enviados pelos fornecedores à empresa exportadora.

Além da adequação à base legal, iremos, nesta release, efetuar algumas melhorias na tela de Relacionamento ao Movimento de Exportação (*"Vendas > Faturamento > Movimentação > Movimento > Itens > Informações Adicionais > Relac. Mov. Export...")*, visando uma maior usabilidade da mesma.

Na parte inferior da tela, na grid relativa aos "*Itens de Movimentos a Serem Relacionados*" serão executadas as seguintes melhorias:

* Serão inseridas colunas com os seguintes campos relativos ao movimento do item a ser relacionado à exportação:
  + Código do Fornecedor;
  + Nome do Fornecedor;
  + Idmov;
  + Série do Movimento;
  + Código do Tipo de Movimento;
* Será criado um lookup que permita ao usuário filtrar os movimentos a serem exibidos, com possibilidade de utilização no mesmo de consulta SQL e fórmula visual;
* Será possível ao usuário configurar a ordenação e a exibição das colunas da grid.

Na parte superior da tela, na grid relativa aos "*Itens de Movimentos Relacionados*" será executada a seguinte melhoria:

* Será inserido o campo 'Número do Memorando de Exportação' que será editável, possibilitando que o usuário informe o memorando que será vinculado a cada uma das NF de entrada dos itens que serão exportados.

Para adequação à base legal e às melhorias que serão implementadas, serão retirados da tela de Informações Adicionais da Exportação (*"Vendas > Faturamento > Movimentação > Movimento > Itens > Informações Adicionais > Exportação")*os seguintes campos:

* Número do Memorando de Exportação, pois o mesmo passará a fazer parte da tela de relacionamento ao Movimento de Exportação;
* Conhecimento de Embarque, pois o mesmo se refere ao movimento de exportação em si e não ao item de movimento. Esse campo, além dos demais que se referem ao embarque já faz parte da tela de Informações Adicionais de Exportação do Movimento (*"Vendas > Faturamento > Movimentação > Movimento > Informações Adicionais > Exportação").*

Veja sobre o procedimento de utilização da rotina em  

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Movimento de Exportação | Alteração | Vendas > Faturamento > Movimentação | Conforme definições constantes deste documento |

## Tabelas Utilizadas:

* TITMVINCEXPORTACAO - Itens de Movimento Vinculados à Exportação

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
