---
content_hash: df6845605153530b55fe669e0890c4a2b6352e2bfd9cb72c620c56fe25eec2a1
fetched_at: '2026-06-29T00:09:48.619609+00:00'
page_id: '435105206'
product: rm
source: tdn-rm
title: Novidades 11.50 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105206
version: 2
---

**Novidade da Versão 11.50**   
**11.50.0 - Gerar Segunda Via de Boleto**  
Foi implementado no Totvs Incorporação o recurso de Gerar Segunda Via de Boleto que é realizado pela *Web*.  
   
**11.50.0 - Seguro por Empreendimento**  
Foi aprimorado o processo de Seguro por Empreendimento, na edição de componentes foi disponibilizado o campo "Compõe valor base para Cálculo do Seguro" que pode ser utilizado para os componentes de Juros e CM.  
   
**11.50.0 - Edição da Venda / Aluguel para os Campos Complementares**  
Foi aprimorada a edição da Venda / Aluguel a aba de Dados Adicionais a qual armazena 10 datas opcionais, 5 tabelas opcionais e um campo de observação irá ser convertida em campos complementares na aba Campos Complementares do cadastro de Vendas / Aluguéis.  
Com esta alteração teremos as seguintes modificações no sistema:

* O cadastro de tabelas opcionais do Totvs incorporação será excluído. Tab OP1, Tab OP2, Tab OP3, Tab OP4 e Tab OP5.
* Os parâmetros por coligada referentes aos campos de Data Opcional e Tabela Opcional da venda serão todos excluídos.
* Todos os campos que estão marcados para utilização na parametrização e que estão na aba Dados Adicionais do cadastro de Venda / Aluguel serão movidos para a aba de Campos Complementares.
* A aba de Dados Adicionais será removida do cadastro de Venda / Aluguel.   
     
  **11.50.0 - Anexo de Compradores**  
  Implementado o cadastro de Compradores, como Anexo da Venda, onde poderemos inserir vários compradores em um determinado contrato e destiná-los a cada componente da Regra do Financiamento. Este irão substituir os Agentes complementares da Venda/Aluguel.  
     
  **11.50.0 - Comissão**  
  No cadastro de comissão foi criado um campo para guardar o valor da comissão e outro para guardar o histórico de execução da fórmula utilizada para este cálculo.  
     
  **11.50.0 - Aprimorado processo de Tabela de Preço**  
  Foi criado um novo modelo de tabela de preço no qual é possível versionar a tabela através de reajuste.  
  O usuário cadastra uma nova tabela e depois aplica esta tabela em um empreendimento específico.  
  Depois de aplicada a tabela pode ser reajustada para manter os preços das sub-unidades atualizados.  
     
  **11.50.0 - Aditivo Troca de Comprador**  
  Foi aprimorado o Aditivo Troca de Comprador. Foram unificados os aditivos de Troca de Comprador e Agente Complementar. Agora na versão 11.60 o conceito de Agente Complementar vai ser descontinuado e poderemos ter mais de um Comprador em conjunto e inclusive assumindo grupos de parcelas.  
     
  **11.50.0 - Navegador**  
  Implementado uma visão especializada (NAVEGADOR) para busca de sub-unidades, auxiliando a venda e ou aluguel do mesmo.  
     
  **11.50.0 - Propostas de Vendas**  
  Foi desenvolvido o recurso de Wizard de Geração de Plano de Financiamento com Comparativo da Modalidade Padrão.  
  Esta novidade está disponível em uma nova aba chamada Propostas onde será possível utilizar as funcionalidades Estande de Imóveis e Proposta de Venda.  
     
  **11.50.0 - Anexo de Vendedores**   
  Foi aprimorado o Cadastro de Vendedores, para isso foi criado um anexo chamado Vendedores na edição de Vendas / Aluguéis.  
  Esta melhoria implicará na:
* Remoção do cadastro de tipo de vendedores.
* Remoção dos cadastros de vendedor pessoa física e jurídica.
* Remoção dos campos de vendedor pessoa física e jurídica da venda/aluguel.
* Criação do anexo de vendedores na venda.
* Deslocamento do anexo de comissões da venda para o anexo de vendedores.
* Conversão das comissões geradas pelo processo de conta corrente para o novo modelo de comissões por fórmula.
