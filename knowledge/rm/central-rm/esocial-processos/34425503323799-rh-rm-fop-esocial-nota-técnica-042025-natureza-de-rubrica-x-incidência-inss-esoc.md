---
article_id: 34425503323799
category: esocial - Processos
content_hash: ec2816bbc15fe9a1439622600bb2825bd381fd300804c4d2b715ee184c5922a4
fetched_at: '2026-06-28T22:47:08.408546+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: RH - RM - FOP - eSocial - Nota Técnica 04/2025 - Natureza de Rubrica X Incidência
  INSS eSocial (Leiaute S-1.3)
type: support-article
updated_at: '2026-04-08T20:46:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34425503323799-RH-RM-FOP-eSocial-Nota-T%C3%A9cnica-04-2025-Natureza-de-Rubrica-X-Incid%C3%AAncia-INSS-eSocial-Leiaute-S-1-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34425545908503) Tempo aproximado para leitura: **00:04:00 min**  
  
**Ocorrência**  
Foi publicada a Nota Técnica S-1.3 nº 04/2025, que traz uma nova regra de validação para os eventos remuneratórios do eSocial (S-2299, S-2399 e S-1200). A partir de 29/08/2025, verbas com incidência de INSS igual a 15 ou 16 (exclusiva do trabalhador) serão validadas com base na Natureza de Rubrica, ou seja, será necessário que a Natureza de Rubrica associada à verba permita esse tipo de incidência, conforme definido na [Tabela 03 - Natureza das Rubricas da Folha de Pagamento](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-04-2025/tabelas.html#03) do eSocial.  
Caso essa compatibilidade não seja respeitada, os eventos serão rejeitados pelo ambiente nacional do eSocial.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Versões de mercado.  
  
**Causa**  
A partir de 29/08/2025, as verbas/eventos com incidência tributária para previdência Social (INSS) que estiverem classificadas como:

**15 – Exclusiva do segurado – Mensal;**  
**16 – Exclusiva do segurado – 13º salário;**  
  
Só serão aceitas se a **Natureza da Rubrica** estiver configurada para permitir essa classificação.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o menu **RH | Folha de Pagamento | Administração de Pessoal | Eventos | Eventos.**  
2. Crie um filtro utilizando os campos **INCINSSEXCLUSIVASEGURADO** ou **INCINSSEXCLUSIVASEGURADO13**, conforme demonstrado abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34432345748631)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34432345751063)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34432345752087)![](https://tdn.totvs.com/download/attachments/979033796/image-2025-8-21_18-12-35.png?version=1&modificationDate=1755811605913&api=v2)

3. O filtro irá gerar todos os eventos que contenham verbas/eventos com incidência marcada como exclusiva do segurado.

![](https://tdn.totvs.com/download/attachments/979033796/image-2025-8-21_18-23-18.png?version=1&modificationDate=1755811605760&api=v2)

4. Verifique a coluna Natureza da Rubrica (eSocial).

![](https://tdn.totvs.com/download/attachments/979033796/image-2025-8-21_18-24-50.png?version=1&modificationDate=1755811605667&api=v2)

5. Verificação na Tabela do eSocial.  
Acesse a tabela do eSocial disponível em: [Tabela 03 - Natureza das Rubricas da Folha de Pagamento](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-04-2025/tabelas.html#03)  
Confira se o campo `{codIncCP}` no evento **S-1010** está marcado como **'Sim'** para verbas com incidência **15 (exclusiva do segurado – mensal)** ou **16 (exclusiva do segurado – 13° salário)**, na Natureza da rubrica correspondente às verbas filtradas.  
  
6 **-**Se a tag `{codIncCP}` estiver igual a **'Sim'** nenhuma ação adicional é necessária. A verba está em conformidade com o leiaute do eSocial.  
  
7 **-** Se a tag `{codIncCP}` estiver igual a **'Não'** e se a verba for utilizada em algum evento remuneratório, a partir de **29/08/2025**, o evento será rejeitado pelo sistema do Governo. Nessa situação, recomenda-se avaliar a melhor estratégia, possivelmente com apoio do setor jurídico da empresa, para decidir o encaminhamento da verba ou ajuste necessário.  
  
**Importante**  
Após a correção da verba, o evento S-1010 deve ser enviado antes dos eventos remuneratórios (S-1200, S-2299, S-2399) para que as alterações sejam reconhecidas corretamente pelo eSocial.

Verifique também se o campo ***iniValid*** está com data igual ou anterior ao período de apuração/data de desligamento. Se necessário, ajuste o campo **Competência** do gatilho do S-1010 para correta geração do início da validade:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34452650258711)

**Saiba Mais**  
Para mais informações, acesse:

* [Leiaute S-1.3 - Nota Técnica 04/2025 - Natureza de Rubrica X Incidência INSS eSocial](https://tdn.totvs.com/pages/viewpage.action?pageId=979033796)
* [eSocial: Fique atento às novas regras da NT 04/2025](https://informa.totvs.com/rh/esocial-fique-atento-as-novas-regras-da-nt-04-2025/)
