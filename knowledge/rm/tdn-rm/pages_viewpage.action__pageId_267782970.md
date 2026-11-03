---
content_hash: 4a4fae1ce142326d3cb698e945d573641a874806afad36475a0e20b0e5296a51
fetched_at: '2026-06-29T00:08:19.375426+00:00'
page_id: '267782970'
product: rm
source: tdn-rm
title: TVBQEU DT Memorando de Exportação - Convênio ICMS / 20
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267782970
version: 134
---

# MEMORANTO DE EXPORTAÇÃO - CONVÊNIO ICMS Nº 20

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | Totvs Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Movimento | MovMovimentoAction | |
| **Chamados Relacionados** | TVBQEU |
| **País:** | Brasil |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Tabelas Utilizadas:** | TITMVINCEXPORTACAO - Itens de Movimento Vinculados à Exportação |
| **Sistema(s) Operacional(is):** | Windows |

## 

## Descrição

O Convênio ICMS nº 20 de 08 de abril de 2016 altera o Convênio ICMS 84/09, que dispõe sobre as operações de saída de mercadoria realizada com o fim específico de exportação. 

Neste convênio o Conselho Nacional de Política Fazendária - CONFAZ, estabelece em sua Cláusula Primeira que vários dispositivos do Convênio ICMS 84/09 passam a vigorar com nova redação.

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

## Procedimento para Implantação

A partir da versão 12.1.15, a ativação das alterações descritas neste documento será automática, porém caso deseje ativá-las nas versões 12.1.13 ou 12.1.14, será necessária a execução do artefato **SCRIPT MEMORANDO 12.1****[SCRIPT\_MEMORANDO\_12.1.ZIP].**

Este artefato está disponível para todos os clientes na  Central de Download do portal do cliente, e para acessá-lo siga as instruções abaixo:

* Acesse a [Central de Download](https://suporte.totvs.com/download)
* Faça o login, com seu e-mail e senha. (O login de senha deverá ser do usuário cadastrado da empresa em questão)
* .       Na barra de menu superior, clique em “DOWNLOADS E ATUALIZAÇÕES”.
* .        Na visão da página “Lista de Produtos” coloque as informações abaixo:

**Outras Linhas de Produto:** RM**Software: 12.1**

## Procedimento para Utilização

Para atendimento ao Convênio ICMS nº 20 de 08 de abril de 2016  o 'Número do Memorando de Exportação' que até então era vinculado a cada item que estava sendo exportado, passará a ser vinculado aos movimentos em que os mesmos foram enviados pelos fornecedores à empresa exportadora.

Para a realização deste vínculo, foram realizadas algumas alterações que descreveremos a seguir.

Na parte inferior da tela, na grid relativa aos  "*Itens de Movimentos a Serem Relacionados"*foram inseridas colunas com os seguintes campos relativos ao movimento do item a ser relacionado à exportação:

* Identificador do Movimento;
* Série do Movimento;
* Código do Tipo de Movimento;
* Código do Fornecedor;
* Nome do Fornecedor.

Foi criado ainda, um filtro que permite selecionar os movimentos a serem exibidos, com possibilidade de utilização no mesmo de consulta SQL e fórmula visual.

Para acionar o filtro clique no binóculo e defina o campo a ser utilizado para selecionar o movimento desejado.

A partir dessa versão será também possível configurar a ordenação e a exibição das colunas dessa grid,bastando clicar no ícone de ordenação de colunas e selecionar os campos a serem exibidos, bem como configurar a sua ordem de exibição através das setas para cima e para baixo.

Além disso, na parte superior da tela, na grid relativa aos**"Itens de Movimento Relacionados"**foi incluído o campo 'Número do Memorando de Exportação' que é editável, possibilitando que você informe o número do memorando que será vinculado a cada uma das notas fiscais de entrada dos itens que estão sendo exportados. Assim, quando da inclusão do relacionamento dos movimentos o Número do Memorando de Exportação virá em branco. Clique no campo e forneça essa informação.

Para adequação à base legal e às melhorias implementadas, foram retirados da tela de Informações Adicionais da Exportação (*"Vendas > Faturamento > Movimentação > Movimento > Itens > Informações Adicionais > Exportação")*os seguintes campos: 

* Conhecimento de Embarque, pois o mesmo se refere ao movimento de exportação em si e não ao item de movimento. Esse campo, além dos demais que se referem ao embarque já faz parte da tela de Informações Adicionais de Exportação do Movimento (*"Vendas > Faturamento > Movimentação > Movimento > Itens > Informações Adicionais > Exportação");*
* Número do Memorando de Exportação, pois, conforme já explicado acima, este campo passou a fazer parte da tela de Relacionamento ao Movimento de Exportação.

divs
