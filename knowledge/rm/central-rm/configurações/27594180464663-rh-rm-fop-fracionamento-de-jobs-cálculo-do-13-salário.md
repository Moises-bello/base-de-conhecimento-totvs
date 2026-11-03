---
article_id: 27594180464663
category: Configurações
content_hash: 3ddd98090aa81c581ba5d7a2413b4b70061d50b8452be57f291de75f50a5f9f8
fetched_at: '2026-06-28T22:46:49.453781+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Fracionamento de Jobs - Cálculo do 13° Salário
type: support-article
updated_at: '2025-08-01T15:23:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27594180464663-RH-RM-FOP-Fracionamento-de-Jobs-C%C3%A1lculo-do-13-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27594180458903) Tempo aproximado para leitura: **00:01:14 min** **Dúvida**Como realizar o Fracionamento de Jobs para a rotina Cálculo 13°. Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento

a partir dos patchs/Release abaixo:

12.1.2402.224  
12.1.2406.151  
12.1.2410

**Solução**Foi implementado o recurso de Fracionamento de JOBs para o processo de Cálculo de 13º Salário no módulo TOTVS Folha de Pagamento.

Para Habilitar o recurso é necessário:

* O Host ou Service Host estar configurado com JobServer3Camandas = True
* Cadastrar a classe de processo FopLancamento13FracionadoProcess em Ambiente | Processos | Segurança de Jobs Fracionáveis, para o perfil que terá acesso  
  Com esta implementação podemos chegar em até 70% de ganho na performance do cálculo de 13º Salário.

Para obter acesso à configuração completa do Fracionamento de Jobs para o Cálculo do 13° salário, por favor, **[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=865405263)**.  
  
**Saiba mais**[RH - RM - FOP - Habilitar Fracionamento de Jobs](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9912971569559-RH-RM-FOP-Habilitar-Fracionamento-de-Jobs)
