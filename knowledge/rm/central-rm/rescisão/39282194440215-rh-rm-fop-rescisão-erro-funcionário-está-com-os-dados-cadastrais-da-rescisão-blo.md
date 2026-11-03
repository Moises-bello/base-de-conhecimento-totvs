---
article_id: 39282194440215
category: Rescisão
content_hash: b6e67ca61348a83bf624a77217bbda38fead4b05533f66917e097985786bc6b9
fetched_at: '2026-06-28T22:46:54.138605+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão - Erro: Funcionário está com os dados cadastrais
  da rescisão bloqueado'
type: support-article
updated_at: '2026-03-25T18:07:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39282194440215-RH-RM-FOP-Rescis%C3%A3o-Erro-Funcion%C3%A1rio-est%C3%A1-com-os-dados-cadastrais-da-rescis%C3%A3o-bloqueado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39282146834199) Tempo aproximado para leitura: **00:01:38 min**  
  
**Ocorrência**  
Ao tentar realizar o cálculo da rescisão ou gerar o líquido, o sistema apresenta a mensagem:  
**"Funcionário [Código] está com os dados cadastrais da rescisão bloqueado. Seus Dados não foram Alterados".**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
A mensagem ocorre devido à **ativação do parâmetro de controle de bloqueio de dados cadastrais da rescisão**. Quando esta opção está marcada, o sistema impede alterações ou cálculos se houver restrições ativas no período.  
  
**Solução**  
Para resolver, é necessário desativar a flag de controle nas configurações do sistema, conforme passo à passo:

1. Acesse o módulo **Folha de Pagamento** (RM Labore);
2. Vá em **Configurações** | **Parametrizador**;
3. No menu lateral, selecione a opção **Rescisão** | **Restrições Cadastrais**;
4. Desmarque o campo **Ativar controle de bloqueio de dados cadastrais da rescisão**;
5. Avance até o final para concluir e salvar a alteração dos parâmetros;
6. Realize um novo teste de cálculo ou geração do líquido.  
     
     
   ![image (2).png](https://centraldeatendimento.totvs.com/hc/article_attachments/39282146834839)

**Saiba Mais**

Para mais informações e dúvidas frequentes sobre o processo de rescisão, acesse:

* [RH - RM - FOP - Dúvidas frequentes: Processo de Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23511360882199-RH-RM-FOP-D%C3%BAvidas-frequentes-Processo-de-Rescis%C3%A3o)
