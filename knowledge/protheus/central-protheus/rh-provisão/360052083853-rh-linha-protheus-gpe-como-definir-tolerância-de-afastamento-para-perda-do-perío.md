---
article_id: 360052083853
category: RH - Provisão
content_hash: 1440d9789da9cb79c1f45eefcc452921c3405dbb44ac050efc659eeaa33fc3db
fetched_at: '2026-06-28T22:43:55.796537+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Definir Tolerância de Afastamento para Perda
  do Período Aquisitivo na Provisão
type: support-article
updated_at: '2022-09-16T17:46:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052083853-RH-Linha-Protheus-GPE-Como-Definir-Toler%C3%A2ncia-de-Afastamento-para-Perda-do-Per%C3%ADodo-Aquisitivo-na-Provis%C3%A3o
---

**Dúvida**Como Definir Tolerância de Afastamento para Perda do Período Aquisitivo na Provisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
Quando o funcionário entrega um atestado de X dias de afastamento, o sistema irá buscar dentro do cadastro de ausência, campo "Dias Afastamento Férias" (RCM\_DIASFE) quantos dias serão toleráveis até que a contagem para perca dos avos seja iniciada.  
Portanto, ao Cadastrar um novo tipo de ausência, é necessário avaliar o preenchimento deste campo antes do Lançamento da Ausência do funcionário.  
**Exemplo:** Considerando um tipo de ausência padrão na qual o direito as férias é perdido após 180 dias. Se no campo RCM\_DIASFE  for informado 100 dias, o funcionário perderá o direito as férias apenas se ficar afastado durante 280 dias, pois os 100 primeiros entram na tolerância e serão ignorados, tanto para o Período Aquisitivo do Funcionário, quanto para o Cálculo das Provisões de Férias.  
  
Para mais informações acesse: <https://tdn.totvs.com/pages/releaseview.action?pageId=360455805>
