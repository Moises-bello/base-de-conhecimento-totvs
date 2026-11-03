---
content_hash: c2f905c344ebc867a54e238fb55054498ca66fb3d9dbd252e84eb186dd27abae
fetched_at: '2026-06-29T00:12:15.443455+00:00'
page_id: '979033796'
product: rm
source: tdn-rm
title: Leiaute S-1.3 - Nota Técnica 04/2025 - Natureza de Rubrica X Incidência INSS
  eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=979033796
version: 14
---

|  |  |
| --- | --- |
| **Produto:** | Linha RM |
| **Ocorrência:** | **Natureza de Rubrica X Incidência INSS eSocial - Nota Técnica 04/2025 - Leiaute S-1.3**  Foi publicada a Nota Técnica S-1.3 nº 04/2025, que traz uma nova regra de validação para os eventos remuneratórios do eSocial (S-2299, S-2399 e S-1200).  A partir de 29/08/2025, verbas com incidência de INSS igual a 15 ou 16 (exclusiva do trabalhador) serão validadas com base na Natureza de Rubrica, ou seja, será necessário que a Natureza de Rubrica associada à verba permita esse tipo de incidência, conforme definido na Tabela 03 do eSocial.  Caso essa compatibilidade não seja respeitada, os eventos serão rejeitados pelo ambiente nacional do eSocial.  Para mais informações, acesse a Tabela 03 no portal oficial do eSocial: 🔗 <https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-04-2025-rev.pdf> |
| **Passo a passo:** | A partir de 29/08/2025, as verbas/eventos com incidência tributária para previdência Social (INSS) que estiverem classificadas como:   * + **15 – Exclusiva do segurado – Mensal**, ou   + **16 – Exclusiva do segurado – 13º salário**, só serão aceitas se a **Natureza da Rubrica** estiver configurada para permitir essa classificação.    Como devo conferir essas informações no sistema? **1 -** Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Eventos | Eventos.  **2 -** Crie um filtro utilizando os campos INCINSSEXCLUSIVASEGURADO ou INCINSSEXCLUSIVASEGURADO13, conforme demonstrado abaixo:              **3 -** O filtro irá gerar todos os eventos que contenham verbas/eventos com incidência marcada como exclusiva do segurado.      **4 -**  Verifique a coluna Natureza da Rubrica (eSocial).       **5 -** Verificação na Tabela do eSocial.  Acesse a tabela do eSocial disponível em: [Link](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-04-2025/tabelas.html#03) Confira se o campo `{codIncCP}` no evento **S-1010** está marcado como **SIM** para verbas com incidência **15 (exclusiva do segurado – mensal)** ou **16 (exclusiva do segurado – 13° salário)**, na Natureza da rubrica correspondente às verbas filtradas.    **6 -** Se a tag `{codIncCP} estiver igual a SIM, n`enhuma ação adicional é necessária. A verba está em conformidade com o leiaute do eSocial.    **7 -** Se a tag `{codIncCP} estiver igual a NÃO e s`e a verba for utilizada em algum evento remuneratório, a partir de 29/08/2025, o evento será rejeitado pelo sistema do Governo. Nessa situação, recomenda-se avaliar a melhor estratégia, possivelmente com apoio do setor jurídico da empresa, para decidir o encaminhamento da verba ou ajuste necessário. |
| **IMPORTANTE** | Após a correção da verba, o evento **S-1010** deve ser **enviado antes** dos eventos remuneratórios (**S-1200, S-2299, S-2399**) para que as alterações sejam reconhecidas corretamente pelo eSocial.  Verifique também se a tag *<***iniValid>**está com data igual ou anterior ao período de apuração/data de desligamento.  Se necessário, ajuste o campo **Competência** no gatilho do evento **S-1010**, garantindo a correta geração da data de início de validade. |
