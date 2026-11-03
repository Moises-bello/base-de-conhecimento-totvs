---
article_id: 19058821924247
category: Integração RM
content_hash: 2973d6ad49ed8caa5bf6b93d0bbc136f203f50ccb6b1e1ebbf3a74f76433dd6a
fetched_at: '2026-06-28T22:42:36.839840+00:00'
product: protheus
section_id: 360012117913
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Atualização de Valor em Abastecimentos
  - Protheus Gestão de Frotas - SIGAGFR - BackOffice RM
type: support-article
updated_at: '2023-12-01T14:13:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19058821924247-Manufatura-Linha-Protheus-MNT-Atualiza%C3%A7%C3%A3o-de-Valor-em-Abastecimentos-Protheus-Gest%C3%A3o-de-Frotas-SIGAGFR-BackOffice-RM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19058797961111) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como é realizada a atualização de abastecimentos na integração do **Gestão de Frotas - SIGAGFR** e **BackOffice RM**?

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integração RM - Todas as versões  
  
**Solução**Realizada implementação da aba **Abastecimentos** na rotina de **Atualização de Custos - MNTA386** para atualizar os custos dos **Abastecimentos - TQN**.  
Para apresentação dos abastecimentos a serem atualizados o Sistema considera o parâmetro de **Data do último fechamento do estoque - MV\_ULMES**, ou seja, são apresentados os abastecimentos cujo campo **Data de Abastecimento - TQN\_DTABAS**, seja superior à data informada no parâmetro.  
  
Os procedimentos para utilização são:

1. Acessar o módulo **Configurador - SIGACFG**;
2. Verificar os parâmetros:
   1. **MV\_ULMES - Data último fechamento do estoque.**
   2. **MV\_NGINTER - Indica se está integrado a outro ERP (L=Logix, R=RM, M=Mensagem Única, N=Não)** igual a **R=RM**;
3. Acessar o módulo **Gestão de Frotas - SIGAGFR**;
4. Em **Atualizações - Controle de Oficina - Backoffice**, acessar a rotina **Atualização de Custos - MNTA386**.- Serão apresentados os registros em duas abas, sendo **Ordens de Serviço** e **Abastecimentos**.  
   - Na aba **Abastecimentos** verificar se os abastecimentos a serem atualizados estão sendo apresentados.  
   - Caso sim, pressione a opção **Atualizar Custos.**   
   - Verificar que o Sistema irá apresentar mensagens de integração**StockLevel**e os **valores dos abastecimentos** serão atualizados.

**Saiba mais**Para ter acesso a documentação completa desse processo, acesse o *link* [Atualização de Custos - MNTA386 - SIGAGFR](https://tdn.totvs.com/pages/releaseview.action?pageId=520120870)
