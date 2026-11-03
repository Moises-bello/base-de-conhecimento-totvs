---
article_id: 1500004779102
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5db15c93fd92962973856e2829c99faaea07afed41e977bac3c44c5be8c0717c
fetched_at: '2026-06-28T22:38:57.040401+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA261 - Pontos de
  Entrada da rotina Transferência Múltipla
type: support-article
updated_at: '2026-03-04T18:37:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004779102-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-Pontos-de-Entrada-da-rotina-Transfer%C3%AAncia-M%C3%BAltipla
---

A rotina MATA261 - Transferência Múltipla no TOTVS Protheus possui diversos Pontos de Entrada para customizações, como MT261MEM (adição de campos memos virtuais), M261FILB (filtros na tela), MA261CPO (inclusão de campos para digitação), MA261IN (preenchimento de campos na tela de estorno), entre outros, permitindo personalizações em validações, interfaces e gravações de dados.

**Dúvida**  
Quais são os Pontos de Entrada relacionados à rotina MATA261 - Transferência Múltipla?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Veja abaixo os Pontos de Entrada relacionados à rotina MATA261 - Transferência Múltipla (clique no nome do ponto de entrada para obter maiores detalhes):  
  
É possível efetuar personalizações com os pontos de entrada abaixo, para  os tipos de Movimentação (D3\_TM) 499 e 999, validar juntamente com seu analista desenvolvedor.

|  |  |  |
| --- | --- | --- |
| **Nome:** | **Título:** | **Descrição:** |
| [**MT261MEM**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087763) | Adiciona campos memos virtuais de usuários | LOCALIZAÇÃO : Function Mata261- Função de Transferência - Modelo II.  EM QUE PONTO : No momento em que o sistema carrega o Array Principal (aMemos), onde é possível adicionar os campos memos virtuais de usuários. |
| [**M261FILB**](https://tdn.totvs.com/pages/releaseview.action?pageId=236602039) | Verificação de filtros na Mbrowse da Função MATA261 | LOCALIZAÇÃO: Ponto de entrada localizado na rotina Transf. (mod.2)  EM QUE PONTO: É executado antes que seja exibida a tela principal da rotina. Este ponto de entrada tem como objetivo permitir que o usuário filtre os dados a serem exibidos. |
| [**MA261CPO**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087616) | Inclui campos para digitação em array | LOCALIZAÇÃO : Localizado nas funções A261Visual( ) , A261Inclui( ) e A261Estorn( ).  EM QUE PONTO : E chamado logo após a criação do array aHeader que controla quais campos aparecerão no browse das transferências. Pode ser utilizado para inclusão de campos no array já mencionado, permitindo ao usuário incluir mais campos para digitação. O array aHeader e montado baseado em campos do arquivo SD3. |
| [**MA261IN**](https://tdn.totvs.com/display/public/PROT/MA261IN+-+Preenche+valores+de+campos+na+tela+de+estorno) | Preenche valores de campos na tela de estorno | LOCALIZAÇÃO : Localizado nas funções A261Visual( ) , A261Inclui( ) e A261Estorn( ).  EM QUE PONTO : E chamado após a montagem do array aCols com as linhas do browse das transferências, nas rotinas de visualização e estorno de transferências. Pode ser utilizado para preenchimento dos valores de campos que o usuário queira apresentar na tela. Não esquecer de verificar a posição correta do campo a ter o valor atribuído no array aCols. A melhor forma de fazer isto e verificando a posição correta através de pesquisa no array aHeader. |
| [**M261BCHOI**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087569) | Montagem de array com botões na tela de inclusão | Localização: localizado nas funções A261Visual( ), A261Inclui( ) e A261Estorn( ).  Em que ponto: na montagem da interface das rotinas. |
| [**MT261CAB**](https://tdn.totvs.com/display/public/PROT/TVKQCT_DT_PONTO_ENTRADA_MT261CAB) | Monta cabeçalho customizado | Permite incluir campos customizados no cabeçalho da rotina de Transferência Mod. II. |
| [**MA261TRD3**](https://tdn.totvs.com/pages/releaseview.action?pageId=172295639) | Atualiza campos após a gravação da transferência | Localização: função a261Inclui() - responsável pela digitação e inclusão das informações para a transferência.  Em que ponto: após a chamada da função a261Grava() em um ponto externo à transação do banco de dados. |
| [**MTA261CAN**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087812) | Exibe alguma mensagem ou atualiza arquivos/campos do usuário | LOCALIZAÇÃO : Nas funções A261Inclui (Inclusão da Transferência do Produto) e A261Estorn (Estorno da Transferência do Produto).  EM QUE PONTO: Após cancelar a opção, na desistência da Inclusão ou Estorno; pode ser utilizado para exibir alguma mensagem ou atualizar arquivos/campos do usuário. |
| [**MA260NFQ**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087615) | Oculta tela de seleção de materiais para o CQ | LOCALIZAÇÃO : Localizado na função A261Grava( ) antes da geração dos movimentos de origem.  EM QUE PONTO : Este Ponto de Entrada tem o objetivo de não exibir a tela para seleção de materiais a serem transferidos para o CQ, quando houver integração com o Quality. |
| [**M261D3O**](https://tdn.totvs.com/pages/releaseview.action?pageId=236602023) | Atualiza campos ou arquivos na gravação | LOCALIZAÇÃO: localizado na gravação dos movimentos de origem na função A261GRAVA( ).  EM QUE PONTO: é chamado na gravação de cada registro de transferência de origem no SD3. |
| [**MT261TDOK**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087931) | Customizações após a gravação da Transferência Mod. II | Localização: Está localizado na função a261Grava.  Quando: O ponto é chamado no final da função após a gravação. Finalidade: Efetuar Customizações após a gravação da Transferência Mod. II. |
| [**MA261LIN**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087621) | Valida movimento de transferência | LOCALIZAÇÃO : Localizado no final da função A261LinOk( ).  EM QUE PONTO : E chamado no final da validação da função A261LinOk( ), que será chamado para cada linha de transferência incluída no Browse. Pode ser utilizado para validar o movimento. |
| [**A261PROD**](https://tdn.totvs.com/pages/releaseview.action?pageId=236421747) | Realiza inicializações adicionais de campos na SD3 | LOCALIZAÇÃO : Localizado no final da função A261VldCod( ).  EM QUE PONTO : Este ponto tem o objetivo de realizar inicializações adicionais de campos da tabela SD3 quando o usuário informar o código do produto no array do acols . Este ponto e executado no final da função A261VldCod( ). |
| [**MT261UM**](https://tdn.totvs.com/display/public/PROT/PEST07665_MT261UM_Trata_a_conversao_de_Unidades_de_Medida_e_validacao_dos_campos) | Trata a conversão de Unidades de Medida e validação dos campos | LOCALIZAÇÃO : Localizado na função A261Quant( ) responsável por tratar Conversão de Unidades de Medida e Validação dos campos ( Quantidade e Quantidade Secundária).  EM QUE PONTO : No final da função, antes de retornar a variável que controla o status da validação executado pela função. |
| [**A261LOC**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087513) | Cria no SB2 o produto no item da transferência | LOCALIZAÇÃO: Localizado na função A261Almox( ) antes da validação do produto origem / local origem na tabela SB2.  EM QUE PONTO : O objetivo deste ponto de entrada e criar na tabela SB2 o produto de origem e local de origem informados no item da transferência antes da validação de armazém da função A261Almox( ). |
| [**MA261EST**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087618) | Valida efetuação de estorno | LOCALIZAÇÃO : Localizado no final da função A261EstrOk( ).  EM QUE PONTO : Este ponto de entrada é chamado após a confirmação do estorno das transferencias. Pode ser utilizado para validar se o estorno pode ser efetuado ou não. |
| [**MTA261MNU**](https://tdn.totvs.com/pages/releaseview.action?pageId=6089473) | Insere novas opções no array aRotina | Localização.: Function MenuDef - Adiciona botões ao Menu Principal através do array aRotina.  Finalidade: o ponto de entrada MTA261MNU tem a finalidade de inserir novos botões no array aRotina (Array Private) |
| [**A261TOK**](https://tdn.totvs.com/pages/viewpage.action?pageId=679168137) | Customizações no momento em que se valida a transferência. | Está localizado na função a261TudoOk que tem o Objetivo de verificar a transferência |

**Saiba mais;**

[*MP - SIGAEST - MATA240 - Pontos de Entrada da rotina Movimentação Simples*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004532861)

[*MP - SIGAEST - MATA241 - Pontos de Entrada da rotina Movimentação Múltipla*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004558141)

[*MP - SIGAEST - MATA185 - Pontos de Entrada da rotina Baixa de Pré-Requisição ao Armazém*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004530301)

[*MP - SIGAEST - MATA175 - Pontos de Entrada da rotina Baixa de CQ*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004325941)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
