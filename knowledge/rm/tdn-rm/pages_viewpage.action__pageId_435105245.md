---
content_hash: bc8f0a3a784f5667a1b15d3321faae0ceec16262c4dcbce8891d27124d94936c
fetched_at: '2026-06-29T00:09:49.156877+00:00'
page_id: '435105245'
product: rm
source: tdn-rm
title: Novidades 11.40 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105245
version: 2
---

**Novidade da Versão 11.40**   
   
**Geração de contrato com situação 'Em Preparação' ou 'Efetivada'**  
Aprimoramento da função de Vendas e Alugueis, localizada em Contrato. Agora é possível gerar Contrato de uma venda com situação 'Em Preparação' ou 'Efetivada'.  
   
   
**11.40.0 - Foi aperfeiçoado o processo de Distrato**  
Agora o processo de Distrato terá etapas para a sua conclusão. Poderemos criar um Distrato e o mesmo ficar em Preparação até que seja aprovado por um fluxo de aprovação e posteriormente ser concluído. O Distrato será um anexo da Venda/Aluguel. O Fluxo de Aprovação é um recurso do produto RM e é opcional a sua utilização.  
   
**As etapas do Distrato são:**  
   
Em Aberto: Ao criar o Distrato, o mesmo ficará com o status "Em Aberto", onde iremos cadastrar as Informações básicas como data de cancelamento, motivo de cancelamento, evento contábil e Fórmula. O cálculo do distrato será por Fórmula e é realizado todas as vezes que uma informação for alterada e o distrato for salvo.   
   
Em Preparação: No processo de preparação do distrato, caso seja necessário devolver algum valor para o cliente, serão gerados lançamentos no financeiro para que seja feita a provisão dos valores financeiros.  
   
Efetivado: Caso o distrato seja efetivado não será possível desfazê-lo. Visto que os lançamentos financeiros não pagos que haviam sido cancelados na efetivação não poderão ser habilitados novamente. A efetivação do distrato contratual consiste em cancelar as parcelas em aberto e parcialmente quitadas no Totvs Incorporação, cancelar os lançamentos financeiros, carregar o evento contábil de distrato, incluir lançamento ou operação contábil, alterar a situação do contrato, incluir o histórico no contrato, alterar a situação da sub unidade e incluir o histórico de sub unidade.  
   
Cancelado: Caso o distrato seja confirmado, ele poderá ser cancelado, más a venda permanecerá Distratada, não retornando para o status de Efetivada. Os lançamentos financeiros de  devolução gerados serão todos cancelados e a contabilidade gerada será excluída ou estornada.   
   
**Para distratar uma Venda / Aluguel, a sua situação deve estar "Efetivada" e ter o número do contrato gerado.**  
   
**11.40.0 - Campo Complementar do Distrato**  
Foi implementado o Campo Complementar do Distrato, onde poderemos inserir novos campos no Distrato para que estes possam compor a fórmula que calculará o Distrato.  
   
**11.40.0 - Foi aperfeiçoado o processo de Aditivo**  
Agora o processo de Aditivo terá etapas para a sua conclusão. Poderemos criar um Aditivo e o mesmo ficar em Preparação até que seja aprovado por um fluxo de aprovação e posteriormente ser concluído. O Aditivo será um anexo da Venda/Aluguel. O Fluxo de Aprovação é um recurso do produto RM e é opcional a sua utilização.  
   
**As etapas do Aditivo são:**  
   
Em Preparação: Ao criar o Aditivo, o mesmo ficará com o status "Em Preparação", onde iremos cadastrar as Informações básicas como data do Aditivo, Descrição e selecionar o Tipo de Aditivo a ser executado. Poderemos selecionar mais de um tipo de Aditivo para ser executado simultaneamente e iremos cadastrar as informações de cada tipo de Aditivo.  
   
Efetivado: Ao efetivar o Aditivo, o sistema irá perguntar se o mesmo será contabilizado e iremos informar o evento contabil. A efetivação do Aditivo consiste em realizar as alterações contratuais de cada tipo de Aditivo selecionado, efetuar a contabilização e incluir o histórico do Aditivo. Caso o Aditivo seja efetivado, não será possível desfazê-lo ou cancelá-lo.  
   
Cancelado: Caso o Aditivo não esteja Efetivado, ele poderá ser cancelado.  
No Anexo Aditivo, temos o processo "Recontabilizar", onde poderemos efetuar a recontabilização do Aditivo, efetuando devidas alterações.  
   
**11.40.0 - Notas Promissórias**  
Aperfeiçoado Numeração de Notas Promissórias  
   
**11.40.0 - Conta Caixa na Geração da Venda**  
Aperfeiçoado inclusão automática da Conta Caixa na Geração da Venda conforme informado no Empreendimento  
   
**11.40.0 - Campos Complementares da Venda**  
Será permitida a edição de Campos Complementares em Vendas Efetivadas.  
   
**11.40.0 - Parâmetros retirados devido a sua inutilização em versões anteriores**  
Os parâmetros abaixo foram retirados devido a sua inutilização em versões anteriores.

* Tamanho do campo rua - Tamanho do campo número - Tamanho do campo complemento  
  MOTIVO DE REMOÇÃO: Campos do cadastro de cliente fornecedor que são de responsabilidade do financeiro.
* Utiliza campo classificação no evento contábil - Excluir contas contábeis zeradas - Manter: filial, percentual e históricos -  
  MOTIVO DE REMOÇÃO: Regras de negócio da nova tela de contabilização compartilhada do contábil.
* Cancelar Parcela Gerada a Banco
* Razão parcela - Prazo da tele cobrança - 2º estágio - Notificado - Mostrar tela de vendas atrasadas - Executar conversor de municipios ao iniciar o sistema - Consistir geração RM  
  MOTIVO DE REMOÇÃO: Funcionalidades descontinuadas em versões anteriores.  
     
  **11.40.0 - Contabilização - Totvs Incorporação**  
  O Totvs Incorporação foi aprimorado para atender a toda a demanda para o Novo Modelo de BackOffice do Totvs Gestão Contábil.  
     
  **11.40.0 - Integração Contábil**  
  Foi aprimorada a integração contábil no Totvs Incorporação, agora é utilizado o padrão para contabilização nos processos do Totvs Incorporação.  
     
  **11.40.0 - Reajuste - Tela de Confirmação** Foi implementado uma tela de confirmação de reajuste quando há vendas no sistemas que estão passando de Momento Antes Entrega para Momento Após Entrega.  
     
  **11.40.0 - Reajuste - Monitor de Reajuste** Após selecionar a venda e os grupos vinculados à venda selecionada, na tela Monitor de Reajuste, os componentes CM e Juros estarão detalhados mostrando os valores que foram calculados respectivamente.  
     
  **11.40.0. - Reajuste - Consultar Log**  
  Foi implementado o botão Consultar Log na tela de Reajuste que detalha os cálculos realizados e informando possíveis erros.
