---
article_id: 1500007484021
category: Inspeção de Processos (SIGAQIP)
content_hash: 3ddf9f3eba70ebff0fa9f8b9aeda5d1a51f7d51d5ea44109b2f95d0b3acd8cd4
fetched_at: '2026-06-28T22:42:25.736318+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQIP - Existe(m) ensaio(s) obrigatório(s)
  cuja medição não foi apontada, para que seja possível informar o laudo do Laboratório,
  favor apontar medições para o ensaio: XXX'
type: support-article
updated_at: '2021-06-04T19:14:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007484021-Manufatura-Linha-Protheus-SIGAQIP-Existe-m-ensaio-s-obrigat%C3%B3rio-s-cuja-medi%C3%A7%C3%A3o-n%C3%A3o-foi-apontada-para-que-seja-poss%C3%ADvel-informar-o-laudo-do-Laborat%C3%B3rio-favor-apontar-medi%C3%A7%C3%B5es-para-o-ensaio-XXX
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:40 min**  
**Ocorrência**No módulo **SIGAQIP - Inspeção de Processos**, ao confirmar a inspeção do resultado na rotina **QIPA215 - Resultados** é exibida a mensagem **Existe(m) ensaio(s) obrigatório(s) cuja medição não foi apontada, para que seja possível informar o laudo do Laboratório, favor apontar medições para o ensaio: XXX**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Causa**A mensagem é exibida em duas situações:  
1. Quando o ensaio está definido como obrigatório na especificação do produto, e durante a inspeção, não foram informadas as medições deste ensaio ou;  
2. Quando o ensaio está definido como obrigatório na especificação do produto, e durante a inspeção, a medição foi informada, mas o registro foi deletado pelo usuário.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se está correto o ensaio estar cadastrado como obrigatório. Esta validação é realizada na rotina **QIPA010 - Especificação do Produto** onde o campo **Ensaio Obrig** para o ensaio em questão, está preenchido como **Sim**;  
2. Se estiver correta a parametrização do ensaio, será necessário informar a medição para o ensaio em questão durante a inspeção do produto.  
  
**Importante**  
Quando o conteúdo do parâmetro **MV\_QPVMDEL - Define se irá VALIDAR o registro deletado para o ensaio obrigatório em medição do Laudo** for igual à **1-Sim**, será validado se a medição informada para ensaio obrigatório está deletada.  
Para que não seja validado medição deletada para ensaio obrigatório, o conteúdo do parâmetro **MV\_QPVMDEL** deve ser alterado para **2-Não**.
