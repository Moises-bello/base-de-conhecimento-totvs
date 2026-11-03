---
content_hash: 78936a6a1f80a0cbf14529d77611aa608607f397bdafd9d05095864ef274e00e
fetched_at: '2026-06-29T00:09:27.426067+00:00'
page_id: '423938518'
product: rm
source: tdn-rm
title: Item da Ordem de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938518
version: 4
---

**Pasta identificação - Ordem de Serviço**

Status: Status atual do item da OS (peças/materiais ou serviços).   
****Dica:**** O status para o material/peça será 'Peça destinada à oficina' quando esta for incluída na OS. E o status 'Peça utilizada em reparos' indica que já foi impresso um pedido de peça pelo técnico da oficina  
 Os status dos serviços são os seguintes:

* 'Aguardando Análise' (a OS recebe este status no momento em que ela é criada no sistema),
* 'Não iniciado' (quando o funcionário responsável ainda não começou a executar o serviço),
* 'Em andamento' (após iniciar o serviço, independente de quantas vezes for interrompido),
* 'Terminado' (quando o serviço for completamente executado),
* 'A faturar' (Após o cliente aprovar a manutenção realizada, o movimento deverá assumir este status.) e
* 'Faturado' (Após o faturamento (TOTVS Gestão de Estoque, Compras e Faturamento), o movimento assumirá este status na janela de visão de movimentos do RM Officina).

Cobrança de tempo efetivo: Marcando esta opção, sendo o item da OS um serviço a ser executado, será desconsiderado o valor do preço de tabela, multiplicando o tempo de execução do serviço pela hora padrão, conforme parametrizado em 'Cadastros | Tipos de Movimento | edição de um Tipo de Movimento | pasta Parâmetros Officina'   
 Início: Data de início da execução do serviço (não será preenchido quando se tratar de um produto). Quando se trabalha com Histórico Detalhado de Serviços este campo é preenchido automaticamente pelo sistema.  
 ***Observação:*** Caso o parâmetro "Controla Histórico Detalhado de Serviços", presente nos parâmetros do sistema não esteja selecionado, este campo estará disponível para edição.  
 Término: Data final de término da execução do serviço (não será preenchido quando se tratar de um produto). Quando se trabalha com Histórico Detalhado de Serviços este campo é preenchido automaticamente pelo sistema.  
Caso o parâmetro "Controla Histórico Detalhado de Serviços", presente nos parâmetros do sistema não esteja selecionado, este campo estará disponível para edição.  
 Tempo padrão (h): Refere-se ao tempo padrão em horas, para execução do item da Ordem de Serviço, parametrizado no TOTVS Gestão de Estoque, Compras e Faturamento em Cadastros | Produtos/Serviços | Edita o serviço | Pasta 'Características' | Campo 'Tempo do Serviço'. Ao inserir um item tratado como Serviço será apresentado o tempo determinado para o serviço neste campo.

**Apropriação**

Usuário: Indica qual usuário logado no sistema efetuou a apropriação do item na OS.

**Vida Útil do Item**

**Dia**: Exibe a quantidade de dias para que vença a vida útil do item selecionado

**Quilometragem**: Exibe a quilometragem que tem que ser atingida para vencer a vida útil do item selecionado.  
******Dica****:** Para que o sistema possa buscar as informações destes campos é necessário configurar previamente o vencimento da vida útil. Para isso basta acessar no RM Officina Cadastro | Produto | Anexo | Produtos – Informações de Manutenção e definir como a vida útil vai ser controlada (Ex: Dia, Quilometragens, hora etc).  
 Os campos de controle de Vida útil só estarão disponíveis se o item for do tipo produto, para serviços não é possível controlar a vida útil.   
 Alocação de Mão de Obra: Permite alocar a mão-de-obra necessária para execução da Ordem de Serviço, caso o item da mesma seja do tipo Serviço. Quando da OS for uma peça/produto, este botão não estará disponível pois não é possível alocar mão-de-obra para um produto. Também não é permitido alocar mão-de-obra para uma OS com o status Aguardando Análise.

**Pasta Observação:**Nesta pasta é possível detalhar o histórico de um item incluído na ordem de serviço, a fim de complementar informações relativas a execução de um determinado serviço.

**Pasta Mão de Obra:**Nesta pasta é possível selecionar uma mão de obra que será responsável pelo serviço do item selecionado.  
 ***Observação:*** Não é possível selecionar uma mão de obra para a ordem de serviço se a mesma estiver com status "Aguardando Análise"  
 Para escolher a mão-de-obra a ser alocada é preciso que esta seja cadastrada no menu Cadastro de Mãos-de-Obra e que também esteja vinculada ao objeto de manutenção, em Opções | Parâmetros | Tipo de Objeto de Manutenção | Edita o Objeto escolhido | Selecione a Pasta - Mãos-de-Obra, referenciado na ordem de serviço.

**Integração / Manutenção**  
 Obj. do RM Officina associado ao item mov: Neste campo pode ser visualizado o objeto de manutenção para qual a OS irá ser aberta. Clicando no objeto de manutenção o sistema exibirá a tela de cadastro de objeto de manutenção com todas as informações do objeto selecionado caso o usuário deseje buscar alguma informação referente ao objeto.  
 Atualizar Múltiplos Registros: Ao clicar neste botão o sistema permite ao usuário atualizar a data dos campos Início e Término que se encontram dentro da edição do item da OS na pasta Ordem de Serviço. Esse processo só poderá ser realizado para ordens de serviço que estiverem com status "em andamento" e para itens que forem do tipo serviço. Para habilitar este botão dentro do item o parâmetro "Controla Histórico Detalhado de Serviços" deverá estar desmarcado nos parâmetros do RM Officina.  
 ***Observação:*** O botão Atualizar Múltiplos Registros só é visível se o movimento for acessado de dentro do RM Officina, acessando o movimento pelo TOTVS Gestão de Estoque, Compras e Faturamento este botão não ficará visível mesmo que o parâmetro "Controla Histórico Detalhado de Serviços" esteja desmarcado no RM Officina.

**Produto Substituto/Similar**

**Menu Movimentos | Movimento | Aba item:**A funcionalidade Produto Substituto/Similar tem como objetivo permitir que o usuário substitua o item do movimento por um item substituto ou similar na Ordem de Serviço.  
 Para mais informações [cliquei aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=423938859).
