---
content_hash: 1e18bad97df742565b1e5b19855212670514d05562edea7c74e266245340e3ab
fetched_at: '2026-06-29T00:09:37.134555+00:00'
page_id: '425459565'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Efetuar Abertura de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Backoffice+RM+x+Protheus+SigaMNT+-+Efetuar+Abertura+de+Atendimento
version: 3
---

**Backoffice RM x Protheus SigaMNT - Efetuar Abertura de Atendimento**

---

Ao abrir um Atendimento é possível incluir Solicitações de Serviço e gerar Ordens de Serviço de Manutenção ou Manutenção de Terceiros por dentro da tela de Atendimento, possibilitando também que todas as funcionalidades e fluxo de Ordem de Serviço sejam executadas e assim feito o acompanhamento da mesma, que no inicio em que será criada com status pendente ou liberada até o Faturamento e reporte de horas em que a manutenção.  
    
   
    
 **Passos para a execução :**

**Pré-Condições:**

1: Cadastrar manualmente o DE-PARA de Coligada e Filial RM x Empresas e Filiais Protheus

2: Cadastrar os tipos de movimento:

* Acréscimo em estoque
* Apropriação de Custos
* Baixa de Estoque
* Ordem de Manutenção
* Ordem de Manutenção de Terceiros
* Solicitação de Armazém
* Solicitação de Compra

3: Sincronizar os Bens (Ativos Fixos) que sofrerão as manutenções.

4: Sincronizar os Locais de Estoque dos produtos a utilizar como Insumos

5: Sincronizar os Produtos / Serviços que serão utilizados como Insumos.

6: Sincronizar o Projeto de manutenção e suas Tarefas.

7: Sincronizar as Unidades de Medida.

8: Sincronizar os Centros de Custos.

9: Sincronizar um Funcionário.

10:Configurar o Parametro MV\_ESTNEG.

* S: Controla se a integração Permitirá estoque negativo
* N: Controla se a integração Não Permitirá estoque negativo

11: Configurar o Parâmetro MV\_NGGERSA. Este parâmetro controla se será gerada ou não Solicitações de Armazém.

* N –Gera solicitação de armazém e solicitação de compra para a quantidade de insumo excedida
* S – Gera Solicitação de Armazém

12: Vincular Funcionário ao Usuário Protheus

13:

**Abertura de Atendimento**

Passo 1- Em Atualizações / Controle de Oficina / Solicitação de Serviço / Atendimento.

Passo 2- Informar ao Tipo de Atendimento o valor : Atendimento Prestador

Passo 3- Incluir uma solicitação de serviço.

Passo 4- Preencha os campos abaixo e Confirmar.

A Solicitação de Serviço é adicionada ao Atendimento.

* Solicitação: Gerado automaticamente pelo Protheus
* Cod Cliente: Código do cliente
* Bem / Localiz: Código do Ativo Fixo.
* Data e Hora de Abertura
* Serviço: Serviço que foi cadastrado previamente para as Solicitações de Serviço.
* Tipo de Solicit: Tipo da solicitação
* Solicitante: Código do Funcionário

Passo 5-  Gerar uma Ordem de Serviço a partir de uma Solicitação de Serviço.

Passo 6- Seguir a execução do o processo de Inclusão de Ordem de Serviço

---
