---
article_id: 360051753333
category: RH - Fechamento Período
content_hash: 0b4821b45af3cd2e1340ec807f59bdee65aac6f0224af1e38151e4de1b30f88b
fetched_at: '2026-06-28T22:43:24.500261+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Rotina de fechamento apresenta roteiros com a legenda
  vermelha
type: support-article
updated_at: '2025-04-16T11:59:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051753333-RH-Linha-Protheus-GPE-Rotina-de-fechamento-apresenta-roteiros-com-a-legenda-vermelha
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22408242181271)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Por que a rotina de fechamento apresenta roteiros com a legenda vermelha e não permite fechar o roteiro?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 12.  
  
**Solução**Para fechamento dos roteiros, BEN, FER, PLA, RES, VRF e VTR, os mesmos devem ser **integrados** primeiramente, assim passam da legenda vermelha para a verde.  
  
**Exemplo**  
A rotina fechamento (GPEM120) apresenta os roteiros sem a integração com legenda vermelha, sendo eles: BEN, FER, PLA, RES, VAL, VEX, VRF e VTR

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22408252046359)

**Após** integração dos roteiros BEN, FER, PLA, RES, VAL, VRF e VTR o Sistema apresenta **legenda verde,** permitindo selecioná-los para execução do Fechamento.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22408252053399)

Para que o roteiro VEX seja apresentado na tela de integrações e entrar para Folha, é necessário ajustar sua configuração em **Atualizações> Definições de Cálculo > Roteiros de Cálculo.** Veja [artigo relacionado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018301831-RH-Linha-Protheus-GPE-Como-e-para-que-pode-ser-utilizado-o-Roteiro-de-C%C3%A1lculo-VEX-Valores-Extras?source=search).

É possível ver a **descrição da legenda** clicando duas vezes em cima do ícone da legenda. Vermelho = **Falta Integrar** e Verde = **Apto para Fechamento**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22408242210711)

Como os roteiros 131, 132, ADI, FOL e PLR **não são integrados**, os mesmos **sempre** apresentam legenda **verde** na rotina fechamento período.

**Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Melhoria de performance no fechamento mensal com MV\_CALCTHD ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050884333-RH-Linha-Protheus-GPE-Melhoria-de-performance-no-fechamento-mensal-com-MV-CALCTHD-ativo)

[RH - Linha Protheus - GPE - Fechamento de Período Gera Erro - array out of bounds ( X of X ) on GP120FECFER(GPEM120.PRX)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046293074-RH-Linha-Protheus-GPE-Fechamento-de-Per%C3%ADodo-Gera-Erro-array-out-of-bounds-X-of-X-on-GP120FECFER-GPEM120-PRX)

[RH - Linha Protheus - GPE - Implementação do Multi Thread no fechamento da folha para melhora no desempenho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034908554-RH-Linha-Protheus-GPE-Implementa%C3%A7%C3%A3o-do-Multi-Thread-no-fechamento-da-folha-para-melhora-no-desempenho)
