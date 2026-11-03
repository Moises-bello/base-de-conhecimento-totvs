---
content_hash: 9e3e28d9ef32e3117ce2b810e10db2d0b20d23ace6c2b57e348e330eefe67151
fetched_at: '2026-06-29T00:09:37.965276+00:00'
page_id: '425459659'
product: rm
source: tdn-rm
title: Sincronização de Registros via atividade de Fórmula Visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459659
version: 2
---

**Sincronização de Registros via atividade de Fórmula Visual**

---

Visando facilitar a sincronização de dados em massa entre o RM e sistemas integrados via Mensagem Única TOTVS, foi desenvolvida uma atividade de fórmula visual que se responsabiliza por, a partir de alguns parâmetros, obter os dados necessários e solicitar o envio da Mensagem Única TOTVS para o sistema de destino.  
    
 Basicamente é necessário informar a esta atividade somente a lista de chaves dos registros que se deseja integrar, qual a Mensagem Única a enviar e qual o objeto de negócio (DataServer) responsável por retornar as informações do registro. A partir destas informações a atividade se responsabiliza pela leitura, transformação e envio dos dados ao sistema de destino, oferecendo como retorno o Log de integração.  
    
 Todas as mensagens trafegadas também constarão no monitor da fila de integração, para posterior conferência.  
     
 **1. Cadastramento da atividade de Fórmula Visual**  
    
Para cadastrar a atividade de fórmula visual acesse: MDI RM | aba Gestão | Fórmula Visual | Atividades  
 Deve-se incluir a ativdade fórmula visual de envio de mensagens, que não é visível por padrão, conforme informações abaixo:

|  |  |
| --- | --- |
| **Campo** | **Valor** |
| Descrição | Sincronizar via Mensagem Única TOTVS |
| Nome da Classe | RM.Mov.FormulaVisual.Activities.MovCargaInicialTotvsMessageActivity |
| Nome do Assembly | RM.Mov.FormulaVisual.Activities |
| Ativo | Sim |

**2. Utilização da atividade de Fórmula Visual**  
     
 Para fazer uso da atividade de fórmula visual acesse: MDI RM | aba Gestão | Fórmula Visual | Fórmula Visual  
     
 Similar a outras atividades de fórmula visual, esta pode ser inserida em meio a um fluxo complexo e com parâmetros dinâmicos obtidos durante o mesmo.  
    
 Segue descrição dos parâmetros disponíveis na atividade:  
 Activity

* **Nome:** Nome apresentado no fluxograma
* Descrição: Descrição longa da atividade
* **Habilitado:** Indica se atividade está ativa ou não

Contexto

* CodColigada: Código da empresa do contexto de execução.
  + Caso seja passado "-1" (valor padrão), será obtido o dado do contexto da aplicação internamente à atividade.
* CodFilial: Código da filial do contexto de execução.
  + Caso seja passado "-1" (valos padrão), será obtido o dado do contexto da aplicação internamente à atividade.
* CodUsuario: Código do usuário do contexto de execução.
  + Caso seja passado vazio (valor padrão), será obtido o dado do contexto da aplicação internamente à atividade.

Mensagem Única

* **Id. Mensagem:** Identificador da mensagem a ser trafegada. Exemplo: ITEM = Produto.
* **Versão Mensagem:** Versão da mensagem a enviar. Exemplo: 1.000

Parâmetros

* **Consulta SQL:** Consulta SQL responsável por informar quais os registros a serem integrados.
  + É necessário que todos os campos chave do registro façam parte da tabela.
* **Tabela de Chaves:** Tabela com informação dos registros a integrar.
  + É necessário que todos os capos chave do registro façam parte da tabela.
* **Nome do DataServer:** Nome do DataServer responsável pelo registro.
  + O DataServer deve ser responsável por fornecer todos os dados para a formação da mensagem (parâmetro de entrada do EAI).
* Log: Log da executação da atividade.
  + Também é gerado o log de execução fisicamente no caminho "Raiz/CargaInicial/Logs/".

***Nota:*** *É necessário que seja informada a Consulta SQL ou Tabela de Chaves obrigatoriamente. Caso as duas sejam informadas, será utilizada a informação disponível no parâmetro Tabela de Chaves.*

---

**Recursos Adicionais**

Para ver exemplos da sincronização de registros via atividade de fórmula visual selecione os boletins técnicos abaixo:

[Exemplo de Sincronização por Consulta SQL](http://tdn.totvs.com/download/attachments/105316820/BT+-+Exemplo+de+Sincroniza%c3%a7%c3%a3o+por+Consulta+SQL.pdf?version=1&modificationDate=1385665076000)  
 [Exemplo de Sincronização por Tabela de Chaves](http://tdn.totvs.com/download/attachments/105316820/BT+-+Exemplo+de+Sincroniza%c3%a7%c3%a3o+por+Tabela+de+Chaves.pdf?version=1&modificationDate=1385665076000)  
 [Exemplo de Sincronização de Registros por Seleção na Visão](http://tdn.totvs.com/download/attachments/105316820/BT+-+Exemplo+de+Sincroniza%c3%a7%c3%a3o+por+Sele%c3%a7%c3%a3o+na+Vis%c3%a3o.pdf?version=1&modificationDate=1385665076000)
