---
article_id: 27059009029399
category: SIGAEST - INTEGRAÇÕES
content_hash: 270f715a1f6c9b93408481913640bc1a607988dac7ea3ec9f3ed641d92e7531f
fetched_at: '2026-06-28T22:38:46.209284+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - INTEGRAÇÃO Carga inicial
  não respeita filial logada para tabela compartilhadas.
type: support-article
updated_at: '2025-03-12T12:25:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27059009029399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-INTEGRA%C3%87%C3%83O-Carga-inicial-n%C3%A3o-respeita-filial-logada-para-tabela-compartilhadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27058997574167) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Via carga inicial quando tenho uma tabela compartilhada no Protheus, esta sendo enviado informações apenas para a primeira filial.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Causa**  
Isso ocorre pois alguns sistemas se utilizam da Tag "Banchid" para efetuar a integração, como por exemplo o sistema Quirions.

**Solução**

Conforme analisado internamente junto ao time de produto, a tag "BranchId" quando efetuado a integração pela alteração via rotina, será preenchida com a filial posicionada no momento.  
  
Porém quando realizado via carga inicial no configurador, durante o sincronismo a tag "BranchId" será preenchia com a primeira filial ativa disponível no sistema, sendo assim, a filial que vc logou para iniciar o sincronismo não interfere.

O comportamento do sistema vai trazer apenas da primeira, pois no conceito de tabela compartilhada, como os dados são os mesmos, não há a necessidade do enviado de todas as filiais de maneira separada.  
  
Dado isso para ter o comportamento desse, se faz necessário o mesmo tipo de compartilhamento de tabela em ambos sistemas.  
  
  
**Observação:** Carga inicial é uma funcionalidado do Framework, sendo assim, ela tem um comportamento diferente da rotina do estoque.

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Integrações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
