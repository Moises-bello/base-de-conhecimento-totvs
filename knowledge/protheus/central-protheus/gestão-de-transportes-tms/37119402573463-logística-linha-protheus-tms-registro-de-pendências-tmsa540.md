---
article_id: 37119402573463
category: Gestão de Transportes (TMS)
content_hash: d7bafb7f204855937664153592c427eefbe52a0fa3d9dea64ac18151b86c20a1
fetched_at: '2026-06-28T22:45:32.525716+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Registro de Pendências - TMSA540
type: support-article
updated_at: '2026-02-04T20:13:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37119402573463-Log%C3%ADstica-Linha-Protheus-TMS-Registro-de-Pend%C3%AAncias-TMSA540
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37119419905815) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Como utilizar a rotina **Registro de Pendências - TMSA540**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões.  
  
**Solução**  
Através do **Registro de Ocorrências - TMSA360** é possível registrar uma ocorrência do tipo **Gera Pendência.**   
Esse tipo de ocorrência é informado para controlar os problemas ocorridos com a mercadoria transportada, como por exemplo: mercadoria avariada, sobra, falta, bloqueios, entre outros.  
  
Após registrar uma ocorrência do tipo **Gera Pendência**, será criado um registro na rotina **Registro de Pendências - TMSA540**, onde poderá ser alterado, indenizado, encerrado ou estornado.  
O registro permanecerá em aberto até que a pendência seja solucionada, após solucionar, poderá encerrar a pendência.  
  
A ocorrência do tipo **Estorna Pendência** é apenas informativa para controle, visto que a ação de encerramento da pendência deve ser feita conforme processo: na tela **Registro de Pendências**, selecione o registro e clique em **Encerrar** > irá abrir a tela com a ocorrência, vá na aba **Encerramento** e adicione alguma informação no campo **Obs. Encerra - DUU\_OBSENC** > **Confirmar**.  
  
Dependendo do motivo que originou a pendência, pode ser necessário realizar uma indenização.   
Para que uma pendência gere também uma indenização, é necessário solicitar a indenização, conforme os passos:

1. Na tela **Registro de Pendências**, clique em **Outras Ações** >**Indenizar**;
2. Na sequência é apresentada a tela **Registro de Pendências - Indenizar,** na qual são exibidos dados da ocorrência;
3. Informe o valor do prejuízo;
4. Para consultar as Notas Fiscais com avarias, clique em **Notas Fiscais com Avaria**;
5. Confira os dados e confirme;
6. Observe que o *status* da pendência foi alterado para**Indenização Solicitada**;
7. Para encerrar a pendência e gerar o registro de indenização, clique em**Encerrar**, caso contrário permanecerão dois registros, sendo uma para a pendência e outro para a indenização.

**Saiba mais**  
Para mais detalhes sobre os demais processos da rotina, verifique a documentação [Registro de Pendências (TMSA540 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=505769714), que orienta como efetuar manutenção no registro da pendência e emitir relatório das mesmas.  
Verifique também a documentação da rotina [Registro de Indenização (TMSA370 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=465393436), visto que as rotinas são ligadas uma à outra.  
  
**Anexos**  
Vídeo simulando o processo de registro da pendência e depois do encerramento da mesma.
