---
article_id: 25332012045335
category: Gestão de Transportes (TMS)
content_hash: 6135f16c8a1418c6b1c3041170c7a344fe60080c4f4cdd3c30d4465df3ee585a
fetched_at: '2026-06-28T22:45:29.411925+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: 'Logística - Linha Protheus - TMS - MDFe Rejeição 219: Circulação do MDFe verificada'
type: support-article
updated_at: '2025-01-31T17:08:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25332012045335-Log%C3%ADstica-Linha-Protheus-TMS-MDFe-Rejei%C3%A7%C3%A3o-219-Circula%C3%A7%C3%A3o-do-MDFe-verificada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25332026071063) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como proceder quando ocorrer a rejeição **219 - Circulação do MDFe verificada** no cancelamento do **MDFe - Manifesto de Transporte Eletrônico**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**Conforme o manual do **MDFe**, a rejeição 219 ocorre quando o **MDFe** já possui registro de circulação verificada:

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25341244584727)

Se por acaso o caminhão não passou por nenhuma barreira fiscal e a **SEFAZ** esta rejeitando o cancelamento, então, será necessário abrir uma consulta protocolada junto a **SEFAZ**. Isso permitirá que avaliem o motivo da rejeição, uma vez que a rejeição é emitida diretamente pela **SEFAZ** e não há qualquer ação que possa ser realizada no **TMS** para autorizar o cancelamento.  
  
Caso a **SEFAZ** negue o cancelamento do **MDFe** ou você perca o prazo de cancelamento do **MDFe**, precisará encerrá-lo.  
  
Mas, se de fato, o caminhão teve o registro de circulação verificada, então, para encerrar este **MDFe** que teve o cancelamento rejeitado pela **SEFAZ**, o Sistema disponibiliza a opção de **Excluir Cancelados** no monitor de transmissão. Esta funcionalidade exclui os registros de cancelamento deste **MDFe** para permitir seguir com o seu encerramento.  
Para isso, é necessário que o monitor do **MDFe** seja aberto utilizando a opção de **Transmissão** igual a **3 - Cancelamento**, para que o **MDFe** aguardando cancelamento seja exibido, basta clicar na opção **Excluir Cancelados.**

![](https://tdn.totvs.com.br/download/attachments/853294912/image-2024-6-28_9-43-34.png?version=1&modificationDate=1719606718543&api=v2)

Se caso, desejar que os documentos da viagem sejam disponibilizados no Sistema novamente para serem reutilizados em uma nova viagem para serem devidamente transportados, então:

* Para deixar os documentos disponíveis para gerar uma nova viagem, é necessário que na viagem original registre uma ocorrência do tipo **04 - Retorna documento** para os documentos que precisar vincular a uma nova viagem:

![image2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25341259420311)

* Encerre a viagem e o **MDFe** atual;
* Crie uma nova viagem, preenchendo os documentos para seguir com o processo.

**Importante**Processo exclusivo com o parâmetro **MV\_MDFECAN=.T.**Caso seu **MV\_MDFECAN** esteja desativado, é necessário que habilite manualmente o **MDFe** na tabela **DTX - Manifesto de Carga** e delete o registro da tabela **DYN - Manifesto Eletrônico Cancelado**  
**Saiba mais**  
Opção Excluir Cancelados para Encerramento de **MDFe**: [Opção Excluir Cancelados para Encerramento de MDFE](https://tdn.totvs.com.br/pages/releaseview.action?pageId=853294912)
