---
article_id: 39133881602071
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: c903b9e346e619820c2436b651ef5cd10094225389a1504982c8d40ac8018b47
fetched_at: '2026-06-28T22:41:55.591129+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Imobilizado (SIGAATF)
  - ATFA036 - Campos obrigatórios não preenchidos na baixa
type: support-article
updated_at: '2026-03-20T19:09:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39133881602071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Ativo-Imobilizado-SIGAATF-ATFA036-Campos-obrigat%C3%B3rios-n%C3%A3o-preenchidos-na-baixa
---

O erro "existem campos obrigatórios não preenchidos" na baixa de ativo imobilizado no TOTVS Protheus ocorre geralmente porque o campo "Filial de Origem" (N3\_FILORIG) está vazio, impedindo o preenchimento do campo interno FN6\_FILORI. Para resolver, deve-se preencher esse campo na ficha do ativo e realizar a baixa em ambiente de homologação para validação.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39133870815639) Tempo aproximado para leitura: 00:05 min  
  
  
**Dúvida**  
Ao realizar a baixa de um item do ativo imobilizado, o sistema apresenta o erro de "existem campos obrigatórios não preenchidos" impedindo a conclusão do processo, mesmo com todos os campos em tela preenchidos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39133870816151)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Imobilizado (SIGAATF) - A partir da versão 12.  
  
**Solução**  
A mensagem de campo obrigatório na rotina ATFA036 geralmente ocorre quando o bem em questão está com o campo da filial de origem (`N3_FILORIG`) em branco.

Ao faltar essa informação, o sistema não consegue realizar o preenchimento do campo interno `FN6_FILORI` no momento da baixa, acionando o erro de obrigatoriedade e impedindo o prosseguimento da rotina.

Verifique os passos:

* No momento da baixa, verifiquei se todos os campos obrigatórios estão preenchidos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39133881575831)

Obs: Pode-se observar que os campos obrigatórios estão com um asterisco na frente do nome do campo 

* Este help pode ocorrer devido ao campo de filial de origem não estar preenchido na Itens do Ativo (SN3), assim deve-se solicitar ao DBA da empresa ou time de TI que verifique:

  + Verifique o campo `Filial de Origem (N3_FILORIG`).
  + Se o campo estiver em branco, deverá ajustar com o código da filial de origem correspondente.
  + Confirme a alteração e execute a baixa do bem novamente.

**OBS: O processo deve ser realizado em ambiente de homologação, para posterior validação.**

**Saiba mais:**  
[SIGAATF - ATFA036 - BAIXA DE ATIVO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018556171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-BAIXA-DE-ATIVO?source=search)
