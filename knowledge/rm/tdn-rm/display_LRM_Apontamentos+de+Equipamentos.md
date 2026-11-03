---
content_hash: 1198898531a400f83ca3092d7eaef691089fc22d3fa1b81d9d5fe33360220d26
fetched_at: '2026-06-29T00:09:13.731871+00:00'
page_id: '421385098'
product: rm
source: tdn-rm
title: Apontamentos de Equipamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Apontamentos+de+Equipamentos
version: 1
---

**Apontamentos de Equipamentos**

---

Os apontamentos estão disponiveis através do menu Controle | Mobilidade | Equipamentos | Apontamentos de Equipamentos. Através dessa funcionalidade é possivel visualizar e editar algumas informações dos apontamentos realizados nos coletores móveis, ou seja, não é possivel adicionar ou excluir apontamentos manualmente.

* A seguir são listadas algumas das informações que estarão disponíveis para visualização:

Identificador do Coletor; Centro de custo; Tarefa; Equipamento; Motivo de Improdutividade; Data/Hora Início; Data/Hora Fim; Status; Horímetro; Quilometragem; Motivo de inconsistência.  
Com relação à edição, somente registros que tenham status "Pendente" poderão ser editados. Além disso, as definições de quais campos serão editáveis, será de acordo com o valor do parâmetro "Integrado com SIGA-MNT", conforme mostrado a seguir:   
Parâmetro "Integrado com SIGA-MNT" habilitado: Todos os campos estarão bloqueados.  
Parâmetro "Integrado com SIGA-MNT" desabilitado: alguns campos serão editáveis, são eles:  
Centro de custo Tarefa Equipamento Motivo de Improdutividade Data/Hora Início Data/Hora Fim  
O campo Horímetro será igual à Data/Hora Início – Data/Hora Fim.  
O campo status pode assumir um dos seguintes valores:   
*Pendente:* o apontamento "chegou" do coletor. *Enviado:* o apontamento foi enviado para o Manutenção de Ativos. *Apropriado:* foi gerada apropriação para o apontamento.  
**Exclusão de Apontamentos no Coletor**  
Essa nova funcionalidade permite que o apontamento de entrada possa ser excluído no coletor, antes de realizar o sincronismo com RM. A exclusão será realizada na tela de saída do apontamento, caso haja algum apontamento de entrada.  
**Observações:** Caso o campo centro de custo esteja preenchido, só será possível selecionar tarefas que estejam associadas ao centro de custo informado.  
**Exclusão de Apontamentos Enviados para o Manutenção de Ativos** Essa nova funcionalidade permite que ao se ter Integração com Manutenção de Ativos ativada, os apontamentos de Equipamentos enviados para Manutenção de Ativos (PROTHEUS), quando excluídos, envie-se uma notificação para o TOTVS Obras e Projetos. Todo apontamento de equipamento realizado pelo coletor, chega no TOTVS Obras e Projetos via mensageria única (EAI). Quando este apontamento é recebido no TOP, é realizado algumas consistências de verificação, como:

* Código da coligada deve ser valido na Integração.
* Código da Filial deve ser valido na Integração.
* Código do Equipamento deve existir no cadastro de Patrimônio.
* O centro de Custo deve existir no projeto

Tendo esse apontamento consistente, deverá realizar o envio para o Manutenção de Ativos (PROTHEUS) através dos processos. Após o envio desse apontamento, será realizado um controle através de status no TOTVS Obras e Projetos, sendo que, apontamentos com: Status Pendente: Apontamento enviado ao Protheus mas ainda não retornado para o TOP. Status Excluído:  Apontamento enviado ao Protheus, mas foi excluído por algum usuário no PROTHEUS. Status Integrado: Apontamento Enviado ao Protheus e retornado para o Solum como Custo.  
Apontamentos 'sem status', são apontamentos que não foram integrados com o PROTHEUS e possuem status de envio pendente. Quando o apontamento é enviado para o Manutenção de Ativos e o mesmo por algum motivo seja excluído, o TOP será avisado dessa exclusão. Ao receber um apontamento excluído do Manutenção de ativos o Totvs Obras e Projetos irá alterar o status de envio do apontamento para cancelado. Tendo cancelado o apontamento, o TOP automaticamente irá excluir a apropriação prevista vinculada ao apontamento, em: 'Controle > Apropriação de Serviços/Insumos'.  
**Observação:**  
Para esta funcionalidade existe uma aba dentro da edição do Apontamento do Equipamento chamada **'Mapa'**, durante o registro dos apontamentos informações da localização são coletadas e enviadas no sincronismo para o sistema, com isso é possível verificar as posições dos apontamentos do coletor. Para habilitar esta funcionalidade é preciso configurar em menu Ambiente > Parâmetros > Parâmetros Globais > aba Google, e preencher o campo 'Chave de identificação para o Google Maps'.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Apropriação de Apontamentos de Equipamentos  
   
Enviar Apontamentos para o Manutenção de Ativos  
   
Sincronização de Bens e Transferência de Filial e Centro de Custo  
Importação de Apontamentos de Equipamentos  
   
Associar Tarefa ao Apontamento
