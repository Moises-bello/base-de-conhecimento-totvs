---
article_id: 20322145438999
category: eSocial - Parametrizador
content_hash: 63c93b0e73eea6513e9f57f40a49c71c3e20c478d563048c7d84f46834e62877
fetched_at: '2026-06-28T22:47:06.262433+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar o S-1200: Necessário preencher o parâmetro
  "Evento INSS Férias envelope" e "Evento INSS Férias Próximo Mês envelope"'
type: support-article
updated_at: '2026-04-17T19:32:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20322145438999-RH-RM-FOP-eSocial-Erro-ao-gerar-o-S-1200-Necess%C3%A1rio-preencher-o-par%C3%A2metro-Evento-INSS-F%C3%A9rias-envelope-e-Evento-INSS-F%C3%A9rias-Pr%C3%B3ximo-M%C3%AAs-envelope
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20322145419159) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao gerar evento S-1200 para funcionários que tiveram férias no mês, são exibidos os erros: **Necessário preencher o parâmetro Evento INSS Férias Envelope nos Parâmetros Gerais do eSocial.**  
**Necessário preencher o parâmetro Evento INSS Férias Próximo Mês Envelope nos Parâmetros Gerais do eSocial.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH - (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O erro ocorre pois os campos **Evento INSS Férias Envelope** e **Evento INSS Férias Próximo Mês Envelope** localizados no menu Configurações | Parametrizador | eSocial | Configurações Gerais 6/7 não estão preenchidos.

Essa implementação foi necessária devido às diretrizes estabelecidas pelo leiaute S-1.0, que indicam que os valores relacionados às incidências de IRRF devem ser reportados no recibo de férias.

Na geração do XML do envelope de pagamento, o produto realizará a substituição desse código de cálculo por meio do evento mencionado neste parâmetro.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20322119083927)**

**Solução**  
Para correção dessa ocorrência, siga os passos abaixo:  
      1. Crie dois eventos como **desconto, sem incidência, sem código de cálculo** e insira-os nos campo supracitados; (Este evento deverá ser informado no parametrizador antes de gerar o XML S-1010, para que a incidência seja gerada corretamente)  
      2. Transmita o evento S-1010 das verbas criadas;  
      3. Em seguida, gere novamente o evento S-1200 e transmita ao governo.

**Importante**  
Antes de enviar o S-1200, é necessário enviar o S-1010 das verbas criadas. Para isso, faça a edição dos gatilhos do S-1010 que serão gerados na fila de eventos do eSocial, informe no campo **Competência** um mês e ano igual ou anterior ao período de apuração do S-1200 e transmita os S-1010 para o governo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20322119084823)

A natureza de rubrica dos novos eventos devem ser as mesmas dos devidos eventos de **Código de Cálculo 82(desconto INSS Férias)** e **130(desconto INSS Férias Próximo Mês)**.  
  
**Saiba mais**  
Para maiores informações, acesse:

• [Configurações Gerais 6/7](https://tdn.totvs.com/pages/releaseview.action?pageId=540899121)  
• [S-1200 e S-1210: Recibo de Férias no leiaute S-1.0](https://tdn.totvs.com/pages/viewpage.action?pageId=627729108)  
• [Configurações Gerais 7/7](https://tdn.totvs.com/pages/releaseview.action?pageId=645896860)
