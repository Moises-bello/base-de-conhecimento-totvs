---
article_id: 1500007469322
category: Inspeção de Processos (SIGAQIP)
content_hash: 2e23a92963e77994a186101b9d275baf5b99ac912a76172a6fb4b5733e0d6f47
fetched_at: '2026-06-28T22:42:25.739685+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Existe ensaio obrigatório que não foi preenchido,
  para que seja possível informar o laudo do Laboratório, será sugerido laudo reprovado,
  deseja continuar
type: support-article
updated_at: '2022-03-18T14:09:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007469322-Manufatura-Linha-Protheus-SIGAQIP-Existe-ensaio-obrigat%C3%B3rio-que-n%C3%A3o-foi-preenchido-para-que-seja-poss%C3%ADvel-informar-o-laudo-do-Laborat%C3%B3rio-ser%C3%A1-sugerido-laudo-reprovado-deseja-continuar
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:10 min**  
**Ocorrência**No módulo **SIGAQIP - Inspeção de Processos**, ao confirmar a inspeção do resultado na rotina **QIPA215 - Resultados** é exibida a mensagem **Existe ensaio obrigatório que não foi preenchido, para que seja possível informar o laudo do Laboratório, será sugerido laudo reprovado, deseja continuar?**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Causa**A mensagem é exibida quando o ensaio está definido como obrigatório na especificação do produto, e durante a inspeção, não foram informadas as medições deste ensaio. Desta forma, como o ensaio é obrigatório, a rotina **QIPA215** entende que o laudo não pode ser aprovado sem medições.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se está correto o ensaio estar cadastrado como obrigatório. Esta validação é realizada na rotina **QIPA010 - Especificação do Produto** onde o campo **Ensaio Obrig** para o ensaio em questão, está preenchido como **Sim**;  
2. Se estiver correta a parametrização do ensaio, será necessário informar a medição para o ensaio em questão durante a inspeção do produto.
