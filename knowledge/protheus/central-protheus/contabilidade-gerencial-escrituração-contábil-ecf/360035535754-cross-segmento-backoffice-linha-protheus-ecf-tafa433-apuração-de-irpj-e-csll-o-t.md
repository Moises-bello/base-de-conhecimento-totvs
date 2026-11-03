---
article_id: 360035535754
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 014cf602b0a7ce474bcc54cacfdbb68b57b4db095fcdccfd63b6f22d29a5b76e
fetched_at: '2026-06-28T22:40:47.638180+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ECF :TAFA433 apuração  de IRPJ
  e CSLL o TAF  saldo "Imposto Devido Meses Anteriores"  cumulativo '
type: support-article
updated_at: '2023-09-15T16:01:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035535754-Cross-Segmento-Backoffice-Linha-Protheus-ECF-TAFA433-apura%C3%A7%C3%A3o-de-IRPJ-e-CSLL-o-TAF-saldo-Imposto-Devido-Meses-Anteriores-cumulativo
---

**Dúvida**

Ao realizar a apuração dos  IRPJ e CSLL por balancete o TAF permite gerar o saldo "Imposto Devido Meses Anteriores" de forma cumulativa ?

Como o campo "Imp. devido Meses ant" se comporta

* é alimentado automaticamente?
* ele acumula ?
* existe uma configuração especifica para que ele seja alimentado?

**Ambiente**Cross Segmento - Backoffice Linha Protheus – TAF – A partir da versão 11.80  
  
  
**Solução**

Para que o saldo  seja levado para o próximo mês (acumulado) é necessário fazer a geração da guia através da rotina TAFA444 e após isso fazer a baixa da guia através da rotina [Documento de Arrecadação - TAFA027](http://tdn.totvs.com.br/pages/viewpage.action?pageId=271166621)

 

Caso o mês de janeiro já tenha sido encerrado, será necessário fazer a reabertura do período e após isso gerar as guias.

Após esse procedimento o saldo irá para o próximo período e será visualizado no momento da simulação da apuração e considerado no cálculo do tributo do mês que está sendo encerrado.

Imp.meses Ant ,

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046298574)

Imp. devido meses ant.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17552064600727)

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=244428177>

**Saiba mais**

**[MP-SIGACTB - ECF Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)**

**[MP-SIGACTB - ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)**

[MP-SIGACTB - ECF Tabelas Relacionadas a Apuração IRPJ CSLL no TAF (Lalur)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034815894-MP-SIGACTB-ECF-Tabelas-Relacionadas-a-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-Lalur-?source=search)

[MP\_SIGACTB LALUR/LACS: CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)

[MP\_SIGACTB :TAF-Controle do PAT na Parte B do LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037249374-MP-SIGACTB-TAF-Controle-do-PAT-na-Parte-B-do-LALUR?source=search)

Rotina de cada bloco :

[Obrigação ECF - Escrituração Contábil Fiscal](http://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoP-LucroPresumido)

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

[Apuração do IRPJ e da CSLL(LALUR e LACS)](http://tdn.totvs.com/pages/releaseview.action?pageId=274832267)

[MP-SIGACTB - ECF Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)

[MP - Cálculo de CSLL e IRPJ - Empresa Lucro Presumido - Trimestral - SIGACTB X SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133373-MP-C%C3%A1lculo-de-CSLL-e-IRPJ-Empresa-Lucro-Presumido-Trimestral-SIGACTB-X-SIGATAF?source=search)

[MP - SIGACTB - ECF TAFA433 - Compensação do Prejuízo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035081174-MP-SIGACTB-ECF-TAFA433-Compensa%C3%A7%C3%A3o-do-Preju%C3%ADzo?source=search)
