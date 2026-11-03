---
content_hash: 2d01f1e36e22e2d519b754e16ab4497379e7d5b7a29d1a7864d8e937373d827c
fetched_at: '2026-06-29T00:09:37.180085+00:00'
page_id: '425459574'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x Backoffice Protheus - Processos - Adiantamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Obras+e+Projetos+x+Backoffice+Protheus+-+Processos+-+Adiantamento
version: 4
---

**Adiantamento**

---

A inclusão, alteração e exclusão do Adiantamento são realizadas no TOP. No Protheus são gerados os títulos a pagar e a receber. É utilizada a tecnologia Web Service para sincronizar os dados entre o TOP e o Protheus.

Para realizar o adiantamento, antes é necessário configurar os parâmetros do projeto. Selecione o projeto e acesse: RM | Projetos | Construção e Projetos | Opções | Construção e Projetos | Projetos  
    
 Na visão de parâmetros do projeto, acesse: Integração | Suprimento/Faturamento | Geral   
    
 O parâmetro Tipo do Movimento é configurado através do parametrizador da integração, e se encontrará como somente leitura. O parâmetro Produto Padrão deve ser configurado sempre que for realizar um adiantamento. O produto informado deve existir no Protheus e ser do tipo Serviço (mão de obra - MO).  
    
 Selecione o contrato e abra o Anexo Adiantamento de Contrato. Inclua um adiantamento e preencha os dados solicitados. Após execute o Processo Liberar Adiantamento. No Protheus será gerado um Título a Pagar caso o seja um Contrato a Pagar, ou um Título a Receber caso seja um Contrato a Receber.  
    
 Para visualizar o Título a Pagar acesse: Protheus | Siga Fin | Atualizações | Contas a Pagar| Contas a Pagar  
 Para visualizar o Título a Receber acesse: Protheus | Siga Fin | Atualizações | Contas a Receber| Contas a Receber  
    
 Para cancelar um adiantamento selecione o mesmo no Anexo Adiantamento de Contrato, e execute o Processo Cancelar Liberação de Adiantamento. O título será excluído do Protheus.

**Observação:**

**Adiantamento Localizado para Argentina**  
  
 O controle de adiantamentos para Argentina é diferente dos demais porque incidem impostos sobre esta operação financeira. Para Argentina o engenheiro irá solicitar ao departamento financeiro que faça o pagamento de um adiantamento a fornecedor (se contrato a pagar) ou que registre um adiantamento recebido (se contrato a receber).  Ou seja diferente da integração para Brasil em que o Titulo é gerado pela liberação de movimento no TOP, este Titulo parte do cadastro realizado no Próprio financeiro do Protheus.  
 Sendo assim o responsável do departamento financeiro efetua o registro no sistema (Protheus). E para permitir integração com o TOP, o adiantamento deve ser incluído já vinculado a um projeto (pré-requisito: sincronizar projetos e tarefas do RM para o Protheus). Mas o usuário do financeiro não conhece a informação de contrato, por isto o engenheiro é que terá que associar o adiantamento feito no financeiro (Protheus) ao contrato cadastrado no sistema de gestão de projetos (TOP). Ou seja, o engenheiro acessa o TOP busca na lista de adiantamentos qual ele deseja importar, e importar este adiantamento para o contrato.  
 Caso seja necessário cancelar/excluir o Adiantamento isto deve ser solicitado pelo Engenheiro no TOP, ou seja, ele deverá executar o processo de Cancelar Liberação de Adiantamento. Neste momento além de alterar o status do adiantamento para Cancelado (Liberado=0) o TOP, o Protheus irá desbloquear o Adiantamento correspondente no financeiro. A partir deste momento o Adiantamento está cancelado no RM e não pode mais ser liberado (esta função estará bloqueada) nem referenciado em Medição. Neste momento, se desejado pelo engenheiro o Adiantamento pode ser excluído no financeiro.  
  
**Versão:**

* RM 11.50.20 (patch Abril/12), 11.80.1 (patch de Maio/12) e posteriores.
* Protheus 11.5 e superiores (patch Abril/12).
