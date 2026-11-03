---
article_id: 360020662472
category: RH - Integração de Titulo
content_hash: 4798298b68c047af85628b8f1982874ed2386c39c56159571a5282d0d70a61fc
fetched_at: '2026-06-28T22:43:36.144113+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - A geração de títulos de 13º, não está funcionando
  após a migração para versão 12
type: support-article
updated_at: '2025-08-13T17:53:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020662472-RH-Linha-Protheus-GPE-A-gera%C3%A7%C3%A3o-de-t%C3%ADtulos-de-13%C2%BA-n%C3%A3o-est%C3%A1-funcionando-ap%C3%B3s-a-migra%C3%A7%C3%A3o-para-vers%C3%A3o-12
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34149042612759) Tempo aproximado para leitura: **00:02:00 min**  
  
Ocorrência**No módulo **GPE**, ao tentar realizar (o processo ou a rotina) **Geração de Títulos (GPEM650),**não é apresentado nenhum erro , porém o título não é gerado.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas – 12.

**Causa**Na versão 11, a tabela para Definição de títulos era SRI. Na versão 12, com a criação dos roteiros, o cálculo de 13º, enquanto o movimento estiver aberto, será apresentado na tabela SRC e caso o movimento esteja fechado, será apresentado na tabela SRD. (idem folha de pagamento).  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse: Miscelânea -> Títulos -> Definição:  
- Abrir a opção de definição da tabela (canto inferior direito): **Definir Título**.

![131218_03.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360017441652)

2. No campo Arquivo, clicar na opção de alteração da tabela ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017442052);

![131218_01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360017441512)

3. Alterar de acordo com o movimento de cálculo do 13º salário.  
**Tabela SRC -** Movimento de Períodos : Caso o movimento de cálculo de 13º esteja aberto.  
**Tabela SRD -** Histórico de Movimentos: Caso o movimento de cálculo de 13º esteja fechado.

![131218_02.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360017327051)  
  
**Saiba Mais:**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
