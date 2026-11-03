---
article_id: 1500003304181
category: Inspeção de Processos (SIGAQIP)
content_hash: c87878bad225c9eadeb0742520799c1d1c101aca6cf41371d6fe8ca584ece65a
fetched_at: '2026-06-28T22:42:25.824313+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Legendas do QIPA215
type: support-article
updated_at: '2021-08-10T14:37:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003304181-Manufatura-Linha-Protheus-SIGAQIP-Legendas-do-QIPA215
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:45 min**  
**Dúvida**Quais as condições que definem a cor da legenda do resultado da inspeção na rotina **QIPA215 - Cadastro de Resultados**?  
  
**Ambiente**Totvs Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**A legenda é definida com base nas informações da inspeção realizada, e sua informação é registrada no campo **QPK\_SITOP - Sit. da OP**, sendo:

* **Cinza**: **Ord. Prod. sem medições cadastradas** - Enquanto o resultado não tiver medições cadastradas e laudo informado, o campo **QPK\_SITOP** estará em **branco**.
* **Azul**: **Laudo Pendente** - Tem medições para os ensaios, laudo do laboratório informado, laudo da operação informado, mas não tem laudo geral informado ou quando. Neste caso, o campo ficará com conteúdo igual à **7**.
* **Verde**: **Aprovado** - Tem medições para os ensaios, laudo do laboratório informado, laudo da operação informado, tem laudo geral informado como **A - Aprovado**. Neste caso, o campo ficará com conteúdo igual à **2**.
* **Vermelho**: **Reprovado** - Tem medições para os ensaios, laudo do laboratório informado, laudo da operação informado, tem laudo geral informado como **E - Rejeitado Totalmente**. Neste caso, o campo ficará com conteúdo igual à **3**.
* **Amarelo**: **Laudo com Liberação Urgente** - Tem medições para os ensaios, laudo do laboratório informado, laudo da operação informado, tem laudo geral informado como **U - Liberação Urgente**. Neste caso, o campo ficará com conteúdo igual à **4**.
* **Laranja**: **Laudo Aprovado Condicionalmente** - Tem medições para os ensaios, laudo do laboratório informado, laudo da operação informado, tem laudo geral informado como **B - Aceito com Desvio Simples**, **C - Aceito com Desvio Grave** ou **D - Com Seleção pelo Produto**. Neste caso, o campo ficará com conteúdo igual à **5**.
