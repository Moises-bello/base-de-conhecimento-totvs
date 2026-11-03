---
article_id: 34788196004631
category: esocial - Periódicos
content_hash: 9ca6740204609edc7aa01e0d24111f54ef9033b22755929994fe672b3799f9e0
fetched_at: '2026-06-28T22:47:09.336663+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro código 1984: Rubrica ''XXXX'' invalida. Somente
  pode ser aceita rubrica com o CodIncCP = [15, 16] para as naturezas de rubrica constantes
  da Tabela 3'
type: support-article
updated_at: '2026-03-12T00:04:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34788196004631-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-1984-Rubrica-XXXX-invalida-Somente-pode-ser-aceita-rubrica-com-o-CodIncCP-15-16-para-as-naturezas-de-rubrica-constantes-da-Tabela-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34788195972247) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao enviar XML S-1010 é apresentada a mensagem: **Erro código 1984: Rubrica SALARIO NORMAL invalida. Somente pode ser aceita rubrica com o CodIncCP = [15, 16] para as naturezas de rubrica constantes da Tabela 3 que sejam compativeis com a incidencia exclusiva do empregado.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**  
Foi publicada a Nota Técnica S-1.3 nº 04/2025, que traz uma nova regra de validação para os eventos remuneratórios do eSocial (S-2299, S-2399 e S-1200). A partir de 29/08/2025, **verbas com incidência de INSS igual a 15 ou 16 (exclusiva do trabalhador) serão validadas com base na Natureza de Rubrica**, ou seja, será necessário que a Natureza de Rubrica associada à verba permita esse tipo de incidência, conforme definido na [Tabela 03 - Natureza das Rubricas da Folha de Pagamento](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-04-2025/tabelas.html#03) do eSocial.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a tabela do eSocial disponível em: [Tabela 03 - Natureza das Rubricas da Folha de Pagamento](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-04-2025/tabelas.html#03)  
2. Confira se o campo `{codIncCP}` no evento **S-1010** está marcado como **'Não'** para verbas com incidência **15 (exclusiva do segurado – mensal)** ou **16 (exclusiva do segurado – 13° salário)**, na Natureza da rubrica correspondente ao evento S-1010 com erro.  
3. Se a tag `{codIncCP}` estiver igual a **'Não'** será necessário validar se a natureza de rubrica do evento está correta, caso positivo, validar se a incidência INSS exclusiva do segurado é devida neste evento. Nessa situação, recomenda-se avaliar a melhor estratégia, possivelmente com apoio do setor jurídico da empresa, para decidir o encaminhamento da verba ou ajuste necessário.

**Exemplo**  
No exemplo abaixo, evento com código de cálculo 145 - Atestado Médico está com incidência exclusiva do segurado marcada, e com natureza de rubrica 1050:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34788195974807)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34788176292759)  
  
Dessa forma, ao enviar o S-1010 desse evento, o mesmo irá ser rejeitado, visto que de acordo com o trecho abaixo da Tabela 03 do leiaute de tabelas do eSocial, não é compatível a natureza de rubrica 1050, sendo necessário trocar a natureza de rubrica, ou trocar a incidência de INSS exclusiva do segurado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34788176294167)  
  
**Importante**  
A TOTVS não orienta qual natureza de rubrica deve ser informada nas verbas, ficando tal escolha a cargo da própria empresa. O que podemos orientar é que a natureza esteja condizente com o Anexo I do Layout eSocial utilizado;
