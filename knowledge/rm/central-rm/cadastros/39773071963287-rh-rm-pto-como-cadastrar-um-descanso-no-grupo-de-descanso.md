---
article_id: 39773071963287
category: Cadastros
content_hash: 8fd818e48eb82a40be9d956e07c4c2ae1553a0b34f82de91fe2767537c1925fc
fetched_at: '2026-06-28T22:46:28.424378+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Como cadastrar um descanso no grupo de descanso
type: support-article
updated_at: '2026-04-15T18:28:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39773071963287-RH-RM-PTO-Como-cadastrar-um-descanso-no-grupo-de-descanso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39773100070935) **Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Como cadastrar um descanso no grupo de descanso ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**  
Para cadastrar um descanso a um grupo de descanso , realize os seguintes passos:  
  
1. No módulo **Automação de Ponto,** acesse a aba **Cadastros,** menu **Grupo de Descanso,** sera aberta a tela com os grupos que já foram cadastrados, selecione o grupo de descanso desejado, acesse **Anexos** e selecione a opção **Descansos**.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/39773100071575)**  
  
2. O anexo será aberta a tela para cadastrar os descansos , clique em Incluir, que será aberta uma nova janela Descanso: <novo> , preeencha os campos:

**Data** : Informe neste campo uma data maior que a data do início do período atual.

**Hora Início** / **Hora Fim** : Estes campos são utilizados para informar o intervalo do dia que será considerado como descanso para o funcionário. Podemos cadastrar um descanso no intervalo de 00:00 às 24:00, por exemplo.  
  
**Considera descanso como:** Deverá selecionar uma das 6 opções de parametrização  e salve o registro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39773071951383)  
  
**Importante**

Segue orientação  do comportamento de cada opção de como o descanso pode ser considerado:

**Hora início até o fim do intervalo planejado:** Marcando este parâmetro, será considerado como extra de descanso o intervalo executado do início do descanso até o fim do intervalo planejado.  
  
**Extra apenas na interseção com o descanso:** Marcando este parâmetro, será considerado como extra de descanso a interseção entre o descaso cadastrado e o intervalo planejado  
  
**Toda jornada em interseção com o descanso:** Marcando este parâmetro, será considerado como extra de descanso toda a jornada que fizer interseção com o descanso cadastrado.  
  
**Considera o intervalo planejado ao fazer interseção com o Descanso:** Marcando este parâmetro, será considerado como extra de descanso intervalo de descanso que fizer interseção com o intervalo planejado.  
  
**Considera como descanso todo o intervalo planejado que iniciou no próprio descanso:** Marcando esse parâmetro, será considerado como extra de descanso todo o intervalo planejado iniciado no dia do descanso cadastrado.  
  
**Considera como descanso todo o intervalo planejado que terminou no próprio descanso:** Marcando esse parâmetro, será considerado como extra de descanso todo o intervalo planejado que terminou no dia do descanso cadastrado.

**Saiba Mais**  
Para mais  informações sobre o grupo de descanso, acesse as documentações:  
[RH - RM - PTO - Cadastrar grupo de descanso para os funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015393071-RH-RM-PTO-Cadastrar-grupo-de-descanso-para-os-funcion%C3%A1rios)  
[Grupos de Descanso - Anexos](https://tdn.totvs.com/display/public/LRM/Grupos+de+Descanso+-+Anexos)
