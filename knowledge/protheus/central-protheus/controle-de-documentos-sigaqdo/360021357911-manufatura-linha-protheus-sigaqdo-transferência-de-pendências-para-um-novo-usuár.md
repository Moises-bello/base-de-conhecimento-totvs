---
article_id: 360021357911
category: Controle de Documentos (SIGAQDO)
content_hash: 87c3538a24609c5e19d16dfb8f30f2f88551532bb9529fc60d21921edacb75c7
fetched_at: '2026-06-28T22:42:29.955680+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Transferência de pendências para um
  novo usuário
type: support-article
updated_at: '2025-05-16T20:18:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021357911-Manufatura-Linha-Protheus-SIGAQDO-Transfer%C3%AAncia-de-pend%C3%AAncias-para-um-novo-usu%C3%A1rio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19384067163415)***Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como **transferir as pendências** do usuário atual para um novo usuário?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Para transferir **todas** as pendências de um usuário para outro, realize os seguintes passos:  
1. Realize *login* no Sistema com um usuário diferente do usuário que possui as pendências.  
2. Acesse a rotina **QAXA010 -****Cadastro de usuários**, selecione o usuário que possui as pendências à serem transferidas.  
3. Clique no botão **Outras Ações** > **Transferir Responsabilidade**.  
4. Informe a **data inicial** e **data final\*** dos documentos à serem transferidos e clique em **OK**.  
5. Selecione o **tipo de pendência** e o **usuário** destino.  
6. No lado direito da tela, selecione as opções **Selecionar**, Pendências **Ambas** e **Transferir sem baixar**.   
7. Clique no botão **Marcar/Desmarcar Usuários** para selecionar as pendências que serão transferidas.   
8. Clicar em **Confirmar**.  
  
Para transferir apenas algumas pendências de um usuário, poderá seguir o mesmo passo a passo acima e marcar a opção **Por Documento** existente no lado direito da tela.  
  
**Importante**O usuário destino deverá ter permissão para receber a pendência. Exemplo: Se a pendência for de elaboração, o usuário destino deve pertencer ao departamento e cargo que possui esta permissão. Esta configuração é realizada no **QDOA020 - Cadastro de Tipo de Documento** em **Outras Ações** > **Respons**.   
  
Caso o usuário destino já possuir a pendência em questão, por pertencer ao mesmo departamento e função do usuário de origem, não será necessário transferir a pendência. Basta inativar o usuário de origem para que o mesmo deixe de receber novas pendências.   
  
Recomenda-se que o procedimento acima seja realizado inicialmente em ambiente de testes ou homologação para melhor entendimento do fluxo do processo.

\*Os filtros iniciais são apresentados quando parâmetro MV\_QDOFTRA estiver marcado.  
  
**Complemento**[Manufatura - Linha Protheus - SIGAQDO - Exibir documentos cancelados para transferência de pendências](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7400083254295-Manufatura-Linha-Protheus-SIGAQDO-Exibir-documentos-cancelados-para-transfer%C3%AAncia-de-pend%C3%AAncias)  
[Manufatura - Linha Protheus - SIGAQDO - Não há lançamentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409189097111-Manufatura-Linha-Protheus-SIGAQDO-N%C3%A3o-h%C3%A1-lan%C3%A7amentos)  
[Manufatura - Linha Protheus - SIGAQDO - Opções de Transferência de Responsabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19383942363415-Manufatura-Linha-Protheus-SIGAQDO-Op%C3%A7%C3%B5es-de-Transfer%C3%AAncia-de-Responsabilidade)
