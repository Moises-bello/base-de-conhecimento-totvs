---
article_id: 360015878451
category: Financeiro - Contas a Receber
content_hash: 23d205bd0e0225e13a9112a72c0b4af7b64d11ac0b3bdb647d7d5a8adf70dfc7
fetched_at: '2026-06-28T22:38:13.991858+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA330 - Comissão
  na compensação com NCC/RA
type: support-article
updated_at: '2022-07-29T02:36:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015878451-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA330-Comiss%C3%A3o-na-compensa%C3%A7%C3%A3o-com-NCC-RA
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como gerar comissão na compensação **NCC**/**NF** - **RA**/**NF**?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. **Tabela Motivos de baixa**  
   Cadastre na tabela de motivos de baixa (**Miscelânea** > **Arquivos**), o motivo **CMP** e habilite o cálculo de comissão no motivo de baixa. Exemplo:  
   Sigla: **CMP**  
   Descrição: Compensac  
   Carteira: A (Ambas)  
   Mov. Bancaria: N  
   Comissão: S  
   Cheque: N
2. **Parâmetros****MV\_TPCOMIS** - indicador se a comissão será executada de forma *ON* ou *OFFLINE* - Conteúdo O(*ONLINE*) ou B(*BATCH*).  
     
   **MV\_COMISCR** - indicador que permitirá o cálculo de comissão para vendedor na compensação **CR**.   
   Pergunta = Sim para calcular  
   Pergunta = Não para não calcular.
3. A comissão sobre a compensação CR(**FINA330**) poderá ser calculada desde que o título financeiro (**NF**) esteja configurado corretamente com vendedor e percentual e as perguntas do **F12** da rotina Compensação CR(**FINA330**) e o parâmetro abaixo estejam configuradas com Sim conforme o tipo de título que será compensado - **NCC ou RA.**
4. **Calc comiss s/ NCC**?  
   Informa se o sistema deve calcular comissão nas compensações com títulos de crédito do tipo **NCC**.  
   Pergunta = Sim- O sistema calcula comissão.  
   Pergunta = Não - O sistema não calcula comissão.
5. **Calc comiss s/ RA**?  
   Informar se o Sistema deve calcular comissão nas compensações com títulos de crédito do tipo **RA**.  
   Pergunta = Sim - O sistema calcula comissão.  
   Pergunta = Não - O sistema não calcula comissão.
