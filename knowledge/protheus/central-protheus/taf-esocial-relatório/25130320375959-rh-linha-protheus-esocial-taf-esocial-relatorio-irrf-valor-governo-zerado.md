---
article_id: 25130320375959
category: TAF - eSocial - Relatório
content_hash: 53e098d51b0ba696e5efcc7510d092c55b2d32fa97dd8c23bf06ea7bd51ebf21
fetched_at: '2026-06-28T22:45:19.947696+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF eSocial - Relatorio IRRF - Valor governo
  zerado
type: support-article
updated_at: '2026-06-22T21:42:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25130320375959-RH-Linha-Protheus-eSocial-TAF-eSocial-Relatorio-IRRF-Valor-governo-zerado
---

**Dúvida**  
Valor governo sem retorno IRRF, como ajustar?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25130348795927)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório IRRF- (TAFA552A)- Todas as versões  
  
**Solução**

**1.** Valide se o S-1210 foi enviado com sucesso ao governo.

**2.** Verifique se o XML retorno do ret S-1210 consta o retorno do totalizador S-5002.

Caminho da rotina: S-1210 Atualizações | Eventos Esocial | Periódicos | Pgto Rend Trab.

Gerar XML RET

[RH - Linha Protheus - TAF - eSocial - Configuração - Como gerar XML de retorno dos eventos no TAF, e o XML do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046869313-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-gerar-XML-de-retorno-dos-eventos-no-TAF-e-o-XML-do-TAF)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25130320362391)

**4.** Caso o XML de retorno consta o valor no S-5002, será necessário seguir processo abaixo

Reavalie os totalizadores.

[RH (Linha Protheus) - eSocial - TAF eSocial - Reavaliar Totalizadores - Painel E-social (TAFA552A)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37204448646935-RH-Linha-Protheus-eSocial-TAF-eSocial-Reavaliar-Totalizadores-Painel-E-social-TAFA552A)

Para reavaliar os totalizadores de maneira adequada, é essencial que você inclua um período adicional de dois meses ao executar a rotina.

Caso o problema persista, é recomendável atualizar o seu ambiente para a versão mais recente disponível.

[RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TAF-E-social-Expedi%C3%A7%C3%A3o-Cont%C3%ADnua)

Ao finalizar atualização, reavalie novamente os totalizadores.

Após realizar a validação de todos os processos mencionados anteriormente, caso ainda não tenha obtido o retorno esperado, enviar as evidências para equipe de suporte TAF.

* Print da divergência.
* Enviar os xml conforme orientado acima.
* Print/vídeo de como reavaliou os totalizadores.
* tela de diagnostico. [RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-Como-acessar-a-tela-de-diagn%C3%B3stico-no-TAF#:~:text=Para%20acessar%20a%20tela%20de,TAF%20%E2%9E%A4%20Diagn%C3%B3stico.)
