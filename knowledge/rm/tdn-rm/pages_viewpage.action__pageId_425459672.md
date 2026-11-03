---
content_hash: fe6bec23f2d82954d0b13f08035f75267d3973a0545261251932f6aa113e1ff7
fetched_at: '2026-06-29T00:09:38.016635+00:00'
page_id: '425459672'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x BackOffice Protheus - Configuração e Parâmetros Linha
  RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459672
version: 4
---

**Configuração e Parâmetros Linha RM**

---

**Assistente de Configuração TOTVS Business Conector**   
    
 O TBC possui uma interface de configuração específica para cada pacote de integração. Após o atendimento dos pré-requisitos, é necessário acessar o Assistente de Configuração, selecionar a integração TOTVS Obras e Projetos x BackOffice Protheus e executar o assistente.  
    
 A configuração, que acontece automaticamente, servirá para criar no banco de dados algumas stored procedures utilizadas nesta integração específica e demais ajustes necessários na base de dados RM.  
    
 **Nota:** A execução do Wizard de Configuração deve ocorrer, quando ocorrer alterações via atendimentos, pois durante correção é realizado manutenções no configurador.    
    
 **Assistente de Implantação de Processos do TOTVS Business Conector**  
    
 O TBC possui uma interface de parametrização específica para cada pacote de integração. A parametrização servirá para ativar/desativar a integração e para o usuário devidamente autorizado informar os parâmetros necessários para o seu funcionamento.  
    
 No Assistente de Implantação de Processos, selecione a integração TOTVS Obras e Projetos (TOP) x BackOffice Protheus, e avance para visualizar os parâmetros referentes ao RM.  
 **Gerais**

* **Ativar Integração:** marque a flag para ativar a integração.
* **URL WebService do Protheus:** informe o endereço do Web Services do BackOffice Protheus.

**Liberação de Pedido de Venda**

* **Tipo:** Informe o tipo de pedido.
* **Tipo do Cliente:** Informe o tipo de cliente.

Os parâmetros Tipo e Tipo do Cliente podem ser preenchidos caso deseje configurar o valor default a ser enviado na geração de Pedidos de Venda pela liberação de medições de contrato no TOP. Caso estes parâmetros não sejam preenchidos, será enviado o valor "N" (Normal) para o parâmetro Tipo, e o valor "F" (Consumidor Final) para o parâmetros Tipo do Cliente.  
    
 **Atenção:** No ambiente **México** esta configuração é obrigatória.  
    
 **Sincronizar Projeto/ Tarefa**  
 Devem ser assinalados os status do projeto que serão sincronizados. Os status disponíveis são:

* Em Andamento
* Paralisado
* Concluído
* A Executar
* Em Negociação
* Revisado
* Cancelado

Os projetos que tiverem o status selecionado para sincronização serão enviados ao Protheus. Se um projeto que foi sincronizado entrar em um status que não está selecionado nos parâmetros de configuração, o mesmo será excluído do Protheus mas estará disponível no TOP normalmente. Caso o projeto volte a um status que esteja configurado para ser sincronizado, o mesmo será enviado novamente ao Protheus.  
    
 **Processos Correlatos**  
    
 Durante a parametrização são apresentados os processos correlatos de cada etapa. Processos correlatos são os processos do Corpore RM que serão influenciados pela parametrização que esta sendo realizada. No TBC não existem processos correlatos.
