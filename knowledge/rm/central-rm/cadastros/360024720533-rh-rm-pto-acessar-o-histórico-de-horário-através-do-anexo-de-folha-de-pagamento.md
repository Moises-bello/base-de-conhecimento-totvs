---
article_id: 360024720533
category: Cadastros
content_hash: 9835e40adcbad7af58b7cb2dea3b84f0ded63dc4afd809bb7b2be215a4762b7c
fetched_at: '2026-06-28T22:46:28.490916+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO -  Acessar o histórico de horário através do anexo de Folha de
  Pagamento no menu de funcionários
type: support-article
updated_at: '2025-02-20T15:56:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024720533-RH-RM-PTO-Acessar-o-hist%C3%B3rico-de-hor%C3%A1rio-atrav%C3%A9s-do-anexo-de-Folha-de-Pagamento-no-menu-de-funcion%C3%A1rios
---

**Dúvida**  
Como acessar o histórico de horário através do anexo de Folha de Pagamento (RM Labore) na visão de funcionários?  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto- A partir da versão 11.80  
  
**Solução**

Para acessar o histórico de horários através da opção Anexos | Folha de Pagamento do cadastro do funcionário. Siga os passos abaixo:

1. Acesse no módulo de **Serviços Globais**, o menu **Serviços** | **Actions do Sistema**.
2. Na visão de **Actions do Sistema**, acesse a opção **Processos** | **Atualização de actions cadastradas**.
3. Ao abrir a tela de atualização, marque a flag dos parâmetros '**Atualiza a tabela com informações das actions encontradas no broker'** e '**Adiciona a tabela actions encontradas no broker**' e clique em executar. ![MvCyGmSIvg.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22655616204311)
4. Acesse no módulo de **Automação de Ponto** ou **Folha de Pagamento**, o menu **Cadastros | Funcionários**.
5. Acesse a opção **Anexos | Configurar Anexos**.
6. Ao abrir a tela de **Configurações dos anexos**, nos menus apresentados, selecione a posição em que o anexo irá ficar. (Para facilitar a visualização, recolha a árvore de menus).
7. Após selecionar a posição, clique no botão de **+Action** (adicionar action).
8. No campo de pesquisa, procure por **Histórico de horários**.  
   Obs.: Serão apresentados dois grupos: ***Folha de Pagamento e Ponto***. Clique na opção de **Folha de Pagamento**.
9. Clique sobre a action **Histórico de horários, r**ecém adicionada e no campo de **Relacionamento**, clique no botão **adicionar** e insira os dois relacionamentos CODCOLIGADA: PFHSTHOR.CODCOLIGADA e CHAPA: PFHSTHOR.CHAPA. Confira se a flag ativo está marcada e clique em ok para salvar os ajustes.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22713296474519)
10. Após seguir os passos, o anexo estará disponível para utilização.  
    ![KRBEu8nbHR.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22713134753431)
