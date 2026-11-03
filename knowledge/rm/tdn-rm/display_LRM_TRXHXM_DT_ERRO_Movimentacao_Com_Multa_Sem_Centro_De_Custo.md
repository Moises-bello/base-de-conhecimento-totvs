---
content_hash: ee4170775566cef4961e7e017d08dea03ba2268606824b3fc69017b3d9e2355b
fetched_at: '2026-06-29T00:06:17.153820+00:00'
page_id: '212905455'
product: rm
source: tdn-rm
title: TRXHXM_DT_ERRO_Movimentacao_Com_Multa_Sem_Centro_De_Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/TRXHXM_DT_ERRO_Movimentacao_Com_Multa_Sem_Centro_De_Custo
version: 2
---

# MOVIMENTAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Bibliotecária* |
| **Função:** | *Movimentações* |
| **Situação/Requisito:** | *Ao realizar o processo de devolução de uma movimentação quando o parâmetro "Rateio Centro de Custo/Natureza Orçamentária" estiver marcado como "Não obrigatório" o centro de custo não está sendo preenchido no lançamento gerado.* |
| **Solução/Implementação:** | *O método responsável por validar o uso do rateio por centro de custo estava utilizando um objeto do Fluxus que não permitia a correta validação se o reateio estava definido para o centro de custo ou não.*  *Foi realizado um ajuste, alterando o objeto utilizado por outro mais coerente com a validação necessária.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *Versão na qual está sendo feita a manutenção deste programa.* |
| **Versão Expedida:** | *Versão em que o programa será oficialmente expedido.* |

divs

- Situação/Incidente (descreva tecnicamente o que ocorre detalhando a situação identificada pelo analista de atendimento).  
Ao realizar o processo de devolução do biblios para o usuario o sistem não levou o centro de custo quando nos parametros do Fluxus o Rateio esteja configurado como Não Obrigatorio. quando alterei o parametro para Obrigaotrio sempre o sistema levou corretamente o valor do centro de custo.  
- Solução (o analista deve descrever o que será feito sugerindo a solução para o programador).  
O método UsarRateioPorCentroDeCusto() estava utilizando o Enum FinObrigUsarRateioCCuNatEnum, porém este Enum não permite validar o uso do Rateio. É necessário utilizar o Enum FinTipoRateioCCuNatEnum, este Enum possui as opções necessárias para o correto funcionamento do método.  
- Identificação dos casos de teste (devem ser indicados os casos de testes que serão utilizados ou uma breve descrição do que deve ser testado para evidenciar a correção do problema reportado)  
Acessar RM Biblios, realizar uma movimentação, atrasar a entrega desta movimentação, realizar a devolução.Ao gerar o lançamento referente à devolução realizada, o centro de custo deve ser preenchido (se estiver cadastrado na unidade).
