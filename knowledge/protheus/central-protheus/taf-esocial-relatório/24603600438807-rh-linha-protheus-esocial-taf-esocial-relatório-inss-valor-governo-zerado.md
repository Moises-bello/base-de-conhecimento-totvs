---
article_id: 24603600438807
category: TAF - eSocial - Relatório
content_hash: 088aa2a405d24682b85a1d4b14c4026db2f5fbdcbfe65bf5b6a2c7790d99bbf5
fetched_at: '2026-06-28T22:45:19.938110+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF eSocial - Relatório INSS - Valor governo
  zerado
type: support-article
updated_at: '2026-04-27T14:02:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24603600438807-RH-Linha-Protheus-eSocial-TAF-eSocial-Relat%C3%B3rio-INSS-Valor-governo-zerado
---

**Dúvida**Valor governo sem retorno INSS, como ajustar?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25453167073175)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório INSS- (TAFA552A)- Todas as versões  
  
**Solução**

**1**. Valide se o S-1200/S-2299 /S-2399 foi enviado com sucesso ao governo.

**2**. Verificar XML retorno do ret S-1200/S-2299 /S-2399 se consta o retorno do totalizador

S-5001.

Caminho das rotinas do menu:

S-1200: Atualizações | Eventos Esocial | Periódicos | Folha de Pagamento  
S-2299: Atualizações | Eventos Esocial | Não-Periódicos | Desligamento  
S-2399: Atualizações | Eventos Esocial | Trabalhador | Término Trabalhador

Acesse a rotina do evento:

Gerar XML RET:

[RH - Linha Protheus - TAF - eSocial - Configuração - Como gerar XML de retorno dos eventos no TAF, e o XML do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046869313-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-gerar-XML-de-retorno-dos-eventos-no-TAF-e-o-XML-do-TAF)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24603600406679)

**3**. Caso o XML de retorno consta o valor no S-5001, será necessário seguir processo abaixo

Reavalie os totalizadores.

RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Reavaliar Totalizadores, como utilizar a rotina.: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/17496282095127](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17496282095127?source=search)

Após realizar a validação de todos os processos mencionados anteriormente, caso ainda não tenha obtido o retorno esperado, enviar as evidências para equipe de suporte TAF.

* Print da divergência.
* Enviar os xml conforme orientado acima.
* Print/vídeo de como reavaliou os totalizadores.
* tela de diagnostico. [RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-Como-acessar-a-tela-de-diagn%C3%B3stico-no-TAF)
