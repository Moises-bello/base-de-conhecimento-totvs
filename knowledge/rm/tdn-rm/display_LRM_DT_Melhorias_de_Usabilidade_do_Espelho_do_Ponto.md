---
content_hash: 4bd6a09f24f87271dd1fcdeb099a21be24fa5307789a8825501b0c3757cead14
fetched_at: '2026-06-29T00:06:25.066366+00:00'
page_id: '224130054'
product: rm
source: tdn-rm
title: DT_Melhorias_de_Usabilidade_do_Espelho_do_Ponto
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Melhorias_de_Usabilidade_do_Espelho_do_Ponto
version: 1
---

# Transferência de Funcionário - Novo controle na criação de chapas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Espelho do Funcionário | *Espelho do Cartão* | |
| **Versão/Release:** | *12.1.4* |

## Descrição

Nesta versão, foi implementado uma melhoria na usabilidade do espelho do cartão, com o objetivo de possibilitar ao usuário uma melhor visualização da grid das batidas.

Também foi implementado uma tela de processo da execução do recalculo do ponto, tendo o objetivo de melhorar a percepção do usuário em relação ao andamento do recalculo e das informações de log sem precisar fechar a tela do espelho.

## Procedimento para Utilização

• Foi criado um agrupador na grid do espelho onde o usuário poderá expandir ou ocultar a grid de batidas.  
• Entre a grid do espelho e do agrupador das janelas de informações, foi inserido um spliter para possibilitar ao usuário redimensionar o espaço entre as grids conforme necessidade.  
• A barra de menu do agrupador Janelas de Informações, foi inserida acima da grid, promovendo uma melhor visualização e usabilidade da barra

***Resoluções 1280 x 1024 VS 1024 x 768.***

Utilizando a resolução 1280 x 1024 é possível a visualização dos 30 dias do mês do espelho do cartão do funcionário

Utilizando a resolução 1024 x 768 definida como resolução padrão para o produto não se torna possível a visualização dos 30 dias do mês do espelho do cartão do funcionário, apenas de 22 dias.

Foi implementado uma barra no canto direito da tela, onde mostra as informações de maior acesso exibindo os totais Diario, do Banco, e Total Geral, que foram as seguintes:

• Horas Trabalhadas   
• Atrasos   
• Faltas   
• Abonos   
• Extra Executado   
• Extra Autorizado   
• Adicional Noturno   
• Horas Base   
• Sobre Aviso

• Esta barra pode ser habilitada e desabilitada em qualquer momento.

Ao realizar o recalculo do espelho é disponibilizada uma tela exindo o processo da execução do recalculo e exibindo as informações de log geradas no final no processo, conforme em destaque nas imagens abaixo.
