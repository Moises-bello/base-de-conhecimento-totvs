---
article_id: 35032695025815
category: Financeiro - Conciliador Backoffice
content_hash: 5cc700c96a8277b5c67b47ce61620d34bd4ecfb9ebc0e8d674f17db0d6338cad
fetched_at: '2026-06-28T22:37:47.211092+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Opções 0023
  e 0024 dos menus do Conciliador Backoffice não estão sendo exibidos
type: support-article
updated_at: '2026-03-26T16:45:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35032695025815-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Op%C3%A7%C3%B5es-0023-e-0024-dos-menus-do-Conciliador-Backoffice-n%C3%A3o-est%C3%A3o-sendo-exibidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35032695003543) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Após a implantação do conciliador, ao acessar a rotina CTBA940, os menus 0023 – Conciliação Automática e 0024 – Conciliação Manual não estão sendo exibidos.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro -  A partir da versão 12.1.2210  
  
**Solução**

Isso ocorre devido à ausência de campos na estrutura das tabelas utilizadas pelo Conciliador durante o processamento do **UPDDISTR**.

Atualmente, o **UPDDISTR** é o único processo disponível para atualizar os campos necessários ao funcionamento das conciliações **0023 – Conciliação Automática** e **0024 – Conciliação Manual**.

⚠️ **Observação:** É fundamental utilizar a versão mais recente do Backoffice para coleta do **SDF** e, em seguida, executar o **UPDDISTR** em modo exclusivo, garantindo que todos os campos sejam corretamente criados e reconhecidos pelo sistema.

Campos validados para a criação dos processos 0023 e 0024:

1. IG\_DTEXTR
2. IG\_DOCEXT
3. IG\_VLREXT
4. IG\_HISTEXT
5. IG\_CARTER
6. IG\_BCOEXT
7. IG\_AGEEXT
8. IG\_CONEXT
9. IG\_FILIAL
10. FK5\_FILORI
11. FK5\_DTDISP
12. FK5\_DATA
13. FK5\_MOEDA
14. FK5\_VALOR
15. FK5\_NATURE
16. FK5\_BANCO
17. FK5\_AGENCI
18. FK5\_CONTA
19. FK5\_NUMCH
20. FK5\_DOC
21. FK5\_RECPAG
22. FK5\_BENEF

**Em especial o campo FK5\_BENEF, criado recentemente em nosso dicionário.**

Caso haja qualquer campo faltante no ambiente, o UPDDISTR não alimentara a QLB com os processos 0024 e 0023.

Caso esteja tudo OK, o acesso ao CTBA940 deve demonstrar os novo processos criados.

![unnamed.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39315460216727)

A criação dos processos na **QLB** ocorre no momento da abertura da rotina **CTBA940**.

* Se o sistema identificar campos ausentes na estrutura, os processos não serão gerados durante a abertura do Conciliador.
* Caso a estrutura esteja completa, ao acessar o **CTBA940**, o sistema exibirá automaticamente os processos recém-criados.

**Saiba mais**

[Financeiro - Conciliador Backoffice](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30769054561431-Financeiro-Conciliador-Backoffice)
