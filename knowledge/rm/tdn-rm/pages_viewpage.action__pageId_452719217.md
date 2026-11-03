---
content_hash: 3cda31c50a0324f4347b057690567bf94877b8593d8535a0dc3ba79c84b403a1
fetched_at: '2026-06-29T00:10:04.559132+00:00'
page_id: '452719217'
product: rm
source: tdn-rm
title: Retificação de Eventos do Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719217
version: 3
---

Neste módulo será gerada a retificação dos registros abaixo, para Integrar com TAF (Sistema da TOTVS responsável pela validação e transmissão dos dados para o governo):

* S-2200- Admissão /Ingresso de Trabalhador
* S-2205 -Alteração de Dados Cadastrais do Trabalhador
* S-2206 -Alteração de Contrato de Trabalho
* S-2300 -Trabalhados sem vinculo de emprego/Estatutário-inicio
* S-2306 -Trabalhados sem vinculo de emprego/Estatutário-Alteração Contratual

**Atenção:**

* + Não será possível gerar a retificação diretamente pela Fila de Eventos.
  + Não será possível retificar campos chaves.
  + Serão listados todos eventos com status 10-Aceito Ret, para a chapa selecionada.

Tela informação para retificação

**Chapa**

Selecione a chapa do funcionário que terá o(s) evento(s) retificados.

**Eventos**

Será apresentada uma lista com todos os eventos gerados para a chapa selecionada.

   
Tela Alteração dos valores do XML  
   
Nesta tela encontra-se os campos disponíveis para a retificação, para editá-lo basta selecionar o grupo na árvore e clicar no campo desejado, a tela apresenta o campo a direita para a correção.   
Para excluir uma tag basta selecionar o grupo na árvore, clicar no campo desejado e escolher a opção Deletar.  
   
**Legenda**  
   
Registro Multivalorados

Os campos Multivalorados (seu conteúdo é formado por mais de um valor) são construídos de acordo com os valores preenchidos na grid. Esse grid se comporta de duas formas:

* Ao clicar em "Carregar dados XML" é trazido as informações existentes do xml selecionado. Pode ser feito a edição ou exclusão dos registros em cada linha apresentada. Caso tenha selecionado mais de um xml do mesmo tipo o sistema trará as informações do primeiro xml conforme data do evento.
* Realizar a inclusão de uma nova lista. Observação: ao incluir uma nova lista os dados do xml('s) anterior(es) será(ão) substituído(s).

Tag Obrigatória

Campo obrigatório no XMl, estará em negrito, diferente dos campos de cadastro estes só serão preenchidos caso o cliente tenha alguma alteração ou adicione algum grupo que possua um campo obrigatório.  
TAG deletada: Campo excluído pela opção deletar.  
 

Tela Detalhamento de mudança  
   
Nesta tela o sistema apresenta um comparativo da tags que foram alteradas pelo processo.

|  |  |
| --- | --- |
|  | Como Fazer |

---

[**Como realizar o processo de retificação de eventos do funcionário**](http://tdn.totvs.com/pages/viewpage.action?pageId=416842991)
