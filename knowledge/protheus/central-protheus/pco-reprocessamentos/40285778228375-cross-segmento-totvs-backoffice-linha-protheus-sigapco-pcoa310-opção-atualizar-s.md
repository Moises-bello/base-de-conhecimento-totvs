---
article_id: 40285778228375
category: PCO - Reprocessamentos
content_hash: 41357723bc21252fe2143c446c0adf666135f67d21dae4de014cd6d811378df8
fetched_at: '2026-06-28T22:37:07.032639+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPCO - PCOA310 - Opção
  "Atualizar Saldos" desabilitada no reprocessamento
type: support-article
updated_at: '2026-05-07T10:52:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40285778228375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAPCO-PCOA310-Op%C3%A7%C3%A3o-Atualizar-Saldos-desabilitada-no-reprocessamento
---

A opção "Atualizar Saldos ?" no reprocessamento de lançamentos (PCOA310.PRW) fica desabilitada quando o parâmetro MV\_PCOTHRE está configurado com valor maior que 1, pois o sistema usa multithread. Para habilitar, altere MV\_PCOTHRE para 1 no módulo Configurador (SIGACFG) e salve. Após isso, a opção estará liberada para seleção.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40285778217751) Tempo aproximado para leitura: 10 min  
  
**Dúvida**  
A opção "Atualizar Saldos ?" no reprocessamento de lançamentos (PCOA310) passou a ficar desabilitada. Existe algum parâmetro que a habilite para seleção?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40285719071127)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPCO - A partir da release 12

**Solução**  
A pergunta de atualização de saldos fica bloqueada para alteração quando o parâmetro MV\_PCOTHRE está configurado com um valor maior que 1.

Isso ocorre porque, sob essa condição, o sistema realiza o reprocessamento utilizando o recurso de multithread, impedindo a seleção manual.

**Para que a pergunta fique habilitada novamente, realize os passos:**

1. Acesse o módulo Configurador (SIGACFG) ou a rotina de Parâmetros do sistema.
2. Pesquise pelo parâmetro MV\_PCOTHRE.
3. Verifique o valor preenchido no conteúdo do parâmetro.
4. Caso o conteúdo seja maior que 1, altere o valor para 1.
5. Salve as alterações e acesse novamente a rotina de reprocessamento de lançamentos (PCOA310).
6. A opção "Atualizar Saldos ?" estará liberada para alteração e seleção.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40285778218775)
